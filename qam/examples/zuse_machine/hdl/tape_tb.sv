`timescale 1ns/1ps
module tape_tb;
    localparam integer CELLS = 8, STATES = 3, SLOTS = 2 * STATES;

    reg clk = 0;
    always #5 clk = ~clk;

    reg reset = 1;
    reg rule_we = 0, load = 0;
    reg [2:0] rule_addr;
    reg [5:0] rule_data;
    reg [7:0] initial_tape;
    reg [3:0] initial_length, max_cells;
    reg [2:0] initial_head;
    reg [1:0] initial_state, halt_state;
    reg grow;
    reg [10:0] max_steps;

    wire [7:0] tape [0:1];
    wire [3:0] length [0:1];
    wire [2:0] head [0:1], stop [0:1];
    wire [1:0] state [0:1];
    wire [10:0] steps [0:1];
    wire trace_valid [0:1];

    genvar controller;
    generate
    for (controller = 0; controller < 2; controller = controller + 1) begin : cores
        tape_core #(.CELLS(CELLS), .STATES(STATES), .SCAN(controller)) dut (
            .clk(clk), .reset(reset), .rule_we(rule_we), .rule_addr(rule_addr),
            .rule_data(rule_data), .load(load), .initial_tape(initial_tape),
            .initial_length(initial_length), .initial_head(initial_head),
            .initial_state(initial_state), .halt_state(halt_state),
            .grow(grow), .max_cells(max_cells), .max_steps(max_steps),
            .tape(tape[controller]), .length(length[controller]), .head(head[controller]),
            .state(state[controller]), .steps(steps[controller]), .stop(stop[controller]),
            .trace_valid(trace_valid[controller])
        );
    end
    endgenerate

    task tick;
        @(posedge clk);
        #1;
    endtask

    task report_trace(input integer case_id);
        integer i;
        for (i = 0; i < 2; i = i + 1)
            if (trace_valid[i])
                $display("TRACE %0d %0d %0d %02h %0d %0d %0d %0d",
                         case_id, i, steps[i], tape[i], length[i], head[i], state[i], stop[i]);
    endtask

    string cases_path, wave_path;
    integer source, count, case_id, slot, i;
    integer cycles [0:1];
    reg [27:0] previous [0:1];
    initial begin
        if (!$value$plusargs("cases=%s", cases_path))
            $fatal(1, "Expected +cases=PATH");
        source = $fopen(cases_path, "r");
        if (source == 0 || $fscanf(source, "%d", count) != 1)
            $fatal(1, "Cannot read case count");
        if ($value$plusargs("wave=%s", wave_path)) begin
            $dumpfile(wave_path);
            $dumpvars(0, tape_tb);
        end
        tick();
        reset = 0;
        for (case_id = 0; case_id < count; case_id = case_id + 1) begin
            if ($fscanf(source, "%h %d %d %d %d %d %d %d",
                        initial_tape, initial_length, initial_head, initial_state,
                        halt_state, grow, max_cells, max_steps) != 8)
                $fatal(1, "Cannot read configuration for case %0d", case_id);
            for (slot = 0; slot < SLOTS; slot = slot + 1) begin
                if ($fscanf(source, "%h", rule_data) != 1)
                    $fatal(1, "Cannot read rule for case %0d, slot %0d", case_id, slot);
                rule_we = 1;
                rule_addr = slot;
                tick();
            end
            rule_we = 0;
            load = 1;
            tick();
            load = 0;
            cycles[0] = 0;
            cycles[1] = 0;
            report_trace(case_id);
            while (stop[0] == 0 || stop[1] == 0) begin
                for (i = 0; i < 2; i = i + 1) begin
                    previous[i] = {tape[i], length[i], head[i], state[i], steps[i]};
                    if (stop[i] == 0)
                        cycles[i] = cycles[i] + 1;
                end
                if (cycles[1] > (max_steps + 1) * SLOTS)
                    $fatal(1, "Simulation timeout in case %0d", case_id);
                tick();
                for (i = 0; i < 2; i = i + 1)
                    if (!trace_valid[i] && previous[i] !== {tape[i], length[i], head[i], state[i], steps[i]})
                        $fatal(1, "Unreported configuration change in case %0d, controller %0d", case_id, i);
                report_trace(case_id);
            end
            for (i = 0; i < 2; i = i + 1)
                $display("DONE %0d %0d %0d %0d %02h %0d %0d %0d %0d",
                         case_id, i, cycles[i], steps[i], tape[i], length[i], head[i], state[i], stop[i]);
        end
        $fclose(source);
        $finish;
    end
endmodule
