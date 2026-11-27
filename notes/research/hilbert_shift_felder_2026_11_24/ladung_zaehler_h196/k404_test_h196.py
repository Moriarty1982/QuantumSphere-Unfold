"""k404 (Test H196): Verschiebt der Ladungsterm (H182) das Quintik-Glied fuer Up anders als Down?
Modell m_s(k) = [A l_k + B l_k^2 + s*gamma*O(l_k)] / (l_i+l_j)^2, s=+1 Up, -1 Down.
O: fester ladungsungerader Zaehler eines H186-Kandidaten, auf dem Vakuum reduziert.
Vorab: notes/research/predictions/Vorab_Notiz_H196_Ladungsterm_und_Up_Down_Zaehler.md (Commit 8cfd9c5).
Aufruf: python k404_test_h196.py > k404_out.txt
"""
import numpy as np
from scipy.optimize import least_squares
rng = np.random.default_rng(404)

l = np.sort([1 + np.sqrt(2) * np.cos(2 / 9 + 2 * np.pi * k / 3) for k in range(3)])
# gemeinsame Skala (M_Z Yukawa, wie H186/H194)
mu = np.array([7.04e-6, 3.56e-3, 0.967]);   su = np.array([0.15e-6, 0.06e-3, 0.004])
md = np.array([1.54e-5, 3.06e-4, 1.630e-2]); sd = np.array([0.02e-5, 0.04e-4, 0.009e-2])
PRS = [(0, 1, 2), (0, 2, 1), (1, 2, 0)]; PERM_B = [2, 1, 0]
lk = np.array([l[k] for (i, j, k) in PRS])[PERM_B]
z = np.array([(l[i] + l[j]) ** 2 for (i, j, k) in PRS])[PERM_B]
print("l_k:", np.array2string(l, precision=6))

# ladungsungerade Zaehler-Kandidaten (auf dem Vakuum, aus H186; sympy in der Vorab)
CANDS = {
    "c1":    lambda x: 2/3 + 0*x,
    "c2":    lambda x: 1 - x/3,
    "c4/c5": lambda x: 2 - x**2/3,
    "c7/c9": lambda x: 3/2 - x + x**2/6,
    "c11":   lambda x: 7/2 - x - x**2/6,
}

def model(params, O):
    A, B, g = params
    num_e = A * lk + B * lk**2
    num_o = g * O(lk)
    mU = (num_e + num_o) / z   # s=+1
    mD = (num_e - num_o) / z   # s=-1
    return mU, mD

def resid(params, O):
    mU, mD = model(params, O)
    return np.concatenate([(mU - mu) / su, (mD - md) / sd])

print("\n=== H196b (Test): fester Kandidat, 3 Parameter (A, B, gamma) gemeinsam ===")
best = None
for nm, O in CANDS.items():
    # mehrere Startwerte
    bestloc = None
    for _ in range(40):
        p0 = rng.normal(scale=[0.1, 0.1, 0.1])
        r = least_squares(resid, p0, args=(O,), method="lm", max_nfev=5000)
        chi2 = np.sum(r.fun**2)
        if bestloc is None or chi2 < bestloc[0]:
            bestloc = (chi2, r.x)
    chi2, p = bestloc
    mU, mD = model(p, O)
    mxU = np.max(np.abs((mU - mu) / su)); mxD = np.max(np.abs((mD - md) / sd))
    print(f"  {nm:6s}: chi2={chi2:10.2f}  A={p[0]:.3e} B={p[1]:.3e} gamma={p[2]:.3e}  "
          f"max Up {mxU:6.1f} sigma, Down {mxD:6.1f} sigma")
    if best is None or chi2 < best[0]:
        best = (chi2, nm, p, mxU, mxD)
print(f"  bester Kandidat: {best[1]} (chi2={best[0]:.2f}, Up {best[3]:.1f} sigma, Down {best[4]:.1f} sigma)")
both3 = best[3] < 3 and best[4] < 3

# === H196c (Bericht): volle Ladungsstruktur 4 Parameter A,B,C,D ===
print("\n=== H196c (Bericht): volle Ladungsstruktur m_s = [A l_k + B l_k^2 + s(C l_k + D l_k^2)]/z ===")
def resid4(p):
    A, B, Cc, D = p
    aU, bU = A + Cc, B + D; aD, bD = A - Cc, B - D
    mU = (aU * lk + bU * lk**2) / z; mD = (aD * lk + bD * lk**2) / z
    return np.concatenate([(mU - mu) / su, (mD - md) / sd])
