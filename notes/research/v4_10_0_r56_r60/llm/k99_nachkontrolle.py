import sys; sys.path.insert(0, '.')
src = open('./k99_test_h44.py').read()
exec(src[:src.index('\nK = {')])
import numpy as np
cand = [2/9, 0.5493**2, 1/3, np.pi/9, 0.5, np.pi/6, 0.5493, 1/np.sqrt(3), 2/3, 1/np.sqrt(2), 0.75, 1.0]
grid = sorted(set(list(np.round(np.arange(0, 1.0 + 1e-12, 0.01), 6)) + [round(c, 10) for c in cand]))
Ce = charged(grid)
UN = np.array([Qphi(p, phi)[:, list(o)] for p in range(3) for phi in PHI for o in itertools.permutations(range(3))])
hits = {}
for e in grid:
    if e not in Ce: continue
    s12, s23, s13 = angles(Ce[e], UN); h, _ = evaluate(s12, s23, s13)
    if h.any(): hits[e] = int(h.sum())
print("eps_e mit Treffern (Variante A):", {round(k, 4): v for k, v in hits.items()})
print("Zweige vorhanden bei Kandidaten:", {round(c, 4): (round(c, 10) in Ce) for c in cand})
