"""k57: Frage 1 und die Bedingung, unter der Weg A (gamma_L = cosh 2 eta) und Weg C (Doppler e^eta) zugleich gelten.

1. Drei Lesarten desselben Abstands: 1/beta = coth eta = sqrt(p+/p-), e^eta (Doppler), cosh 2 eta = 1/|b|; Gleichheit am Tribonacci-Punkt.
2. Klassentrennung auf der sigma-Linie: Skalengroessen X = e^{k sigma} X0 (Homomorphismus, Weg C),
   Auslesegroessen f(sigma) (Zustandsfunktion, z. B. Sichtbarkeit sech 2 sigma, Weg A) - beide komponieren ueber sigma-Addition.
3. Umrechnungen des Hauptkorpus nach Klassen, Zahlen unter C gegen A.
"""
import math

gL = 0.2375 / (math.log(2) / (math.pi * math.sqrt(3)))
eta = 0.5 * math.acosh(gL)
T = 1.8392867552141612; eT = math.log(T)

print("1. Drei Lesarten")
for name, e in (("gemessen (eta_sym)", eta), ("Tribonacci", eT)):
    print("   %-20s 1/beta = coth eta = %.5f, e^eta = %.5f, cosh 2 eta = 1/|b| = %.5f" % (name, 1 / math.tanh(e), math.exp(e), math.cosh(2 * e)))
print("   Dokumentkonstanten: 1/beta_sym = 1,820 (Hauptkorpus), e^eta = 1,854 (r01 Weg C), gamma_L = 1,864 (Weg A)")
print("   sqrt(p+/p-) = 1/beta (r17): %.5f" % (1 / math.tanh(eta)))

print("\n2. Komposition auf der sigma-Linie")
e1, e2 = 0.3, eta
print("   Skala:   e^{e1} e^{e2} = %.5f = e^{e1+e2} = %.5f" % (math.exp(e1) * math.exp(e2), math.exp(e1 + e2)))
print("   Auslese: Sichtbarkeit nach zwei Boosts = sech(2(e1+e2)) = %.5f; Produkt der Einzelwerte = %.5f (nicht gemeint)"
      % (1 / math.cosh(2 * (e1 + e2)), (1 / math.cosh(2 * e1)) * (1 / math.cosh(2 * e2))))
print("   -> Weg A ist als Zustandsfunktion f(sigma) konsistent, sobald man Rapiditaeten addiert statt Faktoren multipliziert")

print("\n3. Umrechnungen des Hauptkorpus (Potenz k) unter C (e^{k eta}) und A (gamma_L^k)")
rows = [("Taktfrequenz, cor:gue-frame", 1, "Skala"), ("Planck-Laenge, thm:planck-photon", 1.5, "Skala"),
        ("Neutrinomasse, prop:k-neutrino", 4, "Skala"), ("Matter-Fehler, cor:matter-error", 5, "Skala"),
        ("Vakuumenergie (r03: k = 5 statt 6)", 5, "Skala"), ("Hawking-Temperatur, prop:hawking-gBI-tachyon", 1, "Skala")]
for name, k, cls in rows:
    a, c = gL ** k, math.exp(k * eta)
    print("   %-46s k = %-4s %-6s A %8.4f  C %8.4f  Abweichung %+.2f %%" % (name, k, cls, a, c, 100 * (c / a - 1)))
print("   Auslesegroessen (Weg A als Zustandsfunktion):")
print("     Sichtbarkeit / Kompensator-Kontrast (r03)  1/gamma_L = %.4f" % (1 / gL))
print("     Eigenwertverhaeltnis p-/p+ = beta^2 (r17), thm:dark-energy Omega_M = beta^2 = %.4f" % math.tanh(eta) ** 2)
print("     Mischungsverhaeltnis cot theta_W ~ gamma_L (r07, Beobachtung) = %.4f" % gL)
print("     gamma_BI/gamma_string (thm:frame-offset, strukturell) = %.4f" % gL)
