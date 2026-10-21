"""k48: Was bleibt laut Dokument bei der Drift fest? Folgen fuer H15 und alpha (Erkundung E11, kein Test).

Quelle im Dokument: Def. Frame-insertion count (X^photon = gamma_L^-k X^matter), thm:k-values (k(alpha^-1) = 1,
k(c) = 0, k(gamma_BI) = 0), Korollar "alpha-drift as a frame effect" (alpha^photon konstant,
alpha^matter(t) = gamma_L^local(t) alpha^photon), prop:saturation (1), prop:H0-tension (Drift 1,6e-12/Jahr in beta_sym).
Daten: Lange et al., PRL 126, 011102 (2021): (1/alpha) d alpha/dt = 1.0(1.1)e-18 / Jahr.
"""
import math

b0, rate_b = 0.5493, 1.6e-12
g0 = (1 + b0 ** 2) / (1 - b0 ** 2)
dg_db = 4 * b0 / (1 - b0 ** 2) ** 2
rate_g = dg_db * rate_b / g0
print("gamma_L heute %.4f; d ln gamma_L/dt = %.2e pro Jahr" % (g0, rate_g))
print("k-Gesetz mit |k(alpha)| = 1: |d ln alpha/dt| = %.2e pro Jahr; Atomuhren 1.0(1.1)e-18 -> Abstand %.1e sigma" %
      (rate_g, (rate_g - 1.0e-18) / 1.1e-18))
b1100 = 0.527; g1100 = (1 + b1100 ** 2) / (1 - b1100 ** 2)
print("seit z = 1100: Delta ln alpha = %.3f (|Delta alpha/alpha| ~ %.1f %%)" % (math.log(g0 / g1100), 100 * abs(g0 / g1100 - 1)))
print("Vorzeichen: thm:k-values k(alpha^-1)=1 -> alpha^matter = alpha^photon / gamma_L; Korollar: alpha^matter = gamma_L alpha^photon")

print("\nE11b: Photon-Frame als Grundlage (Nachbarschritt statt gamma_L)")
eta0, eta1 = math.atanh(b0), math.atanh(b1100)
deta_dt = rate_b / (1 - b0 ** 2)
for name, f0, f1, rate in (("gamma_L = cosh 2 eta", g0, g1100, rate_g),
                           ("Nachbar Lorentz cosh eta", math.cosh(eta0), math.cosh(eta1), math.tanh(eta0) * deta_dt),
                           ("Nachbar Doppler e^eta", math.exp(eta0), math.exp(eta1), deta_dt)):
    kH = math.log(1.083) / math.log(f0 / f1)
    print("   %-26s Exponent fuer H0 = %.2f; |d ln alpha/dt| bei |k(alpha)| = 1: %.2e /Jahr; Delta alpha/alpha seit z=1100: %.1f %%"
          % (name, kH, rate, 100 * (f0 / f1 - 1)))
print("   lesartunabhaengig: Delta ln alpha = ln(1.083) * k(alpha)/k(H0); Atomuhren (2 sigma, 3.2e-18/Jahr) verlangen")
print("   k(alpha)/k(H0) < %.1e (bei linearer Drift ueber 13.8 Gyr)" % (3.2e-18 / (math.log(1.083) / 13.8e9)))
