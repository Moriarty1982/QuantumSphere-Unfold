`timescale 1ns/1ps
// Zustandsspeicher nach dem Vorbild von ZFS: inhaltsadressiert, mit Dedup, Schnappschuessen, Klonen,
// laufendem Pruefhash und Spiegel mit Selbstheilung.
//
// Ein Datensatz (RW Bit, Vorgabe 16 Koeffizienten zu 16 Bit + k) liegt in einem von SLOTS Plaetzen, zweifach
// (Spiegel A und B), mit seiner Pruefsumme CRC-32 (wie zlib.crc32 ueber die Bytes, niedrigstes Bit zuerst).
// Namen (NAMES Eintraege) zeigen auf Plaetze; ein Platz zaehlt, wie viele Namen auf ihn zeigen.
//   1 PUT   a        Datensatz rec_in unter Name a ablegen. Gibt es den Inhalt schon (gleiche Pruefsumme und
//                    gleicher Inhalt), zeigt a auf diesen Platz (Dedup, dedup = 1); sonst wird ein freier Platz
//                    belegt. Ein vorher von a belegter Platz wird freigegeben, wenn niemand mehr darauf zeigt.
//                    Copy-on-write: Teilen sich Namen einen Platz, aendert PUT nur den Namen a.
//                    Guard (ok = 0): a ist ein Schnappschuss (nur lesen) oder kein Platz frei.
//   2 GET   a        Datensatz von Name a lesen. Stimmt Spiegel A nicht mit der Pruefsumme, wird B gelesen und
//                    A repariert (und umgekehrt); repaired = 1. Sind beide falsch: ok = 0, bad = 1.
//   3 SNAP  a -> b   Schnappschuss: Name b zeigt auf den Platz von a und ist nur lesbar.
//   4 CLONE a -> b   Klon: Name b zeigt auf den Platz von a und ist schreibbar (eigene Kopie erst beim PUT).
//   5 DEL   a        Name a loeschen; Platz frei, wenn niemand mehr darauf zeigt.
//   6 FLIP  s, bit, Spiegel b[0]   (nur fuer Pruefungen) ein Bit in Spiegel A (0) oder B (1) von Platz s kippen.
// audit: laufender Pruefhash ueber alle erfolgreichen PUT, audit <- crc32(audit (4 Byte) ++ Pruefsumme (4 Byte)).
module qstore #(
    parameter integer RW = 264,
    parameter integer SLOTS = 8,
    parameter integer NAMES = 8,
    parameter integer SB = SLOTS > 1 ? $clog2(SLOTS) : 1,
    parameter integer NB = NAMES > 1 ? $clog2(NAMES) : 1
) (
    input wire clk,
    input wire rst,
    input wire cmd_valid,
    input wire [2:0] cmd,
    input wire [7:0] a,
    input wire [15:0] b,
    input wire [RW-1:0] rec_in,
    output reg rsp_ok,
    output reg [7:0] rsp_slot,
    output reg [31:0] rsp_hash,
    output reg [RW-1:0] rec_out,
    output reg dedup,
    output reg repaired,
    output reg bad,
    output reg [31:0] audit,
    output reg [7:0] used
);
    localparam [2:0] C_PUT = 1, C_GET = 2, C_SNAP = 3, C_CLONE = 4, C_DEL = 5, C_FLIP = 6;

    reg [RW-1:0] mem_a [0:SLOTS-1];
    reg [RW-1:0] mem_b [0:SLOTS-1];
    reg [31:0] shash [0:SLOTS-1];
    reg [7:0] refc [0:SLOTS-1];
    reg nv [0:NAMES-1];
    reg nro [0:NAMES-1];
    reg [SB-1:0] nslot [0:NAMES-1];

    // CRC-32 (reflektiert, Polynom 0xEDB88320), Bits in Indexreihenfolge
    function automatic [31:0] crc_rec(input [RW-1:0] v);
        integer i;
        reg [31:0] c;
        begin
            c = 32'hFFFF_FFFF;
            for (i = 0; i < RW; i = i + 1) c = (c >> 1) ^ ((c[0] ^ v[i]) ? 32'hEDB8_8320 : 32'd0);
            crc_rec = ~c;
        end
    endfunction
    function automatic [31:0] crc64(input [63:0] v);
        integer i;
        reg [31:0] c;
        begin
            c = 32'hFFFF_FFFF;
            for (i = 0; i < 64; i = i + 1) c = (c >> 1) ^ ((c[0] ^ v[i]) ? 32'hEDB8_8320 : 32'd0);
            crc64 = ~c;
        end
    endfunction

    wire [NB-1:0] na = a[NB-1:0];
    wire [NB-1:0] nb_ = b[NB-1:0];
    wire a_ok = a < NAMES;
    wire b_ok = b < NAMES;
    wire [SB-1:0] sa = nslot[na];

    // PUT: Pruefsumme, Dedup-Suche, freier Platz
    wire [31:0] h_in = crc_rec(rec_in);
    reg hit, have_free;
    reg [SB-1:0] hit_s, free_s;
    integer s;
    always @(*) begin
        hit = 1'b0; hit_s = {SB{1'b0}};
        have_free = 1'b0; free_s = {SB{1'b0}};
        for (s = SLOTS - 1; s >= 0; s = s - 1) begin
            if (refc[s] != 0 && shash[s] == h_in && mem_a[s] == rec_in) begin hit = 1'b1; hit_s = s; end
            if (refc[s] == 0) begin have_free = 1'b1; free_s = s; end
        end
    end
    // GET: Spiegel pruefen
    wire [31:0] ha = crc_rec(mem_a[sa]);
    wire [31:0] hb = crc_rec(mem_b[sa]);

    integer n, cnt;
    always @(*) begin
        cnt = 0;
        for (n = 0; n < SLOTS; n = n + 1) if (refc[n] != 0) cnt = cnt + 1;
        used = cnt;
    end

    reg [SB-1:0] tgt;
    always @(posedge clk) begin
        rsp_ok <= 1'b0;
        dedup <= 1'b0;
        repaired <= 1'b0;
        bad <= 1'b0;
        if (rst) begin
            for (n = 0; n < SLOTS; n = n + 1) begin
                refc[n] <= 8'd0;
                shash[n] <= 32'd0;
                mem_a[n] <= {RW{1'b0}};
                mem_b[n] <= {RW{1'b0}};
            end
            for (n = 0; n < NAMES; n = n + 1) begin
                nv[n] <= 1'b0;
                nro[n] <= 1'b0;
                nslot[n] <= {SB{1'b0}};
            end
            audit <= 32'd0;
            rsp_slot <= 8'd0;
            rsp_hash <= 32'd0;
            rec_out <= {RW{1'b0}};
        end else if (cmd_valid) begin
            case (cmd)
                C_PUT: if (a_ok && !(nv[na] && nro[na]) && (hit || have_free ||
                                                              (nv[na] && refc[sa] == 8'd1))) begin
                    // Ziel: Dedup-Treffer, sonst freier Platz, sonst (einziger Nutzer) der eigene alte Platz
                    if (hit) tgt = hit_s;
                    else if (have_free) tgt = free_s;
                    else tgt = sa;
                    if (!hit) begin
                        mem_a[tgt] <= rec_in;
                        mem_b[tgt] <= rec_in;
                        shash[tgt] <= h_in;
                    end
                    if (nv[na] && sa == tgt) begin
                        // gleicher Platz: Zaehler unveraendert
                    end else begin
                        refc[tgt] <= (hit ? refc[tgt] : 8'd0) + 8'd1;
                        if (nv[na]) refc[sa] <= refc[sa] - 8'd1;
                    end
                    nv[na] <= 1'b1;
                    nslot[na] <= tgt;
                    audit <= crc64({h_in, audit});
                    rsp_ok <= 1'b1;
                    rsp_slot <= tgt;
                    rsp_hash <= h_in;
                    dedup <= hit;
                end
                C_GET: if (a_ok && nv[na]) begin
                    rsp_slot <= sa;
                    rsp_hash <= shash[sa];
                    if (ha == shash[sa]) begin
                        rec_out <= mem_a[sa];
                        rsp_ok <= 1'b1;
                        if (hb != shash[sa]) begin mem_b[sa] <= mem_a[sa]; repaired <= 1'b1; end
                    end else if (hb == shash[sa]) begin
                        rec_out <= mem_b[sa];
                        rsp_ok <= 1'b1;
                        mem_a[sa] <= mem_b[sa];
                        repaired <= 1'b1;
                    end else begin
                        bad <= 1'b1;
                    end
                end
                C_SNAP, C_CLONE: if (a_ok && b_ok && nv[na] && !nv[nb_]) begin
                    nv[nb_] <= 1'b1;
                    nro[nb_] <= cmd == C_SNAP;
                    nslot[nb_] <= sa;
                    refc[sa] <= refc[sa] + 8'd1;
                    rsp_ok <= 1'b1;
                    rsp_slot <= sa;
                end
                C_DEL: if (a_ok && nv[na]) begin
                    nv[na] <= 1'b0;
                    nro[na] <= 1'b0;
                    refc[sa] <= refc[sa] - 8'd1;
                    rsp_ok <= 1'b1;
                end
                C_FLIP: if (a < SLOTS && b[14:0] < RW) begin
                    if (b[15]) mem_b[a[SB-1:0]][b[14:0]] <= ~mem_b[a[SB-1:0]][b[14:0]];
                    else mem_a[a[SB-1:0]][b[14:0]] <= ~mem_a[a[SB-1:0]][b[14:0]];
                    rsp_ok <= 1'b1;
                end
                default: ;
            endcase
        end
    end
endmodule
