#!/usr/bin/env python3
"""k302: Test H133. Kopplung des HS(3)-Anhangs an die Vorstufe.

Vorab-Notiz: notes/research/predictions/Vorab_Notiz_H133_Anhang_HS3_Kopplung.md
Werkzeug: Python (numpy fuer Lie-Algebren und Invarianten, sympy fuer den Fluss,
scipy fuer die Integration). Gegenprobe: k302b_gegenprobe.wl.
Aufruf: python3 k302_test_h133.py > k302_out.txt
"""
import itertools
import numpy as np
import sympy as sp
from scipy.integrate import solve_ivp

np.set_printoptions(precision=4, suppress=True)


# ---------- Oktonionen nach Cayley-Dickson ----------
def qmul(p, q):
    a0, a1, a2, a3 = p
    b0, b1, b2, b3 = q
    return np.array([a0*b0 - a1*b1 - a2*b2 - a3*b3,
                     a0*b1 + a1*b0 + a2*b3 - a3*b2,
                     a0*b2 - a1*b3 + a2*b0 + a3*b1,
                     a0*b3 + a1*b2 - a2*b1 + a3*b0])


def qconj(p):
    return np.array([p[0], -p[1], -p[2], -p[3]])


def omul(x, y):
    """(a,b)(c,d) = (ac - conj(d) b, d a + b conj(c))."""
    a, b, c, d = x[:4], x[4:], y[:4], y[4:]
    return np.concatenate([qmul(a, c) - qmul(qconj(d), b),
                           qmul(d, a) + qmul(b, qconj(c))])


E = np.eye(8)


def Lmat(u):
    return np.array([omul(u, E[k]) for k in range(8)]).T


def Rmat(u):
    return np.array([omul(E[k], u) for k in range(8)]).T


def rank(mats, tol=1e-9):
    if len(mats) == 0:
        return 0
    return np.linalg.matrix_rank(np.array([m.ravel() for m in mats]), tol=tol)


def basis(mats, tol=1e-9):
    """Orthonormale Basis des Spanns (als Liste von Matrizen)."""
    V = np.array([m.ravel() for m in mats])
    u, s, vt = np.linalg.svd(V, full_matrices=False)
    return [vt[k].reshape(8, 8) for k in range(len(s)) if s[k] > tol]


def lie_closure(gens):
    B = basis(gens)
    while True:
        new = B + [x @ y - y @ x for x in B for y in B]
        B2 = basis(new)
        if len(B2) == len(B):
            return B2
        B = B2


# ---------- invariante Polynome ----------
def monomials(n, d):
    return [e for e in itertools.product(range(d + 1), repeat=n) if sum(e) == d]


def invariant_space(gens, d, n=8):
    mons = monomials(n, d)
    idx = {e: k for k, e in enumerate(mons)}
    rows = []
    for X in gens:
        D = np.zeros((len(mons), len(mons)))
        # (X x)_i d/dx_i ; (Xx)_i = sum_j X_ij x_j
        for e in mons:
            for i in range(n):
                if e[i] == 0:
                    continue
                for j in range(n):
                    if abs(X[i, j]) < 1e-12:
                        continue
                    f = list(e)
                    f[i] -= 1
                    f[j] += 1
                    D[idx[tuple(f)], idx[e]] += X[i, j] * e[i]
        rows.append(D)
    Mbig = np.vstack(rows)
    u, s, vt = np.linalg.svd(Mbig)
    null = vt[np.sum(s > 1e-8):]
    return mons, null


def poly_vec(mons, expr, xs):
    p = sp.Poly(sp.expand(expr), *xs)
    v = np.zeros(len(mons))
    idx = {e: k for k, e in enumerate(mons)}
    for e, c in p.terms():
        v[idx[e]] = float(c)
    return v


def in_span(null, v):
    r = v - null.T @ (null @ v)
    return np.linalg.norm(r) < 1e-8


def commutant_dim(gens, block):
    """Dimension des reellen Kommutanten der Wirkung auf einem Block."""
    k = len(block)
    rows = []
    for X in gens:
        Xb = X[np.ix_(block, block)]
        rows.append(np.kron(Xb, np.eye(k)) - np.kron(np.eye(k), Xb.T))
    s = np.linalg.svd(np.vstack(rows), compute_uv=False)
    return int(np.sum(s < 1e-8))


xs = sp.symbols('x0:8')
A4 = sum(x**2 for x in xs[:4])
C4 = sum(x**2 for x in xs[4:])

