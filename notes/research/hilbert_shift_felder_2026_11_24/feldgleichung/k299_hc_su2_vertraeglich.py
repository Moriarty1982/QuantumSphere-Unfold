"""k299 (Erkundung, nicht blind): Fassungen des HC, die mit SU(2) links x U(1) rechts vertraeglich sind.
1  Was ist unter SU(2) links invariant? Potential nur V(N); der Strom J = conj(psi) D psi mit J_i und |J_senkrecht|
2  Der Strom auf der Loesung psi = e^{iwt}(a + b j): J_i = w(a^2 - b^2), |J_senkrecht| = 2 a b w
3  Fassung S (Stauchung): Zusatzterm xi (J_i)^2 / (2 N): Eichfeldmassen, masseloses Feld, rho-Parameter, Energie der Drehung
4  Fassung F (Form der Bewegung): eta2 (J_s^2 - t^2 J_i^2)^2 / N^2: keine Eichfeldmassen, Loesung mit HC-Verhaeltnis exakt
5  Zahlen: rho fuer naheliegende Zuordnungen von xi; Skala aus Eichfeld-Schleifen
Aufruf: python k299_hc_su2_vertraeglich.py > k299_out.txt
"""
import sympy as sp

def qmul(p, q):
    a0, a1, a2, a3 = p; b0, b1, b2, b3 = q
    return [a0 * b0 - a1 * b1 - a2 * b2 - a3 * b3, a0 * b1 + a1 * b0 + a2 * b3 - a3 * b2,
            a0 * b2 - a1 * b3 + a2 * b0 + a3 * b1, a0 * b3 + a1 * b2 - a2 * b1 + a3 * b0]
qc = lambda p: [p[0], -p[1], -p[2], -p[3]]
dot = lambda u, v: sum(p * q for p, q in zip(u, v))
x = list(sp.symbols("x0:4", real=True)); v = list(sp.symbols("v0:4", real=True))        # psi und d psi
N = dot(x, x)
J = [sp.expand(c) for c in qmul(qc(x), v)]                                                 # J = conj(psi) d psi
Ji, Js2 = J[1], J[2] ** 2 + J[3] ** 2

print("== 1  Invarianten ==")
def var(expr, dx, dv):
    return sp.simplify(sum(sp.diff(expr, s) * d for s, d in zip(x, dx)) + sum(sp.diff(expr, s) * d for s, d in zip(v, dv)))
units = {"i": [0, 1, 0, 0], "j": [0, 0, 1, 0], "k": [0, 0, 0, 1]}
A = x[0] ** 2 + x[1] ** 2; B = x[2] ** 2 + x[3] ** 2
for n, u in units.items():
    print(f"  Linksdrehung um {n}: delta N =", var(N, qmul(u, x), qmul(u, v)), ", delta (B - mu^2 A) = 0 ?", var(B - sp.Symbol("mu") ** 2 * A, qmul(u, x), qmul(u, v)) == 0,
          ", delta J =", [var(c, qmul(u, x), qmul(u, v)) for c in J])
print("  Rechtsdrehung um i: delta J_i =", var(Ji, qmul(x, units["i"]), qmul(v, units["i"])), ", delta |J_s|^2 =", var(Js2, qmul(x, units["i"]), qmul(v, units["i"])),
      ", delta J_j =", var(J[2], qmul(x, units["i"]), qmul(v, units["i"])), "(dreht in J_k)")
print("  Re J = 1/2 dN:", sp.simplify(J[0] - sum(s * d for s, d in zip(x, v))) == 0, ";  N(J) = N(psi) N(d psi):", sp.simplify(dot(J, J) - N * dot(v, v)) == 0)

print("\n== 2  Strom auf der Loesung psi = e^{iwt}(a + b j) ==")
a, b, w, t, mu = sp.symbols("a b omega t mu", positive=True)
psi = [a * sp.cos(w * t), a * sp.sin(w * t), b * sp.cos(w * t), b * sp.sin(w * t)]
Jt = [sp.simplify(c) for c in qmul(qc(psi), [sp.diff(c, t) for c in psi])]
print("  J_t =", Jt, " => J_i = w(a^2 - b^2), |J_s| = 2 a b w")
rat = sp.simplify(sp.sqrt(Jt[2] ** 2 + Jt[3] ** 2) / Jt[1]).subs(b, mu * a)
print("  |J_s|/J_i mit b = mu a:", sp.simplify(rat), ";  mit K = (1+mu)/(1-mu): (K - 1/K)/2 =", sp.simplify((((1 + mu) / (1 - mu)) - ((1 - mu) / (1 + mu))) / 2))

