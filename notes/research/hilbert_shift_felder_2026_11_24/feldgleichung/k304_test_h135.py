#!/usr/bin/env python3
"""k304: Test H135. Ist kappa ~ 1,2 ein selbststabilisierender Punkt?

Vorab-Notiz: notes/research/predictions/Vorab_Notiz_H135_Kappa_selbststabilisierend.md
Werkzeug: Python (numpy, sympy, scipy). Gegenprobe: k304b_gegenprobe.wl.
Aufruf: python3 k304_test_h135.py > k304_out.txt
"""
import numpy as np
import sympy as sp
from scipy.integrate import solve_ivp
from scipy.optimize import brentq, minimize_scalar

mW, mZ, mt, mh, v = 80.37, 91.19, 172.6, 125.2, 246.22   # GeV, aus dem Gedaechtnis wie k300
g2, gp2, yt2 = 4 * mW**2 / v**2, 4 * (mZ**2 - mW**2) / v**2, 2 * mt**2 / v**2
cW, cZ, ct = g2 / 4, (g2 + gp2) / 4, yt2 / 2          # c_i^2 = m_i^2/phi^2
kstar, k1 = 1.2039, 1.2004
lo, hi = kstar * np.sqrt(0.8), kstar * np.sqrt(1.2)
kmin = np.sqrt((12 * ct**2 - 6 * cW**2 - 3 * cZ**2) / 4) / 2
print(f"g² = {g2:.4f}, g'² = {gp2:.4f}, y_t² = {yt2:.4f}; Fenster {lo:.4f} bis {hi:.4f}; kappa_min = {kmin:.4f}")

print()
print("=== K-a (L1): Fluss ===")
lA, kp, lC, s = sp.symbols('lambda_A kappa lambda_C s', positive=True)
bA, bK, bC = 8 * (kp**2 + 12 * lA**2), 16 * kp * (kp + 3 * lA + 3 * lC), 8 * (kp**2 + 12 * lC**2)
print("Homogenitaet: beta(s·g) − s²·beta(g) =", [sp.simplify(b.subs({lA: s * lA, kp: s * kp, lC: s * lC}, simultaneous=True) - s**2 * b) for b in (bA, bK, bC)])
print("gemeinsame Nullstellen der drei beta (reell):", sp.solve([bA, bK, bC], [lA, kp, lC], dict=True), "(leere Liste: nur der Ursprung, der bei positiven Symbolen ausgeschlossen ist)")
f = sp.lambdify((lA, kp, lC), [bA, bK, bC], 'numpy')


def run(k0, tend, c0=0.0, a0=0.0):
    def ev(t, y):
        return np.max(np.abs(y)) - 4 * np.pi
    ev.terminal = True
    sol = solve_ivp(lambda t, y: np.array(f(*y)) / (16 * np.pi**2), (0, tend), [a0, k0, c0], rtol=1e-10, atol=1e-12, events=ev, max_step=0.02)
    return sol.y[:, -1], (sol.t_events[0][0] if sol.t_events[0].size else None)


print("kappa(v) = 1,2039, lA = lC = 0 bei mu = v; Lauf zu kleinen Skalen (t < 0) und zu grossen (t > 0):")
for t in (-5, -4, -3, -2, -1, 0, 1, 2, 3):
    y = run(kstar, t)[0] if t != 0 else np.array([0, kstar, 0])
    print(f"  t = {t:+3d} (mu = {v*np.exp(t):.3e} GeV): lA = {y[0]:+.4f}, kappa = {y[1]:.4f}, lC = {y[2]:+.4f}")
for tend, name in ((-60, "kleinen"), (60, "grossen")):
    y, te = run(kstar, tend)
    print(f"  eine Kopplung ueberschreitet 4π zu {name} Skalen bei t = {te:.3f} (mu = {v*np.exp(te):.3e} GeV), dort (lA, kappa, lC) = {np.round(y, 2)}")
print("Naehern sich benachbarte Startwerte an? kappa(v) = 1,0 / 1,2 / 1,4:")
for t in (-5, -3, -1, 1, 3):
    vals = [run(k0, t)[0][1] for k0 in (1.0, 1.2, 1.4)]
    print(f"  t = {t:+d}: {[round(x, 4) for x in vals]}, Spanne {vals[2]-vals[0]:.4f} (Start 0,4)")
print("d(beta_kappa)/d(kappa) bei (0, kappa*, 0) =", float(sp.diff(bK, kp).subs({lA: 0, kp: kstar, lC: 0})), "(ungleich null: kein fester Punkt)")

