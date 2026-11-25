"""k334 (H151): Haengt die Koide-Verschiebung aus H150 mit delta = 2/9 oder einer anderen Setzung zusammen?

Vorab-Notiz: Vorab_Notiz_H151_Verschiebung_und_Zwei_Neuntel.md (Commits 8fc75b5, Nachtrag 4676bce).
Aufruf: python k334_verschiebung_setzungen.py > k334_out.txt
"""
import itertools
import numpy as np
import sympy as sp
from scipy.integrate import solve_ivp

lA, lB, ka, x, k = sp.symbols("lambda_A lambda_B kappa x k", real=True)

def betas(nA, nB):
    X = sp.symbols(f"x0:{nA}", real=True); Y = sp.symbols(f"y0:{nB}", real=True)
    A = sum(v**2 for v in X); B = sum(v**2 for v in Y)
    V = lA * A**2 + ka * A * B + lB * B**2
    H = sp.hessian(V, list(X) + list(Y)); rhs = sp.expand(sp.Rational(1, 2) * (H * H).trace())
    bA, bK, bB = sp.symbols("bA bK bB")
    sol = sp.solve(sp.Poly(sp.expand(rhs - (bA * A**2 + bK * A * B + bB * B**2)), *(list(X) + list(Y))).coeffs(), (bA, bK, bB), dict=True)[0]
    return [sp.expand(sol[b]) for b in (bA, bK, bB)], V, list(Y)

print("=== H151a: der Fluss ist O(n_B)-invariant in der Kopien-Ebene, delta bleibt frei ===")
bet, V, Y = betas(1, 2)
phi = sp.symbols("phi", real=True)
rot = {Y[0]: sp.cos(phi) * Y[0] - sp.sin(phi) * Y[1], Y[1]: sp.sin(phi) * Y[0] + sp.cos(phi) * Y[1]}
print("V(Drehung in der Kopien-Ebene) - V =", sp.simplify(V.subs(rot, simultaneous=True) - V))
print("beta-Funktionen enthalten nur lambda_A, kappa, lambda_B (keine Richtung in der Ebene):", bet)

results = {}
for nB in (2, 7):
    print(f"\n=== H151b: Fixstrahlen fuer n_A = 1, n_B = {nB} ===")
    bet, _, _ = betas(1, nB)
    b = [e.subs({lA: x, ka: k, lB: 1}) for e in bet]
    eqs = [sp.expand(b[0] - x * b[2]), sp.expand(b[1] - k * b[2])]
    sols = sp.solve(eqs, [x, k], dict=True)
    for s in sols:
        xv, kv = s[x], s[k]
        if not (xv.is_real and kv.is_real) or xv <= 0:
            continue
        gw = sp.nsimplify(kv + 2 * sp.sqrt(xv))
        print(f"   Fixstrahl lambda_A/lambda_B = {sp.nsimplify(xv)} = {float(xv):.6f}, kappa/lambda_B = {sp.nsimplify(kv)} = {float(kv):.6f}; kappa + 2 sqrt(lA lB) = {float(kv + 2 * sp.sqrt(xv)):.4f}")
    # Grenzwert kappa0 -> 0-: Strahl mit k = 0
    x0 = sp.solve(sp.expand(b[0] - x * b[2]).subs(k, 0), x)
    x0 = [v for v in x0 if v.is_positive][0]
    K0 = (1 + sp.sqrt(x0)) / 3
    print(f"   Strahl kappa = 0: lambda_A/lambda_B = {x0}; Grenzwert K = (1 + sqrt(lA/lB))/3 = {sp.nsimplify(K0)} = {float(K0):.6f}")
    # numerischer Grenzwert: Start auf der Tausch-Linie, kappa0 -> 0-
    f = sp.lambdify((lA, ka, lB), [-e for e in bet], "numpy")
    ev = lambda t, y: y[1] + 2 * np.sqrt(max(y[0] * y[2], 0.0)); ev.terminal = True; ev.direction = -1
    Ks = []
    for k0 in (-0.1, -0.01, -1e-3, -1e-4, -1e-5):
        s = solve_ivp(lambda t, y: f(*y), (0, 1e6), [0.2, k0 * 0.2, 0.2], events=ev, method="LSODA", rtol=1e-11, atol=1e-16)
        ya, yk, yb = s.y[:, -1]; Ks.append((1 + np.sqrt(ya / yb)) / 3)
        print(f"   Start lambda = 0.2, kappa0/lambda = {k0:g}: GW bei tau = {s.t[-1]:.4g}, lambda_A/lambda_B = {ya / yb:.6f}, K = {Ks[-1]:.6f}")
    # Start auf dem Strahl kappa = 0 mit kleinem kappa
    s = solve_ivp(lambda t, y: f(*y), (0, 1e6), [0.2 * float(x0), -1e-6, 0.2], events=ev, method="LSODA", rtol=1e-11, atol=1e-16)
    ya, yk, yb = s.y[:, -1]
    Klim = (1 + np.sqrt(ya / yb)) / 3
    print(f"   Start auf dem Strahl kappa = 0 (kappa0 = -1e-6): lambda_A/lambda_B am GW = {ya / yb:.6f}, K = {Klim:.6f}")
    results[nB] = dict(Klim=Klim, ratio=ya / yb)

