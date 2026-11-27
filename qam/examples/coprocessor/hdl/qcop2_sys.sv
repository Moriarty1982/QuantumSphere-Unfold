`timescale 1ns/1ps
// System der Baustufe 0 mit Boot-Monitor: Programmspeicher (synchron gelesen, vom Host beschreibbar),
// qboot und qcop2_top. Der Host schreibt ein QIMG-Abbild ueber prog_we/prog_addr/prog_wdata und gibt start;
// bei jedem EMIT liegt emit = 1 fuer einen Takt an, dann sind coeffs/k/status/gates_done gueltig.
// Spaeter kann ein Soft-Core (z. B. RISC-V) denselben Programmspeicher und dieselben Register bedienen.
module qcop2_sys #(
    parameter integer W = 16,
    parameter integer AW = 10
) (
    input wire clk,
    input wire rst,
    input wire prog_we,
    input wire [AW-1:0] prog_addr,
    input wire [31:0] prog_wdata,
    input wire start,
    output wire emit,
    output wire [1:0] boot_status,
    output wire [15:0] pc,
    output wire [16*W-1:0] coeffs,
    output wire [7:0] k,
    output wire [1:0] status,
    output wire [15:0] gates_done,
    output wire [16*32-1:0] phys
);
    reg [31:0] mem [0:(1<<AW)-1];
    reg [31:0] mem_data;
    wire [AW-1:0] mem_addr;

    always @(posedge clk) begin
        if (prog_we) mem[prog_addr] <= prog_wdata;
        mem_data <= mem[mem_addr];
    end

    wire load, op_valid, target, cfg_we;
    wire [3:0] opcode;
    wire [4:0] cfg_addr;
    wire [31:0] cfg_wdata, cfg_rdata;

    qboot #(.AW(AW)) boot (
        .clk(clk), .rst(rst), .start(start), .mem_addr(mem_addr), .mem_data(mem_data),
        .load(load), .op_valid(op_valid), .opcode(opcode), .target(target), .cfg_we(cfg_we),
        .cfg_addr(cfg_addr), .cfg_wdata(cfg_wdata), .emit(emit), .boot_status(boot_status), .pc_out(pc)
    );

    qcop2_top #(.W(W)) cop (
        .clk(clk), .rst(rst), .load(load), .op_valid(op_valid), .opcode(opcode), .target(target),
        .cfg_we(cfg_we), .cfg_addr(cfg_addr), .cfg_wdata(cfg_wdata), .cfg_rdata(cfg_rdata),
        .coeffs(coeffs), .k(k), .status(status), .gates_done(gates_done), .phys(phys)
    );
endmodule
