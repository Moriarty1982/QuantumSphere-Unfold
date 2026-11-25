"""k291 (Erkundung, nicht blind): Ansatz k290 ohne Massenterm auf HS(0) und HS(1). Wo entsteht Masse zuerst?
A  masselose Welle: die Ellipse aus k253 an jedem Ort, omega = |k| statt omega = m
B  Feld fester Norm (Sphaere S^(2^n - 1)): K1 = 0 auf S^1, K1 = Skyrme-Term auf S^3
C  Derrick-Skalierung in D Raumdimensionen
D  Igel-Loesung auf S^3: Ruheenergie aus Amplitude f und Koeffizient c1 (numerisch)
E  geeichte U(1) bei fester Norm: Eichfeldmasse e*f
Aufruf: python k291_masse_zuerst.py > k291_out.txt
"""
import numpy as np
import sympy as sp
from scipy.optimize import minimize
np.random.seed(291)

t, x, y, z, w, k = sp.symbols("t x y z omega k", real=True)
a, b = sp.symbols("a b", positive=True)

print("== A  masselose Welle (Box psi = 0, kein Massenterm) ==")
ph = w * t - k * x
psi = [(a + b) * sp.cos(ph), (a - b) * sp.sin(ph)]              # a e^{i ph} + b e^{-i ph}
box = [sp.simplify(sp.diff(c, t, 2) - sp.diff(c, x, 2)) for c in psi]
print("  Box psi =", box, " => null genau fuer", sp.solve(sp.simplify(box[0] / psi[0]), w))
print("  an festem Ort: psi'' + omega^2 psi =", [sp.simplify(sp.diff(c, t, 2) + w ** 2 * c) for c in psi], "(Regel aus k253, omega = |k|)")
print("  HS(0), a = b:", [c.subs(b, a) for c in psi], " (reelle Welle, lineare Polarisation)")
print("  Ladungsdichte psi0 psi1' - psi1 psi0' =", sp.factor(sp.simplify(psi[0] * sp.diff(psi[1], t) - psi[1] * sp.diff(psi[0], t))),
      " (Drehsinn, null bei a = b)")

print("\n== B  Feld fester Norm ==")
th = sp.Function("theta")(x, y, z)
U1 = [sp.cos(th), sp.sin(th)]
d = lambda v, s: [sp.diff(c, s) for c in v]
dot = lambda u, v: sum(p * q for p, q in zip(u, v))
K1 = lambda u, v: sp.simplify(dot(u, u) * dot(v, v) - dot(u, v) ** 2)
print("  S^1 (HS(1)): K1(d_x psi, d_y psi) =", K1(d(U1, x), d(U1, y)), " (Zielraum eindimensional, keine Flaeche)")
print("  S^1: kinetischer Term = 1/2 f^2 (d theta)^2, also ein masseloses Phasenfeld:",
      sp.simplify(dot(d(U1, x), d(U1, x))))

def qmul(p, q):
    a0, a1, a2, a3 = p; b0, b1, b2, b3 = q
    return [a0 * b0 - a1 * b1 - a2 * b2 - a3 * b3, a0 * b1 + a1 * b0 + a2 * b3 - a3 * b2,
            a0 * b2 - a1 * b3 + a2 * b0 + a3 * b1, a0 * b3 + a1 * b2 - a2 * b1 + a3 * b0]
