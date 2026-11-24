"""k252 / H125 Stufe A (nicht blind): Orientierung der Familien-su(2) je Sektor und Vorzeichen der Bargmann-Invariante.

A1  [R_e7, R_e8] = lambda_X R_e15 auf dem Leptonblock H_n und dem farbigen Block; Vorzeichen von lambda_X je Block.
A2  Ist die Familienstruktur des einen Blocks die komplex konjugierte des anderen (Bargmann-Invariante konjugiert)?
A3  Fuer alle Zuordnungen (e7,e8,e15) -> (+-i,+-j,+-k) der Linkswirkung von H mit vollem Rang auf dem Block:
    Bargmann-Invariante B = Tr(P7 P8 P15)/rang der Bildoperatoren; Vorzeichen von Im B je Sektor.
Aufruf aus dem Repo-Wurzelordner: python notes/research/h125_relatives_cp_2026_11_24/k252_h125_orientierung.py
"""
import importlib.util
import itertools
import os
import sys

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(os.path.dirname(HERE), "op3_cs_dixon_map_2026_11_15"))
import search as s  # noqa: E402

fs = s.fs
HN = [0, 7, 8, 15]
COL = [i for i in range(16) if i not in HN]


def bargmann(G):
    """G: drei reelle antisymmetrische Generatoren mit G^2 = -1. J = (i/2) G, P = Projektor auf +1/2."""
    Ps = []
    for g in G:
        J = 0.5j * g
        w, V = np.linalg.eigh(J)
        Vp = V[:, w > 0]
        Ps.append(Vp @ Vp.conj().T)
    r = int(round(np.trace(Ps[0]).real))
    return np.trace(Ps[0] @ Ps[1] @ Ps[2]) / r, r


def block(M, idx):
    return M[np.ix_(idx, idx)]


def main():
    Rf = [fs.R(fs.su(a)).astype(float) for a in (7, 8, 15)]
    print("A0  Bloecke invariant:", all(np.allclose(block(r, HN), r[np.ix_(HN, HN)]) and np.allclose(r[np.ix_(HN, COL)], 0)
                                       and np.allclose(r[np.ix_(COL, HN)], 0) for r in Rf))
    print("A0  R^2 = -1:", [bool(np.allclose(r @ r, -np.eye(16))) for r in Rf])
    out = {}
    for name, idx in (("Leptonen H_n", HN), ("farbig (Quarks)", COL)):
        G = [block(r, idx) for r in Rf]
        C = G[0] @ G[1] - G[1] @ G[0]
        lam = np.sum(C * G[2]) / np.sum(G[2] * G[2])
        res = np.linalg.norm(C - lam * G[2])
        B, r = bargmann(G)
        out[name] = B
        print(f"A1  {name}: [R7,R8] = {lam:+.6f} R15 (Rest {res:.1e});  A3  B = {B.real:+.6f}{B.imag:+.6f}i (Rang {r})")
    Bn, Bc = out["Leptonen H_n"], out["farbig (Quarks)"]
    print(f"A2  B_Leptonen = conj(B_Quarks): {bool(np.isclose(Bn, np.conj(Bc)))};  Im-Vorzeichen {np.sign(Bn.imag):+.0f} / {np.sign(Bc.imag):+.0f}")

    # Referenz: Linkswirkung von H, (i, j, k)
    E4 = np.eye(4)
    Lh = [np.array([s.hmul(E4[a], E4[j]) for j in range(4)]).T for a in range(4)]
    BL, _ = bargmann([Lh[1], Lh[2], Lh[3]])
    print(f"Ref Linkswirkung (i,j,k): [L_i,L_j] = 2 L_k; B = {BL.real:+.6f}{BL.imag:+.6f}i")

    # A3 ueber alle Zuordnungen mit vollem Rang je Block (wie search.py)
    K, I8 = np.kron, np.eye(8)
    E8 = np.eye(8)
    D8 = s.ho.derivations()
    c = fs.ch.null_space(np.array([d @ E8[7] for d in D8]).T)
    su3_8 = [sum(c[k, j] * D8[k] for k in range(14)).real for j in range(c.shape[1])]
    L8 = [np.array([s.ho.mul(E8[a], E8[j]) for j in range(8)]).T for a in range(8)]
    R8 = [np.array([s.ho.mul(E8[j], E8[a]) for j in range(8)]).T for a in range(8)]
    Q8 = 0.5 * np.eye(8) - (1j / 6) * L8[7] - (1j / 3) * R8[7]
    Rh = [np.array([s.hmul(E4[j], E4[a]) for j in range(4)]).T for a in range(4)]
    Qem = -(0.5j) * K(Rh[3], I8) + K(E4, Q8) - 0.5 * np.eye(32)
    P, SU3, P0, Pc, P3, P3b, Qs = fs.setup()
    base = [(K(np.eye(2), d).astype(complex), K(E4, d).astype(complex)) for d in su3_8] + [(Qs, Qem)]
    B0 = s.intertwiners(base)
    Fs = [r.astype(complex) for r in Rf]
    tally = {"Leptonen H_n": [], "farbig (Quarks)": []}
    for perm in itertools.permutations((1, 2, 3)):
        for signs in itertools.product((1, -1), repeat=3):
            T = [sg * Lh[p] for sg, p in zip(signs, perm)]
            targets = [K(t, I8).astype(complex) for t in T]
            B = s.restrict(B0, list(zip(Fs, targets)))
            Mx = np.zeros((3, 3))
            for rr, (p, sg) in enumerate(zip(perm, signs)):
                Mx[rr, p - 1] = sg
            det = int(round(np.linalg.det(Mx)))
            BT, _ = bargmann(T)
            if s.max_rank(B, HN) == 4:
                tally["Leptonen H_n"].append((det, BT))
            if s.max_rank(B, COL) == 12:
                tally["farbig (Quarks)"].append((det, BT))
    for name, lst in tally.items():
        dets = sorted(set(d for d, _ in lst))
        ims = sorted(set(int(np.sign(b.imag)) for _, b in lst))
        same = all(np.isclose(b, out[name]) for _, b in lst)
        print(f"A3  {name}: {len(lst)} Zuordnungen, det {dets}, Vorzeichen Im B der Zielgeneratoren {ims}, "
              f"alle gleich B des Blocks: {same}")


if __name__ == "__main__":
    main()
