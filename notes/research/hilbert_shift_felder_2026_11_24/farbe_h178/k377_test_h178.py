"""k377 (H178): Frame-Tausch J auf Feldern mit Farbanteil. Aufruf: python k377_test_h178.py > k377_out.txt"""
import numpy as np, sympy as sp
from fractions import Fraction
rng = np.random.default_rng(20261126)

# --- Oktonionen ueber Cayley-Dickson: (a, b)(c, d) = (ac - d* b, d a + b c*)
def conj(x):
    y = -x.copy(); y[0] = x[0]; return y
def mul(x, y):
    n = len(x)
    if n == 1: return x * y
    h = n // 2; a, b, c, d = x[:h], x[h:], y[:h], y[h:]
    return np.concatenate([mul(a, c) - mul(conj(d), b), mul(d, a) + mul(b, conj(c))])
e = np.eye(8); one = e[0]; U = e[7]
J = lambda z: mul(U, conj(z))

print("== H178a: J auf ganz O (U = e7) ==")
err_pl = max(np.abs(J(J(z)) - z).max() for z in (one, U, 0.3 * one - 1.7 * U))
err_c = max(np.abs(J(J(e[i])) + e[i]).max() for i in range(1, 7))
print(f"   J^2 = +1 auf {{1, U}}: Fehler {err_pl:.1e};  J^2 = -1 auf e1..e6: Fehler {err_c:.1e}")
print("   Bilder der Einheiten: " + "; ".join(f"J(e{i}) = {'+' if J(e[i])[np.abs(J(e[i])).argmax()] > 0 else '-'}e{np.abs(J(e[i])).argmax()}" for i in range(8)))
mx = 0
for _ in range(1000):
    z = rng.normal(size=8); Jz = J(z)
    mx = max(mx, abs(Jz[0] - z[7]), abs(Jz[7] - z[0]), abs(np.sum(Jz[1:7]**2) - np.sum(z[1:7]**2)), abs(Jz @ Jz - z @ z))
print(f"   J tauscht x0 und xU, erhaelt |c|^2 und N (1000 Zufallselemente): groesste Abweichung {mx:.1e}")
c = e[1]; th = 0.3
P = np.cos(th) * one + np.sin(th) * c; JP = J(P)
print(f"   Ebene {{1, c}}, c = e1: J(cos t + sin t c) hat Komponenten nur auf {[i for i in range(8) if abs(JP[i]) > 1e-12]} (also auf U und U c): die Ebene wird nicht auf sich abgebildet.")
print("   Folge: Die Abbildung theta -> pi/2 - theta gibt es nur in der Ebene {1, U}.")

print("\n== H178b: allgemeinstes Potential bis Grad 4, invariant unter SU(3)_c, Konjugation und J ==")
print("   Invarianten eines Elements unter SU(3)_c: x0, xU, q = |c|^2. Konjugation: xU -> -xU. J: x0 <-> xU.")
print("   Grad 2: s = x0^2 + xU^2, q.  Grad 4: s^2, s q, q^2, p = x0^2 xU^2.  Auf N = s + q = 1: V = A q + B q^2 + kappa p + konst. (drei Koeffizienten).")
t, al, A, B, kap = sp.symbols("t alpha A B kappa", real=True)
sa, ca = sp.sin(al)**2, sp.cos(al)**2
V = A * sa * t + B * sa**2 * t**2 + kap * ca * t * (1 - t)          # t = sin^2(theta)
tstar = sp.simplify(sp.solve(sp.diff(V, t), t)[0]); curv = sp.simplify(sp.diff(V, t, 2))
print("   V(t), t = sin^2 theta:", V)
print("   stationaer bei t* =", tstar, ";  V'' =", curv)
print("   alpha = 0: t* =", sp.simplify(tstar.subs(al, 0)), "(theta = pi/4, unabhaengig von A, B);  V'' =", sp.simplify(curv.subs(al, 0)), "(Minimum genau fuer kappa < 0)")
print("   d t*/dA =", sp.simplify(sp.diff(tstar, A)), " -> fuer alpha != 0 haengt der Winkel von den Koeffizienten ab.")
print("   Urteil H178b: BESTAETIGT (pi/4 ist nur fuer alpha = 0 festgelegt).")

print("\n== H178c: ein Potential, Sektoren nur durch den Farbanteil unterschieden ==")
TH = {"d": (48.114, 0.039), "u": (52.207, 0.021)}
rules = {"R1 (sin^2 alpha = 1 - |Q|)": {"d": Fraction(2, 3), "u": Fraction(1, 3), "Q0": Fraction(1)},
         "R2 (sin^2 alpha = |Q|)": {"d": Fraction(1, 3), "u": Fraction(2, 3), "Q0": Fraction(0)}}
