"""Gesonderter HC je Frame und die dritte Zaehlart (Erkundung, analytisch; keine Zahl wird mit Daten verglichen).

Masken an einer Punktierung mit Spin j (QAM-Notiz 07.11.): P_T = 1{B_u = 1/2} (nur Minimalspin), P_M(u) = 1{B_u - |J_u| = 0} (Extremzustaende),
Vorschlag P_P = 1 (am Photonpunkt sind die Ports gleich, F2: der Kompensator waehlt nichts aus).
(1) Verschachtelung P_T <= P_M(u) <= P_P je j.
(2) Nach dem Verwischen (Mittel ueber Achsen) ist jede Maske a_X(j) * I: Annahme a_P = 1, a_M = 2/(2j+1), a_T = delta(j, 1/2).
(3) gamma je Frame aus der Zaehlgleichung sum_j Spur * exp(-2 pi gamma sqrt(j(j+1))) = 1.
"""
import numpy as np
from scipy.optimize import brentq
from scipy.linalg import expm
from scipy.spatial.transform import Rotation


def ops(j):
    m = np.arange(j, -j - 1, -1); d = len(m)
    Jz = np.diag(m).astype(complex); Jp = np.zeros((d, d), complex)
    for k in range(1, d): Jp[k - 1, k] = np.sqrt(j * (j + 1) - m[k] * (m[k] + 1))
    return (Jp + Jp.conj().T) / 2, (Jp - Jp.conj().T) / 2j, Jz, m


rng = np.random.default_rng(5)
print("j | Raenge T <= M <= P | verwischte Annahme a_T, a_M, a_P")
for j in (0.5, 1, 1.5, 2, 2.5):
    Jx, Jy, Jz, m = ops(j); d = len(m)
    B = j * (j + 1) - m ** 2
    PT = np.diag((np.isclose(B, 0.5)).astype(float)); PM = np.diag((np.isclose(B - np.abs(m), 0)).astype(float)); PP = np.eye(d)
    nested = np.all(np.diag(PT) <= np.diag(PM)) and np.all(np.diag(PM) <= np.diag(PP))
    acc = []
    for Pm in (PT, PM, PP):
        S = np.zeros((d, d), complex)
        for _ in range(1500):
            a = Rotation.random(random_state=rng.integers(1e9)).as_rotvec()
            U = expm(-1j * (a[0] * Jx + a[1] * Jy + a[2] * Jz)); S += U @ Pm @ U.conj().T
        acc.append(np.trace(S).real / 1500 / d)
    print(f"{j} | {int(PT.trace())} <= {int(PM.trace())} <= {int(PP.trace())}, verschachtelt: {nested} | "
          f"{acc[0]:.4f}, {acc[1]:.4f} (2/(2j+1) = {2/(2*j+1):.4f}), {acc[2]:.4f}")
js = np.arange(1, 4000) / 2; a = np.sqrt(js * (js + 1))
g = lambda w: brentq(lambda x: np.sum(w * np.exp(-2 * np.pi * x * a)) - 1, 0.01, 2)
gT = g(np.where(js == 0.5, 2.0, 0.0)); gM = g(2 * np.ones_like(js)); gP = g(2 * js + 1)
print(f"gamma_T = {gT:.6f} (nur j = 1/2), gamma_M = {gM:.6f} (Gewicht 2), gamma_P = {gP:.6f} (alle 2j+1, dritte Zaehlart)")
print(f"Verhaeltnisse (nur strukturell, kein Datenvergleich): gamma_M/gamma_T = {gM/gT:.6f}, gamma_P/gamma_M = {gP/gM:.6f}, gamma_P/gamma_T = {gP/gT:.6f}")
