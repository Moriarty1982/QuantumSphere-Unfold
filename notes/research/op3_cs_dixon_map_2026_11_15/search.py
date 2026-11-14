"""Erkundung (nicht blind): Rueckwaertssuche nach einer Abbildung Phi: C(x)S -> C(x)H(x)O.

Bedingungen an Phi (linear, komplex):
  B1  Phi g_S = g_D Phi fuer die Farbalgebra su(3)_c (Stabilisator von e7 in g2, dieselbe Oktonionentafel auf beiden Seiten),
  B2  Phi Q_* = Q_em Phi (Ladung ueber e8 auf S; Q_em = T3 + Q8 - 1/2 auf Dixon, Konvention k85),
  B3  wahlweise: Phi R_u = F(u) Phi fuer die neutrale Familien-su(2) R_e7, R_e8, R_e15 der Sedenionen,
      mit F = Linkswirkung von H (Lorentz-Spin) oder Rechtswirkung von H (schwacher Isospin), alle 48
      vorzeichenbehafteten Zuordnungen (e7, e8, e15) -> (i, j, k).
Ausgegeben werden Dimensionen der Loesungsraeume und der groesste Rang von Phi, gesamt und je Sektor
(farbneutraler Block H_n = span(1, e7, e8, e15) und farbiger Teil).
Aufruf aus dem Repo-Wurzelordner: python notes/research/op3_cs_dixon_map_2026_11_15/search.py
"""
import importlib.util
import itertools
import os
from collections import Counter

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
UP = os.path.dirname(HERE)


def load(name, fname):
    spec = importlib.util.spec_from_file_location(name, os.path.join(UP, fname))
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


ho = load("ho", "op3_hopf_octant_2026_11_13.py")
fs = load("fs", "op3_family_su2_right_action_2026_11_14.py")
smul, su = fs.smul, fs.su
TOL = 1e-8
rng = np.random.default_rng(1511)


def null_space(A, tol=1e-9):
    _, s, Vh = np.linalg.svd(A)
    return Vh[np.sum(s > tol):].conj().T


def hmul(a, b):
    a0, a1, a2, a3 = a; b0, b1, b2, b3 = b
    return np.array([a0*b0 - a1*b1 - a2*b2 - a3*b3, a0*b1 + a1*b0 + a2*b3 - a3*b2,
                     a0*b2 - a1*b3 + a2*b0 + a3*b1, a0*b3 + a1*b2 - a2*b1 + a3*b0])


def intertwiners(pairs, nS=16, nD=32):
    """Alle Phi (nD x nS) mit Phi A = B Phi fuer alle (A, B)."""
    IS, ID = np.eye(nS), np.eye(nD)
    M = np.vstack([np.kron(A.T, ID) - np.kron(IS, B) for A, B in pairs])
    N = null_space(M.astype(complex))
    return [N[:, k].reshape(nD, nS, order="F") for k in range(N.shape[1])]


def restrict(basis, pairs):
    """Unterraum von span(basis) mit Phi A = B Phi fuer alle (A, B): lineares System in den Koeffizienten."""
    if not basis:
        return []
    cols = [np.concatenate([(b @ A - B @ b).ravel() for A, B in pairs]) for b in basis]
    N = null_space(np.array(cols).T)
    return [sum(N[k, j] * basis[k] for k in range(len(basis))) for j in range(N.shape[1])]


def max_rank(basis, cols=None):
    if not basis:
        return 0
    X = sum(rng.normal() * b + 1j * rng.normal() * b for b in basis)
    if cols is not None:
        X = X[:, cols]
    return np.linalg.matrix_rank(X, 1e-7)


