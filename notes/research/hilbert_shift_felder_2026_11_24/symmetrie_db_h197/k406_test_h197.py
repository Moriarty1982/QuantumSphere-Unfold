"""k406 (Test H197): Erzwingt eine Symmetrie D = B?
Zerlegt die Quelle des ladungsgeraden l_k^2 (B) und des ladungsungeraden l_k^2 (D):
  A  Grad-Leiter der ladungsgeraden F4-Kruemmung (l_k^2 erst bei Grad 5)
  B  ladungsungerade Kruemmungen aus H186 auf dem Vakuum (l_k^2 schon bei Grad 4)
  C  Rang der (gerade, ungerade)-l_k^2-Quellen -> ist D/B frei?
  D  J-Kovarianz der Ladungsformen Q0-1/2, Q0-1/3, P_up (Eigenwerte 1/3, 2/3 und ihr Tausch)
  E  Daten gegen feste D/B in {0, 1/3, -1} vs. freier Fit; chi2(D/B); 2-sigma-Fenster; Kontrolle
Aufruf: python k406_test_h197.py > k406_out.txt
"""
import numpy as np, sympy as sp
from scipy.linalg import null_space
rng = np.random.default_rng(405)

# ---------- Daten (M_Z-Yukawa, k376) ----------
mu = np.array([7.04e-6, 3.56e-3, 0.967]);   su = np.array([0.15e-6, 0.06e-3, 0.004])
md = np.array([1.54e-5, 3.06e-4, 1.630e-2]); sd = np.array([0.02e-5, 0.04e-4, 0.009e-2])
l = np.sort([1 + np.sqrt(2) * np.cos(2 / 9 + 2 * np.pi * k / 3) for k in range(3)])
PRS = [(0, 1, 2), (0, 2, 1), (1, 2, 0)]; PERM_B = [2, 1, 0]      # Zuordnung B (H194)
lk = np.array([l[k] for (i, j, k) in PRS])[PERM_B]
z  = np.array([(l[i] + l[j]) ** 2 for (i, j, k) in PRS])[PERM_B]

lksym = sp.symbols('l_k'); e1, e2 = sp.symbols('e1 e2')
sub_vac = {e1: 3 - lksym, e2: sp.Rational(3, 2) - lksym * (3 - lksym)}   # Tr=3, e2=3/2 auf dem Vakuum
def coeff2(expr): return sp.Poly(sp.expand(expr), lksym).coeff_monomial(lksym**2)

print("=" * 78)
print("H197a  Quelle von B (ladungsgerade) und D (ladungsungerade) getrennt")
print("=" * 78)

# --- A: ladungsgerade F4-Kruemmung, Grad-Leiter (wie k403c) ---
def hcomp(m):
    H = [sp.Integer(1), e1]
    for k in range(2, m + 1): H.append(sp.expand(e1 * H[k - 1] - e2 * H[k - 2]))
    return H[m]
print("\n(A) ladungsgerade F4-Kruemmung v=x^n  ->  l_k^2-Koeffizient auf dem Vakuum:")
first_even = None
for n in range(2, 7):
    cur = sp.expand((2 * n * hcomp(n - 2)).subs(sub_vac)); c2 = coeff2(cur)
    if first_even is None and c2 != 0: first_even = n
    print(f"    Grad n={n}: l_k^2-Koeff = {c2}")
print(f"    -> ladungsgerades l_k^2 erscheint zuerst bei Grad {first_even} (F4-invariant, GERADE).")

