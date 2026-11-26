"""k360 / Test H162: Bestehen Weg A und das relative CP-Vorzeichen (H125 Stufe A) auf der Ladungsrichtung e7?

Q_u = P0 (1/2 - (i/2) L_u) P0 + 2/3 P3 + 1/3 P3bar,  u Einheit in span(e7, e8, e15);  Q_* = Q_e8 (r13.1).
a  Spektrum, [Q_u, su(3)_c], Q quer = 1 - Q
b  [R_x, Q_u] fuer x = e7, e8, e15; Orientierung und Bargmann-Invariante je Block; 200 Zufallsachsen
c  Zuordnungen zur Dixon-Seite wie k252 A3, mit Q_u statt Q_*
d  Einschraenkung auf die Oktonion-Kopien O_0, O_120, O_240: invariant? gleich Q_8?
e  (Erkundung) [Q_u, psi], psi auf dem neutralen Kern, Bahn-Ueberlapp wie r13.2
Aufruf aus dem Repo-Wurzelordner: python notes/research/hilbert_shift_felder_2026_11_24/ladungsachse_h162/k360_test_h162.py
"""
import itertools
import os
import sys

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
RES = os.path.dirname(os.path.dirname(HERE))
sys.path.insert(0, os.path.join(RES, "op3_cs_dixon_map_2026_11_15"))
import search as s  # noqa: E402

fs = s.fs
su, L, R, nrm = fs.su, fs.L, fs.R, fs.nrm
I16 = np.eye(16)
HN = [0, 7, 8, 15]
COL = [i for i in range(16) if i not in HN]
rng = np.random.default_rng(162)
P, SU3, P0, Pc, P3, P3b, Qstar = fs.setup()


def axis(c7, c8, c15):
    x = np.zeros(16); x[7], x[8], x[15] = c7, c8, c15
    return x / np.linalg.norm(x)


def Q(u):
    return P0 @ (0.5 * I16 - 0.5j * L(u)) @ P0 + (2 / 3) * P3 + (1 / 3) * P3b


def spectrum(M):
    w = np.linalg.eigvals(M)
    out = {}
    for v in (0, 1 / 3, 2 / 3, 1):
        out[round(v, 4)] = int(np.sum(np.abs(w - v) < 1e-9))
    return out, int(sum(out.values()))


def bargmann(G):
    Ps = []
    for g in G:
        w, V = np.linalg.eigh(0.5j * g)
        Vp = V[:, w > 0]
        Ps.append(Vp @ Vp.conj().T)
    r = int(round(np.trace(Ps[0]).real))
    return np.trace(Ps[0] @ Ps[1] @ Ps[2]) / r


def blk(M, idx):
    return M[np.ix_(idx, idx)]


Rf = [R(su(a)).astype(float) for a in (7, 8, 15)]


def part_ab(name, u, verbose=True):
    Qu = Q(u)
    sp, tot = spectrum(Qu)
    r_su3 = max(nrm(Qu @ D - D @ Qu) for D in SU3)
    r_conj = nrm(Qu.conj() - (I16 - Qu))
    r_R = max(nrm(r @ Qu - Qu @ r) for r in Rf)
    r_L = max(nrm(L(su(a)) @ Qu - Qu @ L(su(a))) for a in (7, 8, 15))
    res = {}
    for bname, idx in (("Leptonen", HN), ("Quarks", COL)):
        G = [blk(r, idx) for r in Rf]
        C = G[0] @ G[1] - G[1] @ G[0]
        lam = np.sum(C * G[2]) / np.sum(G[2] * G[2])
        res[bname] = (lam, bargmann(G))
    # Familien-Dublett je Teilchenart: Casimir der R auf dem Ladungseigenraum
    cas = []
    for q, Pp in ((0.0, P0), (1.0, P0), (2 / 3, P3), (1 / 3, P3b)):
        Ps = fs.spec_proj(Qu, (0.0, 1 / 3, 2 / 3, 1.0), q) @ Pp
        ev = fs.eig_on(-(Rf[0] @ Rf[0] + Rf[1] @ Rf[1] + Rf[2] @ Rf[2]) / 4, Ps)
        cas.append((int(round(np.trace(Ps).real)), float(np.max(np.abs(ev - 0.75)))))
    if verbose:
        print(f"  {name}: Spektrum {sp} (Summe {tot}); |[Q,su3]| {r_su3:.1e}; |Qquer-(1-Q)| {r_conj:.1e}; "
              f"|[R_x,Q]| {r_R:.1e}; |[L_x,Q]| {r_L:.2f}")
        print(f"      [R7,R8]/R15: Leptonen {res['Leptonen'][0]:+.6f}, Quarks {res['Quarks'][0]:+.6f}; "
              f"Bargmann Leptonen {res['Leptonen'][1]:.6f}, Quarks {res['Quarks'][1]:.6f}")
        print(f"      Teilchenarten (nu, e+, u, dbar): Dimension und |Casimir - 3/4|: {cas}")
    ok_a = sp == {0: 2, 0.3333: 6, 0.6667: 6, 1: 2} and r_su3 < 1e-10 and r_conj < 1e-10
    ok_b = (r_R < 1e-10 and abs(res["Leptonen"][1] - (0.25 - 0.25j)) < 1e-10
            and abs(res["Quarks"][1] - (0.25 + 0.25j)) < 1e-10)
    return ok_a, ok_b


