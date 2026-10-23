"""k74: Nachkontrolle zu H18 (nach dem Urteil, nicht Teil des Kriteriums): Warum sind die mu so oft 'unbestimmt'?"""
import numpy as np, os, sys
from scipy.optimize import minimize
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from k69_test_h17 import V, G
def mus(z):   # wie k73_test_h18.py (dort ohne main-Schutz, daher hier nicht importiert)
    x = [z[:8], z[8:16], z[16:]]
    area = lambda a, b: 2*((a@a)*(b@b) - (a@b)**2)
    return np.array([area(x[1], x[2]), area(x[0], x[2]), area(x[0], x[1])])
rng = np.random.default_rng(74)
def good(p, starts=20):
    res = [minimize(V, rng.normal(size=24)/np.sqrt(8), args=p, jac=G, method="BFGS", options=dict(gtol=1e-10, maxiter=4000)) for _ in range(starts)]
    best = min(r.fun for r in res); return [r.x for r in res if r.fun <= best + 1e-9*abs(best)], best
# A: flache Winkelrichtung
for p in [(1, 0.1, 2, 0, 0, 0), (0.5, 0.5, 1, 0, 0, 0), (2, -0.1, 5, 0, 0, 0)]:
    xs, best = good(p); M = np.array([np.sort(mus(x)) for x in xs]); S = np.array([(x**2).sum() for x in xs])
    print(f"A {p[:3]}: {len(xs)} gleich tiefe Minima, V = {best:.6f}; S gleich: {np.ptp(S) < 1e-6}; mu_max/S^2 von {M[:,2].min()/S[0]**2:.3f} bis {M[:,2].max()/S[0]**2:.3f}")
# B: wie viele 'unbestimmte' haben mu ~ 0 (parallele Plaetze, reelle Achse)?
zero = flat = 0; N = 0
rng2 = np.random.default_rng(18); pars = []
while len(pars) < 500:
    b, g = rng2.uniform(0.1, 3), rng2.uniform(-1, 2)
    k, mu, nu, la = rng2.uniform(0, 3), rng2.uniform(-2, 2), rng2.uniform(-1, 2), rng2.uniform(-1, 1)
    if b + g <= 0.05: continue
    pars.append((b, g, k, mu, nu, la))
for p in pars[:150]:
    xs, best = good(p)
    if len(xs) < 3: continue
    M = np.array([np.sort(mus(x)) for x in xs]); S = (xs[0]**2).sum()
    if np.abs(M - M[0]).max() <= 1e-3*max(M[0].max(), 1e-300): continue
    N += 1
    if M.max() < 1e-8*S**2: zero += 1
    else: flat += 1
print(f"B (erste 150 Punkte): {N} 'unbestimmt', davon mu ~ 0 (parallele Plaetze): {zero}, echte flache Richtung: {flat}")
