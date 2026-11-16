"""k230: Test H108 (Vorab-Notiz Vorab_Notiz_H108_Verschraenkte_Generationen.md).

Generation k: Majorana-Paar {n_k, b_k}, Zustand g_k ~ |n_k>|b_k> + |b_k>|n_k> (normiert), n_k auf dem Kegel psi um z, Azimut 2 pi k / 3.
  E1: b_k = n_{k+1}   E2: b_k = +z   E3: b_k = -z   E4: b_k = -n_k   E5: b_k = -n_{k+1}
psi aus |<g_j|g_k>|^2 = 1/2 (alle Loesungen); Vorhersage phi = |arg Bargmann|.
Kriterium: bestaetigt, wenn genau ein Mechanismus |phi - 0.666665| <= 0.0002 trifft; mehrdeutig bei mehreren; sonst widerlegt.
"""
import numpy as np

TARGET, TOL = 0.666665, 2e-4
Z = np.array([0.0, 0.0, 1.0])


def coh(n):
    n = np.asarray(n, float) / np.linalg.norm(n)
    th, ph = np.arccos(np.clip(n[2], -1, 1)), np.arctan2(n[1], n[0])
    return np.array([np.cos(th / 2), np.exp(1j * ph) * np.sin(th / 2)])


def dirs(psi):
    return [np.array([np.sin(psi) * np.cos(2 * np.pi * k / 3), np.sin(psi) * np.sin(2 * np.pi * k / 3), np.cos(psi)]) for k in range(3)]


def majorana(a, b):
    v = np.kron(coh(a), coh(b)) + np.kron(coh(b), coh(a))
    return v / np.linalg.norm(v)


SECOND = {
    "E1 Nachbar n_(k+1)": lambda n, k: n[(k + 1) % 3],
    "E2 Pol +z": lambda n, k: Z,
    "E3 Pol -z": lambda n, k: -Z,
    "E4 Gegenpunkt -n_k (polar)": lambda n, k: -n[k],
    "E5 Gegenpunkt des Nachbarn -n_(k+1)": lambda n, k: -n[(k + 1) % 3],
}


def states(mech, psi):
    n = dirs(psi)
    return [majorana(n[k], SECOND[mech](n, k)) for k in range(3)]


def overlap2(g):
    return abs(np.vdot(g[0], g[1])) ** 2


def phase(g):
    return abs(np.angle(np.vdot(g[0], g[1]) * np.vdot(g[1], g[2]) * np.vdot(g[2], g[0])))


def solve(mech):
    f = lambda p: overlap2(states(mech, p)) - 0.5
    xs = np.linspace(1e-3, np.pi - 1e-3, 20001); vs = np.array([f(x) for x in xs]); out = []
    for i in range(len(xs) - 1):
        if np.isfinite(vs[i]) and np.isfinite(vs[i + 1]) and np.sign(vs[i]) != np.sign(vs[i + 1]):
            lo, hi = xs[i], xs[i + 1]
            for _ in range(80):
                mid = (lo + hi) / 2
                if np.sign(f(mid)) == np.sign(f(lo)): lo = mid
                else: hi = mid
            out.append((lo + hi) / 2)
    return out


hits, attempts = [], 0
for mech in SECOND:
    sols = solve(mech)
    if not sols:
        print(f"{mech}: keine Loesung mit Ueberlappung 1/2"); continue
    for psi in sols:
        g = states(mech, psi); ph = phase(g); attempts += 1
        G = np.array([[np.vdot(a, b) for b in g] for a in g])
        ok = abs(ph - TARGET) <= TOL
        if ok: hits.append(mech)
        print(f"{mech}: psi = {np.degrees(psi):8.4f} Grad, |Ueberlappung|^2 = {overlap2(g):.6f}, phi = {ph:.6f},"
              f" phi - Ziel = {ph - TARGET:+.6f}, det G = {np.linalg.det(G).real:.6f}" + ("  -> TREFFER" if ok else ""))
verdict = "bestaetigt" if len(set(hits)) == 1 else ("mehrdeutig" if hits else "widerlegt")
print(f"Versuche: {attempts}; Treffer: {sorted(set(hits))}; Urteil: {verdict}")