def part_c(name, u):
    K, I8, E8, E4 = np.kron, np.eye(8), np.eye(8), np.eye(4)
    D8 = s.ho.derivations()
    c = fs.ch.null_space(np.array([d @ E8[7] for d in D8]).T)
    su3_8 = [sum(c[k, j] * D8[k] for k in range(14)).real for j in range(c.shape[1])]
    L8 = [np.array([s.ho.mul(E8[a], E8[j]) for j in range(8)]).T for a in range(8)]
    R8 = [np.array([s.ho.mul(E8[j], E8[a]) for j in range(8)]).T for a in range(8)]
    Q8 = 0.5 * np.eye(8) - (1j / 6) * L8[7] - (1j / 3) * R8[7]
    Lh = [np.array([s.hmul(E4[a], E4[j]) for j in range(4)]).T for a in range(4)]
    Rh = [np.array([s.hmul(E4[j], E4[a]) for j in range(4)]).T for a in range(4)]
    Qem = -(0.5j) * K(Rh[3], I8) + K(E4, Q8) - 0.5 * np.eye(32)
    base = [(K(np.eye(2), d).astype(complex), K(E4, d).astype(complex)) for d in su3_8] + [(Q(u), Qem)]
    B0 = s.intertwiners(base)
    Fs = [r.astype(complex) for r in Rf]
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
    print(f"  {name}: Verflechter (Farbe, Ladung) Dimension {len(B0)}; Zuordnungen vollen Rangs: "
          f"Leptonen {len(tally['Leptonen'])} mit det {sorted(set(tally['Leptonen']))}, "
          f"Quarks {len(tally['Quarks'])} mit det {sorted(set(tally['Quarks']))}")
    return (len(tally["Leptonen"]) == 24 and set(tally["Leptonen"]) == {-1}
            and len(tally["Quarks"]) == 24 and set(tally["Quarks"]) == {1})


def part_d(name, u):
    QS = 0.5 * I16 - (1j / 6) * L(su(7)) - (1j / 3) * R(su(7))       # geerbte Ladung, Achse e7
    Pr = P.real
    out = []
    for k, cname in ((0, "O_0"), (1, "O_120"), (2, "O_240")):
        M = np.linalg.matrix_power(Pr, k)
        Bk = M[:, :8]                                             # Basis der Kopie psi^k O_0
        Pk = Bk @ Bk.T
        leak = nrm((I16 - Pk) @ Q(u) @ Pk)
        Qk = M @ QS @ M.T                                         # Q_8 der Kopie (Achse psi^k e7)
        diff = nrm(Pk @ (Q(u) - Qk) @ Pk)
        out.append((cname, leak, diff))
    print(f"  {name}: " + "; ".join(f"{c}: Leck {l:.3e}, |Q_u - Q_8(Kopie)| {d:.3e}" for c, l, d in out))
    return out


