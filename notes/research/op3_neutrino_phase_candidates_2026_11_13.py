"""Erkundung (nicht blind): native Varianten zu H99 nach den Ideen 1-3 vom 13.11.2026.

Idee 1: andere Beziehung zwischen Neutrino- und Lepton-Phase als theta_nu = theta_e + pi/12.
Idee 2: andere Auslesung im neutralen Sektor (Masse statt Massenwurzel; Seesaw: m ~ s^4) oder K_nu != 2/3.
Idee 3: theta_e aus laufenden Massen bei M_Z statt Polmassen.
Alle Varianten werden vollstaendig ausgegeben; die Zahl der Versuche wird mitgezaehlt (look-elsewhere).
Aufruf: python op3_neutrino_phase_candidates_2026_11_13.py
"""
import numpy as np
from scipy.optimize import brentq

K3 = np.arange(3)
R_OBS, S_OBS = 0.030016, 0.000457          # NuFIT 6.1, IC24 mit SK, NO (H99b)
POL = [0.51099895, 105.6583755, 1776.93]
MZ = [2.77713e-6, 5.85042e-4, 0.99378e-2]   # r11 / k14 (Huang-Zhou 2021)


def lepton_phase(m):
    v = np.sqrt(np.array(m))
    x = v / v.mean() - 1
    A = np.sqrt(2 * (x ** 2).sum() / 3)
    return np.arccos(np.clip(4 * np.prod(x) / A ** 3, -1, 1)) / 3


def eig(theta, rho2=0.5):
    return 1 + 2 * np.sqrt(rho2) * np.cos(theta + 2 * np.pi * K3 / 3)


def R_of(theta, power, rho2=0.5):
    m = np.sort(np.abs(eig(theta, rho2)) ** power)
    return (m[1] ** 2 - m[0] ** 2) / (m[2] ** 2 - m[0] ** 2)


def boundary(rho2):
    """Rand des Bogens: det S = 1 - 3 rho^2 + 2 rho^3 cos 3theta = 0."""
    return np.arccos(np.clip((3 * rho2 - 1) / (2 * rho2 ** 1.5), -1, 1)) / 3


RELATIONS = {
    "a: th_e + pi/12 (H99)": lambda te: te + np.pi / 12,
    "b: pi/6 - th_e (Spiegelung am Rand)": lambda te: np.pi / 6 - te,
    "c: pi/3 - th_e (cos3th -> -cos3th, Tachyon c -> -c)": lambda te: np.pi / 3 - te,
    "d: det S_nu = -det S_e": lambda te: np.arccos(np.clip(np.sqrt(2) - np.cos(3 * te), -1, 1)) / 3,
}
READOUTS = {"sqrt(m) ~ s (H99)": 2, "m ~ |s|": 1, "Seesaw m ~ s^4": 4}

