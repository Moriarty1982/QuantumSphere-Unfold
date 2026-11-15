"""C5 (B3): Liegen Felder mit Nullaugenblick vor? Rueckwaertssuche von der Bedingung zu Feldklassen (Erkundung, nicht blind).

Zeitharmonisches Feld in einem Punkt: s(t) = [s+ e^{-2iwt} + 2w + conj(s-) e^{2iwt}]/4 (r16.8).
(1) Bedingung: Nullaugenblick <=> conj(s-) x^2 + 2w x + s+ = 0 hat eine Wurzel mit |x| = 1
    <=> Q := -2w e^{-i g} liegt auf der Ellipse mit Halbachsen |s+| + |s-| (reell) und ||s+| - |s-|| (imaginaer),
    g = (arg s+ - arg s-)/2.  Signierter Abstand F = X^2/(a+b)^2 + Y^2/(a-b)^2 - 1, Nullaugenblick <=> F = 0.
(2) Eine ebene Welle: s(t) = 0 fuer alle t (jede Polarisation): bleibende Null von Anfang an (r21.6).
(3) Zwei ebene Wellen gleicher Frequenz: s(t) = 2 z1(t).z2(t).  Ist eine linear polarisiert, verschwindet sie zweimal je Periode;
    dann ist s = 0 und z = z2 != 0: Nullaugenblick in JEDEM Punkt.  Zwei elliptische Wellen: nur auf einer Flaeche.
(4) Linear <=> gleiche Helizitaetsgewichte |F+| = |F-| der Welle.
(5) Allgemeines Feld aus N ebenen Wellen: Vorzeichen von F im Raum; F wechselt das Vorzeichen -> die Punkte mit Nullaugenblick
    bilden Flaechen (Kodimension 1 im Raum).  Kontrolle: Nullstelle von s(t) direkt auf der Flaeche.
"""
import numpy as np

rng = np.random.default_rng(1118)


def invariants(E, B):
    Fp, Fm = E + 1j * B, E - 1j * B
    return Fp @ Fp, Fm @ Fm, Fp @ np.conj(Fm)


def s_of_t(E, B, t):
    z = (E * np.exp(-1j * t)).real + 1j * (B * np.exp(-1j * t)).real
    return z @ z


def F_sign(E, B):
    sp, sm, w = invariants(E, B)
    a, b = abs(sp), abs(sm); g = (np.angle(sp) - np.angle(sm)) / 2
    Q = -2 * w * np.exp(-1j * g)
    return Q.real ** 2 / (a + b) ** 2 + Q.imag ** 2 / max((a - b) ** 2, 1e-300) - 1


def root_dist(E, B):
    """Abstand der naechsten Wurzel von conj(s-) x^2 + 2w x + s+ vom Einheitskreis (0 <=> Nullaugenblick, exakt)."""
    sp, sm, w = invariants(E, B)
    return np.min(abs(abs(np.roots([np.conj(sm), 2 * w, sp])) - 1))


def min_s(E, B, n=4001):
    ts = np.linspace(0, np.pi, n)
    v = np.array([abs(s_of_t(E, B, t)) for t in ts]); u = np.array([np.linalg.norm(
        (E * np.exp(-1j * t)).real) ** 2 + np.linalg.norm((B * np.exp(-1j * t)).real) ** 2 for t in ts])
    return (v / u).min()


# (1) Bedingung gegen direkte Rechnung
agree = 0; N = 400
for _ in range(N):
    E, B = rng.normal(size=3) + 1j * rng.normal(size=3), rng.normal(size=3) + 1j * rng.normal(size=3)
    sp, sm, w = invariants(E, B)
    roots = np.roots([np.conj(sm), 2 * w, sp])
    on_circle = np.min(abs(abs(roots) - 1))
    inside = (abs(roots) < 1).sum() != 1          # Windungszahl von p(x)/x = (#innen) - 1: Ursprung innen <=> 0 oder 2 Wurzeln innen
    agree += inside == (F_sign(E, B) < 0)
print(f"(1) Ellipsenbedingung: 'Ursprung innerhalb' (F < 0) <=> 0 oder 2 Wurzeln in |x| < 1, Uebereinstimmung {agree}/{N};"
      " Nullaugenblick <=> Wurzel auf |x| = 1 <=> F = 0")
E, B = np.array([1, 0, 0.3j]), np.array([0.7j, 1, 0])
sp, sm, w = invariants(E, B)
print(f"    Beispiel r20.1: F = {F_sign(E, B):+.1e}, |Wurzel| = {np.round(abs(np.roots([np.conj(sm), 2*w, sp])), 12)}")


def plane_wave(k, pol, phase=0.0):
    """Komplexe Amplituden (E^, B^) einer ebenen Welle in Richtung k mit Jones-Vektor pol in der Ebene senkrecht zu k."""
    k = k / np.linalg.norm(k)
    e1 = np.cross(k, [0.3, 0.5, 0.8]); e1 /= np.linalg.norm(e1); e2 = np.cross(k, e1)
    E = (pol[0] * e1 + pol[1] * e2) * np.exp(1j * phase)
    return E, np.cross(k, E)


def at(waves, x, kmag=1.0):
    E = sum(Ew * np.exp(1j * kmag * (kw / np.linalg.norm(kw)) @ x) for kw, Ew, Bw in waves)
    B = sum(Bw * np.exp(1j * kmag * (kw / np.linalg.norm(kw)) @ x) for kw, Ew, Bw in waves)
    return E, B


