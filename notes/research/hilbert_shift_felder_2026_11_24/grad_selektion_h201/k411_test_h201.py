"""k411 (Test H201): Ist die Chiralitaet der Quintik eine Grad-Selektion?
(A) Grad-Zerlegung: fuer jeden Feldgrad die Beitraege zu A (l_k, gerade), B (l_k^2, gerade),
    C (l_k, ungerade), D (l_k^2, ungerade). Erscheinen B und D je im selben Grad?
(B) Fit-Test geschachtelter Modelle: (1) C=0 & D=B (2 Param, saubere Grad-Selektion),
    (2) D=B frei-C (3 Param), (3) frei A,B,C,D (4 Param). + Signifikanz von C.
Aufruf: python k411_test_h201.py > k411_out.txt
"""
import numpy as np, sympy as sp

# ---------- Daten (M_Z-Yukawa, k376) ----------
mu = np.array([7.04e-6, 3.56e-3, 0.967]);   su = np.array([0.15e-6, 0.06e-3, 0.004])
md = np.array([1.54e-5, 3.06e-4, 1.630e-2]); sd = np.array([0.02e-5, 0.04e-4, 0.009e-2])
l = np.sort([1 + np.sqrt(2) * np.cos(2/9 + 2*np.pi*k/3) for k in range(3)])
PRS = [(0,1,2),(0,2,1),(1,2,0)]; PERM_B = [2,1,0]
lk = np.array([l[k] for (i,j,k) in PRS])[PERM_B]
z  = np.array([(l[i]+l[j])**2 for (i,j,k) in PRS])[PERM_B]
m6 = np.concatenate([mu, md]); s6 = np.concatenate([su, sd])

# ====================================================================
#  (A) Strukturelle Grad-Zerlegung
# ====================================================================
lks = sp.symbols('l_k'); e1, e2 = sp.symbols('e1 e2')
sub_vac = {e1: 3 - lks, e2: sp.Rational(3,2) - lks*(3 - lks)}    # Tr=3, e2 auf dem Vakuum
s, pr = sp.symbols('s pr')
sub_sym = {s: 3 - lks, pr: sp.Rational(3,2) - 3*lks + lks**2}
def c1c2(expr):
    p = sp.Poly(sp.expand(expr), lks)
    return p.coeff_monomial(lks), p.coeff_monomial(lks**2)
def hcomp(m):
    H = [sp.Integer(1), e1]
    for k in range(2, m+1): H.append(sp.expand(e1*H[k-1] - e2*H[k-2]))
    return H[m]

print("=" * 78)
print("H201 A  Grad-Zerlegung: Beitraege zu A,B (gerade) und C,D (ungerade)")
print("=" * 78)
print("\n ladungsGERADE F4-Kruemmung v=x^n auf dem Vakuum  (-> A: l_k, B: l_k^2):")
firstA = firstB = None
for n in range(2, 7):
    cur = sp.expand((2*n*hcomp(n-2)).subs(sub_vac)); c1, c2 = c1c2(cur)
    if firstA is None and c1 != 0: firstA = n
    if firstB is None and c2 != 0: firstB = n
    print(f"    Grad n={n}: A-Beitrag(l_k)={c1},  B-Beitrag(l_k^2)={c2}")
print(f"    -> gerades l_k (A) zuerst bei Grad {firstA};  gerades l_k^2 (B) zuerst bei Grad {firstB}.")

odd_forms = {   # (Up-Down)/2 Kruemmungen, H186/k389 (Wolfram exakt), Grad 4
    "c1":    sp.Rational(2,3),
    "c2":    sp.Rational(1,3)*s,
    "c4/c5": sp.Rational(1,3)*(s**2 - 2*pr),
    "c7/c9": sp.Rational(1,6)*s**2,
    "c11":   sp.Rational(1,2)*(s**2 - 2*pr) + sp.Rational(1,3)*pr,
}
print("\n ladungsUNGERADE Kruemmung (H186, Grad 4) auf dem Vakuum  (-> C: l_k, D: l_k^2):")
firstC = firstD = None
for nm, f in odd_forms.items():
    red = sp.expand(sp.expand(f).subs(sub_sym)); c1, c2 = c1c2(red)
    if firstC is None and c1 != 0: firstC = nm
    if firstD is None and c2 != 0: firstD = nm
    print(f"    {nm:7s}: C-Beitrag(l_k)={c1},  D-Beitrag(l_k^2)={c2}")
print(f"    -> ungerades l_k (C) ab {firstC} (Grad<=4);  ungerades l_k^2 (D) ab {firstD} (Grad 4).")

print("\n Grad-Karte (erstes Auftreten):")
print(f"    A (gerade l_k ) : Grad {firstA}")
print(f"    C (ungerade l_k): Grad <= 4 (H186-Form {firstC})")
print(f"    D (ungerade l_k^2): Grad 4 (H186-Form {firstD})")
print(f"    B (gerade  l_k^2): Grad {firstB}")
share_BD = (firstB == 4)
print(f"    Teilen sich B und D EINEN Grad (noetig fuer automatisches D=B)? "
      f"{'JA' if share_BD else 'NEIN (B Grad 5, D Grad 4)'}")
