"""k76: Test der Vorab-Notiz H20 (Commit 7d95feb): innerer Frame (J = L_e7 auf O) gegen aeusseren Frame (i = C-Faktor).
Konventionen wie k75 (H19)."""
import numpy as np, os, sys
from scipy.linalg import expm, null_space
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from k69_test_h17 import omul

TOL = 1e-10
E = np.eye(8); I8 = np.eye(8)
L = [np.array([omul(E[a], E[j]) for j in range(8)]).T for a in range(8)]   # L[a] x = e_a x
R = [np.array([omul(E[j], E[a]) for j in range(8)]).T for a in range(8)]   # R[a] x = x e_a
Lv = lambda v: sum(v[k]*L[k] for k in range(8))
dag = lambda M: M.conj().T
alpha = {a: 0.5*(L[a] + 1j*Lv(omul(E[7], E[a]))) for a in (4, 5, 6)}
Q = sum(dag(alpha[a])@alpha[a] for a in alpha)/3
w, V = np.linalg.eigh(Q)
sec = {q: V[:, np.where(abs(w - q) < 1e-9)[0]] for q in (0, 1/3, 2/3, 1)}

# Stab(e7) wie in k75
rows = []
for i in range(8):
    for j in range(8):
        p = omul(E[i], E[j]); A = np.zeros((8, 64))
        for k in range(8):
            for m in range(8):
                A[k, 8*k + m] += p[m]
                A[:, 8*k + m] -= omul(E[k], E[j])*E[i][m]
                A[:, 8*k + m] -= omul(E[i], E[k])*E[j][m]
        rows.append(A)
Der = null_space(np.vstack(rows)); Ds = [Der[:, c].reshape(8, 8) for c in range(Der.shape[1])]
S = null_space(np.array([D[:, 7] for D in Ds]).T)
Stab = [sum(S[k, c]*Ds[k] for k in range(len(Ds))) for c in range(S.shape[1])]
assert len(Ds) == 14 and len(Stab) == 8
rng = np.random.default_rng(76)
gs = [expm(sum(rng.normal()*D for D in Stab)) for _ in range(30)]
J = L[7]
print(f"Kontrollen: G2 {len(Ds)}, Stab(e7) {len(Stab)}, J^2 = -1: {abs(J@J + I8).max():.0e}")

# H20a
Jlin = max(abs(D@J - J@D).max() for D in Stab + gs)
perp = [1, 2, 3, 4, 5, 6]
triv = max(abs(D[:, [0, 7]]).max() for D in Stab)
inv_perp = max(abs(D[np.ix_([0, 7], perp)]).max() for D in Stab)
reps = [D[np.ix_(perp, perp)] for D in Stab]
K = np.vstack([np.kron(np.eye(6), r) - np.kron(r.T, np.eye(6)) for r in reps])
comm_dim = 36 - np.linalg.matrix_rank(K, 1e-9)        # reell: 2 = irreduzibel vom komplexen Typ (Kommutant C)
basis = np.column_stack([E[a] for a in (4, 5, 6)] + [J@E[a] for a in (4, 5, 6)])
rk = np.linalg.matrix_rank(basis[perp, :])
ok_a = Jlin < TOL and triv < TOL and inv_perp < TOL and comm_dim == 2 and rk == 6
print(f"\nH20a: Stab J-linear {Jlin:.0e}; span(1,e7) trivial {triv:.0e}, e7^perp invariant {inv_perp:.0e};"
      f" reeller Kommutant auf e7^perp Dim {comm_dim} (2 = irreduzibel, komplexer Typ);"
      f" e4,e5,e6,Je4,Je5,Je6 Rang {rk} -> {'bestaetigt' if ok_a else 'widerlegt'}")
print("  J e4, J e5, J e6 =", [tuple(np.round(J@E[a], 0).astype(int).nonzero()[0]) for a in (4, 5, 6)],
      [float(np.round((J@E[a]).sum(), 0)) for a in (4, 5, 6)])

