"""k414 (Test H204): Binden B und D eine einzige "Elter"-F4-Darstellung?

Modell: m_s(k) = [A l_k + B l_k^2 + s(C l_k + D l_k^2)]/(l_i+l_j)^2, s=+-1 Ladung.
Offene Stelle: B (ladungsGERADE l_k^2) und D (ladungsUNGERADE l_k^2). Frage: gibt es eine
einzige hoehere F4-Darstellung R, deren Verzweigung D/B darstellungstheoretisch festlegt?

(A) Ladungs-kovariante Operatoralgebra auf dem 36-dim Farbblock (Maschinerie k408):
    erzeugt von {1, iL_U} mit (iL_U)^2=1; Dimension, minimale Idempotente (irred. Komponenten),
    und das je erzwungene (B,D)=(gerade,ungerade) bzw. D/B. Diskrete Verzweigungswerte.
(B) F4-Feldgrad von B und D (Maschinerie k411, sympy): treten sie im selben Grad auf?
(C) Abgleich der diskreten Werte mit dem scharfen Datenwert D/B=1.0085+-0.0010.

Aufruf: python k414_test_h204.py > k414_out.txt
"""
import numpy as np, sympy as sp

# ============================================================================
#  (A) Oktonion-Algebra, Farbblock, Ladungs-kovariante Operatoralgebra (k408)
# ============================================================================
def conj(x):
    y = -x.copy(); y[0] = x[0]; return y
def mul(x, y):
    n = len(x)
    if n == 1: return x * y
    h = n // 2; a, b, c, d = x[:h], x[h:], y[:h], y[h:]
    return np.concatenate([mul(a, c) - mul(conj(d), b), mul(d, a) + mul(b, conj(c))])
e = np.eye(8); C = np.array([[mul(e[i], e[j]) for j in range(8)] for i in range(8)])
LU = np.einsum('i,ijk->kj', e[7], C)[1:7, 1:7]      # L_U auf den 6 Farbrichtungen
I2 = np.eye(2); J2 = np.array([[0, -1.0], [1, 0]])  # Mult. mit i auf (Re,Im)
Ii  = np.kron(J2, np.eye(18))                       # "i" auf dem 36-dim Farbblock (2x3x6)
LUc = np.kron(I2, np.kron(np.eye(3), LU))           # L_U auf dem Farbblock
iLU = Ii @ LUc                                      # i L_U (reelle 36x36)
I36 = np.eye(36)

print("=" * 78)
print("H204 A  Ladungs-kovariante l_k^2-Operatoralgebra auf dem Farbblock")
print("=" * 78)
print(f"  (i L_U)^2 = 1 ?   || (iL_U)^2 - 1 ||_max = {np.abs(iLU@iLU - I36).max():.2e}")

# Dimension der von {1, iL_U} erzeugten (kommutativen) Algebra:
basis = [I36, iLU]                      # 1 und iL_U; hoehere Potenzen (iL_U)^2=1 -> nichts Neues
M = np.stack([b.ravel() for b in basis])
dim = np.linalg.matrix_rank(M, tol=1e-9)
print(f"  dim span{{1, iL_U, (iL_U)^2, ...}} = {dim}  (kommutativ, da (iL_U)^2=1)")

# Minimale Idempotente (irreduzible Komponenten / 'einzelne Darstellungen'):
Pup = 0.5 * (I36 + iLU)                 # +Chiralitaet der Ladung = Up-Typ-Projektor
Pdn = 0.5 * (I36 - iLU)                 # -Chiralitaet = Down-Typ
print(f"  P_up = 1/2(1+iL_U): P^2=P ? {np.abs(Pup@Pup-Pup).max():.1e}  Spur={np.trace(Pup):.3f}")
print(f"  P_dn = 1/2(1-iL_U): P^2=P ? {np.abs(Pdn@Pdn-Pdn).max():.1e}  Spur={np.trace(Pdn):.3f}")
print(f"  Vollstaendig  P_up+P_dn=1 ? {np.abs(Pup+Pdn-I36).max():.1e}")
print(f"  Orthogonal    P_up P_dn=0 ? {np.abs(Pup@Pdn).max():.1e}")

