`timescale 1ns/1ps
// Pipeline-Fassung der Baustufe 0 mit CTX Kontexten (unabhaengige Laeufe, z. B. Baender/Partitionen).
//
// Vier Stufen statt eines langen Takts:
//   S0  Annahme: Kontext op_ctx lesen, Gatter und Zustand registrieren (Budget pruefen)
//   S1  Gatterwerk qgate2
//   S2  Kuerzen und Guard qnorm2
//   S3  Status bestimmen und in den Kontext zurueckschreiben
// Ein Kontext ist waehrend seines Gatters belegt (ready[c] = 0, vier Takte). Wechseln sich mindestens vier
// Kontexte ab, nimmt die Einheit jeden Takt ein Gatter an; ein einzelner Lauf braucht vier Takte je Gatter.
// Rechenregeln, Status und Konfiguration wie qstep2 (bitgenau gleich, geprueft mit pipe_check.py).
// Die Konfiguration ist fuer alle Kontexte gemeinsam.
module qstep2p #(
    parameter integer W = 16,
    parameter integer CTX = 4,
    parameter integer CB = CTX > 1 ? $clog2(CTX) : 1
) (
    input wire clk,
    input wire rst,
    input wire load,
    input wire [CB-1:0] load_ctx,
    input wire op_valid,
    input wire [CB-1:0] op_ctx,
    input wire [3:0] opcode,
    input wire target,
    input wire [15:0] allow,
    input wire [5:0] w_eff,
    input wire [7:0] k_max,
    input wire [15:0] budget,
    input wire reduce_en,
    output wire [CTX-1:0] ready,
    // Lesen eines Kontexts
    input wire [CB-1:0] rd_ctx,
    output wire [16*W-1:0] coeffs,
    output wire [7:0] k,
    output wire [1:0] status,
    output wire [15:0] gates_done
);
    localparam [1:0] CONTINUE = 0, GUARD = 1, REJECT = 2, STEP_LIMIT = 3;
    localparam integer TW = W + 2;

    reg [16*W-1:0] c_coeffs [0:CTX-1];
    reg [7:0] c_k [0:CTX-1];
    reg [1:0] c_status [0:CTX-1];
    reg [15:0] c_done [0:CTX-1];
    reg [CTX-1:0] busy;

    assign coeffs = c_coeffs[rd_ctx];
    assign k = c_k[rd_ctx];
    assign status = c_status[rd_ctx];
    assign gates_done = c_done[rd_ctx];
    genvar g;
    generate
        for (g = 0; g < CTX; g = g + 1) begin : rdy
            assign ready[g] = !busy[g];
        end
    endgenerate

    // Stufe 1 (Eingang des Gatterwerks)
    reg v1, lim1;
    reg [CB-1:0] ctx1;
    reg [3:0] op1;
    reg tg1;
    reg [16*W-1:0] s1_coeffs;
    reg [7:0] s1_k;
    // Stufe 2 (Eingang von Kuerzen/Guard)
    reg v2, lim2, bad2;
    reg [CB-1:0] ctx2;
    reg [16*TW-1:0] s2_o;
    reg [8:0] s2_kn;
    // Stufe 3 (Zurueckschreiben)
    reg v3, lim3, bad3, ovf3;
    reg [CB-1:0] ctx3;
    reg [16*W-1:0] s3_coeffs;
    reg [7:0] s3_k;

    wire [16*TW-1:0] o_flat;
    wire [8:0] kn;
    wire bad;
    wire [16*W-1:0] coeffs_n;
    wire [7:0] k_n;
    wire ovf;

    // Guard-Grenzen einmal je Takt aus w_eff registrieren (w_eff ist waehrend eines Laufs fest; das erste
    // Gatter erreicht S2 fruehestens drei Takte nach dem Laden).
    wire signed [TW-1:0] maxv, minv;
    reg signed [TW-1:0] maxv_q, minv_q;
    qguard_limits #(.TW(TW)) limits (.w_eff(w_eff), .maxv(maxv), .minv(minv));
    always @(posedge clk) begin
        maxv_q <= maxv;
        minv_q <= minv;
    end

    qgate2 #(.W(W), .TW(TW)) gate (
        .coeffs(s1_coeffs), .k(s1_k), .opcode(op1), .target(tg1), .allow(allow),
        .o_flat(o_flat), .kn(kn), .bad(bad)
    );
    qnorm2 #(.W(W), .TW(TW)) norm (
        .o_flat(s2_o), .kn_in(s2_kn), .reduce_en(reduce_en), .maxv(maxv_q), .minv(minv_q), .k_max(k_max),
        .coeffs(coeffs_n), .k(k_n), .ovf(ovf)
    );

    wire accept = op_valid && !busy[op_ctx] && c_status[op_ctx] == CONTINUE;
    integer c;

    always @(posedge clk) begin
        if (rst) begin
            v1 <= 1'b0;
            v2 <= 1'b0;
            v3 <= 1'b0;
            busy <= {CTX{1'b0}};
            for (c = 0; c < CTX; c = c + 1) begin
                c_coeffs[c] <= {{(16*W-1){1'b0}}, 1'b1};
                c_k[c] <= 8'd0;
                c_status[c] <= CONTINUE;
                c_done[c] <= 16'd0;
            end
        end else begin
            // S0 -> S1
            v1 <= accept;
            if (accept) begin
                ctx1 <= op_ctx;
                op1 <= opcode;
                tg1 <= target;
                s1_coeffs <= c_coeffs[op_ctx];
                s1_k <= c_k[op_ctx];
                lim1 <= budget != 16'd0 && c_done[op_ctx] >= budget;
            end
            // S1 -> S2
            v2 <= v1;
            if (v1) begin
                ctx2 <= ctx1;
                s2_o <= o_flat;
                s2_kn <= kn;
                bad2 <= bad;
                lim2 <= lim1;
            end
            // S2 -> S3
            v3 <= v2;
            if (v2) begin
                ctx3 <= ctx2;
                lim3 <= lim2;
                bad3 <= bad2;
                ovf3 <= ovf;
                s3_coeffs <= coeffs_n;
                s3_k <= k_n;
            end
            // S3: zurueckschreiben
            if (v3) begin
                if (lim3) c_status[ctx3] <= STEP_LIMIT;
                else if (bad3) c_status[ctx3] <= REJECT;
                else if (ovf3) c_status[ctx3] <= GUARD;
                else begin
                    c_coeffs[ctx3] <= s3_coeffs;
                    c_k[ctx3] <= s3_k;
                    c_done[ctx3] <= c_done[ctx3] + 16'd1;
                end
            end
            // Belegung: gesetzt bei Annahme, frei nach dem Zurueckschreiben
            for (c = 0; c < CTX; c = c + 1)
                if (accept && op_ctx == c) busy[c] <= 1'b1;
                else if (v3 && ctx3 == c) busy[c] <= 1'b0;
            // Laden (nur fuer einen freien Kontext erlaubt)
            if (load && !busy[load_ctx]) begin
                c_coeffs[load_ctx] <= {{(16*W-1){1'b0}}, 1'b1};
                c_k[load_ctx] <= 8'd0;
                c_status[load_ctx] <= CONTINUE;
                c_done[load_ctx] <= 16'd0;
            end
        end
    end
endmodule
