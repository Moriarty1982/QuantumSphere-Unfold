"""k15: Test der Vorab-Notiz H2 (Commit 434c5a8).
Neutrinomassen m_k = t^2 (1 + sqrt2 cos(delta + 2 pi k/3))^2, r = 1, Vorzeichen der v_k frei.
Daten: NuFIT 6.0 IC24 with SK-atm. Kosmologie: Sigma < 0.0642 eV (DESI DR2 + CMB).
"""
import numpy as np
from scipy.optimize import brentq

D21, s21 = 7.49e-5, 0.19e-5
D31_NO, s31_NO = 2.513e-3, 0.020e-3   # (+0.021/-0.019) gemittelt
D32_IO, s32_IO = 2.484e-3, 0.020e-3
SIG_COSMO = 0.0642
W = {"NO": 0.05, "IO": 0.004}  # Suchfenster: NO-Loesungen weit getrennt, IO-Loesungen 0,011 auseinander
P = 2*np.pi/3

def v(d):
    return 1 + np.sqrt(2)*np.cos(d + P*np.arange(3))

def sorted_masses(d):  # in Einheiten t^2, aufsteigend, plus Vorzeichen in dieser Reihenfolge
    vv = v(d); m = vv**2; i = np.argsort(m)
    return m[i], np.sign(vv[i])

def ratio(d, order):
    (a, b, c), _ = sorted_masses(d)
    if order == "NO":
        return (b*b - a*a)/(c*c - a*a)
    return (c*c - b*b)/(c*c - a*a)

def solve(order, d21, dbig):
    target = d21/dbig
    grid = np.linspace(1e-9, P - 1e-9, 20001)  # eine Periode genuegt (zyklische Vertauschung)
    f = np.array([ratio(g, order) - target for g in grid])
    sols = []
    for j in np.where(np.sign(f[:-1]) != np.sign(f[1:]))[0]:
        # Spruenge an Sortierwechseln ausschliessen
        if abs(f[j] - f[j+1]) > 0.5:
            continue
        d = brentq(lambda x: ratio(x, order) - target, grid[j], grid[j+1], xtol=1e-14)
        (a, b, c), sg = sorted_masses(d)
        t2 = np.sqrt(dbig/(c*c - a*a))          # m = t^2 * v^2
        m = t2*np.array([a, b, c])
        sols.append(dict(delta=d, t=np.sqrt(t2), m=m, Sigma=m.sum(), signs=sg))
    return sols

def report(order, dbig, sbig):
    print(f"\n=== {order} ===")
    sols = solve(order, D21, dbig)
    if not sols:
        print("keine Loesung bei Zentralwerten")
    for k, s in enumerate(sols):
        print(f"Loesung {k}: delta={s['delta']:.6f}  m=({s['m'][0]:.5f}, {s['m'][1]:.5f}, {s['m'][2]:.5f}) eV"
              f"  Sigma={s['Sigma']:.5f} eV  Vorzeichen(a<b<c)={s['signs'].astype(int)}")
    # Monte Carlo
    rng = np.random.default_rng(15)
    N = 100000
    d21 = rng.normal(D21, s21, N); db = rng.normal(dbig, sbig, N)
    out = {k: [] for k in range(len(sols))}
    for x, y in zip(d21, db):
        ss = solve_fast(order, x, y, sols)
        for k, val in ss.items():
            out[k].append(val)
    for k, arr in out.items():
        arr = np.array(arr)
        if len(arr):
            print(f"  MC Loesung {k}: Sigma = {arr[:,0].mean():.5f} +- {arr[:,0].std():.5f} eV, "
                  f"m_leicht = {arr[:,1].mean():.5f} +- {arr[:,1].std():.5f} eV, "
                  f"95%-Bereich Sigma [{np.percentile(arr[:,0],2.5):.5f}, {np.percentile(arr[:,0],97.5):.5f}]")
    # 2-sigma-Grenzen der Eingaben
    for f21 in (-2, 2):
        for fb in (-2, 2):
            ss = solve(order, D21 + f21*s21, dbig + fb*sbig)
            print(f"  Eingaben ({f21:+d}s, {fb:+d}s): Sigma = " + ", ".join(f"{s['Sigma']:.5f}" for s in ss))
    return sols

def solve_fast(order, d21, dbig, ref):
    target = d21/dbig; res = {}
    for k, s in enumerate(ref):
        d0 = s['delta']
        try:
            d = brentq(lambda x: ratio(x, order) - target, d0 - W[order], d0 + W[order], xtol=1e-13)
        except ValueError:
            continue
        (a, b, c), _ = sorted_masses(d)
        t2 = np.sqrt(dbig/(c*c - a*a)); m = t2*np.array([a, b, c])
        res[k] = (m.sum(), m[0])
    return res

if __name__ == "__main__":
    # Kontrolle des Vorbefunds: K bei rein positiven Wurzeln, hierarchischer Grenzfall
    for name, ms in (("NO", [0, np.sqrt(D21), np.sqrt(D31_NO)]),
                     ("IO", [0, np.sqrt(D32_IO - D21), np.sqrt(D32_IO)])):
        ms = np.array(ms); print(f"Vorbefund {name}: K(alle +, m_leicht=0) = {ms.sum()/np.sqrt(ms).sum()**2:.4f}")
    rNO = report("NO", D31_NO, s31_NO)
    rIO = report("IO", D32_IO, s32_IO)
    print(f"\nKosmologie: Sigma < {SIG_COSMO} eV")
    # Koide-Kontrolle mit Vorzeichen
    for s in rNO + rIO:
        sq = s['signs']*np.sqrt(s['m'])
        print(f"  Kontrolle K = {s['m'].sum()/sq.sum()**2:.6f}")
