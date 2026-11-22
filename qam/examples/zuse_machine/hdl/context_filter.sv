`timescale 1ns/1ps
// Stateless filter for host-encoded QAM context metadata.
module context_filter (
    input wire [2:0] mask,
    input wire [31:0] wanted_source,
    input wire [31:0] wanted_frame,
    input wire [31:0] wanted_guard,
    input wire [31:0] row_source,
    input wire [31:0] row_frame,
    input wire [31:0] row_guard,
    output wire row_matches
);
    assign row_matches = (!mask[0] || row_source == wanted_source)
                      && (!mask[1] || row_frame == wanted_frame)
                      && (!mask[2] || row_guard == wanted_guard);
endmodule
