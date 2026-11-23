"""Lesart (b): ein Medium unter der Frame-Abbildung J_B (komplexer Boost mit Rapiditaet i pi/2 entlang der M-T-Achse e = x).
Methoden-Notiz Commit 20c34729. Erkundung, nicht blind. Aufruf: python jb_medium.py (keine Daten, keine Pfade)."""
import numpy as np
import sympy as sp

# ---- E1 Algebra ----
eta = sp.diag(1, -1, -1, -1)                       # eta^{mu nu}


def boost(r):
    L = sp.eye(4)
    L[0, 0] = sp.cosh(r); L[1, 1] = sp.cosh(r); L[0, 1] = L[1, 0] = -sp.sinh(r)
    return sp.simplify(L)


JB = boost(sp.I * sp.pi / 2)
Lpi = boost(sp.I * sp.pi)
print('(E1) J_B =', JB.tolist())
print('     J_B eta J_B^T = eta?', sp.simplify(JB * eta * JB.T - eta) == sp.zeros(4))
print('     Eigenwerte und Eigenvektoren:', [(sp.simplify(v), m, [list(x) for x in vs]) for v, m, vs in JB.eigenvects()])
u = sp.Matrix([1, 0, 0, 0])
print('     Bild des reellen zeitartigen Vektors (1,0,0,0):', list(JB * u), '; Norm', sp.simplify((JB * u).T * sp.diag(1, -1, -1, -1) * (JB * u))[0])

# ---- E2 invariante Tensoren ----
S = sp.Matrix(4, 4, lambda i, j: sp.Symbol('s%d%d' % (min(i, j), max(i, j))))
syms = sorted(S.free_symbols, key=str)
inv = sp.solve(list(JB * S * JB.T - S), syms, dict=True)
anti = sp.solve(list(JB * S * JB.T + S), syms, dict=True)
print('(E2) J_B-invariant:', S.subs(inv[0]).tolist())
print('     Vorzeichenwechsel unter J_B:', S.subs(anti[0]).tolist())
Sinv = S.subs(inv[0])
print('     invariant: Geschwindigkeit^2 entlang e = -S^xx/S^tt =', sp.simplify(-Sinv[1, 1] / Sinv[0, 0]))

# ---- E3 Kegelgrenze ----
Z, G0, GM = 1.0, 0.03, 0.03


def cone_max(r, al):
    A = Z - 2 * GM / 3
    b = Z * r + 2 * GM / 3 * (r - al)
    j0 = np.sqrt(G0 * al ** 2 / 2)
    jm = np.sqrt(max(2 * GM / 3 * (r ** 2 - r * al + al ** 2), 0))
    Kh = np.diag([1 / np.sqrt(A), 1, 1])
    V = np.array([[b, j0, jm], [j0, r, 0], [jm, 0, r]])
    return max(np.linalg.eigvalsh(Kh @ V @ Kh))


def speeds2(G, nvec):
    """Wurzeln v von G^{00} v^2 - 2 G^{0i} n_i v + G^{ij} n_i n_j = 0 (k_mu = (w, -k n)); Rueckgabe groesstes |v|^2 und ob reell."""
    G = np.array(G, dtype=complex)
    a2 = G[0, 0]; a1 = -2 * (G[0, 1:] @ nvec); a0 = nvec @ G[1:, 1:] @ nvec
    roots = np.roots([a2, a1, a0])
    real = all(abs(x.imag) < 1e-12 for x in roots) and abs(a2.imag) + abs(a1.imag) + abs(a0.imag) < 1e-12
    return max(abs(x) ** 2 for x in roots), real


def evaluate(G, label):
    thetas = np.linspace(0, np.pi, 41); alphas = np.linspace(0, 1, 21)
    worst, allreal, rs = 0.0, True, []
    for t in thetas:
        for p in (0.0, np.pi / 2):
            n = np.array([np.cos(t), np.sin(t) * np.cos(p), np.sin(t) * np.sin(p)])
            r, real = speeds2(G, n)
            allreal = allreal and real
            rs.append(r)
            worst = max(worst, max(cone_max(r, al) for al in alphas))
    print(f'     {label}: reell {allreal}; r zwischen {min(rs):.4f} und {max(rs):.4f}; groesstes Geschwindigkeitsquadrat {worst:.6f}')


ka = 0.3
lp = sp.Matrix([1, 1, 0, 0]); lm = sp.Matrix([1, -1, 0, 0])
GM_ = eta + ka * (lp * lp.T + lm * lm.T)
GT_ = sp.simplify(JB * GM_ * JB.T)
Gpi = sp.simplify(Lpi * GM_ * Lpi.T)
print('(E3) (i) Medium aus Gegenstroemen entlang e, kappa a = kappa b = 0.3:')
print('     G_M =', GM_.tolist()); print('     J_B-Bild G_T =', GT_.tolist())
evaluate(np.array(GM_.tolist(), dtype=complex), 'M')
evaluate(np.array(GT_.tolist(), dtype=complex), 'T = J_B-Bild')
kt = 0.5
Gtr = eta + sp.diag(0, 0, kt, kt)
print('     (ii) J_B-invariantes Medium, quer zu e verlangsamt (kappa_t = 0.5): invariant?', sp.simplify(JB * Gtr * JB.T - Gtr) == sp.zeros(4))
evaluate(np.array(Gtr.tolist(), dtype=complex), 'M = T')
print('(E4) Kontrolle, Tachyonbild der Wirkung (Rapiditaet i pi, H79): Lpi =', Lpi.tolist())
print('     Bild des Gegenstrom-Mediums gleich G_M?', sp.simplify(Gpi - GM_) == sp.zeros(4))
evaluate(np.array(Gpi.tolist(), dtype=complex), 'Bild unter i pi')
