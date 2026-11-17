"""Regelraum S aus H98 (Spinbereiche A alle, H halbzahlig, I ganzzahlig, S1/2, S1; Gewichte 2, 2j+1), Spektrum sqrt(j(j+1)):
Moran-Dimension D = gamma/gamma_T und Ebenenbedingung sum g r^2 <= 1 (notwendig fuer Aehnlichkeits-IFS mit offener-Mengen-Bedingung in R^2)."""
import numpy as np
from scipy.optimize import brentq
n = np.arange(1, 400001); j = n / 2
r = 2.0 ** (-np.sqrt(n * (n + 2) / 3))
ranges = {"A": np.ones_like(j, bool), "H": (n % 2 == 1), "I": (n % 2 == 0), "S1/2": (n == 1), "S1": (n == 2)}
gT = np.log(2) / (np.pi * np.sqrt(3))
print("Regel | D = gamma/gamma_T | gamma | sum g r^2 | Ebene")
for rn, m in ranges.items():
    for wn, w in (("2", 2.0 + 0 * j), ("2j+1", 2 * j + 1)):
        g = w * m
        try:
            D = brentq(lambda D: np.sum(g * r ** D) - 1, 0.01, 20)
        except ValueError:
            print(f"{rn:5s},{wn:5s} | keine Loesung"); continue
        s2 = np.sum(g * r ** 2)
        print(f"{rn:5s},{wn:5s} | {D:.4f} | {D*gT:.6f} | {s2:.4f} | {'ja' if s2 <= 1 else 'nein'}")
