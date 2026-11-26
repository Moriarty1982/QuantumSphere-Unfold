"""k350 (Test H159, teilweise nicht blind): Lambda im Photon-Frame als Superposition, HC am Photonpunkt.
Vorab-Notiz: notes/research/predictions/Vorab_Notiz_H159_Lambda_Photon_Superposition.md
1  Tausch J: z -> i conj(z) auf z = a e^{i phi} + b e^{-i phi}; Fixpunkte; C = (1 + J)/2
2  Netto und Brutto: Paritaet der quadratischen Groessen unter J
3  Suche nach K^5 = gamma_L^5 in den Verhaeltnissen (vorab festgelegter Suchraum)
4  HC am Photon: (a) Fassung F bei mu -> 1, (b) Massenmatrix H132 Stufe A bei 45 Grad, (c) J-symmetrisches HC-Potential
Aufruf: python k350_test_h159.py > k350_out.txt
"""
import itertools
import sympy as sp

GL = sp.Rational(186444, 100000)          # gamma_L eingesetzt (OP1), Wert des Bestands 1,86444

def qmul(p, q):
    a0, a1, a2, a3 = p; b0, b1, b2, b3 = q
    return [a0 * b0 - a1 * b1 - a2 * b2 - a3 * b3, a0 * b1 + a1 * b0 + a2 * b3 - a3 * b2,
            a0 * b2 - a1 * b3 + a2 * b0 + a3 * b1, a0 * b3 + a1 * b2 - a2 * b1 + a3 * b0]
qc = lambda p: [p[0], -p[1], -p[2], -p[3]]
dot = lambda u, v: sum(p * q for p, q in zip(u, v))

print("== 1  Tausch J: z -> i conj(z) ==")
ar, ai, br, bi, phi = sp.symbols("a_r a_i b_r b_i phi", real=True)
ac, bc = ar + sp.I * ai, br + sp.I * bi
z = lambda p, q: p * sp.exp(sp.I * phi) + q * sp.exp(-sp.I * phi)
Jab = lambda p, q: (sp.I * sp.conjugate(q), sp.I * sp.conjugate(p))        # Koeffizienten von J z
print("  J z - z(i conj b, i conj a) =", sp.simplify(sp.I * sp.conjugate(z(ac, bc)) - z(*Jab(ac, bc))), " => (a, b) -> (i conj b, i conj a)")
print("  J^2 = 1:", [sp.simplify(c - d) for c, d in zip(Jab(*Jab(ac, bc)), (ac, bc))])
Ca, Cb = [(p + q) / 2 for p, q in zip((ac, bc), Jab(ac, bc))]
print("  C = (1 + J)/2: C^2 - C =", [sp.simplify(c - d) for c, d in zip(((Ca + Jab(Ca, Cb)[0]) / 2, (Cb + Jab(Ca, Cb)[1]) / 2), (Ca, Cb))],
      ";  |C a|^2 - |C b|^2 =", sp.simplify(sp.expand(Ca * sp.conjugate(Ca) - Cb * sp.conjugate(Cb))), " => Bild von C: |a| = |b| (Linie, mu = 1)")
print("  Rang von C als reell-lineare Abbildung auf (a_r, a_i, b_r, b_i):",
      sp.Matrix([[sp.diff(e, s) for s in (ar, ai, br, bi)] for e in (sp.re(Ca), sp.im(Ca), sp.re(Cb), sp.im(Cb))]).rank(), "von 4")
zfix = sp.simplify(sp.expand(z(Ca, Cb) * sp.exp(-sp.I * sp.pi / 4), complex=True))
print("  Im(e^{-i pi/4} C z) =", sp.simplify(sp.im(zfix)), " => C z liegt auf der 45-Grad-Linie (Fixpunktmenge, theta = pi/4 wie H149)")
print("  |mu| unter J: |b/a| ->", sp.Abs(Jab(ac, bc)[1] / Jab(ac, bc)[0]).subs({ai: 0, bi: 0}), "(fuer reelle a, b): mu -> 1/mu wie k297")

