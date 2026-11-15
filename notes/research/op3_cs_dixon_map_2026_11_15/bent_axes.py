"""Erkundung (nicht blind): drei Zustaende mit paarweiser Ueberlappung |<a|b>|^2 = 1/2 und Bargmann-Phase phi.
Gram-Matrix G zirkulant mit G12 = G23 = G31conj ... so dass G12 G23 G31 = exp(i phi)/(2 sqrt2).
Fragen: Rang von G in Abhaengigkeit von phi (flaches Qubit oder Ausbiegen nach C^3), Koide aus G, Lepton-Wert."""
import numpy as np
import sympy as sp
p = sp.symbols('phi', real=True)
a = sp.exp(sp.I * p / 3) / sp.sqrt(2)
G = sp.Matrix([[1, a, sp.conjugate(a)], [sp.conjugate(a), 1, a], [a, sp.conjugate(a), 1]])
det = sp.simplify(sp.expand_complex(G.det()))
print("det G =", sp.simplify(sp.trigsimp(det)))
print("Bargmann G12 G23 G31 =", sp.simplify(G[0, 1] * G[1, 2] * G[2, 0]))
print("det = 0 bei phi = pi/4:", sp.simplify(det.subs(p, sp.pi / 4)) == 0)
for name, phi in (("Oktant pi/4", np.pi / 4), ("Brannen 3*2/9 = 2/3 rad", 2 / 3)):
    Gn = np.array(G.subs(p, phi).evalf(), dtype=complex)
    ev = np.sort(np.linalg.eigvalsh(Gn))
    K = (ev ** 2).sum() / ev.sum() ** 2
    print(f"{name}: det {np.linalg.det(Gn).real:+.6f}, Eigenwerte {np.round(ev, 6)}, Koide {K:.6f}, "
          f"Verhaeltnisse {np.round(ev / ev[0], 3) if ev[0] > 1e-9 else 'eine Null'}")
x = np.sqrt([0.51099895, 105.6583755, 1776.93])
print("Wurzelmassen-Verhaeltnisse der geladenen Leptonen:", np.round(x / x[0], 3))
print("Ausbiegung pi/4 - 2/3 =", round(np.pi / 4 - 2 / 3, 6), " gamma_M/2 (0.2375330/2) =", round(0.2375330 / 2, 6))
