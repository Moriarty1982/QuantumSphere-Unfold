"""k210: Test H94 - gewichtete Norm am Urknall-Uebergang (G2), Bosonen gegen Fermionen.
Vorab-Notiz llm/Vorab_Notiz_H94_Norm_Bosonen_Fermionen.md (Commit 99f1cce).
Bosonen: (w chi')' + k^2 w chi = 0 wie k201 (tanh, Delta = 2), N = a(|C|^2 - |D|^2)/b.
Fermionen: Weyl entlang z, c (i phi' + k sigma_z phi) + (i/2) c' phi = 0, N_F = Q_nach/Q_vor, Q = c |phi|^2.
Aufruf (aus llm/): python k210_norm_uebergang.py [ausgabe.json]
"""
import json, sys
import numpy as np
from scipy.integrate import solve_ivp
from scipy.optimize import brentq

bsym = 1/1.8203; x = bsym**2; a, b = 1/(1+x), x/(1+x); Dlt = 2.0; Lb = 20*Dlt


def wfun(t, sgn):
    s = 0.5*(1 + np.tanh(t/Dlt)); ds = 0.5/(Dlt*np.cosh(t/Dlt)**2)
    w = b**(1-s)*a**s*np.exp(sgn*1j*np.pi*(1-s))
    return w, w*(np.log(a) - np.log(b) - sgn*1j*np.pi)*ds


def boson(kD, sgn):
    k = kD/Dlt
    def rhs(t, y):
        w, dw = wfun(t, sgn); return [y[1], -(dw/w)*y[1] - k**2*y[0]]
    sols = []
    for s0 in (+1, -1):
        c0 = np.exp(s0*1j*k*(-Lb)); sols.append(solve_ivp(rhs, (-Lb, Lb), np.array([c0, s0*1j*k*c0], complex),
                                                           method='DOP853', rtol=1e-12, atol=1e-15, dense_output=True))
    s = sols[0]; chi, d = s.y[0, -1], s.y[1, -1]
    C = (chi - d/(1j*k))/2*np.exp(1j*k*Lb); D = (chi + d/(1j*k))/2*np.exp(-1j*k*Lb)
    g = np.linspace(-Lb, Lb, 400); Y1, Y2 = sols[0].sol(g), sols[1].sol(g)
    W = np.array([wfun(t, sgn)[0] for t in g])*(Y1[0]*Y2[1] - Y2[0]*Y1[1])
    return C, D, float(np.max(np.abs(W - W[0]))/abs(W[0]))


def N_boson(kD, sgn):
    C, D, wr = boson(kD, sgn); return a*(abs(C)**2 - abs(D)**2)/b, abs(C), abs(D), wr


def N_fermion(kD, sgn):
    k = kD/Dlt; out = []
    for sz in (+1, -1):
        def rhs(t, p):
            w, dw = wfun(t, sgn); return [1j*k*sz*p[0] - dw/(2*w)*p[0]]
        p0 = np.exp(1j*sz*k*(-Lb))
        s = solve_ivp(rhs, (-Lb, Lb), np.array([p0], complex), method='DOP853', rtol=1e-12, atol=1e-15)
        wv, wn = wfun(-Lb, sgn)[0], wfun(Lb, sgn)[0]
        out.append((wn.real*abs(s.y[0, -1])**2)/(wv.real*abs(p0)**2))
    return out


if __name__ == '__main__':
    grid = [0.01, 0.02, 0.05] + [round(0.1*i, 1) for i in range(1, 11)] + [1.5, 2, 3, 4, 6, 8, 12, 16, 20]
    res = {}
    for sgn in (+1, -1):
        rows = [(kD,) + N_boson(kD, sgn) for kD in grid]
        Ns = np.array([r[1] for r in rows]); wmax = max(r[4] for r in rows)
        changes = int(np.sum(np.sign(Ns[1:]) != np.sign(Ns[:-1])))
        roots = []
        for i in range(len(grid)-1):
            if np.sign(Ns[i]) != np.sign(Ns[i+1]):
                roots.append(brentq(lambda q: N_boson(q, sgn)[0], grid[i], grid[i+1], xtol=1e-10))
        NF = [N_fermion(kD, sgn) for kD in grid]; nf_dev = float(max(abs(v + 1) for pair in NF for v in pair))
        mid = [(kD, N) for kD, N in zip(grid, Ns) if 0.1 < abs(N) < 0.9]
        res[f'sgn{sgn:+d}'] = dict(rows=[dict(kD=r[0], N=r[1], C=r[2], D=r[3], wronski=r[4]) for r in rows],
                                   sign_changes=changes, roots=roots, NF_max_dev=nf_dev, wronski_max=wmax,
                                   a_ok=bool(abs(Ns[0]-1) <= 0.05 and abs(Ns[-1]+1) <= 0.05), mid_points=mid)
        print(f'sgn {sgn:+d}: N(0.01) = {Ns[0]:+.4f}, N(20) = {Ns[-1]:+.4f}, Vorzeichenwechsel {changes}, Nullstellen {np.round(roots, 6).tolist()}, '
              f'0.1<|N|<0.9 an {len(mid)} Punkten, Fermionen max|N_F+1| = {nf_dev:.1e}, Wronski {wmax:.1e}')
        print('   N:', [f'{kD}:{N:+.3f}' for kD, N in zip(grid, Ns)])
    if len(sys.argv) > 1:
        json.dump(res, open(sys.argv[1], 'w'), indent=1)