# --- B: ladungsungerade Kruemmungen aus H186, in elementarsymmetrischen s=l_i+l_j, pr=l_i l_j
#        reduziert (l_i^2+l_j^2 = s^2-2 pr), dann Vakuum s=3-l_k, pr=3/2-3 l_k+l_k^2 ---
s, pr = sp.symbols('s pr')      # s = l_i+l_j, pr = l_i l_j ; q2 := l_i^2+l_j^2 = s^2-2 pr
odd_forms = {                   # (Up-Down)/2 Kruemmung je Kandidat, H186/k389 (Wolfram exakt)
    "c1":    sp.Rational(2, 3),
    "c2":    sp.Rational(1, 3) * s,
    "c4/c5": sp.Rational(1, 3) * (s**2 - 2*pr),
    "c7/c9": sp.Rational(1, 6) * s**2,
    "c11":   sp.Rational(1, 2) * (s**2 - 2*pr) + sp.Rational(1, 3) * pr,
}
sub_sym = {s: 3 - lksym, pr: sp.Rational(3, 2) - 3*lksym + lksym**2}     # Vakuum-Identitaeten
print("\n(B) ladungsungerade Kruemmung (H186, Grad 4) auf dem Vakuum  ->  l_k^2-Koeffizient:")
odd_grad = 4; first_odd_l2 = None; odd_l2 = {}
for nm, f in odd_forms.items():
    red = sp.expand(sp.expand(f).subs(sub_sym))
    c2 = red.coeff(lksym, 2) if red.has(lksym) else sp.Integer(0)
    odd_l2[nm] = c2
    if first_odd_l2 is None and c2 != 0: first_odd_l2 = nm
    print(f"    {nm:7s}: {red}   (l_k^2-Koeff = {c2})")
print(f"    -> ladungsungerades l_k^2 existiert schon bei Grad {odd_grad} (erster: {first_odd_l2}).")

print("\n(Befund A/B) B braucht Grad 5 (gerade), D existiert bei Grad 4 (ungerade):")
print(f"    verschiedener Grad UND verschiedene Invarianz -> getrennte Kopplungen.")

# --- C: Rang der (gerade, ungerade)-l_k^2-Quellen ---
print("\n" + "=" * 78)
print("H197c (Rang)  Sind B und D unabhaengig?  Abbildung (g_gerade, g_ungerade) -> (B, D)")
print("=" * 78)
# gerade Quelle: Grad-5-F4 traegt l_k^2 (Koeff oben) und nichts ungerades.
even_src = np.array([float(coeff2((10*hcomp(3)).subs(sub_vac))), 0.0])   # (zu B, zu D)
# ungerade Quelle: z.B. c7/c9 traegt l_k^2 nur in D (ungerade), nichts in B.
odd_src  = np.array([0.0, float(odd_l2["c7/c9"])])                        # (zu B, zu D)
M = np.vstack([even_src, odd_src]).T
r = np.linalg.matrix_rank(M, tol=1e-9)
print(f"    gerade Grad-5-Quelle -> (B,D) = {even_src}")
print(f"    ungerade Grad-4-Quelle (c7/c9) -> (B,D) = {odd_src}")
print(f"    Rang der Abbildung auf (B,D) = {r}  -> " +
      ("D/B ist FREI (keine Bindung)." if r == 2 else "D/B gebunden."))

# --- D: J-Kovarianz der Ladungsformen (Eigenwerte 1/3, 2/3 und ihr Tausch) ---
print("\n" + "=" * 78)
print("H197d  J-Kovarianz der Ladungsformen (J: Q0 -> 1 - Q0, tauscht 1/3 <-> 2/3)")
print("=" * 78)
# Q0 auf dem Farbblock explizit (wie k389), Eigenwerte pruefen
def conj(x):
    y = -x.copy(); y[0] = x[0]; return y
def mul(x, y):
    n = len(x)
    if n == 1: return x * y
    h = n // 2; a, b, c, d = x[:h], x[h:], y[:h], y[h:]
    return np.concatenate([mul(a, c) - mul(conj(d), b), mul(d, a) + mul(b, conj(c))])
