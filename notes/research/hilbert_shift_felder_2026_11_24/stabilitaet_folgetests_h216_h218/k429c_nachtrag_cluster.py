"""k429c (Nachtrag zu H216, nachtraeglich, nicht vorab festgelegt): Woher kommt der Ueberschuss N_inv(beta_sym) = 240?

Diagnose 1: Fixpunkte, die mit dem Fixpunkt x_E von E zusammenfallen (|x - x_E| < 1e-9), aus dem Katalog nehmen
            und Zaehlung samt Kontrollen wiederholen.
Diagnose 2: verschiedene Fixpunktwerte zaehlen (auf 1e-9 gerundet) statt Woerter.
Liest k429_katalog.npz (von k429_test_h216.py erzeugt).
"""
import os
import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
z = np.load(os.path.join(HERE, "k429_katalog.npz"))
W, X, D = z["W"], z["X"], z["D"]
REL = 6.5e-4
BETA = 0.549405640974529
XE = 0.5493154519200
rep = np.abs(D) > 1 + 1e-9
att = np.abs(D) < 1 - 1e-9
ctrl = np.random.default_rng(215).uniform(0.35, 0.75, 2000)


def N_words(x0, mask):
    m = mask & (np.abs(X - x0) <= REL * x0) & (W != "E")
    return len(set(W[m]))


def N_vals(x0, mask):
    m = mask & (np.abs(X - x0) <= REL * x0) & (W != "E")
    return len(set(np.round(X[m], 9)))


inE = np.abs(X - XE) < 1e-9
print("Woerter mit Fixpunkt x_E (abstossend):", len(set(W[rep & inE])), " (anziehend):", len(set(W[att & inE])))
for title, mask, f in (("Umkehr, Woerter, ohne x_E-Cluster", rep & ~inE, N_words),
                       ("Umkehr, verschiedene Fixpunktwerte", rep, N_vals),
                       ("Umkehr, verschiedene Werte, ohne x_E", rep & ~inE, N_vals),
                       ("Vorwaerts, verschiedene Fixpunktwerte", att, N_vals)):
    nb = f(BETA, mask)
    nc = np.array([f(x, mask) for x in ctrl])
    p95, p99 = np.percentile(nc, [95, 99])
    print(f"{title}: N(beta_sym) = {nb}; Kontrollen Median {np.median(nc):.0f}, 95. P. {p95:.1f}, 99. P. {p99:.1f}; "
          f"Anteil >= {np.mean(nc >= nb):.4f}")
