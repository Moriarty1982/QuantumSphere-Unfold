`timescale 1ns/1ps
// Konfigurationsregister des Quanten-Coprozessors.
//
// Der Host schreibt Werte ueber cfg_we/cfg_addr/cfg_wdata in die "live"-Register und kann sie
// ueber cfg_rdata zuruecklesen. Wirksam werden sie erst mit dem naechsten commit (= load des
// Kerns): dann kopiert der Baustein alle live-Register in die "aktiven" Register. Ein Lauf sieht
// also immer einen festen Satz Werte, auch wenn der Host waehrenddessen schreibt.
//
// Adressen (32 Bit je Register; Einzelheiten und Formate in ../README.md):
//   0x00  ID          nur lesen, 0x51430001 ("QC", Version 1)
//   0x01  ALLOW       Bit n erlaubt Opcode n; nicht erlaubte Opcodes fuehren zu reject
//   0x02  W_EFF       Guard-Breite in Bit (2..W); Koeffizienten ausserhalb geben guard
//   0x03  K_MAX       hoechster Nennerexponent k; darueber guard
//   0x04  BUDGET      hoechste Zahl ausgefuehrter Gatter; 0 = unbegrenzt; danach step_limit
//   0x05  FLAGS       Bit 0: Kuerzen durch 2 an
//   0x10..0x1F        Bank fuer bisher unsichere Groessen (Stufe 0 liest sie nicht; sie gehen
//                     an spaetere Rechenwerke weiter). Q2.30 = vorzeichenbehaftet, Wert/2^30;
//                     TURN = vorzeichenlos, Bruchteil einer vollen Drehung (Wert/2^32).
//   0x10  BETA_SYM    Q2.30   Vorgabe 0,5494056 (Zaehlpostulat)
//   0x11  EPSILON     Q2.30   Vorgabe artanh(BETA_SYM) = 0,6175295 (Maske, H45)
//   0x12  CHI         TURN    Neigung der Bandachse (H211), Vorgabe 0
//   0x13  DELTA_NU    TURN    Neutrino-Phase, Vorgabe 1/12 (pi/6, H173)
//   0x14  BAND_WEIGHT Q2.30   Gewicht der Baender (H209/H210, gesetzt), Vorgabe 1
//   0x15  X_OFFSET    Q2.30   gemeinsamer Versatz (H168/H207), Vorgabe 0,0396
//   0x16  ROT_ALPHA   TURN    Drehwinkel fuer ROT, Vorgabe 0
//   0x17  SWAP_X      Q2.30   Staerke fuer SWAP, Vorgabe 0
//   0x18  ADD_MU      Q2.30   Gewicht fuer ADD, Vorgabe 0
//   0x19  DROP_LAMBDA Q2.30   Gewicht fuer DROP, Vorgabe 0
//   0x1A  NOISE_EPS   Q2.30   Rauschstaerke fuer NOISE, Vorgabe 0
//   0x1B..0x1F        frei (Vorgabe 0)
module qcfg #(
    parameter integer W = 16
) (
    input wire clk,
    input wire rst,
    input wire commit,
    input wire cfg_we,
    input wire [4:0] cfg_addr,
    input wire [31:0] cfg_wdata,
    output reg [31:0] cfg_rdata,
    // aktive Werte fuer den Kern
    output reg [15:0] allow,
    output reg [5:0] w_eff,
    output reg [7:0] k_max,
    output reg [15:0] budget,
    output reg [1:0] reduce_en,     // Bit 0: durch 2 kuerzen, Bit 1: kanonisch durch sqrt(2)
    output reg mon_en,              // flags Bit 2: Normwaechter (qmon) an
    // aktive Bank 0x10..0x1F, Register n liegt bei phys[32*n +: 32]
    output reg [16*32-1:0] phys
);
    localparam [31:0] ID = 32'h5143_0001;

    reg [31:0] live [0:31];
    integer n, p;

    function automatic [31:0] default_value(input integer a);
        case (a)
            1: default_value = 32'h0000_01FF;           // alle neun Opcodes
            2: default_value = W;
            3: default_value = 32'd255;
            4: default_value = 32'd0;
            5: default_value = 32'd1;
            16: default_value = 32'h2329_761B;          // 0,5494056
            17: default_value = 32'h2785_9A90;          // 0,6175295
            19: default_value = 32'h1555_5555;          // 1/12 Drehung
            20: default_value = 32'h4000_0000;          // 1,0
            21: default_value = 32'h0288_CE70;          // 0,0396
            default: default_value = 32'd0;
        endcase
    endfunction

    // Breite auf 2..W begrenzen, damit der Guard nie mehr erlaubt als die Hardware fasst.
    function automatic [5:0] clamp_w(input [31:0] v);
        if (v < 2) clamp_w = 2;
        else if (v > W) clamp_w = W;
        else clamp_w = v[5:0];
    endfunction

    always @(*) cfg_rdata = (cfg_addr == 5'd0) ? ID : live[cfg_addr];

    always @(posedge clk) begin
        if (rst) begin
            for (p = 0; p < 32; p = p + 1) live[p] <= default_value(p);
        end else if (cfg_we && cfg_addr != 5'd0) begin
            live[cfg_addr] <= cfg_wdata;
        end
    end

    always @(posedge clk) begin
        if (rst) begin
            allow <= default_value(1);
            w_eff <= clamp_w(default_value(2));
            k_max <= default_value(3);
            budget <= default_value(4);
            reduce_en <= 2'b01;
            mon_en <= 1'b0;
            for (n = 0; n < 16; n = n + 1) phys[32*n +: 32] <= default_value(16 + n);
        end else if (commit) begin
            allow <= live[1][15:0];
            w_eff <= clamp_w(live[2]);
            k_max <= live[3][7:0];
            budget <= live[4][15:0];
            reduce_en <= live[5][1:0];
            mon_en <= live[5][2];
            for (n = 0; n < 16; n = n + 1) phys[32*n +: 32] <= live[16 + n];
        end
    end
endmodule
