"""k364 (H169): Erzwingt der Chiralitaetsprojektor (1 + i L_e7)/2 die Ladungsmischung c = 1?
Vorab-Notiz Vorab_Notiz_H169_Projektor_und_Ladungsmischung.md (Commit e462469).
Aufruf: python3 k364_test_h169.py > k364_out.txt
Darstellung: inneres j = e7 als reelle 2x2-Matrix, aeusseres i als komplexe Zahl; beide vertauschen.
"""
import sympy as sp

I2 = sp.eye(2)
J = sp.Matrix([[0, -1], [1, 0]])          # j, j^2 = -1
i = sp.I


def bc(a, b):
    """a + b j (a, b aeussere komplexe Zahlen)"""
    return a * I2 + b * J


def sig(M):
    """sigma: j -> -j (inneres Konjugieren) = Transponieren der 2x2-Darstellung"""
    return M.T


def zero(M):
    return sp.simplify(sp.Matrix(M)) == sp.zeros(*sp.Matrix(M).shape)


c, s, v, r, de, x1, x2, x3, a = sp.symbols('c s v r delta x1 x2 x3 a')
P = (I2 + i * J) / 2
Pb = (I2 - i * J) / 2

print("== H169a: Projektor als Mitglied der Familie 1 + c j ==")
print("P^2 - P = 0:", zero(P * P - P), "; Pb^2 - Pb = 0:", zero(Pb * Pb - Pb), "; P Pb = 0:", zero(P * Pb), "; P + Pb = 1:", zero(P + Pb - I2))
print("1 + c j - [(1 - i c) P + (1 + i c) Pb] = 0:", zero(bc(1, c) - ((1 - i * c) * P + (1 + i * c) * Pb)))
E = bc(1, c) / 2
sol = sp.solve(list(sp.expand(E * E - E)), c)
print("(1 + c j)/2 idempotent genau fuer c =", sol)
print("2P - (1 + c j) bei c = i: Nullrest", zero(2 * P - bc(1, c).subs(c, i)), "; 2Pb bei c = -i:", zero(2 * Pb - bc(1, c).subs(c, -i)))
H = bc(1, 1) / 2
print("((1 + j)/2)^2 - j/2 = 0:", zero(H * H - J / 2), " (kein Projektor; (1+j)/sqrt2 = Drehung um pi/4:",
      zero(bc(1, 1) / sp.sqrt(2) - (sp.cos(sp.pi / 4) * I2 + sp.sin(sp.pi / 4) * J)), ")")

print("\n== H169b: Invarianten von Z_a bei a = +-i (H_3 ueber C(x)C) ==")
xs = [x1, x2, x3]


def Zmat(aa):
    w = [bc(-aa, 1) * xk for xk in xs]                # Eintraege (-a + j) x_k
    Z = sp.zeros(6, 6)
    pos = [(0, 1), (1, 2), (2, 0)]
    for (p, q), wk in zip(pos, w):
        Z[2 * p:2 * p + 2, 2 * q:2 * q + 2] = wk
        Z[2 * q:2 * q + 2, 2 * p:2 * p + 2] = sig(wk)  # inner-hermitesch
    return Z


def tr3(M):
    """Spur ueber die 3 Plaetze, Ergebnis bikomplex (2x2)"""
    return sum((M[2 * k:2 * k + 2, 2 * k:2 * k + 2] for k in range(3)), sp.zeros(2, 2))


Z = Zmat(a)
Z2 = Z * Z
Z3 = Z2 * Z
Z4 = Z2 * Z2
n2 = x1**2 + x2**2 + x3**2
T2 = sp.simplify(tr3(Z2)); T4 = sp.simplify(tr3(Z4)); T3 = sp.simplify(tr3(Z3))
print("Tr Z^2 - 2(1+a^2)|x|^2 = 0:", zero(T2 - 2 * (1 + a**2) * n2 * I2))
print("Tr Z^4 - 2(1+a^2)^2 |x|^4 = 0:", zero(sp.expand(T4 - 2 * (1 + a**2)**2 * n2**2 * I2)))
# N(Z) fuer spurfreies Z: N = Tr Z^3 / 3
print("N(Z) = Tr Z^3/3; N - 2(3a - a^3) x1x2x3 = 0:", zero(sp.expand(T3 / 3 - 2 * (3 * a - a**3) * x1 * x2 * x3 * I2)))
for aa in (i, -i):
    print(f"  a = {aa}: Tr Z^2 = {sp.simplify(T2.subs(a, aa))[0, 0]}, Tr Z^4 = {sp.simplify(T4.subs(a, aa))[0, 0]}, "
          f"N(Z) = {sp.factor(sp.simplify((T3 / 3).subs(a, aa))[0, 0])}")
print("  a = 1 (zum Vergleich): Tr Z^2 =", sp.factor(T2.subs(a, 1)[0, 0]), ", N(Z) =", sp.factor((T3 / 3).subs(a, 1)[0, 0]))
print("Eintrag bei a = i: (-i + j) = 2 j P ? Nullrest", zero(bc(-i, 1) - 2 * J * P))
sp_, vp = sp.symbols("sp vp")
print("Spin-1-Term (1 + c^2) v'^2 bei c = +-i:", sp.simplify(((1 + c**2) * vp**2).subs(c, i)), sp.simplify(((1 + c**2) * vp**2).subs(c, -i)))

