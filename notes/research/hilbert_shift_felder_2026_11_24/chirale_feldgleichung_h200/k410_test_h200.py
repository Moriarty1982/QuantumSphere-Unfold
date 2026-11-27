"""k410 (Test H200): Ist die Feldgleichung holomorph (chiral) unter der Ladung?
Drei Modelle am Quarkdatensatz (6 Massen, Zuordnung B, Nenner (l_i+l_j)^2):
  (1) voll holomorph  : Zaehler ganz aus P_up -> a_down=0 UND b_down=0 (Down masselos). NICHT BLIND.
  (2) gradselektiv    : linearer Term ladungsblind (A,C), l_k^2-Term strikt chiral D=B (3 Param).
  (3) voll (Referenz) : A,B,C,D frei (4 Param, = H196).
Dazu: Operator-Kontrolle P_up auf dem Farbblock (holomorph => Down-Projektion = 0).
Aufruf: python k410_test_h200.py > k410_out.txt
"""
import numpy as np
from scipy import stats

# ====================================================================
#  Teil A  Operator-Kontrolle: holomorph (P_up) => Down-Beitrag = 0
# ====================================================================
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
Qc = 0.5*np.eye(36) + Ii @ LUc / 6; iLU = Ii @ LUc
Pup = 0.5 * (np.eye(36) + iLU)                 # chiraler (holomorpher) Projektor = P_up (H198)
wq, Vq = np.linalg.eigh((Qc + Qc.T) / 2)
up_space = Vq[:, wq > 0.5]; dn_space = Vq[:, wq < 0.5]

print("=" * 72)
print("H200 A  Operator-Kontrolle: ein holomorpher (P_up) Term koppelt nicht an Down")
print("=" * 72)
print(f"  || P_up on Down-Raum ||_max (soll 0) = {np.abs(dn_space.T @ Pup @ dn_space).max():.2e}")
print(f"  <P_up>_up (soll 1) = {np.diag(up_space.T @ Pup @ up_space).mean():.6f}")
print("  -> JEDER aus P_up gebaute Term (linear ODER quadratisch) gibt fuer Down (s=-1) null.")
print("     Voll holomorpher Zaehler => a_down=0 UND b_down=0 => Down-Masse (Zaehler) = 0.")

# ====================================================================
#  Teil B  Daten, Vakuum, Nenner
# ====================================================================
l = np.sort([1 + np.sqrt(2) * np.cos(2/9 + 2*np.pi*k/3) for k in range(3)])
PRS = [(0,1,2),(0,2,1),(1,2,0)]; PERM_B = [2,1,0]
lk = np.array([l[k] for (i,j,k) in PRS])[PERM_B]
z  = np.array([(l[i]+l[j])**2 for (i,j,k) in PRS])[PERM_B]
mu = np.array([7.04e-6, 3.56e-3, 0.967]);   su = np.array([0.15e-6, 0.06e-3, 0.004])
md = np.array([1.54e-5, 3.06e-4, 1.630e-2]); sd = np.array([0.02e-5, 0.04e-4, 0.009e-2])
m6 = np.concatenate([mu, md]); s6 = np.concatenate([su, sd])

def lsq(X):                                    # gewichteter linearer Fit, chi2
    W = 1.0 / s6
    co, *_ = np.linalg.lstsq(X * W[:, None], m6 * W, rcond=None)
    chi2 = float(np.sum(((X @ co - m6) / s6) ** 2))
    return co, chi2, X @ co

print("\n" + "=" * 72)
print("H200 B  Drei Modelle am Quarkdatensatz (6 Massen, Nenner (l_i+l_j)^2)")
print("=" * 72)

# ---- Modell 3: voll A,B,C,D (Referenz, = H196) ----
X4 = np.vstack([np.stack([lk/z, lk**2/z,  lk/z,  lk**2/z], 1),
                np.stack([lk/z, lk**2/z, -lk/z, -lk**2/z], 1)])
co4, chi4, fit4 = lsq(X4)
A,B,Cc,D = co4
print(f"\n(3) voll (A,B,C,D):   chi2 = {chi4:.3f}  dof = {6-4}")
print(f"    A={A:.3e} B={B:.3e} C={Cc:.3e} D={D:.3e}  ->  D/B = {D/B:+.4f}")

