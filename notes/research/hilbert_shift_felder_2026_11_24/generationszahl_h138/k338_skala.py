"""k338 (H155): Skala als Setzung. Macht sie U' schwer, legt sie K = 2/3 und delta fest?

Vorab-Notiz: Vorab_Notiz_H155_Skala_als_Setzung.md (Commit 9d6b6ca).
Aufruf: python -W ignore k338_skala.py > k338_out.txt
V = muA A + muB B + lA A^2 + ka A B + lB B^2 + zeta N(W) + s N(W)^2/Lam^2, A = phi^2, B = |y|^2, c_k = phi/sqrt3 + sqrt(2/3) y.f_k.
"""
import itertools
import numpy as np
import sympy as sp
from scipy.integrate import solve_ivp
from scipy.optimize import minimize, brentq

ph, y1, y2 = sp.symbols("phi y1 y2", real=True)
mA, mB, lA, ka, lB, ze = sp.symbols("mA mB lA ka lB zeta", real=True)
ck = [ph / sp.sqrt(3) + sp.sqrt(sp.Rational(2, 3)) * (y1 * sp.cos(2 * sp.pi * k / 3) + y2 * sp.sin(2 * sp.pi * k / 3)) for k in range(3)]
NW = sp.expand(ck[0] * ck[1] * ck[2])
print("=== Vorbereitung: N(W) in (phi, y) ===")
print("   N(W) =", sp.nsimplify(NW), " = phi^3/(3 sqrt3) - phi B/(2 sqrt3) + C3/(3 sqrt6)?",
      sp.simplify(NW - (ph**3 / (3 * sp.sqrt(3)) - ph * (y1**2 + y2**2) / (2 * sp.sqrt(3)) + (y1**3 - 3 * y1 * y2**2) / (3 * sp.sqrt(6)))) == 0)
t, d = sp.symbols("theta delta", real=True)
Nsph = sp.simplify(NW.subs({ph: sp.cos(t), y1: sp.sin(t) * sp.cos(d), y2: sp.sin(t) * sp.sin(d)}))
print("   auf theta = pi/4:", sp.simplify(sp.expand_trig(Nsph.subs(t, sp.pi / 4)) - (2 * sp.cos(3 * d) - sp.sqrt(2)) / (24 * sp.sqrt(3))), "(Nullrest gegen H149d)")
J = {ph: y1, y1: ph}
print("   Tausch phi <-> y1 bei y2 = 0: N - J(N) =", sp.factor(sp.expand(NW.subs(y2, 0) - NW.subs(y2, 0).subs(J, simultaneous=True))), "(ungleich 0: N(W) bricht den Tausch)")

A = ph**2; B = y1**2 + y2**2
V4 = mA * A + mB * B + lA * A**2 + ka * A * B + lB * B**2
print("\n=== H155a: Baumgraph mit Skala, tauschsymmetrisch ===")
a_, b_ = sp.symbols("a b", positive=True)
lam, kk, mu2 = sp.symbols("lam k mu2", real=True)
sol = sp.solve([mu2 + 2 * lam * a_ + kk * b_, mu2 + kk * a_ + 2 * lam * b_], [a_, b_], dict=True)
print("   Stationaer (A, B) =", sol, "-> A = B, tan^2 theta = 1, K = 2/3; positiv nur fuer mu2 < 0 und 2 lam + k > 0")
Hs = sp.hessian(V4.subs({mA: mu2, mB: mu2, lA: lam, lB: lam, ka: kk}), [ph, y1, y2])
r0 = -mu2 / (2 * lam + kk)
Hm = sp.simplify(Hs.subs({ph: sp.sqrt(r0), y1: sp.sqrt(r0), y2: 0}))
print("   Hessesche am Minimum:", Hm.tolist())
print("   Eigenwerte:", [sp.simplify(e) for e in Hm.eigenvals()], "-> U' (y2) Goldstone, Krummung theta-Mode ~ (2 lam - k): Minimum nur fuer -2 lam < k < 2 lam")

def readK(p, u, w):
    c = np.array([p / np.sqrt(3) + np.sqrt(2 / 3) * (u * np.cos(2 * np.pi * k / 3) + w * np.sin(2 * np.pi * k / 3)) for k in range(3)])
    return np.sum(c**2) / np.sum(c)**2
