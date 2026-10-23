"""k73: Test der Vorab-Notiz H18 (Commit 6130814): Massen aus links-invarianten Etiketten mu_k an den globalen Minima
der gepruefen Potentiale (Familie A = H11, Familie B = H17).  mu_k = 2(|x_i|^2 |x_j|^2 - <x_i,x_j>^2), m_k ~ sqrt(mu_k)."""
import numpy as np, itertools, os, sys
from scipy.optimize import minimize
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from k69_test_h17 import V, G

def mus(z):
    x = [z[:8], z[8:16], z[16:]]
    area = lambda a, b: 2*((a@a)*(b@b) - (a@b)**2)
    return np.array([area(x[1], x[2]), area(x[0], x[2]), area(x[0], x[1])])

def run(p, rng, starts=20):
    res = []
    for _ in range(starts):
        r = minimize(V, rng.normal(size=24)/np.sqrt(8), args=p, jac=G, method="BFGS", options=dict(gtol=1e-10, maxiter=4000))
        res.append((r.fun, r.x))
    best = min(f for f, _ in res)
    good = [x for f, x in res if f <= best + 1e-9*abs(best)]
    if len(good) < 3: return "nicht entschieden", None
    M = [np.sort(mus(x)) for x in good]
    ref = M[0]; scale = max(ref.max(), 1e-300)
    if any(abs(m - ref).max() > 1e-3*scale for m in M): return "unbestimmt", None
    return "bestimmt", ref

def pattern(m):
    s = m.max()
    if s <= 1e-12: return "alle null"
    nz = int((m > 1e-6*s).sum())
    nd = 1 + sum((m[i+1]-m[i]) > 1e-3*s for i in range(2))
    return f"{nd} verschieden, {nz} != 0"

lep = np.array([0.016959, 0.243848, 1.0])
def report(name, pars, rng):
    stat = {}; hits = []
    for p in pars:
        st, m = run(p, rng)
        key = st if m is None else f"{st}, {pattern(m)}"
        stat[key] = stat.get(key, 0) + 1
        if m is not None and pattern(m) == "3 verschieden, 3 != 0":
            sq = m**0.25; sq = sq/sq.max()                       # sqrt(m_k) ~ mu_k^(1/4)
            K = (m**0.5).sum()/(m**0.25).sum()**2
            hits.append((p, m, sq, K, abs(sq[:2]/lep[:2] - 1).max()))
    print(f"\n{name}: {len(pars)} Parameterpunkte")
    for k in sorted(stat): print(f"  {k}: {stat[k]}")
    if hits:
        hits.sort(key=lambda h: h[4])
        print(f"  drei verschiedene, bestimmte mu: {len(hits)}; bester Abstand zu den Lepton-Verhaeltnissen {100*hits[0][4]:.1f} %")
        for p, m, sq, K, d in hits[:5]:
            print(f"    Parameter {np.round(p, 3)}: sqrt(m)/sqrt(m3) = {np.round(sq, 5)}, K = {K:.4f}, Abstand {100*d:.1f} %")
        print(f"  K-Bereich: {min(h[3] for h in hits):.4f} bis {max(h[3] for h in hits):.4f}")
    return hits

rng = np.random.default_rng(18)
A = [(b, g, k, 0.0, 0.0, 0.0) for b, g, k in itertools.product((0.25, 0.5, 1, 2, 4), (-0.2, -0.1, 0, 0.1, 0.5, 1, 3),
                                                            (0, 0.1, 0.5, 1, 2, 5)) if not (g == 0 and k == 0)]
hA = report("Familie A (H11)", A, rng)
B = []
while len(B) < 500:
    b, g = rng.uniform(0.1, 3), rng.uniform(-1, 2)
    k, mu, nu, la = rng.uniform(0, 3), rng.uniform(-2, 2), rng.uniform(-1, 2), rng.uniform(-1, 1)
    if b + g <= 0.05: continue
    B.append((b, g, k, mu, nu, la))
hB = report("Familie B (H17)", B, rng)
print(f"\nH18a: {'bestaetigt' if hA or hB else 'widerlegt'} (drei verschiedene, bestimmte mu: A {len(hA)}, B {len(hB)})")
best = min([h[4] for h in hA + hB], default=None)
print(f"H18b: {'bestaetigt' if best is not None and best <= 0.01 else 'widerlegt'}"
      + (f" (bester Abstand {100*best:.1f} %)" if best is not None else " (keine Kandidaten)"))
