"""k440 (Test H226): Welcher tauschbrechende Term legt den Modulus phi auf den Messwert x?
Vorab-Notiz Vorab_H226_Tauschbruch_phi.md (vor der Rechnung committet). Modell wie H225/k439.
Aufruf aus diesem Ordner: python3 k440_test_h226.py > k440_out.txt
"""
import numpy as np
from scipy.optimize import minimize_scalar, brentq

DSTAR = 0.2222220470731
X = np.pi / 12 - DSTAR
XNU, SXNU = 0.04336, 0.00213
BS, GL = 0.5494056410, 1.8646997646
GM = 0.2375329580
DG = np.linspace(0, 2 * np.pi, 2001)


def fold(d):
    d = d % (2 * np.pi / 3)
    return min(d, 2 * np.pi / 3 - d)


def vmin(f):
    v = f(DG)
    best = (np.inf, None)
    for k in np.argsort(v)[:8]:
        r = minimize_scalar(f, bounds=(DG[max(k - 1, 0)], DG[min(k + 1, 2000)]), method="bounded", options={"xatol": 1e-13})
        if r.fun < best[0]:
            best = (r.fun, r.x)
    return best


def sectors(phi, q, aI=0.0, aR=0.0, lam=1.0, kap=1.0):
    fI = lambda d: -np.cos(2 * (d - np.pi / 4 - phi)) + aI * np.cos(2 * d) + q * np.cos(3 * d)
    fR = lambda d: kap * np.cos(2 * (d - phi)) + aR * np.cos(2 * d) + lam * q * np.cos(3 * d)
    return vmin(fI), vmin(fR)


def E(phi, q, **k):
    (eI, _), (eR, _) = sectors(phi, q, **k)
    return eI + eR


def global_min(q, n=360, **k):
    ph = np.linspace(-np.pi / 2, np.pi / 2, n, endpoint=False)
    e = np.array([E(p, q, **k) for p in ph])
    i = int(np.argmin(e)); h = np.pi / n
    r = minimize_scalar(lambda p: E(p, q, **k), bounds=(ph[i] - h, ph[i] + h), method="bounded", options={"xatol": 1e-12})
    return r.x, r.fun, ph, e


def dE(phi, q, h=1e-6, **k):
    return (E(phi + h, q, **k) - E(phi - h, q, **k)) / (2 * h)


TERMS = {
    "T1 c*alpha cos2d (nur Im)": lambda c: dict(aI=c),
    "T2 q_Re = lam q": lambda c: dict(lam=c),
    "T3 |alpha'_Re| = kap": lambda c: dict(kap=c),
    "T4 alpha cos2d beide (Kontrolle)": lambda c: dict(aI=c, aR=c),
}
FRAME = {"H167 -0,931": 0.0793204104 / -0.0852, "1": 1, "-1": -1, "sqrt2": np.sqrt(2), "-sqrt2": -np.sqrt(2), "1/sqrt2": 2 ** -0.5,
         "-1/sqrt2": -2 ** -0.5, "2": 2, "-2": -2, "1/2": 0.5, "-1/2": -0.5, "3": 3, "-3": -3, "beta_sym": BS, "-beta_sym": -BS,
         "gamma_L": GL, "-gamma_L": -GL, "1/gamma_L": 1 / GL, "-1/gamma_L": -1 / GL, "gamma_M": GM, "-gamma_M": -GM}

print("=" * 92)
print("H226 Kontrolle: ohne Term (H225) globales Minimum bei pi/8")
print("=" * 92)
p0, e0, _, _ = global_min(-1e-4)
print(f"  q=-1e-4: phi* = {p0:.7f} (mod pi/3: {p0 % (np.pi/3):.7f}; pi/8 = {np.pi/8:.7f})")

