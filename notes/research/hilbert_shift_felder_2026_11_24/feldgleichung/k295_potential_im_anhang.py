"""k295 (Erkundung, nicht blind): Kann das Amplituden-Potential erst bei HS(2) eintreten, und in welcher Form?
Vorgaben: (i) kein Massenterm fuer die Vorstufe (HS(1), psi1 in C), (ii) Rekursion aus k290: der Anhang Delta[psi1, chi]
ist gerade in chi und verschwindet bei chi = 0. Feld psi = psi1 + chi j, A = N(psi1), B = N(chi).
Aufruf: python k295_potential_im_anhang.py > k295_out.txt
"""
import itertools
import sympy as sp

print("== 1  Ein Potential in der vollen Norm kann nicht erst bei HS(2) eintreten ==")
A, B, f, lam = sp.symbols("A B f lambda", positive=True)
V = lam * (A + B - f ** 2) ** 2
print("  V = lambda (N - f^2)^2 mit N = A + B; bei chi = 0:", sp.factor(V.subs(B, 0)), " (nicht null: verletzt Delta[psi,0] = 0 oder setzt das Potential schon bei HS(1) voraus)")
print("  darin steckt fuer die Vorstufe der Massenterm", sp.expand(V).coeff(A, 1).subs(B, 0), "* A (ungleich null)")

print("\n== 2  Welche Terme bis zur vierten Ordnung sind zulaessig? ==")
x = sp.symbols("x0:4", real=True)                      # psi1 = x0 + i x1, chi = x2 + i x3  (psi = psi1 + chi j)
al, be = sp.symbols("alpha beta", real=True)
def act(al, be):
    """links e^{i alpha}: psi1, chi -> e^{i alpha} psi1, e^{i alpha} chi; rechts e^{i beta}: psi1 -> psi1 e^{i beta}, chi -> chi e^{-i beta}"""
    z1 = (x[0] + sp.I * x[1]) * sp.exp(sp.I * (al + be)); z2 = (x[2] + sp.I * x[3]) * sp.exp(sp.I * (al - be))
    return {x[0]: sp.re(sp.expand(z1, complex=True)), x[1]: sp.im(sp.expand(z1, complex=True)),
            x[2]: sp.re(sp.expand(z2, complex=True)), x[3]: sp.im(sp.expand(z2, complex=True))}
mons = [sp.Mul(*[v ** e for v, e in zip(x, ex)]) for d in (2, 4) for ex in itertools.product(range(5), repeat=4)
        if sum(ex) == d and (ex[2] + ex[3]) % 2 == 0 and (ex[2] + ex[3]) > 0]       # gerade in chi, verschwindet bei chi = 0
cs = sp.symbols(f"c0:{len(mons)}")
P = sum(c * m for c, m in zip(cs, mons))
def inv_dim(gens):
    eqs = []
    for g in gens:
        sub = act(*g)
        d = sp.expand(sp.diff(P.subs(sub, simultaneous=True), al if g[0] != 0 else be).subs({al: 0, be: 0}))
        eqs += sp.Poly(d, *x).coeffs()
    sol = sp.solve(eqs, cs, dict=True)[0] if eqs else {}
    free = [c for c in cs if c not in sol]
    return len(free), sp.factor(P.subs(sol))
n2, P2 = inv_dim([(al, 0), (0, be)])
print(f"  Monome (Grad 2 und 4, gerade in chi, null bei chi = 0): {len(mons)}")
print(f"  invariant unter Links- und Rechtsdrehung um i: {n2} Terme")
Av, Bv = x[0] ** 2 + x[1] ** 2, x[2] ** 2 + x[3] ** 2
k0, k1, k2 = sp.symbols("mu2 kappa lambdaB")
print("    sind es B, A*B, B^2 ?", sp.expand(P2 - (k0 * Bv + k1 * Av * Bv + k2 * Bv ** 2)).free_symbols >= set(), "; allgemeine Form:", sp.simplify(P2.subs({x[1]: 0, x[3]: 0})))
n1, P1 = inv_dim([(al, 0)])
print(f"  invariant nur unter der Linksdrehung (Regel psi' = w i psi): {n1} Terme (dazu kommen Real- und Imaginaerteil von (psi1 conj(chi))^2 und B mal dem Rest)")

