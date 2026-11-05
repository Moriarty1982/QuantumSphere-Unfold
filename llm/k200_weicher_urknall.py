"""k200: Test H85 - weicher, komplexer Uebergang des Kinetik-Gewichts am Urknall (Gebiet G2).
(w chi')' + w k^2 chi = 0, w = b^(1-s) a^s exp(+-i pi (1-s)), s = (1 + tanh(tau/Delta))/2, Delta = 1.
Ausgabe k200_out.json im aktuellen Ordner.
"""
import json
import numpy as np
from scipy.integrate import solve_ivp

bsym = 1/1.8203; x = bsym**2; a, b = 1/(1+x), x/(1+x)
C0, D0 = (a + b)/(2*a), (a - b)/(2*a)

def wfun(t, sgn):
    s = 0.5*(1 + np.tanh(t)); ds = 0.5/np.cosh(t)**2
    w = b**(1-s)*a**s*np.exp(sgn*1j*np.pi*(1-s))
    dw = w*(np.log(a) - np.log(b) - sgn*1j*np.pi)*ds
    return w, dw

def run(k, sgn, L=20.0):
    def rhs(t, y):
        chi = y[0] + 1j*y[1]; d = y[2] + 1j*y[3]
        w, dw = wfun(t, sgn)
        dd = -(dw/w)*d - k**2*chi
        return [d.real, d.imag, dd.real, dd.imag]
    t0, t1 = -L, L
    chi0 = np.exp(1j*k*t0); d0 = 1j*k*chi0
    s = solve_ivp(rhs, (t0, t1), [chi0.real, chi0.imag, d0.real, d0.imag], rtol=1e-11, atol=1e-13, method='DOP853',
                  dense_output=True)
    chi = s.y[0, -1] + 1j*s.y[1, -1]; d = s.y[2, -1] + 1j*s.y[3, -1]
    C = (chi - d/(1j*k))/2*np.exp(1j*k*t1); D = (chi + d/(1j*k))/2*np.exp(-1j*k*t1)
    # Kontrolle: holomorphe Wronski-Determinante mit der zweiten Loesung (Start e^{-ik tau})
    def rhs2(t, y):
        return rhs(t, y)
    chi20 = np.exp(-1j*k*t0); d20 = -1j*k*chi20
    s2 = solve_ivp(rhs2, (t0, t1), [chi20.real, chi20.imag, d20.real, d20.imag], rtol=1e-11, atol=1e-13, method='DOP853',
                   dense_output=True)
    grid = np.linspace(t0, t1, 400)
    Y1 = s.sol(grid); Y2 = s2.sol(grid)
    c1 = Y1[0] + 1j*Y1[1]; d1 = Y1[2] + 1j*Y1[3]; c2 = Y2[0] + 1j*Y2[1]; d2 = Y2[2] + 1j*Y2[3]
    W = np.array([wfun(t, sgn)[0] for t in grid])*(c1*d2 - c2*d1)
    return C, D, float(np.max(np.abs(W - W[0]))/abs(W[0]))

out = {'sharp': {'C': C0, 'D': D0, '|D/C|': D0/C0, 'n_sharp': (1-x)**2/(4*x)}}
for sgn, name in ((1, 'plus'), (-1, 'minus')):
    rows = []
    for k in (0.01, 0.03, 0.1, 0.3, 1.0, 2.0, 3.0, 5.0):
        C, D, wdev = run(k, sgn)
        rows.append({'k': k, 'C': [C.real, C.imag], 'D': [D.real, D.imag], '|C|': abs(C), '|D|': abs(D), '|D/C|': abs(D/C),
                     'rel_Abw_C_scharf': abs(C - C0)/abs(C0), 'rel_Abw_D_scharf': abs(D - D0)/abs(D0), 'Wronski_rel': wdev})
    out[name] = rows
H85a = all(r['rel_Abw_C_scharf'] < 0.01 and r['rel_Abw_D_scharf'] < 0.01 for nm in ('plus', 'minus') for r in out[nm] if r['k'] == 0.01)
H85b = all(r['|D/C|'] < 1e-3 for nm in ('plus', 'minus') for r in out[nm] if r['k'] == 5.0)
ctrl = max(r['Wronski_rel'] for nm in ('plus', 'minus') for r in out[nm])
out.update({'H85a': H85a, 'H85b': H85b, 'Kontrolle_Wronski_max': ctrl,
            'H85c_|D|_plus_vs_minus': [(r1['k'], r1['|D|'], r2['|D|']) for r1, r2 in zip(out['plus'], out['minus'])]})
json.dump(out, open('k200_out.json', 'w'), indent=1, default=float)
for nm in ('plus', 'minus'):
    for r in out[nm]:
        print(nm, 'k=%5.2f |C|=%.5f |D|=%.3e |D/C|=%.3e devC=%.2e devD=%.2e W=%.1e' % (r['k'], r['|C|'], r['|D|'], r['|D/C|'], r['rel_Abw_C_scharf'], r['rel_Abw_D_scharf'], r['Wronski_rel']))
print('H85a', H85a, 'H85b', H85b, 'Wronski max', ctrl, 'scharf |D/C|', D0/C0)
