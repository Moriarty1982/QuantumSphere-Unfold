"""k208: Test H93 - WKB-Asymptotik der Urknall-Beimischung.
Vorab-Notiz llm/Vorab_Notiz_H93_Wurzelgesetz_WKB.md (Commit a4b1d17).
Vorhersage: ln|r(L x/2)| = c sqrt(x), c = 2 sqrt(pi) Gamma(3/4)/Gamma(1/4) Re sqrt(L);
            ln|C(x)| = -pi x + c sqrt(x) - Re L/2.
Lokal wie k207 (h = 1 + 0.5 sqrt|lam|), voll wie k206 (Konturen 0.90/0.95, rtol 1e-13).
Aufruf (aus llm/): python k208_wkb_pruefung.py [ausgabe.json]
"""
import json, sys
from math import gamma, pi, sqrt
import numpy as np
from scipy.integrate import solve_ivp
from k207_lokales_problem import asym

bsym = 1/1.8203; x2 = bsym**2; a, b = 1/(1+x2), x2/(1+x2)
# Lauf 2: Kontrollweg 1.3*h statt 0.7*h (0.7*h verlor bei Drehsinn + Stellen, Lauf 1 Kontrolle bis 1.0), rtol lokal 1e-13
HCTRL = 1.3; RTOL_LOC = 1e-13
Dl = 2.0; G = 2*sqrt(pi)*gamma(0.75)/gamma(0.25)


def r_of(lam, h, S):
    def rhs(s, y):
        sig = s - 1j*h
        return [y[1], lam/sig**2*y[1] - y[0]]
    f0, df0, _ = asym(-S - 1j*h, lam, +1)
    sol = solve_ivp(rhs, (-S, S), np.array([f0, df0], complex), method='DOP853', rtol=RTOL_LOC, atol=1e-30)
    y, dy = sol.y[0, -1], sol.y[1, -1]
    p, dp, _ = asym(S - 1j*h, lam, +1); q, dq, _ = asym(S - 1j*h, lam, -1)
    A, B = np.linalg.solve(np.array([[p, q], [dp, dq]]), np.array([y, dy]))
    return B/A


def lnC(kD, sgn, hf, LL=60.0):
    k = kD/Dl; h = hf*np.pi*Dl/2; Lc = np.log(a/b) - sgn*1j*np.pi
    def rhs(x, y):
        p = Lc/(2*Dl)/np.cosh((x + 1j*h)/Dl)**2
        return [y[1], -p*y[1] - k**2*y[0]]
    y0 = [np.exp(-1j*k*LL), 1j*k*np.exp(-1j*k*LL)]
    s = solve_ivp(rhs, (-LL, LL), np.array(y0, complex), method='DOP853', rtol=1e-13, atol=1e-16)
    c = (s.y[0, -1] - s.y[1, -1]/(1j*k))/2*np.exp(1j*k*LL)
    return float(np.log(abs(c)) - 2*k*h)


if __name__ == '__main__':
    out = {'G': G}
    for sgn in (+1, -1):
        L = np.log(a/b) - sgn*1j*np.pi; c = G*np.sqrt(L).real; o = {'c_pred': c}
        loc = {}
        for x in (300, 600):
            lam = L*x/2; h = 1 + 0.5*sqrt(abs(lam)); S = 10*abs(lam) + 60
            r1 = r_of(lam, h, S); r2 = r_of(lam, HCTRL*h, S); r3 = r_of(lam, h, 2*S)
            ctrl = float(max(abs(r2/r1 - 1), abs(r3/r1 - 1)))
            loc[x] = dict(ln_r=float(np.log(abs(r1))), ctrl=ctrl, dev=float(np.log(abs(r1)) - c*sqrt(x)))
            print(f'sgn {sgn:+d} lokal x={x}: ln|r| = {loc[x]["ln_r"]:.6f}, Abw. = {loc[x]["dev"]:+.5f}, Kontrolle {ctrl:.1e}', flush=True)
        slope = (loc[600]['ln_r'] - loc[300]['ln_r'])/(sqrt(600) - sqrt(300))
        o.update(local=loc, slope=slope, slope_rel=slope/c - 1)
        full = {}
        for x in (80, 100, 120):
            l95 = lnC(x, sgn, 0.95); l90 = lnC(x, sgn, 0.90)
            full[x] = dict(lnC=l95, contour=float(abs(np.expm1(l95 - l90))), dev=float(l95 + pi*x - c*sqrt(x) + 0.5*np.log(a/b)))
            print(f'sgn {sgn:+d} voll x={x}: Abw. = {full[x]["dev"]:+.5f}, Konturen {full[x]["contour"]:.1e}', flush=True)
        o['full'] = full
        print(f'sgn {sgn:+d}: c_pred = {c:.6f}, Steigung = {slope:.6f} ({slope/c-1:+.4%})', flush=True)
        out[f'sgn{sgn:+d}'] = o
    if len(sys.argv) > 1:
        json.dump(out, open(sys.argv[1], 'w'), indent=1)
