#!/usr/bin/env python3
"""k305: Test H136. Rueckwirkung ueber den HC-Winkel.

Vorab-Notiz: notes/research/predictions/Vorab_Notiz_H136_Rueckwirkung_HC_Winkel.md
Werkzeug: Python (numpy, scipy). Gegenprobe: k305b_gegenprobe.wl.
Aufruf: python3 k305_test_h136.py > k305_out.txt
"""
import itertools
import numpy as np
from scipy.optimize import brentq

mW, mZ, mt, mh, v = 80.37, 91.19, 172.6, 125.2, 246.22   # GeV, aus dem Gedaechtnis wie k300
g2, gp2, yt2 = 4 * mW**2 / v**2, 4 * (mZ**2 - mW**2) / v**2, 2 * mt**2 / v**2
cW, cZ, ct0 = g2 / 4, (g2 + gp2) / 4, yt2 / 2
mu = 0.3018
th0 = np.arctan(mu)
kstar = 1.2039
rule = lambda th: 1 / np.cos(2 * th)
print(f"theta0 = {np.degrees(th0):.3f} Grad, 1/cos(2 theta0) = {rule(th0):.4f}, kappa* = {kstar}")

print()
print("=== Stufe 1 (K-a): Invarianten auf a = psi1 + chi·j ===")


def qmul(p, q):
    a0, a1, a2, a3 = p
    b0, b1, b2, b3 = q
    return np.array([a0*b0 - a1*b1 - a2*b2 - a3*b3, a0*b1 + a1*b0 + a2*b3 - a3*b2,
                     a0*b2 - a1*b3 + a2*b0 + a3*b1, a0*b3 + a1*b2 - a2*b1 + a3*b0])


E = np.eye(4)
L = [np.array([qmul(E[u], E[k]) for k in range(4)]).T for u in (1, 2, 3)]
Ri = np.array([qmul(E[k], E[1]) for k in range(4)]).T


def invariants(gens, d, n=4):
    mons = [e for e in itertools.product(range(d + 1), repeat=n) if sum(e) == d]
    idx = {e: k for k, e in enumerate(mons)}
    rows = []
    for X in gens:
        D = np.zeros((len(mons), len(mons)))
        for e in mons:
            for i in range(n):
                if e[i] == 0:
                    continue
                for j in range(n):
                    if X[i, j] == 0:
                        continue
                    f = list(e); f[i] -= 1; f[j] += 1
                    D[idx[tuple(f)], idx[e]] += X[i, j] * e[i]
        rows.append(D)
    s_ = np.linalg.svd(np.vstack(rows), compute_uv=False)
    null = np.linalg.svd(np.vstack(rows))[2][np.sum(s_ > 1e-9):]
    return mons, idx, null


def contains(mons, idx, null, poly):
    vec = np.zeros(len(mons))
    for e, c in poly.items():
        vec[idx[e]] = c
    return np.linalg.norm(vec - null.T @ (null @ vec)) < 1e-9


A1 = {(2, 0, 0, 0): 1, (0, 2, 0, 0): 1}
Bq = {(0, 0, 2, 0): 1, (0, 0, 0, 2): 1}
diff = {**A1, **{k: -c for k, c in Bq.items()}}
for name, gens in (("SU(2) links × U(1) rechts", L + [Ri]), ("U(1) links × U(1) rechts", [L[0], Ri])):
    out = []
    for d in (2, 4):
        mons, idx, null = invariants(gens, d)
        out.append(null.shape[0])
        if d == 2:
            dep = contains(mons, idx, null, diff)
    print(f"{name}: Invarianten Grad 2: {out[0]}, Grad 4: {out[1]}; A1 − B (haengt an theta) invariant: {dep}")

print()
print("=== Modell U: Tiefe des Vakuums als Funktion von theta ===")


def AB(th, k1, k2, top_theta=True):
    cS = 2 * (k1 * np.cos(th)**2 + k2 * np.sin(th)**2)
    ct = ct0 * (np.cos(th) / np.cos(th0))**2 if top_theta else ct0
    if cS <= 0:
        return np.nan, np.nan          # Anhang haette negatives Massenquadrat
    ct = max(ct, 1e-300)
    terms = [(4, cS, 1.5, +1), (6, cW, 5 / 6, +1), (3, cZ, 5 / 6, +1), (12, ct, 1.5, -1)]
    B = sum(sg * n * c**2 for n, c, k, sg in terms) / (64 * np.pi**2)
    A = sum(sg * n * c**2 * (np.log(c) - k) for n, c, k, sg in terms) / (64 * np.pi**2)
    return A, B


def F(th, k1, k2, top_theta=True):
    A, B = AB(th, k1, k2, top_theta)
    if not np.isfinite(B):
        return np.nan
    return B * np.exp(-2 * A / B) if B > 0 else 0.0


