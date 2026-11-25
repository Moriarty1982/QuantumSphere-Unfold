"""k301 (Erkundung, nicht blind): Fassung F des HC (k299) am ruhenden Igel aus k291, erste Ordnung in eta2.
P = eta2 (S_s - tau^2 S_i)^2 / N^2 mit S_i = sum_a (J_a^i)^2, S_s = sum_a (J_a^j)^2 + (J_a^k)^2, J_a = conj(psi) d_a psi, N = f^2.
Mit S_ges = S_i + S_s und T = 1 + tau^2:  P = eta2 f^4 (S_ges - T S_i)^2 (Stroeme des Einheitsfelds).
1  Stroeme des Igels: S_ges = p + 2 s, S_i = p c + s (1 - c), p = F'^2, s = sin^2 F / r^2, c = (x/r)^2
2  Winkelmittel und das T, bei dem der Igel am wenigsten kostet; Schranken 5/3 <= T* <= 3
3  Profil aus k291 (Minimierung), Integrale, T*, Kosten beim HC-Wert T = 1/cos^2(2 theta)
Aufruf: python k301_fassung_F_am_igel.py > k301_out.txt
"""
import numpy as np
import sympy as sp
from scipy.optimize import minimize

print("== 1  Stroeme des Igels ==")
X, Y, Z = sp.symbols("x y z", real=True)
r = sp.sqrt(X ** 2 + Y ** 2 + Z ** 2); F = lambda u: sp.pi * sp.exp(-u / sp.Rational(6, 5))       # Probeprofil
U = [sp.cos(F(r)), sp.sin(F(r)) * X / r, sp.sin(F(r)) * Y / r, sp.sin(F(r)) * Z / r]
def qmul(p, q):
    a0, a1, a2, a3 = p; b0, b1, b2, b3 = q
    return [a0 * b0 - a1 * b1 - a2 * b2 - a3 * b3, a0 * b1 + a1 * b0 + a2 * b3 - a3 * b2,
            a0 * b2 - a1 * b3 + a2 * b0 + a3 * b1, a0 * b3 + a1 * b2 - a2 * b1 + a3 * b0]
qc = lambda p: [p[0], -p[1], -p[2], -p[3]]
Jc = [qmul(qc(U), [sp.diff(c, s) for c in U]) for s in (X, Y, Z)]
Si = sum(J[1] ** 2 for J in Jc); Sg = sum(J[1] ** 2 + J[2] ** 2 + J[3] ** 2 for J in Jc)
p_, s_, c_ = sp.symbols("p s c", positive=True)
u_ = sp.Symbol("u", positive=True)
print("  Probeprofil F = pi exp(-r/1.2), zwei Punkte:")
for pt in ({X: sp.Rational(3, 10), Y: sp.Rational(-7, 10), Z: sp.Rational(11, 10)}, {X: sp.Rational(9, 10), Y: sp.Rational(2, 10), Z: sp.Rational(-4, 10)}):
    rv = sp.sqrt(sum(v ** 2 for v in pt.values()))
    pp, ss, cc = sp.diff(F(u_), u_).subs(u_, rv) ** 2, sp.sin(F(rv)) ** 2 / rv ** 2, pt[X] ** 2 / rv ** 2
    print("    S_ges - (p + 2 s) =", sp.N(Sg.subs(pt) - (pp + 2 * ss), 3), ";  S_i - (p c + s (1 - c)) =", sp.N(Si.subs(pt) - (pp * cc + ss * (1 - cc)), 3),
          ";  Re J = 0:", [sp.N(J[0].subs(pt), 3) for J in Jc])

