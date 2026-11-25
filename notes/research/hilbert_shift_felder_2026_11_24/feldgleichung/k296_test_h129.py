"""k296: Test H129 (Vorab-Notiz notes/research/predictions/Vorab_Notiz_H129_Schleifen_erzeugen_Skala_im_Anhang.md).
Erzeugt der skalenfreie Ansatz V = lamA A^2 + kappa A B + lamB B^2 (mu2 = 0) bei einer Schleife eine Skala im Anhang?
A  Einschleifen-beta-Funktionen aus 16 pi^2 dV/dln(mu) = 1/2 Tr[(d^2 V)^2]
B  Fluss ins Infrarote auf dem festen Gitter, Klassen (i) keine Skala, (ii) Anhang, (iii) Vorstufe, (iv) beide
C  Korrektur der kinetischen Normierung aus c1 K1 und c2 K2 (Variante D_mu psi, euklidisch, Abschneidung)
Aufruf: python k296_test_h129.py > k296_out.txt
"""
import itertools
import numpy as np
import sympy as sp
from scipy.integrate import solve_ivp

x = sp.symbols("x0:4", real=True)
lA, lB, ka = sp.symbols("lambda_A lambda_B kappa", real=True)
A = x[0] ** 2 + x[1] ** 2; B = x[2] ** 2 + x[3] ** 2
V = lA * A ** 2 + ka * A * B + lB * B ** 2

print("== A  beta-Funktionen (t = ln mu, Faktor 16 pi^2 links) ==")
H = sp.hessian(V, x)
rhs = sp.expand(sp.Rational(1, 2) * (H * H).trace())
bA, bK, bB = sp.symbols("bA bK bB")
rest = sp.Poly(sp.expand(rhs - (bA * A ** 2 + bK * A * B + bB * B ** 2)), *x)
sol = sp.solve(rest.coeffs(), (bA, bK, bB), dict=True)[0]
print("  1/2 Tr[(d^2V)^2] liegt wieder in der Form A^2, A B, B^2 (Nullrest):",
      sp.expand((rhs - (bA * A ** 2 + bK * A * B + bB * B ** 2)).subs(sol)) == 0)
beta = [sp.factor(sol[b]) for b in (bA, bK, bB)]
print("  16 pi^2 d lamA/dt =", beta[0], ";  16 pi^2 d kappa/dt =", beta[1], ";  16 pi^2 d lamB/dt =", beta[2])
lam, r = sp.symbols("lambda r", real=True)
bs = [b.subs({lA: lam, lB: lam, ka: r * lam}) for b in beta]
print("  symmetrisch lamA = lamB = lam, r = kappa/lam: 16 pi^2 dr/dt =", sp.factor(sp.simplify((bs[1] * lam - r * lam * bs[0]) / lam ** 2)),
      " (ins Infrarote mit umgekehrtem Vorzeichen)")
print("  O(4)-Punkt kappa = 2 lam: beta_kappa - 2 beta_lam =", sp.simplify((beta[1] - 2 * beta[0]).subs({lA: lam, lB: lam, ka: 2 * lam})))

print("\n== B  Fluss ins Infrarote, tau = ln(mu0/mu)/(16 pi^2) von 0 bis 1e4 ==")
f = sp.lambdify((lA, ka, lB), [-b for b in beta], "numpy")
def rhs_num(tau, y): return f(*y)
def evA(tau, y): return y[0]
def evB(tau, y): return y[2]
def evS(tau, y): return y[1] + 2 * np.sqrt(max(y[0] * y[2], 0.0))
for e in (evA, evB, evS): e.terminal = True; e.direction = -1
grid_l = [round(0.05 * i, 2) for i in range(1, 11)]
grid_k = [round(-0.95 + 0.05 * i, 2) for i in range(0, 50) if abs(-0.95 + 0.05 * i) > 1e-9]
Hn = sp.lambdify((x, lA, ka, lB), H, "numpy")
count = {}; sub = {}; frueh = 0; fenster = []; gw_ok = {"ii": 0, "iii": 0, "iv": 0}; gw_all = {"ii": 0, "iii": 0, "iv": 0}; taus = {"ii": [], "iii": [], "iv": []}
npts = 0
for a0, b0, k0 in itertools.product(grid_l, grid_l, grid_k):
    if k0 <= -2 * np.sqrt(a0 * b0) + 1e-12: continue
    npts += 1
    s = solve_ivp(rhs_num, (0, 1e4), [a0, k0, b0], events=(evA, evB, evS), method="LSODA", rtol=1e-9, atol=1e-13)
    hit = [len(t) > 0 for t in s.t_events]
    if not any(hit):
        cls = "i"; fenster.append(k0 / np.sqrt(a0 * b0))
    else:
        if hit[2]: cls = "iv"
        elif hit[0] and hit[1] or (a0 == b0 and (hit[0] or hit[1])): cls = "ii=iii"
        elif hit[1]: cls = "ii"
        else: cls = "iii"
        ya, yk, yb = s.y[:, -1]
        if cls != "ii=iii":
            pt = {"ii": (0, 0, 1, 0), "iii": (1, 0, 0, 0), "iv": (np.sqrt(np.sqrt(max(yb, 0))), 0, np.sqrt(np.sqrt(max(ya, 0))), 0)}[cls]
            ev = np.linalg.eigvalsh(np.array(Hn(pt, ya, yk, yb), dtype=float))
            gw_all[cls] += 1; gw_ok[cls] += int(ev.min() > -1e-6 and np.sum(ev ** 2) > 0)
            taus[cls].append(s.t[-1])
    count[cls] = count.get(cls, 0) + 1
    if cls != "i" and s.t[-1] <= 0.25: frueh += 1
    if a0 in (0.1, 0.3, 0.5) and b0 in (0.1, 0.3, 0.5): sub[cls] = sub.get(cls, 0) + 1
