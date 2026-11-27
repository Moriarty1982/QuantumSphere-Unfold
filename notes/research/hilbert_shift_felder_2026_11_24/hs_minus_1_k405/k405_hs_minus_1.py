"""k405 (Erkundung, nicht blind): Wie saehe ein HS(-1) aus, eine Stufe unter HS(0) = R?
Drei Lesarten: (1) Vorzeichen Z2, (2) Koerper mit einem Element F1, (3) Rand des Turms als Ur-Seed.
Konvention Cayley-Dickson wie k253: (a,b)(c,d) = (ac - d* b, d a + b c*).
Aufruf: python k405_hs_minus_1.py > k405_out.txt
"""
import itertools, math
from fractions import Fraction as Fr
import numpy as np

rng = np.random.default_rng(404)

def conj(x):
    y = -x.copy(); y[0] = x[0]; return y

def mul(x, y):
    n = len(x)
    if n == 1: return x * y
    h = n // 2
    a, b, c, d = x[:h], x[h:], y[:h], y[h:]
    return np.concatenate([mul(a, c) - mul(conj(d), b), mul(d, a) + mul(b, conj(c))])

print("=" * 100)
print("TEIL A: Rueckwaertsschritt im Turm. A_{n-1} = gerader Teil der Z2-Graduierung s(a,b) = (a,-b)")
print("=" * 100)
for n in range(0, 6):
    N = 2 ** n
    E = np.eye(N)
    # (i) Indexgruppe: e_a e_b = +- e_{a xor b}  (verdrehte Gruppenalgebra von (Z2)^n = F_2^n)
    ok_xor = True
    for a in range(N):
        for b in range(N):
            p = mul(E[a], E[b]); k = a ^ b
            if abs(abs(p[k]) - 1) > 1e-12 or np.abs(np.delete(p, k)).max(initial=0) > 1e-12: ok_xor = False
    if n == 0:
        # Algebra-Automorphismen von R: lineare Abb. x -> s x mit s*s = s (aus s(xy) = s(x)s(y)) und s != 0
        sols = [s for s in (-1.0, 0.0, 1.0) if abs(s * s - s) < 1e-12 and s != 0]
        print(f"n=0 dim=1 | e_a e_b = +-e_(a xor b): {ok_xor} | imaginaere Einheiten 0 | lineare Automorphismen von R: {sols} "
              f"-> nur die Identitaet, ungerader Teil = {{0}}, kein Schritt nach unten")
        continue
    h = N // 2
    s = np.concatenate([np.ones(h), -np.ones(h)])
    err = 0.0
    for _ in range(200):
        x, y = rng.normal(size=N), rng.normal(size=N)
        err = max(err, np.abs(s * mul(x, y) - mul(s * x, s * y)).max())
    print(f"n={n} dim={N:2d} | e_a e_b = +-e_(a xor b): {ok_xor} | imaginaere Einheiten {N-1} = Punkte von P^{n-1}(F_2) = {2**n-1} | "
          f"s Automorphismus (max Fehler {err:.1e}) | dim Fix(s) = {int((s>0).sum())} = 2^{n-1}")

print()
print("Einheitssphaeren |x| = 1 von A_n: S^(2^n - 1); Sphaere der imaginaeren Einheiten (Wahl von u in k253): S^(2^n - 2)")
for n in range(-1, 5):
    d = Fr(2) ** n
    print(f"  n={n:2d}: dim {str(d):>4} | Einheiten S^({d - 1}) | Wahl von u: S^({d - 2})"
          + ("   <- S^(-1) = leere Menge: bei HS(0) gibt es schon keine Wahl mehr" if n == 0 else "")
          + ("   <- keine Sphaere mit halbzahliger negativer Dimension" if n == -1 else ""))
print("  Dimension 0 (Nullalgebra, Einheiten S^(-1) = leer) liegt bei n = -unendlich, nicht bei n = -1.")

