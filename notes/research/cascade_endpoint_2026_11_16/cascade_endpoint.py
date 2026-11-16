"""Wohin fuehrt die Kaskade "zurueck zu z^- = 0"?  R oder P?  (Erkundung, nicht blind.)

Doublet (E, B) wie v4.9.0-r04/r27/r28; Boden phi = |s|/2u = |b|; R: phi = 1 (rein, Kompensatorachse, r24.3/r29.1(a)); P: phi = 0.
(1) Kompensator-Kaskade K = C o Pi_J (thm:horizon-cascade-singularity; r10/r27 "drehen, dann kompensieren"): das Bild jedes Feldes
    mit E + B != 0 hat phi = 1 (R); nie phi = 0.
(2) Nullachsen-Transport (thm:fractal, Nullachse nach v4.8.0-r06 = {s = 0}): invertible Abbildungen aus Lorentz-Gruppe und Dualitaet
    erhalten s = 0 und erreichen es von aussen nicht (k220): Sie tragen P, sie fuehren nicht hin.
(3) Offenes System mit Tachyon-Reservoir (v4.9.0-r28.2(c)): Attraktor |b| = sin^2 th / (1 - cos^2 th cos 2a).  Grenzen th -> 0 und
    th -> pi/2; Lage des Attraktors zwischen P und R.
(4) Viele Frequenzen ohne Reservoir (r28.2(b)): Kohaerenz ~ N^{-1/2} -> Richtung P nur im Grenzwert.
"""
import numpy as np

rng = np.random.default_rng(1121)


def phi(E, B):
    z = E + 1j * B
    return abs(z @ z) / (E @ E + B @ B)


def comp(E, B):
    m = (E + B) / 2; return m, m


def boost(E, B, v, n):
    n = n / np.linalg.norm(n); g = 1 / np.sqrt(1 - v * v); vv = v * n
    return (g * (E + np.cross(vv, B)) - (g - 1) * np.dot(E, n) * n,
            g * (B - np.cross(vv, E)) - (g - 1) * np.dot(B, n) * n)


# (1)
dev = 0.0; mn = 1.0
for _ in range(2000):
    E, B = rng.normal(size=3), rng.normal(size=3)
    p = phi(*comp(E, B)); dev = max(dev, abs(p - 1)); mn = min(mn, p)
print(f"(1) Kompensator-Bild: phi = 1 fuer 2000 Felder (max Abw. {dev:.1e}, min phi {mn:.6f}); P wird nie erreicht")
n = rng.normal(size=3); a = rng.normal(size=3); b = np.cross(n, a); a = np.cross(b, n); a /= np.linalg.norm(a); b /= np.linalg.norm(b)
print(f"    auch ein lichtartiges Feld (phi = {phi(a, b):.1e}) geht nach der Kompensation auf phi = {phi(*comp(a, b)):.3f}")

# (2)
dev0 = 0.0; mnon = 1.0
for _ in range(1000):
    v, d = rng.uniform(0, 0.99), rng.normal(size=3); al = rng.uniform(0, 2 * np.pi)
    Eb, Bb = boost(a, b, v, d); Eb, Bb = Eb * np.cos(al) - Bb * np.sin(al), Eb * np.sin(al) + Bb * np.cos(al)
    dev0 = max(dev0, phi(Eb, Bb))
    E, B = rng.normal(size=3), rng.normal(size=3); f0 = abs((E + 1j * B) @ (E + 1j * B))
    Eb, Bb = boost(E, B, v, d); mnon = min(mnon, abs((Eb + 1j * Bb) @ (Eb + 1j * Bb)) / f0)
print(f"(2) Boosts und Dualitaet: lichtartig bleibt lichtartig (max phi {dev0:.1e}); |s| nicht lichtartiger Felder bleibt"
      f" (min |s'|/|s| = {mnon:.6f})")

# (3)
al = np.pi / 6
for th_deg in (1, 15, 30, 45, 60, 75, 89.9):
    th = np.radians(th_deg); bb = np.sin(th) ** 2 / (1 - np.cos(th) ** 2 * np.cos(2 * al))
    print(f"(3) Reservoir th = {th_deg:5.1f} Grad: Attraktor |b| = {bb:.4f}")
print("    th -> 0: |b| -> 0 (P); th -> 90 Grad: |b| -> 1 (R).  Die Kopplung an das Reservoir legt die Lage zwischen P und R fest.")
x = 1 / 3; th = np.arcsin(np.sqrt(x)); bb = np.sin(th) ** 2 / (1 - np.cos(th) ** 2 * np.cos(2 * al))
print(f"    Selbstkonsistenz (r28, nachtraeglich): sin^2 th = x = 1/3 gibt |b| = {bb:.4f} = (1-x)/(1+x) = {(1-x)/(1+x):.4f}")

# (4)
for N in (2, 10, 40, 400, 4000):
    g = rng.uniform(10, 100, size=N); ks = np.arange(50, 5000)
    K = np.abs(np.exp(1j * np.outer(ks * 0.3, g)).mean(axis=1)).mean()
    print(f"(4) {N:5d} Frequenzen ohne Reservoir: mittlere Kohaerenz {K:.3f} (N^-1/2 = {N**-0.5:.3f})")
