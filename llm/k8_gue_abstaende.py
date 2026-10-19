"""K8 / r05: GUE-Statistik der Zeta-Nullstellen empirisch pruefen (Companion thm:gue).

Unfolding mit der Riemann-von-Mangoldt-Zaehlfunktion N(T) = T/(2pi) log(T/(2pi e)) + 7/8;
normierte Abstaende s_n = N(g_{n+1}) - N(g_n), Mittelwert 1.
Vergleich mit Wigner-Surmise GUE (beta=2), GOE (beta=1) und Poisson ueber Kolmogorov-Smirnov.
Nullstellen werden in zeros.npy zwischengespeichert.
"""
import os
import numpy as np
import mpmath as mp
from scipy import stats, integrate

mp.mp.dps = 15
f = os.path.join(os.path.dirname(os.path.abspath(__file__)), "zeros.npy")
N = 2000
if os.path.exists(f) and len(np.load(f)) >= N:
    g = np.load(f)[:N]
else:
    g = np.array([float(mp.zetazero(k).imag) for k in range(1, N + 1)])
    np.save(f, g)

def Nsmooth(t): return t/(2*np.pi)*np.log(t/(2*np.pi*np.e)) + 7/8
s = np.diff(Nsmooth(g))
s = s[100:]                     # niedrige Nullstellen weglassen (Unfolding dort grob)
s = s/np.mean(s)

p_gue = lambda x: 32/np.pi**2*x**2*np.exp(-4*x**2/np.pi)
p_goe = lambda x: np.pi/2*x*np.exp(-np.pi*x**2/4)
cdf = lambda p: (lambda x: np.array([integrate.quad(p, 0, xi)[0] for xi in np.atleast_1d(x)]))
for name, cf in (("GUE (beta=2)", cdf(p_gue)), ("GOE (beta=1)", cdf(p_goe)), ("Poisson", lambda x: 1 - np.exp(-np.asarray(x)))):
    D, pval = stats.kstest(s, cf)
    print(f"   {name:13s}: KS-Abstand D = {D:.4f}, p = {pval:.3g}")
print(f"   {len(s)} Abstaende; Anteil s < 0.1: {np.mean(s < 0.1):.4f} "
      f"(GUE erwartet {integrate.quad(p_gue,0,0.1)[0]:.4f}, GOE {integrate.quad(p_goe,0,0.1)[0]:.4f}, Poisson {1-np.exp(-0.1):.4f})")