# Ladungs-Eigenraeume (Up: iL_U=+1, Down: iL_U=-1) zum Ablesen von (B,D):
w, V = np.linalg.eigh(iLU)
up = V[:, w > 0]; dn = V[:, w < 0]
def BD(O, name):
    bu = np.diag(up.T @ O @ up).real.mean()
    bd = np.diag(dn.T @ O @ dn).real.mean()
    B = (bu + bd) / 2.0; D = (bu - bd) / 2.0     # gerade / ungerade
    r = D / B if abs(B) > 1e-9 else np.inf
    print(f"    {name:26s}: b_up={bu:+.3f} b_down={bd:+.3f}  B={B:+.3f} D={D:+.3f}  D/B={r:+.4f}")
    return B, D, r

print("\n  Erzwungenes (B,D) je 'einzelner Darstellung' (irred. Komponente):")
print("  (ein l_k^2-Operator O gibt b_up=<O>_up, b_down=<O>_down)")
vals = {}
vals["1"]      = BD(I36,       "O = 1 (ladungsblind)")
vals["iL_U"]   = BD(iLU,       "O = iL_U (J-Form Q0-1/2)")
vals["Pup"]    = BD(Pup,       "O = P_up (irred. +)")
vals["Pdn"]    = BD(Pdn,       "O = P_dn (irred. -)")
disc = sorted({round(v[2], 4) for v in vals.values() if np.isfinite(v[2])} | {np.inf})
print(f"\n  -> Minimale Idempotente: genau ZWEI (P_up, P_dn). Jede 'einzelne Darstellung'")
print(f"     erzwingt D/B in der DISKRETEN Menge {{0 (1), +1 (P_up), -1 (P_dn), oo (iL_U)}}.")
print(f"     Ein allgemeiner Operator a*P_up + b*P_dn braucht ZWEI Koeffizienten (b_up,b_down)")
print(f"     = zwei Komponenten. D/B=1 nur bei REIN P_up (b_down=0 exakt).")

# ============================================================================
#  (B) F4-Feldgrad von B (gerade l_k^2) und D (ungerade l_k^2)  -- k411
# ============================================================================
print("\n" + "=" * 78)
print("H204 B  F4-Feldgrad: koennen B und D in EINER F4-Irrep (einem Grad) liegen?")
print("=" * 78)
lks = sp.symbols('l_k'); e1, e2 = sp.symbols('e1 e2')
sub_vac = {e1: 3 - lks, e2: sp.Rational(3, 2) - lks * (3 - lks)}
s_, pr = sp.symbols('s pr'); sub_sym = {s_: 3 - lks, pr: sp.Rational(3, 2) - 3*lks + lks**2}
def c1c2(expr):
    p = sp.Poly(sp.expand(expr), lks); return p.coeff_monomial(lks), p.coeff_monomial(lks**2)
def hcomp(m):
    H = [sp.Integer(1), e1]
    for k in range(2, m + 1): H.append(sp.expand(e1*H[k-1] - e2*H[k-2]))
    return H[m]
firstB = None
for n in range(2, 7):
    _, c2 = c1c2(sp.expand((2*n*hcomp(n-2)).subs(sub_vac)))
    if firstB is None and c2 != 0: firstB = n
odd_forms = {"c1": sp.Rational(2,3), "c2": sp.Rational(1,3)*s_,
             "c4/c5": sp.Rational(1,3)*(s_**2 - 2*pr), "c7/c9": sp.Rational(1,6)*s_**2,
             "c11": sp.Rational(1,2)*(s_**2 - 2*pr) + sp.Rational(1,3)*pr}
firstD = None
for nm, f in odd_forms.items():
    _, c2 = c1c2(sp.expand(sp.expand(f).subs(sub_sym)))
    if firstD is None and c2 != 0: firstD = 4     # H186-Formen sind Grad 4
