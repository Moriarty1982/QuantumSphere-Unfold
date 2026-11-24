"""k253c: Erzeugungsregel psi' = u*omega*psi (Linksmultiplikation mit Einheits-Imaginaerer u).
Prueft, ob L_u^2 = -1 (geschlossene Kreisbahn, Periode 2pi/omega) fuer zufaellige u in A_n gilt."""
import numpy as np, importlib.util, sys
spec = importlib.util.spec_from_file_location("k", "k253_cayley_dickson_turm.py")
src = open("k253_cayley_dickson_turm.py").read().split("for n in range(0, 6):")[0]
ns = {}; exec(src, ns); mul = ns["mul"]
rng = np.random.default_rng(2531)
for n in range(1, 6):
    N = 2 ** n; worst = 0
    for _ in range(200):
        u = rng.normal(size=N); u[0] = 0; u /= np.linalg.norm(u)
        L = np.array([mul(u, e) for e in np.eye(N)]).T
        worst = max(worst, np.abs(L @ L + np.eye(N)).max())
    print(f"n={n} dim={N:2d}: max |L_u^2 + 1| ueber 200 zufaellige u = {worst:.2e}")
