"""k64: Dynamik fuer die gekickte Dualitaetsdrehung (Autorlesart, v4.9.0-r16): Drehung plus Kompensator-Messung.

Dublettzustand rho = (1 + b.sigma)/2, reell: b = (b_x, b_z), x = Kompensatorachse (C_HC = (1 + sigma_x)/2).
Schritt: Drehung U = exp(-i alpha sigma_y) (Hilbert-Winkel alpha, Bloch-Winkel 2 alpha), dann Messung {C, A}.
  selektiv:      Zustand in C behalten, Ueberlebenswahrscheinlichkeit p = tr(C U rho U^T)
  nicht-selektiv: rho -> C rho' C + A rho' A   (Inhalt an das Partnerreservoir abgegeben)
"""
import math
import numpy as np

sx = np.array([[0, 1], [1, 0]], float); sz = np.array([[1, 0], [0, -1]], float)
C = (np.eye(2) + sx) / 2; A = (np.eye(2) - sx) / 2
U = lambda a: np.array([[math.cos(a), -math.sin(a)], [math.sin(a), math.cos(a)]])
rho_of = lambda bx, bz: (np.eye(2) + bx * sx + bz * sz) / 2
bvec = lambda r: (np.trace(r @ sx), np.trace(r @ sz))
H = lambda r: -sum(l * math.log2(l) for l in np.linalg.eigvalsh(r) if l > 1e-15)

def kick(r, a, selective):
    r1 = U(a) @ r @ U(a).T
    if selective:
        p = np.trace(C @ r1)
        return C @ r1 @ C / p, p
    return C @ r1 @ C + A @ r1 @ A, None

gL = 0.2375 / (math.log(2) / (math.pi * math.sqrt(3)))
a6 = math.pi / 6

print("1. Selektiv (C5-Rekursion): Ueberleben je Schritt cos^2 alpha")
r = rho_of(1, 0); P = 1.0; n20 = None
for n in range(1, 31):
    r, p = kick(r, a6, True); P *= p
    if n20 is None and P < 1 / 256:
        n20 = n
print("   p = %.6f = 3/4; erstes n mit (3/4)^n < 1/256: n = %d" % (p, n20))

print("\n2. Nicht-selektiv: ein pi/6-Kick aus dem reinen Zustand R")
r1, _ = kick(rho_of(1, 0), a6, False)
b = bvec(r1); ev = np.linalg.eigvalsh(r1)
print("   b = (%.4f, %.4f), |b| = %.4f, gamma = 1/|b| = %.4f, Eigenwerte %.4f / %.4f, Entropie %.4f Bit"
      % (b[0], b[1], math.hypot(*b), 1 / math.hypot(*b), ev[1], ev[0], H(r1)))
am = 0.5 * math.acos(1 / gL)
print("   gemessener Abstand |b| = 1/gamma_L = %.4f  <=>  Kickwinkel alpha = %.3f Grad (pi/6 = 30 Grad); Ueberleben cos^2 = %.4f"
      % (1 / gL, math.degrees(am), math.cos(am) ** 2))
P = 1.0; n = 0
while P >= 1 / 256:
    n += 1; P *= math.cos(am) ** 2
print("   mit diesem Winkel faellt (cos^2 alpha)^n erst bei n = %d unter 1/256" % n)

print("\n3. Fluss zum Photon (b = 0) und Entropie, zufaellige Startzustaende")
rng = np.random.default_rng(3); mono = 0; tot = 0
for _ in range(500):
    rr = rng.uniform(0, 1); th = rng.uniform(0, 2 * math.pi)
    r = rho_of(rr * math.cos(th), rr * math.sin(th)); a = rng.uniform(0.05, math.pi / 2 - 0.05)
    s0 = H(r)
    for k in range(40):
        r2, _ = kick(r, a, False); tot += 1
        mono += H(r2) >= H(r) - 1e-12; r = r2
print("   Entropie nie fallend: %d/%d Schritte; |b| nach 40 Kicks (letzter Lauf) = %.2e" % (mono, tot, math.hypot(*bvec(r))))
r, _ = kick(rho_of(1, 0), math.pi / 4, False)
print("   alpha = pi/4: |b| nach einem Kick = %.2e (Photon-Zustand in einem Schritt); selektives Ueberleben dort = %.2f"
      % (math.hypot(*bvec(r)), math.cos(math.pi / 4) ** 2))
r, p = kick(rho_of(1, 0), math.pi / 2, True) if False else (None, math.cos(math.pi / 2) ** 2)
print("   alpha = pi/2: selektives Ueberleben = %.2e (Kompensatorport leer, Inhalt ganz im Partnerport, r12.2(c))" % p)

print("\n4. Invariante s: |s| = 2u |b| bei festem u")
for name, rr in (("R", rho_of(1, 0)), ("nach 1 Kick", kick(rho_of(1, 0), a6, False)[0]), ("nach 3 Kicks", None)):
    if rr is None:
        rr = rho_of(1, 0)
        for _ in range(3):
            rr, _ = kick(rr, a6, False)
    print("   %-12s |s|/2u = %.4f" % (name, math.hypot(*bvec(rr))))
print("   Drehungen und Boosts von Lesart B lassen |s| fest; die Messung aendert es (nicht unitaer)")

print("\n5. Kontinuumsgrenze: alpha = omega tau, tau -> 0")
w = 1.0
for tau in (0.2, 0.05, 0.01):
    a = w * tau
    rate = -math.log(math.cos(2 * a)) / tau
    print("   tau = %.2f: Zerfallsrate von |b| = %.4f, 2 omega^2 tau = %.4f" % (tau, rate, 2 * w * w * tau))
print("   -> Gamma = 2 omega^2 tau -> 0 fuer tau -> 0 (Zeno): Lindblad-Dephasierung in der Kompensatorbasis")

print("\n6. Tachyon-Frame (J_B tauscht die Ports, b -> -b)")
r = rho_of(-1, 0); rt, pt = kick(r, a6, True) if False else (None, None)
r1 = U(a6) @ rho_of(-1, 0) @ U(a6).T
print("   Ueberleben im Partnerport (Kompensator des Tachyon-Frames) = %.4f; nicht-selektiv |b| = %.4f"
      % (np.trace(A @ r1), math.hypot(*bvec(C @ r1 @ C + A @ r1 @ A))))
