"""k275 (Erkundung, nicht blind, 24.11.2026): Gibt die Trialitaet den drei Generationen eine Spin-1-Wirkung?
Traeger mit Trialitaet und drei Plaetzen: Albert-Algebra H3(O) (27 = 3 reelle Diagonalen + 3 Oktonionen x1, x2, x3).
Unter Spin(8) c F4 tragen x1, x2, x3 die drei Trialitaets-8er; auf G2 eingeschraenkt sind alle drei gleich (1 + 7).
A  Jordan-Produkt, Derivationen f4 (erwartet 52), diagonale Farbe su(3)_c (Stab e7 in G2) in f4.
B  Kommutant von su(3)_c in f4 (erwartet su(3)', 8) und reelle SO(3): X -> R X R^T in diesem Kommutanten.
C  Zerlegung: Farbsinguletts (Diagonale, Re-Anteile, e7-Anteile; 9) und Farbtripletts (e1..e6-Anteile; 18) unter su(3)' und so(3).
D  Ladung: vertauscht su(3)' bzw. so(3) mit der Ladungsstruktur je Platz (L_e7, R_e7, Q8 = 1/2 - i/6 L - i/3 R; r35/r42)?
   Groesste Unteralgebra von su(3)', die mit L_e7 und R_e7 (je Platz) vertauscht.
Konvention Oktonionen wie k253/k270. Aufruf aus diesem Ordner: python3 k275_albert_trialitaet.py
"""
import itertools
import numpy as np

rng = np.random.default_rng(275)


def conj(x):
    y = -x.copy(); y[0] = x[0]; return y


def omul(x, y):
    n = len(x)
    if n == 1:
        return x * y
    h = n // 2
    a, b, c, d = x[:h], x[h:], y[:h], y[h:]
    return np.concatenate([omul(a, c) - omul(conj(d), b), omul(d, a) + omul(b, conj(c))])


E8 = np.eye(8)
OT = np.array([[omul(E8[i], E8[j]) for j in range(8)] for i in range(8)])  # OT[i,j] = e_i e_j


def om(x, y):
    return np.einsum('i,j,ijk->k', x, y, OT)


# ---- Albert-Algebra: Vektor v (27) <-> 3x3-Matrix mit Oktonion-Eintraegen (3,3,8)
def to_mat(v):
    a = v[:3]; x1, x2, x3 = v[3:11], v[11:19], v[19:27]
    M = np.zeros((3, 3, 8))
    for k in range(3):
        M[k, k, 0] = a[k]
    M[0, 1] = x3; M[1, 0] = conj(x3)
    M[1, 2] = x1; M[2, 1] = conj(x1)
    M[2, 0] = x2; M[0, 2] = conj(x2)
    return M


def to_vec(M):
    return np.concatenate([[M[0, 0, 0], M[1, 1, 0], M[2, 2, 0]], M[1, 2], M[2, 0], M[0, 1]])


def mmul(A, B):
    C = np.zeros((3, 3, 8))
    for i in range(3):
        for j in range(3):
            for k in range(3):
                C[i, j] += om(A[i, k], B[k, j])
    return C


def jordan(u, v):
    A, B = to_mat(u), to_mat(v)
    return to_vec(0.5 * (mmul(A, B) + mmul(B, A)))


N = 27
I27 = np.eye(N)
CJ = np.array([[jordan(I27[i], I27[j]) for j in range(N)] for i in range(N)])  # CJ[i,j,k]

print("=" * 78)
print("A  Albert-Algebra H3(O)")
X, Y = rng.normal(size=N), rng.normal(size=N)
XY = jordan(X, Y); X2 = jordan(X, X)
print(f"   Jordan-Identitaet (X^2 o Y) o X = X^2 o (Y o X): Abw. {np.abs(jordan(jordan(X2, Y), X) - jordan(X2, jordan(Y, X))).max():.1e}")


def der_basis(C):
    n = C.shape[0]; rows = []
    for i in range(n):
        for j in range(i, n):
            for m in range(n):
                r = np.zeros(n * n)
                for k in range(n):
                    if abs(C[i, j, k]) > 1e-12:
                        r[m * n + k] += C[i, j, k]
                for p in range(n):
                    if abs(C[p, j, m]) > 1e-12:
                        r[p * n + i] -= C[p, j, m]
                    if abs(C[i, p, m]) > 1e-12:
                        r[p * n + j] -= C[i, p, m]
                if np.abs(r).max() > 1e-12:
                    rows.append(r)
    A = np.array(rows)
    _, s, vt = np.linalg.svd(A, full_matrices=True)
    rank = int((s > 1e-9).sum())
    return [v.reshape(n, n) for v in vt[rank:]]