print("\n== 2  Netto und Brutto: Paritaet unter J (a <-> b, reelle Amplituden) ==")
a, b, w, mu, f, eta = sp.symbols("a b omega mu f eta", positive=True)
t = sp.Symbol("t", real=True)
psi = [a * sp.cos(w * t), a * sp.sin(w * t), b * sp.cos(w * t), b * sp.sin(w * t)]
vt = [sp.diff(c, t) for c in psi]
Jt = [sp.simplify(c) for c in qmul(qc(psi), vt)]
quant = {
    "Norm (Zeitmittel) a^2 + b^2": a ** 2 + b ** 2,
    "Ladung Q/omega = a^2 - b^2 = J_i/omega": sp.simplify(Jt[1] / w),
    "|J_senkrecht|/omega = 2ab": sp.simplify(sp.sqrt(Jt[2] ** 2 + Jt[3] ** 2) / w),
    "Energie der Drehung 1/2 N(psi_t)": sp.simplify(dot(vt, vt) / 2),
    "K1 = Q^2": sp.simplify(Jt[1] ** 2),
    "grosse Halbachse^2 (a + b)^2": (a + b) ** 2,
    "kleine Halbachse^2 (a - b)^2": (a - b) ** 2,
}
sw = lambda e: e.subs({a: b, b: a}, simultaneous=True)
for n, e in quant.items():
    par = "gerade" if sp.simplify(sw(e) - e) == 0 else ("UNGERADE" if sp.simplify(sw(e) + e) == 0 else "keine")
    print(f"  {n:42s}: {str(sp.factor(e)):28s} Paritaet {par:9s} bei a = b: {sp.simplify(e.subs(b, a))}")
print("  Einzige J-ungerade Groesse: die Ladung. Anteile +omega a^2 und -omega b^2, bei P gleich gross, Summe null, Verhaeltnis der Betraege 1.")
print("  Im Materie-Zustand b = mu a: Verhaeltnis der Anteile a^2/b^2 = mu^-2 =", sp.nsimplify(1 / ((GL - 1) / (GL + 1)) ** 2).evalf(6))

print("\n== 3  Suche nach K^5 (K = (1+mu)/(1-mu) = gamma_L) ==")
K = (1 + mu) / (1 - mu)
mu0 = sp.Symbol("mu0", positive=True)       # Wert im HC-Potential (Materie)
A, B, N_ = a ** 2, b ** 2, a ** 2 + b ** 2
tau = 2 * mu0 / (1 - mu0 ** 2)
terms = dict(quant)
terms.pop("Energie der Drehung 1/2 N(psi_t)")
terms.update({
    "V_HC = (B - mu0^2 A)^2 (k297, mu0 = mu_M)": (B - mu0 ** 2 * A) ** 2,
    "V_sym = (B - A)^2 (mu0 = 1)": (B - A) ** 2,
    "Fassung F: (Js^2 - tau^2 Ji^2)^2/N^2 (k299)": ((2 * a * b) ** 2 - tau ** 2 * (A - B) ** 2) ** 2 / N_ ** 2,
    "Fassung S: Ji^2/N (k299)": (A - B) ** 2 / N_,
})
states = {
    "M": {"gleiches f": {a: f / sp.sqrt(1 + mu ** 2), b: mu * f / sp.sqrt(1 + mu ** 2)}, "gleiches a": {b: mu * a}, "gleiche Flaeche": {a: f / sp.sqrt(1 - mu ** 2), b: mu * f / sp.sqrt(1 - mu ** 2)}},
    "P": {"gleiches f": {a: f / sp.sqrt(2), b: f / sp.sqrt(2)}, "gleiches a": {b: a}},
    "R": {"gleiches f": {a: f, b: 0}, "gleiches a": {b: 0}, "gleiche Flaeche": {a: f, b: 0}},
}
muM = (GL - 1) / (GL + 1)
hits, rows = [], []
for n, e in terms.items():
    for other in ("P", "R"):
        for norm in states[other]:
            if norm not in states["M"]:
                continue
            num = sp.simplify(e.subs(states[other][norm], simultaneous=True).subs(mu0, mu))
            den = sp.simplify(e.subs(states["M"][norm], simultaneous=True).subs(mu0, mu))
            if den == 0 or num == 0:
                rows.append((n, other, norm, "0" if num == 0 else "unendlich", None)); continue
            r = sp.simplify(num / den)
            val = float(r.subs(mu, muM))
            expo = sp.log(abs(val)) / sp.log(float(GL)) if val > 0 else None
            for sgn in (1, -1):
                if sp.simplify(r - K ** (5 * sgn)) == 0:
                    hits.append((n, other, norm, sgn))
            rows.append((n, other, norm, f"{val:.5g}", None if expo is None else float(expo)))
