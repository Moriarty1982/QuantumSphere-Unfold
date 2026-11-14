"""Erkundung (nicht blind): Herleitung von gamma_M als Winkel, Schritt 3 fuer CT-001/CT-002 (14.11.2026).

(1) Zaehlregel (r09/r10, Frame M): sum_j g(j) exp(-2 pi gamma a(j)) = 1, alle Spins, g = 2 -> gamma_M.
    In der Sektorlesart (A_j = r_j^2 theta / 2, r_j^2 = 16 pi a(j)) ist das eine Gleichung fuer den Oeffnungswinkel theta:
    sum_j 2 exp(-A_j(theta)/4) = 1. Wurzel = gamma_M?
(2) r10.1 (Frodden-Ghosh-Perez, Unruh): E_j = gamma a(j)/l, beta = 2 pi l. Euklidisch: entlang des Kreises vom Radius l ist
    die aeussere Kruemmung K = 1/l, also kappa = int K ds = phi (euklidischer Drehwinkel). Die gamma K-Holonomie fuer
    Spingewicht w ueber den Winkel phi ist gamma w phi. Fuer phi = 2 pi und w = a(j): 2 pi gamma a(j) = Boltzmann-Exponent?
(3) Lepton-Fluss: gamma/2 = gamma w kappa mit w = |m| = 1/2 und kappa = 1 rad, oder w = a(1/2) und kappa = 1/sqrt3 rad.
    Verlangt (Massen): Delta Phi = 0.118724 +- 0.000019.
Aufruf: python ct002_gamma_angle_2026_11_14.py
"""
import numpy as np
from scipy.optimize import brentq

GAMMA_M = 0.237533
JS = np.arange(1, 4001) / 2.0          # j = 1/2, 1, 3/2, ...


def a(j):
    return np.sqrt(j * (j + 1))


def counting(gamma):
    return np.sum(2 * np.exp(-2 * np.pi * gamma * a(JS))) - 1


def sector_counting(theta):
    r2 = 16 * np.pi * a(JS)
    A = r2 * theta / 2
    return np.sum(2 * np.exp(-A / 4)) - 1


if __name__ == "__main__":
    g = brentq(counting, 0.05, 1.0, xtol=1e-14)
    t = brentq(sector_counting, 0.05, 1.0, xtol=1e-14)
    print(f"(1) Zaehlregel (alle Spins, g = 2): gamma = {g:.6f} (gamma_M = {GAMMA_M}); "
          f"Sektor-Gleichung fuer den Oeffnungswinkel: theta = {t:.6f}; gleich: {abs(g - t) < 1e-12}")
    print("    -> In der Sektorlesart ist gamma_M der Oeffnungswinkel, bei dem die Punktierungssektoren r_j^2 = 16 pi a(j)"
          " die Boltzmann-Summe 1 haben (Umformung, keine neue Information).")
    l = 2.7
    for j in (0.5, 1.0):
        E = g * a(j) / l; beta = 2 * np.pi * l
        hol = g * a(j) * (1 / l) * (2 * np.pi * l)       # gamma * w * int K ds, w = a(j), Kreis vom Radius l, voller Umlauf
        print(f"(2) j = {j}: E beta = {E * beta:.6f}, gamma-K-Holonomie (w = a(j), voller euklidischer Umlauf) = {hol:.6f}, "
              f"gleich: {abs(E * beta - hol) < 1e-12}")
    print("    -> Der Boltzmann-Exponent der Zaehlregel ist die gamma-K-Phase eines vollen euklidischen Umlaufs (Lesart).")
    need, s = 0.118724, 0.000019
    print("(3) Lepton-Fluss als gamma-K-Phase gamma * w * kappa:")
    for w, wname in ((0.5, "|m| = 1/2"), (a(0.5), "a(1/2) = sqrt3/2")):
        kappa = need / (g * w)
        print(f"    w = {wname:16s}: verlangtes kappa = {kappa:.5f} rad (+- {s / (g * w):.5f}); "
              f"bei kappa = 1 rad: Phase {g * w:.6f}")
    print(f"    Kandidat kappa = 1/sqrt3 rad mit w = a(1/2): Phase {g * a(0.5) / np.sqrt(3):.6f} (= gamma/2, identisch, da a(1/2) = sqrt3/2)")
