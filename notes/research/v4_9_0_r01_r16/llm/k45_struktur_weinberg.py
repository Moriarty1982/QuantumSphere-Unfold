"""k45: Welche Groesse beschreibt der Kegel? Strukturelle Umformung von H14 (Erkundung E8, kein Test).

1. cos 2theta = tanh eta  <=>  tan theta = e^-eta  <=>  sin^2 theta = 1/(1 + e^{2 eta})  <=>  2 theta = Pi(eta),
   Pi(x) = 2 arctan(e^-x) der Parallelitaetswinkel (Lobatschewski); cos Pi(x) = tanh x.
2. Portgewichtung e^{t sx} = e^t C + e^-t A (r05.1d) bei t = eta: Gewichtsverhaeltnis e^{2 eta} = cot^2 theta = (g/g')^2.
   H14 ist also eine Aussage ueber ein Kopplungsverhaeltnis, nicht ueber ein Massenverhaeltnis.
3. Kopplungsverhaeltnisse laufen. MS-bar sin^2 (PDG Abb. 10.1): Minimum bei mu = M_W; oberhalb Ein-Schleifen-Lauf.
"""
import math

gL = 0.2375 / (math.log(2) / (math.pi * math.sqrt(3)))
eta = 0.5 * math.acosh(gL); b = math.tanh(eta)
th = math.atan(math.exp(-eta))
print("1. Umformungen bei eta = %.5f" % eta)
print("   cos 2theta = %.6f, tanh eta = %.6f" % (math.cos(2 * th), b))
print("   sin^2 theta = %.6f, 1/(1 + e^{2 eta}) = %.6f, (1 - beta)/2 = %.6f" % (math.sin(th) ** 2, 1 / (1 + math.exp(2 * eta)), (1 - b) / 2))
Pi = 2 * math.atan(math.exp(-eta))
print("   Parallelitaetswinkel Pi(eta) = %.4f Grad, Kegel arccos(beta) = %.4f Grad, 2 theta = %.4f Grad" %
      (math.degrees(Pi), math.degrees(math.acos(b)), math.degrees(2 * th)))
print("   cos^2 theta = (1 + beta)/2 = %.6f = logistisch sigma(2 eta) = %.6f" % ((1 + b) / 2, 1 / (1 + math.exp(-2 * eta))))

print("\n2. Portgewichtung bei t = eta")
print("   Gewichte e^{+-eta} = %.5f, %.5f; Verhaeltnis e^{2 eta} = %.5f = cot^2 theta = %.5f; g/g' = e^eta = %.5f (Doppler, r01 Weg C)" %
      (math.exp(eta), math.exp(-eta), math.exp(2 * eta), 1 / math.tan(th) ** 2, math.exp(eta)))

print("\n3. Vergleich als Kopplungs- bzw. Massenverhaeltnis")
for name, s2 in (("on-shell (Massen)", 0.22321), ("MS-bar bei M_Z", 0.23122)):
    print("   %-20s tan theta = %.5f (Struktur e^-eta = %.5f), g/g' = %.5f (Struktur %.5f)" %
          (name, math.sqrt(s2 / (1 - s2)), math.exp(-eta), math.sqrt((1 - s2) / s2), math.exp(eta)))
# Ein-Schleifen-Lauf oberhalb M_Z (SM, b_Y = 41/6, b_2 = -19/6)
aZ = 1 / 127.930; s2Z = 0.23122
inv_ap = 1 / (aZ / (1 - s2Z)); inv_a2 = 1 / (aZ / s2Z)
print("   MS-bar oberhalb M_Z (Ein-Schleife):")
for mu in (91.19, 200, 1000, 1e4, 1e10, 1e15):
    L = math.log(mu / 91.1880) / (2 * math.pi)
    ip, i2 = inv_ap - 41 / 6 * L, inv_a2 + 19 / 6 * L
    print("     mu = %9.3g GeV: sin^2 = %.5f" % (mu, i2 / (ip + i2)))
print("   unterhalb M_W steigt sin^2 laut PDG Abb. 10.1 (Minimum bei mu = M_W): kein Skalenwert erreicht %.5f" % ((1 - b) / 2))

print("\n4. (aufgefallen beim Rechnen von 3) cot theta_W on-shell gegen die drei Dokumentkonstanten")
mW, sW, mZ, sZ = 80.3692, 0.0133, 91.1880, 0.0020
cot = mW / math.sqrt(mZ ** 2 - mW ** 2)
dc_dmW = mZ ** 2 / (mZ ** 2 - mW ** 2) ** 1.5; dc_dmZ = -mW * mZ / (mZ ** 2 - mW ** 2) ** 1.5
sc = math.hypot(dc_dmW * sW, dc_dmZ * sZ)
print("   cot theta_W (on-shell) = %.5f +- %.5f; MS-bar g/g' = %.5f" % (cot, sc, math.sqrt((1 - 0.23122) / 0.23122)))
for name, v in (("1/beta_sym", 1 / b), ("e^eta (Doppler)", math.exp(eta)), ("gamma_L = cosh 2 eta", gL)):
    print("   %-22s %.5f: z (on-shell) = %+.1f" % (name, v, (v - cot) / sc))
print("   Spanne der Dokumentkonstanten [%.4f, %.4f], Spanne cot theta_W ueber die Schemata [%.4f, %.4f]" %
      (1 / b, gL, math.sqrt((1 - 0.23122) / 0.23122), cot))
for gbi in (0.2375, 0.237532, 0.2740):
    g = gbi / (math.log(2) / (math.pi * math.sqrt(3)))
    print("   gamma_BI = %.6f: gamma_L = %.5f -> m_W = m_Z gamma_L / sqrt(1 + gamma_L^2) = %.4f GeV" % (gbi, g, mZ * g / math.sqrt(1 + g * g)))
print("   gemessen m_W = 80.3692 +- 0.0133; SM-Fit 80.359 +- 0.006 (PDG)")
