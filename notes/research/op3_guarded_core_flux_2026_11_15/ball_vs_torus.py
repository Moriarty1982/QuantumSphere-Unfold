"""Faden 3 (Erkundung): v470/05 schneidet eine Kugel B_eps(K) aus S^3, das Urbild einer Kappe ist ein Volltorus aus Fasern.
Hopf-Abbildung (z1, z2) -> (2 z1 conj z2, |z1|^2 - |z2|^2); K = (1, 0) liegt ueber dem Nordpol.
Fuer einen Basispunkt unter dem Polwinkel theta laeuft die Faser durch (cos(theta/2) e^{it}, sin(theta/2) e^{i(t+chi)}).
Abstand zu K: cos d = cos(theta/2) cos t. Abgeschnittener Faseranteil f(theta) = arccos(cos eps / cos(theta/2)) / pi."""
import math
import numpy as np
from scipy.integrate import quad
from scipy.optimize import brentq
G = 0.2375330

def frac(theta, eps):
    c = math.cos(eps) / math.cos(theta / 2)
    return math.acos(c) / math.pi if c < 1 else 0.0

def omega_binary(eps):           # jede angeschnittene Faser zaehlt ganz: Kappe vom Radius 2 eps
    return 2 * math.pi * (1 - math.cos(2 * eps))

def omega_weighted(eps):         # jede Faser zaehlt mit ihrem abgeschnittenen Anteil
    return quad(lambda th: frac(th, eps) * 2 * math.pi * math.sin(th), 0, min(2 * eps, math.pi), limit=200)[0]

# Kontrolle: gewichteter Raumwinkel = 4 pi * Vol(B_eps)/Vol(S^3), Vol(B_eps) = pi (2 eps - sin 2 eps), Vol(S^3) = 2 pi^2
for eps in (0.1, 0.3, 0.5):
    print(f"eps = {eps}: gewichtet {omega_weighted(eps):.6f}, Volumenformel {4*math.pi*math.pi*(2*eps-math.sin(2*eps))/(2*math.pi**2):.6f}")
# Monte-Carlo-Gegenprobe des Faseranteils
rng = np.random.default_rng(3)
z = rng.normal(size=(400000, 4)); z /= np.linalg.norm(z, axis=1)[:, None]
eps = 0.3
inball = np.arccos(np.clip(z[:, 0], -1, 1)) < eps
theta = np.arccos(np.clip(z[:, 0]**2 + z[:, 1]**2 - z[:, 2]**2 - z[:, 3]**2, -1, 1))
print(f"Monte Carlo eps = 0.3: Anteil im Ball {inball.mean():.5f}, Volumenformel {(2*eps-math.sin(2*eps))/(2*math.pi):.5f}; "
      f"groesster Basiswinkel im Ball {np.degrees(theta[inball].max()):.2f} Grad = 2 eps {np.degrees(2*eps):.2f}")
print(f"Ganz entfernte Fasern: keine fuer eps < pi (Anteil am Pol f(0) = eps/pi = {eps/math.pi:.3f})")
eb = brentq(lambda e: omega_binary(e) - G, 1e-4, 1.0)
ew = brentq(lambda e: omega_weighted(e) - G, 1e-3, 1.5)
print(f"Raumwinkel gamma_M: binaer (Kappe) eps = {eb:.6f} rad = {math.degrees(eb):.3f} Grad; "
      f"gewichtet (Volumen) eps = {ew:.6f} rad = {math.degrees(ew):.3f} Grad")
print(f"Volumen des Balls bei gewichtetem eps: Anteil an S^3 = {(2*ew-math.sin(2*ew))/(2*math.pi):.6f} = gamma_M/(4 pi) = {G/(4*math.pi):.6f}")
