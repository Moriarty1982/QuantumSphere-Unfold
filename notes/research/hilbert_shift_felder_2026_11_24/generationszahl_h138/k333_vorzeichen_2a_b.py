"""k333 (H150): Folgt das Vorzeichen von 2a - b aus der Feldgleichung?

Vorab-Notiz: Vorab_Notiz_H150_Vorzeichen_2a_minus_b.md (Commit fc17ee9).
Aufruf: python k333_vorzeichen_2a_b.py > k333_out.txt  (Laufzeit etwa eine Minute).
Zuordnung: A = Norm der Vorstufe (phi = Re Psi, n_A Komponenten), B = Norm des Anhangs (Kopienrichtung, n_B Komponenten);
a = lambda_A, b = kappa, c = lambda_B. Kein Vorzeichen wird gesetzt.
"""
import itertools
import numpy as np
import sympy as sp
from scipy.integrate import solve_ivp

lA, lB, ka, lam, r, th, eta, mu = sp.symbols("lambda_A lambda_B kappa lambda r theta eta mu", real=True)

def beta_functions(nA, nB):
    x = sp.symbols(f"x0:{nA}", real=True); y = sp.symbols(f"y0:{nB}", real=True)
    A = sum(v**2 for v in x); B = sum(v**2 for v in y)
    V = lA * A**2 + ka * A * B + lB * B**2
    H = sp.hessian(V, list(x) + list(y))
    rhs = sp.expand(sp.Rational(1, 2) * (H * H).trace())
    bA, bK, bB = sp.symbols("bA bK bB")
    sol = sp.solve(sp.Poly(sp.expand(rhs - (bA * A**2 + bK * A * B + bB * B**2)), *(list(x) + list(y))).coeffs(), (bA, bK, bB), dict=True)[0]
    # quadratisch divergente Massenkorrektur: Spur der Hesseschen in den Schleifenfeldern, Koeffizient von A bzw. B
    tr = sp.expand(H.trace())
    dmA = sp.Poly(tr, *(list(x) + list(y))).coeff_monomial(x[0]**2)
    dmB = sp.Poly(tr, *(list(x) + list(y))).coeff_monomial(y[0]**2)
    return [sp.factor(sol[b]) for b in (bA, bK, bB)], (sp.factor(dmA), sp.factor(dmB))

print("=== H150a: volle Norm / geeichte U(1) ===")
a_, b_, c_ = lA, ka, lB
VN = lam * (sp.cos(th)**2 + sp.sin(th)**2)**2
print("V(N) = lambda N^2 -> a = c = lambda, b = 2 lambda: 2a - b =", 2 * lam - 2 * lam)
for n in (1, 2):
    bet, _ = beta_functions(n, n)
    val = sp.simplify((bet[1] - 2 * bet[0]).subs({lA: lam, lB: lam, ka: 2 * lam}))
    print(f"   n_A = n_B = {n}: beta_kappa - 2 beta_lambda bei kappa = 2 lambda: {val}")
    print(f"      beta = ", bet)
bet12, dm12 = beta_functions(1, 2)
val = sp.simplify((bet12[1] - bet12[0] - bet12[2]).subs({lA: lam, lB: lam, ka: 2 * lam}))
print(f"   n_A = 1, n_B = 2: beta_kappa - beta_A - beta_B bei vollem Norm-Punkt: {val}  (volle Norm bleibt auch dort erhalten)")

print("\n=== H150b: Skala als Setzung (mu^2 < 0 gesetzt), Baumgraph ===")
A = sp.cos(th)**2; B = sp.sin(th)**2
V4 = lam * (A**2 + B**2) + ka * A * B
print("V_4 auf N = 1:", sp.simplify(V4 - (lam - (2 * lam - ka) * A * B)) == 0, "-> V_4 = lambda - (2 lambda - kappa) cos^2 sin^2")
print("   radiale Stabilitaet: Richtung pi/4:", sp.simplify(V4.subs(th, sp.pi / 4)), "> 0 <=> kappa > -2 lambda; Richtung 0:", V4.subs(th, 0), "> 0")
# numerisch: Minimum ueber theta fuer Raster r = kappa/lambda
rows = []
for rr in np.round(np.arange(-1.9, 4.01, 0.1), 2):
    t = np.linspace(0, np.pi / 2, 9001); v = (np.cos(t)**4 + np.sin(t)**4) + rr * np.cos(t)**2 * np.sin(t)**2
    tmin = t[np.argmin(v)]; rows.append((rr, tmin))
