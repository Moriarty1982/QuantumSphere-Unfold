"""Erkundung zu v4.10.0-r15.5: Kann der Generationsindex auf dem Frame-Dublett sitzen?

Notwendige Bedingung (Rueckwaertssuche): Ein Generations-Qubit mit drei gegenseitig unverzerrten Basen braucht drei
paarweise antikommutierende Involutionen, die mit Eichgruppe und Lorentzgruppe vertauschen (alle Generationen haben
dieselben Ladungen und denselben Spin). Sie muessen also im Kommutanten der Symmetrien liegen.

Teil A: das reelle Dublett (E, B) mit den Frame-Abbildungen T = sigma_z, J_B = sigma_x, R = Drehung um pi/2.
Teil B: Kommutant von SU(3)_c x SU(2)' x U(1)_Y x Lorentz auf C x H x O (Konventionen wie paper/short, Abschnitt 5;
        Oktonionen nach Cayley-Dickson wie k69_test_h17.py), komplex-linear und antilinear.
Teil C: dasselbe mit n Kopien (Multiplizitaet n).
Aufruf: python frame_bridge_commutant.py   (keine Datenpfade noetig)
"""
import numpy as np
from itertools import combinations

np.set_printoptions(precision=4, suppress=True)
TOL = 1e-9


def qmul(p, q):
    a1, b1, c1, d1 = p; a2, b2, c2, d2 = q
    return np.array([a1*a2-b1*b2-c1*c2-d1*d2, a1*b2+b1*a2+c1*d2-d1*c2,
                     a1*c2-b1*d2+c1*a2+d1*b2, a1*d2+b1*c2-c1*b2+d1*a2])


def qc(q): return q * np.array([1, -1, -1, -1])


def omul(x, y):
    p, q, r, s = x[:4], x[4:], y[:4], y[4:]
    return np.concatenate([qmul(p, r) - qmul(qc(s), q), qmul(s, p) + qmul(q, qc(r))])


def nullspace(M, tol=1e-8):
    _, s, vh = np.linalg.svd(M)
    rank = int((s > tol * max(1.0, s[0])).sum())
    return vh[rank:].conj().T


# ---------------------------------------------------------------- Teil A
print("Teil A: reelles Dublett (E, B)")
Sz = np.array([[1., 0], [0, -1]]); Sx = np.array([[0., 1], [1, 0]]); Rm = np.array([[0., -1], [1, 0]])
print(f"  T^2 = 1: {np.allclose(Sz@Sz, np.eye(2))},  J_B^2 = 1: {np.allclose(Sx@Sx, np.eye(2))},"
      f"  R^2 = -1: {np.allclose(Rm@Rm, -np.eye(2))}  -> R ist keine Involution, sondern eine komplexe Struktur")
# Lie-Algebra, die T, J_B, R aufspannen
basis = [Sz, Sx, Rm]
span = np.array([b.ravel() for b in basis + [Sz@Sx - Sx@Sz, Sx@Rm - Rm@Sx, Sz@Rm - Rm@Sz]])
dim = np.linalg.matrix_rank(span)
kill = np.array([[np.trace(a@b) for b in basis] for a in basis])
print(f"  reelle Huelle der Kommutatoren: Dimension {dim}; Spurform auf (T, J_B, R): Eigenwerte "
      f"{np.sort(np.linalg.eigvalsh(kill))} -> indefinit, also sl(2,R), nicht su(2)")
# Involutionen in O(2) ausser +-1: alle Spiegelungen; paarweise antikommutierend hoechstens zwei
print("  Involutionen von O(2) ausser +-1: Spiegelungen S(a) = cos(2a) sigma_z + sin(2a) sigma_x, eine Kreislinie;")
print("  sie liegen im 2-dim. Raum der spurfreien symmetrischen Matrizen -> hoechstens 2 paarweise antikommutierend")
# Komplexifiziert mit einer ZWEITEN Einheit j: j*R ist Involution, Eigenbasen unverzerrt
j = 1j
ops = {"T": Sz.astype(complex), "J_B": Sx.astype(complex), "jR": j * Rm}
vecs = {k: np.linalg.eigh(v)[1] if k != "jR" else np.linalg.eig(v)[1] for k, v in ops.items()}
print("  nach Komplexifizierung mit einer zweiten Einheit j (C^2 = R^2 x_R C):")
for a, b in combinations(ops, 2):
    ov = np.abs(vecs[a].conj().T @ vecs[b]) ** 2
    print(f"    |<{a}|{b}>|^2 = {np.round(ov, 6).ravel()}")
print("  Die dritte Basis entsteht erst mit j; mit j = i (der Einheit von z = E + iB) waere R skalar (Teil B).")

# ---------------------------------------------------------------- Teil B
print("\nTeil B: Kommutant der Symmetrien auf C x H x O (komplex 32-dim.)")
E8, E4 = np.eye(8), np.eye(4)
L = [np.array([omul(E8[a], E8[k]) for k in range(8)]).T for a in range(8)]
Rr = [np.array([omul(E8[k], E8[a]) for k in range(8)]).T for a in range(8)]
LH = [np.array([qmul(E4[a], E4[k]) for k in range(4)]).T for a in range(4)]
RH = [np.array([qmul(E4[k], E4[a]) for k in range(4)]).T for a in range(4)]
I4, I8 = np.eye(4), np.eye(8)
kron = np.kron

