"""k50: Kandidat fuer die Herkunft des C5-Faktors 3/4 (Erkundung, kein Beweis, keine Guard-Aussage).

r94: 3/4 ist deklariert, nicht hergeleitet; eine einzelne Projektion erklaert hoechstens einen Schritt
(idempotent), eine Rekursion braucht in jedem Schritt eine erneuerte Viertel-Identitaet.
Kandidat: "drehen, dann kompensieren" auf dem (E,B)-Dublett (r04): Dualitaetsdrehung R_a, dann C_HC = (1+sx)/2.
"""
import math
import numpy as np
from fractions import Fraction

sx = np.array([[0., 1], [1, 0]]); I2 = np.eye(2)
C = 0.5 * (I2 + sx); A = 0.5 * (I2 - sx)
R = lambda a: np.array([[math.cos(a), -math.sin(a)], [math.sin(a), math.cos(a)]])
u = np.array([1., 1]) / math.sqrt(2)                      # ran C

print("1. C R_a C = cos a C auf ran C")
for a in (0.3, math.pi / 6, math.pi / 2):
    print("   a = %.4f: C R_a C - cos a C = %.1e;  Energie im C-Port %.6f, im A-Port %.6f" %
          (a, np.abs(C @ R(a) @ C - math.cos(a) * C).max(), np.sum((C @ R(a) @ u) ** 2), np.sum((A @ R(a) @ u) ** 2)))

print("\n2. a = pi/6: Ledger-Werte und Detektorstufe")
q = Fraction(3, 4)
print("   cos^2(pi/6) = %.12f = 3/4; abgegebener Anteil sin^2(pi/6) = %.12f = 1/4" % (math.cos(math.pi / 6) ** 2, math.sin(math.pi / 6) ** 2))
print("   Potenzen:", [str(q ** n) for n in range(1, 5)], "(Ledger r04: 3/4, r05: 9/16, r07: 27/64, r08: 81/256)")
n = next(k for k in range(1, 100) if q ** k <= Fraction(1, 256))
print("   erste Stufe mit Phi <= 1/256: n = %d" % n)

print("\n3. drei Schritte zu pi/6 ergeben zusammen die Vierteldrehung Materie -> Tachyon (pi/2)")
v = u.copy()
for k in range(3):
    v = C @ R(math.pi / 6) @ v
print("   nach drei kompensierten Schritten: Energie im C-Port %.6f = 27/64 = %.6f" % (np.sum(v ** 2), 27 / 64))
print("   eine einzige Vierteldrehung, dann kompensieren: C R(pi/2) u = %s (C-Port leer, Inhalt im A-Port)" % np.round(C @ R(math.pi / 2) @ u, 12))
for m in (3, 6, 30, 300):
    print("   Vierteldrehung in %3d kompensierten Schritten: verbleibend %.6f" % (m, math.cos(math.pi / (2 * m)) ** (2 * m)))

print("\n4. Alternative ueber beta: q = 1/(1+beta^2) = cos^2(arctan beta)")
gL = 0.2375 / (math.log(2) / (math.pi * math.sqrt(3)))
bsym = math.tanh(0.5 * math.acosh(gL))
for name, bb in (("Hopf 1/sqrt3", 1 / math.sqrt(3)), ("beta_sym", bsym)):
    qq = 1 / (1 + bb * bb)
    nn = next(k for k in range(1, 200) if qq ** k <= 1 / 256)
    print("   %-12s beta = %.5f: q = %.5f, Stufe n = %d (r94.2-Intervall (0.746879, 0.757858])" % (name, bb, qq, nn))
print("   tan(pi/6) = %.6f = 1/sqrt3 = %.6f" % (math.tan(math.pi / 6), 1 / math.sqrt(3)))

print("\n5. (aufgefallen) Toleranzzeile r05: Verhaeltnis 5/6 = 1/(1 + 1/5) = cos^2(arctan(1/sqrt5)); Winkel %.3f Grad"
      % math.degrees(math.atan(1 / math.sqrt(5))))
