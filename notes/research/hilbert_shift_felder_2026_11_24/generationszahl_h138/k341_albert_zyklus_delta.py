"""k341 (H158): Offene Zellen der Traeger-Tabelle fuer die Albert-Algebra: Zyklus, magischer Winkel, K = 2/3, delta.
Aufruf: python3 k341_albert_zyklus_delta.py
"""
import itertools
import numpy as np
import sympy as sp
from scipy.optimize import brentq

print("== H158a: Zirkulante, Zyklus, magischer Winkel ==")
a, s, v, c = sp.symbols('a s v c', real=True)
b = s + sp.I * v
S = sp.Matrix([[0, 1, 0], [0, 0, 1], [1, 0, 0]])
W = a * sp.eye(3) + b * S + sp.conjugate(b) * S.T
P = S  # Platztausch
print("P W P^-1 - W =", sp.simplify(P * W * P.T - W).is_zero_matrix)
r_, d_ = sp.symbols('r delta', real=True)
Wp = W.subs({s: r_ * sp.cos(d_), v: r_ * sp.sin(d_)})
lam = [a + 2 * r_ * sp.cos(d_ + 2 * sp.pi * k / 3) for k in range(3)]
x = sp.symbols('x')
cp = sp.expand((Wp - x * sp.eye(3)).det())
res = [sp.simplify(sp.expand_trig(cp.subs(x, l))) for l in lam]
print("charakteristisches Polynom an a + 2r cos(delta + 2 pi k/3):", res)
print("Tr W =", sp.simplify(W.trace()), "; Tr W^2 =", sp.simplify((W * W).trace()), "; det W =", sp.simplify(sp.expand(W.det())))
print("det W in (a, r, delta) - (a^3 - 3 a r^2 + 2 r^3 cos 3delta) =",
      sp.simplify(sp.expand_trig(sp.expand(Wp.det()) - (a**3 - 3 * a * r_**2 + 2 * r_**3 * sp.cos(3 * d_)))))
print("magischer Winkel: (1,1,1)/sqrt3 gegen Platzachse: cos =", sp.sqrt(3) / 3, "-> Winkel", float(sp.acos(1 / sp.sqrt(3)) * 180 / sp.pi), "Grad")
w3 = sp.exp(2 * sp.pi * sp.I / 3)
for k in range(3):
    f = sp.Matrix([1, w3**k, w3**(2 * k)]) / sp.sqrt(3)
    print(f"  Fourier-Vektor k={k}: P f = omega^{k} f:", sp.simplify(P * f - w3**k * f).is_zero_matrix,
          "; W f = lambda f mit lambda =", sp.simplify(sp.expand_complex((W * f)[0] / f[0])))

# Oktonionen (Cayley-Dickson) und Albert-Invarianten fuer x1 = x2 = x3 = x
def cd_mul(p, q):
    n = len(p)
    if n == 1:
        return p * q
    h = n // 2
    a1, b1, c1, d1 = p[:h], p[h:], q[:h], q[h:]
    conj = lambda z: np.concatenate([z[:1], -z[1:]])
    return np.concatenate([cd_mul(a1, c1) - cd_mul(conj(d1), b1), cd_mul(d1, a1) + cd_mul(b1, conj(c1))])

rng = np.random.default_rng(341)
maxerr = 0.0
for _ in range(20):
    xo = rng.normal(size=8)
    dd = rng.normal(size=3)
    n2 = xo @ xo
    # Albert: Tr = sum d, Tr W^2 = sum d^2 + 2 sum |x|^2, det = d1 d2 d3 - sum d_k |x_k|^2 + 2 Re((x1 x2) x3)
    tr = dd.sum(); tr2 = (dd**2).sum() + 6 * n2
    det = dd.prod() - dd.sum() * n2 + 2 * cd_mul(cd_mul(xo, xo), xo)[0]
    bc = xo[0] + 1j * np.linalg.norm(xo[1:])
    M = np.diag(dd).astype(complex) + bc * np.array(S).astype(float) + np.conj(bc) * np.array(S.T).astype(float)
    ev = np.linalg.eigvalsh(M)
    maxerr = max(maxerr, abs(tr - ev.sum()), abs(tr2 - (ev**2).sum()), abs(det - ev.prod()))
