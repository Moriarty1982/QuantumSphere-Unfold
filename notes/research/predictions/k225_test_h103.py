"""H103: Bezug unter dem magischen Winkel im neutralen Qubit N = ker Q_* (Vorab-Notiz Vorab_Notiz_H103_Bezug_im_neutralen_Qubit.md).

Aufruf: python k225_test_h103.py  (Ausgabe nach k225_out.txt umleiten)
"""
import importlib.util
import os
import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
RES = os.path.join(HERE, "..")


def load(name):
    spec = importlib.util.spec_from_file_location(name, os.path.join(RES, name + ".py"))
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


sr = load("op3_sedenion_reference_2026_11_13")
smul, su, psi_matrix = sr.smul, sr.su, sr.psi_matrix
MAGIC = 1 / np.sqrt(3)
TOL = 1e-10

P = psi_matrix(2 * np.pi / 3).astype(complex)
e7, e8, e15 = su(7), su(8), su(15)
L = lambda x: np.array([smul(x, su(b)) for b in range(16)]).T
R = lambda x: np.array([smul(su(b), x) for b in range(16)]).T
QS = 0.5 * np.eye(16) - (1j / 6) * L(e7) - (1j / 3) * R(e7)
H = [0, 7, 8, 15]
P0 = np.zeros((16, 16)); P0[H, H] = 1
Qstar_blk = P0 @ (0.5 * np.eye(16) - 0.5j * L(e8)) @ P0      # farbneutraler Teil von Q_* (farbiger Teil wirkt nicht auf N)
v1 = np.zeros(16, complex); v1[0], v1[8] = 1, 1j
vw = np.zeros(16, complex); vw[7], vw[15] = 1, -1j
v1 /= np.linalg.norm(v1); vw /= np.linalg.norm(vw)
B = np.array([v1, vw]).T                                       # Basis von N


def ctrl_basis():
    return (np.allclose(Qstar_blk @ v1, 0), np.allclose(Qstar_blk @ vw, 0),
            np.allclose(P @ v1, v1), np.allclose(P @ vw, np.exp(2j * np.pi / 3) * vw) or np.allclose(P @ vw, np.exp(-2j * np.pi / 3) * vw))


def c_op(X):
    Xh = (X + X.conj().T) / 2
    M = B.conj().T @ Xh @ B
    nz = (M[0, 0] - M[1, 1]).real
    n = np.array([2 * M[0, 1].real, 2 * M[0, 1].imag, nz])          # Bloch-Vektor (Vorzeichen von n_y egal)
    norm = np.linalg.norm(n)
    if norm < 1e-12:
        return None
    return abs(nz) / norm


def c_el(x):
    w1, ww = abs(np.vdot(v1, x)) ** 2, abs(np.vdot(vw, x)) ** 2
    if w1 + ww < 1e-12:
        return None
    return abs(w1 - ww) / (w1 + ww)


def fmt(c):
    return "skalar/0" if c is None else f"{c:.10f}"


def hit(c):
    return c is not None and abs(c - MAGIC) <= TOL


if __name__ == "__main__":
    print(f"Basis: Q_* v1 = 0, Q_* v_w = 0, psi v1 = v1, psi v_w = omega v_w: {ctrl_basis()}")
    # Kontrollen
    th = np.arccos(MAGIC)
    r = np.cos(th / 2) * v1 + np.sin(th / 2) * vw
    orb = [r, P @ r, P @ P @ r]
    S = np.array([[np.vdot(x, y) for y in orb] for x in orb])
    rho2 = (abs(S[0, 1]) ** 2 + abs(S[1, 2]) ** 2 + abs(S[2, 0]) ** 2) / 3
    ph = abs(np.angle(S[0, 1] * S[1, 2] * S[2, 0]))
    print(f"Kontrolle: c(psi) = {fmt(c_op(1j * (P - P.conj().T)))} (soll 1); Q_* auf N {fmt(c_op(Qstar_blk))} (soll skalar); "
          f"Magie-Mischung rho^2-1/2 = {rho2 - 0.5:.1e}, Phase-pi/4 = {ph - np.pi / 4:.1e}")
    # Kandidat A
    cA = c_op(QS)
    M = B.conj().T @ QS @ B
    print(f"\nH103a  Q_S auf N: Kompression {np.round(M, 6).tolist()}; c = {fmt(cA)}; Ziel 1/sqrt3 = {MAGIC:.10f}; "
          f"Treffer: {hit(cA)}")
    if cA is not None:
        print(f"       Winkel zur psi-Achse {np.degrees(np.arccos(cA)):.4f} Grad (magisch 54.7356)")
    # Liste B
    a = -0.5 * su(0) + (np.sqrt(3) / 2) * e7
    ai = a.copy(); ai[1:] *= -1
    Ca = np.array([smul(smul(a, su(b)), ai) for b in range(16)]).T
    xs = [a, P.real @ a, P.real @ P.real @ a]
    f = (e7 + e8 + e15) / np.sqrt(3)
    Im = lambda x: np.concatenate([[0], x[1:]])
    ops = {}
    for u in range(1, 16):
        ops[f"iL_e{u}"] = 1j * L(su(u)); ops[f"iR_e{u}"] = 1j * R(su(u))
    ops["L_e7 R_e7"] = L(e7) @ R(e7)
    w, V = np.linalg.eigh(QS)
    for q in (0, 1 / 3, 2 / 3, 1):
        cols = V[:, np.abs(w - q) < 1e-9]
        ops[f"Proj Q_S={q:.3f}"] = cols @ cols.conj().T
    ops["eps"] = np.diag([1.0] * 8 + [-1.0] * 8).astype(complex)
    ops["(C_a+C_a^T)/2"] = (Ca + Ca.T) / 2
    ops["i(C_a-C_a^T)/2"] = 1j * (Ca - Ca.T) / 2
    for k, x in enumerate(xs):
        ops[f"iL_Im(psi^{k}a)"] = 1j * L(Im(x)); ops[f"iR_Im(psi^{k}a)"] = 1j * R(Im(x))
    ops["iL_f"] = 1j * L(f); ops["iR_f"] = 1j * R(f)
    ops["Q_S+Q_*"] = QS + Qstar_blk
    hitsB = []
    print(f"\nH103b  Liste B, {len(ops)} Operatoren:")
    vals = {}
    for name, X in ops.items():
        c = c_op(X)
        vals.setdefault(fmt(c), []).append(name)
        if hit(c):
            hitsB.append(name)
    for c, names in sorted(vals.items()):
        print(f"    c = {c}: {', '.join(names)}")
    base = {"1": su(0), "e7": e7, "e8": e8, "e15": e15, "a": xs[0], "psi a": xs[1], "psi^2 a": xs[2]}
    evals = {}
    for n1, x in base.items():
        for n2, y in base.items():
            c = c_el(smul(x, y).astype(complex))
            evals.setdefault(fmt(c), []).append(f"{n1}*{n2}")
            if hit(c):
                hitsB.append(f"{n1}*{n2}")
    print(f"       Liste B3, {len(base) ** 2} Produkte:")
    for c, names in sorted(evals.items()):
        print(f"    c = {c}: {len(names)} Produkte, z. B. {', '.join(names[:4])}")
    print(f"\nTreffer in Liste B: {len(hitsB)} {hitsB}")
    print(f"ERGEBNIS H103a: {'bestaetigt' if hit(cA) else 'widerlegt'}")
