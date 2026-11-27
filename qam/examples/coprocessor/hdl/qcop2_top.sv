`timescale 1ns/1ps
// Oberste Ebene der Baustufe 0: Konfigurationsregister (qcfg) und Rechenkern (qstep2).
// load startet einen Lauf: Zustand |00> und die zuletzt geschriebenen Werte werden aktiv.
// Weitere Rechenwerke (Band, Messung, Drehung) haengen spaeter an derselben Konfiguration;
// die Bank phys (0x10..0x1F) liegt dafuer schon als Ausgang an.
module qcop2_top #(
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

    qstep2 #(.W(W)) core (
        .clk(clk), .rst(rst), .load(load), .op_valid(op_valid), .opcode(opcode),
        .target(target), .allow(allow), .w_eff(w_eff), .k_max(k_max), .budget(budget),
        .reduce_en(reduce_en), .coeffs(coeffs), .k(k), .status(status), .gates_done(gates_done)
    );
endmodule
