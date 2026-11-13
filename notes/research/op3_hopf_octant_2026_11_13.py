"""Erkundung: Oktanten-Tripel im Hopf-Traeger von r15 (13.11.2026, nicht blind, kein Datenvergleich).

r15: Plaetze = Einheits-Oktonionen (a, b, c) mit (ab)c = 1; symmetrischer Punkt a = b = c, a^3 = 1, a = exp(2 pi u/3).
Gelesen als Transport: Position nach k Schritten p_k = s_k f s_k^-1 mit s_1 = a, s_2 = ab, s_3 = (ab)c = 1 (Schleife schliesst).
Geprueft fuer u = e7 (Ladungsachse, Komplexstruktur J = L_e7):
(1) Konjugation mit a = exp(2 pi e7/3) ist ein Automorphismus, fixiert e7, vertauscht mit L_e7 (Q_em-vertraeglich);
(2) f = (e7 + sqrt2 g)/sqrt3 mit g senkrecht e7: Bahn f, a f a^-1, a^2 f a^-2 paarweise orthogonal, assoziative Unteralgebra;
(3) als Qubits gelesen: rho^2 = 1/2, Rang 2, Bargmann-Phase pi/4 (Oktant).
Aufruf: python op3_hopf_octant_2026_11_13.py
"""
import numpy as np

# Oktonionen ueber Fano-Ebene: e_i e_j = e_k fuer (i, j, k) in TRIPLES (zyklisch), Index 0 = 1
TRIPLES = [(1, 2, 3), (1, 4, 5), (1, 7, 6), (2, 4, 6), (2, 5, 7), (3, 4, 7), (3, 6, 5)]
M = np.zeros((8, 8, 8))
for i in range(8):
    M[0, i, i] = M[i, 0, i] = 1
for i in range(1, 8):
    M[i, i, 0] = -1
for (a, b, c) in TRIPLES:
    for (x, y, z) in ((a, b, c), (b, c, a), (c, a, b)):
        M[x, y, z] = 1
        M[y, x, z] = -1


def mul(x, y):
    return np.einsum("i,j,ijk->k", x, y, M)


def conj(x):
    return np.concatenate([[x[0]], -x[1:]])


def unit(k):
    e = np.zeros(8); e[k] = 1; return e


rng = np.random.default_rng(15)

