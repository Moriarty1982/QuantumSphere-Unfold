"""Dimensionsleiter: Welche Regel des Regelraums S (H98) hat die groesste Moran-Dimension unter denen, die in R^d passen
(notwendig: sum g r^d <= 1), fuer d = 1, 2, 3?  Spektrum sqrt(j(j+1)), Skalen in T-Einheiten.  (Erkundung, nicht blind: fuer d = 3 und d = 1
vor der Rechnung ueberschlagen.)  Zusaetzlich: konstante ganzzahlige Kopienzahl w ueber alle Spins, groesstes w je d."""
import numpy as np
from scipy.optimize import brentq

n = np.arange(1, 400001); j = n / 2
r = 2.0 ** (-np.sqrt(n * (n + 2) / 3))
ranges = {"A (alle)": np.ones_like(j, bool), "H (halbzahlig)": (n % 2 == 1), "I (ganzzahlig)": (n % 2 == 0),
          "S1/2": (n == 1), "S1": (n == 2)}
rows = []
for rn, m in ranges.items():
    for wn, w in (("2", 2.0 + 0 * j), ("2j+1", 2 * j + 1)):
        g = w * m
        D = brentq(lambda D: np.sum(g * r ** D) - 1, 1e-3, 20)
        rows.append((rn, wn, D, [np.sum(g * r ** d) for d in (1, 2, 3)]))
print("Regel | D | sum g r^1 | sum g r^2 | sum g r^3")
for rn, wn, D, s in rows:
    print(f"{rn:15s},{wn:5s} | {D:.4f} | {s[0]:.4f} | {s[1]:.4f} | {s[2]:.4f}")
for d in (1, 2, 3):
    fit = [x for x in rows if x[3][d - 1] <= 1 + 1e-12]
    best = max(fit, key=lambda x: x[2]); D = best[2]
    ties = [f"{x[0]},{x[1]}" for x in fit if abs(x[2] - D) < 1e-9]
    print(f"d = {d}: groesste Dimension unter den passenden Regeln: D = {D:.4f}, Regel(n): {ties}")
S = [np.sum(r ** d) for d in (1, 2, 3)]
for d in (1, 2, 3):
    wmax = int(np.floor(1 / S[d - 1] + 1e-12))
    Dw = brentq(lambda D: np.sum(wmax * r ** D) - 1, 1e-3, 20) if wmax >= 1 else float('nan')
    print(f"konstante Kopienzahl ueber alle Spins, d = {d}: groesstes w = {wmax} (Grenze 1/sum r^d = {1/S[d-1]:.3f}), D = {Dw:.4f}")
