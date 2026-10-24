"""k101: Lage des oberen Trefferfensters von Variante A (k97) auf feinem Gitter, als Bestimmung von eta = artanh(beta_sym) aus der Leptonmischung
unter der Lesart r55/r57/r60. Beobachtung fuer die Frame-Pruefung von OP1, kein Test."""
import sys, os, itertools, numpy as np
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
src = open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'k99_test_h44.py')).read()
exec(src[:src.index('\nK = {')])
grid = sorted(set(list(np.round(np.arange(0, 0.6, 0.01), 6)) + list(np.round(np.arange(0.590, 0.680 + 1e-12, 0.001), 6))))
Ce = charged(grid)
UN = np.array([Qphi(p, phi)[:, list(o)] for p in range(3) for phi in PHI for o in itertools.permutations(range(3))])
hits = {}
for e in grid:
    if e < 0.59 or e not in Ce: continue
    s12, s23, s13 = angles(Ce[e], UN); h, _ = evaluate(s12, s23, s13)
    if h.any(): hits[e] = (int(h.sum()), float(s23[h].min()), float(s23[h].max()))
es = sorted(hits)
print("Treffer (eps, Anzahl, sin^2 23 min, max):", [(round(e, 3),) + tuple(round(x, 4) for x in hits[e][1:]) + (hits[e][0],) for e in es])
if es:
    lo, hi = min(es), max(es)
    print(f"Fenster eta in [{lo:.3f}, {hi:.3f}] (Gitter 0.001) -> beta_sym = tanh(eta) in [{np.tanh(lo):.4f}, {np.tanh(hi):.4f}],"
          f" gamma_L = cosh(2 eta) in [{np.cosh(2*lo):.4f}, {np.cosh(2*hi):.4f}]; Vergleich gamma_BI/gamma_string = 1.864 (beta 0.5493), Hopf 2 (0.5774), Tribonacci 1.8393 (0.5437)")
