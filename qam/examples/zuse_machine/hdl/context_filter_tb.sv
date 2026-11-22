`timescale 1ns/1ps
module context_filter_tb;
    reg [31:0] row_count, mask, row_id;
    reg [31:0] wanted_source, wanted_frame, wanted_guard;
    reg [31:0] row_source, row_frame, row_guard;
    wire row_matches;

    context_filter dut (
        .mask(mask[2:0]),
        .wanted_source(wanted_source),
        .wanted_frame(wanted_frame),
        .wanted_guard(wanted_guard),
        .row_source(row_source),
        .row_frame(row_frame),
        .row_guard(row_guard),
        .row_matches(row_matches)
    );

    task automatic fail(input string message);
        begin
            $display("ERROR %s", message);
            $finish_and_return(1);
        end
    endtask

    function automatic is_whitespace(input integer ch);
        is_whitespace = ch == 32 || (ch >= 9 && ch <= 13);
    endfunction

    // The input protocol uses only unsigned decimal fields.
    task automatic read_field(input integer file, output reg [31:0] value);
        integer ch;
        reg [35:0] accumulated;
        begin
            ch = $fgetc(file);
            while (is_whitespace(ch))
                ch = $fgetc(file);
            if (ch < 48 || ch > 57)
                fail("Expected an unsigned decimal field");
            accumulated = 0;
            while (ch >= 48 && ch <= 57) begin
                accumulated = 10 * accumulated + (ch - 48);
                if (accumulated[35:32] != 0)
                    fail("Field exceeds the unsigned 32-bit range");
                ch = $fgetc(file);
            end
            if (ch != -1 && !is_whitespace(ch))
                fail("Expected a delimiter after the decimal field");
            value = accumulated[31:0];
        end
    endtask

    string cases_path;
    integer file, trailing;
    reg [31:0] row;
    initial begin
        if (!$value$plusargs("cases=%s", cases_path))
            fail("Expected +cases=PATH");
        file = $fopen(cases_path, "r");
        if (file == 0)
            fail("Cannot open context filter vectors");
        read_field(file, row_count);
        read_field(file, mask);
        if (mask[31:3] != 0)
            fail("Context filter mask must be between 0 and 7");
        read_field(file, wanted_source);
        read_field(file, wanted_frame);
        read_field(file, wanted_guard);
        for (row = 0; row < row_count; row = row + 1) begin
            read_field(file, row_id);
            read_field(file, row_source);
            read_field(file, row_frame);
            read_field(file, row_guard);
            #1;
            if (row_matches)
                $display("MATCH %0d", row_id);
        end
        trailing = $fgetc(file);
        while (is_whitespace(trailing))
            trailing = $fgetc(file);
        if (trailing != -1)
            fail("Unexpected data after context filter vectors");
        $fclose(file);
        $finish_and_return(0);
    end
endmodule
