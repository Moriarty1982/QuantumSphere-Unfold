"""k297 (Erkundung, nicht blind): Bricht der HC die Tauschsymmetrie Vorstufe <-> Anhang aus H129?
1  Tausch (Rechtsmultiplikation mit j) im Schatten z = psi1 + conj(chi): Beltrami-Koeffizient mu -> 1/mu
2  HC-Bedingung B = mu^2 A als skalenfreies Potential eta (B - mu^2 A)^2: zulaessig nach k295, flache Richtung
3  Spektrum auf der flachen Richtung, Loesung im Anhang, Groesse frei (klassisch)
4  Skala aus der Schleife (Gildener-Weinberg), Verhaeltnis leichte zu schwerer Radialmode
5  Fluss: bleibt das HC-Verhaeltnis erhalten?
6  Zahlen mit beta_sym^2 = 0.3018, gamma_L = 1.8644 (eingesetzt, OP1)
Aufruf: python k297_hc_tauschsymmetrie.py > k297_out.txt
"""
import sympy as sp

a, b, w, t = sp.symbols("a b omega t", positive=True)
mu, eta, f, M = sp.symbols("mu eta f M", positive=True)
x = sp.symbols("x0:4", real=True)
A = x[0] ** 2 + x[1] ** 2; B = x[2] ** 2 + x[3] ** 2

print("== 1  Tausch und Beltrami-Koeffizient ==")
print("  psi = a e^{iwt} + (b j) e^{-iwt}: psi1 = a e^{iwt}, chi = b e^{iwt}; Schatten z = psi1 + conj(chi) = a e^{iwt} + b e^{-iwt}")
print("  Abbildung u -> a u + b conj(u): mu = b/a, K = (a+b)/(a-b)")
K = lambda p, q: (p + q) / (p - q)
print("  Tausch psi -> psi j: (psi1, chi) -> (-chi, psi1), also a <-> b:  mu -> a/b = 1/mu,  K ->", sp.simplify(K(b, a) / K(a, b)), "* K (Orientierung kehrt um)")
print("  invariant nur fuer mu = 1 (a = b, lineare Polarisation, HS(0))")

print("\n== 2  HC-Bedingung als Potential ==")
V = eta * (B - mu ** 2 * A) ** 2
lA, ka, lB = sp.symbols("lambda_A kappa lambda_B")
co = sp.Poly(sp.expand(eta * (sp.Symbol("B_") - mu ** 2 * sp.Symbol("A_")) ** 2), sp.Symbol("A_"), sp.Symbol("B_"))
cA, cK, cB = co.coeff_monomial((2, 0)), co.coeff_monomial((1, 1)), co.coeff_monomial((0, 2))
print("  eta (B - mu^2 A)^2 = lamA A^2 + kappa A B + lamB B^2 mit lamA =", cA, ", kappa =", cK, ", lamB =", cB)
print("  kein Term in A oder B allein (keine Skala, keine Masse der Vorstufe); kappa < 0; kappa + 2 sqrt(lamA lamB) =", sp.simplify(cK + 2 * sp.sqrt(cA * cB)),
      " (genau die Stabilitaetsgrenze, Klasse (iv) aus H129)")
print("  unter dem Tausch A <-> B: eta (A - mu^2 B)^2 = eta mu^4 (B - A/mu^2)^2, also mu -> 1/mu, eta -> eta mu^4")

print("\n== 3  flache Richtung, Spektrum, Loesung ==")
pt = {x[0]: f / sp.sqrt(1 + mu ** 2), x[1]: 0, x[2]: mu * f / sp.sqrt(1 + mu ** 2), x[3]: 0}
print("  Punkt A = f^2/(1+mu^2), B = mu^2 f^2/(1+mu^2): V =", sp.simplify(V.subs(pt)), ", Gradient =", [sp.simplify(sp.diff(V, s).subs(pt)) for s in x], " fuer jedes f")
H = sp.hessian(V, x).subs(pt)
ev = {sp.factor(sp.simplify(k)): v for k, v in H.eigenvals().items()}
print("  Massenquadrate:", ev, " (zwei Phasen, eine Groessenmode, eine schwere Formmode)")
mH2 = [k for k in ev if k != 0][0]
ph = w * t
fld = [a * sp.cos(ph), a * sp.sin(ph), b * sp.cos(ph), b * sp.sin(ph)]            # psi = e^{iwt}(a + b j), ohne Ortsabhaengigkeit
eom = [sp.simplify((sp.diff(c, t, 2) + sp.diff(V, s).subs(dict(zip(x, fld)))) / c) for c, s in zip(fld, x)]
print("  Bewegungsgleichung fuer psi = e^{iwt}(a + b j), geteilt durch das Feld:", [sp.factor(e) for e in eom])
print("    mit b = mu a:", [sp.simplify(e.subs(b, mu * a)) for e in eom], " => loest sie nur als Welle (omega = |k|), nicht als ruhende Drehung; Groesse a frei")