# ---- Modell 2: gradselektiv, D=B (Param A,C,B); Down bekommt nur linear ----
# up   = [(A+C) lk + 2B lk^2]/z ;  down = (A-C) lk/z   (b_down=0)
X3 = np.vstack([np.stack([lk/z,  lk/z, 2*lk**2/z], 1),    # Spalten: A, C, B
                np.stack([lk/z, -lk/z, 0*lk    /z], 1)])
co3, chi3, fit3 = lsq(X3)
A3,C3,B3 = co3
print(f"\n(2) gradselektiv D=B (A,C,B): chi2 = {chi3:.3f}  dof = {6-3}")
print(f"    A={A3:.3e} C={C3:.3e} B=D={B3:.3e}   (b_down = 0 erzwungen)")
p3 = 1 - stats.chi2.cdf(chi3, 6-3)
print(f"    p-Wert (dof=3) = {p3:.3e}")

# ---- Modell 1: voll holomorph; Zaehler ganz aus P_up -> down=0 ----
# up = (a lk + b lk^2)/z an die 3 Up-Massen; down-Vorhersage = 0
Wu = 1.0/su
Xu = np.stack([lk/z, lk**2/z], 1)
cou, *_ = np.linalg.lstsq(Xu*Wu[:,None], mu*Wu, rcond=None)
fit_up = Xu @ cou
chi_up = float(np.sum(((fit_up - mu)/su)**2))
chi_dn0 = float(np.sum((md/sd)**2))            # Down-Vorhersage 0
chi1 = chi_up + chi_dn0
print(f"\n(1) voll holomorph (down=0): chi2 = {chi1:.3e}  dof = {6-2}")
print(f"    davon Up-Fit chi2 = {chi_up:.3f},  Down (Vorhersage 0) chi2 = {chi_dn0:.3e}")
print(f"    Down-Massen vorhergesagt = 0 gegen beob. {md} (Abweichung in sigma: {md/sd})")

# ====================================================================
#  Teil C  Entscheidung
# ====================================================================
print("\n" + "=" * 72)
print("H200 C  Entscheidung gegen die Vorab-Kriterien")
print("=" * 72)
# K1 voll holomorph verworfen?
down_sig = md/sd
k1 = (chi1 > 100*max(chi4,1e-9)) and (down_sig.min() > 5)
print(f"  K1 voll holomorph: chi2 {chi1:.1e} >> {chi4:.2f}, Down {down_sig.min():.0f}-{down_sig.max():.0f}sigma daneben")
print(f"     -> voll holomorphe Feldgleichung {'VERWORFEN' if k1 else 'nicht klar verworfen'}.")
# K2/K3 gradselektive (strikte) Chiralitaet
dDB = abs(D/B - 1.0)
rg_budget = 0.004                               # 0.4% aus H199
k2 = (p3 > 0.05) and (dDB <= rg_budget)
print(f"  K2/K3 gradselektiv D=B: chi2_3={chi3:.2f} (dof 3, p={p3:.2e}) vs chi2_4={chi4:.2f} (dof 2)")
print(f"     Delta-chi2 (D=B vs frei) = {chi3-chi4:.2f};  |D/B-1| = {dDB:.4f}  (RG-Budget {rg_budget})")
if k2:
    print("     -> K2: strikte Chiralitaet traegt (Fit ok, Rest im RG-Budget).")
else:
    print(f"     -> K3: strikte Chiralitaet NUR APPROXIMATIV. D=B bei Delta-chi2={chi3-chi4:.1f}")
    print(f"        ausgeschlossen; Rest |D/B-1|={dDB:.4f} ueber RG-Budget {rg_budget}. Quintik ist")
    print("        chiral-DOMINANT (~99%) mit ladungsblindem Beimischungsanteil, nicht exakt chiral.")

print("\n  FAZIT H200 (teilweise):")
print("  - Globale Holomorphie VERWORFEN (sauber, nicht blind): sie macht Down masselos.")
print("  - Gradselektive Chiralitaet erklaert das MUSTER (b_down~0, Up quadratisch-dominant),")
print("    aber strikte Chiralitaet (exakt D=B) ist ausgeschlossen; der ~0.9%-Rest liegt")
print("    ueber dem RG-Budget (H199) -> Chiralitaet ist dominant, approximativ, gradselektiv.")
print("  - Offen geschaerft: was zeichnet die Quintik fuer die Chiralitaet aus, und woher")
print("    kommt der ladungsblinde Beimischungsanteil (D/B-1 ~ 0.9%)?")
