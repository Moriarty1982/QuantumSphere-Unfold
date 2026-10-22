"""k64: Test der Vorab-Notiz H16 (Commit d0360b8, als H12 angelegt, umbenannt 6bd2f1b):
Massen aus invarianten Potentialen bis Grad 6 auf dem Tripel-Raum.
V6 = -S + beta S^2 + gamma Q - kappa P + delta H,  S = sum n^2, Q = sum n^4, H = sum n^6, P = n1 n2 n3."""
import numpy as np
from scipy.optimize import minimize

TOL = 1e-4   # relative Toleranz fuer "verschieden" und "von null verschieden" (in der Notiz festgelegt)

def V(n, b, g, k, d):
    x = n**2
    return -x.sum() + b*x.sum()**2 + g*(x**2).sum() - k*np.prod(n) + d*(x**3).sum()

def grad(n, b, g, k, d):
    S = (n**2).sum(); P_i = np.array([n[1]*n[2], n[0]*n[2], n[0]*n[1]])
    return -2*n + 4*b*S*n + 4*g*n**3 - k*P_i + 6*d*n**5

def hess(n, b, g, k, d):
    S = (n**2).sum(); Hm = 8*b*np.outer(n, n)
    Hm += np.diag(-2 + 4*b*S + 12*g*n**2 + 30*d*n**4)
    for i in range(3):
        for j in range(3):
            if i != j: Hm[i, j] -= k*n[3-i-j]
    return Hm

def global_min(b, g, k, d, starts, rng, scale=1.0):
    best = None
    for _ in range(starts):
        r = minimize(V, scale*rng.normal(size=3), args=(b, g, k, d), jac=grad, method="BFGS",
                     options=dict(gtol=1e-12, maxiter=5000))
        if best is None or r.fun < best.fun: best = r
    return best

def pattern(n):
    n = np.sort(np.abs(n)); s = n.max()
    if s < 1e-12: return 0, 0
    nz = int((n > TOL*s).sum())
    nd = 1 + sum(abs(n[i+1]-n[i]) > TOL*s for i in range(2))
    return nd, nz

Kf = lambda n: (n**2).sum()/np.abs(n).sum()**2

# ---------------------------------------------------------------- H16a / H16c: feste Verteilung
rng = np.random.default_rng(31)
N = 2000
pars = np.column_stack([rng.uniform(0, 3, N), rng.uniform(-2, 1, N), rng.uniform(0, 3, N), rng.uniform(0.01, 2, N)])
counts = {}; three = []; cubic_res = []
for b, g, k, d in pars:
    r = global_min(b, g, k, d, 40, rng)
    n = np.abs(r.x); nd, nz = pattern(n)
    counts[(nd, nz)] = counts.get((nd, nz), 0) + 1
    if nd == 3 and nz == 3:
        x = n**2; S = x.sum(); P = np.prod(n)
        res = 6*d*x**3 + 4*g*x**2 + (-2 + 4*b*S)*x - k*P
        cubic_res.append(np.abs(res).max()/max(1e-12, np.abs(6*d*x**3).max()))
        three.append((b, g, k, d, Kf(n), x.min()/x.max()))
print("H16a: Muster des globalen Minimums (verschiedene Normen, von null verschiedene) ueber N = 2000:")
for key in sorted(counts): print(f"  {key}: {counts[key]}")
print(f"  drei verschiedene, alle != 0: {len(three)} ({100*len(three)/N:.1f} %)")
if three:
    T = np.array(three)
    print(f"  Kontrolle kubische Gleichung: max. relativer Rest {max(cubic_res):.1e}")
    print(f"  gamma bei diesen Minima: max {T[:,1].max():+.3f} (Vieta verlangt gamma < 0)")
    Ks = T[:, 4]
    print("\nH16c: K-Verteilung der Minima mit drei verschiedenen Normen")
    print(f"  K: min {Ks.min():.4f}, Median {np.median(Ks):.4f}, max {Ks.max():.4f}")
    hist, edges = np.histogram(Ks, bins=np.linspace(1/3, 1, 9))
    for h, a, c in zip(hist, edges[:-1], edges[1:]): print(f"    [{a:.3f}, {c:.3f}): {h}")
    near = np.mean(np.abs(Ks - 2/3) < 0.01)
    print(f"  Anteil |K - 2/3| < 0,01: {100*near:.1f} %  (Schwelle fuer 'ausgezeichnet': 50 %)")
    print(f"  Anteil x_min/x_max < 1e-3: {100*np.mean(T[:,5] < 1e-3):.1f} %;  kleinstes x_min/x_max {T[:,5].min():.2e}")

# ---------------------------------------------------------------- H16b: Lepton-Tripel als globales Minimum?
m = np.array([0.51099895, 105.6583755, 1776.93])
rlep = m/m[2]                                   # x-Verhaeltnisse (x = n^2 ~ m)
print(f"\nH16b: Lepton-Tripel x = {np.round(rlep, 6)}, K = {Kf(np.sqrt(rlep)):.6f}")
grid_s = np.logspace(-2, 2, 41); grid_b = np.linspace(-5, 5, 41)
stat = dict(delta_le_0=0, kein_lokales_min=0, lokal_nicht_global=0, global_=0)
sol = []; rng_b = np.random.default_rng(3116)
for s in grid_s:
    x = s*rlep; S = x.sum(); e2 = x[0]*x[1] + x[0]*x[2] + x[1]*x[2]; P = np.sqrt(np.prod(x)); n0 = np.sqrt(x)
    for b in grid_b:
        d = (-2 + 4*b*S)/(6*e2)
        if d <= 0: stat["delta_le_0"] += 1; continue
        g = -1.5*d*S; k = 6*d*P
        assert np.abs(grad(n0, b, g, k, d)).max() < 1e-8*max(1, np.abs(n0).max())
        if np.linalg.eigvalsh(hess(n0, b, g, k, d)).min() <= 0: stat["kein_lokales_min"] += 1; continue
        V0 = V(n0, b, g, k, d)
        r = global_min(b, g, k, d, 200, rng_b, scale=np.sqrt(s))
        if r.fun < V0 - 1e-9*abs(V0): stat["lokal_nicht_global"] += 1; continue
        stat["global_"] += 1; sol.append((s, b, g, k, d))
print(f"  Gitter 41 x 41 (Skala s, beta): {stat}")
if sol:
    A = np.array(sol)
    print(f"  globale Minima bei s in [{A[:,0].min():.3g}, {A[:,0].max():.3g}], beta in [{A[:,1].min():.3g}, {A[:,1].max():.3g}]"
          f" ({len(np.unique(A[:,0]))} Skalen, {len(np.unique(A[:,1]))} beta-Werte)")
    s, b, g, k, d = sol[len(sol)//2]
    print(f"  Beispiel: s = {s:.4g}, beta = {b:.4g}, gamma = {g:.4g}, kappa = {k:.4g}, delta = {d:.4g}")
    r = global_min(b, g, k, d, 200, rng_b, scale=np.sqrt(s)); n = np.sort(np.abs(r.x))
    print(f"    wiedergefunden: sqrt(m)/sqrt(m_tau) = {np.round(n/n[2], 6)}, K = {Kf(n):.6f}")