print(f"H3(O) mit x1=x2=x3=x, 20 Zufallsproben: max Abweichung (Tr, Tr W^2, det) gegen H3(C_x) = {maxerr:.2e}")

print("\n== H158b: K = 2/3 ==")
K = (3 * a**2 + 6 * r_**2) / (3 * a)**2
print("K = Tr W^2/(Tr W)^2 =", sp.simplify(K), "; K - 2/3 = 0 <=>", sp.solve(sp.Eq(K, sp.Rational(2, 3)), r_), "(r^2 = a^2/2)")
print("Norm Spuranteil 3a^2, Norm Nebendiagonale 6 r^2: gleich <=> r^2 = a^2/2: Rest", sp.simplify((3 * a**2 - 6 * r_**2).subs(r_, a / sp.sqrt(2))))

print("\n== H158c: A4-invariante, J-erlaubte Terme auf dem Zirkulantensektor bis Ordnung 8 ==")
# Monome phi^a prod b_k^p_k conj(b_k)^q_k; V4: m_k = p_k + q_k alle gleiche Paritaet. Einschraenkung: r^m e^{i(p-q)delta}.
def allowed_mn(maxm):
    out = set()
    for m in range(0, maxm + 1):
        for parts in itertools.product(range(m + 1), repeat=3):
            if sum(parts) != m or len({p % 2 for p in parts}) != 1:
                continue
            for pk in itertools.product(*[range(mk + 1) for mk in parts]):
                p = sum(pk); q = m - p
                out.add((m, abs(p - q)))
    return out
MN = allowed_mn(8)
print("erlaubte (m, n) ohne J:", sorted(MN))
for D in range(0, 9):
    terms = []
    for aa in range(0, D + 1):
        m = D - aa
        for n in range(0, m + 1):
            if (m, n) not in MN:
                continue
            # J-Partner (m, aa, n) muss existieren: phi^m r^aa cos n delta
            if (aa, n) in MN:
                if aa <= m:
                    terms.append((aa, m, n))
    harm = sorted({n for (_, _, n) in terms})
    dep = [t for t in terms if t[2] > 0]
    print(f"Ordnung {D}: J-erlaubte Klassen (a, m, n) mit a<=m: {terms}; Harmonische n: {harm}")
print("(je Klasse n > 0: cos n delta, und sin n delta nur ohne sigma-Symmetrie)")

print("\n== H158e: Ladungsmischung c ==")
wk = (1 + sp.I * c) * (s + sp.I * v)
k282 = (1 - c**2) * (s**2 - v**2) - 4 * c * s * v
print("Re(w^2) - [(1-c^2)(s^2-v^2) - 4 c s v] =", sp.simplify(sp.re(sp.expand(wk**2)) - k282))
print("arg w = arctan c + atan2(v, s); |w|^2 =", sp.simplify(sp.expand(wk * sp.conjugate(wk))))

print("\n== H158d: Kandidatensuche (sigma als Symmetrie, Lambda = v, K = 2/3) ==")
me, mmu, mtau, dtau = 0.51099895, 105.6583755, 1776.93, 0.09
def delta_exp(mt):
    rt = np.sqrt(np.array([me, mmu, mt])); rt = rt / rt.sum() * 3  # sum lambda = 3
    # lambda_k = 1 + sqrt2 cos(delta + 2 pi k/3) (K=2/3 angenommen): kleinste Wurzel -> delta
    f = lambda d: (1 + np.sqrt(2) * np.cos(d + 2 * np.pi / 3)) - rt[0]
    return brentq(f, 0.0, np.pi / 12 * 3)
