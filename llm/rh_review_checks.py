"""Numerische Pruefung einzelner Aussagen aus riemann_arxiv_v4.15.

(1) Explizite Formel, Thm. EF:  Theta(tau) = 1 - Sigma(tau) + R(tau)
    mit Theta = sum_{p,m} (1/m) delta(tau - m log p), Sigma = sum_rho e^{-i tau gamma}, R = -e^{-tau/2}/(e^tau - 1).
    Gegenprobe mit der klassischen Form (Riemann-von Mangoldt / Weil):
      sum_n Lambda(n) g(log n) = int g(t) e^t dt - sum_rho int g(t) e^{rho t} dt - sum_{k>=1} int g(t) e^{-2kt} dt
    (gilt fuer glatte g mit kompaktem Traeger in (0, inf)).
(2) Laplace-Konsistenz in T6: Laplace[Sigma] vs. log zeta.
(3) Hopf-Fasern: schneiden sich zwei verschiedene Fasern? (Remark rem:triole)
"""
import numpy as np
import mpmath as mp
from scipy.integrate import quad

mp.mp.dps = 20
NZ = 300
gam = [float(mp.zetazero(k).imag) for k in range(1, NZ + 1)]

a, b = 0.6, 3.2                      # Traeger der Testfunktion in tau
def g(t):
    if t <= a or t >= b: return 0.0
    u = (2*t - a - b)/(b - a)
    return np.exp(-1/(1 - u*u))

def integ(f): return quad(f, a, b, limit=400, epsabs=1e-13)[0]

# Primpotenzen mit log n in (a,b)
N = int(np.exp(b)) + 1
lam = {}
for p in range(2, N + 1):
    if all(p % q for q in range(2, int(p**0.5) + 1)):
        m, pm = 1, p
        while pm <= N:
            lam[pm] = (np.log(p), m); m += 1; pm *= p

theta_side = sum(g(m*lp)/m for n, (lp, m) in lam.items() for _ in [0] if a < np.log(n) < b)
lambda_side = sum(lp*g(np.log(n)) for n, (lp, m) in lam.items() if a < np.log(n) < b)

def ghat_c(z):   # int g(t) e^{z t} dt  fuer komplexes z
    re = integ(lambda t: g(t)*np.exp(z.real*t)*np.cos(z.imag*t))
    im = integ(lambda t: g(t)*np.exp(z.real*t)*np.sin(z.imag*t))
    return re + 1j*im

# Paper-Form: <Theta,g> =? <1,g> - <Sigma,g> + <R,g>
one = integ(g)
Rg = integ(lambda t: g(t)*(-np.exp(-t/2)/(np.exp(t) - 1)))
Sig = sum(2*integ(lambda t: g(t)*np.cos(gm*t)) for gm in gam)   # rho und conj(rho)
paper_rhs = one - Sig + Rg

# Klassische Form
main = integ(lambda t: g(t)*np.exp(t))
zeros = sum(2*ghat_c(complex(0.5, gm)).real for gm in gam)
triv = sum(integ(lambda t, k=k: g(t)*np.exp(-2*k*t)) for k in range(1, 60))
classic_rhs = main - zeros - triv

print("(1) Explizite Formel, Testfunktion auf (0.6, 3.2), 300 Nullstellen")
print(f"    Paper:     <Theta,g> = {theta_side:.6f}   rechte Seite 1 - Sigma + R = {paper_rhs:.6f}")
print(f"    Klassisch: <Lambda,g> = {lambda_side:.6f}  rechte Seite e^t - sum e^(rho t) - triv = {classic_rhs:.6f}")

print("(2) Laplace-Konsistenz in T6 bei s = 2")
s = 2.0
logz = float(mp.log(mp.zeta(s)))
lap_sigma_terms = sum(2*(s/(s*s + gm*gm)) for gm in gam)      # Laplace von 2cos(gamma t)
lap_1 = 1/s
lap_R = quad(lambda t: np.exp(-s*t)*(-np.exp(-t/2)/np.expm1(t)), 1e-9, 60, limit=400)[0]
print(f"    log zeta(2) = {logz:.6f}")
print(f"    Laplace[Sigma] (300 Nullstellen, Partialsumme) = {lap_sigma_terms:.6f}  (divergiert logarithmisch mit mehr Nullstellen)")
print(f"    Laplace[R] = {lap_R:.4f} (Integral divergiert bei t->0: R ~ -1/t)")
print("    Aus Sigma = 1 - Theta + R folgt Laplace[Sigma] = 1/s - log zeta + Laplace[R], nicht log zeta.")

print("(3) Hopf-Fasern")
def fibre(base, n=2000):
    # Faser ueber Bloch-Vektor base: psi = e^{i phi} psi0
    th, ph = np.arccos(base[2]), np.arctan2(base[1], base[0])
    psi0 = np.array([np.cos(th/2), np.exp(1j*ph)*np.sin(th/2)])
    phis = np.linspace(0, 2*np.pi, n, endpoint=False)
    return np.array([np.exp(1j*f)*psi0 for f in phis])
F1 = fibre(np.array([0, 0, 1.0])); F2 = fibre(np.array([1.0, 0, 0]))
d = np.min(np.abs(F1[:, None, :] - F2[None, :, :]).sum(axis=2))
print(f"    minimaler Abstand zweier verschiedener Fasern in S^3: {d:.4f}  (> 0: disjunkt, sie schneiden sich nicht)")
