"""Erkundung: Umkehrwalze (r02) auf der Spin-1/2-Kugel der Generationen.
Antilineare Involutionen auf C^2: Theta = U K. Fixpunktfrei auf Strahlen genau dann, wenn Theta^2 = -1 (Kramers);
dann ist die Wirkung auf den Bloch-Vektor die Antipodenabbildung n -> -n. Bei Theta^2 = +1 gibt es Fixstrahlen (Spiegelung)."""
import numpy as np
sx = np.array([[0, 1], [1, 0]], complex); sy = np.array([[0, -1j], [1j, 0]]); sz = np.diag([1, -1]).astype(complex)
bloch = lambda v: np.real([np.vdot(v, s @ v) for s in (sx, sy, sz)]) / np.vdot(v, v).real
rng = np.random.default_rng(127)
for name, U in (("K (Theta^2 = +1)", np.eye(2)), ("i sigma_y K (Theta^2 = -1)", 1j * sy)):
    sq = U @ U.conj()
    maps = []
    for _ in range(5):
        v = rng.normal(size=2) + 1j * rng.normal(size=2)
        w = U @ v.conj()
        maps.append((bloch(v), bloch(w)))
    anti = all(np.allclose(b, -a) for a, b in maps)
    fixed = abs(np.vdot(maps[0][0], maps[0][1]) - 1) < 1e-9
    print(f"{name:28s} Theta^2 = {np.round(sq[0,0].real):+.0f}; Antipodenabbildung: {anti}; Beispiel n -> {np.round(maps[0][0],3)} -> {np.round(maps[0][1],3)}")
core = np.ones(3) / np.sqrt(3); anti = -core
print("Kern auf der Zyklusachse", np.round(core, 4), "-> Gegenpol", np.round(anti, 4))
print("Gegenpol im Oktanten x,y,z > 0:", bool((anti > 0).all()), "; im 90-Grad-Mond x,y > 0 (Neutrino-Figur):", bool((anti[:2] > 0).all()))