print("\n=== H151c/d: Zahlenvergleich mit delta und allen Setzungen ===")
gL = 1.864700; bs = np.sqrt((gL - 1) / (gL + 1)); gM = 0.237533; gT = 0.127384
sett = {"S1 delta": 2 / 9, "S2 theta": np.pi / 4, "S3 beta_sym": bs, "S4 gamma_L": gL, "S5 eps": np.arctanh(bs), "S6 mu": bs**2,
        "S7 kappa_hit": (gL + 1 / gL) / 2, "S8 kappa*": 1.2039, "S9 rho^2": 0.5, "S10 gamma_M": gM, "S11a gamma_M/6": gM / 6,
        "S11b gamma_M/2": gM / 2, "S12 gamma_T": gT, "S13a 1/2": 0.5, "S13b 1/7": 1 / 7}
print("   Setzungen:", {k_: round(v, 6) for k_, v in sett.items()})
forms = {"s": lambda s: s, "s^2": lambda s: s**2, "sqrt s": np.sqrt, "1/s": lambda s: 1 / s, "s/3": lambda s: s / 3, "s/9": lambda s: s / 9}
Xs = {}
for nB, rr in results.items():
    K = rr["Klim"]; t2 = 3 * K - 1; th = np.arctan(np.sqrt(t2))
    Xs[f"dK* (n_B={nB})"] = K - 2 / 3
    Xs[f"theta*-pi/4 (n_B={nB})"] = th - np.pi / 4
    Xs[f"tan^2 theta*-1 (n_B={nB})"] = t2 - 1
for k_, v in Xs.items():
    print(f"   X: {k_:24s} = {v:.6f}")
# H151c: gegen f(delta)
d = 2 / 9
fd = {"delta": d, "delta^2": d**2, "delta/3": d / 3, "delta/4": d / 4, "delta^2/2": d**2 / 2, "1-cos delta": 1 - np.cos(d), "sin^2 delta": np.sin(d)**2, "1-cos 3delta": 1 - np.cos(3 * d)}
hc = [(xk, fk, xv / fv - 1) for xk, xv in Xs.items() for fk, fv in fd.items() if abs(xv / fv - 1) < 0.005]
print(f"   H151c: {len(Xs)} x {len(fd)} = {len(Xs) * len(fd)} Vergleiche, Treffer < 0,5 %: {len(hc)}", [(a, b_, f'{c:+.4%}') for a, b_, c in hc])
near = sorted(((abs(xv / fv - 1), xk, fk) for xk, xv in Xs.items() for fk, fv in fd.items()))[:3]
print("   naechste:", [(xk, fk, f"{r:.2%}") for r, xk, fk in near])
# H151d: gegen alle Setzungen
cands = {f"{sk} [{fk}]": ff(sv) for sk, sv in sett.items() for fk, ff in forms.items()}
hd = [(xk, ck, xv / cv - 1) for xk, xv in Xs.items() for ck, cv in cands.items() if abs(xv / cv - 1) < 0.005]
ncomp = len(Xs) * len(cands)
print(f"   H151d: {len(Xs)} x {len(cands)} = {ncomp} Vergleiche, Treffer < 0,5 %:", len(hd))
for a, b_, c in hd:
    print(f"      {a} ~ {b_}: {c:+.4%}")
p = np.log(1.005 / 0.995) / np.log(1e4)
print(f"   Look-elsewhere analytisch: p je Paar = {p:.5f}, Erwartung {ncomp * p:.2f} (H151c: {len(Xs) * len(fd) * p:.3f})")
rng = np.random.default_rng(334); cv = np.array(list(cands.values()))
sims = []
for _ in range(10000):
    R = 10**rng.uniform(-3, 1, size=len(Xs))
    sims.append(int(np.sum(np.abs(R[:, None] / cv[None, :] - 1) < 0.005)))
