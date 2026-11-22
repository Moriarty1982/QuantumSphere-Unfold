`timescale 1ns/1ps

module guard_stream_tb;
    reg clk = 0;
    always #5 clk = ~clk;

    reg rst = 1;
    reg in_valid = 0;
    wire in_ready;
    reg [31:0] in_id = 0;
    reg [1:0] in_first = 0, in_second = 0;
    wire out_valid;
    reg out_ready = 0;
    wire [31:0] out_id;
    wire out_positive;
    wire [63:0] accepted_count, selected_count, blocked_count, ambiguous_count;

    guard_stream dut (
        .clk(clk), .rst(rst),
        .in_valid(in_valid), .in_ready(in_ready), .in_id(in_id),
        .in_first(in_first), .in_second(in_second),
        .out_valid(out_valid), .out_ready(out_ready), .out_id(out_id),
        .out_positive(out_positive), .accepted_count(accepted_count),
        .selected_count(selected_count), .blocked_count(blocked_count),
        .ambiguous_count(ambiguous_count)
    );

    task automatic fail(input string message);
        begin
            $display("ERROR %s", message);
            $finish_and_return(1);
        end
    endtask

    string cases_path;
    integer file, stall_mode, have_cases, generate_locally, trailing;
    reg [63:0] row_count, cycles, cycle_limit, input_seen, output_seen;
    reg [63:0] expected_selected, expected_blocked, expected_ambiguous;
    reg [63:0] file_id, file_first, file_second;
    reg advance_input, holding, held_positive;
    reg [31:0] held_id;

    initial begin
        have_cases = $value$plusargs("cases=%s", cases_path);
        generate_locally = $value$plusargs("generate=%d", row_count);
        if (have_cases == generate_locally)
            fail("Use exactly one of +cases=PATH and +generate=N");
        if (have_cases) begin
            file = $fopen(cases_path, "r");
            if (file == 0)
                fail("Cannot open guard stream vectors");
            if ($fscanf(file, "%d", row_count) != 1)
                fail("Expected a guard stream row count");
        end
        if (^row_count === 1'bx || row_count > 1000000)
            fail("Guard stream must contain between zero and one million rows");
        if (!$value$plusargs("stall=%d", stall_mode))
            stall_mode = 0;
        if (stall_mode !== 0 && stall_mode !== 1)
            fail("Stall mode must be zero or one");

        cycles = 0;
        cycle_limit = 4 * row_count + 20;
        input_seen = 0;
        output_seen = 0;
        expected_selected = 0;
        expected_blocked = 0;
        expected_ambiguous = 0;
        advance_input = 1;
        holding = 0;

        // Drive on the falling edge and sample transfers before NBA updates.
        @(negedge clk);
        rst = 0;
        while (input_seen < row_count || out_valid) begin
            if (advance_input) begin
                in_valid = input_seen < row_count;
                if (in_valid && generate_locally) begin
                    in_id = input_seen[31:0];
                    in_first = input_seen[3:2];
                    in_second = input_seen[1:0];
                end else if (in_valid) begin
                    if ($fscanf(file, "%d %d %d", file_id, file_first, file_second) != 3)
                        fail("Expected an ID and two masks for the next row");
                    if (^{file_id, file_first, file_second} === 1'bx ||
                        file_id > 64'hffffffff || file_first > 3 || file_second > 3)
                        fail("Row ID or guard masks outside the allowed range");
                    in_id = file_id[31:0];
                    in_first = file_first[1:0];
                    in_second = file_second[1:0];
                end
            end
            out_ready = !stall_mode || cycles % 5 < 2;
            @(posedge clk);
            cycles = cycles + 1;
            if (cycles > cycle_limit)
                fail("Guard stream timed out");
            if (holding && (out_valid !== 1'b1 || out_id !== held_id ||
                            out_positive !== held_positive))
                fail("Pending output changed while stalled");
            holding = out_valid && !out_ready;
            if (holding) begin
                held_id = out_id;
                held_positive = out_positive;
            end
            if (out_valid && out_ready) begin
                if (^{out_id, out_positive} === 1'bx)
                    fail("Accepted output contains an unknown value");
                $display("MATCH %0d %0d", out_id, out_positive);
                output_seen = output_seen + 1;
            end

            if (in_ready !== 1'b0 && in_ready !== 1'b1)
                fail("Unknown input readiness");
            advance_input = !in_valid || in_ready;
            if (in_valid && in_ready) begin
                input_seen = input_seen + 1;
                case (in_first & in_second)
                    2'b00: expected_blocked = expected_blocked + 1;
                    2'b11: expected_ambiguous = expected_ambiguous + 1;
                    default: expected_selected = expected_selected + 1;
                endcase
            end
            @(negedge clk);
        end

        if (have_cases) begin
            trailing = $fgetc(file);
            while (trailing == 32 || (trailing >= 9 && trailing <= 13))
                trailing = $fgetc(file);
            if (trailing != -1)
                fail("Unexpected data after guard stream vectors");
            $fclose(file);
        end
        if (accepted_count !== input_seen || selected_count !== expected_selected ||
            selected_count !== output_seen || blocked_count !== expected_blocked ||
            ambiguous_count !== expected_ambiguous)
            fail("Guard stream counters disagree with observed transfers");

        $display("STATS %0d %0d %0d %0d %0d", cycles, accepted_count,
                 selected_count, blocked_count, ambiguous_count);
        $finish_and_return(0);
    end
endmodule