print()
print("=" * 100)
print("TEIL B (Lesart 1): Vorzeichen Z2. Gruppenalgebra R[Z2] = Spaltkomplexe Zahlen (j^2 = +1) als Gegenstueck zu C")
print("=" * 100)
# Clifford: C = Cl(0,1) (e^2 = -1), R[Z2] = Cl(1,0) (f^2 = +1). Graduiertes Tensorprodukt = Cl(1,1): e, f antikommutieren.
e = np.array([[0., -1.], [1., 0.]]); f = np.array([[0., 1.], [1., 0.]]); one = np.eye(2)
print("e^2 = -1:", np.allclose(e @ e, -one), "| f^2 = +1:", np.allclose(f @ f, one), "| ef + fe = 0:", np.allclose(e @ f + f @ e, 0))
span = np.array([m.ravel() for m in (one, e, f, e @ f)])
print("Rang von {1, e, f, ef} in M2(R):", np.linalg.matrix_rank(span), "von 4 -> Cl(0,1) (x) Cl(1,0) = Cl(1,1) = M2(R), Morita-aequivalent zu R")
print("Stufenindex der Clifford-Uhr (Zahl der Einheiten mit Quadrat -1 minus Zahl mit Quadrat +1): C hat +1, R[Z2] hat -1, Summe 0.")
# Bott-Uhr: Stufe -1 = Stufe 7 mod 8. Sieben antikommutierende Einheiten mit Quadrat -1: Linksmultiplikationen der Oktonionen.
E8 = np.eye(8)
L = [np.array([mul(E8[i], E8[j]) for j in range(8)]).T for i in range(1, 8)]
ok_sq = all(np.allclose(m @ m, -E8) for m in L)
ok_ac = all(np.allclose(L[a] @ L[b] + L[b] @ L[a], 0) for a in range(7) for b in range(a))
om = E8.copy()
for m in L: om = om @ m
words = []
for bits in range(128):
    w = E8.copy()
    for i in range(7):
        if bits >> i & 1: w = w @ L[i]
    words.append(w.ravel())
print("Cl(0,7) aus den 7 Oktonion-Einheiten (Linksmultiplikation): Quadrate -1:", ok_sq, "| antikommutieren:", ok_ac,
      "| Rang der 128 Worte:", np.linalg.matrix_rank(np.array(words)), "von 64 = dim M8(R)")
print("   Volumenelement L1...L7 =", "+1" if np.allclose(om, E8) else ("-1" if np.allclose(om, -E8) else "anderes"),
      "-> Cl(0,7) = M8(R) (+) M8(R); die zwei Summanden unterscheidet nur das Vorzeichen +-1 dieses Produkts (Links- gegen Rechtsmultiplikation)")
R_ = [np.array([mul(E8[j], E8[i]) for j in range(8)]).T for i in range(1, 8)]
omR = E8.copy()
for m in R_: omR = omR @ m
print("   Rechtsmultiplikation: R1...R7 =", "+1" if np.allclose(omR, E8) else ("-1" if np.allclose(omR, -E8) else "anderes"))
print("   Stufe 7 ist Morita-aequivalent zu R (+) R = R[Z2]: in der Bott-Uhr (Periode 8) ist Stufe -1 = Stufe 7.")
# Bahn psi' = u w psi mit u = j, j^2 = +1
t = np.linspace(0, 2, 5)
print("Bahnregel psi' = u w psi mit u = f (f^2 = +1): exp(f t) = cosh t + f sinh t")
for tt in t:
    M = np.cosh(tt) * one + np.sinh(tt) * f
    # Reihenvergleich
    S = sum(np.linalg.matrix_power(f * tt, k) / math.factorial(k) for k in range(40))
    print(f"   t={tt:.1f}: cosh={np.cosh(tt):8.4f} sinh={np.sinh(tt):8.4f} | Reihe - geschlossen = {np.abs(S-M).max():.1e} | "
          f"Norm x^2-y^2 = {np.cosh(tt)**2-np.sinh(tt)**2:.6f}")
ep, em = (one + f) / 2, (one - f) / 2
print("Idempotente e+- = (1 +- f)/2: e+^2 = e+:", np.allclose(ep @ ep, ep), "| e+ e- = 0 (Nullteiler):", np.allclose(ep @ em, 0),
      "| e+ + e- = 1:", np.allclose(ep + em, one))
print("e+ = (1 + sigma_x)/2 ist der HC-Projektor aus r70 (C_HC = (1 + sigma_x)/2):", np.allclose(ep, np.array([[.5, .5], [.5, .5]])))
print("Konjugation f -> -f vertauscht e+ und e-: zwei Ports. Element p e+ + q e- hat Norm p*q.")

def gammaL(area, K=4000):
    lo, hi = 1.0, 3.0
    F = lambda g: sum(2.0 ** (1 - g * area(k)) for k in range(1, K)) - 1
    for _ in range(200):
        mid = (lo + hi) / 2
        if F(mid) > 0: lo = mid
        else: hi = mid
    return (lo + hi) / 2
