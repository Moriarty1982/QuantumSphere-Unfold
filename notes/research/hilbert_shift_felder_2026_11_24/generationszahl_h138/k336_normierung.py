"""k336 (H153): algebraisch begruendete 1:2-Normierungen N1-N4 im skalenfreien Fluss.

Vorab-Notiz: Vorab_Notiz_H153_Normierung_1_zu_2.md (Commit fd4c7f3).
Aufruf: python -W ignore k336_normierung.py > k336_out.txt
Konvention: V = lA A^2 + ka A B + lB B^2, A = phi^2, B = |y|^2 (kanonische Felder); Fluss ins Infrarote dg/dt = -beta
(Faktor 16 pi^2 in tau absorbiert, aendert K nicht). Vorzeichen werden nicht gesetzt (kappa-hat < 0 ist die Klasse aus H150).
Normierung = Umskalierung A = a*Ahat, B = b*Bhat; symmetrischer Start heisst lAhat = lBhat = lam, kahat = k:
  lA = lam/a^2, ka = k/(a b), lB = lam/b^2.
  N1 (je Komponente, n_A = 1, n_B = 2): a = 1, b = 2       -> (lam, k/2, lam/4)
  N2 (Spur der Auslesung 1/3 : 2/3):   a = 1/3, b = 2/3    -> (9 lam, 9k/2, 9 lam/4)
  N3 (dritte Kopie, (3/2) B):          a = 1, b = 2/3      -> (lam, 3k/2, 9 lam/4)
  N4 (Unteralgebra {1, U}):            n_A = n_B = 1, symmetrischer Start (lam, k, lam)
"""
import itertools
import numpy as np
import sympy as sp
from scipy.integrate import solve_ivp
from scipy.optimize import minimize, brentq

lA, ka, lB, lam, k, a, b, s = sp.symbols("lA ka lB lam k a b s", positive=True)

def beta_functions(nA, nB, wA=1, wB=1):
    """Einschleifen-beta in Feldern x (nA), y (nB); A = wA*|x|^2, B = wB*|y|^2 (w != 1: nicht kanonisch gezaehlt)."""
    x = sp.symbols(f"x0:{nA}", real=True); y = sp.symbols(f"y0:{nB}", real=True)
    A0 = sum(v**2 for v in x); B0 = sum(v**2 for v in y)
    V = lA * (wA * A0)**2 + ka * (wA * A0) * (wB * B0) + lB * (wB * B0)**2
    H = sp.hessian(V, list(x) + list(y))
    rhs = sp.expand(sp.Rational(1, 2) * (H * H).trace())
    bA, bK, bB = sp.symbols("bA bK bB")
    sol = sp.solve(sp.Poly(sp.expand(rhs - (bA * (wA * A0)**2 + bK * (wA * A0) * (wB * B0) + bB * (wB * B0)**2)), *(list(x) + list(y))).coeffs(), (bA, bK, bB), dict=True)[0]
    return [sp.factor(sol[q]) for q in (bA, bK, bB)]

print("=== H153a: Normierung als Umparametrisierung (symbolisch) ===")
b12 = beta_functions(1, 2); b11 = beta_functions(1, 1)
print("   16 pi^2 beta (1,2):", b12)
print("   16 pi^2 beta (1,1):", b11)
S = {lA: lam / a**2, ka: k / (a * b), lB: lam / b**2}
# (1) GW-Bedingung kappa + 2 sqrt(lA lB) = 0 ist homogen: in Hut-Variablen dieselbe Form
gw = (ka + 2 * sp.sqrt(lA * lB)).subs(S)
print("   (1) GW-Bedingung nach Umskalierung * a b:", sp.simplify(gw * a * b), " (= k + 2 lam: dieselbe Form in den Hut-Kopplungen)")
# (2) konjugierter Fluss: d ghat/dt = S^-1 beta(S ghat); in physikalischen Kopplungen derselbe Fluss wie H150
Kphys = (1 + sp.sqrt(lA / lB)) / 3
print("   (2) K am GW-Punkt haengt nur am physikalischen Verhaeltnis lA/lB; Start-Verhaeltnis nach Umskalierung:", sp.simplify((lA / lB).subs(S)), "=> K0 =", sp.simplify(Kphys.subs(S)))
# (3) kovariant: Fluss der physikalischen Kopplungen (Hut-Fluss konjugiert) gleich dem aus H150 -- Gegenprobe gegen 'naive' beta in Hut-Feldern
bh = [sp.expand(q.subs({lA: lam, ka: k, lB: lam})) for q in b12]          # naive: beta-Form auf Hut-Kopplungen angewandt
bc = [sp.expand(q.subs(S) * f) for q, f in zip(b12, (a**2, a * b, b**2))]  # konjugiert: S^-1 beta(S ghat)
print("   (3) konjugierter Hut-Fluss minus naiver Hut-Fluss (Null nur fuer a = b = 1):")
for n_, d_ in zip(("lA", "ka", "lB"), (sp.factor(x - y) for x, y in zip(bc, bh))):
    print(f"       {n_}: {d_}")
