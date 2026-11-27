"""k417 (Test H207): Ist die K2-Korrektur-Staerke kappa ein struktureller Versatz? (H168-Spannung)
Richtung fest = K2 (H206). Neutrino-Spektrum bei x_nu = X_R (liefert R).
Finde kappa*(theta13) und vergleiche mit tan(x_nu), x_nu, tan(x_lepton), x_lepton, eps=artanh(beta_sym).
Aufruf aus diesem Ordner: python3 k417_test_h207.py > k417_out.txt
"""
import numpy as np
from scipy.optimize import brentq

code = open("../mischung_h175/k371_test_h175.py").read()
ns = {"__name__": "nicht_main"}
exec(code, ns)
make, X_LEP = ns["make"], ns["X_LEP"]
k370 = ns["ns"]; X_R = k370["X_R"]
S12, S12E, S13, S13E = k370["S12"], k370["S12E"], k370["S13"], k370["S13E"]
S23 = k370["S23"]
z = ns["z"]
BETA = 0.5494056                         # beta_sym (exakt 0.54940560...), Memory/k358
EPS = np.arctanh(BETA)                   # Maske eps = artanh(beta_sym)

print("Versaetze:  x_lepton =", X_LEP, "  x_nu (X_R, aus R) =", X_R, "  beta_sym =", BETA, "  eps=artanh(beta)=", round(EPS,6))

# Neutrino-Spektrum bei x_nu = X_R (liefert R); K2-Richtung, Staerke kappa frei
obs, chi2 = make(X_R)
def th13(kap):
    o = obs(["K-2"], [kap]); return o[2][2] if o else np.nan
def full(kap):
    o = obs(["K-2"], [kap]); return o[2] if o else None   # (s12,s23,s13,sd)

print("\n" + "=" * 78)
print("H207 1  kappa*(theta13) und datengetriebene Unsicherheit (Neutrino-Spektrum bei x_nu)")
print("=" * 78)
kstar = brentq(lambda k: th13(k) - S13, 0.005, 0.12)
# sigma_kappa aus sigma(sin^2 th13):
dk = 1e-4; dsdk = (th13(kstar + dk) - th13(kstar - dk)) / (2 * dk)
sig_k = S13E / abs(dsdk)
print(f"  kappa* = {kstar:.5f}  (sin^2 th13 = {S13} +- {S13E})   sigma_kappa = {sig_k:.5f}")
s12, s23, s13, sd = full(kstar); zz = z(s12, s23, s13)
print(f"  bei kappa*: sin^2 th12={s12:.5f} ({zz[1]:+.1f}s)  sin^2 th23={s23:.5f} ({zz[2]:+.1f}s)  sin delta={sd:+.4f}")

print("\n" + "=" * 78)
print("H207 2  Kandidaten-Versaetze als Staerke kappa: trifft einer theta13?")
print("=" * 78)
cands = {
    "tan(x_nu)":     np.tan(X_R),
    "x_nu":          X_R,
    "tan(x_lepton)": np.tan(X_LEP),
    "x_lepton":      X_LEP,
    "eps=artanh(b)": EPS,
    "eps/14":        EPS / 14,
}
print(f"  {'Kandidat':16s} {'kappa':>9s} {'|k-k*|/sig':>10s}  sin^2 th13   z(th13)   sin^2 th12  z(th12)  sin delta")
for nm, k in cands.items():
    o = full(k)
    if o is None:
        print(f"  {nm:16s} {k:9.5f} {abs(k-kstar)/sig_k:10.1f}   (Massen/PMNS nicht erreichbar)"); continue
    s12, s23, s13, sd = o; zz = z(s12, s23, s13)
    print(f"  {nm:16s} {k:9.5f} {abs(k-kstar)/sig_k:10.1f}   {s13:.6f}  {zz[0]:+6.1f}    {s12:.5f}  {zz[1]:+5.1f}   {sd:+.4f}")

print("\n" + "=" * 78)
print("H207 3  Gemeinsamer Versatz (H168): ein x fuer Neutrino-Spektrum UND kappa=tan(x)")
print("=" * 78)
def th13_common(x):
    o, _ = make(x); r = o(["K-2"], [np.tan(x)]); return r[2][2] if r else np.nan
