`timescale 1ns/1ps
// Kombinatorisches Kuerzen und Guard der Baustufe 0: teilt durch 2, wenn alle Koeffizienten gerade sind und
// kn >= 2 (falls reduce_en), und meldet ovf, wenn ein Koeffizient ausserhalb [minv, maxv] liegt (die Grenzen
// der Guard-Breite w_eff, siehe qguard_limits) oder k > k_max.
// Fuer kurze Pfade werden beide Faelle parallel verglichen: (o >>> 1) > maxv gilt genau dann, wenn
// o > 2 maxv + 1, und (o >>> 1) < minv genau dann, wenn o < 2 minv; die Auswahl folgt danach.
//
// reduce_en[1] (kanonische Form, hat Vorrang vor Bit 0): x = a0 + a1 w + a2 w^2 + a3 w^3 ist genau dann durch
// sqrt(2) = w - w^3 teilbar, wenn a0 = a2 und a1 = a3 (mod 2); dann ist x / sqrt(2) = x sqrt(2) / 2 =
// ((a1 - a3), (a0 + a2), (a1 + a3), (a2 - a0)) / 2. Gilt das fuer alle vier Amplituden und kn >= 1, sinkt k um
// eins. Der Schritt laeuft zweimal hintereinander: Nach einem Gatter aus kanonischem Zustand genuegt das, denn
// nur H aendert den kleinsten Exponenten, und weil H sich selbst invers ist, um hoechstens eins nach unten
// (kn = k + 1, also hoechstens zwei Schritte). Ergebnis: k ist danach der kleinste moegliche Exponent.
// Die kanonische Form verlaengert den kombinatorischen Pfad deutlich (ECP5: Pipeline 70,5 -> 41 MHz). Mit dem Makro
// QCOP_NO_CANON (iverilog -D, Yosys read_verilog -D) wird sie weggelassen; reduce_en[1] wirkt dann nicht.
`ifdef QCOP_NO_CANON
`define QCOP_CANON 0
`else
`define QCOP_CANON 1
`endif
module qnorm2 #(
    parameter integer CANON = `QCOP_CANON,
    parameter integer W = 16,
    parameter integer TW = W + 2
) (
    input wire [16*TW-1:0] o_flat,
    input wire [8:0] kn_in,
    input wire [1:0] reduce_en,
    input wire signed [TW-1:0] maxv,
    input wire signed [TW-1:0] minv,
    input wire [7:0] k_max,
    output reg [16*W-1:0] coeffs,
    output reg [7:0] k,
    output reg ovf
);
    reg signed [TW-1:0] o [0:15];
    reg signed [TW+1:0] maxv2, minv2;
    reg all_even, red, ovf_plain, ovf_half;
    reg [8:0] kn;
    integer m;
    // kanonische Form: zwei sqrt(2)-Schritte (qroot2), dann Guard (qguard2)
    wire [16*TW-1:0] r_flat;
    wire [8:0] kr;
    wire [16*W-1:0] coeffs_r;
    wire [7:0] k_r;
    wire ovf_r;
    qroot2 #(.TW(TW)) root (.o_flat(o_flat), .kn_in(kn_in), .r_flat(r_flat), .kr(kr));
    qguard2 #(.W(W), .TW(TW)) guard (.r_flat(r_flat), .kr(kr), .maxv(maxv), .minv(minv), .k_max(k_max),
                                     .coeffs(coeffs_r), .k(k_r), .ovf(ovf_r));

    always @(*) begin
        for (m = 0; m < 16; m = m + 1) o[m] = $signed(o_flat[m*TW +: TW]);
        all_even = 1'b1;
        for (m = 0; m < 16; m = m + 1) if (o[m][0]) all_even = 1'b0;
        red = reduce_en[0] && all_even && kn_in >= 2;
        maxv2 = 2 * maxv + 1;
        minv2 = 2 * minv;
        ovf_plain = 1'b0;
        ovf_half = 1'b0;
        for (m = 0; m < 16; m = m + 1) begin
            if (o[m] > maxv || o[m] < minv) ovf_plain = 1'b1;
            if (o[m] > maxv2 || o[m] < minv2) ovf_half = 1'b1;
        end
        kn = red ? kn_in - 9'd2 : kn_in;
        ovf = (red ? ovf_half : ovf_plain) || kn > {1'b0, k_max};
        for (m = 0; m < 16; m = m + 1) coeffs[m*W +: W] = red ? o[m][W:1] : o[m][W-1:0];
        k = kn[7:0];
        if (CANON != 0 && reduce_en[1]) begin
            ovf = ovf_r;
            k = k_r;
            coeffs = coeffs_r;
        end
    end
endmodule

// Grenzen der Guard-Breite: maxv = 2^(w_eff-1) - 1, minv = -2^(w_eff-1).
module qguard_limits #(
    parameter integer TW = 18
) (
    input wire [5:0] w_eff,
    output wire signed [TW-1:0] maxv,
    output wire signed [TW-1:0] minv
);
    assign maxv = ({{(TW-1){1'b0}}, 1'b1} <<< (w_eff - 1)) - 1;
    assign minv = -maxv - 1;
endmodule

// Zwei sqrt(2)-Schritte der kanonischen Form (Regel im Kopf von qnorm2): r = o / sqrt(2)^(k_in - kr).
module qroot2 #(
    parameter integer TW = 18
) (
    input wire [16*TW-1:0] o_flat,
    input wire [8:0] kn_in,
    output reg [16*TW-1:0] r_flat,
    output reg [8:0] kr
);
    reg signed [TW-1:0] o [0:15];
    reg signed [TW-1:0] r1 [0:15];
    reg signed [TW-1:0] r2 [0:15];
    reg signed [TW:0] t0, t1, t2, t3;
    reg div1, div2;
    integer m, q;
    always @(*) begin
        for (m = 0; m < 16; m = m + 1) o[m] = $signed(o_flat[m*TW +: TW]);
        div1 = kn_in >= 1;
        for (q = 0; q < 4; q = q + 1)
            if (o[4*q][0] != o[4*q+2][0] || o[4*q+1][0] != o[4*q+3][0]) div1 = 1'b0;
        for (q = 0; q < 4; q = q + 1) begin
            t0 = o[4*q+1] - o[4*q+3]; t1 = o[4*q] + o[4*q+2];
            t2 = o[4*q+1] + o[4*q+3]; t3 = o[4*q+2] - o[4*q];
            r1[4*q] = div1 ? t0[TW:1] : o[4*q];     r1[4*q+1] = div1 ? t1[TW:1] : o[4*q+1];
            r1[4*q+2] = div1 ? t2[TW:1] : o[4*q+2]; r1[4*q+3] = div1 ? t3[TW:1] : o[4*q+3];
        end
        div2 = div1 && kn_in >= 2;
        for (q = 0; q < 4; q = q + 1)
            if (r1[4*q][0] != r1[4*q+2][0] || r1[4*q+1][0] != r1[4*q+3][0]) div2 = 1'b0;
        for (q = 0; q < 4; q = q + 1) begin
            t0 = r1[4*q+1] - r1[4*q+3]; t1 = r1[4*q] + r1[4*q+2];
            t2 = r1[4*q+1] + r1[4*q+3]; t3 = r1[4*q+2] - r1[4*q];
            r2[4*q] = div2 ? t0[TW:1] : r1[4*q];     r2[4*q+1] = div2 ? t1[TW:1] : r1[4*q+1];
            r2[4*q+2] = div2 ? t2[TW:1] : r1[4*q+2]; r2[4*q+3] = div2 ? t3[TW:1] : r1[4*q+3];
        end
        kr = kn_in - {8'd0, div1} - {8'd0, div2};
        for (m = 0; m < 16; m = m + 1) r_flat[m*TW +: TW] = r2[m];
    end
endmodule

// Guard nach der kanonischen Form: ovf, wenn ein Koeffizient ausserhalb [minv, maxv] liegt oder kr > k_max.
module qguard2 #(
    parameter integer W = 16,
    parameter integer TW = W + 2
) (
    input wire [16*TW-1:0] r_flat,
    input wire [8:0] kr,
    input wire signed [TW-1:0] maxv,
    input wire signed [TW-1:0] minv,
    input wire [7:0] k_max,
    output reg [16*W-1:0] coeffs,
    output reg [7:0] k,
    output reg ovf
);
    reg signed [TW-1:0] r;
    integer m;
    always @(*) begin
        ovf = kr > {1'b0, k_max};
        for (m = 0; m < 16; m = m + 1) begin
            r = $signed(r_flat[m*TW +: TW]);
            if (r > maxv || r < minv) ovf = 1'b1;
            coeffs[m*W +: W] = r[W-1:0];
        end
        k = kr[7:0];
    end
endmodule
