"""k209 (Erkundung, keine Vorab-Notiz): Fermionen am Urknall-Uebergang unter G2.
Gewichtete symmetrische Dirac-/Weyl-Wirkung c(tau)*L_M (zweite Lesart: T-Bild = -L_M, H79), c von -b (vor) nach a (nach).
Feldgleichung (holomorphe Variation): c (i gamma.d - m) psi + (i/2) c' gamma^0 psi = 0.
Pruefung: psi = c^{-1/2} chi mit chi freie Loesung erfuellt sie exakt; daraus Uebergangsfaktor und keine Mischung.
"""
import sympy as sp

t, x, y, z, m = sp.symbols('t x y z m')
c = sp.Function('c')(t)
chi = sp.Matrix([sp.Function(f'chi{i}')(t, x, y, z) for i in range(4)])
I2, Z2 = sp.eye(2), sp.zeros(2)
sx, sy, sz = sp.Matrix([[0, 1], [1, 0]]), sp.Matrix([[0, -sp.I], [sp.I, 0]]), sp.Matrix([[1, 0], [0, -1]])
g0 = sp.Matrix(sp.BlockMatrix([[Z2, I2], [I2, Z2]]))                       # Weyl-Basis
gs = [sp.Matrix(sp.BlockMatrix([[Z2, s], [-s, Z2]])) for s in (sx, sy, sz)]
X = [t, x, y, z]; G = [g0] + gs


def dirac(v):
    return sum((sp.I*G[mu]*v.diff(X[mu]) for mu in range(4)), sp.zeros(4, 1)) - m*v


psi = chi/sp.sqrt(c)
lhs = c*dirac(psi) + sp.I/2*c.diff(t)*g0*psi
res = sp.simplify(lhs - sp.sqrt(c)*dirac(chi))
print('Rest c(iγ∂-m)ψ + (i/2)c\'γ⁰ψ - c^{1/2}(iγ∂-m)χ =', list(res))           # erwartet: Nullvektor

# Uebergangsfaktor entlang w = b^{1-s} a^s e^{+-i pi (1-s)} (wie H85/H86): (w_vor/w_nach)^{1/2}
a, b = sp.symbols('a b', positive=True)
for sgn in (+1, -1):
    s = sp.symbols('s', real=True)
    w = b**(1 - s)*a**s*sp.exp(sgn*sp.I*sp.pi*(1 - s))
    fac = sp.simplify((w.subs(s, 0)/w.subs(s, 1))**sp.Rational(1, 2))      # stetiger Zweig entlang des Weges
    phase = sp.exp(sgn*sp.I*sp.pi/2)*sp.sqrt(b/a)
    print('Drehsinn', sgn, ': psi_nach/psi_vor = (w_vor/w_nach)^{1/2} =', phase, ' (Hauptzweig-Ausdruck:', fac, ')')
bs = 1/sp.Float('1.8203')
print('Betrag sqrt(b/a) = beta_sym =', sp.N(bs, 6))
