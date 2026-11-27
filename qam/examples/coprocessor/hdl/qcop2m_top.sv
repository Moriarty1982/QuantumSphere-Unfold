`timescale 1ns/1ps
// Parallele Rechenwerke je Band: LANES Pipelines (qstep2p) mit je CTX Kontexten, zusammen PARTS = LANES*CTX
// Laeufe. Band p des Bandregisters (qband) gehoert zu Spur p / CTX, Kontext p mod CTX. Jede Spur nimmt je Takt
// ein Gatter an (eigener Eingang je Spur), zusammen also bis zu LANES Gatter je Takt.
// Gatter fuer ein Band, das im Bandregister nicht gueltig ist (oder solange die Aufteilung ungueltig ist),
// werden verworfen und in blocked gezaehlt. Konfiguration (qcfg) gemeinsam; jedes load macht sie aktiv.
module qcop2m_top #(
    parameter integer W = 16,
    parameter integer LANES = 2,
    parameter integer CTX = 4,
    parameter integer PARTS = LANES * CTX,
    parameter integer CB = CTX > 1 ? $clog2(CTX) : 1,
    parameter integer PB = PARTS > 1 ? $clog2(PARTS) : 1
) (
    input wire clk,
    input wire rst,
    // Konfiguration
    input wire cfg_we,
    input wire [4:0] cfg_addr,
    input wire [31:0] cfg_wdata,
    output wire [31:0] cfg_rdata,
    // Bandregister
    input wire band_valid,
    input wire [3:0] band_cmd,
    input wire [7:0] band_a,
    input wire [15:0] band_b,
    input wire [127:0] band_d,
    output wire band_ok,
    output wire [127:0] band_data,
    output wire layout_ok,
    output wire full,
    // Laeufe
    input wire load,
    input wire [PB-1:0] load_part,
    input wire [LANES-1:0] op_valid,
    input wire [LANES*CB-1:0] op_ctx,
    input wire [LANES*4-1:0] opcode,
    input wire [LANES-1:0] target,
    output wire [PARTS-1:0] ready,
    output reg [31:0] blocked,
    input wire [PB-1:0] rd_part,
    output wire [16*W-1:0] coeffs,
    output wire [7:0] k,
    output wire [1:0] status,
    output wire [15:0] gates_done,
    output wire [16*32-1:0] phys
);
    wire [15:0] allow, budget;
    wire [5:0] w_eff;
    wire [7:0] k_max;
    wire reduce_en;
    wire [PARTS-1:0] part_valid;

    qcfg #(.W(W)) cfg (
        .clk(clk), .rst(rst), .commit(load), .cfg_we(cfg_we), .cfg_addr(cfg_addr),
        .cfg_wdata(cfg_wdata), .cfg_rdata(cfg_rdata), .allow(allow), .w_eff(w_eff),
        .k_max(k_max), .budget(budget), .reduce_en(reduce_en), .phys(phys)
    );

    qband #(.CELLS(128), .PARTS(PARTS), .BUSW(128)) band (
        .clk(clk), .rst(rst), .cmd_valid(band_valid), .cmd(band_cmd), .a(band_a), .b(band_b), .d(band_d),
        .rsp_ok(band_ok), .rsp_data(band_data), .layout_ok(layout_ok), .full(full),
        .part_valid(part_valid), .part_base(), .part_order()
    );

    wire [LANES*16*W-1:0] l_coeffs;
    wire [LANES*8-1:0] l_k;
    wire [LANES*2-1:0] l_status;
    wire [LANES*16-1:0] l_done;
    wire [LANES-1:0] enabled;
    wire [CB-1:0] rd_ctx = rd_part % CTX;
    wire [CB-1:0] load_ctx = load_part % CTX;
    wire [PB-1:0] rd_lane = rd_part / CTX;

    genvar g;
    generate
        for (g = 0; g < LANES; g = g + 1) begin : lane
            wire [CB-1:0] ctx = op_ctx[g*CB +: CB];
            assign enabled[g] = layout_ok && part_valid[g * CTX + ctx];
            qstep2p #(.W(W), .CTX(CTX)) core (
                .clk(clk), .rst(rst), .load(load && load_part / CTX == g), .load_ctx(load_ctx),
                .op_valid(op_valid[g] && enabled[g]), .op_ctx(ctx), .opcode(opcode[g*4 +: 4]),
                .target(target[g]), .allow(allow), .w_eff(w_eff), .k_max(k_max), .budget(budget),
                .reduce_en(reduce_en), .ready(ready[g*CTX +: CTX]), .rd_ctx(rd_ctx),
                .coeffs(l_coeffs[g*16*W +: 16*W]), .k(l_k[g*8 +: 8]), .status(l_status[g*2 +: 2]),
                .gates_done(l_done[g*16 +: 16])
            );
        end
    endgenerate

    assign coeffs = l_coeffs[rd_lane*16*W +: 16*W];
    assign k = l_k[rd_lane*8 +: 8];
    assign status = l_status[rd_lane*2 +: 2];
    assign gates_done = l_done[rd_lane*16 +: 16];

    integer n;
    reg [7:0] nblk;
    always @(*) begin
        nblk = 8'd0;
        for (n = 0; n < LANES; n = n + 1) if (op_valid[n] && !enabled[n]) nblk = nblk + 8'd1;
    end
    always @(posedge clk) begin
        if (rst) blocked <= 32'd0;
        else blocked <= blocked + nblk;
    end
endmodule
