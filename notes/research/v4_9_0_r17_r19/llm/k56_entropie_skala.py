"""k56: Entropie als Ordnungsparameter zwischen den Frames, und eine Skalen-Dimension sigma (Erkundung, Fragen 2 und 3).

Zustandsscheibe (r04): b = (Re s, Im s)/2u, |b| = 1/cosh(2 eta_f), eta_f = Rapiditaet gegen das System mit E || B.
rho = (1 + b.sigma)/2, Eigenwerte p = (1 +- |b|)/2, Entropie S = H(p).
Skalen-Dimension: k-Gesetz X = g^k X_ph als Skalierung mit Gewichten k; welche Wahl von sigma ist additiv?
"""
import math
import numpy as np

gL = 0.2375 / (math.log(2) / (math.pi * math.sqrt(3)))
eta_s = 0.5 * math.acosh(gL)
H = lambda p: -sum(x * math.log2(x) for x in (p, 1 - p) if x > 0)

print("1. Eigenwerte und Entropie in Abhaengigkeit von eta_f")
for name, e in (("Ruhesystem", 0.0), ("Hopf (gamma_L = 2)", 0.5 * math.acosh(2)), ("Materie-Frame eta_sym", eta_s),
                ("eta = 1", 1.0), ("eta = 3", 3.0), ("Licht (eta -> inf)", 30.0)):
    b = 1 / math.cosh(2 * e); p = (1 + b) / 2
    print("   %-24s |b| = %.4f  p = %.5f / %.5f  S = %.4f Bit  1/|b| = %8.4f" % (name, b, p, 1 - p, H(p), 1 / b))
e = eta_s; b = math.tanh(e)
print("   Identitaeten: p_max = 1/(1+beta^2) = %.5f, p_min/p_max = beta^2 = %.5f, p_min = beta^2/(1+beta^2) = %.5f"
      % (1 / (1 + b * b), b * b, b * b / (1 + b * b)))
print("   zum Vergleich thm:dark-energy Omega_M = beta^2 = %.4f (nicht gleich p_min = %.4f)" % (b * b, b * b / (1 + b * b)))

print("\n2. Informationsabstand (Bures, reelle Scheibe): ds^2 = (dr^2/(1-r^2) + r^2 dtheta^2)/4")
def bures_radial(eta):
    # r = sech(2x): dr^2/(1 - r^2) = 4 sech^2(2x) dx^2, also ds = sech(2x) dx (mit dem Faktor 1/4 in ds^2)
    xs = np.linspace(0, eta, 200001)
    return np.trapezoid(1 / np.cosh(2 * xs), xs)
gd = lambda x: 2 * math.atan(math.tanh(x / 2))
for e in (eta_s, 1.0, 5.0):
    print("   eta = %.4f: radialer Abstand = %.5f, gd(2 eta)/2 = %.5f" % (e, bures_radial(e), gd(2 * e) / 2))
print("   Licht liegt im Abstand pi/4 = %.5f vom Ruhezustand: endlich; singulaer ist nur die Richtung (r^2 dtheta^2 -> 0)" % (math.pi / 4))

print("\n3. Skalen-Dimension sigma: welche Umrechnung ist eine Verschiebung auf einer Linie?")
e1, e2 = eta_s, eta_s
for name, f in (("Lorentz cosh(eta)", math.cosh), ("Doppler e^eta", math.exp)):
    print("   %-18s f(e1) f(e2) = %.5f, f(e1+e2) = %.5f -> %s" % (name, f(e1) * f(e2), f(e1 + e2),
          "additiv" if math.isclose(f(e1) * f(e2), f(e1 + e2)) else "nicht additiv"))
print("   sigma als Koordinate (Verschiebungen komponieren) verlangt sigma = eta: X = e^{k eta} X_ph (Weg C von r01)")
print("   Weg A (gamma_L) ist cosh(2 eta) = e^{sigma} nur am Tribonacci-Punkt (r01.3)")

print("\n4. Gewicht-0-Kombinationen sind sigma-invariant")
k = {"m_e c^2": 1, "hbar": 1, "alpha": 1, "G_N": 2, "c": 0}
for combo, w in (("m_e c^2 / hbar (Compton)", k["m_e c^2"] - k["hbar"]), ("alpha^2 m_e c^2/hbar (Atomuhr)", 2 * k["alpha"]),
                 ("Verhaeltnis Atomuhr/Compton", 2 * k["alpha"])):
    print("   %-34s Gewicht %d -> %s" % (combo, w, "invariant" if w == 0 else "verschiebt sich mit e^{%d sigma}" % w))
