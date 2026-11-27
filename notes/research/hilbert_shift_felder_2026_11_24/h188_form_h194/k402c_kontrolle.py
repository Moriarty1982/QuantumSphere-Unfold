"""k402c (Zusatzkontrolle zu H194c, im Geist der Vorab-Frage generisch/spezifisch):
Fairere Genericitaet - jedes zufaellige l-Tripel darf seine EIGENE beste der 6 Index-Permutationen nutzen,
so wie im echten Fall ueber Zuordnungen gesucht wurde. Sonst misst die Spezifitaet teils nur die (nachtraeglich
gewaehlte) Zuordnung B. Aufruf: python k402c_kontrolle.py > k402c_out.txt
"""
import numpy as np
from itertools import permutations
rng = np.random.default_rng(4022)
l = np.sort([1 + np.sqrt(2) * np.cos(2 / 9 + 2 * np.pi * k / 3) for k in range(3)])
mu = np.array([7.04e-6, 3.56e-3, 0.967]);   su = np.array([0.15e-6, 0.06e-3, 0.004])
md = np.array([1.54e-5, 3.06e-4, 1.630e-2]); sd = np.array([0.02e-5, 0.04e-4, 0.009e-2])
PRS = [(0, 1, 2), (0, 2, 1), (1, 2, 0)]
def basis(lv, perm):
    lk = np.array([lv[k] for (i, j, k) in PRS]); z = np.array([(lv[i] + lv[j]) ** 2 for (i, j, k) in PRS])
    return (lk / z)[perm], (lk ** 2 / z)[perm]
def fit_chi2(m, s, f1, f2):
    A = np.stack([f1 / s, f2 / s], axis=1); co, *_ = np.linalg.lstsq(A, m / s, rcond=None)
    pred = co[0] * f1 + co[1] * f2; return np.sum(((pred - m) / s) ** 2)
def best_over_perms(lv):
    bu = np.inf; bd = np.inf; both = np.inf
    for perm in permutations(range(3)):
        f1, f2 = basis(lv, list(perm))
        if not (np.all(np.isfinite(f1)) and np.all(np.isfinite(f2))):
            continue
        cu = fit_chi2(mu, su, f1, f2); cd = fit_chi2(md, sd, f1, f2)
        bu = min(bu, cu); bd = min(bd, cd); both = min(both, max(cu, cd))
    return bu, bd, both

# echter Fall (ueber alle Permutationen)
bu0, bd0, both0 = best_over_perms(l)
print(f"echte l_k, beste Permutation: Up chi2={bu0:.2f}, Down chi2={bd0:.2f}, worst={both0:.2f}")

NF = 5000
cu = cd = cb = 0
worst_list = []
for _ in range(NF):
    lr = np.sort(rng.uniform(0.01, 3.0, 3))
    bu, bd, both = best_over_perms(lr)
    worst_list.append(both)
    if bu <= bu0: cu += 1
    if bd <= bd0: cd += 1
    if max(bu, bd) <= max(bu0, bd0): cb += 1
worst_list = np.array(worst_list)
print(f"{NF} zufaellige l-Tripel, jeweils beste der 6 Permutationen:")
print(f"  Up erreicht/unterbietet {bu0:.2f}: {cu/NF:.2%}")
print(f"  Down erreicht/unterbietet {bd0:.2f}: {cd/NF:.2%}")
print(f"  BEIDE (worst <= {max(bu0,bd0):.2f}): {cb/NF:.2%}")
print(f"  Verteilung worst-chi2 der Zufalls-l: Median {np.median(worst_list):.1f}, "
      f"5%-Quantil {np.quantile(worst_list,0.05):.1f}, Minimum {worst_list.min():.1f}")
print(f"  (Der echte worst = {both0:.2f} liegt am Rang {(worst_list < both0).mean():.2%} der Zufalls-l.)")