print("\n=== H155b: U' schwer machen mit zeta N(W) ===")
Vfull = V4 + ze * NW
fV = sp.lambdify([[ph, y1, y2], mA, mB, lA, ka, lB, ze], Vfull, "numpy")
fH = sp.lambdify([[ph, y1, y2], mA, mB, lA, ka, lB, ze], sp.hessian(Vfull, [ph, y1, y2]), "numpy")
hits = 0; lin = []
for kv, zv in itertools.product([-0.2, 0.2], [-0.3, -0.1, -0.01, -0.001, 0.001, 0.01, 0.1, 0.3]):
    best = None
    for s0 in itertools.product([1.5, -1.5], [1.5, -1.5], [0.0, 1.0, -1.0]):
        r = minimize(lambda x: fV(x, -1, -1, 0.2, kv, 0.2, zv), np.array(s0), method="BFGS", options={"gtol": 1e-13})
        if best is None or r.fun < best.fun:
            best = r
    x = best.x; K = readK(*x); H = np.array(fH(x, -1, -1, 0.2, kv, 0.2, zv), dtype=float)
    dl = np.arctan2(x[2], x[1]); e = np.array([0, -np.sin(dl), np.cos(dl)]); mU = e @ H @ e
    dK = K - 2 / 3; ok = mU >= 1 and abs(dK) < 1.5e-5; hits += ok
    lin.append((kv, zv, mU, dK))
    print(f"   k = {kv:+.1f}, zeta = {zv:+.3f}: (phi, y1, y2) = {np.round(x, 6).tolist()}, K - 2/3 = {dK:+.3e}, m^2_U'/|mu^2| = {mU:+.5f}, Eigenwerte {np.round(np.linalg.eigvalsh(H), 5).tolist()}")
print(f"   Punkte mit m^2_U' >= |mu^2| und |K - 2/3| < 1,5e-5: {hits}")
for kv in (-0.2, 0.2):
    sm = [(m, dk) for k_, z_, m, dk in lin if k_ == kv and abs(z_) <= 0.01]
    print(f"   k = {kv:+.1f}, |zeta| <= 0,01: Verhaeltnis (K - 2/3)/m^2_U' =", np.round([dk / m if m != 0 else np.nan for m, dk in sm], 5).tolist())

print("\n=== H155c: Entkopplung im Fluss (Fenster mit n_B = 2) ===")
def betas(nB):
    ys = sp.symbols(f"u0:{nB}", real=True); Bf = sum(v**2 for v in ys); Af = ph**2
    Vf = mA * Af + mB * Bf + lA * Af**2 + ka * Af * Bf + lB * Bf**2
    H = sp.hessian(Vf, [ph] + list(ys)); rhs = sp.expand(sp.Rational(1, 2) * (H * H).trace())
    cs = sp.symbols("q0:6"); basis = [1, Af, Bf, Af**2, Af * Bf, Bf**2]
    so = sp.solve(sp.Poly(sp.expand(rhs - sum(c * b for c, b in zip(cs, basis))), ph, *ys).coeffs(), cs, dict=True)[0]
    return [sp.factor(so[c]) for c in cs[1:]]
B2 = betas(2); B1 = betas(1)
print("   16 pi^2 beta (muA, muB, lA, ka, lB), n_B = 2:", B2)
print("   16 pi^2 beta, n_B = 1:", B1)
f2 = sp.lambdify([[mA, mB, lA, ka, lB]], [-q / (16 * sp.pi**2) for q in B2], "numpy")
f1 = sp.lambdify([[mA, mB, lA, ka, lB]], [-q / (16 * sp.pi**2) for q in B1], "numpy")
def Kmin(g):
    a, b = np.linalg.solve([[2 * g[2], g[3]], [g[3], 2 * g[4]]], [-g[0], -g[1]])
    return (a + b) / (3 * a) if a > 0 and b > 0 else np.nan
def run(g0, L, L2=0.0):
    g = solve_ivp(lambda t, y: f2(y), (0, L), g0, rtol=1e-12, atol=1e-15).y[:, -1] if L > 0 else np.array(g0, float)
    if L2 > 0:
        g = solve_ivp(lambda t, y: f1(y), (0, L2), g, rtol=1e-12, atol=1e-15).y[:, -1]
    return Kmin(g)
