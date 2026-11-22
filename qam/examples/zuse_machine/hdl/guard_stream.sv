`timescale 1ns/1ps

// One registered slot reports unique orientations from a stream of guard masks.
module guard_stream (
    input wire clk,
    input wire rst,
    input wire in_valid,
    output wire in_ready,
    input wire [31:0] in_id,
    input wire [1:0] in_first,
    input wire [1:0] in_second,
    output reg out_valid,
    input wire out_ready,
    output reg [31:0] out_id,
    output reg out_positive,
    output reg [63:0] accepted_count,
    output reg [63:0] selected_count,
    output reg [63:0] blocked_count,
    output reg [63:0] ambiguous_count
);
    wire [1:0] remaining = in_first & in_second;
    wire unique_orientation = remaining[0] ^ remaining[1];

    // A full slot can be consumed and replaced on the same clock edge.
    assign in_ready = !rst && (!out_valid || out_ready);

    always @(posedge clk) begin
        if (rst) begin
            out_valid <= 1'b0;
            out_id <= 32'b0;
            out_positive <= 1'b0;
            accepted_count <= 64'b0;
            selected_count <= 64'b0;
            blocked_count <= 64'b0;
            ambiguous_count <= 64'b0;
        end else if (in_ready) begin
            out_valid <= in_valid && unique_orientation;
            if (in_valid) begin
                accepted_count <= accepted_count + 64'd1;
                case (remaining)
                    2'b01, 2'b10: begin
                        out_id <= in_id;
                        out_positive <= remaining[0];
                        selected_count <= selected_count + 64'd1;
                    end
                    2'b00: blocked_count <= blocked_count + 64'd1;
                    2'b11: ambiguous_count <= ambiguous_count + 64'd1;
                endcase
            end
        end
    end
endmodule