d0 = delta_exp(mtau); sig = abs(delta_exp(mtau + dtau) - delta_exp(mtau - dtau)) / 2
print(f"delta_exp (aus m_e/Summe der Wurzeln, K = 2/3 angenommen) = {d0:.7f} +- {sig:.1e}; 2/9 = {2/9:.7f}; Abstand {(d0 - 2/9)/sig:+.2f} sigma")
a2, b2 = 1 / 6, 1 / 12
A4c = 9 * a2 * 6 * b2                       # I4 = A4c cos 2delta
A6c = 27 * a2**1.5 * 2 * b2**1.5            # I6 = A6c cos 3delta (+ delta-unabhaengig)
A6p = 27 * a2**1.5 * 3 * b2**1.5            # I6' = A6p cos delta
print(f"I4 = {A4c:.6f} cos 2d; I6 = {A6c:.6f} cos 3d; I6' = {A6p:.6f} cos d")
grid = np.linspace(0, 2 * np.pi, 200001)
def fold(d):
    d = d % (2 * np.pi / 3)
    return min(d, 2 * np.pi / 3 - d)
ws = {'1': 1.0, 'sqrt2': np.sqrt(2), 'sqrt3': np.sqrt(3), '1/sqrt2': 1 / np.sqrt(2), '1/sqrt3': 1 / np.sqrt(3)}
for name, Ac, n in (("I6 (cos 3d)", A6c, 3), ("I6' (cos d)", A6p, 1)):
    need = []
    # noetiges beta/alpha: stationaer und Minimum bei delta = d0 (alle aequivalenten Zweige)
    hits = 0; distinct = set(); best = (9, None)
    for sgn in (1, -1):
        for p in range(1, 7):
            for q in range(1, 7):
                for wn, wv in ws.items():
                    for sg2 in (1, -1):
                        ratio = sg2 * p / q * wv
                        V = sgn * (A4c * np.cos(2 * grid) + ratio * Ac * np.cos(n * grid))
                        i = np.argmin(V)
                        # Verfeinerung
                        dd = grid[i]
                        for _ in range(30):
                            g = sgn * (-2 * A4c * np.sin(2 * dd) - n * ratio * Ac * np.sin(n * dd))
                            h = sgn * (-4 * A4c * np.cos(2 * dd) - n * n * ratio * Ac * np.cos(n * dd))
                            if h == 0: break
                            dd -= g / h
                        df = fold(dd)
                        distinct.add(round(df, 9))
                        if abs(df - d0) < 3 * sig:
                            hits += 1
                        if abs(df - d0) < best[0]:
                            best = (abs(df - d0), (sgn, ratio, wn, p, q, df))
    inner = [d for d in distinct if 1e-6 < d < np.pi / 3 - 1e-6]
    print(f"{name}: Kandidaten 2*2*36*5 = 720, verschiedene Minima {len(distinct)} (davon innen {len(inner)}), Treffer (3 sigma) {hits}, "
          f"Zufallserwartung {len(inner) * 6 * sig / (np.pi / 3):.4f}")
    print(f"   naechster Kandidat: Vorzeichen alpha {best[1][0]:+d}, beta/alpha = {best[1][1]:+.6f} ({best[1][3]}/{best[1][4]} * {best[1][2]}), "
          f"delta = {best[1][5]:.6f}, Abstand {best[0]/sig:.0f} sigma")
    # noetiges Verhaeltnis fuer delta = d0 auf allen aequivalenten Zweigen
    for br in [d0, -d0, d0 + 2 * np.pi / 3, -d0 + 2 * np.pi / 3, d0 + 4 * np.pi / 3, -d0 + 4 * np.pi / 3]:
        if abs(np.sin(n * br)) < 1e-12: continue
        rat = -2 * A4c * np.sin(2 * br) / (n * Ac * np.sin(n * br))
        # Minimum? fuer welches Vorzeichen von alpha, und global?
        for sgn in (1, -1):
            V = sgn * (A4c * np.cos(2 * grid) + rat * Ac * np.cos(n * grid))
            if abs(fold(grid[np.argmin(V)]) - d0) < 1e-4 and abs((grid[np.argmin(V)] - br + np.pi) % (2 * np.pi) - np.pi) < 1e-3:
                need.append((br, sgn, rat))
    for br, sgn, rat in need:
        print(f"   noetig: Zweig delta = {br:+.6f}, Vorzeichen alpha {sgn:+d}, beta/alpha = {rat:+.6f}")
