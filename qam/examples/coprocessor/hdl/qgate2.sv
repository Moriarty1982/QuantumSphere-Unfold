`timescale 1ns/1ps
// Kombinatorisches Gatterwerk der Baustufe 0 (ohne Takt): wendet ein Clifford+T-Gatter auf einen
// Zwei-Qubit-Zustand in Z[w]/sqrt(2)^k an. Gemeinsam genutzt von qstep2 (ein Takt) und qstep2p (Pipeline).
// Ausgabe in Arbeitsbreite TW = W + 2 (Reserve fuer Summen bei H), kn = neuer Exponent vor dem Kuerzen.
module qgate2 #(
    parameter integer W = 16,
    parameter integer TW = W + 2
) (
    input wire [16*W-1:0] coeffs,
    input wire [7:0] k,
    input wire [3:0] opcode,
    input wire target,
    input wire [15:0] allow,
    output reg [16*TW-1:0] o_flat,
    output reg [8:0] kn,
    output reg bad
);
    localparam [3:0] OP_NOP = 0, OP_X = 1, OP_Z = 2, OP_S = 3, OP_SDG = 4,
                     OP_T = 5, OP_TDG = 6, OP_H = 7, OP_CX = 8;
    reg signed [TW-1:0] t [0:15];
    reg signed [TW-1:0] o [0:15];
    reg [2:0] rot;
    reg [1:0] b;
    integer m, i, j, d;

    always @(*) begin
        for (m = 0; m < 16; m = m + 1) begin
            t[m] = $signed(coeffs[m*W +: W]);
            o[m] = t[m];
        end
        kn = {1'b0, k};
        bad = (opcode > OP_CX) || !allow[opcode];
        b = target ? 2'd2 : 2'd1;
        case (opcode)
            OP_Z: rot = 3'd4;
            OP_S: rot = 3'd2;
            OP_SDG: rot = 3'd6;
            OP_T: rot = 3'd1;
            default: rot = 3'd7;  // OP_TDG
        endcase
        case (opcode)
            OP_X: for (i = 0; i < 4; i = i + 1)
                if ((i & b) == 0)
                    for (j = 0; j < 4; j = j + 1) begin
                        o[4*i+j] = t[4*(i|b)+j];
                        o[4*(i|b)+j] = t[4*i+j];
                    end
            OP_CX: for (i = 0; i < 4; i = i + 1)
                // Steuerqubit ist das jeweils andere Qubit.
                if ((i & b) == 0 && (i & (3 ^ b)) != 0)
                    for (j = 0; j < 4; j = j + 1) begin
                        o[4*i+j] = t[4*(i|b)+j];
                        o[4*(i|b)+j] = t[4*i+j];
                    end
            OP_Z, OP_S, OP_SDG, OP_T, OP_TDG:
                // w^r * a: Koeffizient j kommt von (j - r) mod 4, negiert bei genau einem Umlauf (w^4 = -1).
                for (i = 0; i < 4; i = i + 1)
                    if ((i & b) != 0)
                        for (j = 0; j < 4; j = j + 1) begin
                            d = j - rot + 8;
                            o[4*i+j] = (d >= 4 && d < 8) ? -t[4*i+(d & 3)] : t[4*i+(d & 3)];
                        end
            OP_H: begin
                for (i = 0; i < 4; i = i + 1)
                    if ((i & b) == 0)
                        for (j = 0; j < 4; j = j + 1) begin
                            o[4*i+j] = t[4*i+j] + t[4*(i|b)+j];
                            o[4*(i|b)+j] = t[4*i+j] - t[4*(i|b)+j];
                        end
                kn = kn + 9'd1;
            end
            default: ;
        endcase
        for (m = 0; m < 16; m = m + 1) o_flat[m*TW +: TW] = o[m];
    end
endmodule
