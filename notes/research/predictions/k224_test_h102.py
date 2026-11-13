"""k224: Test H102 (Vorab_Notiz_H102_Tau_Masse_aus_gamma.md).

Beziehung: Fluss der geladenen Leptonen Phi_e = 3 theta_e = pi/4 - gamma_M/2, gamma_M = 0.237533 (Zaehlregel des Materie-Frames).
theta fest, rho^2 aus m_e/m_mu, Vorhersage m_tau.  Vergleich: exaktes Koide (rho^2 = 1/2) aus m_e, m_mu.
Aufruf ohne Argumente: nur Vorhersage.  Mit Daten:  python k224_test_h102.py m_tau sigma   (MeV)
"""
import sys
import numpy as np
from scipy.optimize import brentq

ME, SME = 0.51099895, 0.00000000015
MMU, SMMU = 105.6583755, 0.0000023
K3 = np.arange(3)


def gamma_M():
    js = np.arange(1, 2000) / 2
    a = np.sqrt(js * (js + 1))
    return brentq(lambda g: np.sum(2 * np.exp(-2 * np.pi * g * a)) - 1, 0.05, 1.0)


def ratios(r2, th):
    s = 1 + 2 * np.sqrt(r2) * np.cos(th + 2 * np.pi * K3 / 3)
    m = np.sort(s ** 2)
    return m / m[1]


def mtau_pred(me, mmu, th):
    r2 = brentq(lambda r: ratios(r, th)[0] - me / mmu, 0.49, 0.52)
    return ratios(r2, th)[2] * mmu, r2


def mtau_koide(me, mmu):
    th = brentq(lambda t: ratios(0.5, t)[0] - me / mmu, 0.15, 0.26)
    return ratios(0.5, th)[2] * mmu


if __name__ == "__main__":
    g = gamma_M()
    th = (np.pi / 4 - g / 2) / 3
    mt, r2 = mtau_pred(ME, MMU, th)
    # Unsicherheit der Vorhersage aus m_e und m_mu
    d1 = abs(mtau_pred(ME + SME, MMU, th)[0] - mt)
    d2 = abs(mtau_pred(ME, MMU + SMMU, th)[0] - mt)
    sp = np.hypot(d1, d2)
    mk = mtau_koide(ME, MMU)
    print(f"gamma_M = {g:.6f}; theta = {th:.7f}; rho^2 = {r2:.7f}")
    print(f"m_tau (H102) = {mt:.3f} +- {sp:.3f} MeV;  m_tau (exaktes Koide) = {mk:.3f} MeV")
    if len(sys.argv) == 3:
        obs, so = map(float, sys.argv[1:])
        z = (mt - obs) / np.hypot(so, sp)
        zk = (mk - obs) / so
        print(f"Daten: {obs:.3f} +- {so:.3f} MeV;  z(H102) = {z:+.2f}  ->  {'bestaetigt (vertraeglich)' if abs(z) <= 2 else 'widerlegt'}")
        print(f"         z(Koide exakt) = {zk:+.2f};  trennend gegen Koide: {abs(z) <= 2 and abs(zk) > 2}")
