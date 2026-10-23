"""k79: Test der Vorab-Notiz H23 (Commit 55043f8): Frame-Triole M/P/T als Z2-Seite der Triality.
rho(x,y,z) = (conj x, conj z, conj y) auf der Symmetrie-Algebra g von t = Re((xy)z)."""
import itertools, numpy as np, os, sys
from scipy.linalg import null_space
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from k69_test_h17 import omul

TOL = 1e-9
E = np.eye(8)
T3 = np.array([[[omul(omul(E[i], E[j]), E[k])[0] for k in range(8)] for j in range(8)] for i in range(8)])
pairs = [(a, b) for a in range(8) for b in range(a + 1, 8)]
so8 = []
for a, b in pairs:
    X = np.zeros((8, 8)); X[a, b] = 1; X[b, a] = -1; so8.append(X)
M = np.column_stack([np.einsum('mi,mjk->ijk', X, T3).ravel() for X in so8] +
                    [np.einsum('mj,imk->ijk', X, T3).ravel() for X in so8] +
                    [np.einsum('mk,ijm->ijk', X, T3).ravel() for X in so8])
N = null_space(M, rcond=1e-12)
mat = lambda c: sum(c[s]*so8[s] for s in range(28))
sg = np.array([1] + [-1]*7)
D = np.diag([sg[a]*sg[b] for a, b in pairs])                   # c X c = s_a s_b X
Z = np.zeros((28, 28))
P = np.block([[D, Z, Z], [Z, Z, D], [Z, D, Z]])                # rho auf (A, B, C)
def intertw(L1, L2):                                            # dim {X : X L1_s = L2_s X}
    K = np.vstack([np.kron(np.eye(8), b) - np.kron(a.T, np.eye(8)) for a, b in zip(L1, L2)])
    return 64 - np.linalg.matrix_rank(K, TOL)
slots = lambda V: [[mat(V[28*p:28*(p + 1), d]) for d in range(V.shape[1])] for p in range(3)]

# H23a
closed = abs(M@(P@N)).max()
order2 = abs(P@P - np.eye(84)).max()
S0, S1 = slots(N), slots(P@N)
cls = {(i, j): intertw(S1[i], S0[j]) for i in range(3) for j in range(3)}
ok_a = closed < TOL and order2 < TOL and cls[(0, 0)] == 1 and cls[(1, 2)] == 1 and cls[(2, 1)] == 1 and \
       cls[(1, 1)] == 0 and cls[(2, 2)] == 0 and cls[(0, 1)] == 0 and cls[(0, 2)] == 0
print(f"H23a: rho bildet g auf sich ab ({closed:.0e}), Ordnung 2 ({order2:.0e});"
      f" Verflechtung Platz i des Bildes mit Platz j: {cls} -> {'bestaetigt' if ok_a else 'widerlegt'}")

# H23b
F = null_space(np.vstack([M, P - np.eye(84)]), rcond=1e-12)
Fs = slots(F)
line = max(abs(A@E[0]).max() for A in Fs[0])
def commutant(L): return intertw(L, L)
c1, c2, c3, c23 = commutant(Fs[0]), commutant(Fs[1]), commutant(Fs[2]), intertw(Fs[1], Fs[2])
L7 = [A[1:, 1:] for A in Fs[0]]
K7 = np.vstack([np.kron(np.eye(7), b) - np.kron(b.T, np.eye(7)) for b in L7]); c7 = 49 - np.linalg.matrix_rank(K7, TOL)
ok_b = F.shape[1] == 21 and line < TOL and c1 == 2 and c7 == 1 and c2 == 1 and c3 == 1 and c23 == 1
print(f"\nH23b: rho-feste Unteralgebra: Dimension {F.shape[1]} (21 = so(7)); Platz 1: A*1 = 0 ({line:.0e}),"
      f" Kommutant {c1} (2 = 1 + 7), auf dem 7er-Teil {c7} (1 = irreduzibel); Platz 2, 3: Kommutant {c2}, {c3};"
      f" Platz 2 ~ Platz 3: Verflechtungsraum {c23} -> {'bestaetigt' if ok_b else 'widerlegt'}")

# H23c
rng = np.random.default_rng(79)
vs = rng.normal(size=(10, 3, 8))
t = lambda x, y, z: omul(omul(x, y), z)[0]
good = [s for s in itertools.product((1, -1), repeat=3)
        if max(abs(t(s[0]*x, s[1]*y, s[2]*z) - t(x, y, z)) for x, y, z in vs) < TOL]
ok_c = sorted(good) == sorted(s for s in itertools.product((1, -1), repeat=3) if np.prod(s) == 1)
print(f"\nH23c: zulaessige Vorzeichen-Tripel {good}; auf dem rho-festen Platz 1 trivial: "
      f"{[s for s in good if s[0] == 1 and s != (1, 1, 1)]} -> {'bestaetigt' if ok_c else 'widerlegt'} (trivial)")

# H23d
gens = [(1, 2, 0), (0, 2, 1)]
comp = lambda p, q: tuple(p[q[i]] for i in range(3))
G = {(0, 1, 2)}; fr = [(0, 1, 2)]
while fr:
    nw = []
    for p in fr:
        for g in gens:
            q = comp(g, p)
            if q not in G: G.add(q); nw.append(q)
    fr = nw
fix = {p: sum(p[i] == i for i in range(3)) for p in G}
ok_d = len(G) == 6 and sorted(fix.values()) == [0, 0, 1, 1, 1, 3]
print(f"\nH23d: Gruppe auf den Plaetzen: Ordnung {len(G)}; Fixpunktzahlen {sorted(fix.values())}"
      f" (Z3: 0 Fixpunkte, Bahn 3; Transpositionen: 1 Fixpunkt, Bahn 2) -> {'bestaetigt' if ok_d else 'widerlegt'} (Kontrolle)")

# H23e
Nd = null_space(M@np.vstack([np.eye(28)]*3), rcond=1e-12)
g2 = np.vstack([Nd]*3)
res_e = abs(P@g2 - g2).max()
in_F = np.linalg.matrix_rank(np.hstack([F, g2]), TOL) == F.shape[1]
ok_e = Nd.shape[1] == 14 and res_e < TOL and in_F
print(f"\nH23e: g2 (A,A,A), Dimension {Nd.shape[1]}: rho-fest ({res_e:.0e}), in der rho-festen Unteralgebra: {in_F}"
      f" -> {'bestaetigt' if ok_e else 'widerlegt'}")
