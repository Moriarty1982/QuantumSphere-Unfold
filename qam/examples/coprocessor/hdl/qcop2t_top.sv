`timescale 1ns/1ps
// Kern mit Selbstjustierung: qcop2_top-Aufbau (qcfg + qstep2) und Rueckkopplungswerk qtune.
// Der Host stellt qtune ueber einen eigenen kleinen Bus ein (tune_we/tune_addr/tune_wdata, Lesen tune_rdata):
//   0  CTRL     Schreiben: Bit 0 Start, Bit 1 Modus (0 FIX, 1 BISECT), Bit 2 Rueckschreiben,
//               Bit 7:4 Zielregister n der Bank (0x10 + n), Bit 8 Abbruch
//   1  C0   2  C1   3  C2   4  X0 (lo)   5  HI   6  TARGET   7  TOL   8  MAX_ITER     (alle Q2.30 ausser 7, 8)
//   9  STATUS   lesen: {busy, letzter Status[1:0]} in Bit 2:0
//   10 X        11 ITERS   12 D_LAST   13 D_PREV
//   14 ADJUSTED lesen: Bit n = Register 0x10 + n ist angepasst (von qtune geschrieben, nicht gesetzt)
// Mit Rueckschreiben schreibt das Werk sein Ergebnis bei Konvergenz in das live-Register 0x10 + n (wirksam ab dem
// naechsten load, wie jeder Wert) und setzt dessen Bit in ADJUSTED. Schreibt der Host das Register selbst, wird
// das Bit wieder geloescht: der Wert ist dann gesetzt. Hostzugriffe auf qcfg haben Vorrang; das Rueckschreiben
// wartet, bis der Host nicht schreibt.
module qcop2t_top #(
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
    input wire tune_we,
    input wire [3:0] tune_addr,
    input wire [31:0] tune_wdata,
    output reg [31:0] tune_rdata,
    output wire [16*W-1:0] coeffs,
    output wire [7:0] k,
    output wire [1:0] status,
    output wire [15:0] gates_done,
    output wire [16*32-1:0] phys,
    output reg [15:0] adjusted
);
    reg [31:0] treg [1:8];
    reg mode_r, wb_r, pend;
    reg [3:0] dest_r;
    reg signed [31:0] res;
    wire start = tune_we && tune_addr == 4'd0 && tune_wdata[0];
    wire abort = tune_we && tune_addr == 4'd0 && tune_wdata[8];
    wire t_busy, t_done;
    wire [1:0] t_status;
    wire signed [31:0] t_x;
    wire [15:0] t_iters;
    wire [31:0] t_dl, t_dp;
    integer n;

    qtune tune (
        .clk(clk), .rst(rst), .start(start), .abort(abort), .mode(start ? tune_wdata[1] : mode_r),
        .c0(treg[1]), .c1(treg[2]), .c2(treg[3]), .x0(treg[4]), .hi(treg[5]), .target(treg[6]), .tol(treg[7]),
        .max_iter(treg[8][15:0]), .busy(t_busy), .done(t_done), .status(t_status), .x(t_x), .iters(t_iters),
        .d_last(t_dl), .d_prev(t_dp)
    );

    // Rueckschreiben ueber den Schreibweg von qcfg (Host hat Vorrang)
    wire wb_go = pend && !cfg_we;
    wire we_eff = cfg_we || wb_go;
    wire [4:0] addr_eff = cfg_we ? cfg_addr : {1'b1, dest_r};
    wire [31:0] data_eff = cfg_we ? cfg_wdata : res;

    qcop2_top #(.W(W)) core (
        .clk(clk), .rst(rst), .load(load), .op_valid(op_valid), .opcode(opcode), .target(target),
        .cfg_we(we_eff), .cfg_addr(addr_eff), .cfg_wdata(data_eff), .cfg_rdata(cfg_rdata), .coeffs(coeffs),
        .k(k), .status(status), .gates_done(gates_done), .phys(phys)
    );

    always @(posedge clk) begin
        if (rst) begin
            for (n = 1; n <= 8; n = n + 1) treg[n] <= 32'd0;
            mode_r <= 1'b0;
            wb_r <= 1'b0;
            dest_r <= 4'd0;
            pend <= 1'b0;
            adjusted <= 16'd0;
        end else begin
            if (tune_we && tune_addr >= 4'd1 && tune_addr <= 4'd8) treg[tune_addr] <= tune_wdata;
            if (start && !t_busy) begin
                mode_r <= tune_wdata[1];
                wb_r <= tune_wdata[2];
                dest_r <= tune_wdata[7:4];
            end
            if (t_done && t_status == 2'd0 && wb_r) begin
                pend <= 1'b1;
                res <= t_x;
            end else if (wb_go) begin
                pend <= 1'b0;
                adjusted[dest_r] <= 1'b1;
            end
            if (cfg_we && cfg_addr[4]) adjusted[cfg_addr[3:0]] <= 1'b0;
            if (cfg_we && cfg_addr == {1'b1, dest_r}) pend <= 1'b0;     // Host setzt das Ziel selbst: verwerfen
        end
    end

    always @(*) begin
        case (tune_addr)
            4'd9: tune_rdata = {29'd0, t_busy, t_status};
            4'd10: tune_rdata = t_x;
            4'd11: tune_rdata = {16'd0, t_iters};
            4'd12: tune_rdata = t_dl;
            4'd13: tune_rdata = t_dp;
            4'd14: tune_rdata = {16'd0, adjusted};
            default: tune_rdata = (tune_addr >= 4'd1 && tune_addr <= 4'd8) ? treg[tune_addr] : 32'd0;
        endcase
    end
endmodule
