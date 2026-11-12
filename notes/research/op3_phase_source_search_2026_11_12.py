"""Selbstpruefung zur Phasen-Quellensuche (12.11.2026).

Nicht blind; prueft die Aussagen der Notiz op3_phase_source_search_2026_11_12.md:
rho wirkt als delta -> -delta, e3 ~ cos(3 delta), Vandermonde ~ sin(3 delta),
und ein rho-ungerader Zusatz legt die Phase ueber tan(3 delta) fest.
Aufruf: python op3_phase_source_search_2026_11_12.py
"""
import numpy as np
from scipy.optimize import minimize

B = np.array([[1, -1, 0], [1, 1, -2]]).T / np.array([np.sqrt(2), np.sqrt(6)])
k = np.arange(3)


def x_of(A, d):
    return A * np.cos(d + 2 * np.pi * k / 3)


def e3(x):
    return np.prod(x)


def vdm(x):
    return (x[0] - x[1]) * (x[1] - x[2]) * (x[2] - x[0])


def identities():
    rng = np.random.default_rng(3)
    err = 0.0
    for _ in range(1000):
        A, d = rng.uniform(0.1, 2), rng.uniform(-np.pi, np.pi)
        x = x_of(A, d)
        err = max(err,
                  abs(e3(x) - A ** 3 * np.cos(3 * d) / 4),
                  abs(abs(vdm(x)) - 3 * np.sqrt(3) / 4 * A ** 3 * abs(np.sin(3 * d))),
                  # rho: Tausch der Plaetze 1 und 2 ist delta -> -delta
                  np.abs(x[[0, 2, 1]] - x_of(A, -d)).max(),
                  abs(vdm(x[[0, 2, 1]]) + vdm(x)), abs(vdm(x[[1, 2, 0]]) - vdm(x)))
    return err


def phase_from_odd_term(kappa, chi, v=1 / np.sqrt(6), lam=1.0):
    """E = Quartik (flach in delta) + kappa*e3 + chi*Vandermonde auf Summe x = 0."""
    sgn = np.sign(vdm(x_of(1.0, 0.1)))            # Vorzeichenkonvention des Vandermonde

    def E(y):
        x = B @ y
        return (lam / 4 * (x ** 2 - v ** 2) ** 2).sum() + kappa * e3(x) + chi * vdm(x)

    best = min((minimize(E, y0, tol=1e-15) for y0 in
                np.random.default_rng(4).uniform(-0.6, 0.6, (40, 2))), key=lambda r: r.fun)
    x = B @ best.x
    A = np.sqrt(2 * (x ** 2).sum() / 3)
    c3, s3 = 4 * e3(x) / A ** 3, sgn * vdm(x) / (3 * np.sqrt(3) / 4 * A ** 3)
    pred = np.arctan2(-sgn * 3 * np.sqrt(3) * chi, -kappa)   # Minimum von kappa*cos + 3 sqrt3 chi sgn*sin
    return np.arctan2(s3, c3), pred


def lepton():
    m = np.array([0.51099895, 105.6583755, 1776.86])
    s = np.sqrt(m)
    x = s / s.mean() - 1
    A = np.sqrt(2 * (x ** 2).sum() / 3)
    c3 = 4 * e3(x) / A ** 3
    return c3, np.sqrt(1 - c3 ** 2) / c3


if __name__ == "__main__":
    print(f"Identitaeten (e3, Vandermonde, rho, tau): groesster Fehler {identities():.1e}")
    for kappa, chi in ((-0.05, 0.0), (-0.05, 0.004), (-0.05, -0.00757)):
        got, pred = phase_from_odd_term(kappa, chi)
        print(f"kappa = {kappa}, chi = {chi}: 3 delta = {got:+.6f}, Formel {pred:+.6f}")
    c3, t3 = lepton()
    print(f"Leptonen: cos 3delta = {c3:.6f}, |tan 3delta| = {t3:.6f}, |chi/kappa| = {t3 / (3 * np.sqrt(3)):.6f}")
    g = np.array([np.log(2) / (np.pi * np.sqrt(3)), 0.237533])
    g = np.append(g, -g.sum())
    A = np.sqrt(2 * (g ** 2).sum() / 3)
    print(f"Nachtraeglich, gamma-Tripel (Summe null per Definition): cos 3delta = {4 * e3(g) / A ** 3:.4f}")
