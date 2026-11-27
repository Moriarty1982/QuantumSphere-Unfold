"""k412 (Test H202): Folgt D/B aus der Struktur, oder ist der ~0,9-%-Rest frei?
(A) Rang der Abbildung Kopplungen -> (A,B,C,D).
(B) Minimale Invariant-Basis: fittet eine Teilmenge mit <=3 Kopplungen alle sechs Massen?
Jede Kopplung g (gerade) traegt (zu A, zu B), jede h (ungerade) traegt (zu C, zu D).
Massenmodell: m = [A lk + B lk^2 + s(C lk + D lk^2)]/z,  s=+1 Up, -1 Down.
Aufruf: python k412_test_h202.py > k412_out.txt
"""
import numpy as np
from itertools import combinations
from scipy import stats

# ---- Vakuum, Daten ----
l = np.sort([1 + np.sqrt(2) * np.cos(2/9 + 2*np.pi*k/3) for k in range(3)])
PRS = [(0,1,2),(0,2,1),(1,2,0)]; PERM_B = [2,1,0]
lk = np.array([l[k] for (i,j,k) in PRS])[PERM_B]
z  = np.array([(l[i]+l[j])**2 for (i,j,k) in PRS])[PERM_B]
mu = np.array([7.04e-6, 3.56e-3, 0.967]);   su = np.array([0.15e-6, 0.06e-3, 0.004])
md = np.array([1.54e-5, 3.06e-4, 1.630e-2]); sd = np.array([0.02e-5, 0.04e-4, 0.009e-2])
m6 = np.concatenate([mu, md]); s6 = np.concatenate([su, sd])
sgn6 = np.array([+1,+1,+1, -1,-1,-1])      # Ladungsvorzeichen

# ---- Strukturkoeffizienten je Kopplung: (zu A, zu B, zu C, zu D) ----
# gerade F4-Invarianten (nur A,B); ungerade H186-Formen (nur C,D). Aus H201/k411 (Wolfram exakt).
COUP = {
    "g3":   (-6.0,   0.0,  0.0,   0.0),
    "g4":   (-24.0,  0.0,  0.0,   0.0),
    "g5":   (-60.0, -30.0, 0.0,   0.0),
    "g6":   (-108.0,-234.0,0.0,   0.0),
    "h_c2": (0.0,    0.0, -1/3,   0.0),
    "h_c45":(0.0,    0.0,  0.0,  -1/3),
    "h_c79":(0.0,    0.0, -1.0,   1/6),
    "h_c11":(0.0,    0.0, -1.0,  -1/6),
}
names = list(COUP)
lk_full = np.concatenate([lk, lk]); z_full = np.concatenate([z, z])
def colvec(cn):
    a,b,c,d = COUP[cn]
    even = (a*lk_full + b*lk_full**2)
    odd  = sgn6*(c*lk_full + d*lk_full**2)
    return (even + odd)/z_full

print("="*74)
print("H202 A  Rang der Abbildung (Kopplungen) -> (A,B,C,D)")
print("="*74)
M = np.array([COUP[n] for n in names]).T     # 4 x 8  (Zeilen A,B,C,D)
r = np.linalg.matrix_rank(M, tol=1e-9)
print(f"  Strukturmatrix 4x8 (A,B,C,D) x Kopplungen; Rang = {r}")
# Minimale Basis, die (A,B,C,D) unabhaengig erreicht:
print(f"  gerade Kopplungen betreffen nur (A,B), ungerade nur (C,D) -> Bloecke 2+2.")
rank_AB = np.linalg.matrix_rank(np.array([COUP[n][:2] for n in names if n.startswith('g')]).T)
rank_CD = np.linalg.matrix_rank(np.array([COUP[n][2:] for n in names if n.startswith('h')]).T)
print(f"  Rang (A,B)-Block (gerade) = {rank_AB};  Rang (C,D)-Block (ungerade) = {rank_CD}")
print(f"  -> volle Abbildung Rang {r} = 4 Koeffizienten unabhaengig -> D/B ist FREI (nicht blind).")

# ---- Fit-Funktion fuer eine Kopplungs-Teilmenge ----
def fit(subset):
    X = np.stack([colvec(cn) for cn in subset], 1)
    W = 1/s6; co,*_ = np.linalg.lstsq(X*W[:,None], m6*W, rcond=None)
    pred = X@co; chi2 = float(np.sum(((pred-m6)/s6)**2))
    return chi2, co

print("\n" + "="*74)
print("H202 B  Minimale Invariant-Basis: fittet <=3 Kopplungen alle sechs Massen?")
print("="*74)
best = {}
for ksz in (2,3,4):
    bc, bs = np.inf, None
    for sub in combinations(names, ksz):
        c2,_ = fit(sub)
        if c2 < bc: bc, bs = c2, sub
    best[ksz] = (bc, bs)
    dof = 6-ksz; p = 1-stats.chi2.cdf(bc, dof) if dof>0 else float('nan')
    print(f"  bester {ksz}-Kopplungs-Fit: chi2={bc:10.2f} (dof {dof}, p={p:.2e})  Basis {bs}")

# D/B des besten 4-Kopplungs-Fits
c4b, co4b = best[4][0], None
_, co4b = fit(best[4][1])
Avec = {n:COUP[n] for n in best[4][1]}
A_ = sum(co4b[i]*Avec[best[4][1][i]][0] for i in range(4))
B_ = sum(co4b[i]*Avec[best[4][1][i]][1] for i in range(4))
C_ = sum(co4b[i]*Avec[best[4][1][i]][2] for i in range(4))
D_ = sum(co4b[i]*Avec[best[4][1][i]][3] for i in range(4))
print(f"\n  bester 4-Kopplungs-Fit -> A={A_:.3e} B={B_:.3e} C={C_:.3e} D={D_:.3e}  D/B={D_/B_:+.4f}")

print("\n" + "="*74)
print("H202 Entscheidung (Vorab-Kriterien)")
print("="*74)
c2_3, sub3 = best[3]; c2_4, sub4 = best[4]
p3 = 1-stats.chi2.cdf(c2_3, 3)
k1 = p3 > 0.05
print(f"  bester <=3-Kopplungs-Fit: chi2={c2_3:.1f} (p={p3:.1e}) -> " +
      ("K1: D/B vorhergesagt" if k1 else "ausgeschlossen"))
if not k1:
    print(f"  -> K2: D/B FREI. Jede <=3-Basis verworfen (bestes chi2={c2_3:.0f} >> {c2_4:.1f} bei 4).")
    print("     Minimal noetig: 2 gerade (A,B) + 2 ungerade (C,D) = 4 Kopplungen = 4 Koeffizienten.")
    print("     Der ~0,9-%-Rest D/B-1 ist ein EINGABEWERT (Quark-Yukawas frei in diesem Rahmen).")
print("\n  FAZIT H202: Weder Grad (H201), Symmetrie (H197), Holomorphie (H200) noch minimale")
print("  Invariant-Zahl (H202) legen D/B fest. Alle Bausteine identifiziert, Kopplungen frei.")
print("  Naechster Schritt braucht eine NEUE Eingabe (Prinzip, das die Kopplungen bindet) —")
print("  dem Autor als Weggabelung vorlegen.")
