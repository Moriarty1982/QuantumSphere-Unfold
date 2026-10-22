"""k47: H15 zusammen mit prop:H0-tension (Drift von beta_sym); Erkundung E10, kein Test.

1. Zwei Lesarten der Drift: symmetrisch (gamma_L = cosh 2 eta(t)) oder nur Materie-Frame (cosh(eta_+(t) + eta_s)).
2. Folge fuer cot theta_W = gamma_L zur Zeit der Hintergrundstrahlung.
3. H0-Faktor 1,083 je Lesart und Exponent (der Exponent steht nicht in der Quelle).
4. Grobe Abschaetzung der BBN-Wirkung bei festem alpha und v: G_F ~ (1/sqrt2 v^2)(1 + Delta alpha - 3 c^2/(32 pi^2 s^2))
   (Yang/Rafelski, arXiv:2603.02652, Gl. 8); Vergleich mit Schranken auf delta v/v (arXiv:2403.09325).
"""
import math

b0, b1100 = 0.5493, 0.527
eta0, eta1 = math.atanh(b0), math.atanh(b1100)
g_sym0, g_sym1 = math.cosh(2 * eta0), math.cosh(2 * eta1)
g_asym1 = math.cosh(eta1 + eta0)                 # Tachyon-Frame fest bei eta_s = eta0
print("1. gamma_L heute %.4f; z = 1100: symmetrisch %.4f, nur Materie-Frame %.4f" % (g_sym0, g_sym1, g_asym1))

print("\n2. H15 + Drift: cot theta_W = gamma_L")
for name, g in (("heute", g_sym0), ("z=1100 symmetrisch", g_sym1), ("z=1100 nur Materie", g_asym1)):
    s2 = 1 / (1 + g * g)
    print("   %-20s sin^2 theta_W = %.4f, m_W/m_Z = %.4f" % (name, s2, g / math.sqrt(1 + g * g)))

print("\n3. H0-Faktor (Soll 1,083)")
for name, r in (("symmetrisch", g_sym0 / g_sym1), ("nur Materie", g_sym0 / g_asym1)):
    print("   %-12s Verhaeltnis %.4f: ^1.5 = %.4f, ^2 = %.4f, ^3 = %.4f; Exponent fuer 1,083: %.2f" %
          (name, r, r ** 1.5, r ** 2, r ** 3, math.log(1.083) / math.log(r)))

print("\n4. BBN-Abschaetzung bei festem alpha und v (nur Schleifenterm)")
for name, g in (("z=1100 symmetrisch", g_sym1), ("z=1100 nur Materie", g_asym1)):
    dGF = 3 / (32 * math.pi ** 2) * (g_sym0 ** 2 - g ** 2)     # c^2/s^2 = cot^2 = gamma_L^2
    print("   %-20s Delta G_F/G_F = %+.4f, gleichwertig delta v/v = %+.4f" % (name, dGF, -dGF / 2))
print("   Schranken delta v/v (arXiv:2403.09325): He-4 [-0.014, +0.026], Deuterium [-0.005, -0.001]")
