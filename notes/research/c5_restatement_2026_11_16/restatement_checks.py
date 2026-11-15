"""C5 frame-sauber neu gestellt: Kontrollrechnungen (Erkundung, nicht blind; alle Ergebnisse stehen analytisch fest).

Doublet (E, B) wie v4.9.0-r04/r27/r28 und frame_audit.py (r20.4): b_z = (E^2 - B^2)/2u, b_x = 2 E.B/2u, 2u = E^2 + B^2,
s = (E + iB).(E + iB), |b| = |s|/2u.  Anteile C5_M = (1 + b_x)/2 (Kompensatorport), C5_T = (1 - b_x)/2 (Partnerport).
(1) Summe der Anteile 1; R (z -> iz) tauscht sie; |s| ist unter R, T, J_B fest.
(2) Gleiche Anteile <=> E.B = 0: notwendig, nicht hinreichend fuer den Photonpunkt P (|s| = 0).
(3) Leerer Kompensatorport (C5_M = 0) <=> E = -B: statisch erreichbar, Boden |s| = 2u maximal -> Verlagerung, keine Entladung.
(4) Bleibende Null: Zeitmittel von |s(t)|^2 = (|s+|^2 + 4|w|^2 + |s-|^2)/16; s(t) = 0 fuer alle t <=> s+ = s- = w = 0.
(5) Ebene Wellen (zirkular, linear) haben s+ = s- = w = 0: bleibend im Photonpunkt, von Anfang an.
(6) Kumulierte Anteile der Kollar-Rekursion: (3/4)^n = 1/2 hat keine ganzzahlige Loesung.
"""
from fractions import Fraction
import numpy as np

rng = np.random.default_rng(1116)


def disk(E, B):
    u2 = E @ E + B @ B
    return (E @ E - B @ B) / u2, 2 * (E @ B) / u2, abs((E + 1j * B) @ (E + 1j * B)) / u2


def invariants(E, B):
    Fp, Fm = E + 1j * B, E - 1j * B
    return Fp @ Fp, Fm @ Fm, Fp @ np.conj(Fm)


def s_of_t(E, B, t):
    z = (E * np.exp(-1j * t)).real + 1j * (B * np.exp(-1j * t)).real
    return z @ z


maps = {"R": lambda E, B: (-B, E), "T": lambda E, B: (E, -B), "J_B": lambda E, B: (B, E)}

# (1)
dev_sum = dev_swap = dev_floor = 0.0
for _ in range(1000):
    E, B = rng.normal(size=3), rng.normal(size=3)
    bz, bx, fl = disk(E, B); cM, cT = (1 + bx) / 2, (1 - bx) / 2
    dev_sum = max(dev_sum, abs(cM + cT - 1))
    _, bxR, _ = disk(*maps["R"](E, B)); dev_swap = max(dev_swap, abs((1 + bxR) / 2 - cT))
    for f in maps.values():
        dev_floor = max(dev_floor, abs(disk(*f(E, B))[2] - fl))
print(f"(1) 1000 Felder: |C5_M + C5_T - 1| <= {dev_sum:.1e}; R tauscht die Anteile (Abw. {dev_swap:.1e});"
      f" |s|/2u fest unter R, T, J_B (Abw. {dev_floor:.1e})")

# (2)
E, B = np.array([1.0, 0, 0]), np.array([0.0, 0.4, 0])
bz, bx, fl = disk(E, B)
print(f"(2) E senkrecht B, |E| != |B|: C5_M = {(1 + bx) / 2:.3f} = C5_T, aber |s|/2u = {fl:.3f} != 0 (nicht P);"
      f" reines E-Feld: C5_M = {(1 + disk(E, 0 * B)[1]) / 2:.3f}, |s|/2u = {disk(E, 0 * B)[2]:.3f}")

# (3)
E = rng.normal(size=3); B = -E
bz, bx, fl = disk(E, B)
print(f"(3) E = -B (statisch): C5_M = {(1 + bx) / 2:.3f}, C5_T = {(1 - bx) / 2:.3f}, |s|/2u = {fl:.3f} (Boden maximal)")

# (4)
ts = np.linspace(0, 2 * np.pi, 4096, endpoint=False); dev = 0.0
for _ in range(300):
    E, B = rng.normal(size=3) + 1j * rng.normal(size=3), rng.normal(size=3) + 1j * rng.normal(size=3)
    sp, sm, w = invariants(E, B)
    mean = np.mean([abs(s_of_t(E, B, t)) ** 2 for t in ts])
    pred = (abs(sp) ** 2 + 4 * abs(w) ** 2 + abs(sm) ** 2) / 16
    dev = max(dev, abs(mean - pred) / pred)
print(f"(4) Zeitmittel von |s(t)|^2 = (|s+|^2 + 4|w|^2 + |s-|^2)/16 (300 Felder, rel. Abw. {dev:.1e});"
      " bleibende Null <=> s+ = s- = w = 0")
E, B = np.array([1, 0, 0.3j]), np.array([0.7j, 1, 0])
sp, sm, w = invariants(E, B)
print(f"    Beispielfeld r20.1: Zeitmittel {(abs(sp) ** 2 + 4 * abs(w) ** 2 + abs(sm) ** 2) / 16:.4f} > 0:"
      " Nullaugenblick, keine bleibende Null")

# (5)
for name, E, B in (("zirkular", np.array([1, 1j, 0]), np.array([-1j, 1, 0])),
                   ("linear", np.array([1, 0, 0], complex), np.array([0, 1, 0], complex))):
    sp, sm, w = invariants(E, B)
    smax = max(abs(s_of_t(E, B, t)) for t in ts[::16])
    print(f"(5) ebene Welle, {name}: |s+|, |s-|, |w| = {abs(sp):.1e}, {abs(sm):.1e}, {abs(w):.1e}; max |s(t)| = {smax:.1e}")

# (6)
q = Fraction(3, 4); hit = [n for n in range(1, 200) if q ** n == Fraction(1, 2)]
print(f"(6) (3/4)^n = 1/2 fuer ganzzahliges n: {hit or 'keine Loesung'}; reell n = {np.log(2) / np.log(4 / 3):.4f};"
      f" (3/4)^2 = {float(q ** 2):.4f}, (3/4)^3 = {float(q ** 3):.4f}")
