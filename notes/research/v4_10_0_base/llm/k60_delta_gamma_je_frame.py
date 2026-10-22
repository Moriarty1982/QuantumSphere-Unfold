"""k60: Delta_gamma je Frame (Materie, Tachyon, Photon) und eine Herleitung der 1/5.

Praemissen (Dublettzustand r17, Fensterkarte r14/r12):
 D1 Uhrgewinn G = 1/|b| = |gamma|: die Photon-Frame-Uhr hebt die Sichtbarkeit |b| auf 1 (Auslesegroesse, Weg A).
 D2 Paar-Kopplung kappa = Inhalt des Partnerports: Materie p-, Tachyon p+ (J_B tauscht die Ports, r02/r04).
 D3 Balance im Frame, der die Uhr braucht (Materie): kappa (N - 1) = 1.
 D4 N ist eine Paketzahl und frame-invariant.
 D5 Tachyonbeschreibung = Uhrsaat (N, kappa, G) = (5, 3/4, 1) der Quelle: G_T = 1.
 Fensterbedingung (r12, P2/P3): G (1 - Delta) S > 16, S = N + kappa N (N - 1).
"""
import math
import sympy as sp

x = sp.symbols("x", positive=True)            # x = beta^2 der Materie
gam = (1 + x) / (1 - x)
pm, pp = x / (1 + x), 1 / (1 + x)
N = 1 + 1 / pm                                 # D3
SM = N + pm * N * (N - 1)
ST = N + pp * N * (N - 1)                      # D4, D2
resM = sp.simplify(1 - 16 / (gam * SM))        # D1
resT = sp.simplify(1 - 16 / (1 * ST))          # D5
print("1. Reserve je Frame (symbolisch, x = beta^2)")
print("   Materie:", sp.factor(resM))
print("   Tachyon:", sp.factor(resT))
sol = sp.solve(sp.Eq(gam * SM, ST), x)
print("   Frame-Konsistenz G_M S_M = G_T S_T  ->  beta^2 =", sol)
for s in sol:
    print("     N = %s, S_M = %s, S_T = %s, Reserve = %s" % (sp.nsimplify(N.subs(x, s)), sp.nsimplify(SM.subs(x, s)),
          sp.nsimplify(ST.subs(x, s)), sp.nsimplify(resM.subs(x, s))))

print("\n   ohne D3, N = 5 fest: G_M S_M = S_T  <=>  4 p-^2 - 9 p- + 2 = 0  ->  p- =",
      sp.solve(4 * sp.Symbol("p") ** 2 - 9 * sp.Symbol("p") + 2, sp.Symbol("p")))

gL = 0.2375 / (math.log(2) / (math.pi * math.sqrt(3)))
xm = math.tanh(0.5 * math.acosh(gL)) ** 2
print("\n2. Zahlen je Frame")
print("   %-34s %8s %8s %8s %8s %8s %10s" % ("Frame / Punkt", "beta^2", "|G|", "kappa", "N", "S", "Reserve"))
def line(name, b2, G, k, n):
    S = n + k * n * (n - 1)
    r = 1 - 16 / (G * S)
    st = "kein Fenster noetig" if S >= 16 and G == 1 else ("blockiert" if G * S < 16 else "")
    print("   %-34s %8.4f %8.4f %8.4f %8.4f %8.4f %10.4f %s" % (name, b2, G, k, n, S, r, st))
for name, b2 in (("Hopf", 1 / 3), ("gemessen", xm)):
    g = (1 + b2) / (1 - b2); m = b2 / (1 + b2); p = 1 / (1 + b2); n = 1 + 1 / m
    line("Materie, " + name, b2, g, m, n)
    line("Tachyon, " + name + " (D5, G = 1)", 1 / b2, 1.0, p, n)
    line("Tachyon, " + name + " (G = |gamma|)", 1 / b2, g, p, n)
print("   Photon (b = 0): p+ = p- = 1/2, |G| = 1/|b| -> unendlich; Reserve -> 1 (Scheibe) oder")
line("Photon, sigma-Linie (G = 1), N = 5", 1.0, 1.0, 0.5, 5)
line("Photon, sigma-Linie (G = 1), N = 3", 1.0, 1.0, 0.5, 3)

print("\n3. Folgen")
rM = 1 - 16 / (gL * ((1 + 1 / (xm / (1 + xm))) * 2))
print("   Materie gemessen %.4f < 1/5: frame-freie 1/5 dort zu grosszuegig um %.4f" % (rM, 0.2 - rM))
print("   Materie: C5-Stufe (Export 1/4) %s, Kollarzeile (1/6) %s" % ("innen" if 0.25 < rM else "aussen", "innen" if 1 / 6 < rM else "aussen"))
print("   Tachyon gemessen: Reserve 0,302 > 1/4, aber dort ist kein Fenster noetig (S >= 16 ohne Uhr)")
print("   r20-Lesarten mit fester Karte (0,10-0,14) widersprechen D3; die Herleitung waehlt die balancierte Lesart")
