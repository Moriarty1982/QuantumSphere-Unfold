"""Vergleich der Koide-Bedingung mit dem Kohaerenzfunktional der Photon-Uhr-Sonde (Erkundung, nicht blind).

Photon-Uhr-Sonde (v4.7.0-r90, Quelle v470-r15): C(tau) = 1 + eta |sum w_m e^{i phi_m}|^2 / (sum |w_m|)^2; Fenster: Selektor
erhalten, solange das Kohaerenzfunktional >= rho_V (erste Ordnung: 1 - Var(phi) >= rho_V); rho_V3 = 3/5, rho_V5 = 2/5,
rho_V8 = 7/9 (r90-Tabelle). r12.2(a): Duality-Drift je Auslesung tolerierbar fuer sin^2 alpha < 1/5 (alpha < 26.57 Grad).
Zeitzyklus (r16.9): Gewichte p_k = sqrt(m_k)/sum sqrt(m), Phasen -2 pi/3, 0, +2 pi/3 nach einem Drittel der Periode.
"""
import numpy as np

m = np.array([0.51099895, 105.6583755, 1776.86])
p = np.sqrt(m) / np.sqrt(m).sum()                       # e, mu, tau
phases = np.array([-2 * np.pi / 3, 2 * np.pi / 3, 0.0])  # e auf s+ (-1), mu auf conj s- (+1), tau auf w (0)
coh = abs(np.sum(p * np.exp(1j * phases))) ** 2 / np.sum(p) ** 2
print(f"(1) Kohaerenzfunktional |sum p e^(i phi)|^2/(sum p)^2 nach einem Drittel der Periode: {coh:.6f} (Koide: 1/2)")
var = np.sum(p * phases ** 2) - np.sum(p * phases) ** 2
print(f"    erste Ordnung 1 - Var(phi) = {1 - var:.4f} (Naeherung bei grosser Streuung unbrauchbar)")
for v, rho in (("V3", 3 / 5), ("V5", 2 / 5), ("V8", 7 / 9)):
    print(f"(2) Fenster {v}: rho = {rho:.4f}; Selektor erhalten (Kohaerenz >= rho): {coh >= rho}")
print(f"(3) Drift je Auslesung im Zeitzyklus: 2 pi/3 = 120 Grad auf den schwingenden Anteilen; Toleranz r12.2(a): 26.57 Grad")
