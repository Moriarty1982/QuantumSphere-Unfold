"""Empfindlichkeit von gamma (DL-Zaehlung, Gewicht 2 je j) auf die Ordnung des Flaechenspektrums (EPRL: sqrt(j(j+1)), j oder j + 1/2).
Nur Grunddaten-Empfindlichkeit, kein Test: zeigt, wie stark die H102-Beziehung phi = pi/4 - gamma/2 an der Spektrumsform haengt."""
import numpy as np
from scipy.optimize import brentq
js = np.arange(1, 4000) / 2
for name, a in (("sqrt(j(j+1))", np.sqrt(js * (js + 1))), ("j", js), ("j + 1/2", js + 0.5)):
    g = brentq(lambda g: np.sum(2 * np.exp(-2 * np.pi * g * a)) - 1, 0.01, 2)
    print(f"a(j) = {name:13s}: gamma = {g:.6f}, pi/4 - gamma/2 = {np.pi/4 - g/2:.6f}")