F4 = der_basis(CJ)
print(f"   dim Der(H3(O)) = {len(F4)}  (f4: 52)")
F4flat = np.array([D.ravel() for D in F4])


def in_span(M, basis_flat):
    c, *_ = np.linalg.lstsq(basis_flat.T, M.ravel(), rcond=None)
    return np.abs(basis_flat.T @ c - M.ravel()).max()


# Farbe: Derivationen von O mit D e7 = 0, diagonal auf x1, x2, x3
def der_O(fix):
    rows = []
    for i in range(8):
        for j in range(8):
            for m in range(8):
                r = np.zeros(64)
                for k in range(8):
                    if OT[i, j, k]:
                        r[m * 8 + k] += OT[i, j, k]
                for p in range(8):
                    if OT[p, j, m]:
                        r[p * 8 + i] -= OT[p, j, m]
                    if OT[i, p, m]:
                        r[p * 8 + j] -= OT[i, p, m]
                if r.any():
                    rows.append(r)
    for f in fix:
        for m in range(8):
            r = np.zeros(64); r[m * 8 + f] = 1; rows.append(r)
    _, s, vt = np.linalg.svd(np.array(rows))
    return [v.reshape(8, 8) for v in vt[(s > 1e-9).sum():]]


def diag_slots(M8):
    D = np.zeros((N, N))
    for s in range(3):
        o = 3 + 8 * s
        D[o:o + 8, o:o + 8] = M8
    return D


SU3c = [diag_slots(D) for D in der_O((7,))]
G2 = [diag_slots(D) for D in der_O(())]
print(f"   su(3)_c: {len(SU3c)} Generatoren, in f4 (max Rest {max(in_span(D, F4flat) for D in SU3c):.1e}); g2 diagonal: {len(G2)}, in f4 ({max(in_span(D, F4flat) for D in G2):.1e})")

print("=" * 78)
print("B  Kommutant der Farbe in f4 und die reelle SO(3)")


def commutant(basis, others):
    # Koeffizienten c mit [sum c_a B_a, O] = 0 fuer alle O
    rows = []
    for O in others:
        rows.append(np.array([(B @ O - O @ B).ravel() for B in basis]).T)
    A = np.vstack(rows)
    _, s, vt = np.linalg.svd(A)
    null = vt[(s > 1e-9).sum():]
    return [sum(c[a] * basis[a] for a in range(len(basis))) for c in null]


SU3p = commutant(F4, SU3c)
print(f"   Kommutant von su(3)_c in f4: dim {len(SU3p)}")
SU3pflat = np.array([D.ravel() for D in SU3p])
# Kommutant von g2 in f4
SO3g2 = commutant(F4, G2)
print(f"   Kommutant von g2 in f4: dim {len(SO3g2)}  (F4 > G2 x SO(3): erwartet 3)")


# reelle SO(3): X -> R X R^T, Generatoren T_a = d/dt
def so3_gen(a):
    Lg = np.zeros((3, 3)); i, j = [(1, 2), (2, 0), (0, 1)][a]
    Lg[i, j], Lg[j, i] = -1, 1
    T = np.zeros((N, N))
    for k in range(N):
        M = to_mat(I27[k])
        dM = np.einsum('ij,jkl->ikl', Lg, M) + np.einsum('ijl,kj->ikl', M, Lg)  # L M + M L^T
        T[:, k] = to_vec(dM)
    return T


SO3 = [so3_gen(a) for a in range(3)]
print(f"   reelle so(3): in f4 (Rest {max(in_span(T, F4flat) for T in SO3):.1e}), im Kommutanten von g2 "
      f"({max(in_span(T, np.array([D.ravel() for D in SO3g2])) for T in SO3):.1e}), in su(3)' ({max(in_span(T, SU3pflat) for T in SO3):.1e})")

print("=" * 78)
print("C  Zerlegung der Materie")
idx_diag = [0, 1, 2]
idx_re = [3, 11, 19]
idx_e7 = [3 + 7, 11 + 7, 19 + 7]
idx_col = [3 + 8 * s + c for s in range(3) for c in range(1, 7)]
Ssing = I27[:, idx_diag + idx_re + idx_e7]
Strip = I27[:, idx_col]


