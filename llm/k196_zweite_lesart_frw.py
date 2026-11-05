"""k196: Test H80/H81 - zweite Lesart auf FRW. Ausgabe k196_out.json im aktuellen Ordner.
Reduzierte Skalarwirkung: K = A a^2 - B a_T^2, P = A a^4 + B a_T^4, Modengleichung (K chi')' + (K k^2 + P m^2) chi = 0.
"""
import json
import numpy as np
import sympy as sp
from scipy.integrate import solve_ivp

out = {}
bsym = 1/1.8203; x = bsym**2; A, B = 1/(1+x), x/(1+x)        # Materie-Gewichte, B/A = bsym^2
out['Gewichte'] = {'A': A, 'B': B, 'B/A': B/A, 'bsym^2': x}

# ---------- H80a (delta = 0) ----------
t, Aa, Bb, m, k, s = sp.symbols('tau A B m k s', positive=True)
chi = sp.Function('chi')(t)
h80 = {}
for n in (1, 2):
    for sgn in (1, -1):
        a = t**n; aT = sgn*t**n                  # Fortsetzung a(-tau) = sgn * a(tau)
        K = Aa*a**2 - Bb*aT**2; P = Aa*a**4 + Bb*aT**4
        eq = sp.diff(K*sp.diff(chi, t), t) + (K*k**2 + P*m**2)*chi
        meff2 = (Aa + Bb)/(Aa - Bb)*m**2
        eqM = sp.diff(a**2*sp.diff(chi, t), t) + (a**2*k**2 + a**4*meff2)*chi
        h80[f'n={n},sgn={sgn}'] = bool(sp.simplify(eq - (Aa - Bb)*eqM) == 0)
out['H80a'] = h80
out['H80a_gamma'] = (A + B)/(A - B)

# ---------- H81a (delta = 1) ----------
d = 1.0
tstar = {}
for n in (1, 2):
    T = sp.symbols('T', positive=True)
    sol = [float(r) for r in sp.solve(sp.Eq(A*T**(2*n) - B*(d - T)**(2*n), 0), T) if 0 < float(r) < d]
    pred = bsym/(1 + bsym) if n == 1 else np.sqrt(bsym)/(1 + np.sqrt(bsym))
    tstar[f'n={n}'] = {'numerisch': sol, 'vorhergesagt': pred}
out['H81a'] = tstar

def KP(tau, n=1):
    a = tau**n; aT = abs(d - tau)**n
    return A*a**2 - B*aT**2, A*a**4 + B*aT**4

def rhs(tau, y, kk, mm, n=1):
    K, P = KP(tau, n)
    return [y[1]/K, -(K*kk**2 + P*mm**2)*y[0]]        # y0 = chi, y1 = K chi'

ts = bsym/(1 + bsym); t0 = 0.05
# ---------- H81b (Strahlung, k = 1, m = 1) ----------
kk, mm = 1.0, 1.0
def run(y0, tend):
    s_ = solve_ivp(rhs, (t0, tend), y0, args=(kk, mm), rtol=1e-12, atol=1e-14, method='DOP853')
    return s_.y[:, -1]
K0, _ = KP(t0)
y_gen = [1.0, K0*0.5]                                  # chi = 1, chi' = 0.5
eps = np.logspace(-2, -9, 15)
chis = np.array([run(y_gen, ts - e)[0] for e in eps])
L = np.log(eps); sel = eps <= 1e-6
pfit = np.polyfit(L[sel], chis[sel], 1); res_ = chis[sel] - np.polyval(pfit, L[sel])
R2 = 1 - (res_**2).sum()/((chis[sel] - chis[sel].mean())**2).sum()
out['H81b_allgemein'] = {'eps': eps.tolist(), 'chi': chis.tolist(), 'Steigung_in_ln_eps': pfit[0], 'R2': R2}
# Schiessverfahren: Kombination zweier Basisloesungen mit K chi' -> 0 bei tau*
e0 = 1e-7
b1 = run([1.0, 0.0], ts - e0); b2 = run([0.0, 1.0], ts - e0)
c = -b1[1]/b2[1]                                        # y1(tau*) = 0
y_reg = [1.0, c]
chis_reg = np.array([run(y_reg, ts - e)[0] for e in eps])
sol_path = solve_ivp(rhs, (t0, ts - 1e-9), y_reg, args=(kk, mm), rtol=1e-12, atol=1e-14, method='DOP853', dense_output=True)
grid = np.linspace(t0, ts - 1e-9, 4000); chimax = np.abs(sol_path.sol(grid)[0]).max()
pr = np.polyfit(L[sel], chis_reg[sel], 1)
out['H81b_regulaer'] = {'chi': chis_reg.tolist(), 'Steigung_in_ln_eps': pr[0], 'max|chi|/|chi(start)|': chimax/1.0}
# ---------- H81c (k = 0, m = 3) ----------
s3 = solve_ivp(rhs, (t0, 0.9*ts), [1.0, 0.0], args=(0.0, 3.0), rtol=1e-12, atol=1e-14, method='DOP853', dense_output=True)
g3 = np.linspace(t0, 0.9*ts, 2000); v3 = np.abs(s3.sol(g3)[0])
Kc, Pc = KP(0.5*ts)
out['H81c'] = {'Wachstum max|chi|/|chi0|': float(v3.max()), 'P/K bei tau*/2': Pc/Kc}
json.dump(out, open('k196_out.json', 'w'), indent=1, default=float)
print(json.dumps(out, indent=1, default=float))