qc = lambda p: [p[0], -p[1], -p[2], -p[3]]
r = sp.sqrt(x ** 2 + y ** 2 + z ** 2); F = sp.Function("F")
U = [sp.cos(F(r)), sp.sin(F(r)) * x / r, sp.sin(F(r)) * y / r, sp.sin(F(r)) * z / r]      # Igel
dU = [d(U, s) for s in (x, y, z)]
L = [qmul(qc(U), v) for v in dU]                                                           # Stroeme
pt = {y: 0, z: 0}                                                                          # Kugelsymmetrie: Punkt (x,0,0)
ev = lambda e: sp.simplify(e.subs(pt).doit().subs(sp.Abs(x), x).subs(sp.sqrt(x ** 2), x))
E2 = sum(dot(v, v) for v in dU)
E4 = sum(dot(dU[i], dU[i]) * dot(dU[j], dU[j]) - dot(dU[i], dU[j]) ** 2 for i in range(3) for j in range(i + 1, 3))
com = lambda p, q: [m - n for m, n in zip(qmul(p, q), qmul(q, p))]
E4J = sum(dot(com(L[i], L[j]), com(L[i], L[j])) for i in range(3) for j in range(i + 1, 3))
e2, e4, e4j = ev(E2), ev(E4), ev(E4J)
print("  S^3 (HS(2)), Igel, bei r = x:  sum N(d_i U) =", e2)
print("                               sum K1(d_i U, d_j U) =", sp.factor(e4))
print("  Kommutator der Stroeme (Skyrme-Term) = 4 * K1 ?", sp.simplify(e4j - 4 * e4) == 0)
Bd = sp.Matrix([[L[i][j + 1] for j in range(3)] for i in range(3)]).det()
print("  Windungsdichte det(L) =", sp.factor(ev(Bd)), " => Windungszahl = -(1/2 pi^2) * 4 pi * Integral = [F - sin(2F)/2]/pi von 0 bis unendlich")

print("\n== C  Derrick-Skalierung x -> x/s in D Raumdimensionen ==")
s, D, A2, A4, A0 = sp.symbols("s D E2 E4 E0", positive=True)
E = s ** (2 - D) * A2 + s ** (4 - D) * A4 + s ** (-D) * A0
print("  E(s) =", E, ";  dE/ds bei s=1:", sp.diff(E, s).subs(s, 1))
for DD in (1, 2, 3):
    print(f"  D={DD}: stationaer verlangt {sp.Eq(sp.diff(E, s).subs({s: 1, D: DD}), 0)}")
print("  D=3: E4 = E2 + 3 E0. Ohne Term vierter Ordnung in den Ableitungen (E4 = 0) gibt es keine ruhende, lokalisierte Loesung.")

print("\n== D  Igel auf S^3: E = 4 pi f sqrt(c1) * I,  I = Int rho^2 [ 1/2 (F'^2 + 2 s^2/rho^2) + s^2/rho^2 (2 F'^2 + s^2/rho^2) ] ==")
def energy(Fv, rho):
    Fm = 0.5 * (Fv[1:] + Fv[:-1]); rm = 0.5 * (rho[1:] + rho[:-1]); dF = np.diff(Fv) / np.diff(rho)
    s2 = np.sin(Fm) ** 2 / rm ** 2
    e2 = 0.5 * (dF ** 2 + 2 * s2); e4 = s2 * (2 * dF ** 2 + s2)
    return np.sum(rm ** 2 * (e2 + e4) * np.diff(rho)), np.sum(rm ** 2 * e2 * np.diff(rho)), np.sum(rm ** 2 * e4 * np.diff(rho))
for npts, R in ((200, 12.0), (400, 16.0)):
    rho = np.linspace(0, 1, npts + 1) ** 2 * R
    F0 = np.pi * np.exp(-rho / 1.2)
    f = lambda v: energy(np.concatenate([[np.pi], v, [0.0]]), rho)[0]
    res = minimize(f, F0[1:-1], method="L-BFGS-B", options={"maxiter": 20000, "maxfun": 10 ** 6, "ftol": 1e-14, "gtol": 1e-9})
    I, I2, I4 = energy(np.concatenate([[np.pi], res.x, [0.0]]), rho)
    bound = 6 * np.sqrt(2) * np.pi ** 2
    print(f"  Gitter {npts}, R={R}: I = {I:.4f}, I2 = {I2:.4f}, I4 = {I4:.4f} (Derrick: I2 = I4), "
          f"E = 4 pi I = {4 * np.pi * I:.3f} f sqrt(c1), Schranke 6 sqrt(2) pi^2 = {bound:.3f}, Verhaeltnis {4 * np.pi * I / bound:.4f}")
