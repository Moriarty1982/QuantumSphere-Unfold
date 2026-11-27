`timescale 1ns/1ps
// Testbench der Selbstjustierung (qcop2t_top). Zeilen der Eingabe:
//   T adr wert   Register des Rueckkopplungswerks schreiben (wert dezimal, auch negativ)
//   S ctrl       Lauf starten (CTRL), warten bis fertig, Ausgabe
//                "tune status s x X iters n dl D dp P adj A"
//   C adr wert   Konfigurationsregister schreiben          R adr   lesen, Ausgabe "cfg adr wert"
module qcop2t_tb;
    parameter integer W = 16;
    reg clk = 0, rst = 1, load = 0, op_valid = 0, target = 0, cfg_we = 0, tune_we = 0;
    reg [3:0] opcode = 0, tune_addr = 0;
    reg [4:0] cfg_addr = 0;
    reg [31:0] cfg_wdata = 0, tune_wdata = 0;
    wire [31:0] cfg_rdata, tune_rdata;
    wire [16*W-1:0] coeffs;
    wire [7:0] k;
    wire [1:0] status;
    wire [15:0] gates_done, adjusted;
    wire [16*32-1:0] phys;
    integer fd, rc, adr, guard;
    reg signed [63:0] val;
    reg [31:0] st, xx, it, dl, dp;
    reg [8*8-1:0] cmd;
    reg [8*512-1:0] path;

    qcop2t_top #(.W(W)) dut (
        .clk(clk), .rst(rst), .load(load), .op_valid(op_valid), .opcode(opcode), .target(target),
        .cfg_we(cfg_we), .cfg_addr(cfg_addr), .cfg_wdata(cfg_wdata), .cfg_rdata(cfg_rdata),
        .tune_we(tune_we), .tune_addr(tune_addr), .tune_wdata(tune_wdata), .tune_rdata(tune_rdata),
        .coeffs(coeffs), .k(k), .status(status), .gates_done(gates_done), .phys(phys), .adjusted(adjusted)
    );

    always #5 clk = ~clk;

    task rd(input [3:0] a, output [31:0] v);
        begin tune_addr = a; #1 v = tune_rdata; end
    endtask

    initial begin
        if (!$value$plusargs("stim=%s", path)) begin
            $display("ERROR missing +stim");
            $finish;
        end
        fd = $fopen(path, "r");
        @(negedge clk) rst = 0;
        while (!$feof(fd)) begin
            rc = $fscanf(fd, "%s", cmd);
            if (rc == 1) begin
                if (cmd == "T") begin
                    rc = $fscanf(fd, "%d %d", adr, val);
                    tune_addr = adr; tune_wdata = val[31:0]; tune_we = 1;
                    @(negedge clk) tune_we = 0;
                end else if (cmd == "S") begin
                    rc = $fscanf(fd, "%d", val);
                    tune_addr = 0; tune_wdata = val[31:0]; tune_we = 1;
                    @(negedge clk) tune_we = 0;
                    guard = 0;
                    rd(9, st);
                    while (st[2] && guard < 70000) begin
                        @(negedge clk); guard = guard + 1; rd(9, st);
                    end
                    @(negedge clk); @(negedge clk);   // Rueckschreiben abwarten
                    rd(9, st); rd(10, xx); rd(11, it); rd(12, dl); rd(13, dp);
                    $display("tune status %0d x %0d iters %0d dl %0d dp %0d adj %0d", st[1:0], $signed(xx), it,
                             dl, dp, adjusted);
                end else if (cmd == "C") begin
                    rc = $fscanf(fd, "%d %d", adr, val);
                    cfg_addr = adr; cfg_wdata = val[31:0]; cfg_we = 1;
                    @(negedge clk) cfg_we = 0;
                end else if (cmd == "R") begin
                    rc = $fscanf(fd, "%d", adr);
                    cfg_addr = adr; #1;
                    $display("cfg %0d %0d adj %0d", adr, $signed(cfg_rdata), adjusted);
                    @(negedge clk);
                end
            end
        end
        $fclose(fd);
        $finish;
    end
endmodule