print("       a = b = 1:", [sp.simplify(x.subs({a: 1, b: 1}) - y) for x, y in zip(bc, bh)])
# (4) Gegenprobe: beta direkt mit Bhat = s*|y|^2 (y kanonisch, Kopplungen je Bhat) gleich dem konjugierten Fluss (b = 1/s)?
bw = beta_functions(1, 2, 1, s)
conj = [sp.expand(q.subs({lA: lA, ka: s * ka, lB: s**2 * lB}, simultaneous=True) * f) for q, f in zip(b12, (1, 1 / s, 1 / s**2))]
print("   (4) beta(Bhat = s|y|^2) minus konjugierter Fluss:", [sp.simplify(x - y) for x, y in zip(bw, conj)], "(Nullrest = kovariant)")

fb12 = sp.lambdify([[lA, ka, lB]], [-q for q in b12], "numpy")
fb11 = sp.lambdify([[lA, ka, lB]], [-q for q in b11], "numpy")

def flow(g0, fb, tmax=1e4):
    ev = lambda t, y: y[1] + 2 * np.sqrt(max(y[0] * y[2], 0.0)); ev.terminal = True; ev.direction = -1
    neg = lambda t, y: min(y[0], y[2]); neg.terminal = True; neg.direction = -1
    r = solve_ivp(lambda t, y: fb(y), (0, tmax), g0, method="LSODA", rtol=1e-12, atol=1e-15, events=[ev, neg])
    if len(r.t_events[0]):
        gv = r.y_events[0][0]; x = gv[0] / gv[2]
        return r.t_events[0][0], (1 + np.sqrt(x)) / 3, np.arctan(x**0.25), x
    return None

maps = {"N1": lambda L, K_: [L, K_ / 2, L / 4], "N2": lambda L, K_: [9 * L, 9 * K_ / 2, 9 * L / 4], "N3": lambda L, K_: [L, 3 * K_ / 2, 9 * L / 4]}
lam_l = [0.05, 0.1, 0.2, 0.3]; kr_l = [-1.9, -1.5, -1.0, -0.5, -0.2, -0.1]
print("\n=== H153b: N1-N3 im (1,2)-Fluss, Gitter 4 x 6 ===")
print("   Kontrolle H150d (Start 0.2, -0.2, 0.2, ohne Normierung):", flow([0.2, -0.2, 0.2], fb12))
summary = {}
for name, mp in maps.items():
    res = []
    for L, kr in itertools.product(lam_l, kr_l):
        out = flow(mp(L, kr * L), fb12)
        res.append((L, kr, out))
    ok = [r for r in res if r[2] is not None]
    Ks = np.array([r[2][1] for r in ok]); ths = np.array([r[2][2] for r in ok])
    print(f"\n   {name}: GW erreicht {len(ok)}/{len(res)}")
    for L, kr, out in res:
        print(f"      lam={L:<5} k/lam={kr:+.1f}: " + (f"tau={out[0]:.5f} lA/lB={out[3]:.6f} K={out[1]:.6f} theta-pi/4={out[2] - np.pi / 4:+.6f}" if out else "kein GW-Punkt"))
    hits = int(np.sum(np.abs(Ks - 0.666661) < 2.1e-5)); stab = int(np.sum(np.abs(ths - np.pi / 4) < 0.01))
    print(f"   {name}: K min {Ks.min():.6f} max {Ks.max():.6f} Mittel {Ks.mean():.6f} Std {Ks.std():.2e} -> {'startunabhaengig' if Ks.std() < 1e-3 else 'startabhaengig'};"
          f" 3sigma-Treffer {hits}/{len(ok)}; |theta - pi/4| < 0,01: {stab}/{len(ok)}")
    summary[name] = (Ks.mean(), Ks.std(), hits, stab, len(ok))
print("\n   Mittelwerte:", {n: round(v[0], 6) for n, v in summary.items()})

print("\n=== H153c: N4, (1,1)-Fluss, symmetrischer Start ===")
devs = []; thd = []
for L, kr in itertools.product(lam_l, kr_l):
    out = flow([L, kr * L, L], fb11)
    if out is None:
        print(f"   lam={L} k/lam={kr}: kein GW-Punkt"); continue
    devs.append(abs(out[1] - 2 / 3)); thd.append(abs(out[2] - np.pi / 4))
print(f"   {len(devs)}/24 mit GW-Punkt; max |K - 2/3| = {max(devs):.2e}; max |theta - pi/4| = {max(thd):.2e} -> {'bestaetigt' if max(devs) < 1e-9 else 'nicht bestaetigt'}")
print(f"   Abstand 2/3 zum Messwert 0,666661: {2 / 3 - 0.666661:.2e} (sigma 7e-6: {(2 / 3 - 0.666661) / 7e-6:.2f} sigma)")
print("   Symbolisch: beta_lA - beta_lB bei lA = lB:", sp.simplify((b11[0] - b11[2]).subs(lB, lA)), "(Tausch-Symmetrie)")

