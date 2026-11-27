`timescale 1ns/1ps
// Selbstueberwachter Kern: qcop2_top-Aufbau (qcfg + qstep2) mit Normwaechter qmon.
// Ist der Waechter an (flags Bit 2), wird nach jedem Takt geprueft, ob der Zustand normiert ist (sum P = 2^k,
// sum Q = 0). Bei einer Verletzung haelt der Kern sofort an: Das naechste Gatter wird nicht mehr angenommen,
// fault bleibt gesetzt bis zum naechsten load, und faults zaehlt die Ereignisse.
// inject_mask (nur fuer Pruefungen) wird auf den Eingang des Waechters gelegt, um einen gekippten Wert
// nachzubilden; im Betrieb ist er 0.
module qcop2s_top #(
    parameter integer W = 16
) (
    input wire clk,
    input wire rst,
    input wire load,
    input wire op_valid,
    input wire [3:0] opcode,
    input wire target,
    input wire cfg_we,
    input wire [4:0] cfg_addr,
    input wire [31:0] cfg_wdata,
    output wire [31:0] cfg_rdata,
    input wire [16*W-1:0] inject_mask,
    output wire [16*W-1:0] coeffs,
    output wire [7:0] k,
    output wire [1:0] status,
    output wire [15:0] gates_done,
    output reg fault,
    output reg [15:0] faults,
    output wire [16*32-1:0] phys
);
    wire [15:0] allow, budget;
    wire [5:0] w_eff;
    wire [7:0] k_max;
    wire [1:0] reduce_en;
    wire mon_en, norm_ok;

    qcfg #(.W(W)) cfg (
        .clk(clk), .rst(rst), .commit(load), .cfg_we(cfg_we), .cfg_addr(cfg_addr),
        .cfg_wdata(cfg_wdata), .cfg_rdata(cfg_rdata), .allow(allow), .w_eff(w_eff),
        .k_max(k_max), .budget(budget), .reduce_en(reduce_en), .mon_en(mon_en), .phys(phys)
    );

    qmon #(.W(W)) mon (.coeffs(coeffs ^ inject_mask), .k(k), .ok(norm_ok), .psum(), .qsum());

    wire violation = mon_en && !norm_ok && !load;
    wire halt = fault || violation;

    qstep2 #(.W(W)) core (
        .clk(clk), .rst(rst), .load(load), .op_valid(op_valid && !halt), .opcode(opcode),
        .target(target), .allow(allow), .w_eff(w_eff), .k_max(k_max), .budget(budget),
        .reduce_en(reduce_en), .coeffs(coeffs), .k(k), .status(status), .gates_done(gates_done)
    );

    always @(posedge clk) begin
        if (rst) begin
            fault <= 1'b0;
            faults <= 16'd0;
        end else begin
            if (load) fault <= 1'b0;
            else if (violation) fault <= 1'b1;
            if (violation && !fault) faults <= faults + 16'd1;
        end
    end
endmodule
