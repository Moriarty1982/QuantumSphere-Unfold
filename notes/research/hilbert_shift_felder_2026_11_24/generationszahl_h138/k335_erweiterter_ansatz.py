"""k335 (H152): skalenfreier Ansatz mit allen Z3-invarianten Viertordnungs-Termen und HS(3)-Rueckwirkung.

Vorab-Notiz: Vorab_Notiz_H152_Erweiterter_Ansatz.md (Commit c76928c).
Aufruf: python k335_erweiterter_ansatz.py > k335_out.txt  (einige Minuten).
Felder: phi (HS(0)-Einheit), y1, y2 (Kopien-Ebene), C (4 Komponenten). Vorzeichen werden nicht gesetzt.
"""
import itertools
import numpy as np
import sympy as sp
from scipy.integrate import solve_ivp
from scipy.optimize import minimize, brentq

ph, y1, y2 = sp.symbols("phi y1 y2", real=True)
Cs = sp.symbols("C0:4", real=True)
fields = [ph, y1, y2] + list(Cs)
B = y1**2 + y2**2; Q = sum(c**2 for c in Cs); C3 = y1**3 - 3 * y1 * y2**2
basis = [ph**4, ph**2 * B, B**2, ph * C3, ph**2 * Q, B * Q, Q**2]
names = ["lA", "ka", "lB", "xi", "kC", "kBC", "lC"]
g = sp.symbols(" ".join(names), real=True)

print("=== H152a: Vollstaendigkeit der Invarianten und Schliessen der beta-Funktionen ===")
# Reynolds-Operator der Gruppe Z3 x| Z2 auf (y1, y2), phi fest
R = sp.Matrix([[sp.Rational(-1, 2), -sp.sqrt(3) / 2], [sp.sqrt(3) / 2, sp.Rational(-1, 2)]]); S = sp.Matrix([[1, 0], [0, -1]])
group = [sp.eye(2), R, R * R, S, R * S, R * R * S]
mons = [ph**a * y1**b * y2**c for a in range(5) for b in range(5) for c in range(5) if a + b + c == 4]
avgs = []
for m in mons:
    tot = 0
    for G in group:
        v = G * sp.Matrix([y1, y2]); tot += m.subs({y1: v[0], y2: v[1]}, simultaneous=True)
    avgs.append(sp.expand(tot / 6))
allm = sorted({mm for a in avgs for mm in sp.Poly(a, ph, y1, y2).monoms()})
M = sp.Matrix([[sp.Poly(a, ph, y1, y2).coeff_monomial(ph**e[0] * y1**e[1] * y2**e[2]) for e in allm] for a in avgs])
print("   Dimension der Z3xZ2-invarianten Quartiken in (phi, y):", M.rank(), "(erwartet 4: phi^4, phi^2 B, B^2, phi C3)")
Mb = sp.Matrix([[sp.Poly(b, ph, y1, y2).coeff_monomial(ph**e[0] * y1**e[1] * y2**e[2]) for e in allm] for b in basis[:4]])
print("   Rang der Basis {phi^4, phi^2 B, B^2, phi C3}:", Mb.rank(), "; zusammen mit allen Mitteln:", Mb.col_join(M).rank())
V = sum(gi * b for gi, b in zip(g, basis))
H = sp.hessian(V, fields)
rhs = sp.expand(sp.Rational(1, 2) * (H * H).trace())
bs_ = sp.symbols("b0:7")
res = sp.Poly(sp.expand(rhs - sum(b * bb for b, bb in zip(bs_, basis))), *fields)
sol = sp.solve(res.coeffs(), bs_, dict=True)
print("   1/2 Tr(d^2V)^2 liegt in der Basis (Nullrest):", len(sol) == 1 and sp.expand((rhs - sum(sol[0][b] * bb for b, bb in zip(bs_, basis)))) == 0)
beta = [sp.factor(sol[0][b]) for b in bs_]
for n, b in zip(names, beta):
    print(f"   16 pi^2 beta_{n} = {b}")
fb = sp.lambdify([g], [-b for b in beta], "numpy")   # ins Infrarote

# Kugel-Minimum: phi = cos a, y = sin a cos b (cos d, sin d), |C| = sin a sin b
A_, B_, D_ = np.meshgrid(np.linspace(0, np.pi, 41), np.linspace(0, np.pi / 2, 21), np.linspace(0, 2 * np.pi, 48, endpoint=False), indexing="ij")
def comps(a, b, d):
    p = np.cos(a); r = np.sin(a) * np.cos(b); c = np.sin(a) * np.sin(b)
    return p, r * np.cos(d), r * np.sin(d), c
def Vnum(gv, p, u, w, c):
    Bv = u**2 + w**2; Qv = c**2
    return gv[0] * p**4 + gv[1] * p**2 * Bv + gv[2] * Bv**2 + gv[3] * p * (u**3 - 3 * u * w**2) + gv[4] * p**2 * Qv + gv[5] * Bv * Qv + gv[6] * Qv**2
PG = comps(A_, B_, D_)
def sphere_min(gv):
    vals = Vnum(gv, *PG); i = np.unravel_index(np.argmin(vals), vals.shape)
    x0 = np.array([A_[i], B_[i], D_[i]])
    r = minimize(lambda x: Vnum(gv, *comps(*x)), x0, method="Nelder-Mead", options={"xatol": 1e-12, "fatol": 1e-16, "maxiter": 4000})
    return r.fun, r.x

