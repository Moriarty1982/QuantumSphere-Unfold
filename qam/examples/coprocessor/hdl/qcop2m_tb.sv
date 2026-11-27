`timescale 1ns/1ps
// Testbench der parallelen Rechenwerke. Eingabe (+stim=DATEI):
//   B cmd a b d        Befehl an das Bandregister (d hexadezimal)
//   C adr wert         Konfigurationsregister schreiben (wirksam ab dem naechsten Laden)
//   G n                Gruppe aus n Faellen; danach n Zeilen "L band len op ziel ..."
// Jede Spur gibt je Takt ein Gatter an den naechsten freien Kontext ihrer Baender mit Restgattern.
// Ausgabe je Fall "case ..." wie qstep2_tb, je Gruppe "group n cycles gates blocked".
module qcop2m_tb;
    parameter integer W = 16;
    parameter integer LANES = 2;
    parameter integer CTX = 4;
    localparam integer PARTS = LANES * CTX;
    localparam integer CB = CTX > 1 ? $clog2(CTX) : 1;
    localparam integer PB = PARTS > 1 ? $clog2(PARTS) : 1;
    localparam integer MAXG = 256;
    reg clk = 0, rst = 1, load = 0, cfg_we = 0, band_valid = 0;
    wire band_busy;
    reg [4:0] cfg_addr = 0;
    reg [31:0] cfg_wdata = 0;
    reg [3:0] band_cmd = 0;
    reg [7:0] band_a = 0;
    reg [15:0] band_b = 0;
    reg [127:0] band_d = 0;
    reg [PB-1:0] load_part = 0, rd_part = 0;
    reg [LANES-1:0] op_valid = 0, target = 0;
    reg [LANES*CB-1:0] op_ctx = 0;
    reg [LANES*4-1:0] opcode = 0;
    wire [31:0] cfg_rdata, blocked;
    wire band_ok, layout_ok, full;
    wire [127:0] band_data;
    wire [PARTS-1:0] ready;
    wire [16*W-1:0] coeffs;
    wire [7:0] k;
    wire [1:0] status;
    wire [15:0] gates_done;
    wire [16*32-1:0] phys;
    integer fd, rc, n, i, j, m, len, adr, cases, cycles, issued, total, g, t, p, x, y, blk0;
    integer part_of [0:PARTS-1];
    integer has [0:PARTS-1];
    integer glen [0:PARTS-1];
    integer gpos [0:PARTS-1];
    integer gop [0:PARTS-1][0:MAXG-1];
    integer gtg [0:PARTS-1][0:MAXG-1];
    integer cur [0:LANES-1];
    reg [31:0] val;
    reg [127:0] dv;
    reg [8*8-1:0] cmd;
    reg [8*512-1:0] path;
    reg [PARTS-1:0] all_ready;

    qcop2m_top #(.W(W), .LANES(LANES), .CTX(CTX)) dut (
        .clk(clk), .rst(rst), .cfg_we(cfg_we), .cfg_addr(cfg_addr), .cfg_wdata(cfg_wdata),
        .cfg_rdata(cfg_rdata), .band_valid(band_valid), .band_cmd(band_cmd), .band_a(band_a),
        .band_b(band_b), .band_d(band_d), .band_ok(band_ok), .band_data(band_data),
        .layout_ok(layout_ok), .full(full), .band_busy(band_busy), .load(load), .load_part(load_part), .op_valid(op_valid),
        .op_ctx(op_ctx), .opcode(opcode), .target(target), .ready(ready), .blocked(blocked),
        .rd_part(rd_part), .coeffs(coeffs), .k(k), .status(status), .gates_done(gates_done), .phys(phys)
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
                    rc = $fscanf(fd, "%d %d %d %h", x, y, adr, dv);
                    band_cmd = x; band_a = y; band_b = adr; band_d = dv; band_valid = 1;
                    @(negedge clk) band_valid = 0;
                    while (band_busy) @(negedge clk);
                end else if (cmd == "C") begin
                    rc = $fscanf(fd, "%d %d", adr, val);
                    cfg_addr = adr; cfg_wdata = val; cfg_we = 1;
                    @(negedge clk) cfg_we = 0;
                end else if (cmd == "G") begin
                    rc = $fscanf(fd, "%d", n);
                    total = 0;
                    blk0 = blocked;
                    for (p = 0; p < PARTS; p = p + 1) has[p] = 0;
                    for (i = 0; i < n; i = i + 1) begin
                        rc = $fscanf(fd, "%s %d %d", cmd, p, len);
                        part_of[i] = p;
                        has[p] = 1;
                        glen[p] = len;
                        gpos[p] = 0;
                        total = total + len;
                        for (j = 0; j < len; j = j + 1) begin
                            rc = $fscanf(fd, "%d %d", x, y);
                            gop[p][j] = x; gtg[p][j] = y;
                        end
                        load_part = p; load = 1;
                        @(negedge clk) load = 0;
                    end
                    for (g = 0; g < LANES; g = g + 1) cur[g] = 0;
                    cycles = 0; issued = 0;
                    all_ready = {PARTS{1'b1}};
                    while (issued < total || ready != all_ready) begin
                        for (g = 0; g < LANES; g = g + 1) begin
                            op_valid[g] = 0;
                            for (t = 0; t < CTX && !op_valid[g]; t = t + 1) begin
                                p = g * CTX + (cur[g] + t) % CTX;
                                if (has[p] && gpos[p] < glen[p] && ready[p]) begin
                                    op_valid[g] = 1;
                                    op_ctx[g*CB +: CB] = p % CTX;
                                    opcode[g*4 +: 4] = gop[p][gpos[p]];
                                    target[g] = gtg[p][gpos[p]];
                                    gpos[p] = gpos[p] + 1;
                                    issued = issued + 1;
                                    cur[g] = (p % CTX + 1) % CTX;
                                end
                            end
                        end
                        @(negedge clk) op_valid = 0;
                        cycles = cycles + 1;
                    end
                    for (i = 0; i < n; i = i + 1) begin
                        rd_part = part_of[i]; #1;
                        $write("case %0d status %0d k %0d gates %0d cycles 0 c", cases, status, k, gates_done);
                        for (m = 0; m < 16; m = m + 1) $write(" %0d", $signed(coeffs[m*W +: W]));
                        $write("\n");
                        cases = cases + 1;
                    end
                    $display("group %0d cycles %0d gates %0d blocked %0d", n, cycles, total, blocked - blk0);
                    @(negedge clk);
                end
            end
        end
        $fclose(fd);
        $finish;
    end
endmodule