print("\n=== H153d: delta mit xi != 0 (Ansatz H152, ohne C-Kopplung) ===")
ph, y1, y2 = sp.symbols("phi y1 y2", real=True); Cs = sp.symbols("C0:4", real=True)
fields = [ph, y1, y2] + list(Cs)
Bf = y1**2 + y2**2; Qf = sum(c**2 for c in Cs); C3 = y1**3 - 3 * y1 * y2**2
basis = [ph**4, ph**2 * Bf, Bf**2, ph * C3, ph**2 * Qf, Bf * Qf, Qf**2]
g = sp.symbols("g0:7", real=True)
V = sum(gi * bb for gi, bb in zip(g, basis)); H = sp.hessian(V, fields)
rhs = sp.expand(sp.Rational(1, 2) * (H * H).trace()); bs_ = sp.symbols("b0:7")
sol = sp.solve(sp.Poly(sp.expand(rhs - sum(q * bb for q, bb in zip(bs_, basis))), *fields).coeffs(), bs_, dict=True)[0]
fb7 = sp.lambdify([g], [-sp.factor(sol[q]) for q in bs_], "numpy")
A_, B_, D_ = np.meshgrid(np.linspace(0, np.pi, 41), np.linspace(0, np.pi / 2, 21), np.linspace(0, 2 * np.pi, 48, endpoint=False), indexing="ij")
def comps(al, be, d):
    p = np.cos(al); r = np.sin(al) * np.cos(be); c = np.sin(al) * np.sin(be)
    return p, r * np.cos(d), r * np.sin(d), c
def Vnum(gv, p, u, w, c):
    Bv = u**2 + w**2; Qv = c**2
    return gv[0] * p**4 + gv[1] * p**2 * Bv + gv[2] * Bv**2 + gv[3] * p * (u**3 - 3 * u * w**2) + gv[4] * p**2 * Qv + gv[5] * Bv * Qv + gv[6] * Qv**2
PG = comps(A_, B_, D_)
def sphere_min(gv):
    vals = Vnum(gv, *PG); i = np.unravel_index(np.argmin(vals), vals.shape)
    r = minimize(lambda x: Vnum(gv, *comps(*x)), np.array([A_[i], B_[i], D_[i]]), method="Nelder-Mead", options={"xatol": 1e-12, "fatol": 1e-16, "maxiter": 4000})
    return r.fun, r.x
def readout(x):
    p, u, w, c = comps(*x); n = np.sqrt(p**2 + u**2 + w**2); p, u, w = p / n, u / n, w / n
    ck = np.array([p / np.sqrt(3) + np.sqrt(2 / 3) * (u * np.cos(2 * np.pi * j / 3) + w * np.sin(2 * np.pi * j / 3)) for j in range(3)])
    K = np.sum(ck**2) / np.sum(ck)**2
    z = sum(ck[j] * np.exp(-2j * np.pi * j / 3) for j in range(3)) * 2 / 3
    d = np.angle(z) % (2 * np.pi / 3); d = min(d, 2 * np.pi / 3 - d)
    return K, d
def run7(g0, tmax=50.0):
    stop = lambda t, y: min(y[0], y[2], y[6]) + 1e-9; stop.terminal = True; stop.direction = -1
    sv = solve_ivp(lambda t, y: fb7(y), (0, tmax), g0, method="LSODA", rtol=1e-10, atol=1e-13, dense_output=True, events=stop)
    ts = np.concatenate([[0], np.logspace(-4, np.log10(sv.t[-1]), 150)])
    if sphere_min(g0)[0] <= 0:
        return None
    f = lambda t: sphere_min(sv.sol(t))[0]
    for i1 in range(1, len(ts)):
        if np.min(Vnum(sv.sol(ts[i1]), *PG)) <= 0:
            i0 = i1 - 1
            while i0 > 0 and f(ts[i0]) <= 0:
                i0 -= 1
            tg = brentq(f, ts[i0], ts[i1], xtol=1e-12)
            return readout(sphere_min(sv.sol(tg))[1])
    return None
# Umskalierung A = a Ahat, B = b Bhat: phi C3 ~ A^(1/2) B^(3/2) -> xi = xihat / (a^(1/2) b^(3/2))
ab = {"N1": (1, 2), "N2": (1 / 3, 2 / 3), "N3": (1, 2 / 3)}
for name, (aa, bb_) in ab.items():
    ds = []
    for L, kr, xr in itertools.product([0.1, 0.2, 0.3], [-1.0, -0.5], [-0.2, 0.2]):
        g0 = np.array([L / aa**2, kr * L / (aa * bb_), L / bb_**2, xr * L / (aa**0.5 * bb_**1.5), 0.0, 0.0, 0.2])
        out = run7(g0)
        ds.append(None if out is None else out)
    got = [o for o in ds if o is not None]
    dd = np.array([o[1] for o in got])
    on = int(np.sum((np.abs(dd) < 1e-4) | (np.abs(dd - np.pi / 3) < 1e-4)))
    print(f"   {name}: GW {len(got)}/12; delta auf 0 oder pi/3: {on}/{len(got)}; delta-Werte {np.round(np.sort(dd), 5).tolist()}; K {np.round([o[0] for o in got], 5).tolist()}")
