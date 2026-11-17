"""Spannung zu P: Ab welcher Register-Sichtbarkeit b passt die Registerzaehlung auf eine Flaeche?  (Erkundung, ohne Zielwert.)

Modell aus ../op1_entropy_count_2026_11_17/: 2j Straenge im Registerzustand rho(b) = (1 + b sigma_z)/2, symmetrischer Unterraum, Gewichte
p+^(j+m) p-^(j-m) (geometrisch).  Effektive Zahl je Spin N_b(j): Shannon 2^H und Beteiligung 1/sum w^2.  Dazu die Mischung mit dem Spiegel
(unbekannter Port, rho(b) und rho(-b) je halb).  Moran: D(b) aus sum N_b(j) r_j^D = 1; Flaeche: sum N_b(j) r_j^2 <= 1.
Bekannte Punkte: b = 1 (R) N = 1; b = 0 (P) N = 2j+1; Mischung bei b = 1 -> 2 (Regel von M).
"""
import numpy as np
from scipy.optimize import brentq

nmax = 400
n = np.arange(1, nmax + 1)
r = 2.0 ** (-np.sqrt(n * (n + 2) / 3))

def weights(k, b):
    pp, pm = (1 + b) / 2, (1 - b) / 2
    w = np.array([pp ** i * pm ** (k - i) for i in range(k + 1)], float)
    return w / w.sum()

def counts(b, kind, mix):
    out = []
    for k in n:
        w = weights(k, b)
        if mix: w = 0.5 * (w + w[::-1])
        w = w[w > 1e-300]
        out.append(2 ** (-np.sum(w * np.log2(w))) if kind == "Shannon" else 1 / np.sum(w ** 2))
    return np.array(out)

def area(b, kind, mix): return np.sum(counts(b, kind, mix) * r ** 2)
def dim(b, kind, mix):
    N = counts(b, kind, mix)
    return brentq(lambda D: np.sum(N * r ** D) - 1, 1e-3, 20)

bM = (1 - 0.549406 ** 2) / (1 + 0.549406 ** 2)
for mix in (False, True):
    for kind in ("Shannon", "Beteiligung"):
        lab = f"{'Mischung mit Spiegel' if mix else 'Register allein':20s} {kind:11s}"
        f = lambda b: area(b, kind, mix) - 1
        bc = brentq(f, 1e-6, 1 - 1e-9) if f(1e-6) > 0 > f(1 - 1e-9) else (float('nan'))
        print(f"{lab}: Flaeche bei b = 0: {area(0.0, kind, mix):.4f}, bei b_M: {area(bM, kind, mix):.4f}, bei b = 1: {area(1-1e-12, kind, mix):.4f}; "
              f"Schwelle b_c = {bc:.4f}; D(b_M) = {dim(bM, kind, mix):.4f}")
print(f"b_M = {bM:.4f}; zum Vergleich gamma_L = 1,8647")
