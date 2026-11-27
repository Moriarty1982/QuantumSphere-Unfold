`timescale 1ns/1ps
// Boot-Monitor des Quanten-Coprozessors: liest ein Programmabbild (QIMG) aus dem Programmspeicher, prueft
// Kopf und Pruefsumme und fuehrt es auf qcop2_top aus. Programme lassen sich so ohne Neubau der Hardware
// tauschen: der Host schreibt ein neues Abbild in den Speicher und startet neu. Die Idee entspricht einer
// kleinen virtuellen Maschine mit portablem Programmformat; die Befehle sind die des Kerns.
//
// Abbild (32-Bit-Worte, Einzelheiten in ../README.md und qimage.py):
//   0  MAGIC   0x51494D47 ("QIMG")
//   1  VERSION[31:16] = 1, N[15:0] = Zahl der Programmworte
//   2  SUM     Summe der N Programmworte mod 2^32
//   3.. Programm, Befehl in [31:28]:
//      0 HALT                      Ende (done)
//      1 CFG   adr = [20:16]       naechstes Wort = Wert; schreibt das Konfigurationsregister
//      2 LOAD                      neuer Lauf: Zustand |00>, Konfiguration wird aktiv
//      3 GATE  op = [7:4], ziel = [0]
//      4 EMIT                      gibt Zustand und Status einmal aus (emit = 1 fuer einen Takt)
//   Laeuft das Programm ohne HALT ueber N Worte hinaus, endet es ebenfalls mit done.
// Monitor-Status boot_status: 0 idle, 1 running, 2 done, 3 reject (falsches Magic/Version/Laenge/Summe,
// unbekannter Befehl). Der Programmspeicher wird synchron gelesen (eine Taktstufe, passt zu Block-RAM); nach jeder
// neuen Adresse wartet der Monitor einen Takt (wait_rd), dann liegt das Wort an. Ein Programmwort braucht zwei Takte.
module qboot #(
    parameter integer AW = 10  // Adressbreite des Programmspeichers
) (
    input wire clk,
    input wire rst,
    input wire start,
    output reg [AW-1:0] mem_addr,
    input wire [31:0] mem_data,
    // Steuerung des Kerns
    output reg load,
    output reg op_valid,
    output reg [3:0] opcode,
    output reg target,
    output reg cfg_we,
    output reg [4:0] cfg_addr,
    output reg [31:0] cfg_wdata,
    output reg emit,
    output reg [1:0] boot_status,
    output reg [15:0] pc_out
);
    localparam [31:0] MAGIC = 32'h5149_4D47;
    localparam [15:0] VERSION = 16'd1;
    localparam [1:0] IDLE = 0, RUNNING = 1, DONE = 2, REJECT = 3;
    localparam [3:0] I_HALT = 0, I_CFG = 1, I_LOAD = 2, I_GATE = 3, I_EMIT = 4;
    localparam [3:0] S_IDLE = 0, S_MAGIC = 1, S_VER = 2, S_SUM = 3, S_CHECK = 4,
                     S_EXEC = 6, S_VALUE = 7;

    reg [3:0] s;
    reg [15:0] n, i;
    reg [31:0] sum, want;
    reg [4:0] pend_addr;
    reg wait_rd;

    always @(posedge clk) begin
        load <= 1'b0;
        op_valid <= 1'b0;
        cfg_we <= 1'b0;
        emit <= 1'b0;
        if (rst) begin
            s <= S_IDLE;
            boot_status <= IDLE;
            mem_addr <= 0;
            wait_rd <= 1'b0;
            opcode <= 0;
            target <= 0;
            cfg_addr <= 0;
            cfg_wdata <= 0;
            pc_out <= 0;
        end else if (start) begin
            // Wort 0 anfordern; es liegt im naechsten Takt an.
            mem_addr <= 0;
            wait_rd <= 1'b1;
            s <= S_MAGIC;
            boot_status <= RUNNING;
        end else if (wait_rd) begin
            wait_rd <= 1'b0;
        end else begin
            case (s)
                S_MAGIC: begin
                    if (mem_data != MAGIC) begin
                        s <= S_IDLE;
                        boot_status <= REJECT;
                    end else begin
                        mem_addr <= 1;
                        wait_rd <= 1'b1;
                        s <= S_VER;
                    end
                end
                S_VER: begin
                    n <= mem_data[15:0];
                    if (mem_data[31:16] != VERSION || {16'd0, mem_data[15:0]} + 32'd3 > (32'd1 << AW)) begin
                        s <= S_IDLE;
                        boot_status <= REJECT;
                    end else begin
                        mem_addr <= 2;
                        wait_rd <= 1'b1;
                        s <= S_SUM;
                    end
                end
                S_SUM: begin
                    want <= mem_data;
                    sum <= 32'd0;
                    i <= 16'd0;
                    mem_addr <= 3;
                    wait_rd <= 1'b1;
                    s <= S_CHECK;
                end
                S_CHECK: begin
                    // Erster Durchgang: Pruefsumme ueber alle Programmworte.
                    if (i == n) begin
                        if (sum != want) begin
                            s <= S_IDLE;
                            boot_status <= REJECT;
                        end else begin
                            i <= 16'd0;
                            mem_addr <= 3;
                            wait_rd <= 1'b1;
                            s <= S_EXEC;
                        end
                    end else begin
                        sum <= sum + mem_data;
                        i <= i + 16'd1;
                        mem_addr <= mem_addr + 1'b1;
                        wait_rd <= 1'b1;
                    end
                end
                S_EXEC: begin
                    pc_out <= i;
                    if (i == n) begin
                        s <= S_IDLE;
                        boot_status <= DONE;
                    end else begin
                        i <= i + 16'd1;
                        mem_addr <= mem_addr + 1'b1;
                        wait_rd <= 1'b1;
                        case (mem_data[31:28])
                            I_HALT: begin
                                s <= S_IDLE;
                                boot_status <= DONE;
                            end
                            I_CFG: begin
                                pend_addr <= mem_data[20:16];
                                s <= S_VALUE;
                            end
                            I_LOAD: begin
                                load <= 1'b1;
                                s <= S_EXEC;
                            end
                            I_GATE: begin
                                opcode <= mem_data[7:4];
                                target <= mem_data[0];
                                op_valid <= 1'b1;
                                s <= S_EXEC;
                            end
                            I_EMIT: begin
                                emit <= 1'b1;
                                s <= S_EXEC;
                            end
                            default: begin
                                s <= S_IDLE;
                                boot_status <= REJECT;
                            end
                        endcase
                    end
                end
                S_VALUE: begin
                    if (i == n) begin
                        // CFG ohne Wert am Programmende
                        s <= S_IDLE;
                        boot_status <= REJECT;
                    end else begin
                        cfg_addr <= pend_addr;
                        cfg_wdata <= mem_data;
                        cfg_we <= 1'b1;
                        i <= i + 16'd1;
                        mem_addr <= mem_addr + 1'b1;
                        wait_rd <= 1'b1;
                        s <= S_EXEC;
                    end
                end
                default: ;
            endcase
        end
    end
endmodule
