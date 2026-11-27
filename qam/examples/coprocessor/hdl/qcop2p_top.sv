`timescale 1ns/1ps
// Oberste Ebene der Pipeline-Fassung: qcfg (gemeinsame Konfiguration) + qstep2p mit CTX Kontexten.
// Jedes load (gleich welcher Kontext) macht die zuletzt geschriebenen Werte aktiv.
module qcop2p_top #(
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
    input wire cfg_we,
    input wire [4:0] cfg_addr,
    input wire [31:0] cfg_wdata,
    output wire [31:0] cfg_rdata,
    output wire [CTX-1:0] ready,
    input wire [CB-1:0] rd_ctx,
    output wire [16*W-1:0] coeffs,
    output wire [7:0] k,
    output wire [1:0] status,
    output wire [15:0] gates_done,
    output wire [16*32-1:0] phys
);
    wire [15:0] allow, budget;
    wire [5:0] w_eff;
    wire [7:0] k_max;
    wire [1:0] reduce_en;

    qcfg #(.W(W)) cfg (
        .clk(clk), .rst(rst), .commit(load), .cfg_we(cfg_we), .cfg_addr(cfg_addr),
        .cfg_wdata(cfg_wdata), .cfg_rdata(cfg_rdata), .allow(allow), .w_eff(w_eff),
        .k_max(k_max), .budget(budget), .reduce_en(reduce_en), .phys(phys)
    );

    qstep2p #(.W(W), .CTX(CTX)) core (
        .clk(clk), .rst(rst), .load(load), .load_ctx(load_ctx), .op_valid(op_valid), .op_ctx(op_ctx),
        .opcode(opcode), .target(target), .allow(allow), .w_eff(w_eff), .k_max(k_max), .budget(budget),
        .reduce_en(reduce_en), .ready(ready), .rd_ctx(rd_ctx), .coeffs(coeffs), .k(k), .status(status),
        .gates_done(gates_done)
    );
endmodule
