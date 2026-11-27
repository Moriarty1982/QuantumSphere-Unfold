"""k406 (Erkundung, nicht blind): Durchlaeuft der Turm beim Hochgehen zyklisch wieder eine Stufe vom Typ HS(-1)?
HS(-1)-Typ nach k405: R (+) R = R[Z2], Stunde 7 = -1 der Clifford-Uhr (Zentrum mit einem j, j^2 = +1).
Zwei Uhren: (A) Clifford-Geschwister Cl(0,n) derselben Dimension 2^n; (B) vertraegliche Kreisachsen im Turm selbst (k254).
Konvention Cayley-Dickson wie k253: (a,b)(c,d) = (ac - d* b, d a + b c*).
Aufruf: python k406_rueckkehr.py > k406_out.txt   (optional: hoechste Stufe als Argument, Standard 11)
"""
import math, random
import numpy as np
random.seed(406)

# ---------- Cayley-Dickson-Vorzeichen: e_a e_b = s(a,b) e_(a xor b) ----------
def cd_sign_table(n):
    if n == 0: return np.ones((1, 1), dtype=np.int8)
    S = cd_sign_table(n - 1); h = S.shape[0]
    cj = -np.ones(h, dtype=np.int8); cj[0] = 1            # Konjugation auf Basis
    T = np.zeros((2 * h, 2 * h), dtype=np.int8)
    idx = np.arange(h)
    for a in range(h):
        for b in range(h):
            x = a ^ b
            T[a, b] = S[a, b]                              # (a,0)(c,0) = (ac,0)
            T[a, b + h] = S[b, a]                          # (a,0)(0,d) = (0, d a)
            T[a + h, b] = S[a, b] * cj[b]                  # (0,b)(c,0) = (0, b c*)
            T[a + h, b + h] = -cj[b] * S[b, a]             # (0,b)(0,d) = (-d* b, 0)
    return T

def check_against_k253(n):
    def conj(x):
        y = -x.copy(); y[0] = x[0]; return y
    def mul(x, y):
        m = len(x)
        if m == 1: return x * y
        h = m // 2; a, b, c, d = x[:h], x[h:], y[:h], y[h:]
        return np.concatenate([mul(a, c) - mul(conj(d), b), mul(d, a) + mul(b, conj(c))])
    N = 2 ** n; E = np.eye(N); T = cd_sign_table(n)
    return all(abs(mul(E[a], E[b])[a ^ b] - T[a, b]) < 1e-12 for a in range(N) for b in range(N))

def Lmat(T, i):      # Linksmultiplikation mit e_i als vorzeichenbehaftete Permutation: (perm, sign), e_k -> sign[k] e_perm[k]
    N = T.shape[0]; k = np.arange(N); return (k ^ i, T[i, k].astype(np.int64))
def Rmat(T, i):
    N = T.shape[0]; k = np.arange(N); return (k ^ i, T[k, i].astype(np.int64))
def comp(A, B):      # A nach B: e_k -> B -> A
    pB, sB = B; pA, sA = A; return (pA[pB], sB * sA[pB])
def same(A, B, f=1): return np.array_equal(A[0], B[0]) and np.array_equal(A[1], f * B[1])
def ident(N): return (np.arange(N), np.ones(N, dtype=np.int64))
def dense(A):
    N = len(A[0]); M = np.zeros((N, N)); M[A[0], np.arange(N)] = A[1]; return M

def max_anticommuting(ops, bound):
    m = len(ops)
    adj = [[False] * m for _ in range(m)]
    for i in range(m):
        for j in range(i):
            adj[i][j] = adj[j][i] = same(comp(ops[i], ops[j]), comp(ops[j], ops[i]), -1)
    nb = [set(j for j in range(m) if adj[i][j]) for i in range(m)]
    best = []
    import sys; sys.setrecursionlimit(10000)
    class Done(Exception): pass
    def bk(R, P, X):          # Bron-Kerbosch mit Pivot, Abbruch bei Erreichen der Radon-Hurwitz-Schranke
        nonlocal best
        if len(R) > len(best): best = list(R)
        if len(best) >= bound: raise Done
        if not P or len(R) + len(P) <= len(best): return
        u = max(P | X, key=lambda v: len(P & nb[v]))
        for v in list(P - nb[u]):
            bk(R + [v], P & nb[v], X & nb[v]); P = P - {v}; X = X | {v}
    try: bk([], set(range(m)), set())
    except Done: pass
    return sorted(best)