print("  Literaturwert des Verhaeltnisses fuer den Skyrme-Igel: 1,2315")

print("\n== E  geeichte U(1) bei fester Norm f (HS(1)) ==")
e, f, A, dth = sp.symbols("e f A dtheta", real=True)
print("  1/2 f^2 (d theta + e A)^2, Eichung theta = 0:", sp.expand(sp.Rational(1, 2) * f ** 2 * (dth + e * A) ** 2).subs(dth, 0),
      " => m_A = e f; ohne feste Norm (f = 0 im Vakuum): m_A = 0")

print("\n== F  Homotopie (Standard, nicht gerechnet): pi_3 der Zielsphaere ==")
print("  S^0: 0   S^1: 0   S^3: Z   S^7: 0   => Knoten mit Windungszahl in drei Raumdimensionen nur fuer S^3, also HS(2)")

print("\n== G  Protomasse bei HS(1): invariante Masse E^2 - P^2 einer masselosen Welle ==")
A_, B_ = sp.symbols("A B", positive=True)
p1, p2 = w * t - k * x, w * t + k * x
psi = [A_ * sp.cos(p1) + B_ * sp.cos(p2), A_ * sp.sin(p1) + B_ * sp.sin(p2)]      # gleicher Drehsinn, entgegengesetzte Laufrichtung
avg = lambda e: sp.simplify(sp.integrate(sp.integrate(sp.expand(e), (x, 0, 2 * sp.pi / k)), (t, 0, 2 * sp.pi / w)) * k * w / (4 * sp.pi ** 2))
Ed = avg(sum(sp.Rational(1, 2) * (sp.diff(c, t) ** 2 + sp.diff(c, x) ** 2) for c in psi)).subs(w, k)
Pd = avg(-sum(sp.diff(c, t) * sp.diff(c, x) for c in psi)).subs(w, k)
print("  Energiedichte:", sp.factor(Ed), " Impulsdichte:", sp.factor(Pd), " E^2 - P^2 =", sp.factor(Ed ** 2 - Pd ** 2))
print("  => eine einzelne laufende Welle (B = 0) ist lichtartig; erst zwei Laufrichtungen geben E^2 - P^2 > 0.")
print("     Diese Protomasse ist nicht gebunden: nach C (Derrick, E4 = 0 auf S^1 und fuer die freie Welle) zerlaeuft sie.")

print("\n== H  HS(2) mit fester Norm f: SU(2) links und U(1) rechts geeicht ==")
g_, gp, f_ = sp.symbols("g gprime f", positive=True)
W1, W2, W3, Bf = sp.symbols("W1 W2 W3 B", real=True)
vac = [f_, 0, 0, 0]
Wq = [0, g_ / 2 * W1, g_ / 2 * W2, g_ / 2 * W3]; Bq = [0, 0, 0, gp / 2 * Bf]
Dv = [m - n for m, n in zip(qmul(Wq, vac), qmul(vac, Bq))]
M2 = sp.expand(sp.Rational(1, 2) * dot(Dv, Dv))
print("  1/2 N(W psi - psi B) im Vakuum psi = f:", sp.factor(M2))
Mm = sp.hessian(M2, (W1, W2, W3, Bf))
print("  Massenquadrate:", {sp.factor(k_): v for k_, v in Mm.eigenvals().items()})
print("  => ein Eichfeld bleibt masselos (g' W3 + g B), drei werden massiv; m_W^2/m_Z^2 = g^2/(g^2+g'^2)")
print("  zum Vergleich HS(1) allein (E): das eine Eichfeld wird massiv, m_A = e f, es bleibt kein masseloses uebrig.")