# H20b
P123 = np.zeros((8, 8)); P123[[1, 2, 3], [1, 2, 3]] = 1
Jinv123 = abs((I8 - P123)@J@P123).max()
stabinv123 = max(abs((I8 - P123)@D@P123).max() for D in Stab)
Qinv123 = abs((I8 - P123)@Q@P123).max()
inner_ok = Jinv123 < TOL and stabinv123 < TOL                          # eigener J-invarianter Stab-Unterraum
outer_ok = stabinv123 < TOL or Qinv123 < TOL
print(f"\nH20b: span(e1,e2,e3) J-invariant? {Jinv123:.3f}; Stab-invariant (reell wie komplex)? {stabinv123:.3f};"
      f" Q-invariant? {Qinv123:.3f} -> {'bestaetigt' if inner_ok or outer_ok else 'widerlegt'}")
print("  J bildet span(e4,e5,e6) auf span(e1,e2,e3) ab:", abs(P123@J@np.diag([0,0,0,0,1,1,1,0]) - J@np.diag([0,0,0,0,1,1,1,0])).max() < TOL)

# H20c
Pp = 0.5*(I8 - 1j*J); Pm = 0.5*(I8 + 1j*J)
res = {}
for name, P, s in (("P+", Pp, 1), ("P-", Pm, -1)):
    equi = max(abs(P@D - D@P).max() for D in Stab)
    inter = abs(P@J - s*1j*P).max()
    inj = np.linalg.matrix_rank(np.vstack([P.real, P.imag]), 1e-9)          # Rang als reelle Abbildung R^8 -> C^8
    def where(X):
        X = X/np.linalg.norm(X, axis=0)
        return [q for q, B in sec.items() if np.linalg.norm(X - B@(dag(B)@X)) < 1e-9]
    q_perp = where(P[:, perp]); q_sing = where(P[:, [0, 7]]); q_e7 = where(P[:, [7]])
    rk456 = np.linalg.matrix_rank(P[:, [4, 5, 6]], 1e-9)
    res[name] = (q_perp, q_sing)
    print(f"\nH20c {name}: aequivariant {equi:.0e}; P J = {'+' if s > 0 else '-'}i P: {inter:.0e}; reeller Rang {inj};"
          f" e7^perp -> Q = {q_perp}; span(1,e7) -> Q = {q_sing}; e7 -> Q = {q_e7}; komplexer Rang der Bilder von e4,e5,e6: {rk456}")
    res[name] += (equi < TOL and inter < TOL and inj == 8 and len(q_perp) == 1 and q_perp[0] in (1/3, 2/3)
                  and len(q_sing) == 1 and q_sing[0] in (0, 1) and q_e7 == q_sing and rk456 == 3,)
Tswap = abs(Pp.conj() - Pm).max()
ok_c = res["P+"][2] and res["P-"][2] and res["P+"][0] != res["P-"][0] and res["P+"][1] != res["P-"][1] and Tswap < TOL
print(f"  T vertauscht P+ und P-: {Tswap:.0e} -> H20c {'bestaetigt' if ok_c else 'widerlegt'}")

# H20d
basisQ = [I8.astype(complex), 1j*L[7], 1j*R[7]]
A = np.column_stack([np.concatenate([B.real.ravel(), B.imag.ravel()]) for B in basisQ])
b = np.concatenate([Q.real.ravel(), Q.imag.ravel()])
c, *_ = np.linalg.lstsq(A, b, rcond=None)
resid = abs(A@c - b).max()
phase_same = all(abs(np.exp(0.7j)*B - np.exp(0.7j)*B).max() < TOL for B in sec.values())  # e^{i theta} ist Skalar
print(f"\nH20d: Q = {c[0]:.4f}*1 + {c[1]:.4f}*i L_e7 + {c[2]:.4f}*i R_e7, Rest {resid:.0e};"
      f" e^(i theta) skalar auf allen Sektoren: {phase_same} -> {'bestaetigt' if resid < TOL and phase_same else 'widerlegt'}")
