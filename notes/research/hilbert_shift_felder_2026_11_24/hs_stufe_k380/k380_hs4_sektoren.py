"""k380 (Erkundung, nicht blind): Welche Sektoren bietet HS(3) = O und HS(4) = S unter der Farbe, und was legt der Tausch J dort fest?
Aufruf: python k380_hs4_sektoren.py > k380_out.txt"""
import numpy as np
from scipy.linalg import null_space
def conj(x):
    y = -x.copy(); y[0] = x[0]; return y
def mul(x, y):
    n = len(x)
    if n == 1: return x * y
    h = n // 2; a, b, c, d = x[:h], x[h:], y[:h], y[h:]
    return np.concatenate([mul(a, c) - mul(conj(d), b), mul(d, a) + mul(b, conj(c))])

def analyse(n, name):
    e = np.eye(n); C = np.array([[mul(e[i], e[j]) for j in range(n)] for i in range(n)])
    rows = []
    for i in range(n):
        for j in range(n):
            for k in range(n):
                r = np.zeros((n, n)); r[k, :] += C[i, j, :]
                r[:, i] -= C[:, j, k]; r[:, j] -= C[i, :, k]
                rows.append(r.ravel())
    A = np.array(rows); der = null_space(A, rcond=1e-9)
    fix = np.zeros((n, n * n))
    for k in range(n): fix[k, k * n + 7] = 1
    st = null_space(np.vstack([A, fix]), rcond=1e-9)
    gens = [st[:, a].reshape(n, n) for a in range(st.shape[1])]
    inv = null_space(np.vstack(gens), rcond=1e-9)
    supp = sorted(set(int(i) for i in np.argwhere(np.abs(inv) > 1e-9)[:, 0]))
    cas = sum(-g @ g for g in gens); ev = np.round(np.linalg.eigvalsh((cas + cas.T) / 2), 6); vals = sorted(set(ev))
    print(f"== {name} (Dimension {n}), U = e7 ==")
    print(f"   dim Der = {der.shape[1]}; Stabilisator von e7: {st.shape[1]}; farblose Richtungen: Dimension {inv.shape[1]}, Einheiten {supp}")
    print(f"   Casimir: " + ", ".join(f"{v:.4f} x {int((ev == v).sum())}" for v in vals))
    U = e[7]; J = np.array([mul(U, conj(e[i])) for i in range(n)]).T            # Spalte i = J(e_i)
    J2 = J @ J
    plus = [i for i in range(n) if abs(J2[i, i] - 1) < 1e-12]; minus = [i for i in range(n) if abs(J2[i, i] + 1) < 1e-12]
    print(f"   J^2 = +1 auf den Einheiten {plus}; J^2 = -1 auf {minus}; J orthogonal: {np.allclose(J.T @ J, np.eye(n))}")
    print("   J-Bilder: " + "; ".join(f"e{i}->{'+' if J[:, i][np.abs(J[:, i]).argmax()] > 0 else '-'}e{np.abs(J[:, i]).argmax()}" for i in range(n)))
    # invariante quadratische Formen: symmetrische Q mit g^T Q + Q g = 0 (Farbe), optional Konjugation und J
    def count(extra):
        rws = []
        idx = [(i, j) for i in range(n) for j in range(i, n)]
        basis = []
        for (i, j) in idx:
            B = np.zeros((n, n)); B[i, j] = B[j, i] = 1; basis.append(B)
        cons = []
        for g in gens: cons.append(np.array([(g.T @ B + B @ g).ravel() for B in basis]).T)
        for M in extra: cons.append(np.array([(M.T @ B @ M - B).ravel() for B in basis]).T)
        ns = null_space(np.vstack(cons), rcond=1e-9)
        return ns, basis
    Kc = np.diag([1.0] + [-1.0] * (n - 1))
    for lab, ex in (("nur Farbe", []), ("Farbe + Konjugation", [Kc]), ("Farbe + J", [J]), ("Farbe + Konjugation + J", [Kc, J])):
        ns, basis = count(ex)
        print(f"   invariante quadratische Formen ({lab}): {ns.shape[1]}")
    ns, basis = count([Kc, J])
    # welche Bloecke: Diagonalbloecke der invarianten Formen auf Singulett- und Farbraum
    Qs = [sum(ns[k, a] * basis[k] for k in range(len(basis))) for a in range(ns.shape[1])]
    col = [i for i in range(n) if i not in supp]
    diag_s = np.linalg.matrix_rank(np.array([Q[np.ix_(supp, supp)].ravel() for Q in Qs]), tol=1e-9)
    diag_c = np.linalg.matrix_rank(np.array([Q[np.ix_(col, col)].ravel() for Q in Qs]), tol=1e-9)
    mix = np.linalg.matrix_rank(np.array([Q[np.ix_(supp, col)].ravel() for Q in Qs]), tol=1e-9)
    print(f"   davon (Farbe + Konjugation + J): auf den farblosen Richtungen {diag_s}, auf den Farbrichtungen {diag_c}, gemischt {mix}")
    if n == 16:
        c1 = [i for i in col if i < 8]; c2 = [i for i in col if i >= 8]
        r11 = np.linalg.matrix_rank(np.array([Q[np.ix_(c1, c1)].ravel() for Q in Qs]), tol=1e-9)
        r22 = np.linalg.matrix_rank(np.array([Q[np.ix_(c2, c2)].ravel() for Q in Qs]), tol=1e-9)
        r12 = np.linalg.matrix_rank(np.array([Q[np.ix_(c1, c2)].ravel() for Q in Qs]), tol=1e-9)
        print(f"   Farbrichtungen zerfallen in zwei Sechserbloecke (in O: {c1}; in O*l: {c2}); invariante Formen: Block 1: {r11}, Block 2: {r22}, zwischen den Bloecken: {r12}")
        # bildet J die Bloecke auf sich ab?
        print(f"   J bildet Block 1 auf Block 1 ab: {np.allclose(J[np.ix_(c2, c1)], 0)}; Block 2 auf Block 2: {np.allclose(J[np.ix_(c1, c2)], 0)}")
        s1 = [i for i in supp if i < 8]; s2 = [i for i in supp if i >= 8]
        print(f"   farblose Ebenen: {s1} (J^2 = {J2[s1[0], s1[0]]:+.0f}) und {s2} (J^2 = {J2[s2[0], s2[0]]:+.0f})")
        rs = [np.linalg.matrix_rank(np.array([Q[np.ix_(s, s)].ravel() for Q in Qs]), tol=1e-9) for s in (s1, s2)]
        print(f"   invariante Formen auf Ebene {s1}: {rs[0]} (1 heisst: nur die Summe der Quadrate, also Tauschsymmetrie); auf Ebene {s2}: {rs[1]}")
    print()
analyse(8, "HS(3) = O")
analyse(16, "HS(4) = S")
