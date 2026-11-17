"""Kandidatenliste_1_2925.md abarbeiten: omega/T_H fuer jede Kandidatenfrequenz gegen das Ziel gamma_L ln2.  (Erkundung, nicht blind.)"""
import numpy as np
from scipy.optimize import brentq
from scipy.special import zeta

gL = 1.864700
target = gL * np.log(2)
K = 8 * np.pi                      # omega/T_H = 8 pi M omega
eta = 0.5 * np.arccosh(gL)
x_e = brentq(lambda x: 3 * (1 - np.exp(-x)) - x, 1, 5)    # Max. Energie pro d omega: x^3/(e^x-1)
x_n = brentq(lambda x: 2 * (1 - np.exp(-x)) - x, 0.5, 5)  # Max. Photonenzahl pro d omega: x^2/(e^x-1)
cands = [
    ("1 QNM asymptotisch gravitativ: ln 3", np.log(3)),
    ("2 Bekenstein-Bit: ln 2", np.log(2)),
    ("2 Halbschritt (j+1/2): ln 4", np.log(4)),
    ("3 Polychronakos: ln((3+sqrt5)/2)", np.log((3 + np.sqrt(5)) / 2)),
    ("4 Maggiore: 2 pi", 2 * np.pi),
    ("5 QNM Grundton Skalar l=0 (0,11046)", K * 0.11046),
    ("5 QNM Grundton Skalar l=1 (0,29294)", K * 0.29294),
    ("5 QNM Grundton EM l=1 (0,24826)", K * 0.24826),
    ("5 QNM Grundton grav l=2 (0,37367)", K * 0.37367),
    ("5 QNM Grundton grav l=3 (0,59944)", K * 0.59944),
    ("6 Photonring 1/(3 sqrt3 M)", K / (3 * np.sqrt(3))),
    ("7 Planck: Max. Energie pro d omega", x_e),
    ("7 Planck: Max. Photonenzahl pro d omega", x_n),
    ("7 Planck: mittlere Photonenenergie", np.pi ** 4 / (30 * zeta(3))),
    ("8 Bestand: 2 eta (gamma_L = cosh 2 eta)", 2 * eta),
    ("8 Bestand: eta", eta),
]
print(f"Ziel omega_M/T_H = gamma_L ln2 = {target:.5f}; Treffer: relative Abweichung <= 1e-3")
hits = 0
for n, v in cands:
    r = abs(v - target) / target
    hits += r <= 1e-3
    print(f"  {n:42s} {v:9.5f}  rel. Abstand {r:.3f}  {'TREFFER' if r <= 1e-3 else ''}")
best = min(cands, key=lambda c: abs(c[1] - target))
print(f"Treffer: {hits} von {len(cands)}; naechster Kandidat: {best[0]} ({best[1]:.5f}, {abs(best[1]-target)/target:.3f})")
