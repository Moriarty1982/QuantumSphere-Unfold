"""k403 (Test H195): Die aus der Feldgleichung hergeleitete Form m ~ (A + B l_k)/(l_i+l_j)^2 gegen die Quarkmassen,
Vergleich mit der nachtraeglichen H188-Form (a l_k + b l_k^2)/(l_i+l_j)^2.
Vorab: notes/research/predictions/Vorab_Notiz_H195_H188_Form_aus_der_Feldgleichung.md (Commit a5f2f6d).
Aufruf: python k403_test_h195.py > k403_out.txt
"""
import numpy as np
from itertools import permutations
rng = np.random.default_rng(403)

l = np.sort([1 + np.sqrt(2) * np.cos(2 / 9 + 2 * np.pi * k / 3) for k in range(3)])
S = l.sum()
mu = np.array([7.04e-6, 3.56e-3, 0.967]);   su = np.array([0.15e-6, 0.06e-3, 0.004])
md = np.array([1.54e-5, 3.06e-4, 1.630e-2]); sd = np.array([0.02e-5, 0.04e-4, 0.009e-2])
PRS = [(0, 1, 2), (0, 2, 1), (1, 2, 0)]
PERM_B = [2, 1, 0]
print("l_k:", np.array2string(l, precision=6), " S=Tr W0 =", round(S, 6))

def cols(lv, perm):
    lk = np.array([lv[k] for (i, j, k) in PRS])
    z = np.array([(lv[i] + lv[j]) ** 2 for (i, j, k) in PRS])
    return lk[perm], z[perm]

def fit2(m, s, b1, b2):
    A = np.stack([b1 / s, b2 / s], axis=1)
    co, *_ = np.linalg.lstsq(A, m / s, rcond=None)
    pred = co[0] * b1 + co[1] * b2
    return co, np.sum(((pred - m) / s) ** 2), (pred - m) / s

lk, z = cols(l, PERM_B)
# hergeleitete Form: Basis (1/z, l_k/z)  -> m = (A + B l_k)/z
# H188-Form:        Basis (l_k/z, l_k^2/z) -> m = (a l_k + b l_k^2)/z
print("\n=== H195b: hergeleitete Form m = (A + B l_k)/(l_i+l_j)^2 ===")
res195 = {}
for nm, m, s in (("Up", mu, su), ("Down", md, sd)):
    co, chi2, r = fit2(m, s, 1.0 / z, lk / z)
    res195[nm] = (co, chi2, r)
    print(f"  {nm:4s}: A={co[0]:.4e} B={co[1]:.4e} B/A={co[1]/co[0]:.3f}  chi2={chi2:.2f}  Abst {np.array2string(r, precision=2)} sigma")

print("\n=== Vergleich: H188-Form m = (a l_k + b l_k^2)/(l_i+l_j)^2 ===")
res188 = {}
for nm, m, s in (("Up", mu, su), ("Down", md, sd)):
    co, chi2, r = fit2(m, s, lk / z, lk ** 2 / z)
    res188[nm] = (co, chi2, r)
    print(f"  {nm:4s}: a={co[0]:.4e} b={co[1]:.4e} b/a={co[1]/co[0]:.3f}  chi2={chi2:.2f}  Abst {np.array2string(r, precision=2)} sigma")

print("\n  Urteil H195b je Sektor (hergeleitet < 3 sigma? und >= so gut wie H188?):")
for nm in ("Up", "Down"):
    c195 = res195[nm][1]; c188 = res188[nm][1]
    mx195 = np.max(np.abs(res195[nm][2]))
    print(f"    {nm:4s}: hergeleitet chi2={c195:.2f} (max {mx195:.2f} sigma), H188 chi2={c188:.2f} "
          f"-> {'beide<3' if mx195<3 else 'NICHT <3'}; hergeleitet {'besser/gleich' if c195<=c188+1e-9 else 'schlechter'}")

