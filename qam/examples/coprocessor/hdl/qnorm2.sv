`timescale 1ns/1ps
// Kombinatorisches Kuerzen und Guard der Baustufe 0: teilt durch 2, wenn alle Koeffizienten gerade sind und
// kn >= 2 (falls reduce_en), und meldet ovf, wenn ein Koeffizient ausserhalb [minv, maxv] liegt (die Grenzen
// der Guard-Breite w_eff, siehe qguard_limits) oder k > k_max.
// Fuer kurze Pfade werden beide Faelle parallel verglichen: (o >>> 1) > maxv gilt genau dann, wenn
// o > 2 maxv + 1, und (o >>> 1) < minv genau dann, wenn o < 2 minv; die Auswahl folgt danach.
module qnorm2 #(
    parameter integer W = 16,
    parameter integer TW = W + 2
) (
    input wire [16*TW-1:0] o_flat,
    input wire [8:0] kn_in,
    input wire reduce_en,
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

    always @(*) begin
        for (m = 0; m < 16; m = m + 1) o[m] = $signed(o_flat[m*TW +: TW]);
        all_even = 1'b1;
        for (m = 0; m < 16; m = m + 1) if (o[m][0]) all_even = 1'b0;
        red = reduce_en && all_even && kn_in >= 2;
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
