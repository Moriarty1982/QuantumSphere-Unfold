"""k365 (H170): c -> -i c. Wick-Drehung, Minkowski-Ebene, beide Sektoren aus einer holomorphen Form.
Vorab-Notiz Vorab_Notiz_H170_c_mal_minus_i_Minkowski.md (Commit 9b479a6).
Aufruf: python3 k365_test_h170.py > k365_out.txt
"""
import sympy as sp
import mpmath as mp

I2 = sp.eye(2); J = sp.Matrix([[0, -1], [1, 0]]); i = sp.I
K = i * J                                             # k = i j, k^2 = +1


def zero(M):
    M = sp.Matrix(M)
    return M.applyfunc(sp.simplify) == sp.zeros(*M.shape)


c, cp, c1, c2, s, v, a, b, eps = sp.symbols("c cp c1 c2 s v a b epsilon")
P = (I2 + i * J) / 2; Pb = (I2 - i * J) / 2

print("== H170a: die Abbildung c -> -i c ==")
m = lambda t: -i * t
orb = [i]
for _ in range(4):
    orb.append(sp.simplify(m(orb[-1])))
print("Bahn von c = i:", orb, "; Ordnung 4:", sp.simplify(m(m(m(m(c)))) - c) == 0, "; Fixpunkte endlich:", sp.solve(m(c) - c, c), "(dazu unendlich)")
print("c = i: 1 + c j = 2P:", zero(I2 + i * J - 2 * P), "; c = -i: 2Pb:", zero(I2 - i * J - 2 * Pb))

print("\n== H170b: Schub und Minkowski-Signatur ==")
print("k^2 = +1:", zero(K * K - I2), "; 1 + c j - (1 + c' k) bei c = i c':", zero((I2 + c * J).subs(c, i * cp) - (I2 + cp * K)))
print("Norm auf span(1, j): (a + b j)(a - b j) =", sp.simplify(((a * I2 + b * J) * (a * I2 - b * J))[0, 0]),
      "; auf span(1, k): (a + b k)(a - b k) =", sp.simplify(((a * I2 + b * K) * (a * I2 - b * K))[0, 0]))
boost = sp.cosh(eps) * I2 + sp.sinh(eps) * K
print("1 + tanh(eps) k - (cosh eps + k sinh eps)/cosh eps = 0:", zero((I2 + sp.tanh(eps) * K - boost / sp.cosh(eps)).applyfunc(lambda e: sp.simplify(e.rewrite(sp.exp)))))
print("exp(eps k) = cosh + k sinh; e^{eps k} P = e^{eps} P:", zero((boost * P - sp.exp(eps) * P).applyfunc(lambda e: sp.simplify(e.rewrite(sp.exp)))),
      "; e^{eps k} Pb = e^{-eps} Pb:", zero((boost * Pb - sp.exp(-eps) * Pb).applyfunc(lambda e: sp.simplify(e.rewrite(sp.exp)))))
prod = (I2 + c1 * K) * (I2 + c2 * K)
print("(1 + c1 k)(1 + c2 k) = (1 + c1 c2)(1 + c12 k) mit c12 = (c1 + c2)/(1 + c1 c2):",
      zero(prod - (1 + c1 * c2) * (I2 + (c1 + c2) / (1 + c1 * c2) * K)))
prodj = (I2 + c1 * J) * (I2 + c2 * J)
print("zum Vergleich reell: (1 + c1 j)(1 + c2 j) = (1 - c1 c2)(1 + c12 j), c12 = (c1 + c2)/(1 - c1 c2):",
      zero(prodj - (1 - c1 * c2) * (I2 + (c1 + c2) / (1 - c1 * c2) * J)))
aa = sp.symbols("aa")
print("Tr Z^2 = 2(1 + a^2)|x|^2 bei a = i c':", sp.factor((2 * (1 + aa**2)).subs(aa, i * cp)), "|x|^2 ; N = 2(3a - a^3) xyz:",
      sp.factor((2 * (3 * aa - aa**3)).subs(aa, i * cp)), "xyz ; Spin-1-Term (1 + c^2) v'^2:", sp.factor((1 + c**2).subs(c, i * cp)), "v'^2")
print("lichtartig (Norm 0) genau fuer c' =", sp.solve(1 - cp**2, cp), "; 1 + k = 2P:", zero(I2 + K - 2 * P))

print("\n== H170c: holomorphe Form am Projektorpunkt ==")
sr, vr, r, d, chi = sp.symbols("s v r delta chi", real=True)
G = lambda cc: (cc * sr - vr)**2
F = lambda cc: G(cc) / (1 + cc**2)
n = sr**2 + vr**2
Gi = sp.expand(G(i))
print("G_i + (s + i v)^2 =", sp.expand(Gi + (sr + i * vr)**2))
print("Re G_i - (2 F_0 - n) =", sp.simplify(sp.re(Gi) - (2 * F(0) - n)), "; Im G_i - (2 F_1 - n) =", sp.simplify(sp.im(Gi) - (2 * F(1) - n)),
      "; Im G_i =", sp.im(Gi))