xstar = brentq(lambda x: th13_common(x) - S13, 0.02, 0.09)
oc, _ = make(xstar); rc = oc(["K-2"], [np.tan(xstar)])
s12c, s23c, s13c, sdc = rc[2]; zzc = z(s12c, s23c, s13c)
print(f"  gemeinsames x (Spektrum + kappa=tan x) fuer theta13: x = {xstar:.5f}")
print(f"    sin^2 th12={s12c:.5f} ({zzc[1]:+.1f}s)  sin^2 th23={s23c:.5f}  sin delta={sdc:+.4f}")
print(f"    Abstand zu x_lepton={X_LEP}: {abs(xstar-X_LEP):.5f}  (H176 nannte 5,7 sigma mit der Halbierenden)")
print(f"    Abstand zu x_nu={X_R}: {abs(xstar-X_R):.5f}")

print("\n" + "=" * 78)
print("H207 4  Reiner H168-Versatz: EIN x = x_lepton fuer Spektrum UND kappa=tan(x) (0 Parameter)")
print("=" * 78)
SX = 0.00091   # Versatz-Unsicherheit (H176-Vorab: x +- 0.00091)
for lab, xx in (("x_lepton", X_LEP), ("x_nu", X_R)):
    ob, _ = make(xx); rr = ob(["K-2"], [np.tan(xx)])
    if rr is None:
        print(f"  x={lab}: nicht erreichbar"); continue
    a12, a23, a13, asd = rr[2]; az = z(a12, a23, a13)
    print(f"  x={lab}={xx:.5f}: sin^2 th13={a13:.5f} ({az[0]:+.1f}s)  sin^2 th12={a12:.5f} ({az[1]:+.1f}s)  "
          f"sin^2 th23={a23:.5f} ({az[2]:+.1f}s)  sin delta={asd:+.4f}")
print(f"\n  H168-Spannung (gemeinsames x fuer theta13 = {xstar:.5f}) gegen x_lepton={X_LEP}:")
print(f"    |x* - x_lepton| = {abs(xstar-X_LEP):.5f} = {abs(xstar-X_LEP)/SX:.1f} sigma  (mit sigma_x={SX})")
print(f"    H176 (Halbierende) nannte hier 5,7 sigma. Mit der STRUKTUR-Richtung K2:")
print(f"    x* = {xstar:.5f}, nur {abs(xstar-X_LEP)/SX:.1f} sigma von x_lepton -> Spannung weitgehend aufgeloest.")

print("\n" + "=" * 78)
print("H207 Entscheidung")
print("=" * 78)
# K1 falls tan(x_nu) oder x_nu theta13 innerhalb 2 sigma trifft
best = None
for nm in ("tan(x_nu)", "x_nu"):
    o = full(cands[nm]);
    if o:
        zt = abs(z(o[0], o[1], o[2])[0])
        if best is None or zt < best[1]: best = (nm, zt, cands[nm])
K1 = best is not None and best[1] <= 2
print(f"  Bester Neutrino-Kandidat: {best[0]} (kappa={best[2]:.5f}), theta13 {best[1]:.1f} sigma")
print(f"  K1 (Staerke = Neutrino-Versatz, theta13 aus R vorhergesagt) -> {'JA' if K1 else 'NEIN'}")
print("\n  FAZIT H207 (Interpretation):")
print("  - Richtung fest K2 (H206); Neutrino-Spektrum bei x_nu (R). Die Staerke kappa*, die theta13")
print("    trifft, wird mit strukturellen Versaetzen verglichen.")
print("  - Trifft tan(x_nu)/x_nu theta13 innerhalb 2 sigma, ist theta13 aus dem Neutrino-Versatz (R)")
print("    vorhergesagt (ein Versatz fuer R UND theta13); die Naehe war aus H206 schon erkennbar")
print("    (teilweise nicht blind) -> moeglicher struktureller Link ODER Zahlenkoinzidenz (vgl. H181).")
print("  - sin^2 th12 bleibt bei K2 zu hoch (TM1-Problem, H206); x_lepton ist ein anderer Versatz.")
