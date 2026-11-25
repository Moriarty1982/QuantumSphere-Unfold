"""k293 (Erkundung, nicht blind): Muss der gegenlaeufige Anteil bei HS(2) in den Anhang wandern?
Vergleich zweier Loesungen der freien Gleichung bei gleichen a, b, k, k', Winkel alpha zwischen den Laufrichtungen:
  S_C: psi = a e^{i p1} + b   e^{-i p2}      (gegenlaeufiger Anteil in C, wie HS(1))
  S_J: psi = a e^{i p1} + b j e^{-i p2}      (gegenlaeufiger Anteil im Anhang)
p1 = k(t - x), p2 = k'(t - x cos(alpha) - y sin(alpha)). Gemittelt ueber beide Phasen.
Energie der Zusatzterme (erste Ordnung in c1, c2): H4 = sum_i K(d_t psi, d_i psi) + sum_{i<j} K(d_i psi, d_j psi).
Aufruf: python k293_anhang_energie.py > k293_out.txt
"""
import itertools
import sympy as sp

a, b, k, kp = sp.symbols("a b k kprime", positive=True)
al, p1, p2 = sp.symbols("alpha p1 p2", real=True)

def qmul(p, q):
    a0, a1, a2, a3 = p; b0, b1, b2, b3 = q
    return [a0 * b0 - a1 * b1 - a2 * b2 - a3 * b3, a0 * b1 + a1 * b0 + a2 * b3 - a3 * b2,
            a0 * b2 - a1 * b3 + a2 * b0 + a3 * b1, a0 * b3 + a1 * b2 - a2 * b1 + a3 * b0]
dot = lambda u, v: sum(x * y for x, y in zip(u, v))
E = lambda s: [sp.cos(s), sp.sin(s), 0, 0]
fields = {
    "S_C": [a * sp.cos(p1) + b * sp.cos(p2), a * sp.sin(p1) - b * sp.sin(p2), 0, 0],
    "S_J": [u + v for u, v in zip([a * c for c in E(p1)], qmul([0, 0, b, 0], E(-p2)))],
}
K1v = (k, -k, 0); K2v = (kp, -kp * sp.cos(al), -kp * sp.sin(al))          # d_mu p1, d_mu p2 fuer mu = t, x, y
avg = lambda e: sp.simplify(sp.integrate(sp.integrate(sp.expand(e), (p1, 0, 2 * sp.pi)), (p2, 0, 2 * sp.pi)) / (4 * sp.pi ** 2))
res = {}
for name, psi in fields.items():
    X = [[K1v[m] * sp.diff(c, p1) + K2v[m] * sp.diff(c, p2) for c in psi] for m in range(3)]
    N = avg(dot(psi, psi)); N2 = avg(dot(psi, psi) ** 2)
    H2 = avg(sp.Rational(1, 2) * sum(dot(x, x) for x in X))
    k1 = k2 = 0
    for m, n in itertools.combinations(range(3), 2):
        k1 += dot(X[m], X[m]) * dot(X[n], X[n]) - dot(X[m], X[n]) ** 2
        cm = [u - v for u, v in zip(qmul(X[m], X[n]), qmul(X[n], X[m]))]
        k2 += dot(cm, cm)
    res[name] = (H2, sp.factor(avg(k1)), sp.factor(avg(k2)), N, sp.factor(N2 - N ** 2))
    print(f"{name}: <N> = {N}, Streuung von N = {res[name][4]}")
    print(f"      freie Energie <H2> = {sp.factor(H2)}")
    print(f"      <H4[K1]> = {res[name][1]}")
    print(f"      <H4[K2]> = {res[name][2]}")
print("\nUnterschied S_J - S_C:")
print("  freie Energie:", sp.simplify(res["S_J"][0] - res["S_C"][0]))
d1 = sp.factor(sp.simplify(res["S_J"][1] - res["S_C"][1])); d2 = sp.factor(sp.simplify(res["S_J"][2] - res["S_C"][2]))
print("  K1:", d1); print("  K2:", d2)
S = sp.factor(sp.simplify(4 - (1 + sp.cos(al)) ** 2))
print("  Winkelfaktor 4 - (1 + cos alpha)^2 =", S, "; bei alpha = 0:", S.subs(al, 0), ", bei alpha = pi:", S.subs(al, sp.pi))
print("  K1-Unterschied / (a^2 b^2 k^2 k'^2 * Winkelfaktor) =", sp.simplify(d1 / (a ** 2 * b ** 2 * k ** 2 * kp ** 2 * (4 - (1 + sp.cos(al)) ** 2))))
print("  K2-Unterschied / (a^2 b^2 k^2 k'^2 * Winkelfaktor) =", sp.simplify(d2 / (a ** 2 * b ** 2 * k ** 2 * kp ** 2 * (4 - (1 + sp.cos(al)) ** 2))))
print("  Verhaeltnis <H4[K1]>(S_J) / <H4[K1]>(S_C) =", sp.simplify(res["S_J"][1] / res["S_C"][1]))
