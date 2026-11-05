"""k192b: Nachrechnung zu H77 - homogenes Higgs-Bild unter Lesart B: phi'' = +V'(phi), Ursprung stabil."""
import sympy as sp
t = sp.symbols('t'); mu, lam = sp.symbols('mu lam', positive=True)
p = sp.Function('p')(t); pd = sp.diff(p, t)
V = -mu**2 * p**2 + lam * p**4
for name, L in (('M', sp.Rational(1, 2) * pd**2 - V), ('B', -sp.Rational(1, 2) * pd**2 - V)):
    eom = sp.diff(sp.diff(L, pd), t) - sp.diff(L, p)
    acc = sp.solve(sp.Eq(eom, 0), sp.diff(p, t, 2))[0]
    c0 = sp.diff(acc, p).subs(p, 0)
    print(name, 'pdd =', sp.expand(acc), '| um 0: pdd =', c0, '* p ->', 'stabil' if c0.could_extract_minus_sign() else 'instabil')