if __name__ == "__main__":
    # Kontrolle: Alternativitaet und Norm
    x, y = rng.normal(size=8), rng.normal(size=8)
    print(f"Kontrolle: |xy| = |x||y| {np.isclose(np.linalg.norm(mul(x, y)), np.linalg.norm(x) * np.linalg.norm(y))}, "
          f"x(xy) = (xx)y {np.allclose(mul(x, mul(x, y)), mul(mul(x, x), y))}")
    e7 = unit(7)
    a = np.cos(2 * np.pi / 3) * unit(0) + np.sin(2 * np.pi / 3) * e7
    ai = conj(a)
    print(f"a^3 = 1: {np.allclose(mul(mul(a, a), a), unit(0))}")
    C = lambda v: mul(mul(a, v), ai)
    # (1) Automorphismus, Fixpunkt e7, Vertauschung mit L_e7
    auto = max(np.abs(C(mul(x, y)) - mul(C(x), C(y))).max() for x, y in
               ((rng.normal(size=8), rng.normal(size=8)) for _ in range(200)))
    comm = max(np.abs(C(mul(e7, x)) - mul(e7, C(x))).max() for x in (rng.normal(size=8) for _ in range(200)))
    print(f"(1) Konjugation mit a: Automorphismus (max. Fehler {auto:.1e}), fixiert e7 {np.allclose(C(e7), e7)}, "
          f"vertauscht mit L_e7 (max. Fehler {comm:.1e})")
    # Wirkung auf e7-orthogonale Einheiten: Drehung um 4pi/3 in der komplexen Ebene (g, e7 g) -> Skalar omega^2, Zentrum von SU(3)
    g = unit(1)
    eg = mul(e7, g)
    Cg = C(g)
    print(f"    C(g) = {np.dot(Cg, g):+.4f} g {np.dot(Cg, eg):+.4f} e7g  (cos 4pi/3 = {np.cos(4 * np.pi / 3):+.4f}, sin = {np.sin(4 * np.pi / 3):+.4f})")
    # (2) Bahn des Vektors mit Winkel arccos(1/sqrt3) zur Ladungsachse
    f = (e7 + np.sqrt(2) * g) / np.sqrt(3)
    orb = [f, C(f), C(C(f))]
    G = np.array([[np.dot(p, q) for q in orb] for p in orb])
    print(f"(2) Bahn von f: Skalarprodukte\n{np.round(G, 12)}")
    print(f"    C^3(f) = f: {np.allclose(C(C(C(f))), f)};  Produkt f0 f1 = +-f2: "
          f"{np.allclose(mul(orb[0], orb[1]), orb[2]) or np.allclose(mul(orb[0], orb[1]), -orb[2])}")
    # (3) als Qubits: Bloch-Vektoren in der Basis (e7, g, e7 g) der assoziativen Unteralgebra
    basis = [e7, g, eg]
    bl = [np.array([np.dot(p, b) for b in basis]) for p in orb]

    def qubit(n):
        n = n / np.linalg.norm(n)
        th, ph = np.arccos(np.clip(n[2], -1, 1)), np.arctan2(n[1], n[0])
        return np.array([np.cos(th / 2), np.exp(1j * ph) * np.sin(th / 2)])

    qs = [qubit(np.array([v[1], v[2], v[0]])) for v in bl]
    S = np.array([[np.vdot(p, q) for q in qs] for p in qs])
    c12, c23, c31 = S[0, 1], S[1, 2], S[2, 0]
    r2 = (abs(c12) ** 2 + abs(c23) ** 2 + abs(c31) ** 2) / 3
    print(f"(3) als Qubits: rho^2 = {r2:.6f}, Rang {np.linalg.matrix_rank(S, tol=1e-10)}, "
          f"Bargmann-Phase {np.angle(c12 * c23 * c31):+.6f} (pi/4 = {np.pi / 4:.6f})")
    # Gegenprobe: ein beliebiger Winkel zur Ladungsachse gibt keine Orthogonalitaet
    for cosang in (0.0, 0.3, 1 / np.sqrt(3), 0.8):
        h = cosang * e7 + np.sqrt(1 - cosang ** 2) * g
        print(f"    Winkel cos = {cosang:.4f}: <h, C h> = {np.dot(h, C(h)):+.4f}")


def derivations():
    """Basis der Derivationsalgebra g2 (D(xy) = D(x)y + xD(y)) als 8x8-Matrizen."""
    rows = []
    for i in range(8):
        for j in range(8):
            ei, ej = unit(i), unit(j)
            eij = mul(ei, ej)
            # lineare Gleichung in den 64 Eintraegen von D
            A = np.zeros((8, 64))
            for k in range(8):
                for l in range(8):
                    E = np.zeros((8, 8)); E[k, l] = 1
                    A[:, 8 * k + l] = E @ eij - mul(E @ ei, ej) - mul(ei, E @ ej)
            rows.append(A)
    A = np.vstack(rows)
    _, sv, Vt = np.linalg.svd(A)
    null = Vt[np.sum(sv > 1e-9):]
    return [v.reshape(8, 8) for v in null]


def stab_dim(D, vecs):
    if not vecs:
        return len(D)
    A = np.array([np.concatenate([d @ v for v in vecs]) for d in D]).T
    return len(D) - np.linalg.matrix_rank(A, tol=1e-9)