print("=== Teil 1: Lesart S-a, Links-ℍ und Rechts-i auf 𝕆 ===")
Li, Lj, Lk = Lmat(E[1]), Lmat(E[2]), Lmat(E[3])
Ri = Rmat(E[1])
# Kontrolle der offengelegten Formeln
p = np.array([0.3, -0.5, 0.7, 0.2]); a = np.array([1.1, 0.4, -0.3, 0.9]); b = np.array([-0.2, 0.6, 0.5, -1.0])
lhs = omul(np.concatenate([p, np.zeros(4)]), np.concatenate([a, b]))
print("p(a+bl) = pa + (bp)l:", np.allclose(lhs, np.concatenate([qmul(p, a), qmul(b, p)])))
rhs = omul(np.concatenate([a, b]), np.concatenate([p, np.zeros(4)]))
print("(a+bl)q = aq + (b conj q)l:", np.allclose(rhs, np.concatenate([qmul(a, p), qmul(b, qconj(p))])))
print("[L_i, L_j] = 2 L_k auf 𝕆?", np.allclose(Li @ Lj - Lj @ Li, 2 * Lk))
print("[L_i, L_j] = 2 L_k auf dem Block a?", np.allclose((Li @ Lj - Lj @ Li)[:4, :4], 2 * Lk[:4, :4]))
print("[L_i, L_j] = -2 L_k auf dem Block b?", np.allclose((Li @ Lj - Lj @ Li)[4:, 4:], -2 * Lk[4:, 4:]))
print("[L_j, R_i] = 0 auf 𝕆?", np.allclose(Lj @ Ri - Ri @ Lj, 0), " auf Block a?", np.allclose((Lj @ Ri - Ri @ Lj)[:4, :4], 0))
print("Dimension Spann(L_i, L_j, L_k):", rank([Li, Lj, Lk]), " Abschluss nur der L:", len(lie_closure([Li, Lj, Lk])))
gSa = lie_closure([Li, Lj, Lk, Ri])
print("Dimension der erzeugten Lie-Algebra (L_i, L_j, L_k, R_i):", len(gSa))
blockdiag = all(np.allclose(X[:4, 4:], 0) and np.allclose(X[4:, :4], 0) for X in gSa)
print("blockdiagonal in (a, b):", blockdiag)
print("Rang der Einschraenkung auf a:", rank([np.pad(X[:4, :4], ((0, 4), (0, 4))) for X in gSa]),
      " auf b:", rank([np.pad(X[4:, 4:], ((0, 4), (0, 4))) for X in gSa]))
purely_b = basis([X for X in lie_closure([Li, Lj, Lk, Ri])])
# Teilalgebra, die auf a trivial ist
V = np.array([X[:4, :4].ravel() for X in gSa])
u, s, vt = np.linalg.svd(V.T)
kern = len(gSa) - int(np.sum(s > 1e-9))
print("Dimension der Teilalgebra, die nur auf b wirkt:", kern)
for d in (2, 4):
    mons, null = invariant_space(gSa, d)
    print(f"Invarianten vom Grad {d}:", null.shape[0])
    if d == 2:
        print("  A, C im Raum:", in_span(null, poly_vec(mons, A4, xs)), in_span(null, poly_vec(mons, C4, xs)))
    else:
        print("  A², AC, C² im Raum:", [in_span(null, poly_vec(mons, q, xs)) for q in (A4**2, A4 * C4, C4**2)])
print("Kommutant auf Block b (1 reell, 2 komplex, 4 quaternionisch):", commutant_dim(gSa, [4, 5, 6, 7]))
print("Kommutant auf Block a:", commutant_dim(gSa, [0, 1, 2, 3]))

print()
print("=== Teil 2: Lesarten S-b (g2) und S-c (su(3), u = i) ===")
# Derivationen: D(xy) = D(x) y + x D(y)
rows = []
for i in range(8):
    for j in range(8):
        prod = omul(E[i], E[j])
        for comp in range(8):
            row = np.zeros((8, 8))
            # (D(e_i e_j))_comp = sum_m D[comp, m] prod[m]
            row[comp, :] += prod
            # (D(e_i) e_j)_comp = sum_m D[m, i] (e_m e_j)_comp
            for m in range(8):
                row[m, i] -= omul(E[m], E[j])[comp]
                row[m, j] -= omul(E[i], E[m])[comp]
            rows.append(row.ravel())