# Farbe: Derivationen von O, die e7 festhalten
rows = []
for a in range(8):
    for b in range(8):
        # D(e_a e_b) - D(e_a) e_b - e_a D(e_b) = 0, linear in D (64 Unbekannte, D[i, k])
        prod = omul(E8[a], E8[b])
        M = np.zeros((8, 64))
        for i in range(8):
            for k in range(8):
                Dik = np.zeros((8, 8)); Dik[i, k] = 1
                M[:, 8*i + k] = Dik @ prod - omul(Dik @ E8[a], E8[b]) - omul(E8[a], Dik @ E8[b])
        rows.append(M)
for i in range(8):            # D e7 = 0
    m = np.zeros(64); m[8*i + 7] = 1; rows.append(m[None, :])
der = nullspace(np.vstack(rows)).real
colour = [d.reshape(8, 8) for d in der.T]
g2 = nullspace(np.vstack(rows[:64])).shape[1]
print(f"  Derivationen von O: {g2} (g2), davon e7 fest: {len(colour)} (su(3))")

L7, R7 = L[7], Rr[7]
Qo = 0.5 * I8 - (1j/6) * L7 - (1j/3) * R7
Cch = kron(I4, 0.5 * (I8 + 1j * L7))
Tk = [kron(-0.5j * RH[k], I8) for k in (1, 2, 3)]
Tp = [Cch @ t for t in Tk]
Y2 = kron(I4, Qo) - 0.5 * np.eye(32) + (np.eye(32) - Cch) @ Tk[2]
lor = [kron(LH[k], I8) for k in (1, 2, 3)] + [1j * kron(LH[k], I8) for k in (1, 2, 3)]
col = [kron(I4, c) for c in colour]
gens = lor + Tp + [Y2] + col

def comm(a, b): return a@b - b@a
ok = all(np.allclose(comm(a, b), 0) for a in Tp + [Y2] for b in lor + col) and \
     np.allclose(comm(Tp[0], Tp[1]), 1j * Tp[2])
print(f"  Pruefung: SU(2)' und Y vertauschen mit Lorentz und Farbe, [T1',T2'] = i T3': {ok}")
ev = np.round(np.linalg.eigvals(Y2).real * 6).astype(int)
vals, cnt = np.unique(ev, return_counts=True)
print(f"  Spektrum von 6*Y/2 (Vielfachheit): {dict(zip(vals.tolist(), cnt.tolist()))}")

N = 32
def _null_gram(Ks, n):
    G = np.zeros((n*n, n*n), complex)
    for K in Ks: G += K.conj().T @ K
    w, v = np.linalg.eigh(G)
    return v[:, w < 1e-8 * max(1.0, w[-1])]
def lin_commutant(G, n):
    # [A, X] = 0; zeilenweise vec: vec(AX) = (A x I) vec X, vec(XA) = (I x A^T) vec X
    return _null_gram((kron(A, np.eye(n)) - kron(np.eye(n), A.T) for A in G), n)
def anti_commutant(G, n):
    # antilineares X = X0 K:  A X0 K = X0 K A = X0 conj(A) K  ->  A X0 - X0 conj(A) = 0
    return _null_gram((kron(A, np.eye(n)) - kron(np.eye(n), A.conj().T) for A in G), n)

Cl = lin_commutant(gens, N)
Ca = anti_commutant(gens, N)
print(f"  komplex-linearer Kommutant: Dimension {Cl.shape[1]} (ueber C)")
Xs = [Cl[:, k].reshape(N, N) for k in range(Cl.shape[1])]
abel = all(np.allclose(comm(a, b), 0, atol=1e-8) for a, b in combinations(Xs, 2))
print(f"  ... kommutativ: {abel}")
print(f"  antilinearer Kommutant: Dimension {Ca.shape[1]}")
print(f"  -> reeller Kommutant = C^{Cl.shape[1]}, kommutativ: kein Paar antikommutierender Operatoren,"
      " also kein Generations-Qubit")
# Frame-Abbildungen von r51: R = i*1 (im Kommutanten, zentral), T = K, J_B = iK
T_in = all(np.allclose(A, A.conj()) for A in gens)
print(f"  R = i*1 liegt im Kommutanten (zentral); T = K vertauscht mit allen Generatoren: {T_in};"
      f" J_B = iK ebenso nicht")
bad = [k for k, A in zip(["Lorentz"]*6 + ["SU(2)'"]*3 + ["Y"] + ["Farbe"]*8, gens) if not np.allclose(A, A.conj())]
print(f"  T scheitert an: {sorted(set(bad))}")

# ---------------------------------------------------------------- Teil C
print("\nTeil C: n Kopien derselben Generation")
S3 = [np.array([[0, 1], [1, 0]]), np.array([[0, -1j], [1j, 0]]), np.array([[1, 0], [0, -1]])]
okc = all(np.allclose(comm(kron(A, np.eye(2)), kron(np.eye(N), s)), 0) for A in gens for s in S3)
print(f"  n = 2: 1 x sigma_k vertauschen mit allen Generatoren (x 1): {okc}; nach Schur ist der Kommutant"
      " (C^6) x M_2(C) -> Generations-Qubit mit drei unverzerrten Basen vorhanden")
print("  Der Raum fuer ein Generations-Qubit entsteht erst durch die Vielfachheit; R = i*1 wirkt darauf skalar,")
print("  T = K vertauscht weiterhin nicht mit den Symmetrien. Die Kopien muessen also vorher da sein.")
