"""k416 (Test H206): Ist die Korrekturrichtung IN der Ebene senkrecht v0 strukturell erzwungen?
D(psi) = cos(psi) K1 + sin(psi) K2 in der Ebene span{K1,K2} (= Ebene senkrecht v0, H205).
(A) Welche psi erhaelt Massen (Koide/Phase) UND sin delta=1, theta23=45 Grad? Eindeutig = K2?
(B) Struktur-Richtung K2 allein: sind theta23=45, |sin delta|=1 parameterfrei? theta13(kappa),theta12(kappa).
    kappa an sin^2 theta13 (Daten) pinnen -> Vorhersage theta12; vs NuFIT/JUNO.
(C) Gegenueberstellung mit der angepassten Halbierenden (K1+K2)/sqrt2 (H176).
Aufruf aus diesem Ordner: python3 k416_test_h206.py > k416_out.txt
"""
import numpy as np

# ---- Maschinerie aus k371 (DIRS, make(x)->obs,chi2, solve, C, Nhat, eig_sorted, pmns, z, X_LEP) ----
# k371 importiert selbst aus k370; wir laden den Definitionsteil (ohne __main__-Block).
code = open("../mischung_h175/k371_test_h175.py").read()
ns = {"__name__": "nicht_main"}
exec(code, ns)
DIRS, make, X_LEP = ns["DIRS"], ns["make"], ns["X_LEP"]
C, eig_sorted, pmns, z = ns["C"], ns["eig_sorted"], ns["pmns"], ns["z"]
k370 = ns["ns"]                            # innerer k370-Namensraum (Konstanten)
S12, S12E, S13, S13E = k370["S12"], k370["S12E"], k370["S13"], k370["S13E"]
S23, S23EU, S23ED = k370["S23"], k370["S23EU"], k370["S23ED"]
r2 = np.sqrt(2)
K1, K2 = DIRS["K-1"], DIRS["K-2"]
x = X_LEP
obs, chi2 = make(x)                       # obs(names,coef)->(rho,delta,pmns); refittet Massen

print("=" * 78)
print("H206 A  Welche Richtung D(psi)=cos psi K1 + sin psi K2 erhaelt Masse + sin delta=1 + th23=45?")
print("=" * 78)
# Unperturbierte geladene-Lepton-Eigenvektoren (Elektron-Zweig, delta = DE):
DE = ns["DE"]; l0, U0 = eig_sorted(C(1.0, DE))
def first_order_mass_shift(D):
    # Diagonalelemente der Stoerung in der C-Eigenbasis = Eigenwert-Verschiebungen 1. Ordnung
    return np.array([np.real(U0[:, i].conj() @ D @ U0[:, i]) for i in range(3)])
print("  Massen-Eigenwert-Verschiebung 1. Ordnung <u_i|D|u_i> (0 = massenerhaltend):")
for nm, D in (("K1", K1), ("K2", K2), ("(K1+K2)/sqrt2", (K1 + K2) / r2)):
    sh = first_order_mass_shift(D)
    print(f"    {nm:16s}: {np.round(sh, 6)}   ||.|| = {np.linalg.norm(sh):.2e}")
# Scan psi: Massen-Erhaltung (1. Ordnung) und sin delta, th23 bei kleiner Staerke
print("\n  Scan psi in [0,180): Massen-Erhaltung und (sin delta, sin^2 th23) bei kappa=0.03")
best_ms = None
for deg in range(0, 180, 5):
    ps = np.radians(deg); D = np.cos(ps) * K1 + np.sin(ps) * K2
    ms = np.linalg.norm(first_order_mass_shift(D))
    o = obs(["K-1", "K-2"], 0.03 * np.array([np.cos(ps), np.sin(ps)]))
    sd, s23 = (o[2][3], o[2][1]) if o else (np.nan, np.nan)
    if best_ms is None or ms < best_ms[1]: best_ms = (deg, ms)
    if deg % 15 == 0:
        print(f"    psi={deg:3d}: ||Massenshift||={ms:.2e}  sin delta={sd:+.4f}  sin^2 th23={s23:.4f}")
print(f"  -> minimale Massen-Verschiebung bei psi ~ {best_ms[0]} Grad (K2 = 90 Grad)")