sims = np.array(sims)
print(f"   empirisch (10^4 Saetze, X log-gleich in [1e-3, 10]): Mittel {sims.mean():.2f}, 99-%-Quantil {np.quantile(sims, 0.99):.0f}; beobachtet {len(hd)} -> {'auffaellig' if len(hd) > np.quantile(sims, 0.99) else 'nicht auffaellig'}")
print("   Gitter (nicht gewertet, aus H150): K 0,6667 .. 0,6778, Median 0,6719 -> dK 0 .. 0,0111, Median 0,0053")

print("\n=== H151e: Frame-Differenz ===")
e_, t_ = sp.symbols("epsilon t", real=True)
phi_, chi_ = sp.cos(t_), sp.sin(t_)
p2 = sp.cosh(e_) * phi_ + sp.sinh(e_) * chi_; c2 = sp.sinh(e_) * phi_ + sp.cosh(e_) * chi_
print("   Boost erhaelt phi^2 - chi^2:", sp.simplify(p2**2 - c2**2 - (phi_**2 - chi_**2)) == 0)
print("   lichtartiger Punkt t = pi/4: chi'/phi' =", sp.simplify((c2 / p2).subs(t_, sp.pi / 4)))
print("   Form S: K = Tr(G^2)/(Tr G)^2 ist unter G -> S G S^-1 invariant (Spuren); keine Aenderung.")
gL = 1.864700; bs = np.sqrt((gL - 1) / (gL + 1))
eps_list = {"artanh beta_sym": np.arctanh(bs), "artanh beta_sym^2": np.arctanh(bs**2), "ln gamma_L": np.log(gL)}
for nB, rr in results.items():
    t2 = 3 * rr["Klim"] - 1; th = np.arctan(np.sqrt(t2)); ph, ch = np.cos(th), np.sin(th)
    print(f"   n_B = {nB}: vor dem Boost K = {rr['Klim']:.6f}, Re Psi^2 = {ph**2 - ch**2:+.6f} (Seite: {'raumartig, tan > 1' if ch > ph else 'zeitartig'})")
    for nm, ev_ in eps_list.items():
        for sg in (+1, -1):
            e = sg * ev_; P = np.cosh(e) * ph + np.sinh(e) * ch; C = np.sinh(e) * ph + np.cosh(e) * ch
            Kb = (1 + (C / P)**2) / 3
            print(f"      eps = {'+' if sg > 0 else '-'}{nm} = {e:+.5f}: tan theta' = {C / P:.6f}, K' = {Kb:.6f}, K' - 2/3 = {Kb - 2 / 3:+.6f}")
    # gibt es irgendein eps mit K' = 2/3?  tan theta' = 1 <=> C = P <=> (ch - ph)(cosh e - sinh e) = 0
    print(f"      K' = 2/3 verlangt (sin - cos)(cosh eps - sinh eps) = 0, also e^(-eps) = 0: fuer kein endliches eps")
# H151e: K' - 2/3 nach dem Boost gegen die Setzungsliste (Regeln wie H151d)
Ye = {}
for nB, rr in results.items():
    t2 = 3 * rr["Klim"] - 1; th = np.arctan(np.sqrt(t2)); ph, ch = np.cos(th), np.sin(th)
    for nm, ev_ in eps_list.items():
        for sg in (+1, -1):
            e = sg * ev_; P = np.cosh(e) * ph + np.sinh(e) * ch; C = np.sinh(e) * ph + np.cosh(e) * ch
            Ye[f"n_B={nB} {'+' if sg > 0 else '-'}{nm}"] = (1 + (C / P)**2) / 3 - 2 / 3
he = [(yk, ck, yv / cv - 1) for yk, yv in Ye.items() for ck, cv in cands.items() if abs(yv / cv - 1) < 0.005]
ne = len(Ye) * len(cands)
sims = np.array([int(np.sum(np.abs((10**rng.uniform(-3, 1, size=len(Ye)))[:, None] / cv[None, :] - 1) < 0.005)) for _ in range(10000)])
print(f"   H151e Setzungsvergleich: {len(Ye)} x {len(cands)} = {ne} Vergleiche, Treffer {len(he)}; Zufall Mittel {sims.mean():.2f}, 99-%-Quantil {np.quantile(sims, 0.99):.0f}")
for a, b_, c in he:
    print(f"      {a} ~ {b_}: {c:+.4%}")
