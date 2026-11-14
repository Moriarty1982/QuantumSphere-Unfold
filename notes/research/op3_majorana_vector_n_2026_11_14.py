"""Erkundung (14.11.2026, nicht blind): symmetrische (Majorana-)Bilinearformen auf dem neutralen Qubit N.

Ein Majorana-Term nu^T M nu hat M symmetrisch; unter der Familien-su(2) ist das der Vektor (Spin 1) in Im H_n.
(1) Die native symmetrische Bilinearform von S (reelles Skalarprodukt, komplex-bilinear fortgesetzt) auf N.
(2) Formen x^T W y mit Woertern W aus L_a, R_a (a in e7, e8, e15) bis Laenge 2: symmetrischer Teil auf N.
(3) Wirkung M -> U^T M U der nativen Elemente (psi; zweizaehlig R_e8, R_e7; dreizaehlig R_h): Eigenformen,
    Eigenwerte, Singulaerwerte (zwei Massen) und Richtung des Vektors.
(4) Mischung der psi-festen und der h-festen Form: K der zwei Massen (mit dritter Masse null).
Aufruf: python op3_majorana_vector_n_2026_11_14.py
"""
import importlib.util
import itertools
import os
import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
spec = importlib.util.spec_from_file_location("fs", os.path.join(HERE, "op3_family_su2_right_action_2026_11_14.py"))
fs = importlib.util.module_from_spec(spec)
spec.loader.exec_module(fs)
L, R, su, quat = fs.L, fs.R, fs.su, fs.quat

SX = np.array([[0, 1], [1, 0]], complex)
SY = np.array([[0, -1j], [1j, 0]])
SZ = np.diag([1.0 + 0j, -1])
EPS = np.array([[0, 1], [-1, 0]], complex)
# Basis der symmetrischen 2x2-Matrizen als Vektor: M = (m . sigma) eps
VEC = [s @ EPS for s in (SX, SY, SZ)]


def to_vec(M):
    """Komponenten m mit M = (m . sigma) eps; M symmetrisch."""
    A = np.array([v.ravel() for v in VEC]).T
    return np.linalg.lstsq(A, M.ravel(), rcond=None)[0]


def describe(M):
    sv = np.linalg.svd(M, compute_uv=False)
    m = to_vec(M)
    n = np.linalg.norm(m)
    mm = abs(np.sum(m * m)) / n ** 2 if n > 1e-12 else 0.0          # 1: reelle Richtung, 0: Nullvektor
    cz = abs(m[2]) / n if n > 1e-12 else 0.0
    return sv / sv.max() if sv.max() > 1e-12 else sv, mm, cz, m / n if n > 1e-12 else m


def K2(sv):
    """Koide-Groesse der Massen (sv[0], sv[1], 0)."""
    s = np.sqrt(sv)
    return float(np.sum(sv) / np.sum(s) ** 2)


