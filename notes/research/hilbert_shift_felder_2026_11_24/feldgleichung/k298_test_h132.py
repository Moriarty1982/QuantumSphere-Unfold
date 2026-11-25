"""k298: Test H132 (Vorab-Notiz notes/research/predictions/Vorab_Notiz_H132_Eichfelder_HC_Richtung.md).
Eichfelder auf der HC-Richtung psi0 = f (cos th + sin th j), tan th = mu.
A  U(1) links x U(1) rechts (Symmetrie des HC-Potentials): Massenmatrix, Determinante, Verhaeltnis
B  SU(2) links x U(1) rechts (k291 Punkt 6) auf demselben Vakuum; Invarianz des HC-Potentials
C  Schleifen-Skala mit Eichfeldern (Gildener-Weinberg), ohne Kriterium
Aufruf: python k298_test_h132.py > k298_out.txt
"""
import sympy as sp

def qmul(p, q):
    a0, a1, a2, a3 = p; b0, b1, b2, b3 = q
    return [a0 * b0 - a1 * b1 - a2 * b2 - a3 * b3, a0 * b1 + a1 * b0 + a2 * b3 - a3 * b2,
            a0 * b2 - a1 * b3 + a2 * b0 + a3 * b1, a0 * b3 + a1 * b2 - a2 * b1 + a3 * b0]
dot = lambda u, v: sum(p * q for p, q in zip(u, v))
f, th, mu, eta = sp.symbols("f theta mu eta", positive=True)
gL, gR, g, gp = sp.symbols("g_L g_R g gprime", positive=True)
L, R, W1, W2, W3, Bf = sp.symbols("L R W1 W2 W3 B", real=True)
psi0 = [f * sp.cos(th), 0, f * sp.sin(th), 0]                # psi1 = f cos th, chi = f sin th
qi = [0, 1, 0, 0]
A0, B0 = f ** 2 * sp.cos(th) ** 2, f ** 2 * sp.sin(th) ** 2

print("== A  U(1) links x U(1) rechts ==")
Dv = [gL * L * p - gR * R * q for p, q in zip(qmul(qi, psi0), qmul(psi0, qi))]
M2 = sp.expand(sp.Rational(1, 2) * dot(Dv, Dv))
Mm = sp.hessian(M2, (L, R)).applyfunc(sp.simplify)
print("  Massenmatrix in (L, R):", Mm.tolist())
print("  Vergleich mit dem Ueberschlag [[gL^2 f^2, -+ gL gR (A-B)], ...]: Diagonale", sp.simplify(Mm[0, 0] - gL ** 2 * f ** 2) == 0, sp.simplify(Mm[1, 1] - gR ** 2 * f ** 2) == 0,
      "; Nebendiagonale / (gL gR (A - B)) =", sp.simplify(Mm[0, 1] / (gL * gR * (A0 - B0))))
det = sp.factor(sp.simplify(Mm.det()))
print("  K-a: Determinante =", det, " = 4 gL^2 gR^2 A B ?", sp.simplify(det - 4 * gL ** 2 * gR ** 2 * A0 * B0) == 0)
ev = [sp.simplify(e) for e in Mm.eigenvals()]
print("  Eigenwerte:", ev)
c2 = sp.symbols("c", real=True)                              # c = cos 2 theta = (1 - mu^2)/(1 + mu^2)
tr, dt = gL ** 2 + gR ** 2, 4 * gL ** 2 * gR ** 2 * (1 - c2 ** 2) / 4
ratio = sp.simplify(((tr - sp.sqrt(tr ** 2 - 4 * dt)) / (tr + sp.sqrt(tr ** 2 - 4 * dt))))
print("  K-b: m-^2/m+^2 mit c = cos 2 theta:", ratio)
print("    gL = gR:", sp.simplify(ratio.subs(gR, gL)), "; fuer mu < 1 also", sp.simplify(((1 - c2) / (1 + c2)).subs(c2, (1 - mu ** 2) / (1 + mu ** 2))), ";", " mit c = (1-mu^2)/(1+mu^2):", sp.simplify(ratio.subs(gR, gL).subs(c2, (1 - mu ** 2) / (1 + mu ** 2))))
print("    Ableitung nach gR bei gR = 2 gL, c = 1/2 (ungleich null heisst: haengt an den Kopplungen):", sp.simplify(sp.diff(ratio, gR).subs({gR: 2 * gL, c2: sp.Rational(1, 2)})))
ee = gL * gR / sp.sqrt(gL ** 2 + gR ** 2)
lam_minus = sp.simplify((tr - sp.sqrt(tr ** 2 - 4 * dt)) / 2).subs(c2, (1 - mu ** 2) / (1 + mu ** 2))
mlight = sp.simplify(sp.series(lam_minus, mu, 0, 4).removeO())
print("  leichtes Feld fuer kleines mu (in Einheiten f^2): m-^2 =", sp.factor(mlight), " ; Vergleich 4 e^2 mu^2 mit e = gL gR/sqrt(gL^2+gR^2):",
      sp.simplify(sp.series(mlight - 4 * ee ** 2 * mu ** 2, mu, 0, 4).removeO()) == 0 or sp.factor(sp.simplify(mlight / (4 * ee ** 2 * mu ** 2))))
