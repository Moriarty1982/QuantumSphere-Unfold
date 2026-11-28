"""k446 (Test H232): Rueckwaertssuche nach dem Brecher des Sektortauschs.
Vorab-Notiz Vorab_H232_Rueckwaerts_Brecher.md (vor der Rechnung committet). Modell wie H225/H226:
V_Im = -cos2(d - pi/4 - phi) + P_Im(cos3d),  V_Re = cos2(d - phi) + P_Re(cos3d),  P(c) = q c + r (2c^2 - 1) [= q cos3d + r cos6d].
Aufruf aus diesem Ordner: python3 k446_test_h232.py > k446_out.txt
"""
import numpy as np
from scipy.optimize import brentq

X = np.pi / 12 - 0.2222220470731
SIG = 7.8e-7
XNU, SXNU = 0.04336, 0.00213
Q0 = -0.0852
BS, GL = 0.549405640974529, 1.864699764609373
DG = np.linspace(0, 2 * np.pi, 8001)[:-1]


def V(d, sec, phi, q, r, eps=0.0):
    c = np.cos(3 * d)
    P = q * c + r * (2 * c * c - 1)
    if sec == "Im":
        return -np.cos(2 * (d - np.pi / 4 - phi)) + P + eps * c
    return np.cos(2 * (d - phi)) + P


def dV(d, sec, phi, q, r, eps=0.0):
    c = np.cos(3 * d)
    dP = (q + 4 * r * c + (eps if sec == "Im" else 0.0)) * (-3 * np.sin(3 * d))
    if sec == "Im":
        return 2 * np.sin(2 * (d - np.pi / 4 - phi)) + dP
    return -2 * np.sin(2 * (d - phi)) + dP


def dmin(sec, phi, q, r, eps=0.0):
    """globales Minimum in delta, Verfeinerung per Nullstelle von V'"""
    v = V(DG, sec, phi, q, r, eps)
    best = (np.inf, None)
    h = DG[1] - DG[0]
    for k in np.argsort(v)[:10]:
        a, b = DG[k] - h, DG[k] + h
        fa, fb = dV(a, sec, phi, q, r, eps), dV(b, sec, phi, q, r, eps)
        if fa * fb > 0:
            continue
        d = brentq(lambda t: dV(t, sec, phi, q, r, eps), a, b, xtol=1e-15)
        e = V(d, sec, phi, q, r, eps)
        if e < best[0] - 1e-15:
            best = (e, d)
    return best


def fold(d):
    d = d % (2 * np.pi / 3)
    return min(d, 2 * np.pi / 3 - d)


def offs(phi, q, r, eps=0.0):
    eI, dI = dmin("Im", phi, q, r, eps)
    eR, dR = dmin("Re", phi, q, r, eps)
    return np.pi / 12 - fold(dI), np.pi / 6 - fold(dR), eI + eR, dI, dR


def dE(phi, q, r, eps=0.0):
    eI, dI = dmin("Im", phi, q, r, eps)
    eR, dR = dmin("Re", phi, q, r, eps)
    return -2 * np.sin(2 * (dI - np.pi / 4 - phi)) + 2 * np.sin(2 * (dR - phi))


def global_minima(q, r, eps=0.0, n=720):
    ph = np.linspace(0, 2 * np.pi / 3, n, endpoint=False)
    e = np.array([offs(p, q, r, eps)[2] for p in ph])
    out = []
    for i in range(n):
        if e[i] <= e[i - 1] and e[i] <= e[(i + 1) % n]:
            a, b = ph[i] - ph[1], ph[i] + ph[1]
            try:
                p = brentq(lambda t: dE(t, q, r, eps), a, b, xtol=1e-15)
            except ValueError:
                p = ph[i]
            out.append((offs(p, q, r, eps)[2], p))
    out.sort()
    emin = out[0][0]
    return [p for v, p in out if v < emin + 1e-11], out