print("\n" + "=" * 78)
print("H206 B  Struktur-Richtung K2 allein: Parameterfreiheit von th23, sin delta?")
print("=" * 78)
print("  kappa-Scan mit D = K2 (psi=90):")
print("   kappa     sin^2 th13   sin^2 th12   sin^2 th23   sin delta   Koide rho")
for kap in (0.00, 0.02, 0.0439, 0.06, 0.08):
    o = obs(["K-1", "K-2"], [0.0, kap])
    if o is None:
        print(f"   {kap:+.4f}  (Massen nicht erreichbar)"); continue
    s12, s23, s13, sd = o[2]
    print(f"   {kap:+.4f}   {s13:.6f}    {s12:.6f}    {s23:.6f}    {sd:+.4f}    {o[0]:.5f}")
# kappa an sin^2 th13 pinnen -> Vorhersage th12
from scipy.optimize import brentq
f13 = lambda k: obs(["K-1", "K-2"], [0.0, k])[2][2] - S13
try:
    kstar = brentq(f13, 0.01, 0.12)
    o = obs(["K-1", "K-2"], [0.0, kstar]); s12, s23, s13, sd = o[2]
    zz = z(s12, s23, s13)
    print(f"\n  kappa* (sin^2 th13 = {S13}) = {kstar:.5f}:")
    print(f"    sin^2 th12 = {s12:.5f}  ({zz[1]:+.1f} sigma gg NuFIT {S12})")
    print(f"    sin^2 th23 = {s23:.5f}  ({zz[2]:+.1f} sigma)   sin delta = {sd:+.4f}")
    print(f"    -> Struktur-Richtung K2 trifft th13, laesst th12 {'zu hoch' if zz[1]>0 else 'daneben'} (TM1-Problem)")
except Exception as ex:
    print("  (brentq:", ex, ")")

print("\n" + "=" * 78)
print("H206 C  Gegenueberstellung: angepasste Halbierende (K1+K2)/sqrt2 (H176)")
print("=" * 78)
f13b = lambda k: obs(["K-1", "K-2"], [k / r2, k / r2])[2][2] - S13
try:
    kb = brentq(f13b, 0.01, 0.15)
    o = obs(["K-1", "K-2"], [kb / r2, kb / r2]); s12, s23, s13, sd = o[2]; zz = z(s12, s23, s13)
    print(f"  Halbierende, kappa (sin^2 th13={S13}) = {kb:.5f}:")
    print(f"    sin^2 th12 = {s12:.5f} ({zz[1]:+.1f}s)  sin^2 th23 = {s23:.5f} ({zz[2]:+.1f}s)  sin delta = {sd:+.4f}  Koide rho={o[0]:.5f}")
    print(f"    -> bricht th23=45 ({s23:.4f}) und |sin delta|=1 ({abs(sd):.4f}), senkt dafuer th12")
except Exception as ex:
    print("  (brentq:", ex, ")")

print("\n" + "=" * 78)
print("H206 Entscheidung")
print("=" * 78)
ms_K2 = np.linalg.norm(first_order_mass_shift(K2))
ms_K1 = np.linalg.norm(first_order_mass_shift(K1))
K1crit = (ms_K2 < 1e-9) and (ms_K1 > 1e-6)
print(f"  Massenerhaltung: K2 ||shift||={ms_K2:.2e} (≈0), K1 ||shift||={ms_K1:.2e} (!=0)")
print(f"  K1 (Richtung in der Ebene strukturell erzwungen = K2) -> {'JA' if K1crit else 'NEIN'}")
print("\n  FAZIT H206 (voraussichtlich):")
print("  - Die Ebene senkrecht v0 ist aus H205 fest; IN der Ebene ist K2 die eindeutige Richtung,")
print("    die die Massen-Eigenwerte (1. Ordnung) erhaelt; K1 aendert sie. Mit K2 sind th23=45 Grad")
print("    und |sin delta|=1 parameterfreie Vorhersagen (fuer jede Staerke exakt).")
print("  - Die Struktur sagt also MAXIMALES th23 und MAXIMALE CP-Verletzung voraus und trifft th13,")
print("    laesst aber sin^2 th12 zu hoch (TM1-Problem). Die in H176 angepasste Halbierende bricht")
print("    th23/sin delta leicht, um th12 zu senken -> nicht strukturell, sondern an die Daten gepasst.")
print("  - Teilweise nicht blind (K2 = th13-Gruppe aus k372 1. Ordnung bekannt); neu: Eindeutigkeit,")
print("    exakte Parameterfreiheit von th23=45/sin delta=1, und die Gegenueberstellung.")