u, s, vt = np.linalg.svd(np.array(rows))
g2 = [v.reshape(8, 8) for v in vt[np.sum(s > 1e-8):]]
print("Dimension Der(𝕆):", len(g2), " alle antisymmetrisch:", all(np.allclose(X, -X.T) for X in g2))
# Stabilisator von e1
Vst = np.array([X[:, 1] for X in g2])
u, s, vt = np.linalg.svd(Vst.T)
coef = vt[np.sum(s > 1e-8):]
su3 = [sum(c[k] * g2[k] for k in range(len(g2))) for c in coef]
print("Dimension des Stabilisators von i:", len(su3))
N7 = sum(x**2 for x in xs[1:])
T6 = sum(x**2 for x in xs[2:])
for name, g, blocks in (("S-b g2", g2, [[0], list(range(1, 8))]), ("S-c su(3)", su3, [[0], [1], list(range(2, 8))])):
    for d in (2, 4):
        mons, null = invariant_space(g, d)
        print(f"{name}: Invarianten vom Grad {d}:", null.shape[0])
    print(f"{name}: Kommutant auf dem grossen Block:", commutant_dim(g, blocks[-1]))
mons, null = invariant_space(g2, 4)
print("S-b: x0²·N(Im) invariant:", in_span(null, poly_vec(mons, xs[0]**2 * N7, xs)))
mons, null = invariant_space(su3, 4)
print("S-c: x0²·T invariant:", in_span(null, poly_vec(mons, xs[0]**2 * T6, xs)),
      " A·C (4+4) invariant:", in_span(null, poly_vec(mons, A4 * C4, xs)))
mons, null = invariant_space(gSa, 4)
print("S-a: x0²·T (2+6) invariant:", in_span(null, poly_vec(mons, xs[0]**2 * T6, xs)))
# vertragen sich S-a und S-c?
both = lie_closure(gSa + su3)
print("Dimension der von S-a und S-c zusammen erzeugten Algebra:", len(both), "(so(8) hat 28, so(7) 21)")
mons, null = invariant_space(both, 4)
print("  gemeinsame Invarianten Grad 4:", null.shape[0])

print()
print("=== Teil 3: noetige Massen und Kopplungen ===")
mW, mZ, mt, mh, v = 80.37, 91.19, 172.6, 125.2, 246.22   # GeV, aus dem Gedaechtnis wie k300
fehl = mh**2 * 8 * np.pi**2 * v**2 - 6 * mW**4 - 3 * mZ**4 + 12 * mt**4
print(f"fehlende Bosonen-Summe: {fehl:.4e} GeV^4")
need = {}
for name, n in (("S-a", 4), ("S-c", 6), ("S-b", 7)):
    m = (fehl / n) ** 0.25
    kap = m**2 / (2 * v**2)
    need[name] = (n, m, kap)
    print(f"{name}: n = {n}, m = {m:.1f} GeV, kappa = m²/(2v²) = {kap:.4f}  (Fenster ±20 % der Summe: m von {(0.8*fehl/n)**0.25:.1f} bis {(1.2*fehl/n)**0.25:.1f} GeV)")
print("Regel R1 (volle Norm, kappa = 2·lambda_A): neue Felder sind Goldstone-Richtungen, m = 0, Summe 0.")
mu = 0.3018
print(f"Regel R2 (HC-Strafe eta(C - mu²A)², mu = {mu}): kappa = -2·eta·mu² = {-2*mu**2:.4f}·eta, negativ, eta frei.")

print()
print("=== Teil 4: Fluss mit einer Schleife, V = lA·A² + k·A·C + lC·C² ===")
lA, kp, lC = sp.symbols('lambda_A kappa lambda_C', real=True)


def betas(N, M):
    x = sp.symbols(f'x0:{N}', real=True)
    y = sp.symbols(f'y0:{M}', real=True)
    A = sum(t**2 for t in x)
    C = sum(t**2 for t in y)
    Vp = lA * A**2 + kp * A * C + lC * C**2
    var = list(x) + list(y)
    H = sp.hessian(Vp, var)
    tr = sp.expand(sum(H[i, j]**2 for i in range(N + M) for j in range(N + M)) / 2)
    bA, bK, bC = sp.symbols('bA bK bC')
    rest = sp.Poly(sp.expand(tr - bA * A**2 - bK * A * C - bC * C**2), *var)
    sol = sp.solve(rest.coeffs(), [bA, bK, bC], dict=True)[0]
    check = sp.expand(tr - (sol[bA] * A**2 + sol[bK] * A * C + sol[bC] * C**2))
    return sp.factor(sol[bA]), sp.factor(sol[bK]), sp.factor(sol[bC]), check


