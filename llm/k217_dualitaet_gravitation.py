"""k217: Tachyon-Abbildung (Dualitaetsdrehung z -> iz) und die Quelle der Gravitation.

Erkundung zu v4.10.0-r06.5 (Dorau-Much-Kette im Tachyon-Frame). Nicht blind: das Ergebnis steht
analytisch fest; dies ist nur eine numerische Kontrolle.

Riemann-Silberstein z = E + iB. Lorentz-Boost entlang n mit Rapiditaet eta wirkt als komplexe
Drehung R_n(i*eta) in SO(3,C) (Vorzeichenkonvention unerheblich fuer die Pruefung).
Geprueft:
  (1) z -> iz vertauscht mit dem Boost (v4.8.0-r20.1);
  (2) Energie-Impuls-Tensor (Energiedichte, Poynting, Maxwell-Spannung) ist unter z -> iz invariant;
  (3) Lagrangedichte (E^2 - B^2)/2 und E.B wechseln das Vorzeichen (s -> -s);
  (4) Energiefluss T_ab xi^a xi^b fuer den Boost-Killingvektor in Nullrichtung: invariant.
Ausgabe: groesste Abweichungen; Negativkontrolle: z -> z* (keine Symmetrie des Tensors? doch: E,B->E,-B)
und z -> (1+0.3i)z (Skalierung, nicht unitaer) muss den Tensor aendern.
"""
import numpy as np

rng = np.random.default_rng(217)


def rot(n, a):
    """Drehmatrix um Achse n mit (komplexem) Winkel a (Rodrigues)."""
    n = np.asarray(n, dtype=complex)
    n = n / np.sqrt(n @ n)
    K = np.array([[0, -n[2], n[1]], [n[2], 0, -n[0]], [-n[1], n[0], 0]], dtype=complex)
    return np.eye(3) + np.sin(a) * K + (1 - np.cos(a)) * (K @ K)


def stress(z):
    """Maxwell-Energie-Impuls-Tensor T^{mu nu} (Einheiten eps0 = c = 1) aus z = E + iB."""
    E, B = z.real, z.imag
    T = np.zeros((4, 4))
    T[0, 0] = 0.5 * (E @ E + B @ B)
    S = np.cross(E, B)
    T[0, 1:] = T[1:, 0] = S
    T[1:, 1:] = -(np.outer(E, E) + np.outer(B, B)) + 0.5 * (E @ E + B @ B) * np.eye(3)
    return T


def lag(z):
    return 0.5 * (z.real @ z.real - z.imag @ z.imag), z.real @ z.imag


max_comm = max_T = max_flux = 0.0
min_lag_flip = np.inf
neg_scale = 0.0
for _ in range(2000):
    z = rng.normal(size=3) + 1j * rng.normal(size=3)
    n = rng.normal(size=3)
    eta = rng.normal() * 2
    L = rot(n, 1j * eta)
    # (1) Vertauschung
    max_comm = max(max_comm, np.abs(L @ (1j * z) - 1j * (L @ z)).max())
    # (2) Tensor invariant
    max_T = max(max_T, np.abs(stress(1j * z) - stress(z)).max())
    # (3) Vorzeichenwechsel der Invarianten
    l0, p0 = lag(z)
    l1, p1 = lag(1j * z)
    min_lag_flip = min(min_lag_flip, -max(abs(l1 + l0), abs(p1 + p0)))
    # (4) Fluss fuer Nullvektor k = (1, x-Richtung) des Boosts
    k = np.array([1.0, 1.0, 0.0, 0.0])
    f0 = k @ stress(z) @ k
    f1 = k @ stress(1j * z) @ k
    max_flux = max(max_flux, abs(f1 - f0))
    # Negativkontrolle: nicht-unitaere Skalierung aendert den Tensor
    neg_scale = max(neg_scale, np.abs(stress((1 + 0.3j) * z) - stress(z)).max())

print(f"(1) max |L(iz) - i Lz|            = {max_comm:.2e}")
print(f"(2) max |T(iz) - T(z)|            = {max_T:.2e}")
print(f"(3) max |L(iz)+L(z)|,|EB(iz)+EB(z)| = {-min_lag_flip:.2e}  (Vorzeichenwechsel)")
print(f"(4) max |T_kk(iz) - T_kk(z)|      = {max_flux:.2e}")
print(f"Negativkontrolle (1+0.3i)z: max |dT| = {neg_scale:.2e}  (muss O(1) sein)")