pol = {sr: r * sp.cos(d), vr: r * sp.sin(d)}
print("G_i + r^2 e^{2 i delta} =", sp.simplify(sp.expand_complex(Gi.subs(pol) + r**2 * sp.exp(2 * i * d))))
fam = sp.re(sp.expand_complex(sp.exp(-2 * i * chi) * (-r**2 * sp.exp(2 * i * d))))
print("Re[e^{-2 i chi} G_i] + r^2 cos 2(delta - chi) =", sp.simplify(fam + r**2 * sp.cos(2 * (d - chi))))
cr = sp.symbols("c", real=True)
print("2 F_c - n + r^2 cos 2(delta - arctan c) =", sp.simplify((2 * F(cr) - n).subs(pol) + r**2 * sp.cos(2 * (d - sp.atan(cr)))))

print("\n== H170d: Multiplikation mit -i ==")
print("Re[-i G_i] - (2 F_1 - n) =", sp.simplify(sp.re(sp.expand(-i * Gi)) - (2 * F(1) - n)), "; Re[G_i] - (2 F_0 - n) =", sp.simplify(sp.re(Gi) - (2 * F(0) - n)))
print("-i G_i(delta) - G_i(delta - pi/4) =", sp.simplify(sp.expand_complex(-i * (-r**2 * sp.exp(2 * i * d)) + r**2 * sp.exp(2 * i * (d - sp.pi / 4)))))
w = sp.exp(-i * sp.pi / 4)
print("Feld mal e^{-i pi/4}: (e^{-i pi/4})^2 + i =", sp.simplify(w**2 + i), "; volle Tachyon-Abbildung z -> i z: i^2 =", i**2, "(G -> -G)")


def fold(x):
    x = x % (2 * mp.pi / 3)
    return min(x, 2 * mp.pi / 3 - x)


mp.mp.dps = 25
print("Minima von sgn * Re[(-i)^q G_i] = -sgn r^2 cos(2 delta - q pi/2), gefaltet:")
for q in range(4):
    for sgn in (+1, -1):
        base = q * mp.pi / 4 + (0 if sgn > 0 else mp.pi / 2)
        mins = sorted({mp.nstr(fold(base + kk * mp.pi), 12) for kk in range(2)})
        print(f"   q = {q}, Vorzeichen {'+' if sgn > 0 else '-'}: {mins}")
print("   pi/12 =", mp.nstr(mp.pi / 12, 12), "; pi/6 =", mp.nstr(mp.pi / 6, 12), "; pi/4 =", mp.nstr(mp.pi / 4, 12), "; pi/3 =", mp.nstr(mp.pi / 3, 12))

print("\n== H170e: Wick-Woerterbuch gegen den Versatz ==")
BETA = mp.mpf("0.5494056410"); DSTAR = mp.mpf("0.2222220470731")
e0 = mp.atanh(BETA); gd = mp.asin(BETA); at = mp.atan(BETA); x = mp.pi / 12 - DSTAR
print("eps0 =", mp.nstr(e0, 12), "; gd(eps0) = arcsin beta =", mp.nstr(gd, 12), "; arctan beta =", mp.nstr(at, 12), "; x =", mp.nstr(x, 12))
targets = {"x": x, "2x": 2 * x, "tan x": mp.tan(x), "tan 2x": mp.tan(2 * x)}
base = {"gd - pi/6": gd - mp.pi / 6, "pi/6 - arctan beta": mp.pi / 6 - at, "eps0 - gd": e0 - gd, "eps0 - pi/6": e0 - mp.pi / 6,
        "pi/4 - eps0": mp.pi / 4 - e0, "gd - arctan beta": gd - at, "pi/4 - gd": mp.pi / 4 - gd}
cands = {}
for kname, val in base.items():
    cands[kname] = val; cands["(" + kname + ")/2"] = val / 2; cands["2(" + kname + ")"] = 2 * val
rows = []
for tn, tv in targets.items():
    for kn, kv in cands.items():
        rows.append((abs(kv / tv - 1), tn, kn, kv))
rows.sort()
print("Vergleiche:", len(rows), "; Treffer (< 1e-3):", sum(1 for rr in rows if rr[0] < mp.mpf("1e-3")))
for rr in rows[:6]:
    print(f"   {rr[1]:>7} gegen {rr[2]:<26} = {mp.nstr(rr[3], 10):>14}: relativ {mp.nstr(rr[0], 4)}")
