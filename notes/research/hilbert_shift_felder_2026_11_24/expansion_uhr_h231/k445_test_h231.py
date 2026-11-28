"""k445 (Test H231): Expansion als Uhr -- friert die Hubble-Reibung phi beim Messwert ein?
Vorab-Notiz Vorab_H231_Expansion_als_Uhr.md (vor der Rechnung committet).
phi'' + (3 + H'/H) phi' + V'(phi)/H^2 = 0 in N = ln a,  V'(phi)/H0^2 = (mu^2/3) sin 3(phi - pi/8),  mu = m/H0.
Aufruf aus diesem Ordner: python3 k445_test_h231.py > k445_out.txt
"""
import math
import numpy as np
from scipy.integrate import solve_ivp
from scipy.optimize import brentq

X = math.pi / 12 - 0.2222220470731
SIG = 7.8e-7
OM, OR = 0.315, 9.1e-5
OL = 1 - OM - OR
H0_YR = 67.4 / 977.792e9 * 1e0  # km/s/Mpc -> 1/yr: 1 km/s/Mpc = 1.0227e-12 /yr
H0_YR = 67.4 * 1.02271e-12
BOUND = 1e-16
BETA, GL = 0.549405640974529, 1.864699764609373
N0 = math.log(1e-8)


def E2(N):
    return OR * math.exp(-4 * N) + OM * math.exp(-3 * N) + OL


def dlnE(N):
    return (-4 * OR * math.exp(-4 * N) - 3 * OM * math.exp(-3 * N)) / (2 * E2(N))


def rhs(N, y, mu):
    p, dp = y
    return [dp, -(3 + dlnE(N)) * dp - (mu * mu / 3) * math.sin(3 * (p - math.pi / 8)) / E2(N)]


def today(mu):
    s = solve_ivp(rhs, (N0, 0.0), [0.0, 0.0], args=(mu,), method="DOP853", rtol=1e-11, atol=1e-13)
    return s.y[0, -1], s.y[1, -1]


def dlnme_dphi(phi):
    d = math.pi / 12 - phi
    vals = []
    for k in range(3):
        c = 1 + math.sqrt(2) * math.cos(d + 2 * math.pi * k / 3)
        vals.append((c * c, k))
    c2, k = min(vals)
    c = 1 + math.sqrt(2) * math.cos(d + 2 * math.pi * k / 3)
    # d/dphi ln c^2 = 2/c * dc/dphi, dc/dphi = +sqrt2 sin(d + ...)
    return 2 * math.sqrt(2) * math.sin(d + 2 * math.pi * k / 3) / c


print("=" * 92)
print("H231 (k445)  Expansion als Uhr: phi rollt in V = -A cos 3(phi - pi/8) im LCDM-Hintergrund, Start phi = 0 bei a = 1e-8")
print("=" * 92)
print(f"Omega_m = {OM}, Omega_r = {OR}, Omega_L = {OL:.6f}; H0 = {H0_YR:.4e} /yr; Grenze |d ln m_e/dt| < {BOUND:.0e} /yr")
print(f"Ziel x = {X:.10f};  d ln m_e / d phi bei x = {dlnme_dphi(X):+.4f}")

print("\nTeil a  phi(heute) und phi' = d phi/d ln a heute als Funktion von mu = m/H0")
mus = np.logspace(-2, 3, 1201)
vals = []
for mu in mus:
    p, dp = today(mu)
    vals.append((mu, p, dp))
for mu, p, dp in vals[::100]:
    print(f"  mu = {mu:10.4g}: phi = {p:+.6f}, phi' = {dp:+.4e}")
pm = np.array([v[1] for v in vals])
print(f"  Bereich phi(heute): {pm.min():.6f} .. {pm.max():.6f}")

print("\nTeil a/b  alle mu* mit phi(heute) = x und die Drift heute")
roots = []
g = pm - X
for i in np.nonzero(np.sign(g[:-1]) * np.sign(g[1:]) < 0)[0]:
    r = brentq(lambda m: today(m)[0] - X, mus[i], mus[i + 1], xtol=1e-12)
    p, dp = today(r)
    drift = abs(dlnme_dphi(p) * dp) * H0_YR
    roots.append((r, p, dp, drift))
    print(f"  mu* = {r:.8f}: phi = {p:.10f}, phi' = {dp:+.4e}, phi_dot = {dp*H0_YR:+.3e} /yr, |d ln m_e/dt| = {drift:.3e} /yr"
          f"  ({drift/BOUND:.1e} x Grenze)")
if not roots:
    print("  kein mu* im Bereich")
ok_b = any(r[3] < BOUND for r in roots)

print("\nTeil c  natuerliche mu-Werte")
nat = {"sqrt(Omega_L) (k251)": math.sqrt(OL), "1": 1.0, "3/2": 1.5, "beta_sym": BETA, "gamma_L": GL, "1/beta_sym": 1 / BETA}
hit_c = False
for k, mu in nat.items():
    p, dp = today(mu)
    drift = abs(dlnme_dphi(p) * dp) * H0_YR
    hit = abs(p - X) <= 2 * SIG and drift < BOUND
    hit_c |= hit
    print(f"  mu = {k:22s} = {mu:.6f}: phi(heute) = {p:+.8f} (Abstand {(p-X)/X*100:+.1f} %), phi' = {dp:+.3e}, Drift {drift:.2e} /yr")

print("\nKontrolle: Einfrieren fuer H >> m (mu = 0,01) und Endwert fuer grosses mu (Schwingung um pi/8)")
for mu in (0.01, 30.0, 300.0):
    s = solve_ivp(rhs, (N0, 0.0), [0.0, 0.0], args=(mu,), method="DOP853", rtol=1e-11, atol=1e-13, dense_output=True)
    Ns = np.linspace(-3, 0, 7)
    print(f"  mu = {mu}: phi bei ln a = {list(np.round(Ns,1))}: {[round(float(s.sol(n)[0]), 5) for n in Ns]}")

print("\n" + "=" * 92)
if hit_c:
    v = "TRAEGT"
elif ok_b:
    v = "TRAEGT TEILWEISE"
else:
    v = "WIDERLEGT"
print(f"H231 Gesamturteil: {v}   (natuerlich {hit_c}, angepasst mit Drift unter Grenze {ok_b}, Zahl der mu* {len(roots)})")