# === H195c: woher koennte l_k^2 kommen? andere kinetische Gewichtungen ===
print("\n=== H195c: andere Nenner / Zaehler aus Feldgleichungs-Bausteinen ===")
# Nenner-Varianten aus kinetischer Gewichtung: N0->const (z^0), N1->(l_i+l_j) (z^{1/2}), N2->(l_i+l_j)^2 (z)
lipj = np.array([(l[i] + l[j]) for (i, j, k) in PRS])[PERM_B]
denoms = {"(l_i+l_j)^2 [W^2-Norm]": z, "(l_i+l_j) [W-Norm]": lipj, "1 [flache Norm]": np.ones(3)}
# Zaehler-Bausteine aus den Invarianten-Kruemmungen (auf dem Vakuum): nur const und l_k verfuegbar.
# Teste jede Kombination (Zaehler in {1, l_k}, Nenner-Variante) ob ein Sektor l_k^2-artiges Verhalten braucht.
print("  Beste 2-Parameter-Fits je Nenner (Zaehler A + B l_k):")
for dn, zz in denoms.items():
    line = []
    for nm, m, s in (("Up", mu, su), ("Down", md, sd)):
        _, chi2, _ = fit2(m, s, 1.0 / zz, lk / zz)
        line.append(f"{nm} chi2={chi2:.1f}")
    print(f"    Nenner {dn:26s}: {'  '.join(line)}")
# Gibt es einen U-/ladungsabhaengigen Baustein, der l_k^2 erzeugt? Die Tabelle H184 hat keinen reinen l_k^2;
# teste, ob der Zaehler l_k^2 (statt const) noetig ist, indem wir (l_k, l_k^2)/z gegen (1, l_k)/z vergleichen (oben).
print("  -> l_k^2 kommt in keiner Invarianten-Kruemmung auf dem Vakuum vor (symbolisch gezeigt, k403b).")

# === Kontrolle ===
print("\n=== Kontrolle: 2000 erfundene Massensaetze, hergeleitete Form ===")
NF = 2000; hu = hd = hb = 0
for _ in range(NF):
    def fake(s, m):
        m2 = 10 ** rng.uniform(-3.5, -0.5); m1 = m2 * 10 ** rng.uniform(-3.5, -0.5)
        mf = np.array([m1, m2, 1.0]); return mf, mf * s / m
    mfU, sfU = fake(su, mu); mfD, sfD = fake(sd, md)
    _, cU, _ = fit2(mfU, sfU, 1.0 / z, lk / z); _, cD, _ = fit2(mfD, sfD, 1.0 / z, lk / z)
    if cU < 3: hu += 1
    if cD < 3: hd += 1
    if cU < 3 and cD < 3: hb += 1
print(f"  ein Sektor < 3: Up {hu/NF:.1%}, Down {hd/NF:.1%}; beide < 3: {hb/NF:.1%}")

# === Urteil ===
print("\n=== Gesamturteil ===")
mxU = np.max(np.abs(res195["Up"][2])); mxD = np.max(np.abs(res195["Down"][2]))
both = mxU < 3 and mxD < 3
atleast = (res195["Up"][1] <= res188["Up"][1] + 1e-9) and (res195["Down"][1] <= res188["Down"][1] + 1e-9)
if both and atleast:
    print("  bestaetigt: die hergeleitete Form trifft beide Sektoren < 3 sigma und mind. so gut wie H188.")
elif both:
    print("  teilweise: hergeleitete Form trifft beide < 3 sigma, aber schlechter als die H188-Form (l_k^2 bevorzugt).")
elif mxU < 3 or mxD < 3:
    print("  teilweise: Nenner hergeleitet, aber die hergeleitete Form trifft nur einen Sektor.")
else:
    print("  widerlegt: die hergeleitete Form trifft keinen Sektor; die Feldgleichung gibt diese Form nicht tragend.")
print(f"  (hergeleitet: Up {mxU:.1f} sigma / chi2 {res195['Up'][1]:.1f}, Down {mxD:.1f} sigma / chi2 {res195['Down'][1]:.1f}; "
      f"H188: Up chi2 {res188['Up'][1]:.1f}, Down chi2 {res188['Down'][1]:.1f})")
