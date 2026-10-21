"""k34: Rueckwaertsanalyse (wie K18) - zaehlt nicht als Test.

Frage: Kann ein dritter Index (der Frame, aus dem gelesen wird) die heutigen Werte aus einer ungestoerten
Starteinstellung erzeugen?  T_abc = Versatz von Frame a gegen Frame b, gelesen aus Frame c.
Starteinstellung: Hopf-Kontinuum, beta = 1/sqrt(3) (gamma_L = 2), J-symmetrisch.
Regel K18: ein Ansatz lohnt nur, wenn er mehr Messwerte erklaert, als er Parameter hinzufuegt.
"""
import math

# ---------------------------------------------------------------- A: reine Kinematik
# Ein Boost in Frame c zieht eta_c von allen Rapiditaeten ab; Differenzen bleiben gleich.
eta = {"+": 0.6, "0": 0.0, "-": -0.6}
inv = all(abs(((eta[a]-eta[c])-(eta[b]-eta[c])) - (eta[a]-eta[b])) < 1e-15
          for a in eta for b in eta for c in eta)
print("A  rein kinematisch ist T_abc unabhaengig von c:", inv)

# ---------------------------------------------------------------- B: Starteinstellung und Daten
eH = math.atanh(1/math.sqrt(3))
def e_from_b2(b2): return math.atanh(math.sqrt(b2))
def se_from_b2(b2, sb2):                 # sigma(eta) aus sigma(beta^2)
    b = math.sqrt(b2); return sb2/(2*b*(1-b2))

OM, sOM = 0.3111, 0.0056                 # Planck 2018 + BAO
s12, ss12 = 0.3036, 0.0064               # JUNO 2026
s13 = 0.02215
b2J, sb2J = s12*(1-s13), ss12*(1-s13)    # ueber die nachtraeglich gefundene H9-Relation |U_e2|^2 = beta^2
gL = 0.2375/(math.log(2)/(math.pi*math.sqrt(3)))

D = [  # (Name, (a,b,c), eta, sigma)
    ("Planck Omega_M", ("-", "0", "+"), e_from_b2(OM), se_from_b2(OM, sOM)),
    ("JUNO theta12",  ("+", "0", "+"), e_from_b2(b2J), se_from_b2(b2J, sb2J)),
]
eLQG = math.acosh(gL)/2                  # Theorie-Verhaeltnis zweier Zaehlungen (r03 F11), kein Messwert
print("\nB  Starteinstellung eta_H = %.5f (beta 0.57735)" % eH)
for n, abc, e, s in D:
    print("   %-15s T%s  eta = %.5f +- %.5f  beta = %.5f  Absenkung gg. Hopf %.2f %%"
          % (n, "".join(abc), e, s, math.tanh(e), 100*(1-e/eH)))
print("   %-15s T+-+/2 eta = %.5f (ohne Fehler)        beta = %.5f  Absenkung %.2f %%"
      % ("LQG gamma_L", eLQG, math.tanh(eLQG), 100*(1-eLQG/eH)))

def chi2(pred):
    return sum(((p-e)/s)**2 for p, (_, _, e, s) in zip(pred, D))

pos = {"+": eH, "0": 0.0, "-": -eH}
print("\nC  Ansaetze (Parameter, chi2 auf 2 Messwerte, Freiheitsgrade)")

# M0: keine Auslesewirkung
p0 = [abs(pos[a]-pos[b]) for _, (a, b, c), _, _ in D]
print("   M0 nur Kinematik           0 Par.  chi2 = %6.2f  (2 FG)" % chi2(p0))

# M1: Auslesung zieht das gelesene Objekt a zum Frame c: eta_a -> eta_a + lam (eta_c - eta_a)
def m1(lam, objekt):
    # objekt: welcher der beiden Frames gelesen (angeregt) wird; Standard a, Bezug ist der andere
    out = []
    for _, (a, b, c), _, _ in D:
        o = objekt.get((a, b, c), a); r = b if o == a else a
        eo = pos[o] + lam*(pos[c]-pos[o])
        out.append(abs(eo - pos[r]))
    return out
def best(f):
    lo, hi = -0.5, 0.5
    grid = [lo + (hi-lo)*i/20000 for i in range(20001)]
    l = min(grid, key=lambda x: chi2(f(x))); return l, chi2(f(l))
l, c = best(lambda x: m1(x, {}))
print("   M1 Zug auf gelesenes Objekt 1 Par.  chi2 = %6.2f  (1 FG)  lam = %+.4f   [JUNO: Selbstlesung, c = a]" % (c, l))
l, c = best(lambda x: m1(x, {("+", "0", "+"): "0"}))
print("   M1' dito, Neutrino lichtartig (H2): gelesenes Objekt 0  chi2 = %6.2f  (1 FG)  lam = %+.4f" % (c, l))

# M2: antisymmetrischer Term kappa * eps_abc (verschwindet bei doppeltem Index)
eps = lambda a, b, c: {("+","0","-"):1,("0","-","+"):1,("-","+","0"):1,("-","0","+"):-1,("0","+","-"):-1,("+","-","0"):-1}.get((a,b,c),0)
l, c = best(lambda k: [abs(pos[a]-pos[b] + k*eps(a, b, c)) for _, (a, b, c), _, _ in D])
print("   M2 kappa * eps_abc          1 Par.  chi2 = %6.2f  (1 FG)  kappa = %+.4f" % (c, l))

# M3: Auslesefaktor je lesendem Frame: T_abc = (eta_a - eta_b) * f(c); beide Messungen aus c = +
w = [1/s**2 for _, _, _, s in D]
eb = sum(wi*e for wi, (_, _, e, _) in zip(w, D))/sum(w); seb = 1/math.sqrt(sum(w))
f = eb/eH
c3 = chi2([eb, eb])
print("   M3 Auslesefaktor f(c)       1 Par.  chi2 = %6.2f  (1 FG)  f(+) = %.4f +- %.4f" % (c3, f, seb/eH))
print("      -> eta = %.5f, beta = %.5f, beta/(1/sqrt3) = %.4f +- %.4f;  LQG-Kontrolle: eta %.5f gegen %.5f"
      % (eb, math.tanh(eb), math.tanh(eb)*math.sqrt(3), seb*(1-math.tanh(eb)**2)*math.sqrt(3), eLQG, eb))
print("      delta_CL des Dokuments (conj:cl-correction, P3 seit r09 als Koinzidenz eingestuft): 0.9512")

# M4: freier Faktor je Messkontext
print("   M4 freier Faktor je Kontext 2 Par.  chi2 =   0.00  (0 FG)  -> erklaert nichts (K18)")

print("\nUnterschied der beiden Messungen in eta: %.4f +- %.4f (%.1f sigma)"
      % (D[0][2]-D[1][2], math.hypot(D[0][3], D[1][3]), (D[0][2]-D[1][2])/math.hypot(D[0][3], D[1][3])))