print(f"  gamma_L^5 = {float(GL**5):.4f};  Suchraum: {len(rows)} Verhaeltnisse (Zustand P oder R gegen M, je Normierung)")
for n, other, norm, val, expo in rows:
    print(f"  {n:46s} {other}:M, {norm:15s}: {val:>10s}" + ("" if expo is None else f"   = gamma_L^{expo:+.4f}"))
# Verhaeltnisse der Anteile innerhalb eines Zustands und reine Halbachsen-Potenzen
print("  Anteile im M-Zustand: a/b = 1/mu, a^2/b^2 = 1/mu^2, (a+b)/(a-b) = K. Als Potenz von K: 1/mu = K^%.4f, 1/mu^2 = K^%.4f"
      % (float(sp.log(1 / muM) / sp.log(GL)), float(sp.log(1 / muM ** 2) / sp.log(GL))))
print("  Exakte Identitaet mit K^5 oder K^-5 im Suchraum:", hits if hits else "keine")
p_, q_ = sp.symbols("p q", integer=True)
print("  Halbachsen-Monom (a+b)^p (a-b)^q, Verhaeltnis unter a-b <-> a+b ist K^(p-q); der Grad p+q einer Lagrange-Groesse ist gerade,")
print("  also p-q gerade: K^5 ist so nicht erreichbar. K^5 = (Halbachsenverhaeltnis)^5 braucht Grad 5 in den Amplituden.")
print("  Gewichtsregel (v4.8.0-r03.1): k(rho_vac) = k(hbar) - 4 k(l_P) = 1 - 4*3/2 =", 1 - 4 * sp.Rational(3, 2), " => der Exponent 5 ist dort eingesetzt.")

print("\n== 4a  Fassung F am Photonpunkt ==")
x = list(sp.symbols("x0:4", real=True)); v = list(sp.symbols("v0:4", real=True))
N = dot(x, x); J = [sp.expand(c) for c in qmul(qc(x), v)]; Ji, Js2 = J[1], J[2] ** 2 + J[3] ** 2
m = sp.Symbol("m", positive=True)
taum = 2 * m / (1 - m ** 2)
PF = (Js2 - taum ** 2 * Ji ** 2) ** 2 / N ** 2
lim = sp.limit(sp.simplify(PF / taum ** 4), m, 1)
print("  lim_{mu->1} P/tau^4 =", sp.factor(lim), " (endlich: eta' J_i^4/N^2; die Bedingung ist J_i = 0)")
PP = Ji ** 4 / N ** 2
def var(expr, dx, dv):
    return sp.simplify(sum(sp.diff(expr, s) * d for s, d in zip(x, dx)) + sum(sp.diff(expr, s) * d for s, d in zip(v, dv)))
