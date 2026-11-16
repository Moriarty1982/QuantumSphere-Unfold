"""OP1, Bedingung U1: Liest der Frame M an einer Punktierung eine native U(1)-Ladung?  (Erkundung, nicht blind)

(1) Dualitaetsdrehung z -> e^{i a} z auf chi = (sqrt s+, sqrt s-): Drehung um die Helizitaetsachse (z-Achse von chi) um 2a?
    R (Tachyon-Abbildung, a = pi/2) = sigma_z bis auf Phase.  Selbstduale / antiselbstduale Felder = Pole von chi.
(2) Buendel aus n Straengen (je ein chi-Qubit, (S1)), Ladung m = Summe der Helizitaeten: Maske P_M(u) = 1{B_u - |J_u| = 0}
    mit u = Helizitaetsachse gibt je j genau die zwei Extremzustaende; Spur mit exp(-2 pi g sqrt(j(j+1))) = DL-Gleichung.
    Ohne Ausrichtung (alle j >= |m| zur Ladung m) = Ghosh-Mitra-Zaehlung.
"""
import numpy as np
from scipy.optimize import brentq

rng = np.random.default_rng(3)


def chi(E, B):
    Fp, Fm = E + 1j * B, E - 1j * B
    sp, sm = Fp @ Fp, Fm @ Fm
    v = np.array([np.sqrt(sp + 0j), np.sqrt(sm + 0j)])
    return v / np.linalg.norm(v)


def bloch(v):
    X = np.array([[0, 1], [1, 0]]); Y = np.array([[0, -1j], [1j, 0]]); Z = np.diag([1, -1])
    return np.real([np.vdot(v, X @ v), np.vdot(v, Y @ v), np.vdot(v, Z @ v)])


dev_z = dev_ang = 0.0
for _ in range(200):
    E, B = rng.normal(size=3) + 1j * rng.normal(size=3), rng.normal(size=3) + 1j * rng.normal(size=3)
    a = rng.uniform(0, np.pi)
    z = (E + 1j * B) * np.exp(1j * a); E2, B2 = z.real + 0j, z.imag + 0j
    # komplexe Amplituden: Dualitaet wirkt auf z = E + iB als Multiplikation; fuer komplexe E, B: E' = Re-Teil im Sinne der Rotation
    E2 = np.cos(a) * E - np.sin(a) * B; B2 = np.sin(a) * E + np.cos(a) * B
    b1, b2 = bloch(chi(E, B)), bloch(chi(E2, B2))
    dev_z = max(dev_z, abs(b1[2] - b2[2]))
    ang = (np.arctan2(b2[1], b2[0]) - np.arctan2(b1[1], b1[0])) % (2 * np.pi)
    target = (-2 * a) % (2 * np.pi); d = min(abs(ang - target), 2 * np.pi - abs(ang - target))
    # Vorzeichenwahl der Wurzeln kann um pi verschieben (r16.3(c))
    dev_ang = max(dev_ang, min(d, abs(d - np.pi)))
print(f"(1) Dualitaetsdrehung um a: Helizitaetskomponente von chi unveraendert (max. Abweichung {dev_z:.1e}),"
      f" Drehwinkel um die Helizitaetsachse = -2a bis auf die Wurzelwahl (max. Abweichung {dev_ang:.1e})")
E = np.array([1, 0, 0], complex); B = -1j * E           # E + iB = 2E, E - iB = 0 -> s- = 0
print(f"    selbstduales Feld (E = iB-Typ): chi-Bloch = {np.round(bloch(chi(E, 1j * E)), 6)}, antiselbstdual: {np.round(bloch(chi(E, -1j * E)), 6)}")

js = np.arange(1, 4000) / 2; a = np.sqrt(js * (js + 1))
def gamma(weights):
    return brentq(lambda g: np.sum(weights * np.exp(-2 * np.pi * g * a)) - 1, 0.01, 2)
# Maske P_M(u) im Einpunktmodell: Rang je j
def mask_rank(j):
    ms = np.arange(-j, j + 1)
    B = j * (j + 1) - ms ** 2
    return int(np.sum(np.isclose(B - np.abs(ms), 0)))
ranks = np.array([mask_rank(j) for j in js[:20]])
print(f"(2) Rang der Maske P_M(u) fuer j = 1/2 .. 10: {sorted(set(ranks.tolist()))} (zwei Extremzustaende je j)")
print(f"    ausgerichtete Buendel (Gewicht 2 je j)  -> gamma = {gamma(2 * np.ones_like(js)):.6f} (DL)")
print(f"    alle j >= |m| zur Ladung (Gewicht 2j+1) -> gamma = {gamma(2 * js + 1):.6f} (Ghosh-Mitra)")
