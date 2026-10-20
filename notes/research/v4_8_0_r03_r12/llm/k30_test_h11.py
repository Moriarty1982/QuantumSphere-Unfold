"""k30: Test der Vorab-Notiz H11 (Commit 8e5eaa9): Massen aus natuerlichen Funktionen auf dem Tripel-Raum."""
import numpy as np, contextlib, io, os, itertools
from scipy.optimize import minimize
here = os.path.dirname(os.path.abspath(__file__))
with contextlib.redirect_stdout(io.StringIO()):
    exec(open(os.path.join(here, "k22_oktonion_triplett.py")).read().split("# Mischung:")[0])
rng = np.random.default_rng(30)
K = lambda n: (n**2).sum()/n.sum()**2
def ndistinct(n, tol=1e-4):   # BFGS-Genauigkeit; 1e-6 zaehlte Rechenrauschen als verschieden
    n = np.sort(np.abs(n)); s = n.max()
    return 1 + sum(abs(n[i+1]-n[i]) > tol*s for i in range(2))

# H11a: Extrema von t = Re((ab)c) auf S = |a|^2+|b|^2+|c|^2 = 3 (24 reelle Variablen), projizierter Gradient
def t(z): a, b, c = z[:8], z[8:16], z[16:]; return omul(omul(a, b), c)[0]
def grad_t(z, h=1e-6):
    g = np.zeros(24)
    for i in range(24):
        e = np.zeros(24); e[i] = h; g[i] = (t(z+e)-t(z-e))/(2*h)
    return g
print("H11a: Extrema der Triality-Form bei fester Gesamtnorm")
pats = []
for sgn in (+1, -1):
    for _ in range(12):
        z = rng.normal(size=24); z *= np.sqrt(3)/np.linalg.norm(z)
        for _ in range(3000):
            g = sgn*grad_t(z); g -= (g@z)/(z@z)*z
            z = z + 0.05*g; z *= np.sqrt(3)/np.linalg.norm(z)
        n = np.array([np.linalg.norm(z[:8]), np.linalg.norm(z[8:16]), np.linalg.norm(z[16:])])
        pats.append(("max" if sgn > 0 else "min", np.round(t(z), 4), np.round(np.sort(n), 4), round(K(n), 4)))
for p in sorted(set((a, b, tuple(c), d) for a, b, c, d in pats)):
    print(f"  {p[0]}: t = {p[1]:+.4f}, Normen {p[2]}, K = {p[3]}")
# Saettel: Lagrange-Loesungen mit zwei leeren Plaetzen (t = 0) -> K = 1
print("  kritische Punkte mit zwei leeren Plaetzen: Normen (0, 0, sqrt3), t = 0, K = 1")

# H11b: V = alpha S + beta S^2 + gamma Q - kappa P, alpha = -1, nur nach unten beschraenkte Faelle
def V(n, b, g, k):
    S = (n**2).sum(); Q = (n**4).sum(); P = np.prod(n)
    return -S + b*S**2 + g*Q - k*P
print("\nH11b: Minima des allgemeinsten invarianten Potentials bis Grad 4")
stat = {1: 0, 2: 0, 3: 0}; examples = {}
grid = list(itertools.product((0.25, 0.5, 1, 2, 4), (-0.2, -0.1, 0, 0.1, 0.5, 1, 3), (0, 0.1, 0.5, 1, 2, 5)))
for b, g, k in grid:
    if g < 0 and b + g <= 0: continue
    best = None
    for _ in range(40):
        r = minimize(V, rng.normal(size=3), args=(b, g, k), method="BFGS", options=dict(gtol=1e-12))
        if best is None or r.fun < best.fun - 1e-12: best = r
    n = np.abs(best.x)
    if g == 0 and k == 0:          # V haengt nur von S ab: Minimum ist eine ganze Kugel, keine bestimmten Massen
        stat.setdefault("flach (gamma = kappa = 0)", 0); stat["flach (gamma = kappa = 0)"] += 1; continue
    nd = ndistinct(n); nz = (n > 1e-4*n.max()).sum()
    stat[nd] += 1; examples.setdefault((nd, nz), (b, g, k, np.round(np.sort(n), 5), round(K(n), 4)))
print("  Zahl der verschiedenen Normen im globalen Minimum (ueber alle Gitterpunkte):", stat)
print("  (Fall flach: V = -S + beta S^2 ist auf der ganzen Kugel S = 1/(2 beta) minimal; die Lage darauf ist beliebig.)")
for key, ex in sorted(examples.items()):
    print(f"  Muster ({key[0]} verschiedene, {key[1]} von null verschieden), Beispiel beta={ex[0]}, gamma={ex[1]}, kappa={ex[2]}: "
          f"Normen {ex[3]}, K = {ex[4]}")
# Analytische Kontrolle: an jedem kritischen Punkt mit n_k != 0 erfuellt x_k = n_k^2 dieselbe quadratische Gleichung
b, g, k = 1.0, 0.1, 2.0
r = minimize(V, np.array([1.0, 0.9, 1.1]), args=(b, g, k), method="BFGS", options=dict(gtol=1e-12)); n = r.x
S = (n**2).sum(); P = np.prod(n)
lhs = [(2*(-1) + 4*b*S)*x + 4*g*x**2 for x in n**2]
print(f"\n  Kontrolle (beta={b}, gamma={g}, kappa={k}): (2 alpha + 4 beta S) x_k + 4 gamma x_k^2 = {np.round(lhs, 8)},"
      f" kappa P = {k*P:.8f}")

# Mindestgrad: mit einem Sextik-Term mu * sum n^6 wird die Gleichung kubisch in x_k -> drei verschiedene Normen moeglich
def V6(n, b, g, k, mu): return V(n, b, g, k) + mu*(n**6).sum()
found = None
for b, g, k, mu in itertools.product((0.5, 1, 2), (-1.5, -1, -0.5), (0.5, 1, 2, 4), (0.2, 0.5, 1)):
    best = None
    for _ in range(60):
        r = minimize(V6, rng.normal(size=3), args=(b, g, k, mu), method="BFGS", options=dict(gtol=1e-12))
        if best is None or r.fun < best.fun - 1e-12: best = r
    n = np.abs(best.x)
    if ndistinct(n) == 3 and (n > 1e-4*n.max()).all():
        found = (b, g, k, mu, np.round(np.sort(n), 5), round(K(n), 4)); break
print("\n  Mit Sextik-Term (Grad 6):", "Minimum mit drei verschiedenen Normen gefunden, Beispiel beta, gamma, kappa, mu ="
      f" {found[:4]}, Normen {found[4]}, K = {found[5]}" if found else "kein Beispiel mit drei verschiedenen Normen im Gitter")
lep = np.sqrt(np.array([0.51099895, 105.6583755, 1776.93]))
print(f"  Zum Vergleich Leptonen: sqrt(m)/sqrt(m_tau) = {np.round(lep/lep[2], 5)}, K = {K(lep):.6f}")
