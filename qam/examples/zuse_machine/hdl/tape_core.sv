`timescale 1ns/1ps
// One bounded binary tape machine. SCAN selects the rule-table controller.
module tape_core #(
    parameter integer CELLS = 8,
    parameter integer STATES = 3,
    parameter integer SCAN = 0,
    parameter integer HEAD_BITS = CELLS > 1 ? $clog2(CELLS) : 1,
    parameter integer LEN_BITS = $clog2(CELLS + 1),
    parameter integer STATE_BITS = STATES > 1 ? $clog2(STATES) : 1,
    parameter integer SLOT_BITS = $clog2(2 * STATES),
    parameter integer RULE_BITS = STATE_BITS + 4
) (
    input wire clk,
    input wire reset,
    input wire rule_we,
    input wire [SLOT_BITS-1:0] rule_addr,
    // Packed rule: valid, write bit, move (0 stay, 1 right, 2 left), next state.
    input wire [RULE_BITS-1:0] rule_data,
    input wire load,
    input wire [CELLS-1:0] initial_tape,
    input wire [LEN_BITS-1:0] initial_length,
    input wire [HEAD_BITS-1:0] initial_head,
    input wire [STATE_BITS-1:0] initial_state,
    input wire [STATE_BITS-1:0] halt_state,
    input wire grow,
    input wire [LEN_BITS-1:0] max_cells,
    input wire [10:0] max_steps,
    output reg [CELLS-1:0] tape,
    output reg [LEN_BITS-1:0] length,
    output reg [HEAD_BITS-1:0] head,
    output reg [STATE_BITS-1:0] state,
    output reg [10:0] steps,
    output reg [2:0] stop,
    output reg trace_valid
);
    localparam [2:0] RUNNING = 0, HALTED = 1, BOUNDARY = 2, STUCK = 3,
                     STEP_LIMIT = 4, CELL_LIMIT = 5;
    localparam [1:0] RIGHT = 1, LEFT = 2;
    localparam [SLOT_BITS-1:0] LAST_SLOT = 2 * STATES - 1;

    reg [RULE_BITS-1:0] rules [0:2*STATES-1];
    reg [STATE_BITS-1:0] halt_latched;
    reg grow_latched;
    reg [LEN_BITS-1:0] cells_latched;
    reg [10:0] steps_latched;
    wire [SLOT_BITS-1:0] matching_slot = {state, tape[head]};
    wire [RULE_BITS-1:0] selected_rule;
    wire ready_to_apply;

    always @(posedge clk)
        if (rule_we && stop != RUNNING)
            rules[rule_addr] <= rule_data;

    generate
        if (SCAN != 0) begin : serial_controller
            reg [SLOT_BITS-1:0] slot;
            reg [RULE_BITS-1:0] matching_rule;
            wire match = slot == matching_slot;
            wire [RULE_BITS-1:0] row = rules[slot];
            assign selected_rule = match ? row : matching_rule;
            assign ready_to_apply = slot == LAST_SLOT;

            always @(posedge clk) begin
                if (reset || load || ready_to_apply) begin
                    slot <= 0;
                    matching_rule <= 0;
                end else if (stop == RUNNING) begin
                    if (match)
                        matching_rule <= row;
                    slot <= slot + 1'b1;
                end
            end
        end else begin : direct_controller
            assign selected_rule = rules[matching_slot];
            assign ready_to_apply = 1'b1;
        end
    endgenerate

    wire [STATE_BITS-1:0] next_state = selected_rule[STATE_BITS-1:0];
    wire [1:0] movement = selected_rule[STATE_BITS+:2];
    wire write_bit = selected_rule[STATE_BITS+2];
    wire valid_rule = selected_rule[STATE_BITS+3];
    wire left_boundary = movement == LEFT && head == 0;
    wire right_boundary = movement == RIGHT && {1'b0, head} + 1'b1 == length;

    always @(posedge clk) begin
        trace_valid <= 0;
        if (reset) begin
            tape <= 0;
            length <= 0;
            head <= 0;
            state <= 0;
            steps <= 0;
            stop <= HALTED;
            halt_latched <= 0;
            grow_latched <= 0;
            cells_latched <= 0;
            steps_latched <= 0;
        end else if (load) begin
            tape <= initial_tape;
            length <= initial_length;
            head <= initial_head;
            state <= initial_state;
            halt_latched <= halt_state;
            grow_latched <= grow;
            cells_latched <= max_cells;
            steps_latched <= max_steps;
            steps <= 0;
            trace_valid <= 1;
            if (initial_state == halt_state)
                stop <= HALTED;
            else if (max_steps == 0)
                stop <= STEP_LIMIT;
            else
                stop <= RUNNING;
        end else if (stop == RUNNING && ready_to_apply) begin
            if (valid_rule && right_boundary && grow_latched && length == cells_latched) begin
                stop <= CELL_LIMIT;
            end else begin
                steps <= steps + 1'b1;
                trace_valid <= 1;
                if (!valid_rule) begin
                    stop <= STUCK;
                end else if (left_boundary || (right_boundary && !grow_latched)) begin
                    stop <= BOUNDARY;
                end else begin
                    tape[head] <= write_bit;
                    if (right_boundary) begin
                        tape[length[HEAD_BITS-1:0]] <= 0;
                        length <= length + 1'b1;
                    end
                    if (movement == LEFT)
                        head <= head - 1'b1;
                    else if (movement == RIGHT)
                        head <= head + 1'b1;
                    state <= next_state;
                    if (next_state == halt_latched)
                        stop <= HALTED;
                    else if (steps + 1'b1 == steps_latched)
                        stop <= STEP_LIMIT;
                end
            end
        end
    end
endmodule
