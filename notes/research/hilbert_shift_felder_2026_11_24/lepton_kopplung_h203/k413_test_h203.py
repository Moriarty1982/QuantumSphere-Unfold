"""k413 (Test H203): Binden die Lepton-Massen / delta die Quark-Kopplungen?
'Ein Vakuum, Sektoren schwingen' (H184): Lepton-(farblos) und Quark-(Farb)-Massen sind
Kruemmungen desselben Potentials um W0. Frage: Gibt es Kopplungen, die die Quark-(Farb)-
Frequenzen aendern, aber die Lepton-(farblosen) Massen nicht? Dann sieht der Lepton-Sektor
die Quark-Kopplungen nicht.
Maschinerie uebernommen aus k387 (H184).
Aufruf: python k413_test_h203.py > k413_out.txt
"""
import itertools, numpy as np
from scipy.linalg import null_space
rng = np.random.default_rng(413)
def conj(x):
    y = -x.copy(); y[0] = x[0]; return y
def mul(x, y):
    n = len(x)
    if n == 1: return x * y
    h = n // 2; a, b, c, d = x[:h], x[h:], y[:h], y[h:]
    return np.concatenate([mul(a, c) - mul(conj(d), b), mul(d, a) + mul(b, conj(c))])
e = np.eye(8); C = np.array([[mul(e[i], e[j]) for j in range(8)] for i in range(8)])
cj = np.diag([1.0] + [-1.0]*7)
PAIRS = [(0,1),(1,2),(2,0)]
def toW(v):
    W = np.zeros((3,3,8))
    for i in range(3): W[i,i,0] = v[i]
    for s,(i,j) in enumerate(PAIRS):
        x = v[3+8*s:11+8*s]; W[i,j] = x; W[j,i] = cj @ x
    return W
mm = lambda X,Y: np.einsum('ija,jkb,abc->ikc', X, Y, C)
jo = lambda X,Y: 0.5*(mm(X,Y)+mm(Y,X))
tr = lambda X: X[0,0,0]+X[1,1,0]+X[2,2,0]
def projU(W):
    Z = np.zeros_like(W); Z[:,:,0] = W[:,:,0]; Z[:,:,7] = W[:,:,7]; return Z
def W0(a,r,delta):
    v = np.zeros(27); v[:3] = a
    for s in range(3): v[3+8*s] = r*np.cos(delta); v[3+8*s+7] = r*np.sin(delta)
    return v
a0=1.0; r0=a0/np.sqrt(2); d0=2.0/9.0; w0 = W0(a0,r0,d0)
ev0 = np.sort([a0 + 2*r0*np.cos(d0 + 2*np.pi*k/3) for k in range(3)])
colidx = [3+8*s+c for s in range(3) for c in range(1,7)]
sngidx = [i for i in range(27) if i not in colidx]

# --- 13 Spur-Invarianten (wie k387) ---
def invs(v):
    W = toW(v); Wu = projU(W); W2 = jo(W,W); U2 = jo(Wu,Wu); t = tr(W)
    return {"Tr W^2": tr(W2), "Tr Wu^2": tr(U2), "Tr W^3": tr(jo(W2,W)), "Tr Wu^3": tr(jo(U2,Wu)),
            "Tr W^4": tr(jo(W2,W2)), "Tr Wu^4": tr(jo(U2,U2)), "Tr W^2 o Wu^2": tr(jo(W2,U2)),
            "(Tr W^2)^2": tr(W2)**2, "Tr W^2 Tr Wu^2": tr(W2)*tr(U2), "(Tr Wu^2)^2": tr(U2)**2,
            "Tr W Tr W^3": t*tr(jo(W2,W)), "(Tr W)^2 Tr W^2": t*t*tr(W2), "(Tr W)^2 Tr Wu^2": t*t*tr(U2)}
names = list(invs(w0).keys())
allf = lambda v: np.array(list(invs(v).values()))
def hess_all(wv, ix):
    nx = len(ix); E = np.eye(27)[ix]; H = np.zeros((len(names), nx, nx))
    def d2(i,j,hh):
        return (allf(wv+hh*E[i]+hh*E[j]) - allf(wv+hh*E[i]-hh*E[j]) - allf(wv-hh*E[i]+hh*E[j]) + allf(wv-hh*E[i]-hh*E[j]))/(4*hh*hh)
    for i in range(nx):
        for j in range(i, nx):
            H[:,i,j] = H[:,j,i] = (4*d2(i,j,0.05) - d2(i,j,0.1))/3
    return H
def grad_all(wv, ix, h=0.05):
    nx = len(ix); E = np.eye(27)[ix]; G = np.zeros((len(names), nx))
    for i in range(nx):
        G[:,i] = (8*(allf(wv+h*E[i]) - allf(wv-h*E[i])) - (allf(wv+2*h*E[i]) - allf(wv-2*h*E[i])))/(12*h)
    return G
Hcol = hess_all(w0, colidx)   # (13, 18, 18)
Hsng = hess_all(w0, sngidx)   # (13, 9, 9)
Gsng = grad_all(w0, sngidx)   # (13, 9)   Gradient farblos (fuer Stationaritaet)

