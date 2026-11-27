`timescale 1ns/1ps
// Laedt je Abbild eine Hexdatei (ein 32-Bit-Wort je Zeile) in den Programmspeicher, startet den Monitor und
// schreibt bei jedem EMIT eine Zeile wie qstep2_tb ("case ..."). +imgs=DATEI listet die Hexdateien.
module qboot_tb;
    parameter integer W = 16;
    parameter integer AW = 10;
    reg clk = 0, rst = 1, prog_we = 0, start = 0;
    reg [AW-1:0] prog_addr = 0;
    reg [31:0] prog_wdata = 0;
    wire emit;
    wire [1:0] boot_status, status;
    wire [15:0] pc, gates_done;
    wire [16*W-1:0] coeffs;
    wire [7:0] k;
    wire [16*32-1:0] phys;
    integer list, img, rc, m, cases, cycles, words;
    reg [31:0] word;
    reg [8*512-1:0] path, imgpath;

    qcop2_sys #(.W(W), .AW(AW)) dut (
        .clk(clk), .rst(rst), .prog_we(prog_we), .prog_addr(prog_addr), .prog_wdata(prog_wdata),
        .start(start), .emit(emit), .boot_status(boot_status), .pc(pc), .coeffs(coeffs), .k(k),
        .status(status), .gates_done(gates_done), .phys(phys)
    );

    always #5 clk = ~clk;

    always @(posedge clk) if (emit) begin
        #1;
        $write("case %0d status %0d k %0d gates %0d cycles 0 c", cases, status, k, gates_done);
        for (m = 0; m < 16; m = m + 1) $write(" %0d", $signed(coeffs[m*W +: W]));
        $write("\n");
        cases = cases + 1;
    end

    initial begin
        if (!$value$plusargs("imgs=%s", path)) begin
            $display("ERROR missing +imgs");
            $finish;
        end
        list = $fopen(path, "r");
        cases = 0;
        @(negedge clk) rst = 0;
        while (!$feof(list)) begin
            rc = $fscanf(list, "%s", imgpath);
            if (rc == 1) begin
                img = $fopen(imgpath, "r");
                words = 0;
                while (!$feof(img)) begin
                    rc = $fscanf(img, "%h", word);
                    if (rc == 1) begin
                        prog_addr = words; prog_wdata = word; prog_we = 1;
                        @(negedge clk) prog_we = 0;
                        words = words + 1;
                    end
                end
                $fclose(img);
                start = 1; @(negedge clk) start = 0;
                cycles = 0;
                while (boot_status == 1 && cycles < 1000000) begin
                    @(negedge clk);
                    cycles = cycles + 1;
                end
                $display("image %0s boot %0d pc %0d cycles %0d", imgpath, boot_status, pc, cycles);
            end
        end
        $fclose(list);
        $finish;
    end
endmodule
