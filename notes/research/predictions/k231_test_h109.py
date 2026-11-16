"""k231: Test H109 (Vorab-Notiz Vorab_Notiz_H109_Generationsabhaengige_Frames.md).

Generation k: g_k = |n_k>|n_k>, n_k auf dem Kegel psi um die Zyklusachse (1,1,1)/sqrt3, Azimut 2 pi k / 3.
Zyklische Zuordnungen Z1-Z3 Generation -> Frame aus {R = sigma_z, T = sigma_x, J_B = sigma_y}.
Lesungen: L1 F_k x F_k;  L2a P0 x 1 + P1 x F_k;  L2b P0 x F_k + P1 x 1  (P in der Basis der Zyklusachse, erstes Kopien-Bit).
psi aus |<g'_j|g'_k>|^2 = 1/2 (alle Loesungen); Vorhersage phi = |arg Bargmann|.
Kriterium: bestaetigt, wenn genau ein Mechanismus |phi - 0.666665| <= 0.0002 trifft; mehrdeutig bei mehreren; sonst widerlegt.
"""
import numpy as np

TARGET, TOL = 0.666665, 2e-4
sx = np.array([[0, 1], [1, 0]], complex); sy = np.array([[0, -1j], [1j, 0]]); sz = np.diag([1, -1]).astype(complex)
I2 = np.eye(2, dtype=complex)
FR = {"R": sz, "T": sx, "J_B": sy}
ZC = np.ones(3) / np.sqrt(3)
ASSIGN = {"Z1": ("R", "T", "J_B"), "Z2": ("J_B", "R", "T"), "Z3": ("T", "J_B", "R")}


def coh(n):
    n = np.asarray(n, float) / np.linalg.norm(n)
    th, ph = np.arccos(np.clip(n[2], -1, 1)), np.arctan2(n[1], n[0])
    return np.array([np.cos(th / 2), np.exp(1j * ph) * np.sin(th / 2)])


def cone(psi):
    e1 = np.cross(ZC, [1, 0, 0]); e1 /= np.linalg.norm(e1); e2 = np.cross(ZC, e1)
    return [np.cos(psi) * ZC + np.sin(psi) * (np.cos(2 * np.pi * k / 3) * e1 + np.sin(2 * np.pi * k / 3) * e2) for k in range(3)]


up, dn = coh(ZC), coh(-ZC)
P0, P1 = np.outer(up, up.conj()), np.outer(dn, dn.conj())
B2 = np.kron(np.column_stack([up, dn]), np.column_stack([up, dn]))
READ = {
    "L1": lambda F: np.kron(F, F),
    "L2a": lambda F: np.kron(P0, I2) + np.kron(P1, F),
    "L2b": lambda F: np.kron(P0, F) + np.kron(P1, I2),
}


def states(mech, psi):
    gens = [np.kron(coh(n), coh(n)) for n in cone(psi)]
    if mech is None:
        return gens
    z, l = mech
    return [READ[l](FR[ASSIGN[z][k]]) @ gens[k] for k in range(3)]


def overlap2(g):
    return abs(np.vdot(g[0], g[1])) ** 2


def all_overlaps(g):
    return [abs(np.vdot(g[i], g[j])) ** 2 for i, j in ((0, 1), (1, 2), (2, 0))]


def phase(g):
    return abs(np.angle(np.vdot(g[0], g[1]) * np.vdot(g[1], g[2]) * np.vdot(g[2], g[0])))


def boxes(g):
    return [np.round(np.abs(B2.conj().T @ x) ** 2, 6) for x in g]


def solve(mech):
    f = lambda p: overlap2(states(mech, p)) - 0.5
    xs = np.linspace(1e-3, np.pi - 1e-3, 20001); vs = np.array([f(x) for x in xs]); out = []
    for i in range(len(xs) - 1):
        if np.sign(vs[i]) != np.sign(vs[i + 1]):
            lo, hi = xs[i], xs[i + 1]
            for _ in range(80):
                mid = (lo + hi) / 2
                if np.sign(f(mid)) == np.sign(f(lo)): lo = mid
                else: hi = mid
            out.append((lo + hi) / 2)
    return out


ctrl = solve(None)
print("Kontrolle ohne Abbildung:", [f"psi = {np.degrees(p):.4f}, phi = {phase(states(None, p)):.6f}" for p in ctrl])
hits, attempts = [], 0
for z in ASSIGN:
    for l in READ:
        mech = (z, l); name = f"{z}/{l}"
        sols = solve(mech)
        if not sols:
            print(f"{name}: keine Loesung mit Ueberlappung 1/2"); continue
        for psi in sols:
            g = states(mech, psi); ph = phase(g); attempts += 1
            bx = boxes(g); equal = all(np.allclose(bx[0], b, atol=1e-5) for b in bx)
            ov = all_overlaps(g); sym = np.allclose(ov, ov[0], atol=1e-6)
            ok = abs(ph - TARGET) <= TOL
            if ok: hits.append(name)
            print(f"{name}: psi = {np.degrees(psi):8.4f} Grad, Ueberlappungen^2 = {np.round(ov, 6)}, phi = {ph:.6f},"
                  f" phi - Ziel = {ph - TARGET:+.6f}, Kaesten gleich: {equal}, Ueberlappungen gleich: {sym}"
                  + ("  -> TREFFER" if ok else ""))
verdict = "bestaetigt" if len(set(hits)) == 1 else ("mehrdeutig" if hits else "widerlegt")
print(f"Versuche: {attempts}; Treffer: {sorted(set(hits))}; Urteil: {verdict}")