units = {"i": [0, 1, 0, 0], "j": [0, 0, 1, 0], "k": [0, 0, 0, 1]}
print("  Invarianz von J_i^4/N^2: links", {n: var(PP, qmul(u, x), qmul(u, v)) for n, u in units.items()}, ", rechts um i:", var(PP, qmul(x, units["i"]), qmul(v, units["i"])))
g, gp, th, xi, d = sp.symbols("g gprime theta xi d", positive=True)
W1, W2, W3, Bf = sp.symbols("W1 W2 W3 B", real=True)
psi0 = [f * sp.cos(th), 0, f * sp.sin(th), 0]
Wq = [0, g / 2 * W1, g / 2 * W2, g / 2 * W3]; Bq = [0, gp / 2 * Bf, 0, 0]
Dv = [p - q for p, q in zip(qmul(Wq, psi0), qmul(psi0, Bq))]
J0 = qmul(qc(psi0), Dv)
Pv = sp.expand(J0[1] ** 4 / f ** 4)
print("  Vakuum mit Eichfeldern: Grad", sp.Poly(Pv, W1, W2, W3, Bf).total_degree(), ", Hesse-Matrix bei null = 0:",
      sp.hessian(Pv, (W1, W2, W3, Bf)).subs({W1: 0, W2: 0, W3: 0, Bf: 0}) == sp.zeros(4, 4), " => keine Massen, rho = 1, Licht masselos")
cost4 = sp.series(sp.simplify((Jt[1] ** 4 / (a ** 2 + b ** 2) ** 2).subs(b, (1 + d) * a)), d, 0, 6).removeO()
print("  Kosten einer Abweichung b = (1 + d) a in J_i^4/N^2:", sp.factor(sp.series(cost4, d, 0, 5).removeO()), "+ O(d^5)  (vierte Ordnung: keine Rueckstellung in fuehrender Ordnung)")
cost2 = sp.series(sp.simplify((Jt[1] ** 2 / (a ** 2 + b ** 2)).subs(b, (1 + d) * a)), d, 0, 3).removeO()
print("  quadratische Variante J_i^2/N (= Fassung S):", sp.factor(cost2), "+ O(d^3)")
Lm = sp.Rational(1, 2) * dot(Dv, Dv) + xi * J0[1] ** 2 / (2 * f ** 2)
M4 = sp.hessian(sp.expand(Lm), (W1, W2, W3, Bf)).applyfunc(sp.simplify)
evs = [sp.factor(sp.simplify(k)) for k in M4.eigenvals()]
print("  ... im Vakuum aber Eichfeldmassen", evs, " => rho = 1/(1 + xi), unabhaengig von theta (wie k299); bei theta = 45 Grad: J_i-Anteil =",
      sp.simplify(J0[1].subs(th, sp.pi / 4)))
PFm = sp.simplify((((Jt[2] ** 2 + Jt[3] ** 2) - taum ** 2 * Jt[1] ** 2) ** 2 / (a ** 2 + b ** 2) ** 2 / taum ** 4).subs(b, (m + d) * a))
c2 = sp.factor(sp.simplify(sp.diff(PFm, d, 2).subs(d, 0) / 2))
print("  umskalierte Fassung F bei allgemeinem mu, Koeffizient von d^2:", c2, ";  bei mu -> 1:", sp.limit(c2, m, 1), ";  bei mu_M:", f"{float(c2.subs({m: muM, a: 1, w: 1})):.5f}", "a^4 omega^4")

print("\n== 4b  H132 Stufe A (U(1) links x U(1) rechts) bei theta = 45 Grad ==")
gL, gR = sp.symbols("g_L g_R", positive=True); L, R = sp.symbols("L R", real=True)
iq = [0, 1, 0, 0]
DA = [gL * L * p - gR * R * q for p, q in zip(qmul(iq, psi0), qmul(psi0, iq))]
MA = sp.hessian(sp.expand(dot(DA, DA) / 2), (L, R)).applyfunc(sp.simplify)
print("  Massenmatrix:", MA.tolist(), ";  det =", sp.factor(sp.simplify(MA.det())))
M45 = MA.subs(th, sp.pi / 4).applyfunc(sp.simplify)
print("  bei 45 Grad:", M45.tolist(), ", Eigenwerte", list(M45.eigenvals()), ";  bei theta = 0 (R, b = 0): det =", sp.simplify(MA.det().subs(th, 0)))
print("  det als Funktion von theta ist maximal bei", sp.solve(sp.diff(sp.simplify(MA.det()), th), th))