def solve_ab(td, tu, sd, su):
    # kappa = -1: t (2 B s^2 + 2 c) = c - A s ... aus dV/dt = 0:  A s + 2 B s^2 t - c (1 - 2 t) = 0
    M = np.array([[sd, 2 * sd**2 * td], [su, 2 * su**2 * tu]]); r = np.array([(1 - sd) * (1 - 2 * td), (1 - su) * (1 - 2 * tu)])
    return np.linalg.solve(M, r)
for name, R in rules.items():
    sd, su = float(R["d"]), float(R["u"])
    td0, tu0 = (np.sin(np.radians(TH[k][0]))**2 for k in "du")
    a, b = solve_ab(td0, tu0, sd, su)
    cd, cu = 2 * b * sd**2 + 2 * (1 - sd), 2 * b * su**2 + 2 * (1 - su)        # V'' mit kappa = -1
    print(f"-- {name}: A/|kappa| = {a:+.4f}, B/|kappa| = {b:+.4f}; V''(d) = {cd:+.4f}, V''(u) = {cu:+.4f}; Leptonen V'' = +2 (kappa < 0)")
    # Fehlerband 3 sigma
    stab = []
    for dd in (-3, 0, 3):
        for du in (-3, 0, 3):
            td = np.sin(np.radians(TH["d"][0] + dd * TH["d"][1]))**2; tu = np.sin(np.radians(TH["u"][0] + du * TH["u"][1]))**2
            a_, b_ = solve_ab(td, tu, sd, su); stab.append(2 * b_ * sd**2 + 2 * (1 - sd) > 0 and 2 * b_ * su**2 + 2 * (1 - su) > 0)
    v = "VERTRAEGLICH (stabile Loesung im ganzen 3-sigma-Band)" if all(stab) else ("WIDERLEGT (keine stabile Loesung)" if not any(stab) else "teilweise stabil")
    print(f"   Urteil: {v}. Zaehlung: zwei Messgroessen (theta_d, theta_u), zwei freie Verhaeltnisse (A/kappa, B/kappa): keine Bestaetigung.")
    s0 = float(R["Q0"])
    if s0 == 0: print("   Bericht Q = 0: alpha = 0, also theta = 45 Grad, K = 2/3 (wie die geladenen Leptonen).")
    else:
        t0 = (-(a * s0) + (1 - s0)) / (2 * b * s0**2 + 2 * (1 - s0)); c0 = 2 * b * s0**2 + 2 * (1 - s0)
        if 0 <= t0 <= 1: print(f"   Bericht Q = 0: reiner Farbanteil, t* = {t0:.4f}, theta = {np.degrees(np.arcsin(np.sqrt(t0))):.2f} Grad, K = {(1 + t0/(1-t0))/3:.4f}, V'' = {c0:+.4f}")
        else: print(f"   Bericht Q = 0: reiner Farbanteil, t* = {t0:.4f} liegt ausserhalb [0, 1]; V'' = {c0:+.4f}: Randminimum bei theta = {'90' if (t0 > 1) == (c0 > 0) else '0'} Grad")
    # Verlauf theta(sin^2 alpha)
    print("   Verlauf theta(sin^2 alpha): " + ", ".join(f"{s:.2f}: {np.degrees(np.arcsin(np.sqrt(np.clip(((1-s) - a*s)/(2*b*s*s + 2*(1-s)), 0, 1)))):.2f}" for s in (0, 0.1, 1/3, 0.5, 2/3, 0.9)))

print("\n== Vorab bekannt (nicht blind): Farbe allein ==")
print(f"   gleiches alpha fuer beide Quarktypen gibt theta_u = theta_d; gemessen {TH['u'][0] - TH['d'][0]:.3f} Grad Unterschied ({(TH['u'][0] - TH['d'][0]) / np.hypot(TH['u'][1], TH['d'][1]):.0f} sigma). Ausgeschlossen.")
print("\n== Bericht: Variante <J> ohne Konjugation ==")
print("   Zusaetzlich erlaubt: m = x0 xU (Grad 2) sowie m s, m q (Grad 4); m^2 = p. Auf N = 1 drei weitere Koeffizienten.")
th_, nu = sp.symbols("theta nu", real=True)
Vm = nu * sp.cos(th_) * sp.sin(th_)
print("   alpha = 0: m = sin(2 theta)/2, d m/d theta bei pi/4 =", sp.diff(Vm, th_).subs(th_, sp.pi / 4), "-> pi/4 bleibt stationaer; fuer alpha != 0 kommen weitere freie Zahlen dazu (keine schaerfere Aussage).")
