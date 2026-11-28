"""k433c (Nachtrag zu H220, nachtraeglich, nicht gewertet): Wie tief muesste die Suche fuer einen Treffer gehen?
Fuer jedes Ziel: kleinste Groesse bis 8 mit Treffer im 2-sigma-Fenster, dazu der Anteil getroffener Kontrollen bei dieser Tiefe."""
import math
import os
import sys

import numpy as np

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import bausteine_h220 as B  # noqa: E402
import k433_test_h220 as T  # noqa: E402

L = B.enumerate_struct(8)
sv, se = {}, {}
for s in range(1, 9):
    v = L[s][0][:, 0]; o = np.argsort(v); sv[s], se[s] = v[o], (L[s][1], o)
rng = np.random.default_rng(220)
for t in T.TARGETS:
    r = 2 * t[2] / t[1]
    lo, hi = t[1] * (1 - r), t[1] * (1 + r)
    hit = None
    for s in range(1, 9):
        i = np.searchsorted(sv[s], lo)
        if i < len(sv[s]) and sv[s][i] <= hi:
            ex, o = se[s]; hit = (s, ex[o[i]], sv[s][i]); break
    xs = t[1] * np.exp(rng.uniform(math.log(1 / 3), math.log(3), 1000))
    if hit:
        s = hit[0]
        fr = np.mean([any(np.searchsorted(sv[k], x * (1 + r), "right") > np.searchsorted(sv[k], x * (1 - r)) for k in range(1, s + 1)) for x in xs])
        print(f"{t[0]:26s} erster Treffer bei Groesse {s}: {hit[1]} = {hit[2]:.12g} ({(hit[2]-t[1])/t[2]:+.2f} sigma); "
              f"Kontrollen bis Groesse {s} getroffen: {fr:.3f}")
    else:
        print(f"{t[0]:26s} kein Treffer bis Groesse 8")
