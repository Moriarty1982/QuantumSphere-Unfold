`timescale 1ns/1ps
// Testbench des Bandregisters. Je Eingabezeile "X cmd a b d" (d hexadezimal) ein Befehl; je Befehl eine
// Ausgabezeile "R ok daten layout_ok full" (daten hexadezimal).
module qband_tb;
    parameter integer CELLS = 128;
    parameter integer PARTS = 16;
    parameter integer CW = 1;
    parameter integer BUSW = 128;
    reg clk = 0, rst = 1, cmd_valid = 0;
    reg [3:0] cmd = 0;
    reg [7:0] a = 0;
    reg [15:0] b = 0;
    reg [BUSW-1:0] d = 0;
    wire rsp_ok, layout_ok, full;
    wire [BUSW-1:0] rsp_data;
    wire [PARTS-1:0] part_valid;
    wire [PARTS*$clog2(CELLS)-1:0] part_base;
    wire [PARTS*4-1:0] part_order;
    integer fd, rc, ci, ai, bi;
    reg [BUSW-1:0] di;
    reg [8*8-1:0] tag;
    reg [8*512-1:0] path;

    qband #(.CELLS(CELLS), .PARTS(PARTS), .CW(CW), .BUSW(BUSW)) dut (
        .clk(clk), .rst(rst), .cmd_valid(cmd_valid), .cmd(cmd), .a(a), .b(b), .d(d), .rsp_ok(rsp_ok),
        .rsp_data(rsp_data), .layout_ok(layout_ok), .full(full), .part_valid(part_valid),
        .part_base(part_base), .part_order(part_order)
    );

    always #5 clk = ~clk;

    initial begin
        if (!$value$plusargs("stim=%s", path)) begin
            $display("ERROR missing +stim");
            $finish;
        end
        fd = $fopen(path, "r");
        @(negedge clk) rst = 0;
        while (!$feof(fd)) begin
            rc = $fscanf(fd, "%s %d %d %d %h", tag, ci, ai, bi, di);
            if (rc == 5) begin
                cmd = ci; a = ai; b = bi; d = di; cmd_valid = 1;
                @(negedge clk) cmd_valid = 0;
                $display("R %0d %h %0d %0d", rsp_ok, rsp_data, layout_ok, full);
            end
        end
        $fclose(fd);
        $finish;
    end
endmodule