print("  Gitterpunkte:", npts, "; Klassen:", dict(sorted(count.items())))
mit = npts - count.get("i", 0)
print(f"  K-a: Anteil mit Skala = {mit}/{npts} = {mit / npts:.4f}")
gl = count.get("ii=iii", 0)
print(f"  K-b: Anteil Anhang unter den Punkten mit Skala = {count.get('ii', 0)}/{mit} = {count.get('ii', 0) / mit:.4f}"
      f" (Gleichstaende lamA = lamB: {gl}; mit halben Gleichstaenden {(count.get('ii', 0) + gl / 2) / mit:.4f})")
print(f"  Fenster ohne Skala: kappa/sqrt(lamA lamB) von {min(fenster):.3f} bis {max(fenster):.3f}; kappa > 0 bei allen: {min(fenster) > 0}")
print("  Gildener-Weinberg (Massenquadrate >= 0 quer zur flachen Richtung, Summe m^4 > 0):", {c: f"{gw_ok[c]}/{gw_all[c]}" for c in gw_ok})
print("  tau beim Ereignis (Median, Maximum):", {c: (float(np.median(v)), float(np.max(v))) for c, v in taus.items() if v})
print(f"  nachtraeglich (nicht im Kriterium): Skala schon bei tau <= 0.25, also ln(mu0/mu) <= 39.5: {frueh}/{npts} = {frueh / npts:.4f}")
print("  Teilgitter lamA, lamB in {0.1, 0.3, 0.5} fuer die Gegenprobe k296b:", dict(sorted(sub.items())))
print("  Kontrolle symmetrischer Fall lam = 0.2: Klasse fuer kappa/lam =", end=" ")
for rr in (-1.0, 0.5, 1.0, 1.9, 2.0, 2.1, 3.0):
    s = solve_ivp(rhs_num, (0, 1e4), [0.2, rr * 0.2, 0.2], events=(evA, evB, evS), method="LSODA", rtol=1e-10, atol=1e-14)
    hit = [len(t) > 0 for t in s.t_events]
    print(rr, "->", "iv" if hit[2] else ("ii=iii" if hit[0] or hit[1] else f"i (kappa/lam am Ende {s.y[1, -1] / s.y[0, -1]:.3f})"), end="; ")
print()

print("\n== C  kinetische Normierung aus den Zusatztermen (eine Kontraktion, <d_mu x_a d_nu x_b> = delta delta J) ==")
v = [[sp.Symbol(f"v{m}{a}", real=True) for a in range(4)] for m in range(4)]
dot = lambda p, q: sum(i * j for i, j in zip(p, q))
def qmul(p, q):
    a0, a1, a2, a3 = p; b0, b1, b2, b3 = q
    return [a0 * b0 - a1 * b1 - a2 * b2 - a3 * b3, a0 * b1 + a1 * b0 + a2 * b3 - a3 * b2,
            a0 * b2 - a1 * b3 + a2 * b0 + a3 * b1, a0 * b3 + a1 * b2 - a2 * b1 + a3 * b0]
com = lambda p, q: [m - n for m, n in zip(qmul(p, q), qmul(q, p))]
pairs = [(m, n) for m in range(4) for n in range(m + 1, 4)]
K1 = sum(dot(v[m], v[m]) * dot(v[n], v[n]) - dot(v[m], v[n]) ** 2 for m, n in pairs)
K2 = sum(dot(com(v[m], v[n]), com(v[m], v[n])) for m, n in pairs)
J, c1, c2 = sp.symbols("J c1 c2", positive=True)
allv = [s for row in v for s in row]
for name, K, c in (("K1", K1, c1), ("K2", K2, c2)):
    quad = sp.expand(c * J / 2 * sum(sp.diff(K, s, 2) for s in allv))
    co = [[quad.coeff(v[m][a], 2) for a in range(4)] for m in range(4)]
    offdiag = sp.expand(quad - sum(co[m][a] * v[m][a] ** 2 for m in range(4) for a in range(4)))
    print(f"  {name}: delta L_E = sum_a z_a (d x_a)^2 mit z_a =", co[0], "; gleich fuer alle mu:", all(co[m] == co[0] for m in range(4)),
          "; gemischte Terme:", offdiag, f" => delta Z_a = 2 z_a")
print("  K-c: Anhang (x2, x3) gegen Vorstufe (x0, x1) siehe z_a oben.")
