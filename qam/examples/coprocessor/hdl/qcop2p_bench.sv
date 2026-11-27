`timescale 1ns/1ps
// Messrahmen der Pipeline-Fassung (wie qcop2_bench.sv) nur fuer Synthese und Platzierung (Takt und Flaeche): wenige Pins, damit der Kern in ein
// FPGA-Gehaeuse passt. Konfigurationsdaten kommen seriell (cfg_sdi), alle Ausgaben werden zu einem
// Pruefbit verknuepft, damit keine Logik wegoptimiert wird. Kein Bestandteil des Rechenwegs.
module qcop2p_bench #(
    parameter integer W = 16,
    parameter integer CTX = 4,
    parameter integer CB = CTX > 1 ? $clog2(CTX) : 1
) (
    input wire clk,
    input wire rst,
    input wire load,
    input wire op_valid,
    input wire [3:0] opcode,
    input wire target,
    input wire cfg_shift,
    input wire cfg_sdi,
    input wire cfg_we,
    input wire [4:0] cfg_addr,
    input wire [CB-1:0] ctx,
    output reg check_q,
    output reg [1:0] status_qq
);
    reg [31:0] sreg;
    reg check;
    reg [1:0] status_q;
    reg rst_q, load_q, op_valid_q, target_q, cfg_we_q;
    reg [3:0] opcode_q;
    reg [4:0] cfg_addr_q;
    reg [CB-1:0] ctx_q;
    wire [CTX-1:0] ready;
    wire [31:0] cfg_rdata;
    wire [16*W-1:0] coeffs;
    wire [7:0] k;
    wire [1:0] status;
    wire [15:0] gates_done;
    wire [16*32-1:0] phys;

    always @(posedge clk) begin
        if (cfg_shift) sreg <= {sreg[30:0], cfg_sdi};
        {rst_q, load_q, op_valid_q, target_q, cfg_we_q, opcode_q, cfg_addr_q, ctx_q} <=
            {rst, load, op_valid, target, cfg_we, opcode, cfg_addr, ctx};
        check <= ^coeffs ^ ^k ^ ^gates_done ^ ^phys ^ ^cfg_rdata ^ ^ready;
        status_q <= status;
        // zweite Registerstufe, damit der Weg zum Pin nicht in die Messung des Kerns eingeht
        check_q <= check;
        status_qq <= status_q;
    end

    qcop2p_top #(.W(W), .CTX(CTX)) dut (
        .clk(clk), .rst(rst_q), .load(load_q), .load_ctx(ctx_q), .op_valid(op_valid_q), .op_ctx(ctx_q),
        .rd_ctx(ctx_q), .ready(ready), .opcode(opcode_q),
        .target(target_q), .cfg_we(cfg_we_q), .cfg_addr(cfg_addr_q), .cfg_wdata(sreg),
        .cfg_rdata(cfg_rdata), .coeffs(coeffs), .k(k), .status(status), .gates_done(gates_done),
        .phys(phys)
    );
endmodule
