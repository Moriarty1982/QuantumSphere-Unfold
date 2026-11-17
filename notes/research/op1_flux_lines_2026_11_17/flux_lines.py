"""OP1, (S1'): Querungen oder Flusslinien?  Lage der Horizont-Punktierungen eines isolierten Horizonts auf der chi-Kugel.
(Erkundung, nicht blind: analytisch absehbar.)

Literatur (Eder-Sahlmann 1801.00747, Abschn. II.B, III.C): Am isolierten Horizont gilt T(l,l) = 0, also phi_0 = o^A o^B phi_AB = 0;
es quert keine Strahlung.  Uebrig bleibt phi_1 mit E_n = -2 Re phi_1, B_n = -2 Im phi_1: Punktierungen tragen elektrische und
magnetische Ladung (Flusslinien).  Hier: chi = (sqrt(F+.F+), sqrt(F-.F-)) wie in u1_check.py, F+- = E +- iB.
(1) reelle Felder (statische Flusslinien): Breite b = chi_z = 0 (P), fuer jede Richtung und jedes Verhaeltnis E_n : B_n.
(2) Dualitaet E + iB -> e^{ia}(E + iB) an einer Flusslinie: Azimut von chi dreht um -2a (mod pi, Wurzelwahl), Breite bleibt 0.
(3) Welche Felder liegen auf der Breite von M (b = 0,5363)?  Nur komplexe (positive Frequenz) mit |s-|/|s+| = beta^2.
(4) Poynting-Fluss durch die Normale fuer eine Flusslinie: E_n x B_n = 0 (keine Querung); fuer eine normal laufende Welle: nicht null.
"""
import numpy as np

rng = np.random.default_rng(7)
beta = 0.549406
bM = (1 - beta ** 2) / (1 + beta ** 2)


def chi(E, B):
    Fp, Fm = E + 1j * B, E - 1j * B
    sp, sm = Fp @ Fp, Fm @ Fm
    v = np.array([np.sqrt(sp + 0j), np.sqrt(sm + 0j)])
    return v / np.linalg.norm(v)


def bloch(v):
    X = np.array([[0, 1], [1, 0]]); Y = np.array([[0, -1j], [1j, 0]]); Z = np.diag([1, -1])
    return np.real([np.vdot(v, X @ v), np.vdot(v, Y @ v), np.vdot(v, Z @ v)])


n = np.array([0, 0, 1.0])
# (1) reelle Flusslinien: E = e n, B = m n (normal), plus beliebige reelle Felder
mx = 0.0
for _ in range(1000):
    e, m = rng.normal(size=2)
    mx = max(mx, abs(bloch(chi(e * n + 0j, m * n + 0j))[2]))
    E, B = rng.normal(size=3) + 0j, rng.normal(size=3) + 0j
    mx = max(mx, abs(bloch(chi(E, B))[2]))
print(f"(1) reelle Felder (Flusslinien und beliebige): max |chi_z| = {mx:.1e}  -> Breite 0 = P")

# (2) Dualitaet an einer Flusslinie
dev = 0.0
for _ in range(200):
    e, m = rng.normal(size=2); a = rng.uniform(0, np.pi)
    z = (e + 1j * m) * np.exp(1j * a)
    b1, b2 = bloch(chi(e * n + 0j, m * n + 0j)), bloch(chi(z.real * n + 0j, z.imag * n + 0j))
    ang = (np.arctan2(b2[1], b2[0]) - np.arctan2(b1[1], b1[0])) % (2 * np.pi); t = (-2 * a) % (2 * np.pi)
    d = min(abs(ang - t), 2 * np.pi - abs(ang - t)); dev = max(dev, min(d, abs(d - np.pi)), abs(b2[2]))
e, m = 1.0, 0.0
th = np.arctan2(m, e)
print(f"(2) Dualitaet an Flusslinien: Azimut dreht um -2a, Breite bleibt 0 (max. Abweichung {dev:.1e}); "
      f"Azimut = -2 arg(E_n + i B_n) bis auf Wurzelwahl, also der Ladungswinkel elektrisch/magnetisch")

# (3) komplexe Felder auf der Breite von M
E = np.array([1, 0, 0], complex)
def b_of(t):
    Ec = E + t * np.array([0, 1j, 0]); Bc = -1j * t * np.array([1, 0, 0]) + np.array([0, 1, 0]) * 0.3
    return bloch(chi(Ec, Bc))[2]
ts = np.linspace(0, 3, 3001); bs = np.array([b_of(t) for t in ts])
k = np.argmin(abs(abs(bs) - bM))
print(f"(3) Breite von M (b = {bM:.4f}) wird von komplexen Feldern erreicht (Beispiel t = {ts[k]:.3f}: b = {bs[k]:.4f}); "
      f"reelle Felder erreichen nur b = 0")

# (4) Poynting-Fluss durch die Normale
S_flux = np.cross(1.0 * n, 0.7 * n) @ n
Ew, Bw = np.array([1.0, 0, 0]), np.array([0, 1.0, 0])     # Welle laeuft entlang n
print(f"(4) Normalfluss S.n: Flusslinie {S_flux:.1e} (keine Querung), normal laufende Welle {np.cross(Ew, Bw) @ n:.1f}")
