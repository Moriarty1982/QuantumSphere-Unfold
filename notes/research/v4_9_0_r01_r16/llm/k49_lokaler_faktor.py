"""k49: Was kann der lokale Faktor gamma_L^(local) sein? (Erkundung E15, kein Test.)

Drei Lesarten, je mit dem k-Gesetz delta ln X = k(X) * delta ln gamma_L^(local):
  V  Geschwindigkeit gegen ein ausgezeichnetes System: Beobachter-Rapiditaet addiert sich zu eta.
  P  Gravitationspotential: delta ln gamma_L^(local) = kappa * delta Phi / c^2 (P5: kappa ~ 1e-10).
  D  Materiedichte: keine Form in der Quelle.
Dazu P5 nachgerechnet: (delta alpha/alpha)/(delta G/G) aus dem k-Gesetz.
"""
import math

gL = 0.2375 / (math.log(2) / (math.pi * math.sqrt(3)))
eta = 0.5 * math.acosh(gL)
c = 299792.458
bound_annual = 8.4e-18 * 2           # r03 F2: Jahresamplitude (-8.9 +- 8.4)e-18, grob 2 sigma

print("V  Geschwindigkeit: Erdbahn 29.8 km/s, Projektion auf den CMB-Dipol ~ cos(11 Grad)")
d_eta = 29.8 * math.cos(math.radians(11)) / c
d_ln_g = 2 * math.tanh(2 * eta) * d_eta
print("   delta eta = %.2e, delta ln gamma_L = 2 tanh(2 eta) delta eta = %.2e -> delta alpha/alpha (k = 1) = %.2e" % (d_eta, d_ln_g, d_ln_g))
print("   Jahresamplitude erlaubt ~ %.1e -> ueberschritten um Faktor %.1e" % (bound_annual, d_ln_g / bound_annual))
d_eta_cmb = 369.8 / c
print("   statischer Anteil (369.8 km/s gegen CMB): delta ln gamma_L = %.2e, richtungsabhaengig" % (2 * math.tanh(2 * eta) * d_eta_cmb))

print("\nP  Potential: Sonnenpotential an der Erde GM/(c^2 a) = 9.87e-9, Exzentrizitaet 0.0167")
dphi = 9.87e-9 * 0.0167
for kappa in (1e-10, 1e-9):
    print("   kappa = %.0e: Jahresamplitude delta alpha/alpha = %.1e" % (kappa, kappa * dphi))
print("   kosmische Drift: Potentiale der grossen Strukturen ~1e-5 -> delta ln gamma ~ %.0e (gebraucht fuer H0: ~5e-2)" % (1e-10 * 1e-5))

print("\nKopplungsmuster der Lesart P: beta_X = k(X) * kappa")
for name, k in (("Compton-Uhr m_e c^2/hbar", 0), ("alpha", 1), ("Atomuhr alpha^2 m_e c^2/hbar", 2), ("G_N", 2)):
    print("   %-30s k = %d -> Kopplung %d kappa" % (name, k, k))

print("\nP5 nachgerechnet: X_m = gamma^k X_ph -> delta X_m / X_m = k delta gamma / gamma")
print("   (delta alpha/alpha)/(delta G/G) = k(alpha)/k(G_N) = 1/2 = 0.5")
print("   P5 schreibt gamma^(k(alpha)-k(G)) * k(alpha)/k(G) und setzt das = gamma^-1 = %.3f;" % (1 / gL))
print("   der Ausdruck selbst waere gamma^-1 / 2 = %.3f; der statische Faktor gehoert nicht in eine relative Aenderung" % (1 / gL / 2))
