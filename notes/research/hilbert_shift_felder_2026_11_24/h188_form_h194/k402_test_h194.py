"""k402 (Test H194): Die H188-Form m ~ (a l_k + b l_k^2)/(l_i+l_j)^2 mit einer unabhaengigen Vorhersage.
Vorab: notes/research/predictions/Vorab_Notiz_H194_H188_Form_unabhaengige_Vorhersage.md (Commit 615c984).
Aufruf: python k402_test_h194.py > k402_out.txt

H194a: bekannter Zwei-Parameter-Fit je Sektor (Kontrolle, nicht blind).
H194b: ein gemeinsames rho = b/a fuer beide Sektoren, Gesamtskala je Sektor frei (Test).
H194c: Spezifitaet der leptonischen l_k gegen zufaellige l-Tripel und alle Index-Permutationen (Test).
"""
import numpy as np
from itertools import permutations
rng = np.random.default_rng(402)

# --- leptonische Eigenwerte l_k (W0, K=2/3, delta=2/9), aus H184/k391c ---
l = np.sort([1 + np.sqrt(2) * np.cos(2 / 9 + 2 * np.pi * k / 3) for k in range(3)])
print("l_k (Leptonvakuum, delta=2/9):", np.array2string(l, precision=6))

# --- Daten (M_Z, wie H188) ---------------------------------------------------
mu = np.array([7.04e-6, 3.56e-3, 0.967]);   su = np.array([0.15e-6, 0.06e-3, 0.004])
md = np.array([1.54e-5, 3.06e-4, 1.630e-2]); sd = np.array([0.02e-5, 0.04e-4, 0.009e-2])

# Zuordnung B (k391c): perm = [2,1,0]; je Generation ein (i,j,k).
# prs: (i,j,k)-Tripel; perm ordnet die drei Generationen.
PRS = [(0, 1, 2), (0, 2, 1), (1, 2, 0)]
def basis(lvals, perm):
    """gibt f1 = l_k/z, f2 = l_k^2/z je Generation, mit z = (l_i+l_j)^2, in Generationsreihenfolge perm."""
    lk = np.array([lvals[k] for (i, j, k) in PRS])
    z = np.array([(lvals[i] + lvals[j]) ** 2 for (i, j, k) in PRS])
    f1 = (lk / z)[perm]; f2 = (lk ** 2 / z)[perm]
    return f1, f2

PERM_B = [2, 1, 0]

# === H194a: bekannter Zwei-Parameter-Fit je Sektor (Kontrolle) ===============
print("\n=== H194a (Kontrolle, nicht blind): freier Fit (a,b) je Sektor ===")
def fit_ab(m, s, f1, f2):
    A = np.stack([f1 / s, f2 / s], axis=1)
    co, *_ = np.linalg.lstsq(A, m / s, rcond=None)
    pred = co[0] * f1 + co[1] * f2
    chi2 = np.sum(((pred - m) / s) ** 2)
    return co, chi2, (pred - m) / s
for nm, m, s in (("Up", mu, su), ("Down", md, sd)):
    f1, f2 = basis(l, PERM_B)
    co, chi2, res = fit_ab(m, s, f1, f2)
    print(f"  {nm:4s}: a={co[0]:.4e} b={co[1]:.4e} b/a={co[1]/co[0]:.3f}  chi2={chi2:.2f}  Abst {np.array2string(res, precision=2)} sigma")
f1, f2 = basis(l, PERM_B)
_, chi2_u0, _ = fit_ab(mu, su, f1, f2)
_, chi2_d0, _ = fit_ab(md, sd, f1, f2)

# === H194b: ein gemeinsames rho fuer beide Sektoren ==========================
# m_gen = S * (l_k + rho l_k^2)/z = S * (f1 + rho f2). Fuer festes rho: S per LS (1 Param).
print("\n=== H194b (Test): ein gemeinsames rho = b/a fuer beide Sektoren, Skala je Sektor frei ===")
def chi2_rho(rho, m, s, f1, f2):
    g = f1 + rho * f2
    S = np.sum(m * g / s ** 2) / np.sum(g ** 2 / s ** 2)
    pred = S * g
    return np.sum(((pred - m) / s) ** 2), S, (pred - m) / s
f1, f2 = basis(l, PERM_B)
# dichte Suche + Verfeinerung ueber rho (b/a); bekannte Einzelwerte -57.9 und -0.085
rhos = np.concatenate([np.linspace(-200, 50, 400001)])
worst = np.array([max(chi2_rho(r, mu, su, f1, f2)[0], chi2_rho(r, md, sd, f1, f2)[0]) for r in rhos])
ib = np.argmin(worst); rb = rhos[ib]
cu, Su, ru = chi2_rho(rb, mu, su, f1, f2); cd, Sd, rd = chi2_rho(rb, md, sd, f1, f2)
print(f"  bestes gemeinsames rho = {rb:.4f}: Up chi2={cu:.1f} (Abst {np.array2string(ru, precision=1)}), "
      f"Down chi2={cd:.1f} (Abst {np.array2string(rd, precision=1)})")
