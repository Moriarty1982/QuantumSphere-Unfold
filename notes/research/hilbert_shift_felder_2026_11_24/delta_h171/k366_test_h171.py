"""k366 (H171): Achteldrehung aus H170 (azimutal) gegen Psi = exp(u pi/4) aus r13 neu (polar).
Vorab-Notiz Vorab_Notiz_H171_Achteldrehung_und_r13.md (Commit 4358c36).
Aufruf aus diesem Ordner: python3 k366_test_h171.py > k366_out.txt
"""
import os
import numpy as np
import sympy as sp

HERE = os.path.dirname(os.path.abspath(__file__))

print("== H171a: zwei verschiedene Drehungen ==")
A, B, d, th, R, chi = sp.symbols("A B delta theta R chi", real=True)
lam = [A + sp.sqrt(2) * B * sp.cos(d + 2 * sp.pi * k / 3) for k in range(3)]      # B = sqrt2 r, also 2 r = sqrt2 B
K = sp.simplify(sum(l**2 for l in lam) / sum(lam)**2)
print("K(A, B, delta) =", K, "; dK/d delta =", sp.simplify(sp.diff(K, d)))
Kth = sp.simplify(K.subs({A: R * sp.cos(th), B: R * sp.sin(th)}))
print("K(theta) =", sp.simplify(Kth), "; K = 2/3 fuer tan^2 theta =", sp.solve(sp.Eq((1 + sp.Symbol('t2')) / 3, sp.Rational(2, 3)), sp.Symbol('t2')),
      "; K(pi/4) =", sp.simplify(Kth.subs(th, sp.pi / 4)))
Vd = -sp.cos(2 * (d - chi))
print("Spin-1-Term -cos 2(delta - chi): Ableitung nach theta =", sp.diff(Vd, th), "; Minima delta = chi + n pi, unabhaengig von theta")
# Drehmatrizen auf n = (A, B cos d, B sin d)
def Rpol(t):   # dreht von der A-Achse in Richtung der ersten Dublettachse
    return sp.Matrix([[sp.cos(t), -sp.sin(t), 0], [sp.sin(t), sp.cos(t), 0], [0, 0, 1]])
def Raz(t):    # dreht in der Dublettebene
    return sp.Matrix([[1, 0, 0], [0, sp.cos(t), -sp.sin(t)], [0, sp.sin(t), sp.cos(t)]])
e = sp.Matrix([1, 0, 0])
n = sp.simplify(Raz(d) * Rpol(th) * e)
print("Raz(delta) Rpol(theta) e_A =", list(n), " (= (cos th, sin th cos d, sin th sin d))")

print("\n== H171b: Fixachsen zweier Tausche; Baumpunkt ==")
J3 = sp.Matrix([[0, 1], [1, 0]])
print("Tausch (x, y) -> (y, x): Fixachse (1, 1)/sqrt2 = Winkel", sp.atan2(1, 1), "; gilt fuer J auf (A, B) und fuer C sigma auf (s, v)")
a = sp.symbols("a", positive=True)
j = sp.I   # innere Einheit hier als komplexe Zahl (H_3(C))
S = sp.Matrix([[0, 1, 0], [0, 0, 1], [1, 0, 0]])
for lab, z in (("z = a(1 + j)/2 ", a * (1 + j) / 2), ("z = a(-1 + j)/2", a * (-1 + j) / 2)):
    W = a * sp.eye(3) + z * S + sp.conjugate(z) * S.T
    ev = sorted([sp.nsimplify(sp.simplify(sp.re(x) / a)) for x in W.eigenvals()], key=lambda x: float(x))
    Kv = sp.simplify((W * W).trace() / W.trace()**2)
    print(f"  {lab}: |z|/a = {sp.simplify(sp.Abs(z) / a)}, arg z = {sp.arg(z)}, K = {Kv}, Eigenwerte/a = {ev}, det/a^3 = {sp.simplify(W.det() / a**3)}")
print("  z - (a/sqrt2) exp(j pi/4) =", sp.simplify(sp.expand_complex(a * (1 + j) / 2 - a / sp.sqrt(2) * sp.exp(j * sp.pi / 4))),
      "; a(-1 + j)/2 - j (a/sqrt2) exp(j pi/4) =", sp.simplify(sp.expand_complex(a * (-1 + j) / 2 - j * a / sp.sqrt(2) * sp.exp(j * sp.pi / 4))))