cas = lambda k: math.sqrt(k * (k + 2) / 3)
glatt = lambda k: (k + 1) / 2
gL = gammaL(cas); bs = math.sqrt((gL - 1) / (gL + 1)); x = bs ** 2
print(f"Zaehlregel (Postulat r67): gamma_L = {gL:.10f}, beta_sym = {bs:.10f}, x = beta_sym^2 = {x:.7f}")
print("Frames als Port-Gewichte (r69.4): R 1:0, M 1:x, T x:1, P 1:1")
for nm, (p, q) in {"R": (1, 0), "M": (1, x), "T": (x, 1), "P": (1, 1)}.items():
    norm = p * q
    rap = "unendlich (Nullteiler, Lichtkegel der Spaltebene)" if norm == 0 else f"{0.5*math.log(p/q):+.6f}"
    print(f"   {nm}: (p,q) = ({p:.6f},{q:.6f}) | Norm p*q = {norm:.6f} | Rapiditaet phi = (1/2) ln(p/q) = {rap}")
print(f"   Vergleich: phi_M = ln(1/beta_sym) = {math.log(1/bs):.6f}; eps = artanh(beta_sym) = {math.atanh(bs):.6f}; "
      f"Verhaeltnis {math.log(1/bs)/math.atanh(bs):.5f} (nicht gleich)")
print(f"   M und T gehen durch die Konjugation f -> -f ineinander ueber (phi -> -phi); P ist reell (phi = 0); R ist ein Idempotent.")