best4 = None
for _ in range(60):
    p0 = rng.normal(scale=[0.05, 0.1, 0.05, 0.1])
    r = least_squares(resid4, p0, method="lm", max_nfev=5000)
    c = np.sum(r.fun**2)
    if best4 is None or c < best4[0]: best4 = (c, r.x)
c4, p4 = best4
A, B, Cc, D = p4
print(f"  A={A:.4e} B={B:.4e} C={Cc:.4e} D={D:.4e}  chi2={c4:.2f} (2 dof)")
print(f"  ladungsgerade a,b: A={A:.3e}, B={B:.3e}; ladungsungerade C(lin)={Cc:.3e}, D(quad)={D:.3e}")
print(f"  Up  b/a = {(B+D)/(A+Cc):.3f};  Down b/a = {(B-D)/(A-Cc):.3f}")
print(f"  -> ladungsungerades l_k^2 (D) {'NOETIG, Vorzeichen '+('+' if D>0 else '-') if abs(D)>1e-6 else 'nahe 0'}; "
      f"verschiebt Up {'staerker' if (B+D)*np.sign(B)>(B-D)*np.sign(B) else 'schwaecher'} ins Quadratische als Down")
# Verhaeltnis D/C gegen die Kandidaten-Formen (fester Kandidat haette festes Verhaeltnis der ungeraden l_k, l_k^2)
print(f"  ungerades Verhaeltnis D/C = {D/Cc:.3f}")
for nm, O in CANDS.items():
    # O(l) = o0 + o1 l + o2 l^2; ungerade Teil traegt l und l^2 Anteile o1,o2 (plus const in Zaehler)
    o = np.polyfit(lk, O(lk), 2)  # o[0] l^2 + o[1] l + o[2]
    if abs(o[1]) > 1e-9:
        print(f"    {nm:6s}: Kandidaten-Verhaeltnis (l^2-Koeff)/(l-Koeff) = {o[0]/o[1]:.3f}")

# === Kontrolle ===
print("\n=== Kontrolle: 2000 erfundene Massenpaare, bester 3-Param-Kandidat ===")
Obest = CANDS[best[1]]
NF = 2000; hit = 0
for _ in range(NF):
    def fake(s, m):
        m2 = 10**rng.uniform(-3.5, -0.5); m1 = m2 * 10**rng.uniform(-3.5, -0.5)
        mf = np.array([m1, m2, 1.0]); return mf, mf * s / m
    mfU, sfU = fake(su, mu); mfD, sfD = fake(sd, md)
    def rr(p):
        A, B, g = p; ne = A*lk+B*lk**2; no = g*Obest(lk)
        return np.concatenate([((ne+no)/z-mfU)/sfU, ((ne-no)/z-mfD)/sfD])
    bl = None
    for _ in range(8):
        r = least_squares(rr, rng.normal(scale=[0.1,0.1,0.1]), method="lm", max_nfev=2000)
        c = np.sum(r.fun**2); bl = c if bl is None else min(bl, c)
    if bl < 2 * 6:  # grob: chi2 < 12 (~beide Sektoren vertraeglich)
        hit += 1
print(f"  erfundene Paare mit chi2 < 12 (fester Kandidat {best[1]}): {hit/NF:.1%}")

# === Urteil ===
print("\n=== Gesamturteil ===")
mxU4 = None
# volle Struktur-Treffer?
rr4 = resid4(p4);
full_ok = np.max(np.abs(rr4)) < 3
if both3:
    print(f"  bestaetigt: Kandidat {best[1]} traegt beide Sektoren < 3 sigma mit 3 Parametern.")
elif full_ok:
    print("  teilweise: volle Ladungsstruktur (4 Param) traegt, aber kein fester Kandidat mit 3 Param.")
    print(f"    -> ladungsungerades l_k^2 D={D:.3e} noetig; Up/Down-Split kommt aus der Ladung, aber mit freier Form.")
else:
    print("  widerlegt: auch die volle Ladungsstruktur gibt den Up/Down-Unterschied nicht < 3 sigma.")
print(f"  (bester Kandidat {best[1]}: chi2 {best[0]:.1f}; volle Struktur: chi2 {c4:.2f}, max {np.max(np.abs(rr4)):.1f} sigma)")
