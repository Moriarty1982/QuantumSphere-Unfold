`timescale 1ns/1ps
// Liest Faelle aus +stim=DATEI und schreibt je Fall eine Ergebniszeile.
// Zeilen der Eingabe:  B            neuer Fall, Zustand |00>
//                      G op ziel    ein Gatter
//                      E            Ergebnis ausgeben
module qstep2_tb;
    parameter integer W = 16;
    reg clk = 0, rst = 1, load = 0, op_valid = 0, target = 0;
    reg [3:0] opcode = 0;
    wire [16*W-1:0] coeffs;
    wire [7:0] k;
    wire [1:0] status;
    wire [15:0] gates_done;
    integer fd, rc, op, tg, m, cases, cycles;
    reg [8*8-1:0] cmd;
    reg [8*512-1:0] path;

    qstep2 #(.W(W)) dut (
        .clk(clk), .rst(rst), .load(load), .op_valid(op_valid), .opcode(opcode),
        .target(target), .coeffs(coeffs), .k(k), .status(status), .gates_done(gates_done)
    );

    always #5 clk = ~clk;

    initial begin
        if (!$value$plusargs("stim=%s", path)) begin
            $display("ERROR missing +stim");
            $finish;
        end
        fd = $fopen(path, "r");
        cases = 0;
        @(negedge clk) rst = 0;
        while (!$feof(fd)) begin
            rc = $fscanf(fd, "%s", cmd);
            if (rc == 1) begin
                if (cmd == "B") begin
                    load = 1; @(negedge clk) load = 0;
                    cycles = 0;
                end else if (cmd == "G") begin
                    rc = $fscanf(fd, "%d %d", op, tg);
                    opcode = op; target = tg; op_valid = 1;
                    @(negedge clk) op_valid = 0;
                    cycles = cycles + 1;
                end else if (cmd == "E") begin
                    $write("case %0d status %0d k %0d gates %0d cycles %0d c", cases, status, k,
                           gates_done, cycles);
                    for (m = 0; m < 16; m = m + 1) $write(" %0d", $signed(coeffs[m*W +: W]));
                    $write("\n");
                    cases = cases + 1;
                end
            end
        end
        $fclose(fd);
        $finish;
    end
endmodule