ok = all((abs(tm - np.pi / 4) < 1e-3) == (rr < 2) for rr, tm in rows if abs(rr - 2) > 1e-9)
print(f"   Raster r in [-1.9, 4]: Minimum bei pi/4 genau fuer r < 2, sonst bei 0 oder pi/2: {ok}")
print("   quadratisch divergente Korrekturen (Koeffizient von x^2 bzw. y^2 in Tr d^2V):")
for nA, nB in [(1, 1), (2, 2), (1, 2), (1, 7)]:
    _, (dA, dB) = beta_functions(nA, nB)
    diff = sp.simplify((dA - dB).subs({lA: lam, lB: lam}))
    print(f"   n_A = {nA}, n_B = {nB}: dmu_A^2 ~ {dA}, dmu_B^2 ~ {dB}; auf der Tausch-Linie Differenz {diff}")
print("   -> mit n_A != n_B entsteht ein tauschungerader Massenterm (mu0^2 != mu1^2, H149c) proportional Lambda^2.")
# Verschiebung von theta durch den tauschungeraden Massenterm (n_A = 1, n_B = 2), Normierung c_L = Lambda^2/(16 pi^2) * Faktor
cL, f = sp.symbols("c_L f", positive=True)
_, (dA12, dB12) = beta_functions(1, 2)
Vq = sp.Rational(1, 2) * cL * (dA12 * A + dB12 * B) * f**2 + f**4 * (lA * A**2 + ka * A * B + lB * B**2)
Vq = Vq.subs({lA: lam, lB: lam})
dV = sp.simplify(sp.diff(Vq, th) / sp.sin(2 * th))
C = sp.Symbol('C')
dVc = sp.simplify(sp.expand_trig(dV).subs(sp.sin(th)**2, (1 - C) / 2).subs(sp.cos(th)**2, (1 + C) / 2))
print("   n_A = 1, n_B = 2 mit Abschneidung: dV/dtheta / sin 2theta =", sp.factor(dVc), " (C = cos 2theta)")
print("   stationaer bei cos 2theta =", [sp.factor(v) for v in sp.solve(dVc, C)], " -> unabhaengig von lambda, kappa; Koide nur fuer c_L/f^2 -> 0 (skalenfrei)")
print("\n=== H150c: skalenfrei, Fluss auf der Tausch-Linie ===")
def flow(nA, nB):
    bet, _ = beta_functions(nA, nB)
    f = sp.lambdify((lA, ka, lB), [-b for b in bet], "numpy")
    return lambda tau, y: f(*y)
def ev_factory():
    evA = lambda tau, y: y[0]; evB = lambda tau, y: y[2]
    evS = lambda tau, y: y[1] + 2 * np.sqrt(max(y[0] * y[2], 0.0))
    for e in (evA, evB, evS): e.terminal = True; e.direction = -1
    return (evA, evB, evS)
def run(rhs, y0, T=1e4):
    s = solve_ivp(rhs, (0, T), y0, events=ev_factory(), method="LSODA", rtol=1e-10, atol=1e-14)
    hit = [len(t) > 0 for t in s.t_events]
    ya, yk, yb = s.y[:, -1]
    if not any(hit): return "i", ya, yk, yb
    if hit[2]: return "iv", ya, yk, yb
    return ("ii/iii", ya, yk, yb)
def K_of(ya, yb):
    t2 = np.sqrt(ya / yb)            # tan^2 theta = B/A = sqrt(lam_A/lam_B)
    return (1 + t2) / 3
lams = [round(0.05 * i, 2) for i in range(1, 11)]
rs = [x for x in np.round(np.arange(-1.9, 4.01, 0.1), 2) if abs(x) > 1e-9 and abs(x - 2) > 1e-9]
for n in (1, 2):
    rhs = flow(n, n); bad = 0; tally = {}
    for l0, r0 in itertools.product(lams, rs):
        cls, ya, yk, yb = run(rhs, [l0, r0 * l0, l0])
        tally[cls] = tally.get(cls, 0) + 1
        exp = "iv" if r0 < 0 else ("i" if r0 < 2 else "ii/iii")
        if cls != exp: bad += 1
        if cls == "iv" and abs(K_of(ya, yb) - 2 / 3) > 1e-6: bad += 1
        if cls == "i" and not (yk / ya < 2 + 1e-6 and yk / ya > r0 - 1e-9): bad += 1
    print(f"   n = {n}: {len(lams) * len(rs)} Startpunkte, Klassen {tally}, Abweichungen von der Vorhersage: {bad}")