print()
print("=== K-b (L2): Vakuumtiefe bei fester Skala Lambda ===")


def AB(kap, with_sm=True):
    cS = 2 * kap
    terms = [(4, cS, 1.5, +1)]
    if with_sm:
        terms += [(6, cW, 5 / 6, +1), (3, cZ, 5 / 6, +1), (12, ct, 1.5, -1)]
    B = sum(sg * n * c**2 for n, c, k, sg in terms) / (64 * np.pi**2)
    A = sum(sg * n * c**2 * (np.log(c) - k) for n, c, k, sg in terms) / (64 * np.pi**2)
    return A, B


def F(kap, with_sm=True):
    A, B = AB(kap, with_sm)
    return B * np.exp(-2 * A / B)


def v_over_L(kap):
    A, B = AB(kap)
    return np.exp(0.5 * (-0.5 - A / B))


Finf = np.exp(3) / (16 * np.pi**2)
print(f"Grenzwert fuer grosses kappa: e³/(16π²) = {Finf:.6f}; ohne Eichfelder und Top ist F fuer jedes kappa gleich: {[round(F(k, False), 6) for k in (0.5, 1.2, 3.0)]}")
print(f"{'kappa':>7s} {'F':>10s} {'F/F_inf':>9s} {'v/Lambda':>9s} {'m_S/Lambda':>10s} {'m_h/GeV':>8s}")
grid = [0.42, 0.45, 0.5, 0.6, 0.8, 1.0, lo, k1, kstar, hi, 1.5, 2.0, 2.5, np.pi, 5.0, 10.0, 30.0]


def mh_of(kap):
    sq = 4 * (2 * kap * v**2)**2 + 6 * mW**4 + 3 * mZ**4 - 12 * mt**4
    return np.sqrt(sq / (8 * np.pi**2 * v**2))


for k_ in grid:
    print(f"{k_:7.4f} {F(k_):10.6f} {F(k_)/Finf:9.5f} {v_over_L(k_):9.5f} {np.sqrt(2*k_)*v_over_L(k_):10.5f} {mh_of(k_):8.1f}")
ks = np.linspace(kmin * 1.0005, 40, 400001)
Fs = np.array([F(k_) for k_ in ks[::40]])
dF = np.diff(Fs)
sign_changes = np.where(np.sign(dF[1:]) != np.sign(dF[:-1]))[0]
print("Vorzeichenwechsel der Steigung von F auf (kappa_min, 40]:", len(sign_changes))
if len(sign_changes):
    for i in sign_changes:
        ka, kb = ks[::40][i], ks[::40][i + 2]
        res = minimize_scalar(lambda x: -F(x), bounds=(ka, kb), method='bounded', options={'xatol': 1e-10})
        kind = "Maximum" if dF[i] > 0 else "Minimum"
        if kind == "Minimum":
            res = minimize_scalar(F, bounds=(ka, kb), method='bounded', options={'xatol': 1e-10})
        print(f"  {kind} bei kappa = {res.x:.4f}: F/F_inf = {F(res.x)/Finf:.5f}, m_S = {np.sqrt(2*res.x)*v:.1f} GeV, m_h = {mh_of(res.x):.1f} GeV, im Fenster: {lo <= res.x <= hi}")
print(f"F ueberschreitet F_inf? max F/F_inf auf dem Gitter = {Fs.max()/Finf:.5f} bei kappa = {ks[::40][Fs.argmax()]:.3f}")
print(f"relative Steigung d ln F/d ln kappa bei kappa*: {(np.log(F(kstar*1.001)) - np.log(F(kstar)))/np.log(1.001):.4f}")
print("Zum Vergleich bei festem v: Tiefe = m_s² v²/16, waechst monoton mit kappa (kein Extremum).")

print()
print("=== L3: Haeufigkeit (ohne Kriterium) ===")
print(f"Anteil der kappa in (0, π] mit Vakuum, gleichverteilt: {(np.pi - kmin)/np.pi:.3f}; log-gleichverteilt auf [0,01, π]: {np.log(np.pi/kmin)/np.log(np.pi/0.01):.3f}")
print(f"m_h reicht dabei von 0 bis {mh_of(np.pi):.0f} GeV; Anteil mit m_h zwischen 120 und 130 GeV (gleichverteilt auf (0, π]):", end=" ")
ka = brentq(lambda x: mh_of(x) - 120, kmin * 1.001, np.pi)
kb = brentq(lambda x: mh_of(x) - 130, kmin * 1.001, np.pi)
print(f"{(kb - ka)/np.pi:.4f} (kappa von {ka:.4f} bis {kb:.4f})")
