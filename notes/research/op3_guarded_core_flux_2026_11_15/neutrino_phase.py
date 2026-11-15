"""Faden 2 (Erkundung): Lage der Neutrino-Triole aus H99 im Bild der Gram-Determinante.
H99: theta_nu = theta_e + pi/12 je Generation, also Bargmann-Phase phi = 3 theta: phi_nu = phi_e + pi/4."""
import math
me, mmu, mtau = 0.51099895, 105.6583755, 1776.93
x = [math.sqrt(m) for m in (me, mmu, mtau)]
A = sum(x) / 3
c3 = 4 * x[0] * x[1] * x[2] / A ** 3 - 3 + 0  # Platzhalter, unten direkt aus der Brannen-Form
# Brannen: x_k = A (1 + sqrt2 cos(theta + 2 pi k/3)); bestimme theta_e durch Anpassung
from scipy.optimize import brentq
def resid(th):
    v = sorted(A * (1 + math.sqrt(2) * math.cos(th + 2 * math.pi * k / 3)) for k in range(3))
    return v[0] - x[0]
th_e = brentq(resid, 0.1, 0.3)
G = 0.2375330
for name, phi in (("geladene Leptonen phi_e = 3 theta_e", 3 * th_e), ("Oktant", math.pi / 4),
                  ("H102: pi/4 - gamma_M/2", math.pi / 4 - G / 2), ("Neutrinos H99: phi_e + pi/4", 3 * th_e + math.pi / 4)):
    det = (math.sqrt(2) * math.cos(phi) - 1) / 2
    print(f"{name:38s} phi = {phi:.6f}  det G = {det:+.6f}  ({'definit, drei positive Wurzeln' if det > 1e-12 else 'Rand' if abs(det) < 1e-9 else 'indefinit, eine negative Wurzel'})")
print(f"theta_e = {th_e:.6f}; Raumwinkel 2 phi: Elektronen {2*3*th_e:.5f} = pi/2 - {math.pi/2 - 6*th_e:.5f}, Neutrinos {2*(3*th_e+math.pi/4):.5f} = pi - {math.pi - 2*(3*th_e + math.pi/4):.5f}")
