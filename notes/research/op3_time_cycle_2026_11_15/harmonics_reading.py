"""Kontrolle zur Lesart: Gewichte des Zeitzyklus = normierte Massenwurzeln (Erkundung, nicht blind).

(1) p_k = sqrt(m_k)/sum sqrt(m) fuer die Leptonen (PDG 2024) gegen die rueckwaerts bestimmten Gewichte.
(2) |<psi|U psi>|^2 = (3 sum p^2 - 1)/2; Koide K = sum p^2.
(3) Flacher Grenzfall phi = pi/4 (delta = pi/12): p- = 0. Allgemein p- = (1 - sqrt2 sin(delta + pi/6))/3; fuer kleine
    Biegung p- ~ (pi/4 - phi)/9.
(4) s(t) eines reellen (kohaerenten) Feldes: sum p^2 = 1/2 (Parseval) bzw. 3/8 (Hilbert-Schmidt).
"""
import numpy as np

W3 = np.exp(2j * np.pi / 3)
m = np.array([0.51099895, 105.6583755, 1776.86])
q = np.sqrt(m) / np.sqrt(m).sum()
print(f"(1) sqrt(m)/sum sqrt(m): e {q[0]:.6f}, mu {q[1]:.6f}, tau {q[2]:.6f}")
d = 2 / 9
p0 = (1 + np.sqrt(2) * np.cos(d)) / 3; pp = (1 - p0 + np.sqrt(2 / 3) * np.sin(d)) / 2; pm = (1 - p0 - np.sqrt(2 / 3) * np.sin(d)) / 2
print(f"    Gewichte aus Koide und phi = 2/3: p- {pm:.6f}, p+ {pp:.6f}, p0 {p0:.6f}")
rng = np.random.default_rng(9)
dev = 0
for _ in range(1000):
    p = rng.dirichlet([1, 1, 1]); g = p[1] + p[0] / W3 + p[2] * W3
    dev = max(dev, abs(abs(g) ** 2 - (3 * np.sum(p ** 2) - 1) / 2))
print(f"(2) |<psi|U psi>|^2 = (3 sum p^2 - 1)/2 auf 1000 Zufallsgewichten: max. Abweichung {dev:.1e};"
      f" Leptonen: sum p^2 = {np.sum(q**2):.6f} = K")
for phi in (np.pi / 4, 0.7, 2 / 3, 0.6):
    dl = phi / 3; pmin = (1 - np.sqrt(2) * np.sin(dl + np.pi / 6)) / 3
    print(f"(3) phi = {phi:.6f}: p- = {pmin:.6f}, (pi/4 - phi)/9 = {(np.pi/4 - phi)/9:.6f}")
print(f"(4) reelles Feld: Parseval (1,4,1)/6 -> sum p^2 = {np.sum((np.array([1,4,1])/6)**2):.4f};"
      f" Hilbert-Schmidt (1,2,1)/4 -> {np.sum((np.array([1,2,1])/4)**2):.4f}")