def readout(x):
    p, u, w, c = comps(*x)
    n = np.sqrt(p**2 + u**2 + w**2); p, u, w = p / n, u / n, w / n
    ck = np.array([p / np.sqrt(3) + np.sqrt(2 / 3) * (u * np.cos(2 * np.pi * k / 3) + w * np.sin(2 * np.pi * k / 3)) for k in range(3)])
    K = np.sum(ck**2) / np.sum(ck)**2
    z = sum(ck[k] * np.exp(-2j * np.pi * k / 3) for k in range(3)) * 2 / 3
    d = np.angle(z) % (2 * np.pi / 3); d = min(d, 2 * np.pi / 3 - d)
    m = np.sort(ck**2)
    theta = np.arctan2(np.sqrt(u**2 + w**2), abs(p))
    return K, d, m, theta, c

def grid_min(gv):
    return np.min(Vnum(gv, *PG))
def run(g0, tmax=50.0):
    # Integration stoppt, sobald eine Diagonalkopplung negativ wird (dann ist V sicher schon instabil geworden)
    stop = lambda t, y: min(y[0], y[2], y[6]) + 1e-9; stop.terminal = True; stop.direction = -1
    s = solve_ivp(lambda t, y: fb(y), (0, tmax), g0, method="LSODA", rtol=1e-10, atol=1e-13, dense_output=True, events=stop)
    ts = np.concatenate([[0], np.logspace(-4, np.log10(s.t[-1]), 150)])
    prev = sphere_min(g0)[0]
    if prev <= 0:
        return "schon instabil", None, None
    f = lambda t: sphere_min(s.sol(t))[0]
    for i1 in range(1, len(ts)):
        if grid_min(s.sol(ts[i1])) <= 0:
            i0 = i1 - 1
            while i0 > 0 and f(ts[i0]) <= 0:
                i0 -= 1
            tg = brentq(f, ts[i0], ts[i1], xtol=1e-12)
            gv = s.sol(tg); x = sphere_min(gv)[1]
            return "GW", tg, (gv, x)
        if not np.all(np.isfinite(s.sol(ts[i1]))):
            break
    return "keine Skala", None, None

print("\n=== H152b-e: Gitter ===")
lam_l = [0.1, 0.2, 0.3]; k_l = [-1.5, -1.0, -0.5, -0.2]; xi_l = [-0.4, -0.2, -0.1, 0.1, 0.2, 0.4]; kc_l = [0.0, 0.2]
rows = []
for lam, kr, xr, kc in itertools.product(lam_l, k_l, xi_l, kc_l):
    g0 = np.array([lam, kr * lam, lam, xr * lam, kc, 0.0, 0.2])
    st, tg, data = run(g0)
    if st != "GW":
        rows.append((lam, kr, xr, kc, st)); continue
    gv, x = data
    K, d, m, th, c = readout(x)
    rows.append((lam, kr, xr, kc, st, tg, K, d, m, th, c))
gw = [r for r in rows if r[4] == "GW"]
print(f"   {len(rows)} Startpunkte: GW {len(gw)}, sonst", {s_: sum(1 for r in rows if r[4] == s_) for s_ in set(r[4] for r in rows) if s_ != "GW"})
for r in gw[:12]:
    lam, kr, xr, kc, st, tg, K, d, m, th, c = r
    print(f"   lam={lam} k/l={kr:+.1f} xi/l={xr:+.1f} kC={kc}: tau={tg:.4f} K={K:.6f} delta={d:.5f} theta-pi/4={th - np.pi / 4:+.5f} |C|={c:.3f} m/m3={np.round(m / m[-1], 5)}")
Ks = np.array([r[6] for r in gw]); ds = np.array([r[7] for r in gw]); ths = np.array([r[9] for r in gw]); cs = np.array([r[10] for r in gw])
distinct = np.array([np.min(np.diff(r[8])) > 1e-3 * r[8][-1] for r in gw])
print(f"\n   H152b: K ueber das Gitter: min {Ks.min():.6f}, max {Ks.max():.6f}, Streuung (Std) {Ks.std():.2e} -> {'fester Punkt' if Ks.std() < 1e-3 else 'startabhaengig'}")
print(f"   H152c: drei verschiedene Massen: {distinct.sum()}/{len(gw)}; davon delta in 1 % von 2/9: {np.sum(distinct & (np.abs(ds / (2 / 9) - 1) < 0.01))}")
print(f"          reduzierte delta (gerundet) und Haeufigkeit:", {k_: int(v) for k_, v in zip(*np.unique(np.round(ds, 3), return_counts=True))})
print(f"   H152d: K innerhalb 3 sigma von 0,666661: {np.sum(np.abs(Ks - 0.666661) < 2.1e-5)}/{len(gw)}; 2/3 im Bereich [min, max]: {Ks.min() <= 2 / 3 <= Ks.max()}")
print(f"   H152e: |theta - pi/4| < 0,01: {np.sum(np.abs(ths - np.pi / 4) < 0.01)}/{len(gw)}; theta - pi/4 von {np.min(ths - np.pi / 4):+.4f} bis {np.max(ths - np.pi / 4):+.4f}")
print(f"   Anteil des Kondensats in C (|C| > 0,01): {np.sum(cs > 0.01)}/{len(gw)}")
# Kontrolle: xi -> 0 gibt H150 zurueck
g0 = np.array([0.2, -0.2, 0.2, 0.0, 0.0, 0.0, 0.2]); st, tg, data = run(g0)
print(f"\n   Kontrolle xi = 0, kC = 0 (H150d-Start 0.2, -0.2, 0.2): {st}, tau = {tg:.6f}, K = {readout(data[1])[0]:.6f} (H150/H151: tau 0.134145, K 0.671941)")
