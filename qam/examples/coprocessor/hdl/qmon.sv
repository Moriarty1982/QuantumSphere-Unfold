`timescale 1ns/1ps
// Waechter fuer die Norm des exakten Zustands (kombinatorisch).
// Fuer x = a0 + a1 w + a2 w^2 + a3 w^3 (w = exp(i pi/4)) ist |x|^2 = P + sqrt(2) Q mit
//   P = a0^2 + a1^2 + a2^2 + a3^2,   Q = a0 a1 + a1 a2 + a2 a3 - a3 a0.
// Ein Zustand aus vier Amplituden x_i / sqrt(2)^k ist genau dann normiert, wenn
//   sum P_i = 2^k  und  sum Q_i = 0
// (1 und sqrt(2) sind ueber Q linear unabhaengig). ok = 1, wenn beides gilt.
// Ein einzelnes gekipptes Bit unterhalb des Vorzeichenbits aendert P immer: aus a wird a + d, d = +2^b (Bit b war
// 0) oder d = -2^b (Bit b war 1), und (a + d)^2 = a^2 nur fuer a = -d/2 = -+2^(b-1); dessen Bit b ist aber jeweils
// das andere. Beim Vorzeichenbit gilt das nicht (a = 2^(W-2) wird zu -2^(W-2)); dort hilft hoechstens Q.
module qmon #(
    parameter integer W = 16,
    parameter integer SW = 2 * W + 6     // Breite der Summen
) (
    input wire [16*W-1:0] coeffs,
    input wire [7:0] k,
    output reg ok,
    output reg signed [SW-1:0] psum,
    output reg signed [SW-1:0] qsum
);
    reg signed [W-1:0] a [0:15];
    reg signed [SW-1:0] target;
    integer m, q;

    always @(*) begin
        for (m = 0; m < 16; m = m + 1) a[m] = $signed(coeffs[m*W +: W]);
        psum = 0;
        qsum = 0;
        for (q = 0; q < 4; q = q + 1) begin
            psum = psum + a[4*q] * a[4*q] + a[4*q+1] * a[4*q+1] + a[4*q+2] * a[4*q+2] + a[4*q+3] * a[4*q+3];
            qsum = qsum + a[4*q] * a[4*q+1] + a[4*q+1] * a[4*q+2] + a[4*q+2] * a[4*q+3] - a[4*q+3] * a[4*q];
        end
        target = (k < SW - 1) ? ({{(SW-1){1'b0}}, 1'b1} << k) : {SW{1'b0}};
        ok = (k < SW - 1) && psum == target && qsum == 0;
    end
endmodule