print("\n== 4c  J-symmetrisches HC-Potential ==")
As, Bs = sp.symbols("A B", positive=True)
V = eta * (Bs - mu0 ** 2 * As) ** 2
print("  V(A,B) - V(B,A) =", sp.factor(V - V.subs({As: Bs, Bs: As}, simultaneous=True)), " => symmetrisch nur fuer mu0 =", sp.solve(sp.Eq(mu0 ** 4, 1), mu0))
Vs = eta * (Bs - As) ** 2
onM = {As: f ** 2 / (1 + mu ** 2), Bs: f ** 2 * mu ** 2 / (1 + mu ** 2)}
VM = sp.factor(sp.simplify(Vs.subs(onM)))
print("  mu0 = 1: V(P) =", Vs.subs({As: f ** 2 / 2, Bs: f ** 2 / 2}), ";  V(M) =", VM, "= eta f^4 cos^2(2 theta);  V(T) =", sp.factor(sp.simplify(Vs.subs({As: onM[Bs], Bs: onM[As]}))), ";  V(R) =", Vs.subs({As: f ** 2, Bs: 0}))
print("  Anteile von V bei P: eta A^2 =", (eta * As ** 2).subs(As, f ** 2 / 2), ", eta B^2 =", (eta * Bs ** 2).subs(Bs, f ** 2 / 2), ", -2 eta A B =", (-2 * eta * As * Bs).subs({As: f ** 2 / 2, Bs: f ** 2 / 2}), "(Summe null, Anteile nicht null)")
c2M = ((1 - mu ** 2) / (1 + mu ** 2)) ** 2
print(f"  V(M)/V(R) = cos^2(2 theta) bei mu_M: {float(c2M.subs(mu, muM)):.6f};  1 - beta_sym^2 = 1 - mu_M: {float(1 - muM):.6f};  Differenz {float(c2M.subs(mu, muM) - (1 - muM)):.6f}")
print("  Identitaet cos^2(2 theta) = 1 - mu ?", sp.simplify(c2M - (1 - mu)) == 0, ";  Gleichheit nur bei mu =", [sp.N(s, 6) for s in sp.Poly(sp.numer(sp.together(c2M - (1 - mu))), mu).nroots() if abs(sp.im(s)) < 1e-12])
print("  als Funktion von K: cos 2 theta =", sp.simplify(((1 - mu ** 2) / (1 + mu ** 2)).subs(mu, (sp.Symbol('K') - 1) / (sp.Symbol('K') + 1))), " (Kehrwert des Zahlentreffers aus k303)")
print("  mit dem Materie-Wert mu0 = mu_M statt 1: V(M) = 0, V(P)/V(R) =", sp.factor(sp.simplify(V.subs({As: f ** 2 / 2, Bs: f ** 2 / 2}) / V.subs({As: f ** 2, Bs: 0}))),
      f"= {float(((1 - muM**2)**2 / (4 * muM**4))):.4f} bei mu_M (gamma_L^5 = {float(GL**5):.4f})")
HM = sp.hessian(Vs.subs({As: x[0] ** 2 + x[1] ** 2, Bs: x[2] ** 2 + x[3] ** 2}), x).subs({x[0]: f / sp.sqrt(2), x[1]: 0, x[2]: f / sp.sqrt(2), x[3]: 0})
print("  Massenquadrate am Vakuum A = B (mu0 = 1):", HM.eigenvals(), " (eine Formmode, drei masselose; f^2 = A + B)")
