"""k254c: Die drei Spiegelungen aus k254b halten je eine 8-dim. Unteralgebra von S fest. Pruefen: abgeschlossen, Oktonionen-artig
(alternativ, normmultiplikativ), paarweise Schnitt. Aufruf aus diesem Ordner."""
import numpy as np
src = open("../k253_cayley_dickson_turm.py").read().split("for n in range(0, 6):")[0]
ns = {}; exec(src, ns); mul = ns["mul"]
rng = np.random.default_rng(2543); E = np.eye(16); s3 = np.sqrt(3) / 2
subs = {}
for name, (c, s) in {"O_0 (Winkel 0)": (1, 0), "O_120": (-0.5, s3), "O_240": (-0.5, -s3)}.items():
    # fester Vektor der Spiegelung in der Vielfachheitsebene: (cos(th/2), sin(th/2)) mit th = 0, 120, 240 Grad
    th = np.arctan2(s, c) / 2; u, v = np.cos(th), np.sin(th)
    B = [E[0]] + [u * E[i] + v * E[i + 8] for i in range(1, 8)]
    subs[name] = np.array(B)
for name, B in subs.items():
    P = B.T @ np.linalg.pinv(B.T)
    clos = max(np.abs(P @ mul(x, y) - mul(x, y)).max() for x in B for y in B)
    w_alt = w_norm = 0
    for _ in range(200):
        x, y = rng.normal(size=8) @ B, rng.normal(size=8) @ B
        w_alt = max(w_alt, np.abs(mul(mul(x, x), y) - mul(x, mul(x, y))).max())
        w_norm = max(w_norm, abs(np.linalg.norm(mul(x, y)) - np.linalg.norm(x) * np.linalg.norm(y)))
    print(f"{name}: abgeschlossen {clos:.1e}, alternativ {w_alt:.1e}, normmultiplikativ {w_norm:.1e}")
names = list(subs)
for i in range(3):
    for j in range(i + 1, 3):
        r = np.linalg.matrix_rank(np.vstack([subs[names[i]], subs[names[j]]]), tol=1e-9)
        print(f"dim({names[i]} ∩ {names[j]}) = {16 - r}")