print("="*74)
print("H203 A  Kontrolle: F4-invariantes stationaeres Potential -> Farbe masselos (H184)")
print("="*74)
l1,l2,l3 = ev0; e1,e2 = l1+l2+l3, l1*l2+l1*l3+l2*l3
cF = {"Tr W^4": 1/4, "Tr W^3": -e1/3, "Tr W^2": e2/2}   # v = l^4/4 - e1 l^3/3 + e2 l^2/2 - e3 l, v' = (l-l1)(l-l2)(l-l3)
gF = np.array([cF.get(nm, 0.0) for nm in names])
HFc = np.einsum('q,qij->ij', gF, Hcol); HFs = np.einsum('q,qij->ij', gF, Hsng)
print(f"   Farbfrequenzen (soll 0): max |EV| = {np.abs(np.linalg.eigvalsh(HFc)).max():.1e}")
print(f"   farbloser Block EV: {np.round(np.linalg.eigvalsh(HFs),4)}  (3 massive = Lepton-Moden, 6 Null aus Familien-SU(3))")
print("   -> Stationaritaet (bindet Leptonen) macht die Quarks masselos: Quarkmassen brauchen U-Terme.")

print("\n" + "="*74)
print("H203 B  Blindheit: aendern Kopplungen die Quarks (Farbe), aber nicht die Leptonen (farblos)?")
print("="*74)
# Lineare Abbildungen Kopplung -> Hesse (farblos / Farbe), als Matrizen (13 -> flach)
def flat_sym(Hstack):
    n = Hstack.shape[1]; iu = np.triu_indices(n)
    return np.array([Hstack[q][iu] for q in range(len(names))])   # (13, n(n+1)/2)
Lsng = flat_sym(Hsng)   # (13, 45)  Kopplung -> farblose Hesse
Lcol = flat_sym(Hcol)   # (13, 171) Kopplung -> Farb-Hesse
Lgrad = Gsng            # (13, 9)   Kopplung -> farbloser Gradient
rk_sng = np.linalg.matrix_rank(Lsng, tol=1e-7)
rk_col = np.linalg.matrix_rank(Lcol, tol=1e-7)
print(f"   Rang Kopplung->farblose Hesse (Leptonen): {rk_sng} von 13")
print(f"   Rang Kopplung->Farb-Hesse   (Quarks):    {rk_col} von 13")

# Kopplungen, die den farblosen Sektor GAR NICHT bewegen (Hesse UND Gradient = 0): Nullraum von [Lsng; Lgrad]
Lsng_full = np.vstack([Lsng.T, Lgrad.T]).T    # (13, 45+9)
null_lepton = null_space(Lsng_full.T, rcond=1e-7)   # Spalten: Kopplungen g mit farbloser Hesse=0 UND Gradient=0
print(f"   Kopplungsrichtungen, die den FARBLOSEN Sektor (Hesse+Gradient) voellig unberuehrt lassen: {null_lepton.shape[1]}")
# Aendern diese die Farb-(Quark)-Frequenzen?
moves_quark = 0
for a in range(null_lepton.shape[1]):
    g = null_lepton[:,a]; Hc = np.einsum('q,qij->ij', g, Hcol)
    if np.abs(Hc).max() > 1e-6: moves_quark += 1
print(f"   davon, die die FARB-(Quark)-Frequenzen aendern: {moves_quark}")

# Explizite Blind-Richtung (falls vorhanden): groesste Quark-Wirkung bei null Lepton-Wirkung
if null_lepton.shape[1] > 0:
    eff = [np.abs(np.einsum('q,qij->ij', null_lepton[:,a], Hcol)).max() for a in range(null_lepton.shape[1])]
    a = int(np.argmax(eff)); g = null_lepton[:,a]
    Hc = np.einsum('q,qij->ij', g, Hcol); Hs = np.einsum('q,qij->ij', g, Hsng); Gg = g @ Gsng
    print(f"\n   Beispiel-Blindrichtung g (Koeffizienten je Invariante):")
    for q,nm in enumerate(names):
        if abs(g[q])>1e-3: print(f"      {nm:18s}: {g[q]:+.3f}")
    print(f"   -> farblose Hesse max|.| = {np.abs(Hs).max():.1e}, farbloser Gradient max|.| = {np.abs(Gg).max():.1e} (beide ~0)")
    print(f"   -> Farb-(Quark)-Hesse Eigenwerte (distinct): {np.round(np.unique(np.round(np.linalg.eigvalsh(Hc),5)),5)} (NICHT null)")

print("\n" + "="*74)
print("H203 Entscheidung (Vorab-Kriterien)")
print("="*74)
if moves_quark > 0:
    print(f"   K2: Es gibt {moves_quark} Kopplungsrichtung(en), die die Quark-Frequenzen aendern, aber")
    print("   den Lepton-Sektor (farblose Hesse UND Stationaritaet) voellig unberuehrt lassen.")
    print("   -> Der Lepton-Sektor ist BLIND gegen diese Quark-Kopplungen. Lepton-Massen + delta")
    print("      binden die Quark-Kopplungen NICHT; D/B bleibt frei. (delta/Vakuum ist geteilt, steckt")
    print("      schon in l_k, legt aber die Kopplungsstaerken nicht fest.)")
else:
    print("   K1: Jede Kopplung, die die Quarks bewegt, bewegt auch die Leptonen -> Lepton-Massen")
    print("   binden die Quark-Kopplungen; Verhaeltnis (D/B) waere vorhergesagt.")
print("\n  Grenze: reelle Feld-Ebene (ein Quarktyp, H184); Up/Down-Spaltung (C,D) braucht H3(C x O).")
print("  H203 beantwortet: bindet der Lepton-Sektor die quarkbestimmenden Kopplungen ueberhaupt.")
