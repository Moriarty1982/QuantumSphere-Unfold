"""k63: Die drei Widersprueche aus v4.9.0-r23 als Folge der Ein-Frame-Arbeit des Hauptkorpus.

W1 Vorzeichen: Sektordefinition (Materie beta < 0) gegen thm:symmetric-frame (Materie +beta).
W2 Tachyon-Lage: Hauptkorpus -beta gegen Konvention F 1/beta.
W3 Photon-Lage: Hauptkorpus beta = 0 gegen Konvention F b = 0 (beta -> 1).
"""
import cmath
import math
import numpy as np

rng = np.random.default_rng(1)
gL = 0.2375 / (math.log(2) / (math.pi * math.sqrt(3)))
eta = 0.5 * math.acosh(gL)
beta = math.tanh(eta)

print("W1: eine gemeinsame Spiegelung z -> -z (Ladungskonjugation C, v4.9.0-r02)")
ok = 0
for _ in range(1000):
    z = rng.normal(size=3) + 1j * rng.normal(size=3)
    s, s2 = z @ z, (-z) @ (-z)
    ok += abs(s - s2) < 1e-12 and np.all(np.sign((-z).real) == -np.sign(z.real))
print("   s(z) = s(-z) und Re z wechselt das Vorzeichen: %d/1000" % ok)
print("   -> das Vorzeichen von beta ist ein Orientierungscode (v4.8.0-r01), der Sektor haengt am Vorzeichen von s (v4.8.0-r07)")

print("\nW2: Tachyon-Rapiditaet -eta + i pi/2")
bT = cmath.tanh(-eta + 1j * math.pi / 2)
print("   tanh(-eta + i pi/2) = %.5f%+.5fi = -coth eta = %.5f" % (bT.real, bT.imag, -1 / beta))
print("   Projektion auf die eine reelle Achse (Imaginaerteil weggelassen): Rapiditaet -eta, beta = %.5f = -beta_sym" % math.tanh(-eta))
print("   im eigenen Frame: beta_T^2 = %.5f = 1/beta^2 = %.5f" % (abs(bT) ** 2, 1 / beta ** 2))
for name, f in (("Omega_M = beta^2", lambda b: b * b), ("g_tt = -beta^2", lambda b: -b * b), ("Beltrami mu = beta^2", lambda b: b * b)):
    print("   %-22s M %.4f   T von R aus %.4f   T im eigenen Frame %.4f" % (name, f(beta), f(-beta), f(abs(bT))))

print("\nW3: Bezugsframe R des Hauptkorpus = reiner Zustand |b| = 1 (beta = 0)")
b = lambda e: 1 / math.cosh(2 * e)
H = lambda p: -sum(q * math.log2(q) for q in (p, 1 - p) if q > 0)
print("   Umrechnungsfaktor |b_R|/|b_M| = %.5f = gamma_L = %.5f" % (b(0) / b(eta), gL))
print("   zum echten Photon (b -> 0) waere der Faktor unendlich: |b(5)| = %.2e" % b(5))
for name, e in (("R (beta = 0)", 0.0), ("Materie", eta), ("P (beta -> 1)", 20.0)):
    p = (1 + b(e)) / 2
    print("   %-15s |b| = %.4f  Entropie %.4f Bit  Rahmenterm beta^2 = %.4f  p-/p+ = %.4f" % (name, b(e), abs(H(p)), math.tanh(e) ** 2, (1 - p) / p))
print("   -> Lambda = 0 und Rahmenterm 0 gelten in R; am echten Photon P sind Rahmenterm und p-/p+ maximal (1)")