e = np.eye(8); C = np.array([[mul(e[i], e[j]) for j in range(8)] for i in range(8)])
LU = np.einsum('i,ijk->kj', e[7], C)[1:7, 1:7]
I2 = np.eye(2); J2 = np.array([[0, -1.0], [1, 0]])
Ii = np.kron(J2, np.eye(18)); LUc = np.kron(I2, np.kron(np.eye(3), LU))
Qc = 0.5 * np.eye(36) + Ii @ LUc / 6
w = np.linalg.eigvalsh((Qc + Qc.T) / 2)
print(f"    Eigenwerte von Q0 auf dem Farbblock: {sorted(set(np.round(w, 6)))}  (erwartet 1/3, 2/3)")
# J bildet Q0-Eigenwert q auf 1-q ab. Werte der drei Formen auf den Eigenwerten:
for nm, f in [("Q0 - 1/2 (H182-Form h)", lambda q: q - sp.Rational(1,2)),
              ("Q0 - 1/3", lambda q: q - sp.Rational(1,3)),
              ("P_up = 3(Q0 - 1/3)", lambda q: 3*(q - sp.Rational(1,3)))]:
    vd, vu = f(sp.Rational(1,3)), f(sp.Rational(2,3))         # Down (1/3), Up (2/3)
    vd_J, vu_J = f(1 - sp.Rational(1,3)), f(1 - sp.Rational(2,3))  # nach J: q->1-q
    # Eigenform unter J?  (vu_J, vd_J) == lam*(vu, vd) ?
    lam = None
    if vu != 0:
        cand = vd_J / vd if vd != 0 else (vu_J / vu)
        if sp.simplify(vu_J - cand*vu) == 0 and sp.simplify(vd_J - cand*vd) == 0: lam = cand
    tag = (f"Eigenform, J-Eigenwert {lam}" if lam is not None else "KEINE Eigenform (J mischt)")
    extra = ""
    if "P_up" in nm: extra = f"; J bildet (Up,Down)=({vu},{vd}) auf ({vu_J},{vd_J}) ab = P_down"
    print(f"    {nm:24s}: Down={vd}, Up={vu} -> {tag}{extra}")
print("    -> nur Q0-1/2 ist J-ausgezeichnet (ladungsungerade). D=B entspricht P_up, NICHT J-kovariant.")

# --- E: Daten gegen feste D/B ---
print("\n" + "=" * 78)
print("H197b/c  Daten (6 Massen) gegen feste D/B vs. freier Fit")
print("=" * 78)
m_all = np.concatenate([mu, md]); s_all = np.concatenate([su, sd])
s_up = np.array([+1, +1, +1]); s_dn = np.array([-1, -1, -1])
def design(DB):
    """Spalten fuer (A, B, C) bei festem Verhaeltnis D = DB*B. s*(C l + DB*B l^2)."""
    # Parameter: A, B, C ; D = DB*B
    def rows(sgn):
        A_col = lk / z
        B_col = (lk**2 + sgn*DB*lk**2) / z      # B*(l^2 + s*DB*l^2)
        C_col = sgn*lk / z                       # C * s*l
        return A_col, B_col, C_col
    Au, Bu, Cu = rows(+1); Ad, Bd, Cd = rows(-1)
    X = np.vstack([np.stack([Au, Bu, Cu], 1), np.stack([Ad, Bd, Cd], 1)])
    return X
def chi2_fixedDB(DB, m=m_all, s=s_all):
    X = design(DB); W = 1 / s
    co, *_ = np.linalg.lstsq(X * W[:, None], m * W, rcond=None)
    pred = X @ co; return float(np.sum(((pred - m) / s) ** 2)), co
def chi2_free(m=m_all, s=s_all):
    # 4 Parameter A,B,C,D frei
    Xf = np.vstack([
        np.stack([lk/z, lk**2/z,  lk/z,  lk**2/z], 1),      # Up: A,B,C,D (s=+1)
        np.stack([lk/z, lk**2/z, -lk/z, -lk**2/z], 1)])     # Down: s=-1
    W = 1/s; co,*_ = np.linalg.lstsq(Xf*W[:,None], m*W, rcond=None)
    pred = Xf@co; return float(np.sum(((pred-m)/s)**2)), co