if __name__ == "__main__":
    print("\n== Magischer Winkel ==")
    print("    (a) Eine 120-Grad-Drehung, die ein Orthonormal-Dreibein zyklisch vertauscht, hat dessen Raumdiagonale als Achse;")
    print("        jeder Vektor des Dreibeins steht dann unter arccos(1/sqrt3) zur Achse. Bedingung = Plaetze orthonormal.")
    D = derivations()
    f = (e7 + np.sqrt(2) * unit(1)) / np.sqrt(3)
    fano = (unit(1) + unit(6) + e7) / np.sqrt(3)
    print(f"    (b) dim g2 = {len(D)}; Stabilisator von e7: {stab_dim(D, [e7])} (Farb-SU(3)); "
          f"von e7 und f: {stab_dim(D, [e7, f])}; von e7 und der Fano-Diagonale (e1+e6+e7)/sqrt3: {stab_dim(D, [e7, fano])}")
    print(f"        Fano-Diagonale: Winkel zu e7 cos = {np.dot(fano, e7):.6f} = 1/sqrt3 {1 / np.sqrt(3):.6f}")
    # farbneutrale imaginaere Richtungen: vom Stabilisator von e7 festgehalten
    # Unterraum der Stabilisator-Derivationen: Kern von d -> d e7
    Bm = np.array([(d @ e7) for d in D]).T
    _, sv, Vt = np.linalg.svd(Bm)
    coeffs = Vt[np.sum(sv > 1e-9):]
    Dsu3 = [sum(c * d for c, d in zip(cv, D)) for cv in coeffs]
    Mfix = np.vstack([d[1:, 1:] for d in Dsu3])
    _, sv2, Vt2 = np.linalg.svd(Mfix)
    fixed = Vt2[np.sum(sv2 > 1e-9):]
    print(f"    (c) imaginaere Richtungen, die die Farb-SU(3) festhaelt: {len(fixed)} (nur e7) -> jede Richtung unter dem "
          "magischen Winkel hat Farbanteile")


if __name__ == "__main__":
    print("\n== Neutrale Dixon-Richtungen (ohne Farbe und Ladung): e3 (x) 1, 1 (x) e7, e3 (x) e7 ==")
    # Linksmultiplikation auf H (x) O (reell 32-dim); Quaternionen ueber Paulimatrizen nicht noetig: H als 4x4 reell
    def qmul_mat(k):
        # Linksmultiplikation mit Quaternion-Einheit k in Basis (1, i, j, k)
        tab = {(1, 1): (0, -1), (1, 2): (3, 1), (1, 3): (2, -1), (2, 1): (3, -1), (2, 2): (0, -1), (2, 3): (1, 1),
               (3, 1): (2, 1), (3, 2): (1, -1), (3, 3): (0, -1)}
        Mq = np.zeros((4, 4))
        for b in range(4):
            if b == 0:
                Mq[k, 0] = 1
            else:
                idx, sg = tab[(k, b)]
                Mq[idx, b] = sg
        return Mq
    Lo7 = np.array([mul(e7, unit(b)) for b in range(8)]).T
    I4, I8 = np.eye(4), np.eye(8)
    E3 = np.kron(qmul_mat(3), I8); E7 = np.kron(I4, Lo7); E37 = E3 @ E7
    for lab, X in (("e3 (x) 1", E3), ("1 (x) e7", E7), ("e3 (x) e7", E37)):
        sq = X @ X
        print(f"    ({lab})^2 = {'+1' if np.allclose(sq, np.eye(32)) else ('-1' if np.allclose(sq, -np.eye(32)) else '?')}")
    print("    -> zwei Richtungen mit Quadrat -1, eine mit +1: Signatur (2,1), wie die indefinite Form im neutralen Sektor.")
    print("    In Signatur (2,1) gibt es keine drei paarweise orthogonalen raumartigen Einheitsvektoren: ein exakter Oktant")
    print("    ist dort nicht moeglich (Sylvester); eine Lorentz-Fassung waere eine eigene Rechnung.")
