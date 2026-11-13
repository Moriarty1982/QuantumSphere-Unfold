"""k223: Test H101 (Vorab_Notiz_H101_Maske_hebt_Elektron.md).

Exaktes Oktanten-Tripel C (Auslesung A), Maske W_l = diag(0,0,-3) in Form K: M = D C D, D = exp(eps W).
eps so, dass m_min/m_max = m_e/m_tau; Vorhersage m_mu/m_tau und K.
Aufruf: python k223_test_h101.py
"""
import numpy as np
from scipy.optimize import brentq

POL = np.array([0.51099895, 105.6583755, 1776.93])
R_E_TAU, R_MU_TAU = POL[0] / POL[2], POL[1] / POL[2]
K_POL = POL.sum() / np.sqrt(POL).sum() ** 2
P = np.roll(np.eye(3), 1, axis=0)
z = np.exp(1j * np.pi / 12) / np.sqrt(2)
C = np.eye(3) + z * P + np.conj(z) * P.T


def masses(M):
    ev = np.linalg.eigvalsh((M + M.conj().T) / 2)
    return np.sort(ev ** 2)


def form_K(eps, slot=2):
    w = np.zeros(3); w[slot] = -3.0
    D = np.diag(np.exp(eps * w))
    return D @ C @ D


def form_lin(eps, slot=2):
    W = np.zeros((3, 3)); W[slot, slot] = -3.0
    return C + eps * (W @ C + C @ W)


def solve(form, slot=2):
    f = lambda e: (lambda m: m[0] / m[2])(masses(form(e, slot))) - R_E_TAU
    sols = []
    grid = np.concatenate([-np.logspace(-6, 0.5, 400)[::-1], np.logspace(-6, 0.5, 400)])
    vals = [f(e) for e in grid]
    for i in range(len(grid) - 1):
        if np.sign(vals[i]) != np.sign(vals[i + 1]) and grid[i] * grid[i + 1] > 0:
            sols.append(brentq(f, grid[i], grid[i + 1]))
    return sorted(sols, key=abs)


def report(lab, form, eps, slot=2):
    m = masses(form(eps, slot))
    K = m.sum() / np.sqrt(m).sum() ** 2
    r = m[1] / m[2]
    return f"{lab}: eps = {eps:+.6f}, m_e/m_tau = {m[0] / m[2]:.4e}, m_mu/m_tau = {r:.6f} (Daten {R_MU_TAU:.6f}, " \
           f"Abw. {100 * (r - R_MU_TAU) / R_MU_TAU:+.2f} %), K = {K:.6f} (Pol {K_POL:.6f})"


if __name__ == "__main__":
    print(f"Kontrolle: Spektrum von C = {np.round(np.linalg.eigvalsh(C), 6)} (ein Eigenwert null)")
    sols = {s: solve(form_K, s) for s in range(3)}
    for s, ss in sols.items():
        print(f"Platz {s + 1}: Loesungen eps = {[round(x, 6) for x in ss]}")
    sK = sols[2]
    if not sK:
        print("H101: keine Loesung -> widerlegt")
    else:
        eps = sK[0]
        print(report("Form K (primaer)", form_K, eps))
        m = masses(form_K(eps))
        a = abs(m[1] / m[2] - R_MU_TAU) / R_MU_TAU <= 0.01
        Kp = m.sum() / np.sqrt(m).sum() ** 2
        b = abs(Kp - K_POL) <= 1e-3
        print(f"H101a: {'bestaetigt' if a else 'widerlegt'};  H101b: {'vertraeglich' if b else 'nicht vertraeglich'};  "
              f"H101: {'bestaetigt' if (a and b) else 'widerlegt'}")
        for e in sK[1:]:
            print("  weitere Loesung, " + report("Form K", form_K, e))
    sl = solve(form_lin)
    for e in sl[:2]:
        print("Nebenrechnung, " + report("lineare Form r47", form_lin, e))
