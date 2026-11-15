"""Erkundung (nicht blind): Der Kern auf der Generationskugel als Schatten eines Horizonts (Idee des Autors, 15.11.2026).
(1) Schwarzschild-Schatten nach Synge: sin^2 alpha = 27 (M/r)^2 (1 - 2M/r) fuer einen statischen Beobachter bei r.
(2) Flacher Schatten einer Flaeche A im Abstand d: Omega ~ A/d^2; Sektorlesart von CT-001: A/r^2 = gamma/2.
(3) Ladung q pro Steradiant: Phasendefizit = q * Omega. Spin 1/2: q = 1/2; Vektor (Spin 1): q = 1.
Aufruf: python shadow.py"""
import math
from scipy.optimize import brentq
G = 0.2375330
TARGET = math.pi / 4 - 2 / 3          # verlangtes Phasendefizit der geladenen Leptonen (Brannen 2/9)
def omega_synge(x):                    # x = r/M
    s2 = 27 * (1 - 2 / x) / x ** 2
    return 2 * math.pi * (1 - math.sqrt(1 - s2)), math.degrees(math.asin(math.sqrt(s2)))
print(f"verlangtes Defizit pi/4 - 2/3 = {TARGET:.6f}; gamma_M/2 = {G/2:.6f}")
print("(1) Schwarzschild-Schatten:")
for name, x in (("Photonensphaere 3M", 3.000001), ("ISCO 6M", 6.0), ("Frame-Versatz 2/beta^2", 2 / ((1.8647 - 1) / (1.8647 + 1))), ("10M", 10.0), ("18M", 18.0)):
    om, al = omega_synge(x)
    print(f"    {name:24s} r/M = {x:8.3f}: alpha = {al:6.2f} Grad, Omega = {om:.5f} sr")
x = brentq(lambda x: omega_synge(x)[0] - G, 3.5, 1000)
print(f"    Omega = gamma_M bei r/M = {x:.4f} (= {x/2:.4f} r_s); kein ausgezeichneter Abstand")
print("(2)+(3) flacher Schatten mit der Sektorlesart A/r^2 = gamma/2:")
for q, name in ((0.5, "Spin 1/2 (q = 1/2)"), (1.0, "Vektor (q = 1)")):
    print(f"    {name:20s}: Defizit = q * gamma/2 = {q*G/2:.6f}  (verlangt {TARGET:.6f})")
print("    -> mit Ladung 1 trifft die Sektorlesart; mit Spin 1/2 braucht der Schatten Omega = gamma (Kappenbild)")
