"""OP1, Setzung (S1)/(A): elementarer Strang = Quant von chi; Frame-Abbildungen wirken auf die Punktierung ueber dieselbe SU(2) wie auf chi.
(Erkundung, nicht blind)

(1) Wirkt die raeumliche Drehgruppe (die SU(2) des Punktierungsspins) auf chi?  s+- unter zufaelligen Drehungen (und Boosts, r16.3).
(2) Masselose Lesart (S1'): Strang = masseloses Quant, das den Horizont entlang der Normalen quert; Helizitaet lambda = J . p.
    Wirkung von R, T, J_B auf das Vorzeichen der Helizitaet (r16.3(b)) und auf die Ausbreitungsrichtung (Poynting E x B), an Feldern
    mit Ausbreitungsrichtung (zirkular polarisierte ebene Welle als Vertreter der Helizitaet; Poynting fuer reelle Momentaufnahme).
    Daraus J_nu = lambda * (p . nu) an einer festen Normalen nu.
(3) Kleine Gruppe masseloser Teilchen: nur Helizitaet +-j -> Gewicht 2 je j (DL); massive Punktierung: 2j+1 (GM).
"""
import numpy as np
from scipy.spatial.transform import Rotation

rng = np.random.default_rng(11)
dev = 0.0
for _ in range(500):
    E, B = rng.normal(size=3) + 1j * rng.normal(size=3), rng.normal(size=3) + 1j * rng.normal(size=3)
    Rm = Rotation.random(random_state=rng.integers(1e9)).as_matrix()
    sp = (E + 1j * B) @ (E + 1j * B); sm = (E - 1j * B) @ (E - 1j * B)
    E2, B2 = Rm @ E, Rm @ B
    sp2 = (E2 + 1j * B2) @ (E2 + 1j * B2); sm2 = (E2 - 1j * B2) @ (E2 - 1j * B2)
    dev = max(dev, abs(sp - sp2), abs(sm - sm2))
print(f"(1) s+- unter 500 zufaelligen Drehungen: max. Abweichung {dev:.1e} -> chi ist ein Singulett der raeumlichen Drehgruppe")

# (2) zirkular polarisierte ebene Welle entlang z: E = (1, i*lam, 0), B = k x E = z x E
def wave(lam):
    E = np.array([1, 1j * lam, 0], complex); B = np.cross([0, 0, 1], E)
    return E, B

def helicity(E, B):
    # Vorzeichen der Helizitaet: Anteil an F+ = E + iB gegen F- = E - iB (selbstdual gegen antiselbstdual)
    Fp, Fm = E + 1j * B, E - 1j * B
    return int(np.sign(np.linalg.norm(Fp) - np.linalg.norm(Fm)))

def poynting(E, B):
    return np.real(np.cross(E, np.conj(B)))

MAPS = {"R: (E,B) -> (-B, E)": lambda E, B: (-B, E), "T: (E,B) -> (E,-B)": lambda E, B: (E, -B), "J_B: (E,B) -> (B, E)": lambda E, B: (B, E)}
nu = np.array([0, 0, 1.0])
for lam in (+1, -1):
    E, B = wave(lam); h0, p0 = helicity(E, B), np.sign(poynting(E, B) @ nu)
    print(f"(2) Welle Helizitaet {h0:+d}, Richtung entlang Normale {p0:+.0f}, J_nu = {h0 * p0:+.0f}")
    for name, f in MAPS.items():
        E2, B2 = f(E, B); h, p = helicity(E2, B2), np.sign(poynting(E2, B2) @ nu)
        print(f"      {name:22s}: Helizitaet {h:+d}, Richtung {p:+.0f}, J_nu = {h * p:+.0f}")

js = np.arange(1, 9) / 2
print("(3) Zustaende je j an einer Punktierung: masselos (nur Helizitaet +-j)", [2] * len(js), "| massiv (2j+1)", (2 * js + 1).astype(int).tolist())
