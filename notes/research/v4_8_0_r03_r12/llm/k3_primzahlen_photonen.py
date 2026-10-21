"""K3: Primzahlen, Zeta und die Sektoren der Sphaera.

 (1) Dilatationsgenerator L0 = -i(x d/dx + 1/2) (Companion Z. 7255 / Riemann-Arbeit):
     Eigenfunktionen x^(-1/2+iE) mit Eigenwert E; L0 erzeugt Translationen in tau = log x.
 (2) Primon-Gas (Julia 1990, Spector 1990), drei Statistiken:
       bosonisch      Z_B(s) = sum_n n^-s              = zeta(s)
       fermionisch    Z_F(s) = sum_{n quadratfrei} n^-s = zeta(s)/zeta(2s)
       (-1)^F-Index   W(s)   = sum_n mu(n) n^-s        = 1/zeta(s)
 (3) Zusammenfuehrung |z^-| = x * l_P (linear, Companion) und tau = log x (Gamma_P = {log p}).
 (4) Torus aus der Hopf-Faserung: Urbild eines Breitenkreises von S^2 ist ein Clifford-Torus in S^3.
"""
import numpy as np
import sympy as sp
import mpmath as mp

print("(1) Dilatationsgenerator")
x, E = sp.symbols('x E', positive=True)
f = x**(-sp.Rational(1, 2) + sp.I*E)
L0f = -sp.I*(x*sp.diff(f, x) + f/2)
print("   L0 x^(-1/2+iE) = E x^(-1/2+iE):", sp.simplify(L0f - E*f) == 0)
tau = sp.symbols('tau', real=True)
g = sp.Function('g')
print("   In tau = log x: L0 = -i(d/dtau + 1/2)  -> Erzeuger der Translation in tau (Takt-Variable)")

print("(2) Primon-Gas, numerisch bis n = 200000")
N = 200000
mu = np.ones(N + 1, dtype=np.int64); mu[0] = 0
is_p = np.ones(N + 1, bool); is_p[:2] = False
for p in range(2, N + 1):
    if is_p[p]:
        is_p[2*p::p] = False
        mu[p::p] *= -1
        mu[p*p::p*p] = 0
n = np.arange(1, N + 1, dtype=float)
m = mu[1:]
for s in (2.0, 3.0):
    ZB = np.sum(n**-s)
    ZF = np.sum((m != 0)*n**-s)
    W = np.sum(m*n**-s)
    z1, z2 = float(mp.zeta(s)), float(mp.zeta(2*s))
    print(f"   s={s:.0f}: Z_B={ZB:.6f} vs zeta={z1:.6f} | Z_F={ZF:.6f} vs zeta(s)/zeta(2s)={z1/z2:.6f}"
          f" | W={W:.6f} vs 1/zeta={1/z1:.6f}")
primes = np.nonzero(is_p)[0]
s = 2.0
euler = np.prod(1/(1 - primes.astype(float)**-s))
print(f"   Euler-Produkt (Bosonen, eine Mode pro Primzahl, Energie log p): {euler:.6f}")
print(f"   Fermionisches Produkt prod(1+p^-s):                            {np.prod(1 + primes.astype(float)**-s):.6f}")

print("(3) Linear vs. logarithmisch")
print("   |z^-|_n = n*l_P ist die multiplikative Koordinate x = n; tau = log n ist die Takt-Koordinate.")
print("   Primitive Stufen p*l_P  <->  Moden-Energien log p: dieselbe Information, zwei Koordinaten.")
gam1 = float(mp.zetazero(1).imag)
for nn in (2, 3, 5, 7):
    print(f"   n={nn}: tau=log n={np.log(nn):.4f}, Phase des ersten Nullstellen-Takts gamma_1*tau mod 2pi = {(gam1*np.log(nn)) % (2*np.pi):.4f}")

print("(4) Clifford-Torus aus der Hopf-Faserung")
rng = np.random.default_rng(3)
th = 1.1                                   # Breitengrad auf S^2
a, b = np.cos(th/2), np.sin(th/2)
ok = True
for _ in range(1000):
    u, v = rng.uniform(0, 2*np.pi, 2)
    psi = np.array([a*np.exp(1j*u), b*np.exp(1j*v)])  # Torus |psi1|=a, |psi2|=b in S^3
    bloch_z = abs(psi[0])**2 - abs(psi[1])**2
    ok &= np.isclose(bloch_z, np.cos(th))
print("   Alle Punkte (a e^iu, b e^iv) liegen ueber dem Breitenkreis cos(theta) =", round(np.cos(th), 6), ":", bool(ok))
print("   Urbild eines Punktes = Kreis (Faser); Urbild eines Breitenkreises = Torus S^1 x S^1;")
print("   Grenzfaelle theta=0, pi: Torus entartet zu einem Kreis (Pole).")
