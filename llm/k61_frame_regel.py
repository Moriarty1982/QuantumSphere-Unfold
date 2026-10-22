"""k61: Regel der Frame-Unterscheidung (v4.9.0-r21) auf die Hauptaussagen angewandt.

Regel: Materie M bei x = beta^2; Tachyon T = J_B-Bild: x -> 1/x, p+ <-> p-, gamma -> -gamma (Rapiditaet eta + i pi/2,
cosh 2 eta -> -cosh 2 eta); Photon P = entarteter Fixpunkt b = 0, p+ = p- = 1/2.
Eine Aussage ist frame-frei, wenn M und T denselben Wert geben; P wird eigens vermerkt.
"""
import cmath
import math

gL = 0.2375 / (math.log(2) / (math.pi * math.sqrt(3)))
eta = 0.5 * math.acosh(gL)
x = math.tanh(eta) ** 2

def frame(x, tach=False):
    g = (1 + x) / (1 - x)
    pp, pm = 1 / (1 + x), x / (1 + x)
    return g, pp, pm

gM, ppM, pmM = frame(x)
xT = 1 / x
gT, ppT, pmT = frame(xT)       # gamma negativ, p+ und p- getauscht
H = lambda p: -sum(q * math.log2(q) for q in (p, 1 - p) if q > 0)

print("Probe Tachyon: gamma_T = %.4f (= -gamma_M), p+_T = %.4f (= p-_M), p-_T = %.4f (= p+_M)" % (gT, ppT, pmT))
rows = []
def add(name, m, t, p, note=""):
    rows.append((name, m, t, p, note))

add("Frame-Faktor gamma", "%.4f" % gM, "%.4f" % gT, "unendlich", "Betrag gleich, Vorzeichen (Phase i pi)")
add("Sichtbarkeit |b| = 1/|gamma|", "%.4f" % (1 / gM), "%.4f" % (1 / abs(gT)), "0", "frame-frei M/T")
add("Eigenwerte (p+, p-)", "(%.3f, %.3f)" % (ppM, pmM), "(%.3f, %.3f)" % (ppT, pmT), "(0.5, 0.5)", "getauscht")
add("Entropie [Bit]", "%.4f" % H(ppM), "%.4f" % H(ppT), "1", "frame-frei M/T")
add("C5-Faktor, Kick-Lesart cos^2(pi/6)", "0.75", "0.75", "-", "frame-frei (A R A = cos a A wie C R C)")
add("C5-Faktor, Eigenwert im Kompensatorport", "%.4f" % ppM, "%.4f" % pmM, "0.5", "nur Materie")
add("Omega_M = p-/p+ (thm:dark-energy)", "%.4f" % (pmM / ppM), "%.4f" % (pmT / ppT), "1", "nur Materie")
kt = "undefiniert (1/beta > 1)"
add("Koide-Phase pi - sqrt2 arcsin(beta)", "%.2f Grad" % math.degrees(math.pi - math.sqrt(2) * math.asin(math.sqrt(x))), kt, "-", "nur Materie")
add("cot theta_W ~ gamma (r07)", "%.4f" % gM, "%.4f" % gT, "unendlich", "theta -> 180 - theta")
add("sin^2 theta_W = 1/(1+gamma^2)", "%.4f" % (1 / (1 + gM ** 2)), "%.4f" % (1 / (1 + gT ** 2)), "0", "frame-frei M/T; H15 unberuehrt")
add("P5 = k(alpha)/k(G_N)", "0.5", "0.5", "-", "frame-frei (Phasen konstant)")
add("k = 0-Groessen (c, gamma_BI, m_e c^2/hbar)", "1", "1", "1", "frame-frei in allen drei")
add("Uhrschranke Delta_gamma (r21)", "0.1925", "kein Fenster", "entartet", "nur Materie")

print("\n%-44s %-16s %-26s %-10s %s" % ("Aussage", "Materie", "Tachyon", "Photon", "Status"))
for r in rows:
    print("%-44s %-16s %-26s %-10s %s" % r)

print("\nSkalengesetz im Tachyon-Frame (r82: ell_T^2 = -lambda_T^2, ell_T = i lambda_T)")
for k, name in ((1.5, "ell_P (k = 3/2)"), (3, "ell_P^2 (k = 3)"), (1, "Frequenz (k = 1)")):
    A = (-1 + 0j) ** k                       # Weg A: gamma -> -gamma
    C = cmath.exp(1j * math.pi / 2 * k)      # Weg C: e^{k(eta + i pi/2)} / e^{k eta}
    C2 = cmath.exp(1j * math.pi * k)         # Weg C mit Verschiebung i pi je Einfuegung
    f = lambda z: "%+.3f%+.3fi" % (z.real, z.imag)
    print("   %-18s Phase unter A: %s   unter C (i pi/2): %s   unter C (i pi): %s" % (name, f(A), f(C), f(C2)))
print("   -> r82-Vorzeichenskala (ell^2 -> -1) folgt aus A oder aus C mit i pi je Einfuegung, nicht aus C mit i pi/2")