print("\n== 4  Skala aus der Schleife ==")
phi = sp.symbols("phi", positive=True)
m2 = mH2.subs(f, phi)
V1 = m2 ** 2 / (64 * sp.pi ** 2) * (sp.log(m2 / M ** 2) - sp.Rational(3, 2))
sol = sp.solve(sp.diff(V1, phi), phi)
print("  V1(phi) = m_H^4/(64 pi^2) (ln(m_H^2/M^2) - 3/2), m_H^2 =", m2, ";  Minimum bei phi^2 =", [sp.simplify(s ** 2) for s in sol])
ms2 = sp.simplify(sp.diff(V1, phi, 2).subs(phi, sol[0]))
print("  Masse der Groessenmode: m_s^2 =", ms2, ";  m_s^2/m_H^2 =", sp.simplify(ms2 / m2.subs(phi, sol[0])), ";  V1 am Minimum =", sp.simplify(V1.subs(phi, sol[0])), "(< 0)")

print("\n== 5  Fluss (beta-Funktionen aus k296) ==")
bA, bK, bB = 4 * (ka ** 2 + 20 * lA ** 2), 16 * ka * (ka + 2 * lA + 2 * lB), 4 * (ka ** 2 + 20 * lB ** 2)
rho = sp.symbols("rho", positive=True)
onflat = {ka: -2 * sp.sqrt(lA * lB)}
drho = sp.simplify(((bB * lA - bA * lB) / lA ** 2).subs(onflat).subs(lB, rho * lA))
lAp = sp.symbols("lambda_A", positive=True)
dgap = sp.simplify(((bK + (bA * lB + bB * lA) / sp.sqrt(lA * lB))).subs(onflat).subs(lB, rho * lA).subs(lA, lAp))
print("  auf der flachen Flaeche, rho = lamB/lamA = mu^-4:  16 pi^2 d rho/dt =", sp.factor(drho), ";  16 pi^2 d(kappa + 2 sqrt(lamA lamB))/dt =", sp.factor(dgap))
print("  => rho ist nur bei rho = 1 fest (und bei 0, unendlich). Fuer rho > 1 (mu < 1) waechst rho mit t: ins Ultraviolette wird der Anhang kleiner (mu -> 0),")
print("     ins Infrarote laeuft mu langsam auf 1 zu. Der Abstand zur flachen Flaeche waechst mit t: von oben (stabil) kommend wird sie ins Infrarote durchquert, dort entsteht die Skala.")

print("\n== 6  Zahlen (beta_sym^2 und gamma_L eingesetzt, nicht hergeleitet) ==")
gL = sp.Float("1.8644"); muv = (gL - 1) / (gL + 1)
print(f"  mu = (gamma_L - 1)/(gamma_L + 1) = {muv:.4f};  B/A = mu^2 = {muv**2:.4f};  Anteil des Anhangs an der Norm = {muv**2/(1+muv**2):.4f}")
print(f"  lamB/lamA = mu^-4 = {muv**-4:.1f};  m_H^2 = {sp.N(mH2.subs({mu: muv, eta: 1, f: 1}), 4)} eta f^2;  m_s^2/m_H^2 = {sp.N((ms2 / m2.subs(phi, sol[0])).subs({mu: muv, eta: 1}), 4)} eta")
print(f"  Winkel auf der Hopf-Sphaere: cos = (1 - mu^2)/(1 + mu^2) = {(1-muv**2)/(1+muv**2):.4f}, also {sp.N(sp.acos((1-muv**2)/(1+muv**2))*180/sp.pi, 4)} Grad vom Pol (k292: 33,6)")