def casimir_on(gens, S):
    # Unterraum invariant? Casimir -sum T^2 eingeschraenkt
    P = S @ S.T
    leak = max(np.abs((np.eye(N) - P) @ T @ S).max() for T in gens)
    Cm = -sum(T @ T for T in gens)
    ev = np.linalg.eigvalsh(S.T @ Cm @ S)
    vals, cnt = np.unique(np.round(ev, 6), return_counts=True)
    return leak, dict(zip(vals, cnt))


# Normierung su(3)': Generatoren orthonormieren bzgl. -tr(XY) auf der 27
G = np.array([[-np.trace(A @ B) for B in SU3p] for A in SU3p])
w, V = np.linalg.eigh(G)
SU3pn = [sum(V[a, b] * SU3p[a] for a in range(len(SU3p))) / np.sqrt(w[b]) for b in range(len(SU3p))]
for name, S in (("Farbsinguletts (9)", Ssing), ("Farbtripletts (18)", Strip)):
    l1, c1 = casimir_on(SU3pn, S)
    l2, c2 = casimir_on(SO3, S)
    print(f"   {name}: su(3)'-invariant (Leck {l1:.1e}), Casimir {c1};  so(3) (Leck {l2:.1e}), Casimir j(j+1): {c2}")
print("   Lesart: so(3)-Casimir 2 = Spin 1 (Vektor), 6 = Spin 2, 0 = Singulett.")
l3, c3 = casimir_on(SO3, I27[:, idx_e7])
l4, c4 = casimir_on(SO3, I27[:, idx_diag + idx_re])
print(f"   nur e7-Anteile (3): so(3)-Leck {l3:.1e}, Casimir {c3};  Diagonale + Re-Anteile (6): Leck {l4:.1e}, Casimir {c4}")

print("=" * 78)
print("D  Ladungsstruktur je Platz gegen die Generations-Symmetrie")


def slot_op(M8):
    return diag_slots(M8)


Le7 = slot_op(OT[7].T)          # x -> e7 x
Re7 = slot_op(OT[:, 7, :].T)    # x -> x e7
for name, gens in (("so(3) reell", SO3), ("su(3)'", SU3p)):
    cL = max(np.abs(T @ Le7 - Le7 @ T).max() for T in gens)
    cR = max(np.abs(T @ Re7 - Re7 @ T).max() for T in gens)
    print(f"   {name:12s}: max|[T, L_e7]| = {cL:.3f}, max|[T, R_e7]| = {cR:.3f}")
H = commutant(SU3p, [Le7, Re7])
print(f"   Unteralgebra von su(3)', die mit L_e7 und R_e7 (je Platz) vertauscht: dim {len(H)}")
if H:
    # Struktur: abelsch?
    ab = max((np.abs(A @ B - B @ A).max() for A, B in itertools.combinations(H, 2)), default=0.0)
    print(f"      abelsch: {ab < 1e-9} (max Kommutator {ab:.1e})")
    for A in H:
        ev = np.unique(np.round(np.linalg.eigvals(A).imag, 4))
        print(f"      Eigenwerte (Im) eines Generators: {ev}")
Hs = commutant(SO3, [Le7, Re7])
print(f"   Unteralgebra von so(3) reell, die mit L_e7, R_e7 vertauscht: dim {len(Hs)}")
# Diskrete Slot-Permutationen (S3 der Trialitaet als Teil von SO(3)): zyklische Vertauschung der Plaetze
P = np.array([[0, 0, 1], [1, 0, 0], [0, 1, 0]], float)
Pc = np.zeros((N, N))
for k in range(N):
    M = to_mat(I27[k]); Pc[:, k] = to_vec(np.einsum('ij,jkl,mk->iml', P, M, P))
print(f"   zyklische Platzvertauschung (R = Permutation, det +1): Automorphismus "
      f"{np.abs(Pc @ jordan(X, Y) - jordan(Pc @ X, Pc @ Y)).max():.1e}, [P, L_e7] = {np.abs(Pc @ Le7 - Le7 @ Pc).max():.1e}")

print("=" * 78)
print("E  Wo genau bricht die Ladung die Familien-SO(3)?")
for name, idx in (("Farbtripletts e1..e6 (18)", idx_col), ("Farbsinguletts (9)", idx_diag + idx_re + idx_e7)):
    S = I27[:, idx]
    cL = max(np.abs(S.T @ (T @ Le7 - Le7 @ T) @ S).max() for T in SO3)
    cR = max(np.abs(S.T @ (T @ Re7 - Re7 @ T) @ S).max() for T in SO3)
    print(f"   {name}: max|[T, L_e7]| = {cL:.1e}, max|[T, R_e7]| = {cR:.1e}")
