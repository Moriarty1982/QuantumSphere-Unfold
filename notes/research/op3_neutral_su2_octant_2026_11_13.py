"""Erkundung: Oktanten-Tripel fuer Spin j entlang dreier orthogonaler Achsen (13.11.2026, nicht blind, kein Datenvergleich).

Anlass: Bei Sumino (arXiv:0812.2103) transformiert Phi als U Phi O^T mit O in SO(3); im Vakuum sitzen die drei Generationen
auf drei orthogonalen Achsen dieser farb- und ladungsneutralen SU(2). Frage: Welcher Spin j gibt an diesen Achsen
Koide-Ueberlappung 1/2 und welche Bargmann-Phase?
Aufruf: python op3_neutral_su2_octant_2026_11_13.py
"""
import numpy as np


def spin_ops(j):
    m = np.arange(j, -j - 1, -1)
    Jz = np.diag(m)
    Jp = np.zeros((len(m), len(m)))
    for k in range(1, len(m)):
        Jp[k - 1, k] = np.sqrt(j * (j + 1) - m[k] * (m[k] + 1))
    Jx = (Jp + Jp.T) / 2
    Jy = (Jp - Jp.T) / 2j
    return Jx, Jy, Jz


def coherent(j, n):
    """Hoechstgewichtszustand entlang der Achse n."""
    Jx, Jy, Jz = spin_ops(j)
    w, V = np.linalg.eigh(n[0] * Jx + n[1] * Jy + n[2] * Jz)
    return V[:, np.argmax(w)]


if __name__ == "__main__":
    axes = [np.array(a, float) for a in ((1, 0, 0), (0, 1, 0), (0, 0, 1))]
    print("Spin-j-Zustaende entlang x, y, z (Oktant, Raumwinkel pi/2):")
    for j in (0.5, 1.0, 1.5, 2.0):
        q = [coherent(j, a) for a in axes]
        S = np.array([[np.vdot(a, b) for b in q] for a in q])
        fid = abs(S[0, 1]) ** 2
        r2 = (abs(S[0, 1]) ** 2 + abs(S[1, 2]) ** 2 + abs(S[2, 0]) ** 2) / 3
        ph = np.angle(S[0, 1] * S[1, 2] * S[2, 0])
        K = (1 + 2 * r2) / 3
        print(f"  j = {j}: Treue {fid:.4f} (= (1/2)^(2j) {0.5 ** (2 * j):.4f}), rho^2 = {r2:.4f}, K = {K:.4f}, "
              f"Bargmann-Phase {abs(ph):.4f} (j * pi/2 mod 2pi = {(j * np.pi / 2) % (2 * np.pi):.4f})")
    print("  -> nur j = 1/2 gibt rho^2 = 1/2 (Koide) und die Phase pi/4.")
    # reelle Vektoren (SO(3)-Vektorindex, wie Suminos zweiter Index): orthogonal, Ueberlappung 0, keine Phase
    V = np.eye(3)
    print(f"  SO(3)-Vektoren entlang der Achsen: Ueberlappungen {np.round(V.T @ V - np.eye(3), 3).ravel().tolist()} -> rho^2 = 0, keine Phase")
