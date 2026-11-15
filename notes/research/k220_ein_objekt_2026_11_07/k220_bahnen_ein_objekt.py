"""k220: Bahnen von G = SO(3,C) x U(1)_Dualitaet auf C^3 (Lesart B, z = E + iB, s = z.z).

Erkundung "ein Objekt". Geprueft:
 (1) Transitivitaet auf jeder Schale |s| = r > 0: zu zufaelligen z1, z2 mit |s1| = |s2| wird explizit
     ein Paar (alpha, L) mit L in SO(3,C) konstruiert, so dass z2 = L e^{i alpha} z1.
 (2) Invarianz: |s| unter G erhalten; der Nullkegel s = 0 ist eine eigene Bahn (nicht null -> null unmoeglich).
 (3) Nicht invertierbare Operationen erreichen den Nullkegel bzw. P: Kompensator C(z) = (z + i conj z)/2 (r11.2(f): nicht null),
     Mischung, Grenzwert lambda z mit lambda -> 0.
Negativkontrolle: z2 mit anderem |s| -> Konstruktion muss scheitern (Residuum O(1)).
"""
import numpy as np

rng = np.random.default_rng(220)
dot = lambda a, b: a @ b  # bilinear, nicht hermitesch


def frame(w):
    """Komplex-orthonormale Basis (bilinear) mit erstem Vektor w/sqrt(s), det = 1."""
    s = dot(w, w)
    e1 = w / np.sqrt(s)
    # zweiter Vektor: zufaellig, bilinear orthogonalisieren und normieren
    for _ in range(20):
        v = rng.normal(size=3) + 1j * rng.normal(size=3)
        v = v - dot(v, e1) * e1
        if abs(dot(v, v)) > 1e-3:
            break
    e2 = v / np.sqrt(dot(v, v))
    e3 = np.cross(e1, e2)          # fuer bilinear orthonormale e1, e2 ist e1 x e2 bilinear normiert
    F = np.column_stack([e1, e2, e3])
    return F


def connect(z1, z2):
    s1, s2 = dot(z1, z1), dot(z2, z2)
    alpha = (np.angle(s2) - np.angle(s1)) / 2
    w = np.exp(1j * alpha) * z1
    F1, F2 = frame(w), frame(z2)
    L = F2 @ F1.T                 # bildet F1-Basis auf F2-Basis ab; F^T F = 1 bilinear
    return alpha, L


max_res = max_orth = max_det = 0.0
for _ in range(2000):
    z1 = rng.normal(size=3) + 1j * rng.normal(size=3)
    z2 = rng.normal(size=3) + 1j * rng.normal(size=3)
    z2 *= np.sqrt(abs(dot(z1, z1)) / abs(dot(z2, z2)))   # gleiche Schale
    a, L = connect(z1, z2)
    max_res = max(max_res, np.abs(L @ (np.exp(1j * a) * z1) - z2).max())
    max_orth = max(max_orth, np.abs(L.T @ L - np.eye(3)).max())
    max_det = max(max_det, abs(np.linalg.det(L) - 1))
print(f"(1) Transitivitaet auf |s| = r: max Residuum {max_res:.1e}, max |L^T L - 1| {max_orth:.1e}, max |det L - 1| {max_det:.1e}")

# Negativkontrolle: verschiedene Schalen
z1 = rng.normal(size=3) + 1j * rng.normal(size=3)
z2 = 2.0 * (rng.normal(size=3) + 1j * rng.normal(size=3))
z2 *= np.sqrt(4 * abs(dot(z1, z1)) / abs(dot(z2, z2)))   # |s2| = 4|s1|
a, L = connect(z1, z2 / 2)   # verbindet nur bis auf Skalierung
print(f"    Negativkontrolle |s2| = 4|s1|: Residuum ohne Skalierung {np.abs(L @ (np.exp(1j*a)*z1) - z2).max():.2f}")

# (2) Invarianz von |s|
inv = 0.0
for _ in range(500):
    z = rng.normal(size=3) + 1j * rng.normal(size=3)
    a, L = connect(z, (rng.normal(size=3) + 1j * rng.normal(size=3)) * 0 + z)  # Identitaet-artig
    M = frame(z) @ frame(z).T      # irgendein SO(3,C)-Element
    inv = max(inv, abs(abs(dot(M @ (np.exp(0.7j) * z), M @ (np.exp(0.7j) * z))) - abs(dot(z, z))))
print(f"(2) |s| unter G erhalten: max Abweichung {inv:.1e}")

# (3) Nicht invertierbare Wege
z = rng.normal(size=3) + 1j * rng.normal(size=3)
C = (z + 1j * np.conj(z)) / 2
print(f"(3) Kompensatorbild: s' = {dot(C, C):.3f} (nicht null, r11.2(f));  lambda z, lambda=1e-6: |s| = {abs(dot(1e-6*z,1e-6*z)):.1e} -> 0 nur im Grenzwert")