print("\n== 3  Fassung S: L = 1/2 N(D psi) + xi (J_i)^2/(2 N), SU(2) links (g) x U(1) rechts (g') ==")
g, gp, f, th, xi = sp.symbols("g gprime f theta xi", positive=True)
W1, W2, W3, Bf = sp.symbols("W1 W2 W3 B", real=True)
psi0 = [f * sp.cos(th), 0, f * sp.sin(th), 0]
Wq = [0, g / 2 * W1, g / 2 * W2, g / 2 * W3]; Bq = [0, gp / 2 * Bf, 0, 0]
Dv = [p - q for p, q in zip(qmul(Wq, psi0), qmul(psi0, Bq))]
J0 = qmul(qc(psi0), Dv)
Lm = sp.Rational(1, 2) * dot(Dv, Dv) + xi * J0[1] ** 2 / (2 * f ** 2)
M4 = sp.hessian(sp.expand(Lm), (W1, W2, W3, Bf)).applyfunc(sp.simplify)
evs = {sp.factor(sp.simplify(k)): m for k, m in M4.eigenvals().items()}
print("  Massenquadrate:", evs, " (unabhaengig von theta)")
print("  masselose Richtung:", [list(sp.simplify(n_.T)) for n_ in M4.nullspace()])
mW2, mZ2 = g ** 2 * f ** 2 / 4, (g ** 2 + gp ** 2) * (1 + xi) * f ** 2 / 4
print("  m_W^2 = g^2 f^2/4 und m_Z^2 = (g^2+g'^2)(1+xi) f^2/4 im Spektrum:", mW2 in evs, sp.factor(mZ2) in evs or any(sp.simplify(k - mZ2) == 0 for k in evs),
      ";  rho = m_W^2 (g^2+g'^2)/(m_Z^2 g^2) =", sp.simplify(mW2 * (g ** 2 + gp ** 2) / (mZ2 * g ** 2)))
vt = [sp.diff(c, t) for c in psi]
Jrot = qmul(qc(psi), vt)
E = sp.simplify((sp.Rational(1, 2) * dot(vt, vt) + xi * Jrot[1] ** 2 / (2 * dot(psi, psi))).subs({a: f * sp.cos(th), b: f * sp.sin(th)}))
print("  Energie der Drehung e^{iwt}(a + b j), a = f cos th, b = f sin th:", sp.factor(E), ";  dE/dth = 0 bei th =", sp.solve(sp.diff(E, th), th))

print("\n== 4  Fassung F: P = eta2 (|J_s|^2 - tau^2 J_i^2)^2 / N^2, tau = 2 mu/(1 - mu^2) ==")
tau = 2 * mu / (1 - mu ** 2)
P = (Js2 - tau ** 2 * Ji ** 2) ** 2 / N ** 2
for n, u in units.items():
    print(f"  Linksdrehung um {n}: delta P =", var(P, qmul(u, x), qmul(u, v)), end=";")
print("  Rechtsdrehung um i: delta P =", var(P, qmul(x, units["i"]), qmul(v, units["i"])))
Pv = ((J0[2] ** 2 + J0[3] ** 2) - tau ** 2 * J0[1] ** 2) ** 2 / f ** 4
print("  im Vakuum mit Eichfeldern: Grad in den Feldern =", sp.Poly(sp.expand(Pv), W1, W2, W3, Bf).total_degree(), ", zweite Ableitungen bei null alle null:",
      sp.hessian(sp.expand(Pv), (W1, W2, W3, Bf)).subs({W1: 0, W2: 0, W3: 0, Bf: 0}) == sp.zeros(4, 4), " => keine Massen, rho = 1")
Psol = sp.simplify(((Jt[2] ** 2 + Jt[3] ** 2) - tau ** 2 * Jt[1] ** 2).subs(b, mu * a))
print("  auf der Loesung mit b = mu a: |J_s|^2 - tau^2 J_i^2 =", Psol, " (doppelte Nullstelle von P: die Loesung bleibt exakt)")
print("  Abweichung b = (mu + d) a, P bis d^2:", sp.factor(sp.series(sp.simplify((((Jt[2] ** 2 + Jt[3] ** 2) - tau ** 2 * Jt[1] ** 2) ** 2 / (a ** 2 + b ** 2) ** 2).subs(b, (mu + sp.Symbol("d")) * a)), sp.Symbol("d"), 0, 3).removeO()))

print("\n== 5  Zahlen (gamma_L eingesetzt; Messwerte aus dem Gedaechtnis, nicht nachgeschlagen) ==")
gLv = 1.8644; muv = (gLv - 1) / (gLv + 1); c2 = (1 - muv ** 2) / (1 + muv ** 2)
print(f"  mu = {muv:.4f}; |J_s|/J_i = {2*muv/(1-muv**2):.4f}; J_i/|J| = cos 2 theta = {c2:.4f}")
for name, val in (("1 + xi = gamma_L^2", gLv ** 2), ("1 + xi = gamma_L", gLv), ("1 + xi = 1/gamma_L", 1 / gLv), ("1 + xi = 1/gamma_L^2", gLv ** -2),
                  ("1 + xi = 1 + mu^2", 1 + muv ** 2), ("1 + xi = 1/cos^2(2 theta)", 1 / c2 ** 2)):
    print(f"  Fassung S, {name:28s}: rho = {1/val:.4f}")
print("  gemessen: rho_0 etwa 1,0004 +- 0,0002 => |xi| unter etwa 0,001; keine der Zuordnungen passt")
gv, gpv, fv = 0.652, 0.357, 246.0
ms = (3 * (2 * gv ** 4 + (gv ** 2 + gpv ** 2) ** 2) / (128 * sp.pi ** 2)) ** 0.5 * fv
print(f"  Fassung F, Skala nur aus V(N) und Eichfeld-Schleifen: m_s^2 = 3 (2 g^4 + (g^2+g'^2)^2) f^2/(128 pi^2); mit g = {gv}, g' = {gpv}, f = {fv:.0f} GeV: m_s = {float(ms):.1f} GeV")
