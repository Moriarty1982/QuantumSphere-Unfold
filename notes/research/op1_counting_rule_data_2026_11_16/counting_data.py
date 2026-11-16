"""H102-Grunddaten und Zaehlregel (Erkundung, nicht blind).

(1) Zaehlvarianten der Literatur als Gleichung fuer gamma:
    DL/Meissner (U(1), nur m = +-j, Gewicht 2, alle j):  sum_j 2 exp(-2 pi g sqrt(j(j+1))) = 1   (Companion: Frame M)
    GM (alle m, j >= |m|, Gewicht 2j+1):                 sum_j (2j+1) exp(-2 pi g sqrt(j(j+1))) = 1
    ABK (nur j = 1/2):                                    2 exp(-2 pi g sqrt(3)/2) = 1               (Companion: Frame T)
(2) Je gamma: H102-Beziehung phi = pi/4 - gamma/2 und daraus m_tau (rho^2 aus m_e/m_mu, wie k224).
(3) Zielphase 3 delta aus verschiedenen m_tau-Werten (PDG 2022, PDG 2024/2026, Belle II 2023, BESIII).
"""
import numpy as np
from scipy.optimize import brentq

ME, MMU = 0.51099895, 105.6583755
K3 = np.arange(3)
js = np.arange(1, 4000) / 2
a = np.sqrt(js * (js + 1))
variants = {
    "DL/Meissner (U(1), m = +-j)": lambda g: np.sum(2 * np.exp(-2 * np.pi * g * a)) - 1,
    "GM (alle m, 2j+1)": lambda g: np.sum((2 * js + 1) * np.exp(-2 * np.pi * g * a)) - 1,
    "ABK (nur j = 1/2)": lambda g: 2 * np.exp(-2 * np.pi * g * np.sqrt(3) / 2) - 1,
}


def ratios(r2, th):
    s = 1 + 2 * np.sqrt(r2) * np.cos(th + 2 * np.pi * K3 / 3)
    m = np.sort(s ** 2)
    return m / m[1]


def mtau_from_phi(phi):
    th = phi / 3
    f = lambda r: ratios(r, th)[0] - ME / MMU
    grid = np.linspace(0.30, 0.70, 4001); vals = [f(x) for x in grid]
    for i in range(len(grid) - 1):
        if np.sign(vals[i]) != np.sign(vals[i + 1]):
            r2 = brentq(f, grid[i], grid[i + 1])
            return ratios(r2, th)[2] * MMU, r2
    return float("nan"), float("nan")


print("(1)/(2) Zaehlvarianten, gamma, H102-Phase und m_tau:")
for name, f in variants.items():
    g = brentq(f, 0.01, 2.0)
    phi = np.pi / 4 - g / 2
    mt, r2 = mtau_from_phi(phi)
    print(f"   {name:30s} gamma = {g:.6f}  phi = pi/4 - gamma/2 = {phi:.6f}  m_tau = {mt:9.3f} MeV  (rho^2 = {r2:.5f})")


def three_delta(mtau):
    r = np.sqrt([ME, MMU, mtau]); F = np.fft.fft(r) / 3
    d = abs(np.angle(F[1])) % (2 * np.pi / 3)
    d = min(d, 2 * np.pi / 3 - d)
    K = (ME + MMU + mtau) / r.sum() ** 2
    return 3 * d, K


print("(3) Zielphase 3 delta und K je m_tau-Wert:")
for name, mt, s in (("PDG 2022", 1776.86, 0.12), ("PDG 2024 = PDG 2026", 1776.93, 0.09), ("Belle II 2023", 1777.09, 0.14),
                    ("BESIII 2020", 1776.91, 0.15), ("H102", 1777.134, 0.0), ("exaktes Koide", 1776.969, 0.0)):
    ph, K = three_delta(mt)
    z = (1777.134 - mt) / s if s else float("nan")
    print(f"   {name:22s} m_tau = {mt:9.3f} +- {s:.2f}: 3 delta = {ph:.6f}, K = {K:.7f}, z(H102) = {z:+.2f}")