s_, v_ = a / 2, a / 2
tot = a**2 + 2 * s_**2 + 2 * v_**2
print("  Gewichte (A^2, 2 s^2, 2 v^2)/Summe =", [sp.simplify(x / tot) for x in (a**2, 2 * s_**2, 2 * v_**2)])
nstar = sp.simplify(Raz(sp.pi / 4) * Rpol(sp.pi / 4) * e)
print("  Raz(pi/4) Rpol(pi/4) e_A =", list(nstar), "; Quadrate:", [sp.simplify(x**2) for x in nstar])

print("\n== H171c: Sedenionen, wer erzeugt den Azimut? ==")
src = open(os.path.join(HERE, "..", "k253_cayley_dickson_turm.py")).read().split("for n in range(0, 6):")[0]
ns = {}; exec(src, ns); mul = ns["mul"]
E = np.eye(16)
rs, ls = [], []
for i in range(1, 8):
    r_ = mul(E[i], E[8]); l_ = mul(E[8], E[i])
    rs.append(float(r_ @ E[i + 8])); ls.append(float(l_ @ E[i + 8]))
    assert abs(abs(rs[-1]) - 1) < 1e-12 and abs(abs(ls[-1]) - 1) < 1e-12
print("e_i e_8 = s_R e_{i+8}, s_R =", rs, "; e_8 e_i = s_L e_{i+8}, s_L =", ls)
print("einheitlich:", len(set(rs)) == 1, len(set(ls)) == 1, "; e_8^2 =", mul(E[8], E[8])[0])
th_ = 0.37
w = E[3]
rot = np.cos(th_) * w + np.sin(th_) * rs[0] * mul(w, E[8])
print("cos th e_3 + sin th s_R (e_3 e_8) - (cos th e_3 + sin th e_11): max", np.abs(rot - (np.cos(th_) * E[3] + np.sin(th_) * E[11])).max())
# polare Einheit u in Kopie O_delta; vertauscht sie mit e_8?
u = np.cos(0.2) * E[3] + np.sin(0.2) * E[11]
print("u^2 = -1:", np.allclose(mul(u, u), -E[0]), "; u e_8 + e_8 u (Antikommutator), max:", np.abs(mul(u, E[8]) + mul(E[8], u)).max(), "; u senkrecht e_8:", abs(u @ E[8]) < 1e-15)
def copy(t):
    return np.array([E[0]] + [np.cos(t) * E[i] + np.sin(t) * E[i + 8] for i in range(1, 8)])
def proj(Bm):
    return Bm.T @ np.linalg.pinv(Bm.T)
print("Abgeschlossenheit von O_theta (max |(1-P) xy|), wie k255 (3):")
for name, ang in (("0", 0), ("pi/12", 15), ("pi/6", 30), ("pi/4", 45), ("pi/3", 60), ("pi/12 - x", np.rad2deg(0.2222220470731)), ("pi/6 - x", np.rad2deg(np.pi / 6 - 0.0395773407))):
    Bm = copy(np.deg2rad(ang)); Pt = proj(Bm)
    cdev = max(np.abs(mul(x, y) - Pt @ mul(x, y)).max() for x in Bm for y in Bm)
    print(f"   delta = {name:>9} ({ang:8.4f} Grad): {cdev:.6f}")

print("\n== H171d: Zusammensetzung ==")
M = sp.simplify(Raz(sp.pi / 4) * Rpol(sp.pi / 4))
cosT = sp.simplify((M.trace() - 1) / 2)
print("cos Theta =", sp.nsimplify(cosT), "; minus (2 sqrt2 - 1)/4 =", sp.simplify(cosT - (2 * sp.sqrt(2) - 1) / 4), "; Theta =", float(sp.acos(cosT) * 180 / sp.pi), "Grad")
comm = sp.simplify(Raz(sp.pi / 4) * Rpol(sp.pi / 4) - Rpol(sp.pi / 4) * Raz(sp.pi / 4))
print("Kommutator ungleich null:", comm != sp.zeros(3, 3), "; Norm:", float(comm.norm()))
