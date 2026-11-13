"""k221: Test H99 (Vorab-Notiz Vorab_Notiz_H99_Neutrino_Phase_Bogenrand.md, Commit 5b23c5a).

Neutrino-Phase = Lepton-Phase + pi/12 bei r = 1; vorhergesagt wird R = dm21/dm31 (normale Ordnung).
Aufruf: python k221_test_h99.py [dm21 sig21 dm31 sig31]   (optionale Daten fuer H99b, in eV^2)
"""
import sys
import numpy as np

ME, MMU, MTAU, SIG_TAU = 0.51099895, 105.6583755, 1776.93, 0.09
DM21, S21, DM31, S31 = 7.49e-5, 0.19e-5, 2.513e-3, 0.020e-3      # NuFIT 6.0, wie H2 (asymmetrischer Fehler gemittelt)
k = np.arange(3)


def lepton_phase(mtau):
    v = np.sqrt(np.array([ME, MMU, mtau]))
    t = v.mean()
    x = v / t - 1
    A = np.sqrt(2 * (x ** 2).sum() / 3)
    th = np.arccos(np.clip(4 * np.prod(x) / A ** 3, -1, 1)) / 3
    return t, A, th


def triole(t, A, th):
    return t * (1 + A * np.cos(th + 2 * np.pi * k / 3))


def ratio(theta_nu):
    v = triole(1.0, np.sqrt(2), theta_nu)
    m = np.sort(v ** 2)
    a, b, c = m
    return (b ** 2 - a ** 2) / (c ** 2 - a ** 2), v, m


def decide(name, dm21, s21, dm31, s31, R, sig_pred):
    Robs = dm21 / dm31
    sR = Robs * np.hypot(s21 / dm21, s31 / dm31)
    stot = np.hypot(sR, sig_pred)
    dev = (R - Robs) / stot
    print(f"{name}: R_obs = {Robs:.6f} +- {sR:.6f}; Abweichung {R - Robs:+.6f} = {dev:+.2f} sigma_tot"
          f" -> {'bestaetigt (vertraeglich)' if abs(dev) <= 2 else 'widerlegt'}")
    return dev


if __name__ == "__main__":
    t, A, th_e = lepton_phase(MTAU)
    rec = np.sort(triole(t, A, th_e) ** 2)
    c2 = abs(rec - np.sort([ME, MMU, MTAU])) / np.sort([ME, MMU, MTAU])
    th_nu = th_e + np.pi / 12
    R, v, m = ratio(th_nu)
    K = (v ** 2).sum() / v.sum() ** 2
    dR = (ratio(lepton_phase(MTAU + SIG_TAU)[2] + np.pi / 12)[0] - ratio(lepton_phase(MTAU - SIG_TAU)[2] + np.pi / 12)[0]) / 2
    print(f"theta_e = {th_e:.7f}, A = {A:.7f}; theta_nu = {th_nu:.7f}")
    print(f"Kontrolle 1: K - 2/3 = {K - 2 / 3:.1e}")
    print(f"Kontrolle 2: Leptonmassen zurueckgewonnen, groesster relativer Fehler {c2.max():.1e}")
    print(f"Kontrolle 3: Wurzeln {np.round(np.sort(v), 6)} -> leichteste negativ: {np.sort(np.abs(v))[0] == abs(v.min()) and v.min() < 0}")
    print(f"R_pred = {R:.6f} +- {abs(dR):.6f} (aus m_tau)")
    decide("H99a (NuFIT 6.0)", DM21, S21, DM31, S31, R, abs(dR))
    if len(sys.argv) == 5:
        d21, s21, d31, s31 = map(float, sys.argv[1:])
        decide("H99b (NuFIT 6.1)", d21, s21, d31, s31, R, abs(dR))
    # abgeleitet, nicht Teil des Kriteriums: Skala aus dm31
    scale = np.sqrt(DM31 / (m[2] ** 2 - m[0] ** 2))
    mm = m * scale
    print(f"abgeleitet (Skala aus dm31, nicht Teil des Kriteriums): Massen {np.round(mm * 1e3, 3)} meV, Summe {mm.sum():.5f} eV")
    # nachtraeglich: Variante mit -pi/12
    Rm, vm, _ = ratio(th_e - np.pi / 12)
    print(f"nachtraeglich: theta_e - pi/12 gibt R = {Rm:.6f}, Wurzeln {np.round(np.sort(vm), 4)}")