print("\n== 3  Vakuum von V = lamA A^2 + kappa A B + lamB B^2 + mu2 B  (kein Term mu2_A A: keine Masse der Vorstufe) ==")
lA, lB, ka, mu2 = sp.symbols("lambda_A lambda_B kappa mu2", real=True)
Vg = lA * A ** 2 + ka * A * B + lB * B ** 2 + mu2 * B
sol = sp.solve([sp.diff(Vg, A), sp.diff(Vg, B)], [A, B], dict=True)[0]
print("  stationaer in A und B (beide ungleich null):  A =", sp.factor(sol[A]), ",  B =", sp.factor(sol[B]))
print("    Verhaeltnis A/B =", sp.simplify(sol[A] / sol[B]), " (positiv nur fuer kappa < 0);  Norm f^2 = A + B =", sp.factor(sol[A] + sol[B]))
print("    Wert des Potentials dort:", sp.factor(Vg.subs(sol)))
B0 = sp.solve(sp.diff(Vg.subs(A, 0), B), B)[0]
print("  Rand A = 0:  B =", B0, " (positiv nur fuer mu2 < 0),  V =", sp.factor(Vg.subs({A: 0, B: B0})), ",  dV/dA dort =", sp.factor(sp.diff(Vg, A).subs({A: 0, B: B0})))
print("  Rand B = 0:  V = lamA A^2, Minimum bei A = 0; dV/dB bei A = B = 0:", sp.diff(Vg, B).subs({A: 0, B: 0}), " => chi = 0 ist instabil genau fuer mu2 < 0")

print("\n== 4  Massen der kleinen Schwingungen (Felder psi1 = (a + h1) e^{i..}, chi = (b + h2) e^{i..}) ==")
a, b, h1, h2 = sp.symbols("a b h1 h2", real=True)
Vh = Vg.subs({A: (a + h1) ** 2, B: (b + h2) ** 2})
H = sp.hessian(Vh, (h1, h2)).subs({h1: 0, h2: 0})
Hi = sp.simplify(H.subs({a: sp.sqrt(sol[A]), b: sp.sqrt(sol[B])}))
print("  beide ungleich null: Massenmatrix der Radialmoden hat Determinante", sp.factor(sp.simplify(Hi.det())), "und Spur", sp.factor(sp.simplify(Hi.trace())))
print("    die zwei Phasen sind masselos (V haengt nur von A und B ab)")
print("  Rand A = 0:  m^2(psi1) = 2 dV/dA =", sp.factor(2 * sp.diff(Vg, A).subs({A: 0, B: B0})), " (beide Komponenten von psi1);  m^2(Radialmode von chi) =",
      sp.factor(sp.diff(Vg.subs({A: 0, B: (b + h2) ** 2}), h2, 2).subs(h2, 0).subs(b, sp.sqrt(B0))))
print("    fuer kappa = 0 bleibt psi1 masselos, obwohl chi eine feste Amplitude hat")

print("\n== 5  Die Loesung im Anhang ist am Minimum exakt, mit festen Amplituden ==")
t, xs, k, kp = sp.symbols("t x k kprime", real=True)
p1, p2 = k * (t - xs), kp * (t + xs)
psi1 = [a * sp.cos(p1), a * sp.sin(p1)]; chi = [b * sp.cos(p2), -b * sp.sin(p2)]
dVA, dVB = sp.diff(Vg, A).subs({A: a ** 2, B: b ** 2}), sp.diff(Vg, B).subs({A: a ** 2, B: b ** 2})
r1 = [sp.simplify(sp.diff(c, t, 2) - sp.diff(c, xs, 2) + 2 * dVA * c) for c in psi1]
r2 = [sp.simplify(sp.diff(c, t, 2) - sp.diff(c, xs, 2) + 2 * dVB * c) for c in chi]
print("  Reste der Feldgleichung:", [sp.factor(sp.simplify(r / c)) for r, c in zip(r1 + r2, psi1 + chi)])
print("  => null genau dann, wenn dV/dA = dV/dB = 0: a und b sind durch das Potential festgelegt (in k272 waren sie frei)")

print("\n== 6  Instabilitaet der Loesung ohne Anhang ==")
q, om = sp.symbols("q omega", real=True)
print("  kleines chi auf konstantem Hintergrund A: omega^2 = q^2 + 2 (mu2 + kappa A);  instabil fuer q^2 <", sp.simplify(-2 * (mu2 + ka * A)), " (lange Wellen)")
print("  Vergleich mit dem Potential der vollen Norm aus k294: lamA = lamB = lambda, kappa = 2 lambda, mu2 = -2 lambda f^2, dazu mu2_A = -2 lambda f^2 (verboten)")
