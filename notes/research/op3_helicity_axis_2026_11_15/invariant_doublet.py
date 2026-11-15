"""Das Lorentz-invariante Dublett chi = (sqrt s+, sqrt s-) (Erkundung, nicht blind).

s+- = (E +- iB).(E +- iB) (bilinear). Bezug: v4.8.0-r06.3 (SO(3,C)-Bahnen = Niveaumengen von s), v4.9.0-r04.2,
r05.2, r51. Bloch-Koordinaten von chi: z = Helizitaetsachse, Aequatorwinkel = arg(conj(sqrt s+) sqrt s-),
fuer reelle Felder = -arg s (Orientierungskonvention).
"""
import numpy as np

rng = np.random.default_rng(2026)

def boost(E, B, v, n):
    n = n / np.linalg.norm(n); g = 1 / np.sqrt(1 - v * v); vv = v * n
    return (g * (E + np.cross(vv, B)) - (g - 1) * np.dot(E, n) * n,
            g * (B - np.cross(vv, E)) - (g - 1) * np.dot(B, n) * n)

def spm(E, B):
    Fp, Fm = E + 1j * B, E - 1j * B
    return np.dot(Fp, Fp), np.dot(Fm, Fm)

def bloch(chi):
    a, b = chi / np.linalg.norm(chi)
    return np.array([2 * (np.conj(a) * b).real, 2 * (np.conj(a) * b).imag, abs(a) ** 2 - abs(b) ** 2])

def chi_of(E, B, compatible=True, flip=False):
    sp, sm = spm(E, B)
    rp = np.sqrt(sp + 0j)
    # konjugationsvertraegliche Wahl: fuer reelle Felder sqrt s- = conj sqrt s+
    rm = np.conj(rp) if (compatible and abs(sm - np.conj(sp)) < 1e-12) else np.sqrt(sm + 0j)
    if flip: rm = -rm
    return np.array([rp, rm])

# (1) Invarianz von s+- unter Boosts, komplexe Amplituden
dev = 0.0
for _ in range(500):
    E, B = rng.normal(size=3) + 1j * rng.normal(size=3), rng.normal(size=3) + 1j * rng.normal(size=3)
    Ep, Bp = boost(E, B, rng.uniform(0.05, 0.95), rng.normal(size=3))
    dev = max(dev, max(abs(np.array(spm(Ep, Bp)) - np.array(spm(E, B)))) / max(1, max(abs(np.array(spm(E, B))))))
print(f"(1) s+ und s- unter 500 Boosts invariant: max. rel. Abweichung {dev:.1e}")

# (2) Reelle Felder liegen auf dem Aequator, Winkel = arg s
mx = 0.0
for _ in range(300):
    E, B = rng.normal(size=3), rng.normal(size=3)
    s = np.dot(E + 1j * B, E + 1j * B); bl = bloch(chi_of(E, B))
    mx = max(mx, abs(bl[2]), abs(np.angle(np.exp(1j * (np.arctan2(bl[1], bl[0]) + np.angle(s))))))
print(f"(2) Reelle Felder: Helizitaetskomponente 0 und Aequatorwinkel = -arg s (max. Abweichung {mx:.1e})")

# (3) Wirkung von R, T, J_B auf reelle Felder (vertraegliche Wurzelwahl)
maps = {"R (E,B)->(-B,E)": lambda E, B: (-B, E), "T (E,B)->(E,-B)": lambda E, B: (E, -B),
        "J_B (E,B)->(B,E)": lambda E, B: (B, E)}
for name, f in maps.items():
    E, B = rng.normal(size=3), rng.normal(size=3)
    b0, b1 = bloch(chi_of(E, B)), bloch(chi_of(*f(E, B)))
    s0, s1 = np.dot(E + 1j * B, E + 1j * B), np.dot(*(lambda e, b: (e + 1j * b, e + 1j * b))(*f(E, B)))
    print(f"(3) {name}: arg s {np.angle(s0):+.4f} -> {np.angle(s1):+.4f}; Bloch {np.round(b0, 3)} -> {np.round(b1, 3)}")
print("    Erwartung r04.2(b): R dreht um pi, T spiegelt arg s -> -arg s, J_B spiegelt arg s -> pi - arg s")

# (3b) Helizitaet unter R, T, J_B fuer komplexe Felder (Betraege, unabhaengig von der Wurzelwahl)
for name, f in maps.items():
    E, B = rng.normal(size=3) + 1j * rng.normal(size=3), rng.normal(size=3) + 1j * rng.normal(size=3)
    z0, z1 = bloch(chi_of(E, B))[2], bloch(chi_of(*f(E, B)))[2]
    print(f"(3b) {name}: Helizitaetskomponente {z0:+.4f} -> {z1:+.4f}")

# (4) Zweigwahl: die andere Wurzel von s- gibt den um pi um die Helizitaetsachse gedrehten Punkt (= R-Bild)
E, B = rng.normal(size=3) + 1j * rng.normal(size=3), rng.normal(size=3) + 1j * rng.normal(size=3)
a, b = bloch(chi_of(E, B)), bloch(chi_of(E, B, flip=True))
print(f"(4) Zweigwahl: {np.round(a, 4)} vs. {np.round(b, 4)}; z gleich, (x,y) -> -(x,y): "
      f"{np.allclose(b, a * [-1, -1, 1])}")

# (5) Ein invariantes Oktant: Materiefeld, Photonseite, selbstduales Feld
fields = {"Materie (s = 1)": (np.array([1, 0, 0.]), np.zeros(3)),
          "Photonseite (s = i)": (np.array([1, 0, 0.]) / np.sqrt(2), np.array([1, 0, 0.]) / np.sqrt(2)),
          "selbstdual (E = iB, s- = 0)": (np.array([1j, 0, 0]), np.array([1, 0, 0.]))}
chis = []
for name, (E, B) in fields.items():
    c = chi_of(E, B); c = c / np.linalg.norm(c); chis.append(c)
    print(f"(5) {name}: s+ = {spm(E, B)[0]:.3f}, s- = {spm(E, B)[1]:.3f}, Bloch {np.round(bloch(c), 4)}")
G = np.array([[abs(np.vdot(u, w)) for w in chis] for u in chis])
ph = np.angle(np.vdot(chis[0], chis[1]) * np.vdot(chis[1], chis[2]) * np.vdot(chis[2], chis[0]))
print(f"    Ueberlappungen^2 {np.round(G[np.triu_indices(3, 1)] ** 2, 6)}, K = {np.trace(G @ G) / np.trace(G) ** 2:.6f},"
      f" Bargmann-Phase/pi = {ph / np.pi:+.4f}")
ok = True
for _ in range(50):
    v, n = rng.uniform(0.1, 0.9), rng.normal(size=3)
    for (E, B), c in zip(fields.values(), chis):
        Ep, Bp = boost(E, B, v, n); cp = chi_of(Ep, Bp); cp = cp / np.linalg.norm(cp)
        ok &= abs(abs(np.vdot(c, cp)) - 1) < 1e-9
print(f"    Alle drei Zustaende unter 50 Boosts als Strahlen unveraendert: {ok}")
