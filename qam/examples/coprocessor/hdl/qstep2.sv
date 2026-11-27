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
// Aufbau: qgate2 (Gatter) und qnorm2 (Kuerzen, Guard) sind kombinatorisch und werden auch von der
// Pipeline-Fassung qstep2p benutzt; hier liegen beide in einem Takt.
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
    localparam [1:0] CONTINUE = 0, GUARD = 1, REJECT = 2, STEP_LIMIT = 3;
    localparam integer TW = W + 2;  // Arbeitsbreite mit Reserve fuer Summen

    wire [16*TW-1:0] o_flat;
    wire [8:0] kn;
    wire bad, ovf;
    wire [16*W-1:0] coeffs_n;
    wire [7:0] k_n;

    wire signed [TW-1:0] maxv, minv;
    qguard_limits #(.TW(TW)) limits (.w_eff(w_eff), .maxv(maxv), .minv(minv));

    qgate2 #(.W(W), .TW(TW)) gate (
        .coeffs(coeffs), .k(k), .opcode(opcode), .target(target), .allow(allow),
        .o_flat(o_flat), .kn(kn), .bad(bad)
    );
    qnorm2 #(.W(W), .TW(TW)) norm (
        .o_flat(o_flat), .kn_in(kn), .reduce_en(reduce_en), .maxv(maxv), .minv(minv), .k_max(k_max),
        .coeffs(coeffs_n), .k(k_n), .ovf(ovf)
    );

    always @(posedge clk) begin
        if (rst || load) begin
            coeffs <= {{(16*W-1){1'b0}}, 1'b1};
            k <= 8'd0;
            status <= CONTINUE;
            gates_done <= 16'd0;
        end else if (op_valid && status == CONTINUE) begin
            if (budget != 16'd0 && gates_done >= budget) status <= STEP_LIMIT;
            else if (bad) status <= REJECT;
            else if (ovf) status <= GUARD;
            else begin
                coeffs <= coeffs_n;
                k <= k_n;
                gates_done <= gates_done + 16'd1;
            end
        end
    end
endmodule