# (2)
for name, pol in (("linear", (1, 0)), ("zirkular", (1, 1j)), ("elliptisch", (1, 0.4j))):
    E, B = plane_wave(rng.normal(size=3), np.array(pol, complex))
    print(f"(2) eine ebene Welle, {name}: max |s(t)| = {max(abs(s_of_t(E, B, t)) for t in np.linspace(0, np.pi, 200)):.1e}")


# (3) zwei Wellen
def two_wave_stats(pol1, pol2, npts=300):
    k1, k2 = rng.normal(size=3), rng.normal(size=3)
    w1, w2 = plane_wave(k1, np.array(pol1, complex)), plane_wave(k2, np.array(pol2, complex), rng.uniform(0, 6))
    waves = [(k1, *w1), (k2, *w2)]
    m = []
    for _ in range(npts):
        x = rng.uniform(-5, 5, size=3); E, B = at(waves, x); m.append(root_dist(E, B))
    m = np.array(m); return (m < 1e-9).mean(), np.median(m)


for lab, p1, p2 in (("linear + linear", (1, 0), (0.6, 0.8)), ("linear + elliptisch", (1, 0), (1, 0.5j)),
                    ("linear + zirkular", (1, 0), (1, 1j)), ("elliptisch + elliptisch", (1, 0.3j), (1, 0.6j)),
                    ("zirkular + zirkular", (1, 1j), (1, 1j))):
    frac, med = two_wave_stats(p1, p2)
    print(f"(3) zwei Wellen, {lab:24s}: Anteil der Punkte mit Nullaugenblick {frac:.2f} (Median Wurzelabstand {med:.1e})")

# (4)
for name, pol in (("linear", (1, 0)), ("zirkular", (1, 1j)), ("elliptisch", (1, 0.4j))):
    E, B = plane_wave(np.array([0, 0, 1.0]), np.array(pol, complex))
    Fp, Fm = E + 1j * B, E - 1j * B
    # Helizitaetsanteile einer ebenen Welle: Projektion des Jones-Vektors auf (1, +i)/sqrt2 und (1, -i)/sqrt2
    j = np.array(pol, complex); hp, hm = abs(j @ np.array([1, -1j]) / np.sqrt(2)), abs(j @ np.array([1, 1j]) / np.sqrt(2))
    print(f"(4) {name:10s}: Helizitaetsgewichte {hp**2/(hp**2+hm**2):.3f} / {hm**2/(hp**2+hm**2):.3f}; Feld hat zeitliche Nullstelle:"
          f" {min(np.linalg.norm((E*np.exp(-1j*t)).real) for t in np.linspace(0, np.pi, 2001)) < 1e-3}")

# (5) allgemeines Feld aus 6 elliptischen Wellen: Vorzeichen von F auf einem Gitter
waves = []
for _ in range(6):
    k = rng.normal(size=3); pol = rng.normal(size=2) + 1j * rng.normal(size=2)
    waves.append((k, *plane_wave(k, pol, rng.uniform(0, 6))))
g = np.linspace(-3, 3, 31); Fs = np.zeros((31, 31, 31))
for i, xi in enumerate(g):
    for j_, yj in enumerate(g):
        for l, zl in enumerate(g):
            E, B = at(waves, np.array([xi, yj, zl])); Fs[i, j_, l] = F_sign(E, B)
neg = (Fs < 0).mean(); flips = (np.sign(Fs[1:]) != np.sign(Fs[:-1])).sum()
print(f"(5) 6 elliptische Wellen, Gitter 31^3: Anteil F < 0 (Ursprung in der Ellipse) {neg:.2f}, Vorzeichenwechsel entlang x: {flips}")
# Kontrolle: an einem Vorzeichenwechsel per Bisektion auf F = 0 gehen und s(t) direkt pruefen
idx = np.argwhere(np.sign(Fs[1:]) != np.sign(Fs[:-1]))[:5]; worst = 0.0
for i, j_, l in idx:
    lo, hi = np.array([g[i], g[j_], g[l]]), np.array([g[i + 1], g[j_], g[l]])
    flo = F_sign(*at(waves, lo))
    for _ in range(60):
        mid = (lo + hi) / 2; fm = F_sign(*at(waves, mid))
        if np.sign(fm) == np.sign(flo): lo, flo = mid, fm
        else: hi = mid
    E, B = at(waves, mid); sp, sm, w = invariants(E, B)
    x0 = [r for r in np.roots([np.conj(sm), 2 * w, sp]) if abs(abs(r) - 1) < 1e-6][0]
    t0 = -np.angle(x0) / 2                                  # x = e^{2iwt} mit s(t) ~ s+ e^{-2iwt}: Vorzeichen pruefen
    val = min(abs(s_of_t(E, B, t0)), abs(s_of_t(E, B, -t0)))
    zn = np.linalg.norm((E * np.exp(-1j * t0)).real) ** 2 + np.linalg.norm((B * np.exp(-1j * t0)).real) ** 2
    worst = max(worst, val / zn)
print(f"    an 5 Punkten der Flaeche F = 0: |s(t0)|/2u <= {worst:.1e} zur Wurzelzeit (Nullaugenblick), Feld != 0")