def d1(fun, x, h=1e-5):
    return (fun(x + h) - fun(x - h)) / (2 * h)


def d2(fun, x, h=1e-4):
    return (fun(x + h) - 2 * fun(x) + fun(x - h)) / h**2


print("--- Stufe 2: mit HC-Strafe eta, Verschiebung von theta durch die Schleife des Anhangs (fuehrende Ordnung) ---")
A0, B0 = AB(th0, kstar, kstar)
lnv2L2 = -0.5 - A0 / B0
M2 = 2 * kstar
dV1_pref = (4 / (64 * np.pi**2)) * 2 * M2 * (np.log(M2) + lnv2L2 - 1) * 2 * np.sin(2 * th0)   # mal (k2 − k1), in v^4
stiff = 2 * np.sin(2 * th0)**2 * (1 + mu**2)**2                                          # mal eta, in v^4
print(f"ln(v²/Lambda²) = {lnv2L2:.4f}; dV1/dtheta = {dV1_pref:.5f}·(k2 − k1)·v⁴; d²V0/dtheta² = {stiff:.4f}·eta·v⁴")
for eta in (0.1, 1.0, 6.6):
    for dl in (-0.5, 0.5):
        dth = -dV1_pref * dl / (stiff * eta)
        print(f"  eta = {eta}, k2 − k1 = {dl:+.1f}: Verschiebung {np.degrees(dth):+.3f} Grad; Regel 1/cos2theta aendert sich um {rule(th0 + dth) - rule(th0):+.5f}")
print("  Die Verschiebung ist klein gegen theta0 und proportional zu (k2 − k1)/eta: sie haengt an zwei freien Zahlen.")

print()
print("--- Stufe 3 (K-b, K-c): Schleifen allein (eta = 0) ---")
s0, c0 = np.sin(th0)**2, np.cos(th0)**2


def ks(dl):            # (k1, k2) mit kappa_eff(theta0) = kappa* und k2 − k1 = dl
    k1 = kstar - dl * s0
    return k1, k1 + dl


g_stat = lambda dl: d1(lambda th: F(th, *ks(dl)), th0)
grid = np.linspace(-3, 3, 601)
vals = [g_stat(x) for x in grid]
roots = [brentq(g_stat, grid[i], grid[i + 1], xtol=1e-13) for i in range(len(grid) - 1) if vals[i] * vals[i + 1] < 0]
print("Loesungen k2 − k1 mit dF/dtheta(theta0) = 0:", [round(r, 5) for r in roots])
slope_rule = 2 * np.sin(2 * th0) / np.cos(2 * th0)**2
for dl in roots:
    k1, k2 = ks(dl)
    curv = d2(lambda th: F(th, k1, k2), th0)
    slope = dl * np.sin(2 * th0)
    print(f"  k1 = {k1:.4f}, k2 = {k2:.4f} (beide in (0, π): {0 < k1 < np.pi and 0 < k2 < np.pi}); kappa_eff(theta0) = {k1*c0 + k2*s0:.4f}")
    print(f"  d²F/dtheta² bei theta0 = {curv:+.5f}  ->  {'Maximum (stabil)' if curv < 0 else 'Minimum (instabil)'}")
    ths = np.radians(np.linspace(0, 90, 181))
    Fs = np.array([F(t, k1, k2) for t in ths])
    ok = np.isfinite(Fs)
    print(f"  kappa_eff > 0 nur fuer theta < {np.degrees(ths[ok][-1]):.1f}°; F(0) = {Fs[0]:.5f}, F(theta0) = {F(th0, k1, k2):.5f}, F(45°) = {Fs[90]:.5f}, F(70°) = {Fs[140]:.5f}")
    print(f"  groesstes F im zulaessigen Bereich bei {np.degrees(ths[np.nanargmax(Fs)]):.1f}°, kleinstes bei {np.degrees(ths[np.nanargmin(Fs)]):.1f}°")
    print(f"  Steigung d kappa_eff/d theta = {slope:+.4f}; Regel: {slope_rule:+.4f}; Verhaeltnis {slope/slope_rule:+.3f}")
print("Kontrolle ohne theta-Abhaengigkeit des Top: dF/dtheta(theta0) fuer k2 − k1 = −0,5 / 0 / +0,5:",
      [round(d1(lambda th: F(th, *ks(dl), top_theta=False), th0), 6) for dl in (-0.5, 0.0, 0.5)], "(nur k1 = k2 ist stationaer, und dann ist F flach)")
print("Welche Steigung haette die Regel noetig? k2 − k1 =", round(slope_rule / np.sin(2 * th0), 4), "; dort dF/dtheta(theta0) =", round(g_stat(slope_rule / np.sin(2 * th0)), 6))
