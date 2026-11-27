`timescale 1ns/1ps
// Testbench des selbstueberwachten Kerns (qcop2s_top). Zeilen der Eingabe:
//   C adr wert   Konfigurationsregister schreiben (wirksam ab dem naechsten B)
//   B            neuer Fall, Zustand |00>, Konfiguration wird aktiv
//   G op ziel    ein Gatter
//   I idx bit    Bit bit von Koeffizient idx am Eingang des Waechters kippen, im selben Takt wie das naechste
//                Gatter (prueft, dass der Kern ohne Verzug anhaelt), sonst einen Leertakt vor E
//   E            Ergebnis ausgeben: "case n status s k k gates g fault f faults z c ..."
module qcop2s_tb;
    parameter integer W = 16;
    reg clk = 0, rst = 1, load = 0, op_valid = 0, target = 0, cfg_we = 0;
    reg [3:0] opcode = 0;
    reg [4:0] cfg_addr = 0;
    reg [31:0] cfg_wdata = 0;
    reg [16*W-1:0] inject_mask = 0;
    wire [31:0] cfg_rdata;
    wire [16*W-1:0] coeffs;
    wire [7:0] k;
    wire [1:0] status;
    wire [15:0] gates_done, faults;
    wire fault;
    wire [16*32-1:0] phys;
    integer fd, rc, op, tg, m, cases, adr, idx, bt;
    reg [31:0] val;
    reg [8*8-1:0] cmd;
    reg [8*512-1:0] path;

    qcop2s_top #(.W(W)) dut (
        .clk(clk), .rst(rst), .load(load), .op_valid(op_valid), .opcode(opcode), .target(target),
        .cfg_we(cfg_we), .cfg_addr(cfg_addr), .cfg_wdata(cfg_wdata), .cfg_rdata(cfg_rdata),
        .inject_mask(inject_mask), .coeffs(coeffs), .k(k), .status(status), .gates_done(gates_done),
        .fault(fault), .faults(faults), .phys(phys)
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
                if (cmd == "C") begin
                    rc = $fscanf(fd, "%d %d", adr, val);
                    cfg_addr = adr; cfg_wdata = val; cfg_we = 1;
                    @(negedge clk) cfg_we = 0;
                end else if (cmd == "B") begin
                    load = 1; @(negedge clk) load = 0;
                end else if (cmd == "G") begin
                    rc = $fscanf(fd, "%d %d", op, tg);
                    opcode = op; target = tg; op_valid = 1;
                    @(negedge clk) op_valid = 0;
                    inject_mask = 0;
                end else if (cmd == "I") begin
                    rc = $fscanf(fd, "%d %d", idx, bt);
                    inject_mask = 0;
                    inject_mask[idx*W + bt] = 1'b1;
                end else if (cmd == "E") begin
                    if (inject_mask != 0) begin
                        @(negedge clk) inject_mask = 0;
                    end
                    $write("case %0d status %0d k %0d gates %0d fault %0d faults %0d c", cases, status, k,
                           gates_done, fault, faults);
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
