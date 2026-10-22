"""k54: Zeitskala der gekickten Dualitaetsdynamik (r11) aus dem Uhrenmodell der Quelle (r15). Erkundung K7.

1. Die r15-Tickform G_V(tau) = 1 + (G_avail - 1) cos^2((tau - tau_V)/sigma_V) hat dieselbe Form wie die
   C-Port-Energie zwischen zwei Kicks, cos^2(omega t): omega = 1/sigma_V.
2. Kleinste Uhrensonde mit Profil: zwei Terme -> cos^2(Delta gamma tau / 2), sigma = 2/Delta gamma (Schwebung).
3. Fenster der Kette R_A gegen eine C5-Stufe (30 Grad).
4. Die Quelle verbindet Hopf- und Gitterwert: beta_sym = (1/sqrt3) exp(-gamma_1/(4 pi gamma_L^5)).
"""
import math
import numpy as np

g1, g2 = 14.134725141734693, 21.022039638771555          # erste zwei Riemann-Nullstellen (Ordinaten)
dg = g2 - g1
tau = np.linspace(-1, 1, 2001)
probe = np.abs(np.exp(1j * g1 * tau) + np.exp(1j * g2 * tau)) ** 2 / 4
print("1./2. Zwei-Term-Sonde = cos^2(Delta gamma tau/2): max Abweichung %.1e" % np.abs(probe - np.cos(dg * tau / 2) ** 2).max())
sigma = 2 / dg; Tb = 2 * math.pi / dg
print("   Delta gamma = %.6f, sigma = 2/Delta gamma = %.6f, Schwebungsperiode T_b = %.6f (Uhreneinheiten)" % (dg, sigma, Tb))
tk = math.pi / 6 * sigma
print("   Kickabstand tau_k = (pi/6) sigma = %.6f = T_b/6 = %.6f" % (tk, Tb / 6))
for k, txt in ((3, "Vierteldrehung"), (6, "z -> -z"), (12, "volle Drehung"), (20, "Detektorstufe"), (24, "Spinor")):
    print("   %2d Stufen = %.4f Uhreneinheiten = %.3f Schwebungsperioden (%s)" % (k, k * tk, k * tk / Tb, txt))

print("\n3. Fensterhalbbreiten delta_V/sigma_V (r15) gegen eine C5-Stufe (30 Grad) und die r12-Toleranz (26.57 Grad)")
for v, x, chain in (("V3", 0.684719, "R_A"), ("V5", 0.886077, "R_A"), ("V8", 0.490883, "R_B")):
    d = math.degrees(x)
    print("   %s (%s): %.2f Grad -> eine C5-Stufe %s" % (v, chain, d, "passt hinein" if d > 30 else "passt nicht"))

print("\n4. Hopf- und Gitterwert in der Quelle")
gL = 0.2375 / (math.log(2) / (math.pi * math.sqrt(3)))
b_lat = math.exp(-g1 / (4 * math.pi * gL ** 5)) / math.sqrt(3)
print("   beta = (1/sqrt3) exp(-gamma_1/(4 pi gamma_L^5)) = %.5f (Quelle: 0.5492)" % b_lat)
for name, b in (("Hopf (gamma_1 -> 0)", 1 / math.sqrt(3)), ("Gitter", b_lat)):
    q = 1 / (1 + b * b)
    print("   %-20s Stufenwinkel arctan(beta) = %.3f Grad, q = %.5f" % (name, math.degrees(math.atan(b)), q))