print("\n== H169c: reelles c als relative Phase der Chiralitaetsanteile ==")
z = r * (sp.cos(de) * I2 + sp.sin(de) * J)            # r e^{j delta}
print("P z - r e^{-i delta} P = 0:", zero((P * z - r * sp.exp(-i * de) * P).applyfunc(lambda e: sp.simplify(e.rewrite(sp.cos)))),
      "; Pb z - r e^{+i delta} Pb = 0:", zero((Pb * z - r * sp.exp(i * de) * Pb).applyfunc(lambda e: sp.simplify(e.rewrite(sp.cos)))))
chi = sp.atan(c)
mix = bc(1, c)
print("(1 + c j) - sqrt(1+c^2) e^{j chi} = 0:", zero(sp.simplify(mix - sp.sqrt(1 + c**2) * (sp.cos(chi) * I2 + sp.sin(chi) * J))))
print("sigma(P) = Pb:", zero(sig(P) - Pb), "; sigma(z) = r e^{-j delta}:", zero(sig(z) - r * (sp.cos(de) * I2 - sp.sin(de) * J)))
zz = bc(s, v)
print("C sigma: j * sigma(s + j v) - (v + j s) = 0:", zero(J * sig(zz) - bc(v, s)))
print("relative Phase P gegen Pb bei c = 1: Faktor (1 + i c)/(1 - i c) =", sp.simplify(((1 + i * c) / (1 - i * c)).subs(c, 1)),
      "; bei c = 0:", sp.simplify(((1 + i * c) / (1 - i * c)).subs(c, 0)))

print("\n== H169d: sigma-Paritaet des Spin-1-Terms ==")
d = sp.symbols('d', real=True)
cr = sp.symbols('c', real=True)
chi_r = sp.atan(cr)
f = -sp.cos(2 * (d - chi_r))
fe = sp.simplify(sp.expand_trig((f + f.subs(d, -d)) / 2))
fo = sp.simplify(sp.expand_trig((f - f.subs(d, -d)) / 2))
print("gerader Teil:", sp.simplify(fe), "; ungerader Teil:", sp.simplify(fo))
ce = sp.simplify(sp.cos(2 * chi_r)); co = sp.simplify(sp.sin(2 * chi_r))
print("cos 2chi =", ce, "; sin 2chi =", co)
print("rein sigma-ungerade (cos 2chi = 0) genau fuer c =", sp.solve(sp.numer(sp.together(ce)), cr),
      "; rein sigma-gerade (sin 2chi = 0) genau fuer c =", sp.solve(sp.numer(sp.together(co)), cr), "(und c -> unendlich)")
# Spin-1-Term in ungemischten Koordinaten: z = s + j v = (1 + c j)(s' + j v')
spv = sp.solve([sp.Eq(s, sp_ - c * vp), sp.Eq(v, vp + c * sp_)], [sp_, vp])
T1 = sp.simplify((1 + c**2) * spv[vp]**2)
print("(1 + c^2) v'^2 in (s, v):", sp.factor(T1))
print("  c = 1: minus [(s^2 + v^2)/2 - s v] =", sp.simplify(T1.subs(c, 1) - ((s**2 + v**2) / 2 - s * v)),
      "; invariant unter s <-> v:", sp.simplify(T1.subs(c, 1) - T1.subs(c, 1).subs({s: v, v: s}, simultaneous=True)) == 0,
      "; unter v -> -v:", sp.simplify(T1.subs(c, 1) - T1.subs(c, 1).subs(v, -v)) == 0)
print("  c = 0:", T1.subs(c, 0), "; invariant unter v -> -v:", sp.simplify(T1.subs(c, 0) - T1.subs(c, 0).subs(v, -v)) == 0,
      "; unter s <-> v:", sp.simplify(T1.subs(c, 0) - T1.subs(c, 0).subs({s: v, v: s}, simultaneous=True)) == 0)
print("  allgemeines c, invariant unter s <-> v genau fuer c =",
      sp.solve(sp.Poly(sp.expand(sp.numer(sp.together(T1 - T1.subs({s: v, v: s}, simultaneous=True)))), s, v).coeffs(), c))

print("\n== H169e: Beimischung der anderen Paritaet in beiden Sektoren (Bericht) ==")
import mpmath as mp
mp.mp.dps = 20
DSTAR = mp.mpf('0.2222220470731')
x = mp.pi / 12 - DSTAR
print("x = pi/12 - delta* =", mp.nstr(x, 12), "; tan 2x =", mp.nstr(mp.tan(2 * x), 12))
# V = X cos 2d + Y sin 2d; stationaer bei tan 2d = Y/X; Minimum, wenn X cos 2d + Y sin 2d < 0.
for name, t, pure in (("geladen (rein ungerade + gerade Beimischung X/Y)", DSTAR, "odd"), ("neutral (rein gerade + ungerade Beimischung Y/X)", mp.pi / 6 - x, "even")):
    print(name, "; Ziel gefaltet", mp.nstr(t, 12))
    for sgn in (+1, -1):
        for k in range(3):
            dd = sgn * t + 2 * mp.pi * k / 3
            ratio = mp.cot(2 * dd) if pure == "odd" else mp.tan(2 * dd)
            # Vorzeichen des reinen Terms, damit dd ein Minimum ist
            main = mp.sin(2 * dd) if pure == "odd" else mp.cos(2 * dd)
            print(f"   delta = {'+' if sgn > 0 else '-'}t + 2pi*{k}/3 = {mp.nstr(dd, 9):>12}: Verhaeltnis = {mp.nstr(ratio, 10):>14}, "
                  f"Vorzeichen des reinen Terms im Minimum: {'-' if main > 0 else '+'}")
