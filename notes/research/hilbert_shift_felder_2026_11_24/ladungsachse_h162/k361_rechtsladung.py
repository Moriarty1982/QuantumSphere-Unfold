"""k361 (Erkundung, nicht blind, Nachtrag zu H162): Ladungen mit Rechts- statt Linksmultiplikation auf H_n.

Q^L_u = P0 (1/2 - (i/2) L_u) P0 + 2/3 P3 + 1/3 P3bar   (r13.1, H162)
Q^R_u = P0 (1/2 - (i/2) R_u) P0 + 2/3 P3 + 1/3 P3bar
1  Vollstaendigkeit: jede komplexe Struktur A auf H_n (A reell, A^2 = -1, A^T = -A) ist L_u oder R_u
2  Q^R_u: Spektrum, Farbe, Konjugation, psi, Fortsetzung von Q_8 auf der Kopie O_0
3  Familienalgebra: welche nativen Multiplikationen vertauschen mit Q^R_u; Orientierung und Bargmann-Invariante je Block
4  Zuordnungen zur Dixon-Seite (wie k252 A3) mit Q^R_u, Familie = L auf Leptonen, R auf Quarks
Aufruf aus dem Repo-Wurzelordner: python notes/research/hilbert_shift_felder_2026_11_24/ladungsachse_h162/k361_rechtsladung.py
"""
import itertools
import os
import sys

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import k360_test_h162 as k  # noqa: E402

s, fs = k.s, k.fs
su, L, R, nrm, I16 = k.su, k.L, k.R, k.nrm, k.I16
HN, COL, P, SU3, P0, Pc, P3, P3b = k.HN, k.COL, k.P, k.SU3, k.P0, k.Pc, k.P3, k.P3b
rng = np.random.default_rng(361)


def QR(u):
    return P0 @ (0.5 * I16 - 0.5j * R(u)) @ P0 + (2 / 3) * P3 + (1 / 3) * P3b


def part1():
    # reelle antisymmetrische 4x4 mit A^2 = -1: so(4) = su(2)_L + su(2)_R, A = a.L + b.R; A^2 = -1 <=> (|a|,|b|) = (1,0) oder (0,1)
    Lb = [k.blk(L(su(a)), HN) for a in (7, 8, 15)]
    Rb = [k.blk(R(su(a)), HN) for a in (7, 8, 15)]
    basis = np.array([m.ravel() for m in Lb + Rb])
    print(f"1  Rang von (L_e7, L_e8, L_e15, R_e7, R_e8, R_e15) auf H_n: {np.linalg.matrix_rank(basis)} (so(4) hat Dimension 6); "
          f"|[L_x, R_y]| max = {max(nrm(a @ b - b @ a) for a in Lb for b in Rb):.1e}")
    worst = 0.0
    for _ in range(2000):
        a, b = rng.normal(size=3), rng.normal(size=3)
        A = sum(x * m for x, m in zip(a, Lb)) + sum(x * m for x, m in zip(b, Rb))
        dev = nrm(A @ A + (a @ a + b @ b) * np.eye(4) - 2 * sum(x * m for x, m in zip(a, Lb)) @ sum(x * m for x, m in zip(b, Rb)))
        worst = max(worst, dev)
    print(f"   A = a.L + b.R: A^2 = -(|a|^2 + |b|^2) + 2 (a.L)(b.R), Rest {worst:.1e}; (a.L)(b.R) ist spurfrei und ungleich null fuer a, b != 0,")
    print("   also A^2 = -1 genau fuer (|a|, |b|) = (1, 0) oder (0, 1): L_u oder R_u.")