print("   -> Auf den Quark-Anteilen vertauscht die Familien-SO(3) exakt mit der Ladungsstruktur; gebrochen wird sie nur")
print("      in der farbneutralen Ebene span(1, e7), wo L_e7 den Spin-2/Singulett-Teil (1) mit dem Vektor-Teil (e7) mischt.")
# Die 2-dim. Unteralgebra H: Wirkung zwischen Plaetzen?
blocks = lambda A: max(np.abs(A[3 + 8 * s:11 + 8 * s, 3 + 8 * t:11 + 8 * t]).max() for s in range(3) for t in range(3) if s != t)
print(f"   die 2-dim. Restalgebra in su(3)': Kopplung zwischen verschiedenen Plaetzen max {max(blocks(A) for A in H):.1e}"
      " (0 = nur Phasen je Platz, kein Generationswechsel)")

print("=" * 78)
print("F  Welche endliche Untergruppe der Familien-SO(3) uebersteht die Ladung?")


def rep27(R):
    Mx = np.zeros((N, N))
    for k in range(N):
        M = to_mat(I27[k]); Mx[:, k] = to_vec(np.einsum('ij,jkl,mk->iml', R, M, R))
    return Mx


ok, tot = [], 0
for perm in itertools.permutations(range(3)):
    for signs in itertools.product((1, -1), repeat=3):
        R = np.zeros((3, 3))
        for i, p in enumerate(perm):
            R[i, p] = signs[i]
        if np.linalg.det(R) < 0:
            continue
        tot += 1
        Rr = rep27(R)
        aut = np.abs(Rr @ jordan(X, Y) - jordan(Rr @ X, Rr @ Y)).max()
        c = max(np.abs(Rr @ Le7 - Le7 @ Rr).max(), np.abs(Rr @ Re7 - Re7 @ Rr).max())
        if c < 1e-9:
            ok.append((perm, signs))
        assert aut < 1e-9
even = sum(1 for p, s in ok if np.linalg.det(np.eye(3)[list(p)]) > 0)
print(f"   vorzeichenbehaftete Permutationen mit det +1 (Oktaedergruppe, {tot} Elemente): {len(ok)} vertauschen mit L_e7, R_e7,"
      f" davon mit gerader Platzpermutation {even}")
# Untergruppen-Check: abgeschlossen? Ordnung 12 und keine Elemente der Ordnung 4 -> A4
mats = []
for p, s in ok:
    R = np.zeros((3, 3))
    for i, q in enumerate(p):
        R[i, q] = s[i]
    mats.append(R)
closed = all(any(np.allclose(A @ B, C) for C in mats) for A in mats for B in mats)
orders = sorted({next(k for k in range(1, 13) if np.allclose(np.linalg.matrix_power(A, k), np.eye(3))) for A in mats})
print(f"   abgeschlossen: {closed}; Elementordnungen {orders} -> {'A4 (Tetraedergruppe)' if len(ok) == 12 and 4 not in orders else '?'}")
# Ikosaeder-Fortsetzung: 5-zaehlige Drehung um (0, 1, phi) (A5 enthaelt dieses A4)
phi = (1 + 5 ** 0.5) / 2
ax = np.array([0, 1, phi]); ax /= np.linalg.norm(ax)
K = np.array([[0, -ax[2], ax[1]], [ax[2], 0, -ax[0]], [-ax[1], ax[0], 0]])
th = 2 * np.pi / 5
R5 = np.eye(3) + np.sin(th) * K + (1 - np.cos(th)) * K @ K
Rr = rep27(R5)
print(f"   5-zaehlige Ikosaeder-Drehung: |[R, L_e7]| = {np.abs(Rr @ Le7 - Le7 @ Rr).max():.3f} -> A5 bricht")
# Zufallsdrehungen nahe 1 sind ausgeschlossen (Kommutant-Dimension 0, Teil D)
print("   -> Mit der Ladung bleibt von der Familien-SO(3) genau die Tetraedergruppe A4 (endlich, Lie-Algebra 0).")
print("      Die drei Plaetze tragen ihre dreidimensionale irreduzible Darstellung (Vektor von SO(3) eingeschraenkt).")
