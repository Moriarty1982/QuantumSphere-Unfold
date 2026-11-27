`timescale 1ns/1ps
// Selbstjustierung: Rueckkopplungs-Rechenwerk fuer eine von aussen gesetzte Groesse (Q2.30, vorzeichenbehaftet,
// Wert/2^30). Ausgewertet wird f(x) = c0 + c1 x + c2 x^2 in Festkomma (Produkte auf 64 Bit, dann >>> 30 und
// auf 32 Bit abgeschnitten; Summe auf 32 Bit). Ein Schritt je Takt.
//
//   mode 0  FIX     Fixpunktsuche x <- f(x) ab x0, bis |f(x) - x| <= tol oder max_iter Schritte.
//                   d_last, d_prev = |dx| der letzten zwei Schritte (ihr Verhaeltnis schaetzt |f'(x*)|).
//   mode 1  BISECT  Nullstelle von g(x) = f(x) - target in [lo, hi] durch Halbierung, bis hi - lo <= tol oder
//                   max_iter Schritte; Voraussetzung: g(lo) und g(hi) haben verschiedene Vorzeichen.
// status: 0 konvergiert, 1 max_iter erreicht, 2 ungueltige Klammer (BISECT), 3 Lauf abgebrochen.
// Jedes Ergebnis dieses Werks ist eine angepasste Groesse (gesucht, nicht hergeleitet); qcop2t_top markiert sie so.
module qtune (
    input wire clk,
    input wire rst,
    input wire start,
    input wire abort,
    input wire mode,
    input wire signed [31:0] c0,
    input wire signed [31:0] c1,
    input wire signed [31:0] c2,
    input wire signed [31:0] x0,        // Startwert (FIX) bzw. lo (BISECT)
    input wire signed [31:0] hi,
    input wire signed [31:0] target,
    input wire [31:0] tol,
    input wire [15:0] max_iter,
    output reg busy,
    output reg done,
    output reg [1:0] status,
    output reg signed [31:0] x,
    output reg [15:0] iters,
    output reg [31:0] d_last,
    output reg [31:0] d_prev
);
    localparam [1:0] S_IDLE = 0, S_GLO = 1, S_GHI = 2, S_RUN = 3;
    reg [1:0] st;
    reg signed [31:0] lo_r, hi_r;
    reg neg_lo;                 // Vorzeichen von g(lo)

    // Auswerter
    reg signed [31:0] ev_x;
    wire signed [63:0] p1 = c1 * ev_x;
    wire signed [63:0] pxx = ev_x * ev_x;
    wire signed [31:0] xx = pxx[61:30];
    wire signed [63:0] p2 = c2 * xx;
    wire signed [31:0] t1 = p1[61:30];
    wire signed [31:0] t2 = p2[61:30];
    wire signed [31:0] fx = c0 + t1 + t2;

    wire signed [32:0] dx = {fx[31], fx} - {ev_x[31], ev_x};
    wire [32:0] adx = dx[32] ? -dx : dx;
    wire signed [32:0] gx = {fx[31], fx} - {target[31], target};
    wire signed [32:0] sum_lh = {lo_r[31], lo_r} + {hi_r[31], hi_r};
    wire signed [31:0] mid = sum_lh[32:1];                       // floor((lo + hi) / 2)
    wire signed [32:0] w_left = {mid[31], mid} - {lo_r[31], lo_r};
    wire signed [32:0] w_right = {hi_r[31], hi_r} - {mid[31], mid};
    wire go_right = gx[32] == neg_lo;                           // Nullstelle rechts von mid
    wire signed [32:0] w_new = go_right ? w_right : w_left;

    function automatic [31:0] sat32(input [32:0] v);
        sat32 = v[32] ? 32'hFFFF_FFFF : v[31:0];
    endfunction

    always @(*) begin
        case (st)
            S_GLO: ev_x = lo_r;
            S_GHI: ev_x = hi_r;
            S_RUN: ev_x = mode ? mid : x;
            default: ev_x = x0;
        endcase
    end

    always @(posedge clk) begin
        done <= 1'b0;
        if (rst) begin
            st <= S_IDLE;
            busy <= 1'b0;
            status <= 2'd0;
            x <= 32'sd0;
            iters <= 16'd0;
            d_last <= 32'd0;
            d_prev <= 32'd0;
        end else if (abort && busy) begin
            st <= S_IDLE;
            busy <= 1'b0;
            done <= 1'b1;
            status <= 2'd3;
        end else begin
            case (st)
                S_IDLE: if (start) begin
                    busy <= 1'b1;
                    iters <= 16'd0;
                    d_last <= 32'd0;
                    d_prev <= 32'd0;
                    x <= x0;
                    lo_r <= x0;
                    hi_r <= hi;
                    st <= mode ? S_GLO : S_RUN;
                end
                S_GLO: begin
                    neg_lo <= gx[32];
                    if (gx == 0) begin
                        x <= lo_r; status <= 2'd0; busy <= 1'b0; done <= 1'b1; st <= S_IDLE;
                    end else st <= S_GHI;
                end
                S_GHI: begin
                    if (gx == 0) begin
                        x <= hi_r; status <= 2'd0; busy <= 1'b0; done <= 1'b1; st <= S_IDLE;
                    end else if (gx[32] == neg_lo || hi_r <= lo_r) begin
                        status <= 2'd2; busy <= 1'b0; done <= 1'b1; st <= S_IDLE;
                    end else st <= S_RUN;
                end
                S_RUN: begin
                    iters <= iters + 16'd1;
                    if (!mode) begin
                        // FIX: x <- f(x)
                        x <= fx;
                        d_prev <= d_last;
                        d_last <= sat32(adx);
                        if (adx <= {1'b0, tol}) begin
                            status <= 2'd0; busy <= 1'b0; done <= 1'b1; st <= S_IDLE;
                        end else if (iters + 16'd1 >= max_iter) begin
                            status <= 2'd1; busy <= 1'b0; done <= 1'b1; st <= S_IDLE;
                        end
                    end else begin
                        // BISECT-Schritt: ev_x = mid
                        x <= mid;
                        if (gx == 0) begin
                            status <= 2'd0; busy <= 1'b0; done <= 1'b1; st <= S_IDLE;
                        end else begin
                            if (go_right) lo_r <= mid; else hi_r <= mid;
                            if (w_new <= $signed({1'b0, tol})) begin
                                status <= 2'd0; busy <= 1'b0; done <= 1'b1; st <= S_IDLE;
                            end else if (iters + 16'd1 >= max_iter) begin
                                status <= 2'd1; busy <= 1'b0; done <= 1'b1; st <= S_IDLE;
                            end
                        end
                    end
                end
            endcase
        end
    end
endmodule
