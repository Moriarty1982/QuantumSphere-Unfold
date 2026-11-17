"""Konstante ganzzahlige Kopienzahl w je Skala (alle Spins), Spektrum sqrt(j(j+1)): Dimension und Ebenenbedingung sum w r^2 <= 1.
Dazu die (nicht ganzzahlige) Kopienzahl, bei der D = 2 genau erreicht wird."""
import numpy as np
from scipy.optimize import brentq
n = np.arange(1, 400001); r = 2.0 ** (-np.sqrt(n * (n + 2) / 3))
S2 = np.sum(r ** 2)
for w in (1, 2, 3, 4):
    D = brentq(lambda D: np.sum(w * r ** D) - 1, 0.01, 20)
    print(f"w = {w}: D = {D:.4f}, sum w r^2 = {w*S2:.4f} -> {'passt in die Ebene' if w*S2 <= 1 else 'passt nicht (D > 2)'}")
print(f"D = 2 genau bei w = 1/sum r^2 = {1/S2:.4f} (nicht ganzzahlig); groesste ganzzahlige Kopienzahl in der Ebene: {int(np.floor(1/S2))}")
