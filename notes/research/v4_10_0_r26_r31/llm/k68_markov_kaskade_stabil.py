"""k68: Ist die Markov-Kaskade aus thm:dark-energy selbststabilisierend? (Autorabsicht 2026-10-22: die Kette sollte die
Wahrscheinlichkeiten besser vorhersagen und pruefen, ob sie sich selbst stabilisieren kann.)

1. Kette wie im Beweis: S8 -> S4 (beta^2), S8 -> S2 (1 - beta^2), S4 -> S2 (1), S2 absorbierend.
2. Mit Rueckweg S2 -> S8 (Rate r), etwa durch Paarerzeugung aus dem Vakuum (v4.9.0-r29).
"""
import sympy as sp

b2, r = sp.symbols("beta2 r", positive=True)
P = sp.Matrix([[1, 0, 0], [1, 0, 0], [1 - b2, b2, 0]])      # Reihen von S2, S4, S8; Spalten nach S2, S4, S8
print("1. ohne Rueckweg")
print("   P^3 =", (P ** 3).subs(b2, sp.Rational(1, 3)).tolist(), "-> alles endet in S2 (Photon)")
pi = sp.symbols("p2 p4 p8")
sol = sp.solve(list(sp.Matrix([pi]) * P - sp.Matrix([pi])) + [sum(pi) - 1], pi, dict=True)
print("   stationaer:", sol)

print("\n2. mit Rueckweg S2 -> S8 (Rate r)")
Q = sp.Matrix([[1 - r, 0, r], [1, 0, 0], [1 - b2, b2, 0]])
sol = sp.solve(list(sp.Matrix([pi]) * Q - sp.Matrix([pi])) + [sum(pi) - 1], pi, dict=True)[0]
sol = {k: sp.simplify(v) for k, v in sol.items()}
print("   stationaer:", sol)
p2, p4, p8 = (sol[s] for s in pi)
print("   Fluss aus S8 nach S4 : nach S2 =", sp.simplify(p8 * b2), ":", sp.simplify(p8 * (1 - b2)),
      "-> Anteile", sp.simplify(p8 * b2 / p8), "und", sp.simplify(p8 * (1 - b2) / p8), "fuer jedes r > 0")
for rv in (sp.Rational(1, 10), sp.Rational(1, 2), 1):
    Qn = Q.subs({b2: sp.Rational(1, 3), r: rv})
    v = sp.Matrix([[0, 0, 1]])
    for _ in range(200):
        v = v * Qn
    print("   r = %s: Verteilung nach 200 Schritten aus S8 = %s, stationaer = %s"
          % (rv, [float(x) for x in v], [float(sol[s].subs({b2: sp.Rational(1, 3), r: rv})) for s in pi]))
print("   Eigenwerte von Q (beta^2 = 1/3, r = 1/2):", [sp.nsimplify(e) for e in Q.subs({b2: sp.Rational(1, 3), r: sp.Rational(1, 2)}).eigenvals()])