if __name__ == "__main__":
    P, SU3, P0, Pc, P3, P3b, Qs = fs.setup()
    e7, e8, e15 = su(7), su(8), su(15)
    v1 = np.zeros(16, complex); v1[0], v1[8] = 1, 1j
    vw = np.zeros(16, complex); vw[7], vw[15] = 1, -1j
    v1 /= np.linalg.norm(v1); vw /= np.linalg.norm(vw)
    B = np.array([v1, vw]).T
    onN = lambda X: B.conj().T @ X @ B
    # Kontrolle: Pauli-Tripel auf N (i R_e7, i R_e15, i R_e8) ~ (sx, sy, sz) bis auf Vorzeichen
    pa = [onN(1j * R(x)) for x in (e7, e15, e8)]
    pauli = (all(np.allclose(p @ p, np.eye(2)) for p in pa)
             and all(np.allclose(a @ b + b @ a, 0) for a, b in itertools.combinations(pa, 2)))
    print(f"Kontrolle: i R_e7, i R_e15, i R_e8 auf N sind ein Pauli-Tripel: {pauli}; "
          f"i R_e8 = +-sz: {bool(min(np.linalg.norm(pa[2] - SZ), np.linalg.norm(pa[2] + SZ)) < 1e-12)}")

    print("\n(1) Native symmetrische Bilinearform x^T y auf N:")
    G = B.T @ B
    print(f"    Gram (bilinear) = {np.round(G, 12).tolist()}  -> N ist isotrop: {np.allclose(G, 0)}")

    print("\n(2) Formen x^T W y, W Wort aus L_a, R_a (a = e7, e8, e15), Laenge 1 und 2; symmetrischer Teil auf N")
    ops = {f"{k}_{n}": f(x) for k, f in (("L", L), ("R", R)) for n, x in (("e7", e7), ("e8", e8), ("e15", e15))}
    words = [((a,), ops[a]) for a in ops] + [((a, b), ops[a] @ ops[b]) for a, b in itertools.product(ops, repeat=2)]
    classes = {}
    nz = 0
    for name, Wm in words:
        M = B.T @ Wm @ B
        Ms = (M + M.T) / 2
        if np.linalg.norm(Ms) < 1e-12:
            continue
        nz += 1
        sv, mm, cz, m = describe(Ms)
        key = (tuple(np.round(sv, 6)), round(mm, 6), round(cz, 6))
        classes.setdefault(key, []).append("*".join(name))
    print(f"    {len(words)} Woerter, davon {nz} mit symmetrischem Teil ungleich null")
    for (sv, mm, cz), names in sorted(classes.items()):
        print(f"    Singulaerwerte {sv}, |m.m|/|m|^2 = {mm}, |m_z|/|m| = {cz}: {len(names)} Woerter, z. B. {names[:3]}")

    print("\n(3) Wirkung M -> U^T M U auf den symmetrischen Formen (Eigenwert; Singulaerwerte; Richtung)")
    h = quat(np.array([1, 1, 1, 1]) / 2)
    elems = [("psi (Ordnung 3, Achse e8)", onN(P)), ("R_e8 (zweizaehlig, Achse e8)", onN(R(e8))),
             ("R_e7 (zweizaehlig, Achse e7)", onN(R(e7))), ("R_h (dreizaehlig, Diagonale)", onN(R(h).astype(complex)))]
    fixed = {}
    for name, U in elems:
        A = np.array([to_vec(U.T @ V @ U) for V in VEC]).T            # 3x3 auf dem Vektor m
        w, X = np.linalg.eig(A)
        print(f"    {name}: det U = {np.round(np.linalg.det(U), 4)}")
        for k in range(3):
            if sum(abs(w - w[k]) < 1e-9) > 1:
                continue                                              # entarteter Eigenraum: Eigenform nicht eindeutig
            M = sum(X[j, k] * VEC[j] for j in range(3))
            sv, mm, cz, m = describe(M)
            print(f"        Eigenwert {np.round(w[k], 4)}: Massen {np.round(sv, 4).tolist()}, |m.m|/|m|^2 = {mm:.4f}, "
                  f"|m_z|/|m| = {cz:.4f}")
            if abs(w[k] - 1) < 1e-9:
                fixed[name.split(" ")[0]] = M / np.linalg.norm(M)
    print(f"    feste Formen (Eigenwert 1): {sorted(fixed)}")

    print("\n(4) Mischung M = cos(t) M_psi + sin(t) e^(i d) M_h: K der Massen (m1, m2, 0)")
    if "psi" in fixed and "R_h" in fixed:
        Mp, Mh = fixed["psi"], fixed["R_h"]
        for d in (0.0, np.pi / 2):
            ks = []
            for t in np.linspace(0, np.pi / 2, 7):
                sv = np.linalg.svd(np.cos(t) * Mp + np.sin(t) * np.exp(1j * d) * Mh, compute_uv=False)
                ks.append(K2(sv))
            print(f"    d = {d:.4f}: K(t = 0 .. pi/2) = {np.round(ks, 4).tolist()}")
        print("    K = 1: eine Masse; K = 1/2: zwei gleiche Massen; 2/3 wird bei einem freien Mischwinkel durchlaufen")
    else:
        print("    keine zwei festen Formen; Mischung entfaellt")
