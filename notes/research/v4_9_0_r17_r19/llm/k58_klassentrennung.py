"""k58: Klassentrennung (v4.9.0-r18.2) auf alle gamma_L-Stellen des Hauptkorpus angewandt.

Regel, mechanisch und vor dem Ablesen der Vergleichswerte festgelegt:
  - Monom in k-gewichteten Konstanten (X = prod Konstanten^n, Gewicht k = sum n k_i) -> Skala, Faktor e^{k eta} (Weg C).
  - Zustandsfunktion (Sichtbarkeit, Eigenwertverhaeltnis, Mischung, Verhaeltnis zweier k = 0-Groessen) -> Auslese, gamma_L (Weg A).
  eta = arcosh(gamma_L)/2 wie in k57/r18; artanh(beta_sym) weicht in der vierten Stelle ab (Probe unten).
"""
import math

gBI = 0.2375
gs = math.log(2) / (math.pi * math.sqrt(3))
gL = gBI / gs
bsym = 0.5493
eta = 0.5 * math.acosh(gL)
D = math.exp(eta)
g1 = 14.134725

print("Probe: gamma_L = %.5f, cosh 2 artanh(beta_sym) = %.5f, e^eta = %.5f, tanh eta = %.5f" % (gL, math.cosh(2 * math.atanh(bsym)), D, math.tanh(eta)))

def row(name, a, c, unit=""):
    print("   %-52s A %-12s C %-12s  C/A %+.2f %%" % (name, ("%.4g" % a) + unit, ("%.4g" % c) + unit, 100 * (c / a - 1)))

print("\n1. Skalengroessen (Weg C)")
row("Planck-Laenge Photon-Frame, thm:planck-photon [m]", 1.616e-35 * gL ** -1.5, 1.616e-35 * D ** -1.5)
row("Vakuum-Verhaeltnis, k = 5 (r03 F1)", gL ** 5, D ** 5)
row("Vakuum-Verhaeltnis, k = 6 (alter Wortlaut)", gL ** 6, D ** 6)
row("Matter-Fehler: log10 Rest nach 10^-122 (k = 5)", -122 + 5 * math.log10(gL), -122 + 5 * math.log10(D))
row("Neutrino gamma^4", gL ** 4, D ** 4)
row("Neutrino Photon-Frame-Unterdrueckung gamma^-3", gL ** -3, D ** -3)
row("Muon g-2: hvp-Faktor bei k(alpha_s) = 1", gL ** -1, D ** -1)
row("Muon g-2: Untergrenze Bereich gamma^-2", gL ** -2, D ** -2)
row("Lambda_bare Photon-Frame [m_P^4], prop:bare-lambda", g1 ** 2 / gL ** 2, g1 ** 2 / D ** 2)
row("rem:open: beta^2 gamma^-3 / 200", bsym ** 2 * gL ** -3 / 200, bsym ** 2 * D ** -3 / 200)
row("erste Nullstelle Photon-Frame gamma_1/gamma", g1 / gL, g1 / D)
row("beta_eff = 2 gamma (cor:gue-frame (iii))", 2 * gL, 2 * D)

print("\n2. P3 (conj:cl-correction), Exponent k = 5 -> Skala")
pA = math.exp(-g1 / (4 * math.pi * gL ** 5)) / math.sqrt(3)
pC = math.exp(-g1 / (4 * math.pi * D ** 5)) / math.sqrt(3)
b = 0.55
for _ in range(200):
    b = math.exp(-g1 / (4 * math.pi * math.exp(5 * math.atanh(b)))) / math.sqrt(3)
print("   A: %.5f (%+.3f %% gegen 0,5493)   C: %.5f (%+.3f %%)   C selbstkonsistent: %.5f (%+.3f %%)"
      % (pA, 100 * (pA / bsym - 1), pC, 100 * (pC / bsym - 1), b, 100 * (b / bsym - 1)))

print("\n3. P5 (Jahresmodulation): d ln X = k d sigma unter C")
print("   unter C: (dalpha/alpha)/(dG/G) = k(alpha)/k(G_N) = %.3f exakt, ohne Vorfaktor" % (1 / 2))
print("   Hauptkorpus nennt gamma^-1 = %.3f (die Formel dort ergaebe %.3f); r09 korrigierte auf 1/2, unter C folgt das von selbst" % (gL ** -1, gL ** -1 / 2))

print("\n4. P6 (Hawking): T_H hat k = -1 -> Skala")
print("   T_Sphaera / T_H^tachyon = gamma_string * Faktor: A %.5f, C %.5f; gamma_BI = %.5f (Abweichung unter C %+.2f %%)"
      % (gs * gL, gs * D, gBI, 100 * (gs * D / gBI - 1)))
print("   gamma_string/gamma (Photon-Frame-Vorfaktor): A %.5f, C %.5f" % (gs / gL, gs / D))

print("\n5. Auslesegroessen (Weg A, unveraendert)")
print("   gamma_BI/gamma_string = %.5f (thm:frame-offset), 1/gamma_L = %.4f, Omega_M = beta^2 = %.4f" % (gL, 1 / gL, bsym ** 2))
print("   H15 (cot theta_W on-shell = gamma_L): Mischungswinkel = Auslese, Vorab-Notiz H15 unberuehrt")
print("   Koide P2: theta_K = pi - sqrt2 arcsin(beta_sym) = %.2f Grad, unveraendert" % math.degrees(math.pi - math.sqrt(2) * math.asin(bsym)))
