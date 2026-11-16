"""Testsuche zur Querungs-Lesart (v4.10.0-r24.4): Flaechenschritte und Linien.  (Erkundung, nicht blind.)

Einheiten G = c = hbar = 1.  T-Regel: nur j = 1/2, gamma_T = ln 2 / (pi sqrt 3).
(1) Flaechenquant einer j = 1/2-Punktierung: a = 8 pi gamma_T sqrt(j(j+1)) = 4 ln 2  ->  Bekenstein-Mukhanov mit alpha = 4 ln 2.
(2) Schwarzschild: Uebergangsfrequenz omega_0 = alpha / (32 pi M) = ln 2 * T_H (T_H = 1/(8 pi M)).
    Grundton (l = m = 2, n = 0) M omega = 0.37367 -> Verhaeltnis omega_QNM / omega_0.
(3) Kerr: omega_n = alpha kappa n / (8 pi) + m Omega_H; Lage des 220-Tons zwischen den Linien fuer typische Endspins
    (Fit von Berti, Cardoso, Will 2006: M omega_220 = 1.5251 - 1.1568 (1 - a)^0.1292).
(4) M-Regel zum Vergleich: alle j mit Gewicht 2, gamma_M = 0.237533: Flaechenquanten 8 pi gamma_M sqrt(j(j+1)) sind nicht
    aequidistant; Abstaende zwischen Summen werden dicht (keine Linien).
"""
import numpy as np

gT = np.log(2) / (np.pi * np.sqrt(3)); gM = 0.237533
a_half = 8 * np.pi * gT * np.sqrt(0.75)
print(f"(1) Flaechenquant j = 1/2 in T: a = {a_half:.6f} = 4 ln 2 = {4*np.log(2):.6f}")
alpha = a_half
w0 = alpha / (32 * np.pi)          # in Einheiten 1/M
TH = 1 / (8 * np.pi)
print(f"(2) Schwarzschild: M omega_0 = {w0:.6f} = ln2 * M T_H = {np.log(2)*TH:.6f}; M omega_220 = 0.37367;"
      f" Verhaeltnis = {0.37367 / w0:.3f} (nicht ganzzahlig -> 220-Ton liegt zwischen zwei Linien)")
for a in (0.0, 0.5, 0.69, 0.8, 0.9):
    r = np.sqrt(1 - a * a); kappa = r / (2 * (1 + r)); Om = a / (2 * (1 + r))
    w220 = 1.5251 - 1.1568 * (1 - a) ** 0.1292
    step = alpha * kappa / (8 * np.pi); n = (w220 - 2 * Om) / step
    print(f"(3) Kerr a = {a:.2f}: M omega_220 = {w220:.4f}, Linienabstand M dw = {step:.5f}, Lage n = {n:.3f}"
          f" (Abstand zur naechsten Linie {abs(n - round(n)):.3f} Linienabstaende)")
js = np.arange(0.5, 6.01, 0.5); quanta = 8 * np.pi * gM * np.sqrt(js * (js + 1))
print("(4) M-Regel: Flaechenquanten j = 1/2..3:", np.round(quanta[:6], 4), "-> Verhaeltnisse nicht rational, Summen dicht")
