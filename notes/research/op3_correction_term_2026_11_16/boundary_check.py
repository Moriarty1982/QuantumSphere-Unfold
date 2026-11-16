"""Undurchlaessiger Rand: zwei analytische Pruefungen, numerisch bestaetigt.
(1) Die Kanten des Oktanten liegen auf den Grosskreisen x=0, y=0, z=0, den Fixkreisen der drei Spiegelungen; antilineare Abbildungen (K) wirken auf
    der Bloch-Kugel als Spiegelung.  Berry-Fluss (Bargmann-Phase) wechselt unter Spiegelung das Vorzeichen: pseudoskalar.
(2) Mit undurchlaessigem Rand und einer Senke im Innern ist der sparsamste Abfluss eine Scheibe um die Senke mit Raumwinkel 2*Delta, Lage frei,
    solange sie den Rand nicht beruehrt; Kosten unabhaengig von der Lage."""
import numpy as np
def coh(n):
    n = np.asarray(n, float) / np.linalg.norm(n); th, ph = np.arccos(n[2]), np.arctan2(n[1], n[0])
    return np.array([np.cos(th / 2), np.exp(1j * ph) * np.sin(th / 2)])
def phase(g): return np.angle(np.vdot(g[0], g[1]) * np.vdot(g[1], g[2]) * np.vdot(g[2], g[0]))
E = [[0, 0, 1], [1, 0, 0], [0, 1, 0]]
g = [coh(e) for e in E]; gK = [np.conj(x) for x in g]
print(f"(1) Bargmann-Phase Oktant {phase(g):+.6f}, nach komplexer Konjugation K {phase(gK):+.6f} (Vorzeichen gewechselt: pseudoskalar)")
rng = np.random.default_rng(1); ok = True
for _ in range(200):
    n = rng.normal(size=(3, 3)); gg = [coh(v) for v in n]
    ok &= abs(phase(gg) + phase([np.conj(x) for x in gg])) < 1e-12
print(f"    an 200 Zufallsdreiecken: Phase(K g) = -Phase(g): {ok}")
D = np.pi / 4 - 0.666674
Om = 2 * D; alpha = np.arccos(1 - Om / (2 * np.pi))
print(f"(2) Raumwinkel der geleerten Scheibe = 2*Delta = {Om:.6f} sr (gamma_M = 0.237533), Radius {np.degrees(alpha):.2f} Grad;"
      f" Abstand Schwerpunkt-Kante 35.26 Grad -> Lage der Scheibe frei in einem Bereich von {35.26 - np.degrees(alpha):.2f} Grad um die Mitte")
# Kosten W2 einer Scheibe zur Senke im Mittelpunkt: int r^2 dm, Dichte 1/2
r = np.linspace(0, alpha, 20001); dm = 0.5 * 2 * np.pi * np.sin(r)
print(f"    Kosten (Masse zur Senke im Mittelpunkt): {np.trapezoid(r**2 * dm, r):.3e}, unabhaengig von der Lage (Isometrie)")
