`timescale 1ns/1ps
// Partitionierbares Bandregister: CELLS Zellen (Vorgabe 128 = 2^7), aufteilbar in bis zu PARTS Baender der
// Laenge 2^n (Buddy-Regel: ein Band der Stufe n beginnt auf einem Vielfachen von 2^n). Jedes Band traegt ein
// Profil; die Vorgaben sind "eingebrannt" (fester Festwertteil je Stufe n) und lassen sich je Stufe ueber
// Register ueberschreiben, ohne die Hardware neu zu bauen.
//
// Eingebranntes Profil der Stufe n (Setzungen, keine hergeleiteten Werte):
//   HS      = n                         (Bandlaenge 2^n entspricht HS(n))
//   CLOCK   = n mod 8                   (Typ-Uhr mod 8, k407)
//   LENGTH  = 2^n,  REPEAT = CELLS/2^n  (wie oft das Band in das ganze Register passt)
//   WEIGHT  = 2^n / CELLS  in Q2.30     (Anteil am Register)
//   PHASE   = n/8 Drehung   (TURN)      (Achter-Uhr, ein 45-Grad-Schritt je Stufe, vgl. H211)
// Ueberschreibbar je Stufe: WEIGHT, PHASE, CLOCK (Bit im Ueberschreib-Register).
//
// Befehle (cmd_valid, ein Befehl je Takt, Antwort im naechsten Takt: rsp_ok, rsp_data):
//   1 SET_PART   idx = a, b = {valid, order[3:0], base[..]}      Abschnitt idx setzen
//   2 WR_CELL    Band a, Zelle b, Wert d[CW-1:0]                guard, wenn Band ungueltig oder b >= Laenge
//   3 RD_CELL    Band a, Zelle b                                 rsp_data = Zellwert
//   4 WR_WORD    Wort a (BUSW Bit), Daten d                      direkter Zugriff auf das ganze Register
//   5 RD_WORD    Wort a                                          rsp_data = Wort
//   6 SET_PROF   Stufe a, Feld b (0 WEIGHT, 1 PHASE, 2 CLOCK), Wert d[31:0]; setzt das Ueberschreib-Bit
//   7 CLR_PROF   Stufe a                                         zurueck auf das eingebrannte Profil
//   8 RD_PROF    Band a, Feld b (0 WEIGHT, 1 PHASE, 2 CLOCK, 3 HS, 4 LENGTH, 5 REPEAT, 6 BASE)  wirksamer Wert
// Laufend gueltig: layout_ok (alle gueltigen Abschnitte ausgerichtet, im Register, ohne Ueberlappung) und
// full (zusaetzlich jede Zelle belegt). WR_CELL/RD_CELL melden guard (rsp_ok = 0), solange layout_ok = 0.
module qband #(
    parameter integer CELLS = 128,
    parameter integer PARTS = 16,
    parameter integer CW = 1,       // Bit je Zelle
    parameter integer BUSW = 128,   // Busbreite fuer WR_WORD/RD_WORD
    parameter integer L = $clog2(CELLS),
    parameter integer PB = PARTS > 1 ? $clog2(PARTS) : 1
) (
    input wire clk,
    input wire rst,
    input wire cmd_valid,
    input wire [3:0] cmd,
    input wire [7:0] a,
    input wire [15:0] b,
    input wire [BUSW-1:0] d,
    output reg rsp_ok,
    output reg [BUSW-1:0] rsp_data,
    output wire layout_ok,
    output wire full,
    // Abschnittstabelle fuer spaetere Rechenwerke je Band
    output wire [PARTS-1:0] part_valid,
    output wire [PARTS*L-1:0] part_base,
    output wire [PARTS*4-1:0] part_order
);
    localparam integer WORDS = (CELLS * CW + BUSW - 1) / BUSW;
    localparam [3:0] C_SET_PART = 1, C_WR_CELL = 2, C_RD_CELL = 3, C_WR_WORD = 4, C_RD_WORD = 5,
                     C_SET_PROF = 6, C_CLR_PROF = 7, C_RD_PROF = 8;

    reg [CELLS*CW-1:0] cells;
    reg pv [0:PARTS-1];
    reg [L-1:0] pb [0:PARTS-1];
    reg [3:0] po [0:PARTS-1];
    reg [2:0] ov [0:L];             // Ueberschreib-Bits je Stufe: {CLOCK, PHASE, WEIGHT}
    reg [31:0] ov_weight [0:L];
    reg [31:0] ov_phase [0:L];
    reg [2:0] ov_clock [0:L];

    genvar g;
    generate
        for (g = 0; g < PARTS; g = g + 1) begin : tab
            assign part_valid[g] = pv[g];
            assign part_base[g*L +: L] = pb[g];
            assign part_order[g*4 +: 4] = po[g];
        end
    endgenerate

    // ---------------------------------------------------------------- Pruefung der Aufteilung
    reg ok_r, full_r;
    reg [L+4:0] total;
    reg [L:0] len_i, len_j;
    integer i, j;
    always @(*) begin
        ok_r = 1'b1;
        total = 0;
        len_i = 0;
        len_j = 0;
        for (i = 0; i < PARTS; i = i + 1) if (pv[i]) begin
            len_i = {{L{1'b0}}, 1'b1} << po[i];
            if (po[i] > L) ok_r = 1'b0;
            if ((pb[i] & (len_i - 1'b1)) != 0) ok_r = 1'b0;          // ausgerichtet (Buddy-Regel)
            if ({1'b0, pb[i]} + len_i > CELLS) ok_r = 1'b0;           // im Register
            for (j = i + 1; j < PARTS; j = j + 1) if (pv[j]) begin   // keine Ueberlappung
                len_j = {{L{1'b0}}, 1'b1} << po[j];
                if ({1'b0, pb[i]} < {1'b0, pb[j]} + len_j && {1'b0, pb[j]} < {1'b0, pb[i]} + len_i) ok_r = 1'b0;
            end
            total = total + len_i;
        end
        // Ohne Ueberlappung und alle im Register: voll genau dann, wenn die Laengen sich zu CELLS summieren.
        full_r = ok_r && total == CELLS;
    end
    assign layout_ok = ok_r;
    assign full = full_r;

    // ---------------------------------------------------------------- Profile
    function automatic [31:0] burned(input [3:0] n, input [2:0] field);
        case (field)
            3'd0: burned = (32'h4000_0000 >> L) << n;   // WEIGHT = 2^n / CELLS, Q2.30
            3'd1: burned = {n[2:0], 29'd0};               // PHASE = n/8 Drehung
            3'd2: burned = {29'd0, n[2:0]};               // CLOCK = n mod 8
            3'd3: burned = n;                              // HS
            3'd4: burned = 32'd1 << n;                     // LENGTH
            3'd5: burned = CELLS >> n;                     // REPEAT
            default: burned = 32'd0;
        endcase
    endfunction

    reg [L:0] len_a;
    reg [L-1:0] base_a;
    reg [3:0] n_a;
    reg [31:0] prof;
    integer p, s, cc;

    always @(posedge clk) begin
        rsp_ok <= 1'b0;
        rsp_data <= {BUSW{1'b0}};
        if (rst) begin
            cells <= {(CELLS*CW){1'b0}};
            for (p = 0; p < PARTS; p = p + 1) begin
                pv[p] <= 1'b0;
                pb[p] <= {L{1'b0}};
                po[p] <= 4'd0;
            end
            for (s = 0; s <= L; s = s + 1) begin
                ov[s] <= 3'b000;
                ov_weight[s] <= 32'd0;
                ov_phase[s] <= 32'd0;
                ov_clock[s] <= 3'd0;
            end
        end else if (cmd_valid) begin
            n_a = po[a[PB-1:0]];
            base_a = pb[a[PB-1:0]];
            len_a = {{L{1'b0}}, 1'b1} << n_a;
            case (cmd)
                C_SET_PART: if (a < PARTS) begin
                    pv[a[PB-1:0]] <= b[L+4];
                    po[a[PB-1:0]] <= b[L+3:L];
                    pb[a[PB-1:0]] <= b[L-1:0];
                    rsp_ok <= 1'b1;
                end
                C_WR_CELL: if (a < PARTS && layout_ok && pv[a[PB-1:0]] && b < len_a) begin
                    cells[(base_a + b[L-1:0]) * CW +: CW] <= d[CW-1:0];
                    rsp_ok <= 1'b1;
                end
                C_RD_CELL: if (a < PARTS && layout_ok && pv[a[PB-1:0]] && b < len_a) begin
                    rsp_data <= cells[(base_a + b[L-1:0]) * CW +: CW];
                    rsp_ok <= 1'b1;
                end
                C_WR_WORD: if (a < WORDS) begin
                    for (cc = 0; cc < BUSW; cc = cc + 1)
                        if (a * BUSW + cc < CELLS * CW) cells[a * BUSW + cc] <= d[cc];
                    rsp_ok <= 1'b1;
                end
                C_RD_WORD: if (a < WORDS) begin
                    for (cc = 0; cc < BUSW; cc = cc + 1)
                        rsp_data[cc] <= (a * BUSW + cc < CELLS * CW) ? cells[a * BUSW + cc] : 1'b0;
                    rsp_ok <= 1'b1;
                end
                C_SET_PROF: if (a <= L && b < 3) begin
                    ov[a] <= ov[a] | (3'b001 << b[1:0]);
                    if (b == 0) ov_weight[a] <= d[31:0];
                    if (b == 1) ov_phase[a] <= d[31:0];
                    if (b == 2) ov_clock[a] <= d[2:0];
                    rsp_ok <= 1'b1;
                end
                C_CLR_PROF: if (a <= L) begin
                    ov[a] <= 3'b000;
                    rsp_ok <= 1'b1;
                end
                C_RD_PROF: if (a < PARTS && layout_ok && pv[a[PB-1:0]] && b < 7) begin
                    if (b == 6) prof = base_a;
                    else if (b == 0 && ov[n_a][0]) prof = ov_weight[n_a];
                    else if (b == 1 && ov[n_a][1]) prof = ov_phase[n_a];
                    else if (b == 2 && ov[n_a][2]) prof = ov_clock[n_a];
                    else prof = burned(n_a, b[2:0]);
                    rsp_data <= prof;
                    rsp_ok <= 1'b1;
                end
                default: ;
            endcase
        end
    end
endmodule
