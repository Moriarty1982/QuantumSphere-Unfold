"""OP3, Weg des Autors „Renormierung“: Wie aendert sich die Koide-Phase der geladenen Leptonen mit der Skala?
(Erkundung, nicht blind: die Richtung folgt schon aus den laufenden Massen bei M_Z in H1, v4.8.0-r12.)

Konvention wie H1 (k14): sqrt(m_k) Fourier-Phase delta (mod 2 pi/3), K = sum m / (sum sqrt m)^2.  Die Bargmann-Phase der Runden
(r14, Spin-1-Dreieck) ist phi = 3 delta (geprueft unten an zwei Faellen).
(1) phi = 3 delta: Polmassen (phi ~ 2/3) und Spin-1-Dreieck (Wurzelgewichte 0.7927 / 0.1952 / 0.0120 -> phi 0.679042).
(2) Laufende Massen bei M_Z (Eingaben aus H1/k14): K und phi.
(3) Ein-Schleifen-QED-Laufen ab den Polmassen, m(mu) = M [1 - (alpha/pi)(1 + (3/2) ln(mu/M))], fuer mu ab m_tau (alle Leptonen aktiv),
    alpha = 1/137.036 fest: Richtung und Groesse der Aenderung von phi.
(4) Ziel des Spin-1-Dreiecks: phi = 0.679042.  Liegt es in Laufrichtung?
"""
import numpy as np

w = np.exp(2j * np.pi / 3); k = np.arange(3)


def K_delta(m):
    v = np.sqrt(np.sort(m))
    c = np.sqrt(2) / 3 * np.sum(v * np.conj(w ** k))
    return np.sum(m) / np.sum(v) ** 2, np.mod(np.angle(c), 2 * np.pi / 3)


pole = np.array([0.51099895069, 105.6583755, 1776.93])            # MeV, wie op3_mass_backsolve (CODATA 2022, PDG 2025)
K, d = K_delta(pole)
print(f"(1) Polmassen: K = {K:.6f}, delta = {d:.6f}, 3 delta = {3*d:.6f} (Lepton-Phase der Runden 2/3 = {2/3:.6f})")
wts = np.array([0.0120, 0.1952, 0.7927])                           # Wurzelgewichte des Spin-1-Dreiecks (r25.5), gerundet
cpsi = np.sqrt((2 * np.sqrt(2) - 1) / 3); c2 = (1 + cpsi) / 2; s2 = 1 - c2
wex = np.array([s2 * s2, 2 * c2 * s2, c2 * c2])                    # exakt
K1, d1 = K_delta(wex ** 2)
print(f"    Spin-1-Dreieck (Wurzelgewichte exakt {np.round(wex, 5)}): K = {K1:.6f}, 3 delta = {3*d1:.6f} (0.679042)")

mz = np.array([2.77713e-6, 5.85042e-4, 0.99378e-2])               # Yukawa bei M_Z aus H1/k14 (Verhaeltnisse = Massenverhaeltnisse)
K2, d2 = K_delta(mz)
print(f"(2) laufende Massen bei M_Z (H1): K = {K2:.6f}, delta = {d2:.6f}, 3 delta = {3*d2:.6f};"
      f" Aenderung gegen Polmassen {3*d2 - 3*d:+.6f}")

alpha = 1 / 137.036
print("(3) Ein-Schleifen-QED ab den Polmassen:")
for mu in (1776.93, 1e4, 91187.6, 1e6, 1e9):
    m = pole * (1 - alpha / np.pi * (1 + 1.5 * np.log(mu / pole)))
    Km, dm = K_delta(m)
    print(f"    mu = {mu:10.4g} MeV: K = {Km:.6f}, 3 delta = {3*dm:.6f}, Aenderung {3*dm - 3*d:+.6f}")

print(f"(4) Spin-1-Dreieck 0.679042 liegt {0.679042 - 3*d:+.6f} ueber der Polmassen-Phase; das Laufen zu hoeheren Skalen senkt die Phase"
      f" -> Abstand waechst.  Unterhalb der Polmassen ist die MSbar-Masse eines Leptons nicht definiert (Entkopplung).")