def solve_at_x(q, r, eps=0.0):
    """Modulus-Minimum, dessen Im-Versatz nahe x liegt: (phi, off_Im, off_Re, global?)"""
    glob, allm = global_minima(q, r, eps)
    best = None
    for v, p in allm:
        oI, oR, e, dI, dR = offs(p, q, r, eps)
        if best is None or abs(oI - X) < abs(best[1] - X):
            best = (p, oI, oR, any(abs(p - g) < 1e-7 for g in glob), e)
    return best


print("=" * 96)
print("H232 (k446)  Rueckwaertssuche nach dem Brecher: symmetrisches P(c) = q c + r cos6d bei q = -0,0852")
print("=" * 96)

# ---- A numerisch ----
print("\nTeil A1 (nicht blind)  Stationaritaet: off_Im + off_Re = 2 phi an jedem stationaeren phi")
for q, r, eps in ((Q0, 0.0, 0.0), (Q0, 0.05, 0.0), (Q0, 0.057, 0.03), (-0.2, 0.1, -0.05)):
    glob, allm = global_minima(q, r, eps, n=360)
    for v, p in allm[:3]:
        oI, oR, e, dI, dR = offs(p, q, r, eps)
        print(f"  q={q}, r={r}, eps={eps}: phi = {p:.10f}, (off_Im + off_Re)/2 = {(oI + oR)/2:.10f}  (Diff {((oI+oR)/2 - p + np.pi/4) % (np.pi/2) - np.pi/4:+.1e})")
print(f"  Daten: phi* = (x + x_nu)/2 = {(X + XNU)/2:.5f} +- {SXNU/2:.5f}")

print("\nTeil A2 (nicht blind)  fuehrende Ordnung: c0 = 0,374590, r/|q| = 0,667396 (siehe Vorab)")
for q in (-1e-4,):
    r_lo = 0.667396 * abs(q)
    p, oI, oR, g, e = solve_at_x(q, r_lo)
    print(f"  q = {q}: r = 0,667396 |q| -> Im-Versatz am Minimum {oI:.7f} (x = {X:.7f}), Re-Versatz {oR:.7f}, global {g}")

# ---- B ----
print("\nTeil B (blind)  q = -0,0852: Abtastung r, Im-Versatz am globalen Minimum")
rs = np.linspace(0.02, 0.12, 51)
rows = []
for r in rs:
    p, oI, oR, g, e = solve_at_x(Q0, r)
    rows.append((r, p, oI, oR, g))
for r, p, oI, oR, g in rows[::5]:
    print(f"  r = {r:.4f} (r/|q| = {r/abs(Q0):.4f}): phi = {p:.6f}, off_Im = {oI:+.6f}, off_Re = {oR:+.6f}, global {g}")
f = np.array([row[2] - X for row in rows])
roots = []
for i in np.nonzero(np.sign(f[:-1]) * np.sign(f[1:]) < 0)[0]:
    if abs(f[i] - f[i + 1]) > 0.1:
        continue
    rr = brentq(lambda r: solve_at_x(Q0, r)[1] - X, rs[i], rs[i + 1], xtol=1e-14)
    roots.append(rr)
