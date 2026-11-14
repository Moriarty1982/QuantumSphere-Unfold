"""Erkundung (14.11.2026): Ist die Rechtswirkung von H_n = span(1, e7, e8, e15) auf ganz C(x)S eine Familiensymmetrie?

Rueckwaertssuche zu Punkt (c) der Uebergabe ("zweite Familienstruktur mit neutralem Qubit"). Notwendig nach Schur:
eine neutrale SU(2) wirkt nur auf den Generationsindex. Kandidat: R_u, u in Im H_n (auf N schon ein Pauli-Tripel).
Offen vor der Rechnung: ob R_u auf dem farbigen Teil (S ist nicht assoziativ) eine Darstellung bleibt.

Abschnitte: 1 Quaternionen-Relationen der R_e7, R_e8, R_e15 (neutral und farbig); 2 Vertauschung mit su(3)_c, Q_*, psi;
3 die 24 Hurwitz-Einheiten auf ganz S; 4 Spektren je Teilchenart; 5 psi als Drehung der Familien-su(2);
6 Oktant mit den urspruenglichen Rollen; 7 Majorana-Bilinear des Familien-Dubletts.
Aufruf: python op3_family_su2_right_action_2026_11_14.py
"""
import importlib.util
import itertools
import os
import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))


def load(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


ho = load("ho", os.path.join(HERE, "op3_hopf_octant_2026_11_13.py"))
sr = load("sr", os.path.join(HERE, "op3_sedenion_reference_2026_11_13.py"))
ch = load("ch", os.path.join(HERE, "op3_sedenion_charge_2026_11_13.py"))
smul, su, psi_matrix = sr.smul, sr.su, sr.psi_matrix
I16 = np.eye(16)
HN = [0, 7, 8, 15]


def L(x):
    return np.array([smul(x, su(b)) for b in range(16)]).T


def R(x):
    return np.array([smul(su(b), x) for b in range(16)]).T


def nrm(M):
    return float(np.linalg.norm(M))


def quat(cv):
    x = np.zeros(16); x[HN] = cv; return x


def qbar(cv):
    return quat(np.asarray(cv) * np.array([1, -1, -1, -1]))


def setup():
    e7, e8 = su(7), su(8)
    P = psi_matrix(2 * np.pi / 3).astype(complex)
    DS = [np.kron(np.eye(2), d) for d in ho.derivations()]
    c = ch.null_space(np.array([D @ e7 for D in DS]).T)
    SU3 = [sum(c[k, j] * DS[k] for k in range(14)).real for j in range(c.shape[1])]
    P0 = np.zeros((16, 16)); P0[HN, HN] = 1
    Pc = I16 - P0
    QS = 0.5 * I16 - (1j / 6) * L(e7) - (1j / 3) * R(e7)
    w, V = np.linalg.eig(QS[1:7, 1:7])
    V3 = []
    for k in range(6):
        if abs(w[k] - 2 / 3) < 1e-9:
            v = np.zeros(16, complex); v[1:7] = V[:, k]; V3.append(v)
    V3 = V3 + [P @ v for v in V3] + [P @ P @ v for v in V3]
    P3 = ch.proj(V3)
    P3b = Pc - P3
    Qs = P0 @ (0.5 * I16 - 0.5j * L(e8)) @ P0 + (2 / 3) * P3 + (1 / 3) * P3b
    return P, SU3, P0, Pc, P3, P3b, Qs


def spec_proj(Q, vals, v):
    Pq = np.eye(16, dtype=complex)
    for q2 in vals:
        if abs(q2 - v) > 1e-9:
            Pq = Pq @ (Q - q2 * I16) / (v - q2)
    return Pq


def eig_on(M, Pp):
    U, s, _ = np.linalg.svd(Pp)
    Bq = U[:, s > 0.5]
    return np.linalg.eigvals(Bq.conj().T @ M @ Bq)


def fmt_eigs(ev):
    r = sorted({(round(z.real, 4) + 0.0, round(z.imag, 4) + 0.0) for z in ev})
    return ", ".join(f"{a:+.4f}{b:+.4f}i" for a, b in r)


def group_orders(G):
    orders = {}
    for u in G:
        for n in range(1, 13):
            if np.allclose(np.linalg.matrix_power(u, n), I16):
                orders[n] = orders.get(n, 0) + 1; break
    return dict(sorted(orders.items()))


def closed(G):
    return all(any(np.allclose(a @ b, c) for c in G) for a in G for b in G)


if __name__ == "__main__":
    P, SU3, P0, Pc, P3, P3b, Qs = setup()
    e7, e8, e15 = su(7), su(8), su(15)
    R7, R8, R15 = R(e7), R(e8), R(e15)
    Rs = {"e7": R7, "e8": R8, "e15": R15}
    blocks = (("neutral", P0), ("farbig", Pc))
    print(f"Kontrolle: e7 e8 = {'+' if np.allclose(smul(e7, e8), e15) else '-'}e15; Spur Q_* = {np.trace(Qs).real:.4f} "
          f"(soll 8); |[Q_*, psi]| = {nrm(Qs @ P - P @ Qs):.1e}; Raenge P0, P3, P3bar = "
          f"{int(round(np.trace(P0)))}, {int(round(np.trace(P3).real))}, {int(round(np.trace(P3b).real))}")

    print("\n(1) Quaternionen-Relationen der Rechtsmultiplikationen (Norm der Abweichung)")
    for name, blk in blocks:
        sq = max(nrm((Ra @ Ra + I16) @ blk) for Ra in Rs.values())
        ac = max(nrm((Ra @ Rb + Rb @ Ra) @ blk) for Ra, Rb in itertools.combinations(Rs.values(), 2))
        orth = max(nrm((Ra.T @ Ra - I16) @ blk) for Ra in Rs.values())
        inv = max(nrm(Pc @ Ra @ P0) + nrm(P0 @ Ra @ Pc) for Ra in Rs.values())
        sgn = "+" if nrm((R7 @ R8 - R15) @ blk) < 1e-12 else ("-" if nrm((R7 @ R8 + R15) @ blk) < 1e-12 else "?")
        print(f"    {name:8s}: R^2 + 1: {sq:.1e}; Antikommutatoren: {ac:.1e}; orthogonal: {orth:.1e}; "
              f"mischt neutral/farbig: {inv:.1e}; R_e7 R_e8 = {sgn}R_e15")
    print("    (e7 e8 = +e15; ein Rechtsmodul verlangt R_e7 R_e8 = R_(e8 e7) = -R_e15)")

    print("\n(2) Vertauschung (Norm des Kommutators)")
    for name, Ra in Rs.items():
        c_su3 = max(nrm(Ra @ D - D @ Ra) for D in SU3)
        print(f"    R_{name:3s}: mit su(3)_c {c_su3:.1e}; mit Q_* {nrm(Ra @ Qs - Qs @ Ra):.1e}; "
              f"mit P3 {nrm(Ra @ P3 - P3 @ Ra):.1e}; mit psi {nrm(Ra @ P - P @ Ra):.2f}")
    print("    zum Vergleich Linksmultiplikation: " + "; ".join(
        f"L_{n}: su(3)_c {max(nrm(L(x) @ D - D @ L(x)) for D in SU3):.1e}, Q_* {nrm(L(x) @ Qs - Qs @ L(x)):.2f}"
        for n, x in (("e7", e7), ("e8", e8), ("e15", e15))))

    print("\n(3) 24 Hurwitz-Einheiten von rechts auf ganz S")
    units = []
    for i in range(4):
        for s in (1, -1):
            cvec = np.zeros(4); cvec[i] = s; units.append(cvec)
    for s in itertools.product((1, -1), repeat=4):
        units.append(np.array(s) / 2)
    U = [R(quat(cv)) for cv in units]
    print(f"    R_g orthogonal {all(np.allclose(u.T @ u, I16) for u in U)}; als Menge abgeschlossen {closed(U)}")
    for bname, blk in blocks:
        for oname, order in (("R_(y x)", lambda x, y: smul(y, x)), ("R_(x y)", lambda x, y: smul(x, y))):
            v = max(nrm((R(quat(x)) @ R(quat(y)) - R(order(quat(x), quat(y)))) @ blk) for x in units for y in units)
            print(f"    {bname:8s}: max |R_x R_y - {oname}| = {v:.1e}")
    T = [R(quat(cv)) @ P0 + R(qbar(cv)) @ Pc for cv in units]            # neutral: R_g, farbig: R_(g quer)
    print(f"    T_g = R_g (neutral) + R_(g quer) (farbig): abgeschlossen {closed(T)}; treu "
          f"{len({tuple(np.round(u.ravel(), 6)) for u in T}) == 24}; Ordnungen {group_orders(T)} "
          f"(2T: 1:1, 2:1, 3:8, 4:6, 6:8)")
    c_all = max(max(nrm(u @ D - D @ u) for D in SU3) + nrm(u @ Qs - Qs @ u) for u in T)
    print(f"    T_g vertauscht mit su(3)_c und Q_*: {c_all:.1e}")
    gens = [R7, R8, R15, R7 @ R8 - R8 @ R7, R8 @ R15 - R15 @ R8, R15 @ R7 - R7 @ R15]
    print(f"    Lie-Algebra aus R_e7, R_e8, R_e15 und ihren Kommutatoren: Dimension "
          f"{np.linalg.matrix_rank(np.array([m.ravel() for m in gens]))} "
          f"(3: eine su(2); 6: su(2) neutral + su(2) farbig)")

    print("\n(4) Wirkung je Teilchenart (Eigenwerte auf dem Teilraum; Dimension = Farbe x Familie)")
    vals = (0.0, 1 / 3, 2 / 3, 1.0)
    for name, q, Pp in (("nu", 0.0, P0), ("e+", 1.0, P0), ("u", 2 / 3, P3), ("dbar", 1 / 3, P3b)):
        Ps = spec_proj(Qs, vals, q) @ Pp
        dim = int(round(np.trace(Ps).real))
        cas = eig_on(-(R7 @ R7 + R8 @ R8 + R15 @ R15) / 4, Ps)
        print(f"    {name:5s} dim {dim}: i R_e8 {{{fmt_eigs(eig_on(1j * R8, Ps))}}}; i R_e7 {{{fmt_eigs(eig_on(1j * R7, Ps))}}}; "
              f"Casimir j(j+1) {{{fmt_eigs(cas)}}}; psi {{{fmt_eigs(eig_on(P, Ps))}}}")

    print("\n(5) psi auf der Familien-su(2): psi R_u psi^-1 = R_(psi u)")
    Pr, Pi = P.real, np.linalg.inv(P)
    for name, x in (("e7", e7), ("e8", e8), ("e15", e15)):
        img = Pr @ x
        print(f"    psi {name:3s} = {np.round(img[[7, 8, 15]], 4).tolist()} in (e7, e8, e15); "
              f"|psi R psi^-1 - R_(psi u)| = {nrm(P @ R(x) @ Pi - R(img)):.1e}")

    print("\n(6) Oktant mit den urspruenglichen Rollen auf N (Bezug: psi-Eigenzustand; Zyklus: Hurwitz-Einheit)")
    v1 = np.zeros(16, complex); v1[0], v1[8] = 1, 1j
    vw = np.zeros(16, complex); vw[7], vw[15] = 1, -1j
    v1 /= np.linalg.norm(v1); vw /= np.linalg.norm(vw)
    for hc in ((1, 1, 1, 1), (-1, -1, -1, -1), (1, -1, 1, 1)):
        Rh = R(quat(np.array(hc) / 2)).astype(complex)
        for rname, r in (("1+i e8", v1), ("e7-i e15", vw)):
            orb = [r, Rh @ r, Rh @ Rh @ r]
            S = np.array([[np.vdot(x, y) for y in orb] for x in orb])
            rho2 = (abs(S[0, 1]) ** 2 + abs(S[1, 2]) ** 2 + abs(S[2, 0]) ** 2) / 3
            ph = abs(np.angle(S[0, 1] * S[1, 2] * S[2, 0]))
            print(f"    h = {hc}/2, Bezug {rname:8s}: rho^2 = {rho2:.6f}, K = {(1 + 2 * rho2) / 3:.6f}, "
                  f"Phase {ph:.6f} (pi/4 = {np.pi / 4:.6f}), Rang {np.linalg.matrix_rank(S, 1e-9)}, "
                  f"bleibt in N: {nrm(Qs @ orb[1]) < 1e-12}")
    h, hb = quat(np.array([1, 1, 1, 1]) / 2), qbar(np.array([1, 1, 1, 1]) / 2)
    print("    Konjugation mit h auf den Achsen: " + "; ".join(
        f"{n} -> {np.round(smul(smul(hb, x), h)[[7, 8, 15]], 3).tolist()}" for n, x in (("e7", e7), ("e8", e8), ("e15", e15))))

    print("\n(7) Majorana-Bilinear des Familien-Dubletts N: Zerlegung von N (x) N unter der Familien-su(2)")
    Bn = np.array([v1, vw]).T
    J = [Bn.conj().T @ (Ra / 2) @ Bn for Ra in (R7, R15, R8)]
    J2 = [np.kron(j, np.eye(2)) + np.kron(np.eye(2), j) for j in J]
    C2 = -sum(j @ j for j in J2)
    SW = np.zeros((4, 4)); SW[0, 0] = SW[3, 3] = 1; SW[1, 2] = SW[2, 1] = 1
    Bs = np.linalg.svd((np.eye(4) + SW) / 2)[0][:, :3]
    Ba = np.linalg.svd((np.eye(4) - SW) / 2)[0][:, :1]
    print(f"    Casimir auf dem symmetrischen Teil (dim 3): {fmt_eigs(np.linalg.eigvals(Bs.conj().T @ C2 @ Bs))} (Vektor: 2); "
          f"auf dem antisymmetrischen (dim 1): {fmt_eigs(np.linalg.eigvals(Ba.conj().T @ C2 @ Ba))} (Singulett: 0)")