def part23(name, u):
    Q = QR(u)
    sp, tot = k.spectrum(Q)
    QS = 0.5 * I16 - (1j / 6) * L(su(7)) - (1j / 3) * R(su(7))
    print(f"2  {name}: Spektrum {sp}; |[Q,su3]| {max(nrm(Q @ D - D @ Q) for D in SU3):.1e}; |Qquer-(1-Q)| {nrm(Q.conj() - (I16 - Q)):.1e}; "
          f"|[Q,psi]| {nrm(Q @ P - P @ Q):.3f}; O_0: Leck {nrm(Q[8:, :8]):.3f}, |Q - Q_8| {nrm((Q - QS)[:8, :8]):.3f}")
    Lf = [L(su(a)).astype(float) for a in (7, 8, 15)]
    Rf = k.Rf
    cL = max(nrm(P0 @ (m @ Q - Q @ m) @ P0) for m in Lf)
    cR = max(nrm(P0 @ (m @ Q - Q @ m) @ P0) for m in Rf)
    cRc = max(nrm(Pc @ (m @ Q - Q @ m) @ Pc) for m in Rf)
    cLc = max(nrm(Pc @ (m @ Q - Q @ m) @ Pc) for m in Lf)
    mixL = max(nrm(Pc @ m @ P0) + nrm(P0 @ m @ Pc) for m in Lf)
    print(f"3  {name}: Kommutator mit Q auf H_n: L_x {cL:.1e}, R_x {cR:.2f}; farbig: R_x {cRc:.1e}, L_x {cLc:.2f}; L_x mischt neutral/farbig: {mixL:.1e}")
    GL = [k.blk(m, HN) for m in Lf]
    C = GL[0] @ GL[1] - GL[1] @ GL[0]
    lamL = np.sum(C * GL[2]) / np.sum(GL[2] * GL[2])
    GR = [k.blk(m, COL) for m in Rf]
    C = GR[0] @ GR[1] - GR[1] @ GR[0]
    lamR = np.sum(C * GR[2]) / np.sum(GR[2] * GR[2])
    print(f"   Familie Leptonen = L_x auf H_n: [L7,L8] = {lamL:+.4f} L15, Bargmann {k.bargmann(GL):.4f};  "
          f"Familie Quarks = R_x: [R7,R8] = {lamR:+.4f} R15, Bargmann {k.bargmann(GR):.4f}")


def part4(name, u):
    K, I8, E8, E4 = np.kron, np.eye(8), np.eye(8), np.eye(4)
    D8 = s.ho.derivations()
    c = fs.ch.null_space(np.array([d @ E8[7] for d in D8]).T)
    su3_8 = [sum(c[kk, j] * D8[kk] for kk in range(14)).real for j in range(c.shape[1])]
    L8 = [np.array([s.ho.mul(E8[a], E8[j]) for j in range(8)]).T for a in range(8)]
    R8 = [np.array([s.ho.mul(E8[j], E8[a]) for j in range(8)]).T for a in range(8)]
    Q8 = 0.5 * np.eye(8) - (1j / 6) * L8[7] - (1j / 3) * R8[7]
    Lh = [np.array([s.hmul(E4[a], E4[j]) for j in range(4)]).T for a in range(4)]
    Rh = [np.array([s.hmul(E4[j], E4[a]) for j in range(4)]).T for a in range(4)]
    Qem = -(0.5j) * K(Rh[3], I8) + K(E4, Q8) - 0.5 * np.eye(32)
    base = [(K(np.eye(2), d).astype(complex), K(E4, d).astype(complex)) for d in su3_8] + [(QR(u), Qem)]
    B0 = s.intertwiners(base)
    # Familienoperatoren: L_x auf dem Leptonblock, R_x auf dem farbigen Block
    Fs = [(P0 @ L(su(a)) @ P0 + Pc @ R(su(a)) @ Pc).astype(complex) for a in (7, 8, 15)]
    tally = {"Leptonen": [], "Quarks": []}
    for perm in itertools.permutations((1, 2, 3)):
        for signs in itertools.product((1, -1), repeat=3):
            T = [sg * Lh[p] for sg, p in zip(signs, perm)]
            B = s.restrict(B0, list(zip(Fs, [K(t, I8).astype(complex) for t in T])))
            Mx = np.zeros((3, 3))
            for rr, (p, sg) in enumerate(zip(perm, signs)):
                Mx[rr, p - 1] = sg
            det = int(round(np.linalg.det(Mx)))
            if s.max_rank(B, HN) == 4:
                tally["Leptonen"].append(det)
            if s.max_rank(B, COL) == 12:
                tally["Quarks"].append(det)
    print(f"4  {name}: Verflechter Dimension {len(B0)}; Zuordnungen vollen Rangs: Leptonen {len(tally['Leptonen'])} mit det "
          f"{sorted(set(tally['Leptonen']))}, Quarks {len(tally['Quarks'])} mit det {sorted(set(tally['Quarks']))}")


if __name__ == "__main__":
    part1()
    cases = [("Q^R, u = e7", k.axis(1, 0, 0)), ("Q^R, u = e8", k.axis(0, 1, 0)), ("Q^R, u zufaellig", k.axis(*rng.normal(size=3)))]
    for n, u in cases:
        part23(n, u)
    for n, u in cases[:2]:
        part4(n, u)