c2f, cof = chi2_free()
A_,B_,C_,D_ = cof
print(f"    freier 4-Param-Fit: chi2={c2f:.2f} (2 dof); A={A_:.3e} B={B_:.3e} C={C_:.3e} D={D_:.3e}; D/B={D_/B_:+.3f}")
print("\n    feste D/B (symmetrieausgezeichnet), je 3 Param (A,B,C):")
for nm, DB in [("ladungsblind  D/B=0", 0.0), ("lineare Ladung D/B=1/3", 1/3),
               ("reine J-Form  D/B=-1", -1.0), ("P_up/Fit     D/B=+1", 1.0)]:
    c2, co = chi2_fixedDB(DB); dof = 6 - 3
    print(f"      {nm:24s}: chi2={c2:10.2f}  ({dof} dof)  " +
          ("<-- traegt" if c2 < 12 else "ausgeschlossen"))

# chi2(D/B)-Kurve und 2-sigma-Fenster (um das Minimum, Delta chi2 < 4 fuer 1 Param)
# feines Gitter: die leichten Down-Massen pinnen D/B sehr scharf nahe 1
grid = np.linspace(0.95, 1.06, 11001)
c2g = np.array([chi2_fixedDB(DB)[0] for DB in grid])
imin = int(np.argmin(c2g)); DBmin = grid[imin]; c2min = c2g[imin]
win = grid[c2g <= c2min + 4]
print(f"\n    chi2(D/B)-Minimum bei D/B = {DBmin:+.4f} (chi2={c2min:.2f}); 2-sigma-Fenster D/B in "
      f"[{win.min():+.4f}, {win.max():+.4f}]  (Breite {win.max()-win.min():.4f})")
for DB in [0.0, 1/3, -1.0]:
    print(f"      D/B={DB:+.3f}: chi2={chi2_fixedDB(DB)[0]:.1f}  (Delta chi2 ggue Minimum = {chi2_fixedDB(DB)[0]-c2min:.1f})")

# --- Kontrolle: erfundene Massenpaare, Trefferquote fester-D/B-Fit ---
print("\n    Kontrolle: 2000 erfundene Massenpaare, wie oft trifft ein festes D/B (0, 1/3, -1) mit chi2<12?")
NMC = 2000; hits = {0.0: 0, 1/3: 0, -1.0: 0}; hit_free = 0
for _ in range(NMC):
    fu = np.exp(rng.uniform(np.log(1e-6), np.log(1.0), 3)); fu.sort()
    fd = np.exp(rng.uniform(np.log(1e-5), np.log(2e-2), 3)); fd.sort()
    mm = np.concatenate([fu, fd]); ss = 0.02 * mm
    if chi2_free(mm, ss)[0] < 12: hit_free += 1
    for DB in hits:
        if chi2_fixedDB(DB, mm, ss)[0] < 12: hits[DB] += 1
print(f"      freier 4-Param: {100*hit_free/NMC:.1f}%   feste D/B: " +
      "  ".join(f"D/B={DB:+.2f}: {100*h/NMC:.1f}%" for DB, h in hits.items()))

print("\n" + "=" * 78)
print("Urteil H197:")
sym_excluded = all(chi2_fixedDB(DB)[0] > 12 for DB in [0.0, 1/3, -1.0])
db_near1 = abs(DBmin - 1.0) < abs(DBmin - 1/3) and abs(DBmin-1.0) < 0.3
print(f"    symmetrieausgezeichnete D/B (0, 1/3, -1) alle ausgeschlossen: {sym_excluded}")
print(f"    Daten verlangen D/B ~ {DBmin:+.2f} (= P_up, nicht J-kovariant): {db_near1}")
if sym_excluded and db_near1:
    print("    -> NEIN, keine Symmetrie erzwingt D=B. 'Down linear' ist eine empirische")
    print("       Auswahlregel (Up-Typ-Projektor P_up), die der H182/F4-Rahmen nicht erzeugt.")
else:
    print("    -> siehe Zahlen oben.")