# Krummung 2a - b im Infraroten fuer 0 < r < 2
rhs = flow(2, 2)
s = solve_ivp(rhs, (0, 1e4), [0.2, 0.2, 0.2], method="LSODA", rtol=1e-10, atol=1e-14, dense_output=True)
for tau in (0, 1, 10, 100, 1e4):
    ya, yk, yb = s.sol(tau); print(f"   n = 2, r0 = 1: tau = {tau:g}: r = {yk / ya:.6f}, (2a - b)/a = {2 - yk / ya:.3e}")

print("\n=== H150d: reelle Einheit (n_A = 1) gegen Kopien-Ebene (n_B = 2), Start auf der Tausch-Linie ===")
print("   beta (1, 2):", bet12)
rhs = flow(1, 2); Ks = []; cls_t = {}
for l0 in lams:
    for rk in np.round(np.arange(-1.9, 0.0, 0.1), 2):
        cls, ya, yk, yb = run(rhs, [l0, rk * l0, l0])
        cls_t[cls] = cls_t.get(cls, 0) + 1
        if cls == "iv": Ks.append(K_of(ya, yb))
Ks = np.array(Ks)
frac = np.mean(np.abs(Ks / (2 / 3) - 1) < 0.01) if len(Ks) else 0
print(f"   Klassen {cls_t}; K am GW-Punkt: min {Ks.min():.4f}, Median {np.median(Ks):.4f}, max {Ks.max():.4f}; Anteil |K - 2/3| < 1 %: {frac:.3f}")
print("   Urteil:", "Koide ueberlebt" if frac >= 0.9 else "Koide verschoben")
for nB in (7,):
    rhs7 = flow(1, nB); K7 = []
    for l0 in lams:
        for rk in np.round(np.arange(-1.9, 0.0, 0.1), 2):
            cls, ya, yk, yb = run(rhs7, [l0, rk * l0, l0])
            if cls == "iv": K7.append(K_of(ya, yb))
    K7 = np.array(K7)
    print(f"   Zusatz n_B = {nB} (ganze Im O): K Median {np.median(K7):.4f}, Bereich {K7.min():.4f} .. {K7.max():.4f}, Anteil in 1 %: {np.mean(np.abs(K7 / (2 / 3) - 1) < 0.01):.3f}")

print("\n=== H150e: gleiche Komponentenzahl (n = 2), abseits der Tausch-Linie (Gitter wie H129) ===")
rhs = flow(2, 2); closer = 0; niv = 0; kin = 0
grid_k = [round(-0.95 + 0.05 * i, 2) for i in range(0, 50) if abs(-0.95 + 0.05 * i) > 1e-9]
for a0, b0, k0 in itertools.product(lams, lams, grid_k):
    if k0 <= -2 * np.sqrt(a0 * b0) + 1e-12 or a0 == b0: continue
    cls, ya, yk, yb = run(rhs, [a0, k0, b0])
    if cls != "iv": continue
    niv += 1
    closer += abs(np.log(ya / yb)) < abs(np.log(a0 / b0))
    kin += abs(K_of(ya, yb) / (2 / 3) - 1) < 0.01
print(f"   Klasse (iv) abseits der Linie: {niv} Punkte; |ln(lA/lB)| kleiner am Ende: {closer}/{niv} = {closer / niv:.3f}; |K - 2/3| < 1 %: {kin}/{niv} = {kin / niv:.3f}")
print("   Urteil:", "anziehend" if closer / niv >= 0.9 else ("abstossend" if closer / niv <= 0.1 else "gemischt"))

print("\n=== H150f: HC-Form eta (B - mu^2 A)^2 ===")
Vhc = sp.expand(eta * (B - mu**2 * A)**2)
P = sp.Poly(sp.expand(eta * (sp.Symbol('B') - mu**2 * sp.Symbol('A'))**2), sp.Symbol('A'), sp.Symbol('B'))
aa, bb, cc = P.coeff_monomial(sp.Symbol('A')**2), P.coeff_monomial(sp.Symbol('A') * sp.Symbol('B')), P.coeff_monomial(sp.Symbol('B')**2)
print(f"   a = {aa}, b = {bb}, c = {cc}; 2a - b = {sp.factor(2 * aa - bb)}; tauschungerade 2(a - c) = {sp.factor(2 * (aa - cc))}")
print("   Beschraenktheit verlangt eta >= 0 (V -> eta * B^2 fuer A = 0); dann kappa = b =", bb, "<= 0")
print("   Minimum (V = 0) bei tan^2 theta = mu^2, also tan theta = mu; Kontrolle V(arctan mu) =", sp.simplify(Vhc.subs(th, sp.atan(mu))))