if __name__ == "__main__":
    th = {"Pol": lepton_phase(POL), "M_Z": lepton_phase(MZ)}
    print(f"theta_e: Pol {th['Pol']:.5f}, M_Z {th['M_Z']:.5f}; Rand bei rho^2=1/2: pi/12 = {np.pi / 12:.5f}")
    tnu = brentq(lambda x: R_of(x, 2) - R_OBS, 0.40, 0.52)
    dRdth = (R_of(tnu + 1e-6, 2) - R_of(tnu - 1e-6, 2)) / 2e-6
    print(f"Ziel (Lesart s^2, rho^2=1/2): theta_nu = {tnu:.5f} +- {S_OBS / dRdth:.5f}")
    print("\n== Raster: Beziehung x Auslesung x Skala (rho^2 = 1/2) ==")
    n, hits = 0, []
    for rn, f in RELATIONS.items():
        for on, p in READOUTS.items():
            for sn, te in th.items():
                tv = f(te)
                R = R_of(tv, p)
                z = (R - R_OBS) / S_OBS
                n += 1
                mark = "  <-- |z|<=2" if abs(z) <= 2 else ""
                if mark:
                    hits.append((rn, on, sn, z))
                print(f"{rn:52s} {on:18s} {sn:4s} theta_nu={tv:.4f} R={R:.6f} z={z:+8.2f}{mark}")
    print(f"\nVersuche: {n}; innerhalb 2 sigma: {len(hits)}")
    # Zufallserwartung: Anteil eines gleichverteilten theta in [pi/12, pi/3] (Lesart s^2), der 2 sigma trifft
    xs = np.linspace(np.pi / 12 + 1e-4, np.pi / 3 - 1e-4, 200001)
    Rs = np.array([R_of(x, 2) for x in xs[::50]])
    frac = np.mean(np.abs(Rs - R_OBS) <= 2 * S_OBS)
    print(f"Trefferwahrscheinlichkeit je zufaelligem theta_nu in [pi/12, pi/3]: {frac:.4f}; "
          f"bei {n} Versuchen mind. ein Treffer: {1 - (1 - frac) ** n:.2f}")

    print("\n== Idee 1+2 verbunden: Verschiebung = Rand des Bogens bei K_nu (rho_nu^2 frei) ==")
    for sn, te in th.items():
        g = lambda r2: R_of(te + boundary(r2), 2, r2) - R_OBS
        r2s = np.linspace(0.34, 0.99, 400)
        vals = np.array([g(r) for r in r2s])
        roots = [brentq(g, r2s[i], r2s[i + 1]) for i in range(len(r2s) - 1) if vals[i] * vals[i + 1] < 0]
        for r2 in roots:
            print(f"{sn}: rho_nu^2 = {r2:.5f}, K_nu = {(1 + 2 * r2) / 3:.5f}, Rand = {boundary(r2):.5f} (Fit, keine Vorhersage)")
    print("\n== Idee 2 allein: K_nu frei bei theta_nu = theta_e + pi/12 ==")
    for sn, te in th.items():
        g = lambda r2: R_of(te + np.pi / 12, 2, r2) - R_OBS
        r2s = np.linspace(0.34, 0.99, 400)
        vals = np.array([g(r) for r in r2s])
        roots = [brentq(g, r2s[i], r2s[i + 1]) for i in range(len(r2s) - 1) if vals[i] * vals[i + 1] < 0]
        for r2 in roots:
            print(f"{sn}: rho_nu^2 = {r2:.5f}, K_nu = {(1 + 2 * r2) / 3:.5f} (Fit, keine Vorhersage)")


def lepton_rho2(m):
    v = np.sqrt(np.array(m))
    K = (v ** 2).sum() / v.sum() ** 2
    return (3 * K - 1) / 2


if __name__ == "__main__":
    print("\n== Nachtraeglich (aus dem Fit oben gefunden): H99 konsequent bei einer Skala ==")
    print("rho_nu^2 = rho_e^2(mu), theta_nu = theta_e(mu) + Rand(rho_e^2(mu)); bei mu = Pol praktisch H99")
    for sn, m in (("Pol", POL), ("M_Z", MZ)):
        r2 = lepton_rho2(m)
        tv = lepton_phase(m) + boundary(r2)
        R = R_of(tv, 2, r2)
        for lab, ro, so in (("NuFIT 6.1", R_OBS, S_OBS), ("NuFIT 6.0", 0.029805, 0.000792)):
            print(f"{sn}: rho_e^2 = {r2:.6f} (K = {(1 + 2 * r2) / 3:.6f}), Rand = {boundary(r2):.5f}, "
                  f"theta_nu = {tv:.5f}, R = {R:.6f}; {lab}: z = {(R - ro) / so:+.2f}")
        v = eig(tv, r2)
        mm = np.sort(v ** 2)
        sc = np.sqrt(2.511e-3 / (mm[2] ** 2 - mm[0] ** 2))
        print(f"     Wurzeln {np.round(np.sort(v), 4)}, Massen (Skala aus dm31) {np.round(mm * sc * 1e3, 3)} meV, "
              f"dm21 = {R * 251.1:.3f}e-5, JUNO 7.50 +- 0.12: {(R * 251.1 - 7.50) / 0.12:+.2f} sigma")
