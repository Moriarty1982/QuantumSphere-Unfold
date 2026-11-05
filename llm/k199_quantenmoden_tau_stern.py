"""k199: Test H84 - komplexe Moden mit Wronski-Determinante i bei tau* (Strahlung, delta = 1, Materie-Gewichte).
Ausgabe k199_out.json im aktuellen Ordner.
"""
import json
import numpy as np
from scipy.integrate import solve_ivp

bsym = 1/1.8203; x = bsym**2; A, B = 1/(1+x), x/(1+x); d = 1.0
ts = bsym/(1 + bsym); kk, mm = 1.0, 1.0

def KP(t):
    a, aT = t, abs(d - t)
    return A*a**2 - B*aT**2, A*a**4 + B*aT**4

def rhs(t, y):          # y = [Re chi, Im chi, Re Kchi', Im Kchi']
    K, P = KP(t)
    return [y[2]/K, y[3]/K, -(K*kk**2 + P*mm**2)*y[0], -(K*kk**2 + P*mm**2)*y[1]]

def mode(t0):
    K0, _ = KP(t0)
    dchi = -1/(2*K0)                         # chi = 1, chi' = i*dchi  ->  K(chi chibar' - chibar chi') = i
    return [1.0, 0.0, 0.0, K0*dchi]

def wronski(y):
    chi = y[0] + 1j*y[1]; Kd = y[2] + 1j*y[3]
    return chi*np.conj(Kd) - np.conj(chi)*Kd

def energy(t, y):
    K, P = KP(t)
    chi = y[0] + 1j*y[1]; dchi = (y[2] + 1j*y[3])/K
    return 0.5*K*(abs(dchi)**2 + kk**2*abs(chi)**2) + 0.5*P*mm**2*abs(chi)**2

out = {'tau_stern': ts}
eps = np.logspace(-2, -8, 13)
for side, t0, sgn in (('links', 0.05, -1), ('rechts', 0.9, +1)):
    y0 = mode(t0); W0 = wronski(y0)
    rows = []
    for e in eps:
        s = solve_ivp(rhs, (t0, ts + sgn*e), y0, rtol=1e-12, atol=1e-14, method='DOP853')
        y = s.y[:, -1]; W = wronski(y)
        rows.append({'eps': e, 'Wronski_rel_Abw': abs(W - W0)/abs(W0), '|chi|': abs(y[0] + 1j*y[1]),
                     'E': energy(ts + sgn*e, y), 'E*eps': energy(ts + sgn*e, y)*e})
    last = [r['E*eps'] for r in rows if r['eps'] <= 1e-5 + 1e-20]
    out[side] = {'W0': str(W0), 'Zeilen': rows, 'max_Wronski_rel_Abw': max(r['Wronski_rel_Abw'] for r in rows),
                 'E*eps_letzte_drei_Dekaden': last, 'Streuung_rel': (max(last) - min(last))/abs(np.mean(last))}
out['H84a'] = bool(out['links']['max_Wronski_rel_Abw'] < 1e-8 and out['rechts']['max_Wronski_rel_Abw'] < 1e-8)
out['H84b'] = bool(out['links']['Streuung_rel'] < 0.05 and out['rechts']['Streuung_rel'] < 0.05
                  and np.sign(np.mean(out['links']['E*eps_letzte_drei_Dekaden'])) != np.sign(np.mean(out['rechts']['E*eps_letzte_drei_Dekaden'])))
json.dump(out, open('k199_out.json', 'w'), indent=1, default=float)
print(json.dumps({k: v for k, v in out.items() if k not in ('links', 'rechts')}, indent=1, default=float))
for side in ('links', 'rechts'):
    print(side, 'max W-Abw', out[side]['max_Wronski_rel_Abw'], 'E*eps', [round(v, 5) for v in out[side]['E*eps_letzte_drei_Dekaden']], 'Streuung', out[side]['Streuung_rel'])