print("\n" + "=" * 92)
print("H226 A  Grenzfall q = -1e-4: Verhaeltnis (Koeffizient/|q| bei T1, T4; lam, kap direkt), das phi = x stationaer macht; Globalitaet")
print("=" * 92)
q = -1e-4
resA = {}
for name, mk in TERMS.items():
    scale = abs(q) if name.startswith(("T1", "T4")) else 1.0
    grid = np.concatenate([-np.logspace(-2, 1.5, 120)[::-1], np.logspace(-2, 1.5, 120)]) if scale != 1.0 else np.logspace(-2, 1.5, 200)
    vals = [dE(X, q, **mk(r * scale)) for r in grid]
    roots = []
    for i in range(len(grid) - 1):
        if np.sign(vals[i]) != np.sign(vals[i + 1]) and np.isfinite(vals[i]) and np.isfinite(vals[i + 1]):
            try:
                roots.append(brentq(lambda r: dE(X, q, **mk(r * scale)), grid[i], grid[i + 1], xtol=1e-10))
            except ValueError:
                pass
    print(f"  {name}: Nullstellen der Steigung bei phi = x: {[round(r, 6) for r in roots] if roots else 'keine'}")
    resA[name] = []
    for r in roots:
        pg, eg, _, _ = global_min(q, **mk(r * scale))
        glob = abs(((pg - X + np.pi / 2) % np.pi) - np.pi / 2) < 1e-4
        curv = (E(X + 1e-4, q, **mk(r * scale)) - 2 * E(X, q, **mk(r * scale)) + E(X - 1e-4, q, **mk(r * scale))) / 1e-8
        near = sorted(FRAME.items(), key=lambda kv: abs(kv[1] - r))[0]
        match = abs(near[1] - r) / abs(r) < 0.02
        resA[name].append((r, glob, match))
        print(f"     Verhaeltnis {r:+.6f}: Kruemmung {curv:+.3e}, globales Minimum bei {pg:+.7f} -> phi = x global: {glob};"
              f" naechste Rahmenzahl {near[0]} = {near[1]:+.5f} ({(r/near[1]-1)*100:+.1f} %) -> Treffer: {match}")

print("\n" + "=" * 92)
print("H226 B  endliche Kopplung q = -0,0852: Koeffizient so, dass delta_Im = delta* am globalen Modulus-Minimum; Vorhersage x_nu")
print("=" * 92)
q = -0.0852
resB = {}
for name, mk in TERMS.items():
    grid = np.linspace(-1, 1, 81) if name.startswith(("T1", "T4")) else np.linspace(0.05, 3, 60)
    rows = []
    for c in grid:
        pg, eg, _, _ = global_min(q, n=240, **mk(c))
        (eI, dI), (eR, dR) = sectors(pg, q, **mk(c))
        rows.append((c, pg, fold(dI), fold(dR)))
    f = [r[2] - DSTAR for r in rows]
    sols = []
    for i in range(len(rows) - 1):
        if np.sign(f[i]) != np.sign(f[i + 1]) and abs(f[i] - f[i + 1]) < 0.05:
            def g(c):
                pg, _, _, _ = global_min(q, n=240, **mk(c))
                return fold(sectors(pg, q, **mk(c))[0][1]) - DSTAR
            try:
                c0 = brentq(g, rows[i][0], rows[i + 1][0], xtol=1e-9)
            except ValueError:
                continue
            pg, _, _, _ = global_min(q, n=240, **mk(c0))
            (eI, dI), (eR, dR) = sectors(pg, q, **mk(c0))
            xnu = np.pi / 6 - fold(dR)
            sols.append((c0, pg, fold(dI), fold(dR), xnu))
    resB[name] = sols
    print(f"  {name}: delta_Im ueber dem Gitter von {min(r[2] for r in rows):.4f} bis {max(r[2] for r in rows):.4f} (Ziel {DSTAR:.4f})")
    if not sols:
        print("     keine Loesung mit natuerlicher Groesse")
    for c0, pg, dI, dR, xnu in sols:
        print(f"     Koeffizient {c0:+.6f}: phi* = {pg:+.6f}, delta_Im = {dI:.7f}, delta_Re = {dR:.6f} -> x_nu,pred = {xnu:+.5f}"
              f" ({(xnu-XNU)/SXNU:+.1f} sigma) -> {'innerhalb 2 sigma' if abs(xnu-XNU) < 2*SXNU else 'ausserhalb'}")

print("\n" + "=" * 92)
print("H226 Gesamturteil (T4 ist Kontrolle)")
print("=" * 92)
best = "WIDERLEGT"
for name in list(TERMS)[:3]:
    okB = any(abs(s[4] - XNU) < 2 * SXNU for s in resB[name])
    okA = any(g and m for r, g, m in resA[name])
    anyglobA = any(g for r, g, m in resA[name])
    print(f"  {name}: A global bei x: {anyglobA}, A Rahmenzahl: {okA}, B innerhalb 2 sigma: {okB}")
    if okB and okA:
        best = "TRAEGT"
    elif okB and best != "TRAEGT":
        best = "TRAEGT TEILWEISE"
print("  ->", best)