print("\n== 2  Winkelmittel ==")
T = sp.symbols("T", positive=True)
avg = lambda e: sp.integrate(sp.expand(e).subs(c_, sp.Symbol("u") ** 2), (sp.Symbol("u"), 0, 1))       # c = cos^2, u gleichverteilt auf [0, 1]
Sg_, Si_ = p_ + 2 * s_, p_ * c_ + s_ * (1 - c_)
m1, m2 = sp.simplify(avg(Si_)), sp.factor(avg(Si_ ** 2))
print("  <S_i> =", m1, " (= S_ges/3);  <S_i^2> =", m2)
dens = sp.expand(Sg_ ** 2 - 2 * T * Sg_ * m1 + T ** 2 * m2)
print("  <(S_ges - T S_i)^2> =", sp.factor(dens))
Tloc = sp.simplify(Sg_ * m1 / m2)
print("  punktweise bestes T:", Tloc, ";  p = s:", Tloc.subs(p_, s_), ";  s = 0:", sp.limit(Tloc, s_, 0), ";  p = 0:", sp.limit(Tloc, p_, 0))
q = sp.symbols("q", positive=True)
Tq = sp.simplify(Tloc.subs(p_, q * s_))
print("  als Funktion von q = p/s:", Tq, ";  Maximum bei q =", sp.solve(sp.diff(Tq, q), q), ";  also 5/3 <= T* <= 3")
print("  kleinster Wert von <(S_ges - T S_i)^2>/S_ges^2 bei p = s:", sp.simplify((dens / Sg_ ** 2).subs(p_, s_)), " => null nur fuer T = 3")

print("\n== 3  Profil und Integrale (Laengeneinheit und Energieeinheit wie k291) ==")
def energy(Fv, rho):
    Fm = 0.5 * (Fv[1:] + Fv[:-1]); rm = 0.5 * (rho[1:] + rho[:-1]); dF = np.diff(Fv) / np.diff(rho)
    s2 = np.sin(Fm) ** 2 / rm ** 2
    return np.sum(rm ** 2 * (0.5 * (dF ** 2 + 2 * s2) + s2 * (2 * dF ** 2 + s2)) * np.diff(rho))
gL = 1.8644; mu = (gL - 1) / (gL + 1); THC = ((1 + mu ** 2) / (1 - mu ** 2)) ** 2
for npts, R in ((200, 12.0), (400, 16.0)):
    rho = np.linspace(0, 1, npts + 1) ** 2 * R
    F0 = np.pi * np.exp(-rho / 1.2)
    res = minimize(lambda v: energy(np.concatenate([[np.pi], v, [0.0]]), rho), F0[1:-1], method="L-BFGS-B",
                   options={"maxiter": 20000, "maxfun": 10 ** 6, "ftol": 1e-14, "gtol": 1e-9})
    Fp = np.concatenate([[np.pi], res.x, [0.0]])
    Fm = 0.5 * (Fp[1:] + Fp[:-1]); rm = 0.5 * (rho[1:] + rho[:-1]); dr = np.diff(rho)
    p = (np.diff(Fp) / dr) ** 2; s = np.sin(Fm) ** 2 / rm ** 2
    w = 4 * np.pi * rm ** 2 * dr
    I0 = np.sum(w * (p + 2 * s) ** 2); I1 = np.sum(w * (p + 2 * s) ** 2 / 3); I2 = np.sum(w * (s ** 2 + 2 * s * (p - s) / 3 + (p - s) ** 2 / 5))
    Ts = I1 / I2
    IP = lambda t: I0 - 2 * t * I1 + t ** 2 * I2
    print(f"  Gitter {npts}, R={R}: E_Igel = 4 pi * {energy(Fp, rho):.4f};  Int S_ges^2 = {I0:.3f}, Int S_ges <S_i> = {I1:.3f}, Int <S_i^2> = {I2:.3f}")
    print(f"    T* = {Ts:.4f} (tau*^2 = {Ts - 1:.4f});  I_P(T*) = {IP(Ts):.3f};  I_P(3) = {IP(3.0):.3f};  HC-Wert T = {THC:.4f}: I_P = {IP(THC):.3f} = {IP(THC) / IP(Ts):.2f} x Minimum")
print(f"  HC: mu = {mu:.4f}, tau^2 = {THC - 1:.4f}, T = 1/cos^2(2 theta) = {THC:.4f}; liegt unter der Schranke 5/3 = {5/3:.4f}")
print("  Energie in erster Ordnung: Delta E = eta2 f^4 I_P / l, l = Laengeneinheit von k291 (proportional sqrt(c1)/f)")
