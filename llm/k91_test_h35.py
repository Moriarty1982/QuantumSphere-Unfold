"""k91: Test der Vorab-Notiz H35 (Commit 42e4fcc): Ist e7 die Bezugsachse der Frames? Frame-Abbildungen R (z -> iz), T (z -> conj z),
J_B = R o T auf C x O; innere Gegenstuecke mit J = L_e7; Frame-Ebene und Singulett-Ebene."""
import numpy as np, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from k69_test_h17 import omul

TOL = 1e-9
E = np.eye(8)
L7 = np.array([omul(E[7], E[j]) for j in range(8)]).T
R7 = np.array([omul(E[j], E[7]) for j in range(8)]).T
iL, iR = 1j*L7, 1j*R7
Q = 0.5*np.eye(8) - (1j/6)*L7 - (1j/3)*R7
BL = 2*(Q - 0.5*np.eye(8))
def P(l, r): return 0.25*(np.eye(8) + l*iL)@(np.eye(8) + r*iR)
S = [(1, 1), (-1, 1), (1, -1), (-1, -1)]

# Derivationen von O (Lie-Algebra g2) und ihr Stabilisator von e7 (su(3))
mt = np.array([[omul(E[a], E[b]) for b in range(8)] for a in range(8)])     # mt[a, b] = e_a e_b
rows = []
for a in range(8):
    for b in range(8):
        for k in range(8):
            row = np.zeros(64)
            # (D(e_a e_b))_k - (D e_a e_b)_k - (e_a D e_b)_k = 0,  D[i, j] = Variable 8 i + j (D e_j = sum_i D[i, j] e_i)
            for j in range(8): row[8*k + j] += mt[a, b, j]
            for i in range(8): row[8*i + a] -= mt[i, b, k]; row[8*i + b] -= mt[a, i, k]
            rows.append(row)
A = np.array(rows)
_, sv, Vt = np.linalg.svd(A)
der = Vt[np.sum(sv > 1e-9):]                                                # Basis der Derivationen
g2 = [d.reshape(8, 8) for d in der]
# Stabilisator von e7: D e7 = 0
Mst = np.array([d.reshape(8, 8)[:, 7] for d in der]).T
_, s2, V2 = np.linalg.svd(Mst)
coef = V2[np.sum(s2 > 1e-9):]
su3 = [sum(c[i]*g2[i] for i in range(len(g2))) for c in coef]
print(f"Vorpruefung: dim g2 = {len(g2)}, dim Stab(e7) = {len(su3)}")

# H35a
Rop = 1j*np.eye(8)                                  # z -> iz, C-linear
comm = max(abs(Rop@X - X@Rop).max() for X in [iL, iR, Q, BL] + su3 + [P(*s) for s in S])
# T: v -> conj(v); T X T^-1 = conj(X).  J_B = R o T: v -> i conj(v); J_B X J_B^-1 = conj(X) (i kommutiert)
swapT = max(abs(np.conj(P(l, r)) - P(-l, -r)).max() for l, r in S)
ok_a = comm < TOL and swapT < TOL
print(f"\nH35a: R vertauscht mit iL, iR, Q, B-L, su(3), allen P_s: {comm:.1e}; T und J_B: conj(P_(l,r)) = P_(-l,-r): {swapT:.1e}"
      f" -> {'bestaetigt' if ok_a else 'widerlegt'}")

# H35b
cL = max(abs(L7@D - D@L7).max() for D in su3)
rows = []
for D in su3:
    for i in range(8):
        for j in range(8):
            row = np.zeros(64)       # (K D - D K)[i, j]
            for k in range(8): row[8*i + k] += D[k, j]; row[8*k + j] -= D[i, k]
            rows.append(row)
for i in range(8):
    for j in range(8):
        row = np.zeros(64)           # (K L7 + L7 K)[i, j]
        for k in range(8): row[8*i + k] += L7[k, j]; row[8*k + j] += L7[i, k]
        rows.append(row)
A = np.array(rows)
_, sv, Vt = np.linalg.svd(A)
Ks = [v.reshape(8, 8) for v in Vt[np.sum(sv > 1e-9):]]
perp = [1, 2, 3, 4, 5, 6]
on_perp = max(abs(K[:, perp]).max() for K in Ks) if Ks else 0.0
ok_b = cL < TOL and len(Ks) == 2 and on_perp < TOL
print(f"\nH35b: [L_e7, su(3)] = {cL:.1e}; Loesungsraum K (K D = D K, K L_e7 = -L_e7 K): Dimension {len(Ks)}, max |K auf e7^perp| = {on_perp:.1e}"
      f" -> {'bestaetigt' if ok_b else 'widerlegt'}")

# H35c
c = np.diag([1, -1, -1, -1, -1, -1, -1, -1.])
phi = lambda z: z.real*E[0] + z.imag*E[7]
rng = np.random.default_rng(91); dev = 0
for _ in range(100):
    z = complex(*rng.normal(size=2))
    dev = max(dev, abs(phi(1j*z) - L7@phi(z)).max(), abs(phi(np.conj(z)) - c@phi(z)).max(),
              abs(phi(1j*np.conj(z)) - L7@c@phi(z)).max())
ok_c = dev < TOL
print(f"\nH35c: phi(iz) = L_e7 phi(z), phi(conj z) = c phi(z), phi(i conj z) = L_e7 c phi(z) auf 100 Zufallspunkten: {dev:.1e}"
      f" -> {'bestaetigt' if ok_c else 'widerlegt'}")
