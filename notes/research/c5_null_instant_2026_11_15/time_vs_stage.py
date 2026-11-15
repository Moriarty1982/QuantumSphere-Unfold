"""C5, Luecke 3: Laesst sich die Zeit eines Nullaugenblicks einer Kollar-Stufe zuordnen? (Erkundung, nicht blind)

Kollar-Stufe nach v4.9.0-r10.1/r27: Dualitaetsdrehung um alpha = pi/6, dann Kompensation. Dualitaet: F+ -> e^{-i a} F+,
F- -> e^{+i a} F-. Zeitverschiebung: E^, B^ -> e^{-i w dt} E^, B^, also F+ -> e^{-i w dt} F+, F- -> e^{-i w dt} F-.
(1) Fuer welche Felder wirkt eine Zeitverschiebung auf das augenblickliche Feld z(t) wie eine Dualitaetsdrehung?
(2) Haben diese Felder Nullaugenblicke?
(3) Fuer Felder mit Nullaugenblick: Abstand der Zeitentwicklung von jeder Dualitaetsdrehung.
"""
import numpy as np

rng = np.random.default_rng(3)


def z_of_t(E, B, t):
    return (E * np.exp(-1j * t)).real + 1j * (B * np.exp(-1j * t)).real


def from_F(Fp, Fm):
    return (Fp + Fm) / 2, (Fp - Fm) / 2j


# (1) reine Helizitaet: F- = 0  ->  z(t) = (F+ e^{-it} + conj(F-) e^{it})/2 = F+ e^{-it}/2
Fp = rng.normal(size=3) + 1j * rng.normal(size=3)
E, B = from_F(Fp, np.zeros(3, complex))
dev = max(np.abs(z_of_t(E, B, t) - np.exp(-1j * t) * z_of_t(E, B, 0)).max() for t in np.linspace(0, 3, 50))
print(f"(1) reine Helizitaet (F- = 0): Zeitverschiebung um t = Dualitaetsdrehung z -> e^(-it) z (max. Abweichung {dev:.1e})")
ss = [abs(z_of_t(E, B, t) @ z_of_t(E, B, t)) for t in np.linspace(0, np.pi, 400)]
print(f"(2) |s(t)| konstant: min {min(ss):.4f}, max {max(ss):.4f} -> kein Nullaugenblick (ausser s+ = 0, dann immer lichtartig)")

# (3) Feld mit Nullaugenblick (aus null_instant.py): Abstand von jeder Dualitaetsdrehung
E = np.array([1, 0, 0.3j]); B = np.array([0.7j, 1, 0])
Fp, Fm = E + 1j * B, E - 1j * B
print(f"    Feld mit Nullaugenblick: |F+| = {np.linalg.norm(Fp):.3f}, |F-| = {np.linalg.norm(Fm):.3f} (beide Helizitaeten)")
best = []
for t in np.linspace(0.05, np.pi - 0.05, 60):
    zt, z0 = z_of_t(E, B, t), z_of_t(E, B, 0)
    alphas = np.linspace(0, 2 * np.pi, 3601)
    res = min(np.linalg.norm(zt - np.exp(-1j * a) * z0) / np.linalg.norm(zt) for a in alphas)
    best.append(res)
print(f"(3) Zeitentwicklung gegen beste Dualitaetsdrehung: relativer Rest min {min(best):.3f}, Median {np.median(best):.3f}"
      f" -> die Zeitentwicklung ist keine Folge von Kollar-Stufen")
