"""C5, Form (iii): Die augenblickliche Invariante s(t) eines zeitharmonischen Feldes wird zu endlichen Zeiten null
(Erkundung, nicht blind).

E(t) = Re(E^ e^{-i w t}), B(t) = Re(B^ e^{-i w t}), z(t) = E(t) + i B(t), s(t) = z(t).z(t) (bilinear).
(1) Konstruktion: Amplituden mit z(0) lichtartig und ungleich null, aber nicht lichtartig als Zustand (s+, s-, w != 0).
(2) s(t) = [s+ e^{-2iwt} + 2w + conj(s-) e^{2iwt}]/4: Ellipse um w/2; Nullstellen; Kontrolle z(t*) != 0.
(3) Haeufigkeit: Anteil zufaelliger Amplituden, deren Ellipse durch 0 geht (Kodimension 1 -> Anteil 0); Abstand der Ellipse
    von 0 als Groesse.
(4) Invarianz: Boost der augenblicklichen Felder E(t*), B(t*) laesst s(t*) = 0 (s ist Lorentz-Skalar).
(5) Zustand im Nullaugenblick: Stokes-Vektor b = (E^2 - B^2, 2 E.B)/(E^2 + B^2) = 0 (Photonpunkt P der Scheibe, r04/r19);
    Kompensatoranteil (r27: C = (1 + sigma_x)/2 auf der Scheibe) = 1/2, nicht 0.
(6) Triviale Faelle: reelle gleichphasige Amplituden geben z(t) = z cos(wt); dort ist der Nullaugenblick z = 0 (kein Zeuge).
"""
import numpy as np

rng = np.random.default_rng(155)


def inst(E, B, t):
    return (E * np.exp(-1j * t)).real, (B * np.exp(-1j * t)).real


def invariants(E, B):
    Fp, Fm = E + 1j * B, E - 1j * B
    return Fp @ Fp, Fm @ Fm, Fp @ np.conj(Fm)


def s_of_t(E, B, t):
    e, b = inst(E, B, t); z = e + 1j * b; return z @ z


def boost(E, B, v, n):
    n = n / np.linalg.norm(n); g = 1 / np.sqrt(1 - v * v); vv = v * n
    return (g * (E + np.cross(vv, B)) - (g - 1) * np.dot(E, n) * n,
            g * (B - np.cross(vv, E)) - (g - 1) * np.dot(B, n) * n)


# (1) Konstruktion
E = np.array([1, 0, 0.3j]); B = np.array([0.7j, 1, 0])
sp, sm, w = invariants(E, B)
e0, b0 = inst(E, B, 0.0)
print(f"(1) Zustandsinvarianten s+ = {sp:.4f}, s- = {sm:.4f}, w = {w:.4f} (alle ungleich 0)")
print(f"    t = 0: E = {e0}, B = {b0}, s(0) = {s_of_t(E, B, 0):.2e}, |z(0)| = {np.linalg.norm(e0 + 1j*b0):.4f}")

# (2) Ellipse und Nullstellen
ts = np.linspace(0, np.pi, 200001)
vals = np.array([s_of_t(E, B, t) for t in ts])
model = (sp * np.exp(-2j * ts) + 2 * w + np.conj(sm) * np.exp(2j * ts)) / 4
i0 = np.argsort(abs(vals))[:6]
print(f"(2) Formel fuer s(t) bestaetigt: max. Abweichung {abs(vals - model).max():.1e}; Nullstellen pro halbe Periode bei t ~"
      f" {sorted(set(np.round(ts[i0], 3)))} (|s| min {abs(vals).min():.1e})")
for t in sorted(set(np.round(ts[i0], 3))):
    e, b = inst(E, B, t); print(f"    t = {t}: |z(t)| = {np.linalg.norm(e + 1j*b):.4f}")

# (3) Haeufigkeit
dist = []
for _ in range(2000):
    Er, Br = rng.normal(size=3) + 1j * rng.normal(size=3), rng.normal(size=3) + 1j * rng.normal(size=3)
    tt = np.linspace(0, np.pi, 2001)
    sv = np.array([s_of_t(Er, Br, t) for t in tt])
    dist.append(abs(sv).min() / abs(sv).max())
dist = np.array(dist)
print(f"(3) Zufaellige Amplituden: kleinster relativer Abstand der Ellipse von 0: Median {np.median(dist):.3f},"
      f" Anteil < 1e-3: {(dist < 1e-3).mean():.4f} (Kodimension 1: nur Sonderfaelle)")

# (4) Invarianz im Nullaugenblick
t0 = 0.0
e, b = inst(E, B, t0); dev = 0
for _ in range(200):
    ep, bp = boost(e, b, rng.uniform(0.1, 0.95), rng.normal(size=3)); z = ep + 1j * bp
    dev = max(dev, abs(z @ z))
print(f"(4) Boost der augenblicklichen Felder: s bleibt 0 (max. |s'| = {dev:.1e}); der Nullaugenblick ist ein invariantes Ereignis")

# (5) Zustand im Nullaugenblick
G = np.array([[e @ e, e @ b], [b @ e, b @ b]]); u = np.trace(G) / 2
bvec = np.array([G[0, 0] - G[1, 1], 2 * G[0, 1]]) / (2 * u)
comp = (1 + bvec[1]) / 2   # Kompensatorachse x der Scheibe (r27) entspricht hier der zweiten Komponente
print(f"(5) Stokes-Vektor im Nullaugenblick b = {np.round(bvec, 12)} (Photonpunkt P); Kompensatoranteil {comp:.3f} (nicht 0)")
t1 = 0.6; e1, b1 = inst(E, B, t1); G1 = np.array([[e1 @ e1, e1 @ b1], [b1 @ e1, b1 @ b1]])
print(f"    zum Vergleich t = {t1}: |b| = {np.hypot(G1[0,0]-G1[1,1], 2*G1[0,1])/np.trace(G1):.3f}")

# (6) trivialer Fall
Er = np.array([1., 0, 0]); Br = np.array([0., 0.5, 0])
tt = np.linspace(0, np.pi, 20001); sv = np.array([s_of_t(Er, Br, t) for t in tt]); k = np.argmin(abs(sv))
e, b = inst(Er, Br, tt[k])
print(f"(6) reelle gleichphasige Amplituden: min |s| = {abs(sv).min():.1e} bei t = {tt[k]:.4f}, dort |z| = {np.linalg.norm(e + 1j*b):.1e} (Feld null)")