print(f"  B (ladungsGERADE l_k^2) zuerst bei Feldgrad : {firstB}")
print(f"  D (ladungsUNGERADE l_k^2) zuerst bei Feldgrad: {firstD}  (H186-Formen, Grad 4)")
same_grade = (firstB == firstD)
print(f"  Gleicher Grad (noetig, damit EINE F4-Irrep beide traegt)? "
      f"{'JA' if same_grade else 'NEIN'}  (B Grad %d, D Grad %d)" % (firstB, firstD))
print("  -> Eine irreduzible F4-Darstellung lebt in EINEM homogenen Tensorgrad (Sym^n des 26).")
print("     B in Sym^5, D in Sym^4 => keine einzelne F4-Irrep kann beide Beine tragen.")

# ============================================================================
#  (C) Abgleich mit dem Datenwert
# ============================================================================
print("\n" + "=" * 78)
print("H204 C  Abgleich: diskrete Verzweigungswerte vs Datenwert D/B")
print("=" * 78)
DB_data, DB_err = 1.0085, 0.0010
disc_vals = {"0 (ladungsblind, O=1)": 0.0, "+1 (chiral P_up)": 1.0,
             "-1 (P_dn)": -1.0, "oo (J-Form, B=0)": np.inf}
print(f"  Datenwert D/B = {DB_data:.4f} +- {DB_err:.4f} (scharf, 4-Param-Fit H197/H202)")
best = None
for nm, v in disc_vals.items():
    if np.isinf(v):
        print(f"    einzelne Darstellung D/B={nm:22s}: unendlich weit (B=0 ausgeschlossen, B!=0)")
        continue
    dsig = abs(DB_data - v) / DB_err
    print(f"    einzelne Darstellung D/B={nm:22s}: |Delta|/sigma = {dsig:7.1f}")
    if best is None or dsig < best[1]: best = (nm, dsig)
print(f"  Naechster diskreter Wert: {best[0]}, {best[1]:.1f} sigma entfernt.")

# ============================================================================
#  Entscheidung (Vorab-Kriterien)
# ============================================================================
print("\n" + "=" * 78)
print("H204 Entscheidung")
print("=" * 78)
K1 = (best[1] <= 2) and same_grade
print(f"  K1 (eine Elter-Darstellung bindet D/B): naechster diskreter Wert {best[1]:.1f} sigma, "
      f"gleicher Grad={same_grade} -> {'JA' if K1 else 'NEIN'}")
print(f"  K2 (keine einzelne Elter-Darstellung, frei): diskreter Wert {best[1]:.0f} sigma entfernt")
print(f"     (zweite Komponente noetig) UND B/D in verschiedenen Graden ({firstB} vs {firstD}).")
print("\n  FAZIT H204 (voraussichtlich nein):")
print("  - Die Ladungs-kovariante l_k^2-Operatoralgebra ist 2-dimensional (kommutativ), mit genau")
print("    zwei minimalen Idempotenten P_up, P_dn. Eine 'einzelne Darstellung' erzwingt D/B nur")
print("    diskret {0,+1,-1,oo}; der Datenwert 1.0085 liegt %.1f sigma vom naechsten (+1) entfernt" % best[1])
print("    => eine zweite, unabhaengige Komponente ist noetig (b_down != 0).")
print("  - B (Feldgrad 5) und D (Feldgrad 4) leben in VERSCHIEDENEN F4-Tensorgraden; keine einzelne")
print("    F4-irreduzible Darstellung kann beide tragen. D/B ist eine FREIE relative Normierung")
print("    zwischen zwei unabhaengigen Invarianten verschiedenen Grades, kein Clebsch-Gordan-Verhaeltnis.")
print("  - Bestaetigt H202 (Rang 4, Kopplungen frei). Schliesst die Elter-Route.")
print("  - (Teilweise nicht blind: Grad-Trennung aus H201; neu ist die Branching-Lesart und der")
print("    quantitative Abgleich mit den diskreten Verzweigungswerten.)")
