"""k222: Test H100 (Vorab-Notiz Vorab_Notiz_H100_Neutrino_Verhaeltnis_naechster_Fit.md).

Drei festgeschriebene Vorhersagen fuer R = dm21/dm31 (normale Ordnung):
  A  H99, Polmassen:                   theta_nu = theta_e + pi/12, rho^2 = 1/2
  B  eine Skala (Kopplungsseite, M_Z):  rho_nu^2 = rho_e^2(M_Z), theta_nu = theta_e(M_Z) + Rand(rho_e^2(M_Z))
  C  Sumino, c = 1, PMNS-gemittelt:     Struktur A, Neutrinomassen mal exp(-sum_i |U_ik|^2 ln Q_i), alpha(m_tau)
Aufruf ohne Argumente: nur Vorhersagen.  Mit Daten:  python k222_test_h100.py dm21 sig21 dm31 sig31   (eV^2)
"""
import sys
import numpy as np

K3 = np.arange(3)
POL = np.array([0.51099895, 105.6583755, 1776.93])                 # MeV
MZ = np.array([2.77713e-6, 5.85042e-4, 0.99378e-2])                # MSbar-Yukawas bei M_Z (r11, Antusch-Hinze-Saad)
PMNS_DEG = (33.76, 43.29, 8.62, 212.0)                             # NuFIT 6.1, IC24 mit SK, NO (festgeschrieben)
ALPHA_MTAU = 1 / 133.47
SIG_PRED = {"A": 1e-6, "B": 3e-5, "C": 2e-5}                       # Spannweiten der Rechenwahl, siehe Vorab-Notiz


def phase_and_rho2(m):
    v = np.sqrt(m)
    x = v / v.mean() - 1
    A = np.sqrt(2 * (x ** 2).sum() / 3)
    th = np.arccos(np.clip(4 * np.prod(x) / A ** 3, -1, 1)) / 3
    K = (v ** 2).sum() / v.sum() ** 2
    return th, (3 * K - 1) / 2


def boundary(r2):
    return np.arccos(np.clip((3 * r2 - 1) / (2 * r2 ** 1.5), -1, 1)) / 3


def roots(theta, r2):
    return 1 + 2 * np.sqrt(r2) * np.cos(theta + 2 * np.pi * K3 / 3)


def ratio(m):
    m = np.sort(np.abs(m))
    return (m[1] ** 2 - m[0] ** 2) / (m[2] ** 2 - m[0] ** 2)


def pmns(t12, t23, t13, d):
    s12, c12, s23, c23, s13, c13 = np.sin(t12), np.cos(t12), np.sin(t23), np.cos(t23), np.sin(t13), np.cos(t13)
    e = np.exp(1j * d)
    return np.array([[c12 * c13, s12 * c13, s13 / e],
                     [-s12 * c23 - c12 * s23 * s13 * e, c12 * c23 - s12 * s23 * s13 * e, s23 * c13],
                     [s12 * s23 - c12 * c23 * s13 * e, -c12 * s23 - s12 * c23 * s13 * e, c23 * c13]])


def predictions():
    te, _ = phase_and_rho2(POL)
    RA = ratio(roots(te + np.pi / 12, 0.5) ** 2)
    tz, r2z = phase_and_rho2(MZ)
    RB = ratio(roots(tz + boundary(r2z), r2z) ** 2)
    m_struct = np.sort(roots(te + np.pi / 12, 0.5) ** 2)
    W = np.abs(pmns(*np.radians(PMNS_DEG))) ** 2
    lnQ = np.log(1 + ALPHA_MTAU / np.pi * (1 + 1.5 * np.log(91187.6 / POL)))
    RC = ratio(m_struct * np.exp(-(W.T @ lnQ)))
    return {"A": RA, "B": RB, "C": RC}


if __name__ == "__main__":
    P = predictions()
    for k, v in P.items():
        print(f"R_pred {k} = {v:.6f} +- {SIG_PRED[k]:.0e}")
    if len(sys.argv) == 5:
        d21, s21, d31, s31 = map(float, sys.argv[1:])
        Robs = d21 / d31
        sR = Robs * np.hypot(s21 / d21, s31 / d31)
        print(f"R_obs = {Robs:.6f} +- {sR:.6f}")
        z = {k: (v - Robs) / np.hypot(sR, SIG_PRED[k]) for k, v in P.items()}
        for k in P:
            print(f"  {k}: z = {z[k]:+.2f} -> {'vertraeglich' if abs(z[k]) <= 2 else 'widerlegt'}")
        best = min(z, key=lambda k: abs(z[k]))
        print(f"  bevorzugt: {best}; trennend gegen A: {abs(z['A']) - abs(z[best]) >= 2}")
        if abs(z["A"]) > 2 and (abs(z["B"]) <= 2 or abs(z["C"]) <= 2):
            print("  H100: bestaetigt (Korrektur zu H99 noetig und ausreichend)")
        elif abs(z["B"]) > 2 and abs(z["C"]) > 2:
            print("  H100: widerlegt (keine der Korrekturen B, C vertraeglich)")
        else:
            print("  H100: nicht entschieden")