print(f"  schlechtester Sektor-max-Abstand bei diesem rho: Up {np.max(np.abs(ru)):.1f} sigma, Down {np.max(np.abs(rd)):.1f} sigma")
# einzelne optimale rho je Sektor zum Vergleich
for nm, m, s in (("Up", mu, su), ("Down", md, sd)):
    cs = np.array([chi2_rho(r, m, s, f1, f2)[0] for r in rhos])
    j = np.argmin(cs); print(f"  (zum Vergleich) {nm} allein optimal bei rho={rhos[j]:.3f}, chi2={cs[j]:.2f}")
both3 = (np.max(np.abs(ru)) < 3) and (np.max(np.abs(rd)) < 3)
print(f"  Kriterium bestaetigt (beide < 3 sigma mit EINEM rho): {'JA' if both3 else 'NEIN'}")

# === H194c: Spezifitaet der leptonischen l_k ================================
print("\n=== H194c (Test): Spezifitaet der leptonischen l_k ===")
# alle 6 Index-Permutationen der Generationszuordnung mit den echten l_k
print("  alle 6 Index-Permutationen (echte l_k):")
best_perm = None
for perm in permutations(range(3)):
    f1, f2 = basis(l, list(perm))
    _, cu, _ = fit_ab(mu, su, f1, f2); _, cd, _ = fit_ab(md, sd, f1, f2)
    tag = "  <- Zuordnung B" if list(perm) == PERM_B else ""
    print(f"    perm {perm}: Up chi2={cu:7.2f}  Down chi2={cd:7.2f}{tag}")
    if best_perm is None or max(cu, cd) < best_perm[0]:
        best_perm = (max(cu, cd), perm)
# Zufaellige l-Tripel durch denselben Fit (Zuordnung B)
print("\n  2000 zufaellige l-Tripel (gleiche Normierung, Zuordnung B):")
NF = 2000
cnt_both = 0; cnt_up = 0; cnt_dn = 0
for _ in range(NF):
    lr = np.sort(rng.uniform(0.01, 3.0, 3))  # gleiche Groessenordnung wie l
    f1, f2 = basis(lr, PERM_B)
    if np.any(~np.isfinite(f1)) or np.any(~np.isfinite(f2)):
        continue
    _, cu, _ = fit_ab(mu, su, f1, f2); _, cd, _ = fit_ab(md, sd, f1, f2)
    if cu <= chi2_u0: cnt_up += 1
    if cd <= chi2_d0: cnt_dn += 1
    if cu <= chi2_u0 and cd <= chi2_d0: cnt_both += 1
print(f"    beobachtet (echte l_k, B): Up chi2={chi2_u0:.2f}, Down chi2={chi2_d0:.2f}")
print(f"    Zufalls-l erreichen/unterbieten Up: {cnt_up/NF:.1%}, Down: {cnt_dn/NF:.1%}, beide: {cnt_both/NF:.1%}")

# === Nachtraeglich (kein Test): rho gegen Modellwerte ========================
print("\n=== Nachtraeglich (kein Test): b/a gegen Modellwerte ===")
beta = 0.5494056410; gammaL = 1.8646997646
f1, f2 = basis(l, PERM_B)
cou, _, _ = fit_ab(mu, su, f1, f2); cod, _, _ = fit_ab(md, sd, f1, f2)
bau = cou[1]/cou[0]; bad = cod[1]/cod[0]
print(f"  b/a Up={bau:.4f}, Down={bad:.4f}; Produkt={bau*bad:.4f}, Verh.={bau/bad:.2f}")
print(f"  Modellwerte: beta={beta:.4f}, gammaL={gammaL:.4f}, 1/l1={1/l[0]:.3f}, -1/l1={-1/l[0]:.3f}, l3={l[2]:.3f}")
print(f"  Vergleich: b/a Up vs -1/l1 ({-1/l[0]:.2f}) Abstand {abs(bau+1/l[0])/abs(1/l[0])*100:.1f}%; "
      f"b/a Down vs -l1 ({-l[0]:.3f}) Abstand {abs(bad+l[0])/l[0]*100:.1f}%")

# === Urteil ==================================================================
print("\n=== Gesamturteil ===")
spezifisch = cnt_both / NF < 0.05 and best_perm[1] == tuple(PERM_B)
if both3:
    print("  Form traegt: ein gemeinsames rho bringt beide Sektoren < 3 sigma (H194b).")
elif spezifisch:
    print("  Form teilweise gestuetzt: leptonische l_k sind spezifisch (H194c), aber kein gemeinsames rho.")
else:
    print("  widerlegt als eigenstaendiger Befund: kein gemeinsames rho (H194b),")
    print("  und der Zwei-Parameter-Fit ist nicht spezifisch fuer die leptonischen l_k (H194c).")
print(f"  (H194b bestes gemeinsames rho: worst {max(np.max(np.abs(ru)),np.max(np.abs(rd))):.1f} sigma; "
      f"H194c Zufalls-l beide {cnt_both/NF:.1%})")
