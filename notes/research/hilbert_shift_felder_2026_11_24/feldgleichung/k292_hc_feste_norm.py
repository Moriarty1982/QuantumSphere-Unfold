"""k292 (Erkundung, nicht blind): Lesart A oder B? Liefert der HC die feste Amplitude f bei HS(1)?
HC = quasikonforme Projektion C(f) = (f + Jf)/2 mit Beltrami-Koeffizient mu = beta_sym^2 und Dilatation K = gamma_L
(thm:hc-quasiconformal). HS(1)-Familie aus k253: psi = a e^{iwt} + b e^{-iwt}.
Aufruf: python k292_hc_feste_norm.py > k292_out.txt
"""
import sympy as sp

t, w = sp.symbols("t omega", real=True)
a, b = sp.symbols("a b", positive=True)
lam, gam = sp.symbols("lambda gamma_L", positive=True)

print("== 1  Die Ellipse als quasikonforme Abbildung z -> a z + b conj(z) ==")
zx, zy = sp.symbols("x y", real=True)
fz = a * (zx + sp.I * zy) + b * (zx - sp.I * zy)
dz = (sp.diff(fz, zx) - sp.I * sp.diff(fz, zy)) / 2; dzb = (sp.diff(fz, zx) + sp.I * sp.diff(fz, zy)) / 2
mu = sp.simplify(dzb / dz)
print("  Beltrami-Koeffizient mu =", mu, ";  K = (1+mu)/(1-mu) =", sp.simplify((1 + mu) / (1 - mu)), "= Verhaeltnis der Halbachsen")
print("  mit mu = beta_sym^2 = (gamma_L - 1)/(gamma_L + 1):  K =", sp.simplify((1 + (gam - 1) / (gam + 1)) / (1 - (gam - 1) / (gam + 1))))
g = 1.8644; m = (g - 1) / (g + 1)
print(f"  Zahlen: gamma_L = {g}, mu = b/a = {m:.5f}, beta_sym = {m ** 0.5:.4f}")
print("  Skalierung psi -> lambda psi: mu bleibt", sp.simplify((lam * b) / (lam * a)), "(der HC legt die Form fest, nicht die Groesse)")
print("  C ist linear: C(lambda f) - lambda C(f) = 0 fuer jede Involution J; eine lineare Abbildung kann keine Amplitude auszeichnen.")

print("\n== 2  Norm auf der HS(1)-Ellipse ==")
psi = [(a + b) * sp.cos(w * t), (a - b) * sp.sin(w * t)]
N = sp.simplify(psi[0] ** 2 + psi[1] ** 2)
print("  N(psi) =", sp.simplify(sp.expand_trig(N).rewrite(sp.cos)), " = a^2 + b^2 + 2ab cos(2wt) ?", sp.simplify(N - (a ** 2 + b ** 2 + 2 * a * b * sp.cos(2 * w * t))) == 0)
print("  Schwankung: zwischen", sp.factor(N.subs(t, sp.pi / (2 * w))), "und", sp.factor(N.subs(t, 0)),
      "; Zeitmittel:", sp.simplify(sp.integrate(N, (t, 0, 2 * sp.pi / w)) * w / (2 * sp.pi)))
print("  feste Norm verlangt 2ab = 0, also mu = 0 und K = 1 (gamma_L = 1). Mit gamma_L = 1,8644 schwankt N um den Faktor K^2 =", round(g ** 2, 4))

print("\n== 3  Lesart B mit verformtem Kreis (Feld auf der Ellipse festgehalten) ==")
th = sp.Function("theta")(t)
e = [(a + b) * sp.cos(th), (a - b) * sp.sin(th)]
Lk = sp.simplify(sp.Rational(1, 2) * sum(sp.diff(c, t) ** 2 for c in e))
EL = sp.simplify(sp.diff(Lk, th) - sp.diff(sp.diff(Lk, sp.diff(th, t)), t))
res = sp.simplify(EL.subs(sp.diff(th, t, 2), 0).subs(sp.diff(th, t), w).subs(th, w * t))
print("  L = 1/2 |psi'|^2 auf der Ellipse; Euler-Lagrange-Rest fuer die harmonische Bewegung theta = w t:", sp.factor(res))
print("  => die Regel psi'' = -w^2 psi loest die Gleichung des festgehaltenen Felds nur fuer ab = 0.")

print("\n== 4  HS(2): der gegenlaeufige Anteil im Anhang ==")
def qmul(p, q):
    a0, a1, a2, a3 = p; b0, b1, b2, b3 = q
    return [a0 * b0 - a1 * b1 - a2 * b2 - a3 * b3, a0 * b1 + a1 * b0 + a2 * b3 - a3 * b2,
            a0 * b2 - a1 * b3 + a2 * b0 + a3 * b1, a0 * b3 + a1 * b2 - a2 * b1 + a3 * b0]
E = lambda s: [sp.cos(s), sp.sin(s), 0, 0]                       # e^{i s}
qi, qj = [0, 1, 0, 0], [0, 0, 1, 0]
sc = lambda c, q: [c * v for v in q]
add = lambda p, q: [u + v for u, v in zip(p, q)]
psi2 = add(sc(a, E(w * t)), qmul(sc(b, qj), E(-w * t)))           # a e^{iwt} + (b j) e^{-iwt}
alt = qmul(E(w * t), add(sc(a, [1, 0, 0, 0]), sc(b, qj)))         # e^{iwt} (a + b j)
print("  psi = a e^{iwt} + (b j) e^{-iwt} =", [sp.simplify(c) for c in psi2])
print("  gleich e^{iwt}(a + b j)?", all(sp.simplify(u - v) == 0 for u, v in zip(psi2, alt)))
print("  N(psi) =", sp.simplify(sum(c ** 2 for c in psi2)), " (fest, gleich dem Zeitmittel aus 2)")
d2 = [sp.diff(c, t) for c in psi2]
print("  Regel erster Ordnung psi' - w i psi =", [sp.simplify(u - v) for u, v in zip(d2, sc(w, qmul(qi, psi2)))], " (beide Anteile drehen jetzt gleichsinnig von links)")
dot = lambda p, q: sp.simplify(sum(u * v for u, v in zip(p, q)))
print("  Ladung der Linksdrehung  <psi', i psi> =", sp.factor(dot(d2, qmul(qi, psi2))))
print("  Ladung der Rechtsdrehung <psi', psi i> =", sp.factor(dot(d2, qmul(psi2, qi))), " (die Ladung w(a^2 - b^2) von HS(1))")
sh = [psi2[0] + psi2[2], psi2[1] - psi2[3]]
print("  Schatten in C (psi_1 + conj(chi)):", [sp.simplify(c) for c in sh], " = Ellipse aus k253")
ct = sp.simplify((a ** 2 - b ** 2) / (a ** 2 + b ** 2))
print("  Punkt auf der Hopf-Sphaere: cos(Breite) =", ct, "; a = b ist der Aequator (HS(0)), b = 0 der Pol")
import math
print(f"  mit mu = b/a = {m:.5f}: cos = {(1 - m * m) / (1 + m * m):.4f}, Winkel vom Pol = {math.degrees(math.acos((1 - m * m) / (1 + m * m))):.2f} Grad (nur ausgerechnet, keine Zuordnung)")
