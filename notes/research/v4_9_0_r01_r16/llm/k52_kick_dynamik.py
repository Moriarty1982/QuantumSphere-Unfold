"""k52: Vorschlag einer minimalen Dynamik fuer Lesart B: gekickte Dualitaetsdynamik (Erkundung K5, Modellvorschlag).

Zwischen den Kicks: Dualitaetsdrehung z(t) = e^{i w t} z (auf dem Dublett: F -> F R(wt)^T).
Bei t_n = n tau: Kompensator C_HC (Auslese); der Anteil im A-Port geht an ein Reservoir (wird exportiert).
Geprueft: Stufenfaktor, Energiebilanz mit Reservoir, Bloch-Bild, Zyklen (3, 6, 12 Stufen), Aenderung von s, Zeno-Grenze.
"""
import math
import numpy as np

sx = np.array([[0., 1], [1, 0]]); I2 = np.eye(2)
C = 0.5 * (I2 + sx); A = 0.5 * (I2 - sx)
R = lambda a: np.array([[math.cos(a), -math.sin(a)], [math.sin(a), math.cos(a)]])
rng = np.random.default_rng(52)

def run(F, wtau, n):
    res, out = 0.0, []
    for _ in range(n):
        G = F @ R(wtau).T              # Drehung zwischen den Kicks
        res += np.sum((G @ A) ** 2)    # exportiert
        F = G @ C                      # Kompensation
        out.append(np.sum(F ** 2))
    return F, out, res

F0 = rng.normal(size=(3, 2)); F0 = F0 @ C; F0 /= math.sqrt(np.sum(F0 ** 2))   # Start im C-Port, Energie 1
F, out, res = run(F0, math.pi / 6, 20)
print("1. w tau = pi/6: Energie nach Stufe 1..4: %s; Stufe 20: %.6f = (3/4)^20 = %.6f" %
      ([round(x, 6) for x in out[:4]], out[19], 0.75 ** 20))
print("   Bilanz: verbleibend + exportiert = %.12f" % (out[19] + res))
print("   eindeutig: q = cos^2(w tau) = 3/4 in (0, pi/2) nur fuer w tau = %.6f = pi/6" % math.acos(math.sqrt(0.75)))

print("\n2. Bloch-Bild (r04): Drehung um 2 w tau = 60 Grad, dann Messung laengs sigma_x")
G = F0.T @ F0; b = np.array([G[0, 0] - G[1, 1], 2 * G[0, 1]]) / np.trace(G)
print("   Start b = %s (J-Achse); Behaltewahrscheinlichkeit (1 + cos 60)/2 = %.4f" % (np.round(b, 6), (1 + math.cos(math.pi / 3)) / 2))

print("\n3. Zyklen der Dualitaetsphase")
for k, txt in ((3, "Vierteldrehung Materie -> Tachyon (pi/2)"), (6, "halbe Drehung pi: z -> -z, Ladungskonjugation (r02)"),
               (12, "volle Drehung 2 pi: z -> z"), (24, "Spinor zurueck (psi -> psi, r06.4)")):
    print("   %2d Stufen: Phase %5.1f Grad, %s; behalten (3/4)^%d = %.5f" % (k, 30 * k, txt, k, 0.75 ** k))

print("\n4. Die Kompensation aendert s (die Drehung nur seine Phase)")
z = rng.normal(size=3) + 1j * rng.normal(size=3)
s0 = z @ z
zr = np.exp(1j * math.pi / 6) * z
Fr = np.column_stack([zr.real, zr.imag]) @ C; zc = Fr[:, 0] + 1j * Fr[:, 1]
print("   |s| vorher %.4f, nach Drehung %.4f, nach Kompensation %.4f (Re s = %.1e)" % (abs(s0), abs(zr @ zr), abs(zc @ zc), (zc @ zc).real))

print("\n5. Zeno-Grenze: dieselbe Phase pi/6 in m Teilkicks")
for m in (1, 2, 5, 50):
    print("   m = %2d: behalten %.6f" % (m, math.cos(math.pi / (6 * m)) ** (2 * m)))

print("\n6. Endlicher Abschluss? Behalten nach n Stufen = (3/4)^n > 0 fuer jedes n; null nur bei w tau = pi/2,")
print("   und dann liegt alles im Reservoir (Export, keine Vernichtung).")