okB1 = okB2 = False
for rr in roots:
    p, oI, oR, g, e = solve_at_x(Q0, rr)
    h = 1e-6
    der = (solve_at_x(Q0, rr + h)[1] - solve_at_x(Q0, rr - h)[1]) / (2 * h)
    sr = SIG / abs(der)
    z = (oR - XNU) / SXNU
    eI, dI = dmin("Im", p, Q0, rr); eR, dR = dmin("Re", p, Q0, rr)
    b1 = g and abs(z) <= 2
    okB1 |= b1
    rat = rr / abs(Q0)
    srat = sr / abs(Q0)
    zK = (rat - 2 / 3) / srat
    okB2 |= b1 and abs(zK) <= 2
    print(f"\n  r* = {rr:.12f}  r*/|q| = {rat:.10f} +- {srat:.2e}  (phi = {p:.10f}, off_Im = {oI:.10f}, global {g})")
    print(f"     x_nu,pred = off_Re = {oR:.6f}  ({z:+.2f} sigma);  Datenzweige: delta_Im = {dI:.6f} (Klasse {fold(dI):.6f}),"
          f" delta_Re = {dR:.6f} (Klasse {fold(dR):.6f})")
    print(f"     Abstand zu 2/3: {(rat - 2/3):+.3e} = {zK:+.1f} sigma_r ({(rat/(2/3) - 1)*100:+.3f} %)")
    for nm, val in (("1/2", 0.5), ("1/sqrt2", 2 ** -0.5), ("beta_sym", BS), ("1/gamma_L", 1 / GL), ("3/4", 0.75), ("1", 1.0)):
        print(f"       {nm:10s} = {val:.6f}: {(rat/val - 1)*100:+.2f} %")
    c0 = -Q0 / (4 * rr)
    print(f"     c0 = -q/(4r) = {c0:.8f} (3/8: {(c0/0.375 - 1)*100:+.3f} %)")
if not roots:
    print("  kein r* im Bereich")

# Wert bei r = 2/3 |q| direkt
p, oI, oR, g, e = solve_at_x(Q0, 2 / 3 * abs(Q0))
print(f"\n  direkt r = 2/3 |q| = {2/3*abs(Q0):.6f}: phi = {p:.10f}, off_Im = {oI:.10f} (x {X:.10f}, Abstand {(oI - X)/SIG:+.1f} sigma_x), off_Re = {oR:.6f}, global {g}")

# ---- C ----
print("\nTeil C (nur Bericht)  r*/|q| in Abhaengigkeit von q")
for q in (-0.001, -0.01, -0.03, -0.0852, -0.15, -0.3):
    lo, hi = 0.3 * abs(q), 1.5 * abs(q)
    grid = np.linspace(lo, hi, 25)
    vals = [solve_at_x(q, r)[1] - X for r in grid]
    found = None
    for i in range(len(grid) - 1):
        if np.sign(vals[i]) != np.sign(vals[i + 1]) and abs(vals[i] - vals[i + 1]) < 0.1:
            found = brentq(lambda r: solve_at_x(q, r)[1] - X, grid[i], grid[i + 1], xtol=1e-14)
            break
    if found:
        p, oI, oR, g, e = solve_at_x(q, found)
        print(f"  q = {q:8.4f}: r*/|q| = {found/abs(q):.8f}, off_Re = {oR:.6f} ({(oR-XNU)/SXNU:+.2f} sigma), global {g}")
    else:
        print(f"  q = {q:8.4f}: kein r* in [{lo:.4g}, {hi:.4g}]")
print("  Expliziter Zusatz eps*c nur im Im-Sektor bei r = 2/3 |q|, q = -0,0852:")
r23 = 2 / 3 * abs(Q0)
eg = np.linspace(-0.01, 0.01, 41)
ev = [solve_at_x(Q0, r23, e_)[1] - X for e_ in eg]
for i in range(len(eg) - 1):
    if np.sign(ev[i]) != np.sign(ev[i + 1]) and abs(ev[i] - ev[i + 1]) < 0.1:
        es = brentq(lambda e_: solve_at_x(Q0, r23, e_)[1] - X, eg[i], eg[i + 1], xtol=1e-15)
        p, oI, oR, g, e = solve_at_x(Q0, r23, es)
        print(f"    eps* = {es:+.4e}  (|eps*|/alpha = {abs(es)*137.036:.3e}), off_Re = {oR:.6f}, global {g}")

print("\n" + "=" * 96)
v = "TRAEGT" if okB2 else ("TRAEGT TEILWEISE" if okB1 else "WIDERLEGT")
print(f"H232 Gesamturteil: {v}   (B1 {okB1}, B2 {okB2})")
