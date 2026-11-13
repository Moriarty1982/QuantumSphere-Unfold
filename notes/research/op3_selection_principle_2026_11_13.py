"""Rueckwaertssuche: was ein Auswahlprinzip fuer die geladenen Leptonen festlegen muss (13.11.2026, nicht blind).

Gram-Lesart A, s_k = 1 + 2 rho cos(theta + 2 pi k/3). Rand des Bogens (Qubit-Oktant): rho^2 = 1/2, theta = pi/12, s_min = 0.
(1) Bei rho^2 = 1/2 ist der kleinste Eigenwert in erster Ordnung der Abstand vom Rand: s_min ~ (pi/12 - theta).
(2) Geladene Leptonen (Polmassen): Vergleich von sqrt(m_e)/<sqrt m> mit pi/12 - theta_e.
(3) Zwei Zahlen sind festzulegen: Treue 1/2 (Koide) und der Abstand vom Qubit-Rand (Elektronmasse).
Aufruf: python op3_selection_principle_2026_11_13.py
"""
import numpy as np

POL = np.array([0.51099895, 105.6583755, 1776.93])
K3 = np.arange(3)


def lepton_phase(m):
    v = np.sqrt(m); x = v / v.mean() - 1
    A = np.sqrt(2 * (x ** 2).sum() / 3)
    return np.arccos(np.clip(4 * np.prod(x) / A ** 3, -1, 1)) / 3


if __name__ == "__main__":
    te = lepton_phase(POL)
    s = 1 + np.sqrt(2) * np.cos(te + 2 * np.pi * K3 / 3)
    smin = s.min()
    d = np.pi / 12 - te
    print(f"theta_e = {te:.6f}; Abstand vom Rand pi/12 - theta_e = {d:.6f}")
    print(f"s_min = sqrt(m_e)/<sqrt m> = {smin:.6f}; Verhaeltnis s_min/Abstand = {smin / d:.4f} "
          f"(erste Ordnung: sqrt2 sin(3pi/4) = 1, zweite Ordnung korrigiert)")
    # exakte Beziehung: s_min = 1 + sqrt2 cos(theta + 2pi/3) = 1 - sqrt2 cos(pi/3 - theta)... Taylor um pi/12
    for th in (np.pi / 12, 0.25, te, 0.18, 0.10):
        sm = (1 + np.sqrt(2) * np.cos(th + 2 * np.pi * K3 / 3)).min()
        print(f"   theta = {th:.4f}: s_min = {sm:.5f}, Abstand {np.pi / 12 - th:+.5f}, m_min/m_max = {(sm / (1 + np.sqrt(2) * np.cos(th))) ** 2:.3e}")
    print(f"Massenverhaeltnis m_e/m_tau = {POL[0] / POL[2]:.3e}; Bargmann-Abstand pi/4 - 3 theta_e = {np.pi / 4 - 3 * te:.5f}")
