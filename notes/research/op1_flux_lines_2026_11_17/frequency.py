"""Nachtrag: Die Breite von M setzt eine Frequenz voraus.  (Erkundung, nicht blind, analytisch.)

(a) Gravitatives Analogon: Weyl-Feld als Q = E + iB mit reellen, symmetrischen, spurfreien E_ij, B_ij (gravito-elektrisch/-magnetisch);
    s+ = tr Q^2, s- = tr Qbar^2 (Analogon zu F+.F+, F-.F-).  Fuer reelle Felder s- = conj s+, also Breite 0 (Lage von P).
    Typ D am isolierten Horizont (nur Psi_2): E, B diagonal proportional diag(-1,-1,2); Breite 0 fuer jedes Psi_2 (Schwarzschild und Kerr).
(b) Zeitharmonisches Maxwell-Feld E(t) = Re(Ehat e^{-i w t}): Breite aus den komplexen Amplituden (r16.8).  Grenzfall w -> 0 mit festem
    reellem Feld: Ehat reell (bis auf Phase) -> Breite 0.  Breite ungleich 0 braucht relative Phasen zwischen Komponenten, also w > 0.
"""
import numpy as np

rng = np.random.default_rng(11)


def lat(sp, sm):
    a, b = np.sqrt(abs(sp)), np.sqrt(abs(sm))
    return (a - b) / (a + b)


def stf(M):
    M = (M + M.T) / 2
    return M - np.trace(M) / 3 * np.eye(3)


mx = 0.0
for _ in range(1000):
    E, B = stf(rng.normal(size=(3, 3))), stf(rng.normal(size=(3, 3)))
    Q = E + 1j * B
    mx = max(mx, abs(lat(np.trace(Q @ Q), np.trace(Q.conj() @ Q.conj()))))
print(f"(a) reelle Weyl-Felder: max |Breite| = {mx:.1e} (Lage von P)")
D = np.diag([-1.0, -1.0, 2.0])
for psi2 in (1.0, 0.8 + 0.3j, 0.2 + 1.0j):
    Q = psi2 * D
    print(f"    Typ D, Psi_2 = {psi2}: Breite {lat(np.trace(Q @ Q), np.trace(Q.conj() @ Q.conj())):.1e}")


def chi_lat(Eh, Bh):
    Fp, Fm = Eh + 1j * Bh, Eh - 1j * Bh
    return lat(Fp @ Fp, Fm @ Fm)


# (b) Amplituden mit relativer Phase phi zwischen zwei Komponenten
for phi in (0.0, 0.3, 0.8, 1.2):
    Eh = np.array([1.0, 0.6 * np.exp(1j * phi), 0]); Bh = np.array([0.2, 0, 0.9 * np.exp(1j * phi)])
    print(f"(b) relative Phase {phi:.1f}: Breite {chi_lat(Eh, Bh):+.4f}")
print("    relative Phase 0 = reelles (statisches) Feld bis auf Gesamtphase -> Breite 0; Phasen gibt es nur bei w > 0")
