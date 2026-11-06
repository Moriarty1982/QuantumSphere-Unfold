"""k207: Test H92 - Vorfaktor der Urknall-Beimischung aus dem lokalen Problem an der Singularitaet t0 = i pi Delta/2.
Vorab-Notiz llm/Vorab_Notiz_H92_Vorfaktor_lokales_Problem.md (Commit c347a92).
Lokale Gleichung: y'' - (lam/sigma^2) y' + y = 0, lam = L kDelta/2; Weg sigma = s - i h (unterhalb der Singularitaet).
Von links e^{i sigma}, rechts e^{i sigma} + r e^{-i sigma}; Vorhersage |C| = |r(L kDelta/2)| e^{-pi kDelta}.
Rand- und Auswertewerte aus der asymptotischen Reihe y = e^{+-i sigma}(1 + sum a_n sigma^-n).
Aufruf (aus llm/): python k207_lokales_problem.py [k206_out.json] [ausgabe.json]
"""
import json, sys
import numpy as np
from scipy.integrate import solve_ivp

HF = 0.7   # Lauf 2 (Lauf 1: 1.5; dort verlor der grosse Weg Stellen, Kontrolle 3.7e-6/5.5e-6)
bsym = 1/1.8203; x2 = bsym**2; a, b = 1/(1+x2), x2/(1+x2)


def asym(sig, lam, sgn, N=40):
    """f = e^{sgn i sig} u, u = sum c_n sig^-n; gibt (f, f')."""
    c = [1.0+0j]; cm1 = 0j
    for m in range(N):
        cm = c[m]; prev = c[m-1] if m >= 1 else 0j
        nxt = (m*(m+1)*cm - sgn*1j*lam*cm + lam*(m-1)*prev)/(sgn*2j*(m+1))
        c.append(nxt)
    terms = [c[n]*sig**(-n) for n in range(N+1)]
    mags = np.abs(terms); stop = int(np.argmin(mags[1:]))+1      # optimales Abschneiden
    u = sum(terms[:stop+1]); du = sum(-n*c[n]*sig**(-n-1) for n in range(1, stop+1))
    e = np.exp(sgn*1j*sig)
    return e*u, e*(sgn*1j*u + du), float(mags[stop])


def r_of(lam, h, S):
    def rhs(s, y):
        sig = s - 1j*h
        return [y[1], lam/sig**2*y[1] - y[0]]
    f0, df0, _ = asym(-S - 1j*h, lam, +1)
    sol = solve_ivp(rhs, (-S, S), np.array([f0, df0], complex), method='DOP853', rtol=1e-12, atol=1e-30)
    y, dy = sol.y[0, -1], sol.y[1, -1]
    p, dp, _ = asym(S - 1j*h, lam, +1); q, dq, _ = asym(S - 1j*h, lam, -1)
    A, B = np.linalg.solve(np.array([[p, q], [dp, dq]]), np.array([y, dy]))
    return B/A


def r_check(lam):
    hb = 1.0 + np.sqrt(abs(lam)); Sb = 40*abs(lam) + 60
    r1 = r_of(lam, hb, Sb); r2 = r_of(lam, HF*hb, Sb); r3 = r_of(lam, hb, 2*Sb)
    return r1, float(max(abs(r2/r1 - 1), abs(r3/r1 - 1)))


if __name__ == '__main__':
    src = sys.argv[1] if len(sys.argv) > 1 else 'k206_out.json'
    d = json.load(open(src)); out = {}
    # H92d: Born-Grenzfall
    L0 = np.log(a/b) - 1j*np.pi
    lam0 = 1e-3*L0/abs(L0); r0, c0 = r_check(lam0)
    out['H92d'] = dict(lam=str(lam0), ratio=str(r0/(2*np.pi*lam0)), dev=float(abs(r0/(2*np.pi*lam0) - 1)), ctrl=c0)
    print('d:', out['H92d'])
    lnr = {}
    for sgn in (+1, -1):
        L = np.log(a/b) - sgn*1j*np.pi
        g = np.array(d[f'sgn{sgn:+d}']['grid']); lc = np.array(d[f'sgn{sgn:+d}']['lnC_095'])
        rs, ctrl = [], []
        for x in g:
            r, c = r_check(L*x/2); rs.append(r); ctrl.append(c)
        rs = np.array(rs); lnr[sgn] = np.log(np.abs(rs))
        lnR = lc + np.pi*g - lnr[sgn]
        m = (g >= 20) & (g <= 60)
        M = np.stack([np.ones(m.sum()), g[m]**-0.5, 1/g[m]], 1)
        co, *_ = np.linalg.lstsq(M, lnR[m], rcond=None); rms = float(np.sqrt(np.mean((M @ co - lnR[m])**2)))
        out[f'sgn{sgn:+d}'] = dict(grid=g.tolist(), ln_abs_r=lnr[sgn].tolist(), lnR=lnR.tolist(), ctrl_max=float(max(ctrl)),
                                   fit=dict(a0=co[0], a1=co[1], a2=co[2], rms=rms), r=[str(z) for z in rs])
        print(f'sgn {sgn:+d}: Kontrolle {max(ctrl):.1e}; a0 = {co[0]:+.4f}, a1 = {co[1]:+.3f}, a2 = {co[2]:+.3f}, rms = {rms:.1e}')
        print('   lnR:', np.round(lnR, 4).tolist())
    dc = float(np.max(np.abs(lnr[+1] - lnr[-1])))
    out['H92c'] = dict(max_diff_ln_abs_r=dc); print('c: max |ln|r(L+)| - ln|r(L-)|| =', dc)
    if len(sys.argv) > 2:
        json.dump(out, open(sys.argv[2], 'w'), indent=1)
