"""k206: Test H91 - Abfall der Beimischung am Urknall bis kDelta = 60 (tanh-Profil, Delta = 2, beide Drehsinne).
Vorab-Notiz llm/Vorab_Notiz_H91_Abfall_Beimischung_Wurzelterm.md (Commit a49ed7e).
Gleichung wie k201/k202: y'' = -(L/(2 Delta)) sech^2(tau/Delta) y' - k^2 y, L = ln(a/b) - sgn*i*pi,
integriert entlang tau = x + i h (h = hf * pi Delta/2), einlaufend e^{i k tau} von links,
C = Koeffizient von e^{-i k tau} rechts. Skalierung: Anfangswert ohne e^{-k h}; ln|C| = ln|...| - 2 k h.
Aufruf: python llm/k206_abfall_wurzelterm.py [ausgabe.json]
"""
import json, sys
import numpy as np
from scipy.integrate import solve_ivp

bsym = 1/1.8203; x2 = bsym**2; a, b = 1/(1+x2), x2/(1+x2)
Dl = 2.0; LL = 60.0


def lnC(kD, sgn, hf):
    k = kD/Dl; h = hf*np.pi*Dl/2; Lc = np.log(a/b) - sgn*1j*np.pi
    def rhs(x, y):
        tau = x + 1j*h
        p = Lc/(2*Dl)/np.cosh(tau/Dl)**2
        return [y[1], -p*y[1] - k**2*y[0]]
    y0 = [np.exp(-1j*k*LL), 1j*k*np.exp(-1j*k*LL)]
    s = solve_ivp(rhs, (-LL, LL), np.array(y0, complex), method='DOP853', rtol=1e-12, atol=1e-14, dense_output=False)
    yy, dy = s.y[0, -1], s.y[1, -1]
    c = (yy - dy/(1j*k))/2*np.exp(1j*k*LL)
    return float(np.log(abs(c)) - 2*k*h)


def fit(xs, ys, cols):
    M = np.stack(cols, 1); co, *_ = np.linalg.lstsq(M, ys, rcond=None)
    return co, float(np.sqrt(np.mean((M @ co - ys)**2)))


if __name__ == '__main__':
    grid = np.arange(10, 60.01, 2.5)
    h87 = {10: 4.230e-12, 15: 1.879e-18, 20: 8.942e-25, 25: 3.765e-31, 30: 1.304e-37}
    out = {}
    for sgn in (+1, -1):
        r90 = np.array([lnC(x, sgn, 0.90) for x in grid]); r95 = np.array([lnC(x, sgn, 0.95) for x in grid])
        agree = float(np.max(np.abs(np.expm1(r90 - r95))))
        o = dict(grid=grid.tolist(), lnC_095=r95.tolist(), lnC_090=r90.tolist(), contour_agreement_rel=agree)
        if sgn == +1:
            o['h87_rel'] = {k: float(np.exp(r95[list(grid).index(k)])/v - 1) for k, v in h87.items()}
        m = (grid >= 20) & (grid <= 60); xs, ys = grid[m], r95[m]
        cb, rb = fit(xs, ys, [np.ones_like(xs), np.sqrt(xs), np.log(xs), -xs])
        o['H91b'] = dict(c0=cb[0], c1=cb[1], q=cb[2], s=cb[3], s_rel_pi=float(cb[3]/np.pi - 1), rms=rb)
        yp = ys + np.pi*xs
        cw, rw = fit(xs, yp, [np.ones_like(xs), np.sqrt(xs), np.log(xs)])
        cn, rn = fit(xs, yp, [np.ones_like(xs), np.log(xs)])
        o['H91c'] = dict(with_sqrt=dict(c0=cw[0], c1=cw[1], q=cw[2], rms=rw), without=dict(c0=cn[0], q=cn[1], rms=rn),
                         ratio=float(rn/rw))
        i50, i60 = list(grid).index(50.0), list(grid).index(60.0)
        sl = -(r95[i60] - r95[i50])/10
        o['H91d'] = dict(slope_50_60=float(sl), rel_pi=float(sl/np.pi - 1))
        o['local_slopes'] = (-(np.diff(r95))/2.5).tolist()
        out[f'sgn{sgn:+d}'] = o
        print(f'sgn {sgn:+d}: Kontur {agree:.1e}; b: s = {cb[3]:.5f} ({cb[3]/np.pi-1:+.4%}), c1 = {cb[1]:.3f}, q = {cb[2]:.3f}, rms {rb:.1e}; '
              f'c: rms mit {rw:.1e}, ohne {rn:.1e}, Verh. {rn/rw:.1f}; d: {sl:.4f} ({sl/np.pi-1:+.2%})')
        if sgn == +1:
            print('   H87-Vergleich:', {k: f'{v:+.1e}' for k, v in o['h87_rel'].items()})
    if len(sys.argv) > 1:
        json.dump(out, open(sys.argv[1], 'w'), indent=1)
