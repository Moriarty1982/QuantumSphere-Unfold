"""k51: Form (iii) unter der Deutung K1 (C5-Inhalt = Feldinhalt auf dem Dublett, Score = Energie im C-Port).

Geprueft: welche Zeugen aus der Transportgruppe von Lesart B (Drehungen, Dualitaet, Boosts) den Gesamtinhalt
endlich zum Verschwinden bringen koennten. Keine Aussage ueber C5 = 0.
"""
import math
import numpy as np

rng = np.random.default_rng(51)
sx = np.array([[0., 1], [1, 0]]); I2 = np.eye(2)
C = 0.5 * (I2 + sx); A = 0.5 * (I2 - sx)


def boost(F, n, eta):
    E, B = F[:, 0], F[:, 1]
    g, bv = math.cosh(eta), math.tanh(eta) * n
    Ep = g * (E + np.cross(bv, B)) - (g - 1) * (E @ n) * n
    Bp = g * (B - np.cross(bv, E)) - (g - 1) * (B @ n) * n
    return np.column_stack([Ep, Bp])


F = rng.normal(size=(3, 2))
tot = lambda F: np.sum(F ** 2)                   # = E^2 + B^2 = 2u
print("1. Isometrische Zeugen (Dualitaetsdrehung rechts, Raumdrehung links): C- plus A-Energie bleibt gleich")
for a in (0.4, math.pi / 2, 2.0):
    Rm = np.array([[math.cos(a), -math.sin(a)], [math.sin(a), math.cos(a)]])
    G = F @ Rm.T
    print("   a = %.3f: |FC|^2 + |FA|^2 = %.6f, |F|^2 = %.6f" % (a, tot(G @ C) + tot(G @ A), tot(F)))

print("\n2. Boosts: Gesamtenergie 2u >= |s| (Boden durch die Invariante)")
z = F[:, 0] + 1j * F[:, 1]; s = z @ z
n = np.array([0, 0, 1.])
best = min(tot(boost(F, nv / np.linalg.norm(nv), eta)) for nv in rng.normal(size=(200, 3)) for eta in np.linspace(-4, 4, 81))
print("   |s| = %.6f; kleinste Gesamtenergie ueber 16200 Boosts = %.6f (>= |s|)" % (abs(s), best))
Sv = np.cross(F[:, 0], F[:, 1]); u = 0.5 * tot(F); eta_f = 0.5 * math.atanh(np.linalg.norm(Sv) / u)
print("   im System E || B: Gesamtenergie = %.6f = |s|" % tot(boost(F, Sv / np.linalg.norm(Sv), eta_f)))

print("\n3. Nullfeld (Licht): Energie faellt beim Boost laengs der Ausbreitung wie e^(-2 eta), nie endlich null")
L = np.column_stack([[1., 0, 0], [0., 1, 0]])        # E = x, B = y, Ausbreitung +z
for eta in (0, 1, 3, 10):
    print("   eta = %4.1f: Gesamtenergie %.3e (e^-2eta * 2 = %.3e)" % (eta, tot(boost(L, n, eta)), 2 * math.exp(-2 * eta)))