def part_e(name, u):
    Qu = Q(u)
    w, V = np.linalg.eig(Qu)
    N = V[:, np.abs(w) < 1e-9]
    N, _ = np.linalg.qr(N)
    PN = N @ N.conj().T
    print(f"  {name}: |[Q_u, psi]| = {nrm(Qu @ P - P @ Qu):.4f}; dim ker Q_u = {N.shape[1]}; "
          f"|(1 - P_N) psi P_N| = {nrm((I16 - PN) @ P @ PN):.4f}")
    # Ordnung-3-Abbildungen, die mit Q_u und Farbe vertauschen: Rechtswirkung der Hurwitz-Einheiten (T_g wie in fs)
    units = [np.array(sg) / 2 for sg in itertools.product((1, -1), repeat=4)]
    Tg = [R(fs.quat(cv)) @ P0 + R(fs.qbar(cv)) @ Pc for cv in units]
    comm = max(nrm(t @ Qu - Qu @ t) for t in Tg)
    # Drehung der Familien-su(2) um die Achse u um 120 Grad (Ersatz fuer psi): exp(-(pi/3) R_u) auf N
    c3 = np.cos(np.pi / 3) * I16 - np.sin(np.pi / 3) * R(u)
    c3n = N.conj().T @ c3 @ N
    vals = []
    for cv in units:
        if not np.isclose(cv[0], 0.5):
            continue
        hn = N.conj().T @ R(fs.quat(cv)) @ N
        ww, VV = np.linalg.eig(hn)
        ref = VV[:, 0]
        orb = [ref, c3n @ ref, c3n @ c3n @ ref]
        S = np.array([[np.vdot(x, y) for y in orb] for x in orb])
        rho2 = (abs(S[0, 1]) ** 2 + abs(S[1, 2]) ** 2 + abs(S[2, 0]) ** 2) / 3
        vals.append((round(float(rho2), 6), round(float(abs(np.angle(S[0, 1] * S[1, 2] * S[2, 0]))), 6)))
    print(f"      Hurwitz-Einheiten T_g vertauschen mit Q_u: {comm:.1e}; Ersatzzyklus exp(-(pi/3)R_u) auf N: "
          f"Ordnung 3 projektiv {np.allclose(np.linalg.matrix_power(c3n, 3), -np.eye(2))}; "
          f"(rho^2, Bargmann-Phase) der Bahnen: {sorted(set(vals))} (pi/4 = {np.pi / 4:.6f})")


if __name__ == "__main__":
    s3 = np.sqrt(3) / 2
    cases = [("u = e7", axis(1, 0, 0)), ("u = -e7/2 + s3 e15", axis(-0.5, 0, s3)), ("u = -e7/2 - s3 e15", axis(-0.5, 0, -s3)),
             ("u = e8 (Q_*, Kontrolle)", axis(0, 1, 0))]
    print(f"Kontrolle: |Q_e8 - Q_*| = {nrm(Q(axis(0, 1, 0)) - Qstar):.1e}; e7 e8 = +e15: "
          f"{np.allclose(fs.smul(su(7), su(8)), su(15))}; Raenge P0, P3, P3bar = {int(np.trace(P0))}, "
          f"{int(round(np.trace(P3).real))}, {int(round(np.trace(P3b).real))}")
    print("\nH162a, H162b")
    ab = {n: part_ab(n, u) for n, u in cases}
    rnd = [part_ab("", axis(*rng.normal(size=3)), verbose=False) for _ in range(200)]
    print(f"  200 Zufallsachsen: a erfuellt {sum(a for a, _ in rnd)}/200, b erfuellt {sum(b for _, b in rnd)}/200")
    print("\nH162c (Zuordnungen zur Dixon-Seite, wie k252 A3)")
    cres = {n: part_c(n, u) for n, u in cases}
    print("\nH162d (Einschraenkung auf die Oktonion-Kopien)")
    dres = {n: part_d(n, u) for n, u in cases}
    print("\nH162e (Erkundung)")
    for n, u in cases:
        part_e(n, u)
    print("\nEntscheidungen")
    n7 = "u = e7"
    d7 = dres[n7]; d8 = dres["u = e8 (Q_*, Kontrolle)"]
    okd = d7[0][1] < 1e-10 and d7[0][2] < 1e-10 and d7[1][1] > 1e-3 and d7[2][1] > 1e-3 and (d8[0][1] > 1e-3 or d8[0][2] > 1e-3)
    print(f"  H162a: {'bestaetigt' if ab[n7][0] else 'widerlegt'}")
    print(f"  H162b: {'bestaetigt' if ab[n7][1] and all(b for _, b in rnd) else 'widerlegt'}")
    print(f"  H162c: {'bestaetigt' if cres[n7] else 'widerlegt'}")
    print(f"  H162d: {'bestaetigt' if okd else 'widerlegt'}")
