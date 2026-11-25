"""k294 (Erkundung, nicht blind): Wettbewerb zwischen dem Amplituden-Potential lambda (N - f^2)^2 und den Zusatztermen K1, K2.
Der gegenlaeufige Anteil steht unter dem Winkel theta zwischen C (theta = 0, wie HS(1)) und Anhang (theta = pi/2):
    psi = a e^{i p1} + b (cos(theta) + j sin(theta)) e^{-i p2},   a^2 + b^2 = f^2,
p1 = k(t - x), p2 = k'(t - x cos(alpha) - y sin(alpha)). Mittel ueber beide Phasen, erste Ordnung in lambda, c1, c2.
Aufruf: python k294_schwelle.py > k294_out.txt
"""
import itertools
import sympy as sp

a, b, k, kp, lam, c1, c2 = sp.symbols("a b k kprime lambda c1 c2", positive=True)
al, th, p1, p2, t, x = sp.symbols("alpha theta p1 p2 t x", real=True)

def qmul(p, q):
    a0, a1, a2, a3 = p; b0, b1, b2, b3 = q
    return [a0 * b0 - a1 * b1 - a2 * b2 - a3 * b3, a0 * b1 + a1 * b0 + a2 * b3 - a3 * b2,
            a0 * b2 - a1 * b3 + a2 * b0 + a3 * b1, a0 * b3 + a1 * b2 - a2 * b1 + a3 * b0]
dot = lambda u, v: sum(p * q for p, q in zip(u, v))
E = lambda s: [sp.cos(s), sp.sin(s), 0, 0]
B = [b * sp.cos(th), 0, b * sp.sin(th), 0]
psi = [u + v for u, v in zip([a * c for c in E(p1)], qmul(B, E(-p2)))]
K1v = (k, -k, 0); K2v = (kp, -kp * sp.cos(al), -kp * sp.sin(al))
avg = lambda e: sp.simplify(sp.integrate(sp.integrate(sp.expand(e), (p1, 0, 2 * sp.pi)), (p2, 0, 2 * sp.pi)) / (4 * sp.pi ** 2))
X = [[K1v[m] * sp.diff(c, p1) + K2v[m] * sp.diff(c, p2) for c in psi] for m in range(3)]
N = dot(psi, psi)
varN = sp.factor(avg(N ** 2) - avg(N) ** 2)
h2 = avg(sp.Rational(1, 2) * sum(dot(v, v) for v in X))
k1 = k2 = 0
for m, n in itertools.combinations(range(3), 2):
    k1 += dot(X[m], X[m]) * dot(X[n], X[n]) - dot(X[m], X[n]) ** 2
    cm = [u - v for u, v in zip(qmul(X[m], X[n]), qmul(X[n], X[m]))]
    k2 += dot(cm, cm)
W = 4 - (1 + sp.cos(al)) ** 2
g1 = sp.simplify(avg(k1) / (a ** 2 * b ** 2 * k ** 2 * kp ** 2 * W)); g2 = sp.simplify(avg(k2) / (a ** 2 * b ** 2 * k ** 2 * kp ** 2 * W))
print("== 1  Mittelwerte als Funktion des Winkels theta ==")
print("  <N> =", avg(N), ";  Streuung von N =", varN, " (mit a^2 + b^2 = f^2 ist <V> = lambda * Streuung)")
print("  freie Energie =", sp.factor(h2), " (haengt nicht von theta ab)")
print("  <H4[K1]> / (a^2 b^2 k^2 k'^2 W) = (1 + sin^2 theta)/2 ?", sp.simplify(g1 - (1 + sp.sin(th) ** 2) / 2) == 0,
      ";  <H4[K2]> / (...) =", sp.simplify(sp.trigsimp(g2)))
s = sp.symbols("s", nonnegative=True)                       # s = sin^2(theta)
dE = lam * varN + a ** 2 * b ** 2 * k ** 2 * kp ** 2 * W * (c1 * g1 + c2 * g2)
dEs = sp.expand(sp.simplify(dE.rewrite(sp.cos)).subs(sp.cos(2 * th), 1 - 2 * s).subs(sp.cos(th) ** 2, 1 - s).subs(sp.sin(th) ** 2, s))
dEs = sp.collect(sp.expand(sp.simplify(dEs / (a ** 2 * b ** 2))), s)
print("\n== 2  Energie in s = sin^2(theta), geteilt durch a^2 b^2 ==")
slope = sp.diff(dEs, s)
print("  E(s) ist linear in s; dE/ds haengt nicht von s ab:", sp.simplify(sp.diff(dEs, s, 2)) == 0,
      " => das Minimum liegt immer an einem Ende, s = 0 (in C) oder s = 1 (im Anhang)")
print("  E(0) =", sp.factor(sp.simplify(dEs.subs(s, 0) - (2 * lam + c1 / 2 * k ** 2 * kp ** 2 * W))), "+ 2 lambda + (c1/2) k^2 k'^2 W")
Wc = sp.symbols("Q", nonnegative=True)
print("  Schwelle dE/ds = 0 mit Q = k^2 k'^2 W:  Q =", sp.solve(sp.Eq(-2 * lam + (c1 / 2 + 2 * c2) * Wc, 0), Wc)[0])
print("  Probe: dE/ds - [ -2 lambda + (c1/2 + 2 c2) k^2 k'^2 W ] =", sp.simplify(slope - (-2 * lam + (c1 / 2 + 2 * c2) * k ** 2 * kp ** 2 * W)))

print("\n== 3  Schwelle in Groessen aus k291 ==")
f, mr, r0, ct1, ct2 = sp.symbols("f m_r r0 ctilde1 ctilde2", positive=True)
print("  Radialmode: V = lambda (N - f^2)^2 mit N = (f + h)^2  =>  m_r^2 =", sp.diff(lam * ((f + sp.Symbol('h')) ** 2 - f ** 2) ** 2, sp.Symbol('h'), 2).subs(sp.Symbol('h'), 0))
kc4 = (4 * lam / (c1 + 4 * c2) / 4).subs({lam: mr ** 2 / (8 * f ** 2), c1: ct1 / f ** 4, c2: ct2 / f ** 4})
print("  gleiche Wellenzahl, entgegengesetzte Richtung (W = 4), c = ctilde / f^4 (psi = f U):  k_c^4 =", sp.simplify(kc4))
print("  mit der Knotengroesse r0 = sqrt(ctilde1)/f:  (k_c r0)^4 =", sp.simplify(kc4 * (sp.sqrt(ct1) / f) ** 4), " = (m_r r0)^2 / (8 (1 + 4 c2/c1))")

print("\n== 4  Genauigkeit der beiden Enden in der Gleichung mit Potential (ohne K-Terme): Box psi + 4 lambda (N - f^2) psi ==")
y = sp.symbols("y", real=True)
for name, thv in (("Anhang (theta = pi/2)", sp.pi / 2), ("C (theta = 0)", 0)):
    ps = [c.subs(th, thv).subs({p1: k * (t - x), p2: kp * (t - x * sp.cos(al) - y * sp.sin(al))}) for c in psi]
    Nn = sp.simplify(dot(ps, ps))
    rest = [sp.simplify(sp.diff(c, t, 2) - sp.diff(c, x, 2) - sp.diff(c, y, 2) + 4 * lam * (Nn - a ** 2 - b ** 2) * c) for c in ps]
    print(f"  {name}: N - f^2 = {sp.simplify(Nn - a ** 2 - b ** 2)};  Rest null? {all(r == 0 for r in rest)}")
