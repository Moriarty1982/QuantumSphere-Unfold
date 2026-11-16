"""k228: Test H106 (Vorab-Notiz Vorab_Notiz_H106_Singulett_Restbiegung.md, Commit abf54a0).

Konstruktion wie festgelegt: n_k auf einem Kegel (halber Oeffnungswinkel psi, Azimut 2 pi k / 3), |n> kohaerenter Spin-1/2-Zustand,
Kopienindex C^2 (x) C^2, eps = (|01> - |10>)/sqrt2.
  M0 (Kontrolle, r15.3): g_k = |n_k>|n_k>
  M1: g_k = sqrt(3/4) |n_k>|n_k> + sqrt(1/4) eps
  M2: g_k = |n_k> (x) |n_{k+1}>
psi aus |<g_j|g_k>|^2 = 1/2 (alle Loesungen in (0, pi) per Vorzeichenwechsel und Bisektion); Vorhersage phi = |arg Bargmann|.
Kriterium: bestaetigt, wenn eine Loesung |phi - 2/3| <= 0.001.
"""
import numpy as np

TARGET, TOL = 2 / 3, 1e-3
eps = np.array([0, 1, -1, 0], complex) / np.sqrt(2)


def coh(n):
    th, ph = np.arccos(np.clip(n[2], -1, 1)), np.arctan2(n[1], n[0])
    return np.array([np.cos(th / 2), np.exp(1j * ph) * np.sin(th / 2)])


def dirs(psi):
    return [np.array([np.sin(psi) * np.cos(2 * np.pi * k / 3), np.sin(psi) * np.sin(2 * np.pi * k / 3), np.cos(psi)]) for k in range(3)]


def states(mech, psi):
    s = [coh(d) for d in dirs(psi)]
    if mech == "M0":
        return [np.kron(s[k], s[k]) for k in range(3)]
    if mech == "M1":
        return [np.sqrt(3 / 4) * np.kron(s[k], s[k]) + np.sqrt(1 / 4) * eps for k in range(3)]
    if mech == "M2":
        return [np.kron(s[k], s[(k + 1) % 3]) for k in range(3)]


def overlap2(g):
    g = [x / np.linalg.norm(x) for x in g]
    return abs(np.vdot(g[0], g[1])) ** 2


def phase(g):
    g = [x / np.linalg.norm(x) for x in g]
    return abs(np.angle(np.vdot(g[0], g[1]) * np.vdot(g[1], g[2]) * np.vdot(g[2], g[0])))


def solutions(mech):
    f = lambda p: overlap2(states(mech, p)) - 0.5
    grid = np.linspace(1e-4, np.pi - 1e-4, 20001); vals = np.array([f(p) for p in grid]); out = []
    for i in range(len(grid) - 1):
        if np.sign(vals[i]) != np.sign(vals[i + 1]):
            lo, hi = grid[i], grid[i + 1]
            for _ in range(80):
                mid = (lo + hi) / 2
                if np.sign(f(mid)) == np.sign(f(lo)): lo = mid
                else: hi = mid
            out.append((lo + hi) / 2)
    return out


hits = 0; attempts = 0
for mech in ("M0", "M1", "M2"):
    sols = solutions(mech)
    if not sols:
        print(f"{mech}: keine Loesung mit Ueberlappung 1/2")
    for psi in sols:
        g = states(mech, psi); ph = phase(g)
        G = np.array([[np.vdot(a / np.linalg.norm(a), b / np.linalg.norm(b)) for b in g] for a in g])
        sing = np.mean([abs(np.vdot(eps, x / np.linalg.norm(x))) ** 2 for x in g])
        ok = abs(ph - TARGET) <= TOL
        if mech != "M0":
            attempts += 1; hits += ok
        print(f"{mech}: psi = {np.degrees(psi):8.4f} Grad, |Ueberlappung|^2 = {overlap2(g):.6f}, phi = {ph:.6f},"
              f" phi - 2/3 = {ph - TARGET:+.6f}, det G = {np.linalg.det(G).real:.6f}, Singulettgewicht = {sing:.4f}"
              + ("" if mech == "M0" else ("  -> TREFFER" if ok else "  -> kein Treffer")))
print(f"Versuche (M1, M2, alle Loesungen): {attempts}; Treffer: {hits}; Urteil: {'bestaetigt' if hits else 'widerlegt'}")