print()
print("Gruppoid-Zaehlung (Baez-Dolan): |X//G| = Summe ueber Bahnen 1/|Stabilisator|")
def gcard(X, act):
    seen, tot = set(), Fr(0)
    for p in X:
        if p in seen: continue
        orb = {p, act(p)}; seen |= orb
        tot += Fr(1, 2 // len(orb))
    return tot
print("   {+1,-1}//Z2 (Vorzeichen, freie Wirkung):", gcard([1, -1], lambda p: -p))
print("   {0}//Z2 (Nullpunkt, Vorzeichen wirkt unsichtbar):", gcard([0], lambda p: -p), " <- einzige Menge mit 'Groesse' 1/2 = 2^(-1)")
print("   {-2..2}//Z2:", gcard(list(range(-2, 3)), lambda p: -p), " = 5/2: die halbe Gerade plus halber Nullpunkt")

print()
print("=" * 100)
print("TEIL C: Negative Stufen in der Zaehlregel. Gewicht eines Durchstosspunkts mit Spin j = k/2: p_k = 2^(1 - gamma a_k)")
print("=" * 100)
print(" k   j    glatt: a=(k+1)/2, gamma=2        Casimir: a=sqrt(k(k+2)/3), gamma=gamma_L")
print("           p_k        log2 p_k              p_k         log2 p_k   (effektive Stufe)")
sg = sc = 0.0
for k in range(1, 9):
    pg = 2.0 ** (1 - 2 * glatt(k)); pc = 2.0 ** (1 - gL * cas(k)); sg += pg; sc += pc
    print(f" {k}  {k/2:3.1f}   {pg:.8f}  {math.log2(pg):+.4f}             {pc:.8f}  {math.log2(pc):+.4f}")
print(f" Summe k=1..8: glatt {sg:.8f}, Casimir {sc:.8f}; Summe ueber alle k: je 1 (Definition von gamma)")
print(f" glatt: p_k = 2^(-k) exakt = formale Dimension von HS(-k); Summe_(k>=1) dim HS(-k) = 1 = dim HS(0)")
p1 = 2 ** (1 - gL)
print(f" Casimir: p_1 = 2^(1-gamma_L) = {p1:.7f}; beta_sym = {bs:.7f}; Unterschied {bs-p1:+.7f} ({abs(bs-p1)/bs*100:.3f} %), schon in k396 vermerkt, ungeklaert")

print()
print("=" * 100)
print("TEIL D (Lesart 3): Rand des Turms als Ur-Seed. Schleife L3 aus k395: b' = 1 - 2b(1-b)")
print("=" * 100)
bb = np.linspace(-0.5, 1.5, 2001); cc = 2 * bb - 1
print("Mit c = 2b - 1: c' - c^2 (max ueber 2001 Punkte) =", f"{np.abs((2*(1-2*bb*(1-bb))-1) - cc**2).max():.1e}", "-> L3 ist die Quadrierabbildung c -> c^2")
for c0 in (0.9, -0.9, 0.3, -0.3):
    c = c0; tr = []
    for _ in range(7): c = c * c; tr.append(c)
    print(f"   Start c = {c0:+.1f} (b = {(1+c0)/2:.2f}): " + ", ".join(f"{v:.3e}" for v in tr))
print("   Nach einem Schritt sind +c und -c gleich: das Vorzeichen (1 Bit) ist weg. Fixpunkte c = 0 (b = 1/2, Steigung 0) und c = 1 (b = 1, Steigung 2).")
print("   Rueckwaerts (Wurzelziehen) verdoppelt jeder Schritt die Zahl der Vorgaenger:")
for n in range(0, 6):
    pts = {complex(0.37)}
    for _ in range(n):
        new = set()
        for z in pts:
            r = np.sqrt(z + 0j); new |= {complex(np.round(r, 12)), complex(np.round(-r, 12))}
        pts = new
    reell = sum(1 for z in pts if abs(z.imag) < 1e-9)
    print(f"      {n} Schritte zurueck: {len(pts):2d} Vorgaenger in C = 2^{n} = dim HS({n}); davon reell: {reell}")
print("   Reell bleiben immer nur 2 Vorgaenger (+-): in R endet die Verzweigung nach einem Bit; die volle Verdopplung braucht C.")

print()
print("=" * 100)
print("TEIL E (Lesart 2): Koerper mit einem Element. Basis 2 des Turms durch q ersetzen, Grenzfall q -> 1")
print("=" * 100)
def qint(n, q):
    q = Fr(q)
    if q == 1: return Fr(n)
    return (q ** n - 1) / (q - 1)
print(" n   dim q^n (q=2)  dim (q=1)   imag. Einheiten [n]_q = (q^n-1)/(q-1): q=2    q=3    q=1")
for n in range(-2, 5):
    print(f" {n:2d}   {str(Fr(2)**n):>6}        1          {str(qint(n,2)):>22}  {str(qint(n,3)):>6}  {str(qint(n,1)):>4}")
print(" [n]_2 = 2^n - 1 ist fuer n >= 1 die Zahl der imaginaeren Einheiten und die Punktzahl von P^(n-1)(F_2) (n = 3: Fano-Ebene, 7).")
print(" Bei q = 1 hat jede Stufe Dimension 1 und Stufe n genau n 'Einheiten': der Turm faellt auf HS(0) zusammen.")
print(" Fuer n = -1 bei q = 2: [-1]_2 = -1/2 imaginaere Einheiten, Dimension 1 + (-1/2) = 1/2.")
def gl(n, q):
    r = Fr(1)
    for i in range(n): r *= (Fr(q) ** n - Fr(q) ** i)
    return r
print(" |GL_n(F_q)| / (q-1)^n fuer q -> 1 (Tits: GL_n(F_1) = S_n):")
for n in range(1, 5):
    vals = [gl(n, Fr(1) + Fr(1, 10 ** m)) / Fr(1, 10 ** m) ** n for m in (2, 4, 6)]
    print(f"   n={n}: " + ", ".join(f"{float(v):.6f}" for v in vals) + f"  -> n! = {math.factorial(n)}")
print(" Vorzeichen-Hyperkoerper S = R/R_+ = {0, +1, -1} (Connes-Consani): Summe zweier Klassen = Menge aller Vorzeichen von x + y")
def cls(v): return 0 if v == 0 else (1 if v > 0 else -1)
for a, b in itertools.combinations_with_replacement((1, -1, 0), 2):
    out = set()
    for _ in range(4000):
        xx = 0.0 if a == 0 else a * rng.exponential(); yy = 0.0 if b == 0 else b * rng.exponential()
        out.add(cls(xx + yy))
    if a == -b and a != 0: out.add(0)   # x = -y hat Mass null in der Stichprobe, gehoert aber dazu
    print(f"   ({a:+d}) + ({b:+d}) = {sorted(out)}")
print(" S hat als multiplikatives Monoid {0, +1, -1} = F_(1^2) (quadratische Erweiterung von F_1); weiter geteilt durch +-1: Krasner K = {0,1}, Monoid F_1.")
print(" Kette: R -> S = R/R_+ (nur Vorzeichen, 3 Elemente) -> K = S/{+-1} (nur 'null oder nicht', 2 Elemente).")
