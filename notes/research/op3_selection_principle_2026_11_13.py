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


def coherent(n):
    n = np.array(n, float) / np.linalg.norm(n)
    th, ph = np.arccos(np.clip(n[2], -1, 1)), np.arctan2(n[1], n[0])
    return np.array([np.cos(th / 2), np.exp(1j * ph) * np.sin(th / 2)])


def rot(axis, ang):
    a = np.array(axis, float) / np.linalg.norm(axis)
    K = np.array([[0, -a[2], a[1]], [a[2], 0, -a[0]], [-a[1], a[0], 0]])
    return np.eye(3) + np.sin(ang) * K + (1 - np.cos(ang)) * K @ K


def orbit_K(axis3, n0):
    R = rot(axis3, 2 * np.pi / 3)
    ns = [np.array(n0, float), R @ n0, R @ R @ n0]
    q = [coherent(n) for n in ns]
    S = np.array([[np.vdot(a, b) for b in q] for a in q])
    r2 = (abs(S[0, 1]) ** 2 + abs(S[1, 2]) ** 2 + abs(S[2, 0]) ** 2) / 3
    return (1 + 2 * r2) / 3, abs(np.angle(S[0, 1] * S[1, 2] * S[2, 0])), abs(np.linalg.det(S))


if __name__ == "__main__":
    print("\n== Teil A: Treue 1/2 aus der Geometrie einer endlichen Untergruppe von SU(2) ==")
    ax = np.array([1.0, 1, 1]) / np.sqrt(3)
    err = 0
    for beta in np.linspace(0.05, np.pi / 2, 40):
        perp = np.array([1.0, -1, 0]) / np.sqrt(2)
        n0 = np.cos(beta) * ax + np.sin(beta) * perp
        K, _, _ = orbit_K(ax, n0)
        err = max(err, abs(K - (1 + np.cos(beta) ** 2) / 2))
    print(f"    Bahn eines Qubits unter Winkel beta zur dreizaehligen Achse: K = (1 + cos^2 beta)/2 (max. Fehler {err:.1e})")
    print("    -> K = 2/3 genau fuer cos^2 beta = 1/3 (magischer Winkel); die Gram-Matrix hat stets Rang 2 (Rand des Bogens).")
    # Winkel zwischen drei- und zweizaehligen Achsen in den Polyedergruppen
    phi = (1 + np.sqrt(5)) / 2
    groups = {
        "Tetraeder (A4)": ([(1, 1, 1)], [(1, 0, 0), (0, 1, 0), (0, 0, 1)]),
        "Oktaeder (S4), Koordinatenachsen": ([(1, 1, 1)], [(1, 0, 0)]),
        "Oktaeder (S4), Kantenachsen": ([(1, 1, 1)], [(1, 1, 0), (1, -1, 0), (0, 1, 1), (0, 1, -1), (1, 0, 1), (1, 0, -1)]),
        "Ikosaeder (A5)": ([(1, 1, 1)], [(1, 0, 0), (0, 1, 0), (0, 0, 1), (phi, 1 / phi, 1), (1 / phi, 1, phi), (1, phi, 1 / phi),
                                         (phi, -1 / phi, 1), (-1, phi, 1 / phi), (1 / phi, -1, phi)]),
    }
    for g, (a3s, a2s) in groups.items():
        Ks = set()
        for a3 in a3s:
            for a2 in a2s:
                c2 = (np.dot(a3, a2) / np.linalg.norm(a3) / np.linalg.norm(a2)) ** 2
                Ks.add(float(round((1 + c2) / 2, 4)))
        print(f"    {g:34s}: K-Werte der Bahnen zweizaehliger Eigenzustaende {sorted(Ks)}")
    K, Phi, det = orbit_K(ax, np.array([1.0, 0, 0]))
    print(f"    A4: Eigenzustand der Klein-Achse x, Bahn unter der Drehung um (1,1,1): K = {K:.6f}, Phase {Phi:.6f}, det {det:.1e}")
