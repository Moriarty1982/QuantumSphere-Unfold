"""k450c (Nachtrag, nachtraeglich, nicht gewertet): H235 bei kleinem q, wenn der Versatz ganz aus phi kommt (statt aus dem H167-Fit q = -0,0852).
Aufruf aus diesem Ordner: python3 k450c_kleines_q.py > k450c_out.txt
"""
import numpy as np
from scipy.optimize import brentq
src = open("k450_test_h235.py").read().split('print("=" * 96)')[0]
exec(src)
print("k450c  Nachtrag: kleines q (Versatz aus phi), Gewichte (2, 1), Fermionen-Vorzeichen")
for q in (-0.01, -0.001, -1e-4):
    tq = lambda p: tree(p, q)
    g = np.linspace(0.0, 0.2, 201)
    f = [tq(p)[2] - X for p in g]
    px = [brentq(lambda p: tq(p)[2] - X, g[i], g[i + 1], xtol=1e-15) for i in range(200) if f[i] * f[i + 1] < 0 and abs(f[i] - f[i + 1]) < 0.05][0]
    Et, dEt, oI, oR = tq(px)
    k = -dEt / Cp(px, 2, 1)
    EE = lambda p: tq(p)[0] + k * C(p, 2, 1)
    h = 1e-5
    d2 = (EE(px + h) - 2 * EE(px) + EE(px - h)) / h ** 2
    ph = np.linspace(0, 2 * np.pi / 3, 1441, endpoint=False)
    ev = np.array([EE(p) for p in ph]); i = int(np.argmin(ev))
    print(f"  q = {q:g}: phi_x = {px:.7f}, x_nu,pred = {oR:.6f} ({(oR - XNU)/SXNU:+.2f} sigma), kappa* = {k:+.3e} (kappa*/|q| = {k/abs(q):+.4f}),"
          f" d2E = {d2:+.3e}, globales Minimum bei {ph[i]:.4f} (E {ev[i]:.8f} gegen E(phi_x) {EE(px):.8f})")