wins = {"ln(382/246,22)": np.log(382 / 246.22), "ln(246,22/91,19)": np.log(246.22 / 91.1876), "ln(91,19/9,78)": np.log(91.1876 / 9.78), "ln(246,22/9,78)": np.log(246.22 / 9.78)}
miss = 0; tot = 0
for L_, kr in itertools.product([0.05, 0.1, 0.2], [-1.0, -0.5, 0.5, 1.0]):
    g0 = [-1.0, -1.0, L_, kr * L_, L_]
    out = {n: run(g0, w) - 2 / 3 for n, w in wins.items()}
    tot += len(out); miss += sum(not (abs(v) < 1.5e-5) for v in out.values())
    fL = lambda L: (abs(run(g0, L) - 2 / 3) if np.isfinite(run(g0, L)) else 1.0) - 1.5e-5
    Lg = np.logspace(-3, 2.5, 120); i1 = next((i for i, L in enumerate(Lg) if fL(L) >= 0), None)
    Lmax = brentq(fL, Lg[i1 - 1], Lg[i1]) if i1 else np.inf
    print(f"   lam = {L_}, k/lam = {kr:+.1f}: K - 2/3 = " + ", ".join(f"{n}: {v:+.2e}" for n, v in out.items()) + f"; Fenster 0: {run(g0, 0) - 2 / 3:+.1e}; L_max = {Lmax:.2e} (Faktor {np.exp(Lmax):.6f})")
print(f"   verfehlt (|K - 2/3| >= 1,5e-5): {miss}/{tot}")
# nachtraeglich: erste Ordnung im Fenster verschwindet exakt
Lsym, mu = sp.symbols("L mu2", real=True)
gsym = [mu, mu, lam, kk, lam]
sub = dict(zip([mA, mB, lA, ka, lB], gsym))
dg = [-(q.subs(sub)) / (16 * sp.pi**2) for q in B2]
a0 = -mu / (2 * lam + kk)
# linearisierte Minimumsbedingung: (dmA - dmB) + 2 (dlA a0 - dlB a0) + (2 lam - k)(A - B) = 0 (dka wirkt symmetrisch)
first = sp.simplify((dg[0] - dg[1]) + 2 * a0 * (dg[2] - dg[4]))
print("   (nachtraeglich) erste Ordnung in L: d(muA - muB) + 2 A0 d(lA - lB) =", first, "-> dK/dL bei L = 0 verschwindet exakt")
g0 = [-1.0, -1.0, 0.1, -0.05, 0.1]
print(f"   Nachlauf mit n_B = 1 (L2 = 2) nach Fenster ln(246,22/91,19): K - 2/3 = {run(g0, wins['ln(246,22/91,19)'], 2.0) - 2 / 3:+.3e} (ohne Nachlauf {run(g0, wins['ln(246,22/91,19)']) - 2 / 3:+.3e})")
print(f"   nur n_B = 1 ab symmetrischem Start (L2 = 5): K - 2/3 = {Kmin(solve_ivp(lambda t, y: f1(y), (0, 5), g0, rtol=1e-12, atol=1e-15).y[:, -1]) - 2 / 3:+.1e}")

print("\n=== H155d: delta mit Term sechster Ordnung ===")
Rs = sp.symbols("R", real=True)
cos3 = (sp.sqrt(2) - 12 * sp.sqrt(3) * Rs) / 2
Rstar = sp.solve(sp.Eq(cos3, sp.cos(sp.Rational(2, 3))), Rs)[0]
print("   Minimum von zeta N + N^2/Lam^2 auf theta = pi/4: cos 3 delta =", cos3, "; delta = 2/9 bei R* =", Rstar, "=", float(Rstar))
print("   innere Minima (drei verschiedene Massen) fuer R in", [float(sp.solve(sp.Eq(cos3, s_), Rs)[0]) for s_ in (1, -1)], "; mit negativem N^2-Koeffizienten: Maximum, delta bleibt 0 oder pi/3")
Rst = float(Rstar)
sc = {"Sum m_l": 1.88310, "m_tau": 1.77693, "9,78": 9.78, "m_Z": 91.1876, "m_h": 125.2, "v": 246.22, "382": 382.0}
vals = []
for (n1, z), (n2, Lm), vn, sg in itertools.product(sc.items(), sc.items(), [("v", 246.22), ("Sum m_l", 1.88310)], [1, -1]):
    vals.append((n1, n2, vn[0], sg, sg * z * Lm**2 / vn[1]**3))
