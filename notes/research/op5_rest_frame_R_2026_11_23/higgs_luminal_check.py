"""Nachtraeglich (nicht in der Methoden-Notiz): obere Bedingung der Kegelgrenze bei luminalem Higgsradius c_h^2 = 1 (W2, r33).
Sympy, exakt. Aufruf: python higgs_luminal_check.py"""
import sympy as s
Z, g, g0, r0, rm, al, ch2 = s.symbols('Z g g0 r0 rm al ch2', real=True)
A = Z - s.Rational(2, 3)*g
b = Z*ch2 + s.Rational(2, 3)*g*(rm - al)
j0s = g0*al**2/2
jms = s.Rational(2, 3)*g*(rm**2 - rm*al + al**2)
upper = A - j0s/(1 - r0) - jms/(1 - rm) - b
u1 = s.simplify(upper.subs(ch2, 1))
print('upper(c_h^2 = 1) =', u1)
split = -s.Rational(2, 3)*g*(1 + rm - al) - j0s/(1 - r0) - jms/(1 - rm)
print('gleich -2g/3 (1 + rm - al) - j0^2/(1 - r0) - jm^2/(1 - rm)?', s.simplify(u1 - split) == 0)
print('jm^2 >= 0 fuer alle rm, al (Diskriminante von rm^2 - rm al + al^2 in al):', s.discriminant(rm**2 - rm*al + al**2, al))
grid = [u1.subs({Z: 1, g: s.Rational(3, 100), g0: s.Rational(3, 100), r0: a, rm: c, al: d})
        for a in (s.Rational(1, 10), s.Rational(1, 2), s.Rational(9, 10)) for c in (s.Rational(1, 10), s.Rational(1, 2), s.Rational(9, 10))
        for d in (0, s.Rational(1, 2), 1)]
print('Stichprobe (27 Punkte, Z = 1, g = g0 = 3/100): groesster Wert von upper =', max(grid), '(negativ heisst verletzt)')
