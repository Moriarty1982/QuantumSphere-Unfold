"""(B1) rueckwaerts: Ist "Obstruktion = Boden |s|" mit der urspruenglichen C5-Definition vertraeglich? (Erkundung, nicht blind.)

Urspruenglich (v4.7.0-r04, def:v470-r04-c5-lowering-score): Phi_5 = ||rho_bd||^2 + ||rho_ext||^2 + ||rho_mix||^2, der Score ist das
Normquadrat des Residuums rho_5; also Phi_5 = 0 <=> rho_5 = 0 (notwendige Bedingung N1 an jede Obstruktionsgroesse O: O = 0 <=> Score = 0).
Lesart r10: Score = Inhalt im Kompensatorport C_HC = (1 + sigma_x)/2 des Dubletts (E, B); Kollar-Stufe = Dualitaetsdrehung um pi/6,
dann Kompensation (Projektion auf den Port).
(1) Auf der Kollar-Bahn: Boden |s| und Score nach jeder Kompensation.
(2) Am Nullaugenblick (r20.1): Boden 0, Score 1/2 des Inhalts -> N1 verletzt.
(3) Wo ist der Score 0 (N1 mit Boden)?  Nur bei leerem Kompensatorport, E = -B; dort ist der Boden maximal.
"""
import numpy as np

rng = np.random.default_rng(1120)


def rot(E, B, a):
    return E * np.cos(a) - B * np.sin(a), E * np.sin(a) + B * np.cos(a)


def comp(E, B):
    m = (E + B) / 2; return m, m


def content(E, B): return E @ E + B @ B
def score(E, B): m = (E + B) / 2; return 2 * (m @ m)
def floor(E, B): z = E + 1j * B; return abs(z @ z)


v = rng.normal(size=3); v /= np.linalg.norm(v) * np.sqrt(2)
E, B = v.copy(), v.copy()
print("(1) Kollar-Bahn (drehen um pi/6, dann kompensieren):")
for n in range(1, 6):
    E, B = comp(*rot(E, B, np.pi / 6))
    print(f"    n = {n}: Score {score(E, B):.5f} = (3/4)^n {0.75**n:.5f}; Boden |s| {floor(E, B):.5f}; Inhalt {content(E, B):.5f}")

Ec, Bc = np.array([1, 0, 0.3j]), np.array([0.7j, 1, 0])
e, b = Ec.real, Bc.real                      # t = 0
print(f"(2) Nullaugenblick r20.1: Boden/Inhalt {floor(e, b) / content(e, b):.1e}, Score/Inhalt {score(e, b) / content(e, b):.3f}")

E = rng.normal(size=3); B = -E
print(f"(3) E = -B: Score/Inhalt {score(E, B) / content(E, B):.3f}, Boden/Inhalt {floor(E, B) / content(E, B):.3f}")
print("    Score = 0 erzwingt E = -B und damit Boden = Inhalt (analytisch: b_x = -1 => |b| = 1)")