R = np.array([v[-1] for v in vals]); hit = [v for v in vals if abs(v[-1] / Rst - 1) < 0.01]
same = R[R * Rst > 0]; width = np.log(np.abs(same).max() / np.abs(same).min())
print(f"   {len(vals)} Kombinationen; Treffer innerhalb 1 %: {len(hit)} {hit}")
print(f"   Zufallserwartung (log-gleichverteilt ueber {width:.1f} e-Folgen, {len(same)} mit passendem Vorzeichen): {len(same) * 0.02 / width:.2f}")
near = sorted(vals, key=lambda v: abs(np.log(abs(v[-1] / Rst))) if v[-1] * Rst > 0 else 1e9)[:3]
print("   naechste:", [(a, b, c, round(e / Rst - 1, 4)) for a, b, c, s_, e in near])
# delta, das die naechsten Kombinationen ergeben, gegen delta aus den drei Massen (H149: 0,222225 +- 0,000006)
for a, b, c, s_, e in near:
    dlt = np.arccos(np.sqrt(2) / 2 - 6 * np.sqrt(3) * e) / 3
    print(f"   {a}, {b}, {c}: delta = {dlt:.6f}, Abstand zu 0,222225: {(dlt - 0.222225) / 6e-6:+.0f} sigma")

print("\n=== Nachtraeglich (Erkundung, nicht in der Vorab-Notiz): K und delta gemeinsam, wenn zeta N + N^2/Lam^2 delta = 2/9 einstellt ===")
# v = 1, Lam = v, zeta = R* (genau der Fit-Wert); mu^2 so, dass |Psi| = 1 ohne zeta
Vf6 = V4 + ze * NW + NW**2
fV6 = sp.lambdify([[ph, y1, y2], mA, mB, lA, ka, lB, ze], Vf6, "numpy")
def readKd(x):
    p, u, w = x; c = np.array([p / np.sqrt(3) + np.sqrt(2 / 3) * (u * np.cos(2 * np.pi * k / 3) + w * np.sin(2 * np.pi * k / 3)) for k in range(3)])
    sg = np.sign(c.sum())
    if sg < 0: c = -c
    z = sum(c[k] * np.exp(-2j * np.pi * k / 3) for k in range(3)) * 2 / 3
    dd = np.angle(z) % (2 * np.pi / 3); dd = min(dd, 2 * np.pi / 3 - dd)
    return np.sum(c**2) / np.sum(c)**2, dd, sg
for lv, kr in itertools.product([0.1, 0.5, 2.0], [-1.0, 1.0]):
    kv = kr * lv; m2 = -(2 * lv + kv) / 2
    res = []
    for s0 in itertools.product([0.7, -0.7], np.linspace(0, 2 * np.pi, 12, endpoint=False)):
        x0 = np.array([s0[0], 0.7 * np.cos(s0[1]), 0.7 * np.sin(s0[1])])
        r = minimize(lambda x: fV6(x, m2, m2, lv, kv, lv, Rst), x0, method="BFGS", options={"gtol": 1e-14}); res.append((r.fun, r.x))
    fmin = min(f for f, _ in res); sols = {}
    for f, x in res:
        if f - fmin < 1e-12:
            Kv, dv, sg = readKd(x); sols[(round(dv, 5), int(sg))] = Kv
    print(f"   lam = {lv}, k/lam = {kr:+.0f}: entartete Minima (delta, Vorzeichen Summe c): " + "; ".join(f"delta = {d_:.5f}, {'+' if s_ > 0 else '-'}: K - 2/3 = {k_ - 2 / 3:+.1e}" for (d_, s_), k_ in sorted(sols.items())))
print("   delta zum zweiten Zweig (Summe c < 0, N -> -N): arccos(sqrt2 - cos(2/3))/3 =", np.arccos(np.sqrt(2) - np.cos(2 / 3)) / 3)