flows = {}
for (N, M) in ((2, 2), (4, 4), (2, 6), (1, 7)):
    bA_, bK_, bC_, chk = betas(N, M)
    flows[(N, M)] = (bA_, bK_, bC_)
    print(f"(N, M) = ({N}, {M}): 16π² dlA/dt = {bA_};  16π² dk/dt = {bK_};  16π² dlC/dt = {bC_};  Nullrest: {chk}")
print("Kontrolle (2, 2) gegen H129: 4(k² + 20 lA²) und 16k(k + 2lA + 2lC).")

print()
print("--- feste Strahlen (R3): beta_k·lA = k·beta_A und beta_k·lC = k·beta_C, lA = 1 ---")
for (N, M) in ((4, 4), (2, 6), (1, 7)):
    bA_, bK_, bC_ = flows[(N, M)]
    # kappa = 0 (entkoppelt) getrennt; hier kappa != 0
    e1 = sp.expand(sp.cancel((bK_ * lA - kp * bA_).subs(lA, 1) / kp))
    e2 = sp.expand(sp.cancel((bK_ * lC - kp * bC_).subs(lA, 1) / kp))
    sols = sp.solve([e1, e2], [kp, lC], dict=True)
    out = []
    for s_ in sols:
        kv, cv = complex(sp.N(s_[kp])), complex(sp.N(s_[lC]))
        if abs(kv.imag) < 1e-12 and abs(cv.imag) < 1e-12:
            out.append((sp.simplify(s_[kp]), sp.simplify(s_[lC]), kv.real, cv.real))
    print(f"({N}, {M}): reelle Loesungen (kappa/lA, lC/lA):", [(str(o[0]), str(o[1])) for o in out])
    print("        Zahlen:", [(round(o[2], 4), round(o[3], 4)) for o in out])
print("Der Punkt (2, 1) ist die volle Norm (A + C)². Skalenfrei verlangt lA = 0 an der Skala; ein festes Verhaeltnis kappa/lA")
print("legt dort keinen Wert von kappa fest.")

print()
print("--- Pol der Kopplungen, Start mu = v, lA = 0 ---")


def pole(N, M, k0, c0, tmax=200.0):
    bA_, bK_, bC_ = flows[(N, M)]
    f = sp.lambdify((lA, kp, lC), [bA_, bK_, bC_], 'numpy')

    def rhs(t, g):
        return np.array(f(*g), dtype=float) / (16 * np.pi**2)

    def ev(t, g):
        return np.max(np.abs(g)) - 4 * np.pi
    ev.terminal = True
    sol = solve_ivp(rhs, (0, tmax), [0.0, k0, c0], events=ev, rtol=1e-9, atol=1e-11, max_step=0.05)
    if sol.t_events[0].size:
        t = sol.t_events[0][0]
        return t, v * np.exp(t), sol.y_events[0][0]
    return None, None, sol.y[:, -1]


for name, (N, M) in (("S-a", (4, 4)), ("S-c", (2, 6)), ("S-b", (1, 7))):
    n, m, kap = need[name]
    for c0 in (0.0, 0.5, 1.0):
        t, mu_p, g = pole(N, M, kap, c0)
        print(f"{name} ({N},{M}), kappa(v) = {kap:.3f}, lC(v) = {c0}: t = {t:.3f}, Pol bei {mu_p:.3e} GeV, Kopplungen dort {np.round(g, 2)}")
# Empfindlichkeit: halbe/doppelte Kopplung
for fac in (0.5, 2.0):
    t, mu_p, g = pole(4, 4, need['S-a'][2] * fac, 0.0)
    print(f"S-a mit kappa·{fac}: Pol bei {mu_p:.3e} GeV")
# erste Schritte: wann ueberschreitet eine Kopplung 1 bzw. pi
bA_, bK_, bC_ = flows[(4, 4)]
k0 = need['S-a'][2]
print("S-a: Anfangssteigungen je e-Faltung (durch 16π²):",
      [float(b.subs({lA: 0, kp: k0, lC: 0})) / (16 * np.pi**2) for b in (bA_, bK_, bC_)])

print()
print("=== Urteil nach den Kriterien der Vorab-Notiz ===")
print("K-a, K-b, K-c: siehe Ergebnis-Notiz; die Zahlen oben entscheiden.")
