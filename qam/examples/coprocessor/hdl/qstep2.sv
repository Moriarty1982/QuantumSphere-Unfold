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
//   0 continue    Gatter ausgefuehrt
//   1 guard       Ergebnis passt nicht in w_eff Bit oder k > k_max; Zustand bleibt, Einheit stoppt
//   2 reject      unbekannter oder nicht erlaubter Opcode; Zustand bleibt, Einheit stoppt
//   3 step_limit  budget Gatter ausgefuehrt (budget > 0); Zustand bleibt, Einheit stoppt
//
// Die Laufzeitwerte allow, w_eff, k_max, budget und reduce_en kommen aus qcfg.sv. Mit den
// Vorgaben (alle Opcodes, w_eff = W, k_max = 255, budget = 0, Kuerzen an) rechnet die Einheit
// genau wie die erste Fassung vom 25.11.2026.
//
// Synthesefest (27.11.2026): alle Schleifen haben feste Grenzen; die Phase w^r ist ein
// Umsortieren der vier Koeffizienten mit Vorzeichenwechsel, also reine Verdrahtung.
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
    // Laufzeitwerte (siehe qcfg.sv)
    input wire [15:0] allow,
    input wire [5:0] w_eff,
    input wire [7:0] k_max,
    input wire [15:0] budget,
    input wire reduce_en,
    output reg [16*W-1:0] coeffs,
    output reg [7:0] k,
    output reg [1:0] status,
    output reg [15:0] gates_done
);
    localparam [3:0] OP_NOP = 0, OP_X = 1, OP_Z = 2, OP_S = 3, OP_SDG = 4,
                     OP_T = 5, OP_TDG = 6, OP_H = 7, OP_CX = 8;
    localparam [1:0] CONTINUE = 0, GUARD = 1, REJECT = 2, STEP_LIMIT = 3;
    localparam integer TW = W + 2;  // Arbeitsbreite mit Reserve fuer Summen

    reg signed [TW-1:0] t [0:15];
    reg signed [TW-1:0] o [0:15];
    reg signed [TW-1:0] maxv, minv;
    reg [8:0] kn;
    reg bad, ovf, all_even;
    reg [2:0] rot;
    reg [1:0] b;
    integer m, i, j, d;

    always @(posedge clk) begin
        if (rst || load) begin
            coeffs <= {{(16*W-1){1'b0}}, 1'b1};
            k <= 8'd0;
            status <= CONTINUE;
            gates_done <= 16'd0;
        end else if (op_valid && status == CONTINUE) begin
            for (m = 0; m < 16; m = m + 1) begin
                t[m] = $signed(coeffs[m*W +: W]);
                o[m] = t[m];
            end
            kn = {1'b0, k};
            bad = (opcode > OP_CX) || !allow[opcode];
            ovf = 1'b0;
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
                    // w^r * a: Koeffizient j kommt von (j - r) mod 4, negiert bei genau einem
                    // Umlauf (w^4 = -1).
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

            // Kuerzen: sind alle Koeffizienten gerade und k >= 2, durch 2 teilen.
            all_even = 1'b1;
            for (m = 0; m < 16; m = m + 1) if (o[m][0]) all_even = 1'b0;
            if (reduce_en && all_even && kn >= 2) begin
                for (m = 0; m < 16; m = m + 1) o[m] = o[m] >>> 1;
                kn = kn - 9'd2;
            end

            maxv = ({{(TW-1){1'b0}}, 1'b1} <<< (w_eff - 1)) - 1;
            minv = -maxv - 1;
            for (m = 0; m < 16; m = m + 1) if (o[m] > maxv || o[m] < minv) ovf = 1'b1;
            if (kn > {1'b0, k_max}) ovf = 1'b1;

            if (budget != 16'd0 && gates_done >= budget) status <= STEP_LIMIT;
            else if (bad) status <= REJECT;
            else if (ovf) status <= GUARD;
            else begin
                for (m = 0; m < 16; m = m + 1) coeffs[m*W +: W] <= o[m][W-1:0];
                k <= kn[7:0];
                gates_done <= gates_done + 16'd1;
            end
        end
    end
endmodule
