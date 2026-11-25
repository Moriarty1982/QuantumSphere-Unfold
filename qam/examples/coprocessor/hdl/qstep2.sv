`timescale 1ns/1ps
// Baustufe 0 des Quanten-Coprozessors: exakte Zustandsvektor-Einheit fuer zwei Qubits.
//
// Jede der vier Amplituden ist ein Element von Z[w]/sqrt(2)^k mit w = exp(i*pi/4):
//   amp[i] = (c[4i] + c[4i+1] w + c[4i+2] w^2 + c[4i+3] w^3) / sqrt(2)^k
// Die Exponentenzahl k ist fuer den ganzen Zustand gemeinsam. Damit sind alle
// Clifford+T-Gatter exakt: T multipliziert mit w (ein Oktantschritt), H addiert und
// subtrahiert Paare und erhoeht k um eins. Es gibt keine Rundung.
//
// Amplitudenindex i: Bit q von i ist Qubit q (Reihenfolge wie Qiskit).
// Ein Gatter pro Takt. Status wie die MMA-Antwort:
//   0 continue  Gatter ausgefuehrt
//   1 guard     Ergebnis passt nicht in W Bit; Zustand bleibt, Einheit stoppt
//   2 reject    unbekannter Opcode; Zustand bleibt, Einheit stoppt
module qstep2 #(
    parameter integer W = 16
) (
    input wire clk,
    input wire rst,
    // Laden setzt den Zustand auf |00> und den Status auf continue.
    input wire load,
    input wire op_valid,
    input wire [3:0] opcode,
    input wire target,
    output reg [16*W-1:0] coeffs,
    output reg [7:0] k,
    output reg [1:0] status,
    output reg [15:0] gates_done
);
    localparam [3:0] OP_NOP = 0, OP_X = 1, OP_Z = 2, OP_S = 3, OP_SDG = 4,
                     OP_T = 5, OP_TDG = 6, OP_H = 7, OP_CX = 8;
    localparam [1:0] CONTINUE = 0, GUARD = 1, REJECT = 2;
    localparam integer TW = W + 2;  // Arbeitsbreite mit Reserve fuer Summen
    localparam signed [TW-1:0] MAXV = (1 <<< (W - 1)) - 1;
    localparam signed [TW-1:0] MINV = -(1 <<< (W - 1));

    reg signed [TW-1:0] t [0:15];
    reg signed [TW-1:0] u;
    reg signed [TW-1:0] v;
    reg [8:0] kn;
    reg bad, ovf, all_even;
    integer m, i, j, p, r, rr, rot, b;

    // Multipliziert Amplitude a mit w^rot: w*(a0,a1,a2,a3) = (-a3,a0,a1,a2).
    task phase(input integer a, input integer rot_in);
        begin
            for (rr = 0; rr < rot_in; rr = rr + 1) begin
                u = t[4*a+3];
                t[4*a+3] = t[4*a+2];
                t[4*a+2] = t[4*a+1];
                t[4*a+1] = t[4*a];
                t[4*a] = -u;
            end
        end
    endtask

    task swap_amp(input integer a, input integer c);
        begin
            for (j = 0; j < 4; j = j + 1) begin
                u = t[4*a+j];
                t[4*a+j] = t[4*c+j];
                t[4*c+j] = u;
            end
        end
    endtask

    always @(posedge clk) begin
        if (rst || load) begin
            coeffs <= {{(16*W-1){1'b0}}, 1'b1};
            k <= 8'd0;
            status <= CONTINUE;
            gates_done <= 16'd0;
        end else if (op_valid && status == CONTINUE) begin
            for (m = 0; m < 16; m = m + 1)
                t[m] = $signed(coeffs[m*W +: W]);
            kn = {1'b0, k};
            bad = 1'b0;
            ovf = 1'b0;
            b = target ? 2 : 1;
            case (opcode)
                OP_NOP: ;
                OP_X: for (i = 0; i < 4; i = i + 1) if ((i & b) == 0) swap_amp(i, i | b);
                OP_CX: for (i = 0; i < 4; i = i + 1)
                    // Steuerqubit ist das jeweils andere Qubit.
                    if ((i & b) == 0 && (i & (3 ^ b)) != 0) swap_amp(i, i | b);
                OP_Z, OP_S, OP_SDG, OP_T, OP_TDG: begin
                    case (opcode)
                        OP_Z: rot = 4;
                        OP_S: rot = 2;
                        OP_SDG: rot = 6;
                        OP_T: rot = 1;
                        default: rot = 7;
                    endcase
                    for (i = 0; i < 4; i = i + 1) if ((i & b) != 0) phase(i, rot);
                end
                OP_H: begin
                    for (i = 0; i < 4; i = i + 1) if ((i & b) == 0) begin
                        p = i | b;
                        for (j = 0; j < 4; j = j + 1) begin
                            u = t[4*i+j] + t[4*p+j];
                            v = t[4*i+j] - t[4*p+j];
                            t[4*i+j] = u;
                            t[4*p+j] = v;
                        end
                    end
                    kn = kn + 9'd1;
                end
                default: bad = 1'b1;
            endcase

            // Kuerzen: sind alle Koeffizienten gerade und k >= 2, durch 2 teilen.
            all_even = 1'b1;
            for (m = 0; m < 16; m = m + 1) if (t[m][0]) all_even = 1'b0;
            if (all_even && kn >= 2) begin
                for (m = 0; m < 16; m = m + 1) t[m] = t[m] >>> 1;
                kn = kn - 9'd2;
            end

            for (m = 0; m < 16; m = m + 1) if (t[m] > MAXV || t[m] < MINV) ovf = 1'b1;
            if (kn > 9'd255) ovf = 1'b1;

            if (bad) status <= REJECT;
            else if (ovf) status <= GUARD;
            else begin
                for (m = 0; m < 16; m = m + 1) coeffs[m*W +: W] <= t[m][W-1:0];
                k <= kn[7:0];
                gates_done <= gates_done + 16'd1;
            end
        end
    end
endmodule
