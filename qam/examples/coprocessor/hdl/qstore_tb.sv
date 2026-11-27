`timescale 1ns/1ps
// Testbench des Zustandsspeichers. Je Eingabezeile "X cmd a b rec" (rec hexadezimal) ein Befehl; je Befehl
// eine Ausgabezeile "R ok slot hash dedup repaired bad audit used rec" (hash, audit, rec hexadezimal).
module qstore_tb;
    parameter integer RW = 264;
    reg clk = 0, rst = 1, cmd_valid = 0;
    reg [2:0] cmd = 0;
    reg [7:0] a = 0;
    reg [15:0] b = 0;
    reg [RW-1:0] rec_in = 0;
    wire rsp_ok, dedup, repaired, bad;
    wire [7:0] rsp_slot, used;
    wire [31:0] rsp_hash, audit;
    wire [RW-1:0] rec_out;
    integer fd, rc, ci, ai, bi;
    reg [RW-1:0] ri;
    reg [8*8-1:0] tag;
    reg [8*512-1:0] path;

    qstore #(.RW(RW)) dut (
        .clk(clk), .rst(rst), .cmd_valid(cmd_valid), .cmd(cmd), .a(a), .b(b), .rec_in(rec_in), .rsp_ok(rsp_ok),
        .rsp_slot(rsp_slot), .rsp_hash(rsp_hash), .rec_out(rec_out), .dedup(dedup), .repaired(repaired),
        .bad(bad), .audit(audit), .used(used)
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
            rc = $fscanf(fd, "%s %d %d %d %h", tag, ci, ai, bi, ri);
            if (rc == 5) begin
                cmd = ci; a = ai; b = bi; rec_in = ri; cmd_valid = 1;
                @(negedge clk) cmd_valid = 0;
                $display("R %0d %0d %h %0d %0d %0d %h %0d %h", rsp_ok, rsp_slot, rsp_hash, dedup, repaired, bad,
                         audit, used, rec_out);
            end
        end
        $fclose(fd);
        $finish;
    end
endmodule
