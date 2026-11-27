`timescale 1ns/1ps
// Messrahmen der parallelen Rechenwerke (wie qcop2_bench.sv) nur fuer Synthese und Platzierung: serielle
// Eingabe fuer Konfigurations- und Banddaten, alle Ausgaben zu einem Pruefbit verknuepft, Pins doppelt registriert.
module qcop2m_bench #(
    parameter integer W = 16,
    parameter integer LANES = 2,
    parameter integer CTX = 4,
    parameter integer PARTS = LANES * CTX,
    parameter integer CB = CTX > 1 ? $clog2(CTX) : 1,
    parameter integer PB = PARTS > 1 ? $clog2(PARTS) : 1
) (
    input wire clk,
    input wire rst,
    input wire sdi,
    input wire shift,
    input wire cfg_we,
    input wire band_valid,
    input wire load,
    input wire [LANES-1:0] op_valid,
    input wire [3:0] sel,
    output reg check_q,
    output reg [1:0] status_qq
);
    reg [255:0] sreg;
    reg rst_q, cfg_we_q, band_valid_q, load_q;
    reg [LANES-1:0] op_valid_q;
    reg check;
    reg [1:0] status_q;
    wire [31:0] cfg_rdata, blocked;
    wire band_ok, layout_ok, full;
    wire [127:0] band_data;
    wire [PARTS-1:0] ready;
    wire [16*W-1:0] coeffs;
    wire [7:0] k;
    wire [1:0] status;
    wire [15:0] gates_done;
    wire [16*32-1:0] phys;

    always @(posedge clk) begin
        if (shift) sreg <= {sreg[254:0], sdi};
        {rst_q, cfg_we_q, band_valid_q, load_q, op_valid_q} <= {rst, cfg_we, band_valid, load, op_valid};
        check <= ^coeffs ^ ^k ^ ^gates_done ^ ^phys ^ ^cfg_rdata ^ ^blocked ^ ^band_data ^ band_ok ^ layout_ok
                 ^ full ^ ^ready;
        status_q <= status;
        check_q <= check;
        status_qq <= status_q;
    end

    qcop2m_top #(.W(W), .LANES(LANES), .CTX(CTX)) dut (
        .clk(clk), .rst(rst_q), .cfg_we(cfg_we_q), .cfg_addr(sreg[4:0]), .cfg_wdata(sreg[36:5]),
        .cfg_rdata(cfg_rdata), .band_valid(band_valid_q), .band_cmd(sreg[40:37]), .band_a(sreg[48:41]),
        .band_b(sreg[64:49]), .band_d(sreg[192:65]), .band_ok(band_ok), .band_data(band_data),
        .layout_ok(layout_ok), .full(full), .band_busy(), .load(load_q), .load_part(sreg[200:193]), .op_valid(op_valid_q),
        .op_ctx(sreg[193 +: LANES*CB]), .opcode(sreg[210 +: LANES*4]), .target(sreg[240 +: LANES]),
        .ready(ready), .blocked(blocked), .rd_part(sreg[248 +: PB]), .coeffs(coeffs), .k(k), .status(status),
        .gates_done(gates_done), .phys(phys)
    );
endmodule
