"""k229: Test H107 (Vorab-Notiz Vorab_Notiz_H107_Verschachtelte_Normierung.md, Commit 30a4a50).

Konstruktion wie festgelegt.  Basis der Zyklusachse z; Kaesten |00>,|01>,|10>,|11>; HS(7)-Haelften H0 = {00, 01}, H1 = {10, 11}.
g_k = sqrt(1-w) |n_k>|n_k> + sqrt(w) eps;  n_k auf dem Kegel psi um z.
Kastengewichte des Triplettanteils: p00 = c^4, p01 = p10 = c^2 s^2, p11 = s^4 mit c = cos(psi/2), s = sin(psi/2).
Mechanismen N1-N10 (N8-N10 vor der Rechnung ergaenzt, Commit 44cda89): w = F(psi).  Loesungen (psi, w) aus |<g_j|g_k>|^2 = 1/2 und w = F(psi).
Kriterium: bestaetigt, wenn genau ein Mechanismus |phi - 0.666665| <= 0.0002 trifft; mehrdeutig bei mehreren; sonst widerlegt.
AUSFUEHRUNG ERST NACH FREIGABE DES AUTORS.
"""
import numpy as np

TARGET, TOL = 0.666665, 2e-4
eps = np.array([0, 1, -1, 0], complex) / np.sqrt(2)


def coh(n):
    th, ph = np.arccos(np.clip(n[2], -1, 1)), np.arctan2(n[1], n[0])
    return np.array([np.cos(th / 2), np.exp(1j * ph) * np.sin(th / 2)])


def dirs(psi):
    return [np.array([np.sin(psi) * np.cos(2 * np.pi * k / 3), np.sin(psi) * np.sin(2 * np.pi * k / 3), np.cos(psi)]) for k in range(3)]


def states(w, psi):
    return [np.sqrt(1 - w) * np.kron(coh(d), coh(d)) + np.sqrt(w) * eps for d in dirs(psi)]


def overlap2(g):
    return abs(np.vdot(g[0], g[1])) ** 2


def phase(g):
    return abs(np.angle(np.vdot(g[0], g[1]) * np.vdot(g[1], g[2]) * np.vdot(g[2], g[0])))


def boxes(psi):
    c2, s2 = np.cos(psi / 2) ** 2, np.sin(psi / 2) ** 2
    return {"00": c2 * c2, "01": c2 * s2, "10": c2 * s2, "11": s2 * s2}


MECH = {
    "N1 mittleres HS(6)": lambda p: p["01"],
    "N2 leichtes HS(6)": lambda p: p["11"],
    "N3 schweres HS(6)": lambda p: p["00"],
    "N4 beide mittleren HS(6)": lambda p: p["01"] + p["10"],
    "N5 mittleres HS(6) in H0 normiert": lambda p: p["01"] / (p["00"] + p["01"]),
    "N6 mittleres HS(6) in H1 normiert": lambda p: p["10"] / (p["10"] + p["11"]),
    "N7 leichtes HS(6) in H1 normiert": lambda p: p["11"] / (p["10"] + p["11"]),
    # Ergaenzung vor der Rechnung (Commit 44cda89): volle Grammatik von HS(8)
    "N8 ganze HS(7)-Haelfte H0": lambda p: p["00"] + p["01"],
    "N9 ganze HS(7)-Haelfte H1": lambda p: p["10"] + p["11"],
    "N10 schweres HS(6) in H0 normiert": lambda p: p["00"] / (p["00"] + p["01"]),
}


def solve(F):
    # gemeinsame Bedingung: h(psi) = overlap2(states(F(psi), psi)) - 1/2 = 0
    def h(psi):
        w = F(boxes(psi))
        if not (0 <= w <= 1):
            return np.nan
        return overlap2(states(w, psi)) - 0.5
    grid = np.linspace(1e-4, np.pi - 1e-4, 40001); vals = np.array([h(p) for p in grid]); sols = []
    for i in range(len(grid) - 1):
        a, b = vals[i], vals[i + 1]
        if np.isfinite(a) and np.isfinite(b) and np.sign(a) != np.sign(b):
            lo, hi = grid[i], grid[i + 1]
            for _ in range(80):
                mid = (lo + hi) / 2
                if np.sign(h(mid)) == np.sign(h(lo)): lo = mid
                else: hi = mid
            sols.append((lo + hi) / 2)
    return sols


hits, attempts = [], 0
for name, F in MECH.items():
    sols = solve(F)
    if not sols:
        print(f"{name}: keine Loesung"); continue
    for psi in sols:
        w = F(boxes(psi)); g = states(w, psi); ph = phase(g); attempts += 1
        ok = abs(ph - TARGET) <= TOL
        if ok: hits.append(name)
        print(f"{name}: psi = {np.degrees(psi):8.4f} Grad, w = {w:.6f}, |Ueberlappung|^2 = {overlap2(g):.6f}, phi = {ph:.6f},"
              f" phi - Ziel = {ph - TARGET:+.6f}" + ("  -> TREFFER" if ok else ""))
verdict = "bestaetigt" if len(set(hits)) == 1 else ("mehrdeutig" if hits else "widerlegt")
print(f"Versuche: {attempts}; Treffer: {sorted(set(hits))}; Urteil: {verdict}")