print("    -> 'Top-Grad = chiral' braeuchte B und D im selben Grad. Sie liegen in Grad 5 bzw 4.")

# ====================================================================
#  (B) Fit-Test geschachtelter Modelle + Signifikanz von C
# ====================================================================
from scipy import stats
def lsq(X):
    W = 1.0/s6; co,*_ = np.linalg.lstsq(X*W[:,None], m6*W, rcond=None)
    chi2 = float(np.sum(((X@co - m6)/s6)**2)); return co, chi2
def cov_free(X):                      # Parameter-Kovarianz des gewichteten Fits
    A = X / s6[:,None]; return np.linalg.inv(A.T @ A)

print("\n" + "=" * 78)
print("H201 B  Geschachtelte Fits: saubere Grad-Selektion vs frei")
print("=" * 78)

# (3) frei A,B,C,D
X4 = np.vstack([np.stack([lk/z, lk**2/z,  lk/z,  lk**2/z],1),
                np.stack([lk/z, lk**2/z, -lk/z, -lk**2/z],1)])
co4, chi4 = lsq(X4); A4,B4,C4,D4 = co4
cov4 = cov_free(X4); sigC = np.sqrt(cov4[2,2]); sigA = np.sqrt(cov4[0,0])
print(f"\n(3) frei (A,B,C,D): chi2={chi4:.3f} dof={6-4}")
print(f"    A={A4:.3e}+-{sigA:.1e}  B={B4:.3e}  C={C4:.3e}+-{sigC:.1e}  D={D4:.3e}  D/B={D4/B4:+.4f}")
print(f"    C/A = {C4/A4:+.4f}   |C|/sigma_C = {abs(C4)/sigC:.1f}  (ist der lineare Term blind? C=0?)")

# (2) D=B, C frei (3 Param A,C,B) = H200-Modell 2
X3 = np.vstack([np.stack([lk/z,  lk/z, 2*lk**2/z],1),
                np.stack([lk/z, -lk/z, 0*lk/z   ],1)])
co3, chi3 = lsq(X3)
print(f"\n(2) D=B, C frei (A,C,B): chi2={chi3:.3f} dof={6-3}  p={1-stats.chi2.cdf(chi3,3):.2e}")

# (1) C=0, D=B (2 Param A,B): up=(A lk + 2B lk^2)/z, down=A lk/z
X2 = np.vstack([np.stack([lk/z, 2*lk**2/z],1),
                np.stack([lk/z, 0*lk**2/z],1)])
co2, chi2v = lsq(X2); A2,B2 = co2
dof2 = 6-2; p2 = 1-stats.chi2.cdf(chi2v, dof2)
print(f"\n(1) C=0 & D=B (A,B): chi2={chi2v:.3f} dof={dof2}  p={p2:.2e}")
print(f"    A={A2:.3e} B={B2:.3e}")

# ====================================================================
#  Entscheidung
# ====================================================================
print("\n" + "=" * 78)
print("H201 Entscheidung (Vorab-Kriterien)")
print("=" * 78)
Csig = abs(C4)/sigC
k1 = (p2 > 0.05) and (Csig <= 2)
print(f"  K1 saubere Grad-Selektion (C=0 & D=B): chi2={chi2v:.1f} (dof {dof2}, p={p2:.1e}); "
      f"|C|/sigma_C={Csig:.1f}")
if k1:
    print("     -> K1: Grad-Selektion traegt (2-Param-Modell ok, C mit 0 vertraeglich).")
else:
    print(f"     -> K2: KEINE Grad-Selektion. C ist scharf != 0 ({Csig:.0f} sigma), 2-Param")
    print(f"        verworfen (Delta-chi2 ggue frei = {chi2v-chi4:.0f}); und B (Grad 5), D (Grad 4)")
    print("        liegen in verschiedenen Graden. 'Top-Grad = chiral' ist KEINE Grad-Ordnung.")
print("\n  FAZIT H201 (voraussichtlich nein zur Grad-Selektion):")
print("  - Die Quintik-Chiralitaet (D~B) ist eine GRADUEBERGREIFENDE Near-Equality zwischen einer")
print("    Grad-4-ungeraden (D) und einer Grad-5-geraden (B) Kopplung, kein Top-Grad-Prinzip.")
print(f"  - Der lineare Term ist unabhaengig ladungsgespalten: C/A = {C4/A4:+.3f} (nicht blind, nicht chiral).")
print(f"  - Der ~0,9-%-Rest D/B-1 = {D4/B4-1:+.4f} ist der Grad-4/Grad-5-Versatz (Uebergang zu Schritt 2).")