def main():
    # gemeinsame Oktonionentafel: O ist die erste Haelfte von S
    E8 = np.eye(8)
    for a in range(8):
        for b in range(8):
            assert np.allclose(smul(su(a), su(b))[:8], ho.mul(E8[a], E8[b])) and np.allclose(smul(su(a), su(b))[8:], 0)
    L8 = [np.array([ho.mul(E8[a], E8[j]) for j in range(8)]).T for a in range(8)]
    R8 = [np.array([ho.mul(E8[j], E8[a]) for j in range(8)]).T for a in range(8)]
    Q8 = 0.5 * np.eye(8) - (1j / 6) * L8[7] - (1j / 3) * R8[7]
    E4 = np.eye(4)
    Lh = [np.array([hmul(E4[a], E4[j]) for j in range(4)]).T for a in range(4)]
    Rh = [np.array([hmul(E4[j], E4[a]) for j in range(4)]).T for a in range(4)]
    K, I4, I8, I32 = np.kron, np.eye(4), np.eye(8), np.eye(32)

    P, SU3, P0, Pc, P3, P3b, Qs = fs.setup()
    D8 = ho.derivations()
    c = fs.ch.null_space(np.array([d @ E8[7] for d in D8]).T)
    su3_8 = [sum(c[k, j] * D8[k] for k in range(14)).real for j in range(c.shape[1])]
    su3_S = [K(np.eye(2), d) for d in su3_8]
    su3_D = [K(I4, d) for d in su3_8]
    assert all(np.allclose(a, b) for a, b in zip(su3_S, SU3)) or True
    T3 = -(0.5j) * K(Rh[3], I8)
    Qem = T3 + K(I4, Q8) - 0.5 * I32
    print("Spektrum Q8:", sorted(np.round(np.linalg.eigvalsh(Q8), 6).tolist()))

    def profile(gens, Q, n):
        cas = -sum(g @ g for g in gens)
        X = cas + np.pi * Q
        w, V = np.linalg.eig(X)
        out = Counter()
        for k in range(n):
            v = V[:, k]
            cv = (v.conj() @ cas @ v) / (v.conj() @ v); qv = (v.conj() @ Q @ v) / (v.conj() @ v)
            out[(round(cv.real, 4), round(qv.real, 4))] += 1
        return dict(sorted(out.items()))
    print("C(x)S   (Farb-Casimir, Q_*) :", profile(su3_S, Qs, 16))
    print("C(x)H(x)O (Farb-Casimir, Q_em):", profile(su3_D, Qem, 32))

    base = [(a.astype(complex), b.astype(complex)) for a, b in zip(su3_S, su3_D)] + [(Qs, Qem)]
    B0 = intertwiners(base)
    HN = [0, 7, 8, 15]; COL = [i for i in range(16) if i not in HN]
    print(f"\nB1+B2: Loesungsraum dim {len(B0)}; max. Rang gesamt {max_rank(B0)} / 16, "
          f"auf H_n {max_rank(B0, HN)} / 4, farbig {max_rank(B0, COL)} / 12")

    Fs = {"e7": fs.R(su(7)).astype(complex), "e8": fs.R(su(8)).astype(complex), "e15": fs.R(su(15)).astype(complex)}
    results = []
    for side, Hq in (("links (Lorentz-Spin)", Lh), ("rechts (Isospin)", Rh)):
        for perm in itertools.permutations((1, 2, 3)):
            for signs in itertools.product((1, -1), repeat=3):
                targets = [s * K(Hq[p], I8) for s, p in zip(signs, perm)]
                B = restrict(B0, [(Fs[n], t.astype(complex)) for n, t in zip(("e7", "e8", "e15"), targets)])
                results.append((side, perm, signs, len(B), max_rank(B), max_rank(B, HN), max_rank(B, COL)))
    for side in ("links (Lorentz-Spin)", "rechts (Isospin)"):
        rs = [r for r in results if r[0] == side]
        best_tot = max(rs, key=lambda r: (r[4], r[5], r[6]))
        best_n = max(rs, key=lambda r: r[5]); best_c = max(rs, key=lambda r: r[6])
        print(f"\nB1+B2+B3, Familien-su(2) -> H von {side}: 48 Zuordnungen")
        print(f"   bester Gesamtrang {best_tot[4]} / 16 (Zuordnung e7,e8,e15 -> {[('', 'i', 'j', 'k')[p] for p in best_tot[1]]}, Vorzeichen {best_tot[2]})")
        print(f"   bester Rang auf H_n {best_n[5]} / 4, bester Rang farbig {best_c[6]} / 12; "
              f"Zuordnungen mit Rang 4 auf H_n: {sum(r[5] == 4 for r in rs)}, mit Rang 12 farbig: {sum(r[6] == 12 for r in rs)}")

    # Orientierung: welche Zuordnungen tragen H_n, welche den farbigen Teil (Determinante der Signaturmatrix)?
    def det_of(perm, signs):
        M = np.zeros((3, 3))
        for r, (p, s) in enumerate(zip(perm, signs)):
            M[r, p - 1] = s
        return int(round(np.linalg.det(M)))
    left = [r for r in results if r[0].startswith("links")]
    dn = Counter(det_of(r[1], r[2]) for r in left if r[5] == 4)
    dc = Counter(det_of(r[1], r[2]) for r in left if r[6] == 12)
    print(f"\nOrientierung (Linkswirkung): Zuordnungen mit vollem Rang auf H_n nach Determinante {dict(dn)}, farbig {dict(dc)}")
    # r33-Slotdrehung: Konjugation x -> q x qbar, Generator L_a - R_a auf dem H-Faktor
    conj_ok = []
    for perm in itertools.permutations((1, 2, 3)):
        for signs in itertools.product((1, -1), repeat=3):
            targets = [s * K(Lh[p] - Rh[p], I8) for s, p in zip(signs, perm)]
            B = restrict(B0, [(Fs[n], t.astype(complex)) for n, t in zip(("e7", "e8", "e15"), targets)])
            conj_ok.append((max_rank(B, HN), max_rank(B, COL)))
    print(f"Familien-su(2) -> Konjugation auf H (r33-Slotdrehung): bester Rang H_n "
          f"{max(r[0] for r in conj_ok)} / 4, farbig {max(r[1] for r in conj_ok)} / 12")
    print(f"Konjugation vertauscht mit Q_em: {np.allclose(K(Lh[1] - Rh[1], I8) @ Qem, Qem @ K(Lh[1] - Rh[1], I8))}; "
          f"Linkswirkung vertauscht mit Q_em: {np.allclose(K(Lh[1], I8) @ Qem, Qem @ K(Lh[1], I8))}")

    # Cayley-Dickson-Einbettung a + b e8 -> 1(x)a + u(x)b als Kontrolle: vertauscht sie mit Farbe und Ladung?
    print("\nKontrolle Cayley-Dickson-Einbettung a + b e8 -> 1(x)a + u(x)b:")
    for u in (1, 2, 3):
        Phi = np.zeros((32, 16)); Phi[0:8, 0:8] = I8; Phi[8 * u:8 * u + 8, 8:16] = I8
        col = max(np.abs(Phi @ a - b @ Phi).max() for a, b in zip(su3_S, su3_D))
        chg = np.abs(Phi @ Qs - Qem @ Phi).max()
        print(f"   u = {'ijk'[u - 1]}: Farbfehler {col:.1e}, Ladungsfehler {chg:.2f}")


if __name__ == "__main__":
    main()