print("  exakt fuer gL = gR = g: m+^2 = g^2 f^2 (1 + c) = 2 g^2 f^2/(1 + mu^2), m-^2 = 2 g^2 f^2 mu^2/(1 + mu^2)")
vec0 = Mm.subs(th, 0).nullspace()
print("  bei theta = 0 (kein Anhang) masselos:", [list(v.T) for v in vec0], " (Kombination, unter der psi1 neutral ist)")

print("\n== B  SU(2) links x U(1) rechts auf demselben Vakuum ==")
Wq = [0, g / 2 * W1, g / 2 * W2, g / 2 * W3]; Bq = [0, gp / 2 * Bf, 0, 0]
Dv2 = [p - q for p, q in zip(qmul(Wq, psi0), qmul(psi0, Bq))]
M4 = sp.hessian(sp.expand(sp.Rational(1, 2) * dot(Dv2, Dv2)), (W1, W2, W3, Bf)).applyfunc(sp.simplify)
print("  Massenquadrate:", {sp.factor(sp.simplify(k)): v for k, v in M4.eigenvals().items()}, " (haengen nicht von theta ab)")
print("  masselose Richtung:", [list(sp.simplify(v.T)) for v in M4.nullspace()])
x = sp.symbols("x0:4", real=True)
V = eta * ((x[2] ** 2 + x[3] ** 2) - mu ** 2 * (x[0] ** 2 + x[1] ** 2)) ** 2
for name, q in (("i", [0, 1, 0, 0]), ("j", [0, 0, 1, 0]), ("k", [0, 0, 0, 1])):
    dx = qmul(q, list(x))
    print(f"  Aenderung von V unter der Linksdrehung um {name}:", sp.factor(sp.simplify(sum(sp.diff(V, s) * d for s, d in zip(x, dx)))))

print("\n== C  Schleifen-Skala mit Eichfeldern (ohne Kriterium) ==")
phi, M = sp.symbols("phi M", positive=True)
mH2 = 8 * eta * mu ** 2
c = (1 - mu ** 2) / (1 + mu ** 2)
mp, mm = g ** 2 * (1 + c), g ** 2 * (1 - c)                 # gL = gR = g, in Einheiten f^2
S = sp.simplify(mH2 ** 2 + 3 * (mp ** 2 + mm ** 2))
print("  gL = gR = g: Summe m^4/f^4 = m_H^4 + 3 (m+^4 + m-^4) =", sp.factor(S))
print("  Masse der Groessenmode: m_s^2 = Summe/(8 pi^2) f^2 =", sp.factor(S / (8 * sp.pi ** 2)), "* f^2")
gLv = sp.Float("1.8644"); muv = (gLv - 1) / (gLv + 1)
num = {mu: muv}
print(f"  Zahlen mit mu = {muv:.4f}: m-/m+ = {sp.sqrt(mm/mp).subs(num):.4f};  m+^2 = {(mp/g**2).subs(num):.4f} g^2 f^2;  m-^2 = {(mm/g**2).subs(num):.4f} g^2 f^2;"
      f"  m_H^2 = {mH2.subs(num)/eta:.4f} eta f^2")
print(f"  m_s^2/f^2 = {sp.N((mH2**2/(8*sp.pi**2)).subs(num)/eta**2, 4)} eta^2 + {sp.N((3*(mp**2+mm**2)/(8*sp.pi**2)).subs(num)/g**4, 4)} g^4")
