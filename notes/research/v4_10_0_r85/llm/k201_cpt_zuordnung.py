"""k201: Test H86 - CPT-Zuordnung und Beimischung am Urknall (G2), neue Einstellungen Delta = 2, Profile tanh und erf.
Ausgabe k201_out.json im aktuellen Ordner.
"""
import json
import numpy as np
from math import erf
from scipy.integrate import solve_ivp
from scipy.special import erf as verf

bsym = 1/1.8203; x = bsym**2; a, b = 1/(1+x), x/(1+x)
C0, D0 = (a + b)/(2*a), (a - b)/(2*a); Dl = np.sqrt(b/a)
Dlt = 2.0

def sfun(t, prof):
    if prof == 'tanh':
        return 0.5*(1 + np.tanh(t/Dlt)), 0.5/(Dlt*np.cosh(t/Dlt)**2)
    return 0.5*(1 + verf(t/Dlt)), np.exp(-(t/Dlt)**2)/(Dlt*np.sqrt(np.pi))

def wfun(t, sgn, prof):
    s, ds = sfun(t, prof)
    w = b**(1-s)*a**s*np.exp(sgn*1j*np.pi*(1-s))
    return w, w*(np.log(a) - np.log(b) - sgn*1j*np.pi)*ds

def run(kD, sgn, prof):
    k = kD/Dlt; L = (20 if prof == 'tanh' else 10)*Dlt
    def rhs(t, y):
        chi = y[0] + 1j*y[1]; d = y[2] + 1j*y[3]
        w, dw = wfun(t, sgn, prof)
        dd = -(dw/w)*d - k**2*chi
        return [d.real, d.imag, dd.real, dd.imag]
    sols = []
    for sg0 in (+1, -1):
        c0 = np.exp(sg0*1j*k*(-L)); d0 = sg0*1j*k*c0
        sols.append(solve_ivp(rhs, (-L, L), [c0.real, c0.imag, d0.real, d0.imag], rtol=1e-13, atol=1e-15,
                              method='DOP853', dense_output=True))
    s = sols[0]
    chi = s.y[0, -1] + 1j*s.y[1, -1]; d = s.y[2, -1] + 1j*s.y[3, -1]
    C = (chi - d/(1j*k))/2*np.exp(1j*k*L); D = (chi + d/(1j*k))/2*np.exp(-1j*k*L)
    grid = np.linspace(-L, L, 300); Y1 = sols[0].sol(grid); Y2 = sols[1].sol(grid)
    W = np.array([wfun(t, sgn, prof)[0] for t in grid])*((Y1[0]+1j*Y1[1])*(Y2[2]+1j*Y2[3]) - (Y2[0]+1j*Y2[1])*(Y1[2]+1j*Y1[3]))
    return C, D, float(np.max(np.abs(W - W[0]))/abs(W[0]))

out = {'C0': C0, 'D0': D0, 'sqrt(b/a)': Dl, 'Delta': Dlt}
res = {}
for prof in ('tanh', 'erf'):
    for kD in (0.01, 0.02, 2, 3, 4, 5, 6, 7, 8):
        for sgn in (1, -1):
            C, D, wdev = run(kD, sgn, prof)
            res[f'{prof}|{kD}|{sgn}'] = {'|C|': abs(C), '|D|': abs(D), 'Wronski_rel': wdev}
out['Werte'] = res
g = lambda p, k, s, q: res[f'{p}|{k}|{s}'][q]
# H86a
a_ok = {}
for prof in ('tanh', 'erf'):
    a_ok[prof] = all(g(prof, kD, s, '|C|') < 1e-2 for kD in (6, 7, 8) for s in (1, -1)) and \
        all(abs(np.sqrt(g(prof, kD, 1, '|D|')*g(prof, kD, -1, '|D|'))/Dl - 1) < 0.02 for kD in (6, 7, 8))
out['H86a'] = {'erfuellt': all(a_ok.values()), 'je_Profil': a_ok,
               'geom_Mittel_D/sqrt(b/a)': {p: [np.sqrt(g(p, kD, 1, '|D|')*g(p, kD, -1, '|D|'))/Dl for kD in (6, 7, 8)] for p in ('tanh', 'erf')}}
# H86b (tanh)
ks = np.array([2, 3, 4, 5, 6, 7, 8], float)
lc = {s: np.log([g('tanh', int(k), s, '|C|') for k in ks]) for s in (1, -1)}
fits = {}
for s in (1, -1):
    p = np.polyfit(ks, lc[s], 1); r = lc[s] - np.polyval(p, ks)
    fits[s] = {'Steigung_je_kDelta': p[0], 'R2': 1 - (r**2).sum()/((lc[s]-lc[s].mean())**2).sum(), '|C|': np.exp(lc[s]).tolist()}
out['H86b'] = {'fits': {str(s): v for s, v in fits.items()},
               'erfuellt': all(v['R2'] > 0.99 and abs(abs(v['Steigung_je_kDelta'])/np.pi - 1) < 0.15 for v in fits.values())}
# H86c
out['H86c'] = {p: [abs(g(p, 0.01, s, '|C|') - C0)/C0 for s in (1, -1)] for p in ('tanh', 'erf')}
out['H86c_erfuellt'] = all(v < 0.01 for p in ('tanh', 'erf') for v in out['H86c'][p])
# H86d
d_ = {}
for p in ('tanh', 'erf'):
    Dp, Dm = g(p, 0.02, 1, '|D|'), g(p, 0.02, -1, '|D|')
    d_[p] = {'|D-|/|D+|': Dm/Dp, 'geom/D0': np.sqrt(Dp*Dm)/D0}
out['H86d'] = d_
out['H86d_erfuellt'] = all(abs(v['|D-|/|D+|'] - 1) > 0.01 and abs(v['geom/D0'] - 1) < 0.02 for v in d_.values())
out['Kontrolle_Wronski_max'] = max(v['Wronski_rel'] for v in res.values())
json.dump(out, open('k201_out.json', 'w'), indent=1, default=float)
print(json.dumps({k: v for k, v in out.items() if k != 'Werte'}, indent=1, default=float))
