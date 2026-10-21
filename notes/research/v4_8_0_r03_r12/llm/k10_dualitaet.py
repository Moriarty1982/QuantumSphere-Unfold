r"""K10 / r07: Sektor-Zuordnung und Dualitaetswinkel in Lesart B.

 (1) Jeder Nicht-Nullvektor z (s != 0) zerfaellt eindeutig (bis auf Vorzeichen) als z = e^{i alpha} z_m
     mit s(z_m) = |s| > 0 (reiner Materie-Rahmen); alpha = arg(s)/2 mod pi.
 (2) Tachyon-Rahmen: alpha = pi/2  <=>  s < 0. Materie: alpha = 0  <=>  s > 0.
 (3) Gruppe SO(3,C) x U(1)_dual: Bahnen auf C^3 \ {0} sind {|s| = r} (r > 0) und der punktierte Nullkegel.
     Pruefung: zwei zufaellige z mit gleichem |s| werden durch (R, alpha) ineinander ueberfuehrt.
 (4) Nebenbedingung N(q) = 0 des Kerns: s = t^2. Reelles t != 0 -> Materie-Rahmen; t = 0 -> Photon;
     tachyonartig nur mit imaginaerem t.
"""
import numpy as np
rng = np.random.default_rng(5)
s_of = lambda z: np.sum(z*z)

def frame(z):
    s = s_of(z); alpha = np.angle(s)/2
    zm = np.exp(-1j*alpha)*z
    return alpha, zm

ok1 = ok2 = True
for _ in range(500):
    z = rng.normal(size=3) + 1j*rng.normal(size=3)
    a, zm = frame(z)
    sm = s_of(zm)
    ok1 &= abs(sm.imag) < 1e-10 and sm.real > 0 and np.isclose(sm.real, abs(s_of(z)))
    # Eindeutigkeit: alpha + pi liefert -zm, gleiche Klasse; alpha + pi/2 liefert s < 0
    ok2 &= s_of(np.exp(-1j*(a + np.pi/2))*z).real < 0
print("(1) z = e^{i alpha} z_m mit s(z_m) = |s| > 0:", bool(ok1))
print("(2) alpha + pi/2 ergibt Tachyon-Rahmen (s < 0):", bool(ok2))

def to_axis(z):
    r = np.sqrt(s_of(z)); e1 = z/r
    v = rng.normal(size=3) + 0j
    e2 = v - (e1@v)*e1; e2 = e2/np.sqrt(e2@e2); e3 = np.cross(e1, e2)
    return np.array([e1, e2, e3]), r
ok3 = True
for _ in range(200):
    z1 = rng.normal(size=3) + 1j*rng.normal(size=3)
    z2 = rng.normal(size=3) + 1j*rng.normal(size=3)
    z2 = z2*np.sqrt(abs(s_of(z1))/abs(s_of(z2)))          # gleiches |s|
    a1, m1 = frame(z1); a2, m2 = frame(z2)
    R1, r1 = to_axis(m1); R2, r2 = to_axis(m2)            # beide auf (sqrt|s|, 0, 0)
    R = R2.T @ R1                                          # m1 -> m2
    w = np.exp(1j*(a2 - a1))*(R @ z1)
    ok3 &= np.allclose(w, z2) or np.allclose(-w, z2) or np.allclose(np.exp(1j*np.pi)*w, z2)
print("(3) gleiches |s| -> eine Bahn von SO(3,C) x U(1):", bool(ok3))

t = 0.7
print("(4) N(q) = -t^2 + s = 0  ->  s = t^2 =", t*t, "(reell positiv: Materie-Rahmen); t = 0 -> s = 0 (Photon);",
      "s < 0 erfordert t^2 < 0")
