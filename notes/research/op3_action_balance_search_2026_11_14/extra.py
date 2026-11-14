"""Natural multi-term candidates and size profile of the 0/1 hits (supplement to search.py)."""
import itertools, sys
from collections import Counter
sys.path.insert(0, ".")
import search as s
import numpy as np
names = [f"{g},w^{k}" for g, k, _ in s.PROJ]
def run(w):
    H = -sum(x * P for x, (_, _, P) in zip(w, s.PROJ) if x)
    gap, psi = s.ground(H)
    return round(gap, 6), [(sl, round(K, 6), round(ph/np.pi, 4)) for sl, K, ph in s.orbit_data(psi)]
idx = {n: i for i, n in enumerate(names)}
def vec(terms):
    w = [0]*12
    for t in terms: w[idx[t]] = 1
    return w
print("eigenvalue-1 lines of all four:", run(vec(["D,w^0", "tau,w^0", "tauD,w^0", "tauD2,w^0"])))
print("eigenvalue-1 lines of D,tau,tauD:", run(vec(["D,w^0", "tau,w^0", "tauD,w^0"])))
print("D,tau eigenvalue-1 pair:", run(vec(["D,w^0", "tau,w^0"])))
print("all three D lines + tau line:", run(vec(["D,w^0","D,w^1","D,w^2","tau,w^0"])))
sizes = Counter(); pairs_total = 0; pairs_hit = 0
for w in itertools.product((0, 1), repeat=12):
    if not any(w): continue
    h = s.classify(w)
    n = sum(w)
    if n == 2:
        a, b = [i for i, x in enumerate(w) if x]
        if s.PROJ[a][0] != s.PROJ[b][0]:
            pairs_total += 1; pairs_hit += bool(h)
    if h: sizes[n] += 1
print("0/1 hits by number of terms:", dict(sorted(sizes.items())))
print("pairs from different subgroups:", pairs_hit, "of", pairs_total)
# Reduction: drop complete bases (sum = identity); describe what remains per subgroup.
shapes = Counter()
for w in itertools.product((0, 1), repeat=12):
    if not any(w) or not s.classify(w): continue
    per = Counter(s.PROJ[i][0] for i, x in enumerate(w) if x)
    rest = tuple(sorted(n for g, n in per.items() if n != 3))
    shapes[rest] += 1
print("lines per subgroup after dropping complete bases:", dict(shapes))
