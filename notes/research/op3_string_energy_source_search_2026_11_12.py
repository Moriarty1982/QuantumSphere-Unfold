"""Selbstpruefung zur Quellensuche W-b (12.11.2026): kubische Kraft und Brannen-Form.

Nicht blind; prueft die analytischen Aussagen der Notiz
op3_string_energy_source_search_2026_11_12.md.
Aufruf: python op3_string_energy_source_search_2026_11_12.py
"""
import numpy as np
from scipy.optimize import minimize

L = 1.0
B = np.array([[1, -1, 0], [1, 1, -2]]).T / np.array([np.sqrt(2), np.sqrt(6)])


def lengths(theta, v, l0=L / 3):
    return l0 + 2 * v / np.sqrt(3) * np.cos(theta + 2 * np.pi * np.arange(3) / 3)


def quartic_circle(v=L / np.sqrt(6), lam=1.0):
    """U = lam/4 ((l-L/3)^2 - v^2)^2: Kreis von Gleichgewichten, K = 1/3 + 2 v^2/L^2."""
    U = lambda l: lam / 4 * ((l - L / 3) ** 2 - v ** 2) ** 2
    F = lambda l: lam * (l - L / 3) * ((l - L / 3) ** 2 - v ** 2)
    dF = lambda l: lam * (3 * (l - L / 3) ** 2 - v ** 2)
    out = []
    for th in np.linspace(0.01, np.pi / 12, 6):
        l = lengths(th, v)
        hess = np.linalg.eigvalsh(B.T @ np.diag(dF(l)) @ B)
        out.append((np.ptp(F(l)), abs(l.sum() - L), (l ** 2).sum() / L ** 2, U(l).sum(), hess))
    spread = max(o[0] for o in out)
    sumerr = max(o[1] for o in out)
    Ks = np.array([o[2] for o in out])
    Es = np.array([o[3] for o in out])
    hs = np.array([o[4] for o in out])
    return spread, sumerr, Ks, np.ptp(Es), hs, 2 * lam * v ** 2


def off_centre(l0=0.30, v=L / np.sqrt(6), lam=1.0):
    """Topf nicht bei L/3: Minimierung liefert zwei gleiche Laengen."""
    U = lambda l: lam / 4 * ((l - l0) ** 2 - v ** 2) ** 2
    best = []
    rng = np.random.default_rng(1)
    for _ in range(200):
        y0 = rng.uniform(-0.6, 0.6, 2)
        r = minimize(lambda y: U(L / 3 + B @ y).sum(), y0, tol=1e-14)
        l = np.sort(L / 3 + B @ r.x)
        best.append(min(l[1] - l[0], l[2] - l[1]))
    return max(best)


def higher_terms(e5, e6, v=L / np.sqrt(6), lam=1.0):
    """Zusaetze e5*x^5 + e6*x^6 (e6 > 0) heben die flache Richtung auf.

    Rueckgabe: gefundene Werte von cos(3 theta) und K in den Minima.
    """
    U = lambda l: (lam / 4 * ((l - L / 3) ** 2 - v ** 2) ** 2
                   + e5 * (l - L / 3) ** 5 + e6 * (l - L / 3) ** 6)
    found = set()
    rng = np.random.default_rng(2)
    for _ in range(60):
        r = minimize(lambda y: U(L / 3 + B @ y).sum(), rng.uniform(-0.4, 0.4, 2), tol=1e-14)
        x = B @ r.x
        A = np.sqrt(2 * (x ** 2).sum() / 3)
        found.add((round(float(np.clip(4 * np.prod(x) / A ** 3, -1, 1)), 4),
                   round(float(((L / 3 + x) ** 2).sum() / L ** 2), 4)))
    return sorted(found)


def lepton_phase():
    m = np.array([0.51099895, 105.6583755, 1776.86])
    s = np.sqrt(m)
    a = s.mean()
    x = (s - a) / a
    A = np.sqrt(2 * (x ** 2).sum() / 3)
    cos3 = 4 * np.prod(x) / A ** 3
    return A, np.arccos(cos3) / 3, cos3


if __name__ == "__main__":
    spread, sumerr, Ks, dE, hs, rad = quartic_circle()
    print(f"Quartik, v = L/sqrt(6): Kraftdifferenz {spread:.1e}, Summenfehler {sumerr:.1e}")
    print(f"  K auf dem Kreis: {Ks.min():.12f} .. {Ks.max():.12f}; Energieschwankung {dE:.1e}")
    print(f"  Hesse-Eigenwerte: flach {np.abs(hs[:, 0]).max():.1e}, radial {hs[:, 1].min():.6f} (Formel 2 lam v^2 = {rad:.6f})")
    print(f"Topf neben L/3: groesster kleinster Laengenabstand in 200 Minimierungen = {off_centre():.1e}")
    for e5, e6 in ((0.0, 0.5), (0.04, 0.5), (0.3, 0.5)):
        print(f"Zusatz e5 = {e5}, e6 = {e6}: Minima (cos 3theta, K) = {higher_terms(e5, e6)}")
    A, th, c3 = lepton_phase()
    print(f"Leptonen: Amplitude {A:.6f} (sqrt2 = {np.sqrt(2):.6f}), theta = {th:.6f} rad, cos 3theta = {c3:.6f}; Rand pi/12 = {np.pi/12:.6f}")
    print(f"Feder-Satz 1:1:3 -> K = {(1 + 1 + 9) / 25:.4f}")