def radon_hurwitz(N):     # rho(N), N = 2^(4d+c) * ungerade: rho = 8d + 2^c
    b = 0
    while N % 2 == 0: N //= 2; b += 1
    return 8 * (b // 4) + 2 ** (b % 4)

import sys
NMAX = int(sys.argv[1]) if len(sys.argv) > 1 else 11   # n = 11 braucht etwa eine Minute
TYP = {0: "R", 1: "C", 2: "H", 3: "H(+)H", 4: "H", 5: "C", 6: "R", 7: "R(+)R"}

print("=" * 110)
print("Kontrolle der Vorzeichentabelle gegen die rekursive Multiplikation aus k253, n = 0..5:", [check_against_k253(n) for n in range(6)])
print("=" * 110)
print("UHR A: Clifford-Geschwister Cl(0,n), gleiche Dimension 2^n und gleiche Beschriftung (Z2)^n wie HS(n)")
print("=" * 110)
def clifford_sign(n):     # e_A e_B = s e_(A xor B), Erzeuger quadrieren zu -1 und antikommutieren
    N = 2 ** n; T = np.zeros((N, N), dtype=np.int8)
    for A in range(N):
        for B in range(N):
            s = 0
            for i in range(n):
                if B >> i & 1: s += bin(A >> (i + 1)).count("1")
            s += bin(A & B).count("1")
            T[A, B] = -1 if s % 2 else 1
    return T
print(" n  dim   omega^2   omega zentral   Zentrum        Typ (Stunde n mod 8)        HS(-1)-Typ?")
for n in range(0, 10):
    T = clifford_sign(n); N = 2 ** n; top = N - 1
    if n == 0:
        print(f" 0    1      -          -          R              R                           nein  <- HS(0)"); continue
    w2 = T[top, top]; central = all(T[top, k] == T[k, top] for k in range(N))
    centre = sum(1 for A in range(N) if all(T[A, k] == T[k, A] for k in range(N)))
    ctyp = "R" if centre == 1 else ("C" if w2 == -1 else "R(+)R")
    hit = "JA" if (centre == 2 and w2 == 1 and TYP[n % 8] == "R(+)R") else ("Vorzeichen, quaternionisch" if centre == 2 and w2 == 1 else "nein")
    print(f" {n}  {N:4d}    {w2:+d}        {str(central):5}       {ctyp:6} (dim {centre})  {TYP[n % 8]:8} x Matrizen          {hit}")
print(" Ergebnis Uhr A: Zentrum R(+)R (ein j mit j^2 = +1, zentral) bei n = 3 und n = 7; Stunde 7 = -1 (reell) bei n = 7, 15, ...; Periode 8.")

print()
print("=" * 110)
print("UHR B: der Turm selbst. Groesste Menge paarweise antikommutierender Linksmultiplikationen L_(e_i) (k254), ihr Produkt omega")
print("=" * 110)
print(" (Suche exakt: Bron-Kerbosch ueber alle Basis-Einheiten; rho(2^n)-1 ist die Obergrenze fuer beliebige Richtungen)")
print(" n  dim  Achsen a  rho(2^n)-1  a mod 8  Typ der Stunde   omega^2  omega zentral  omega (links)               omega (rechts)              Rang der erzeugten Algebra")
rows = {}
for n in range(0, NMAX + 1):
    N = 2 ** n; T = cd_sign_table(n); rh = radon_hurwitz(N) - 1
    if n == 0:
        print(f" 0    1     0          0          0     R                 -         -            -               -            1"); rows[0] = (0, None); continue
    ops = [Lmat(T, i) for i in range(1, N)]
    cl = max_anticommuting(ops, rh)
    a = len(cl)
    def omega(maker):
        W = ident(N)
        for i in cl: W = comp(W, maker(T, i + 1))
        return W
    W = omega(Lmat); W2 = comp(W, W)
    w2 = "+1" if same(W2, ident(N)) else ("-1" if same(W2, ident(N), -1) else "?")
    central = all(same(comp(W, ops[i]), comp(ops[i], W)) for i in cl)
    anti = all(same(comp(W, ops[i]), comp(ops[i], W), -1) for i in cl)
    def name(W):
        if same(W, ident(N)): return "+1 (Skalar)"
        if same(W, ident(N), -1): return "-1 (Skalar)"
        if same(comp(W, W), ident(N)):                  # Involution: Eigenwerte +-1, Anzahl aus der Spur
            tr = int(W[1][W[0] == np.arange(N)].sum()); return f"{(N + tr)//2} mal +1, {(N - tr)//2} mal -1"
        return "kein Skalar"
    # Rechtsmultiplikationen derselben Einheiten (nur sinnvoll, wenn sie ebenfalls antikommutieren)
    rops = [Rmat(T, i + 1) for i in cl]
    r_ok = all(same(comp(rops[x], rops[y]), comp(rops[y], rops[x]), -1) for x in range(a) for y in range(x))
    WR = ident(N)
    for r in rops: WR = comp(WR, r)
    rname = name(WR) if r_ok else "(antikomm. nicht)"
    rank = "-"
    if a <= 11 and N <= 64:
        words = []
        for bits in range(2 ** a):
            Wd = ident(N)
            for t in range(a):
                if bits >> t & 1: Wd = comp(Wd, ops[cl[t]])
            words.append(dense(Wd).ravel())
        rank = f"{np.linalg.matrix_rank(np.array(words))} von {N*N}"
    print(f" {n}  {N:3d}    {a:2d}         {rh:2d}         {a % 8}     {TYP[a % 8]:8}          {w2}      {'ja' if central else ('nein, antikomm.' if anti else 'nein'):14} {name(W):26}  {rname:26} {rank}")
    rows[n] = (a, name(W))
h7 = [n for n in rows if rows[n][0] % 8 == 7]; h3 = [n for n in rows if rows[n][0] % 8 == 3]
print(f" Gemessene Achsenzahlen n = 0..{NMAX}: {[rows[n][0] for n in sorted(rows)]}")
print(f" Radon-Hurwitz-Obergrenze    n = 0..{NMAX}: {[radon_hurwitz(2**n) - 1 for n in sorted(rows)]}")
print(f" a = n + 4 fuer n >= 3: {all(rows[n][0] == n + 4 for n in rows if n >= 3)}")
print(f" Stunde 7 = -1 (Typ R(+)R) gemessen bei n = {h7}; dort omega = {[rows[n][1] for n in h7]}")
print(f" Stunde 3 (Typ H(+)H) gemessen bei n = {h3}; dort omega = {[rows[n][1] for n in h3]}")
print(" Folge: Bis HS(3) springt die Uhr (0, 1, 3, 7). Ab HS(3) geht sie fuer die Basis-Einheiten jede Stufe genau eine Stunde weiter.")
print(" Mit a = n + 4 liegt die naechste Stunde 7 bei n = 11, dann 19 (Periode 8); Stunde 0 bei n = 4, 12, 20.")

print()
print("=" * 110)
print("Obergrenze nach Radon-Hurwitz (Lesart aus k254), rueckwaerts fortgesetzt: a(n+4) = a(n) + 8 -> a(-1) = a(3) - 8, usw.")
print("Negative Achsenzahl = Achsen mit Quadrat +1. Diese Tabelle ist Formel, nicht Messung.")
print("=" * 110)
a_of = {n: radon_hurwitz(2 ** n) - 1 for n in range(0, 12)}
for n in range(-4, 0): a_of[n] = a_of[n + 4] - 8
POS = {1: "R(+)R", 5: "M2(H)(+)M2(H)", 7: "M8(C)", 8: "M16(R)"}
print(" n   Achsen a   Stunde a mod 8   Typ      gleiche Stunde wie")
for n in range(-4, 12):
    a = a_of[n]; same_h = [m for m in range(-4, 12) if m != n and a_of[m] % 8 == a % 8]
    extra = f"  (als Cl({-a},0) = {POS[-a]})" if a < 0 else ""
    print(f" {n:2d}     {a:3d}          {a % 8}         {TYP[a % 8]:6}   HS({'), HS('.join(str(m) for m in same_h)}){extra}")
print(" Nach der Obergrenze: Block mit HS(0) als Anfang  = HS(0..3),  Stunden 0,1,3,7; Rueckkehr zum Typ von HS(0)  bei HS(4), HS(8)  (k254).")
print("                      Block mit HS(-1) als Anfang = HS(-1..2), Stunden 7,0,1,3; Rueckkehr zum Typ von HS(-1) bei HS(3), HS(7), HS(11).")
print(" Gemessen (Basis-Einheiten): Rueckkehr zum Typ von HS(-1) bei HS(3), dann erst HS(11); zum Typ von HS(0) bei HS(4), dann HS(12).")

print()
print("=" * 110)
print("Der Schritt von Stunde 7 auf Stunde 0: HS(-1) -> HS(0) entspricht HS(3) -> HS(4) (Oktonionen -> Sedenionen)")
print("=" * 110)
T3, T4 = cd_sign_table(3), cd_sign_table(4)
L3 = [Lmat(T3, i) for i in range(1, 8)]; R3 = [Rmat(T3, i) for i in range(1, 8)]
wl = ident(8); wr = ident(8)
for x in L3: wl = comp(wl, x)
for x in R3: wr = comp(wr, x)
print(" HS(3): L1...L7 =", "+1" if same(wl, ident(8)) else "-1", "| R1...R7 =", "+1" if same(wr, ident(8)) else "-1",
      "-> die zwei Haelften von R(+)R sind Links- und Rechtsmultiplikation; das Vorzeichen ist die Haendigkeit des Produkts.")
ops4 = [Lmat(T4, i) for i in range(1, 16)]
cl4 = max_anticommuting(ops4, 8)
W4 = ident(16)
for i in cl4: W4 = comp(W4, ops4[i])
ev = np.linalg.eigvalsh((dense(W4) + dense(W4).T) / 2)
print(f" HS(4): 8 vertraegliche Achsen {[i+1 for i in cl4]}; omega^2 = +1: {same(comp(W4, W4), ident(16))}; "
      f"omega antikommutiert mit allen 8: {all(same(comp(W4, ops4[i]), comp(ops4[i], W4), -1) for i in cl4)}; "
      f"Eigenwerte: {int((ev > 0).sum())} mal +1, {int((ev < 0).sum())} mal -1")
print("   -> aus dem Skalar +-1 (zwei getrennte Welten) wird ein Operator mit beiden Vorzeichen in einem Raum (8 + 8): die zwei Haelften sind verbunden.")
print(" Zum Vergleich unten: R(+)R (HS(-1)-Typ) -> R (HS(0)): die zwei Vorzeichen-Haelften werden zu einer Geraden mit +- darauf.")
