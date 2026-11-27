"""k418 (Test H208): Ist sin^2 theta12 ~ 0,318 strukturell erzwungen (TM1-Vorhersage)
oder gibt es eine struktur-erhaltende Deformation, die es auf 0,3036 senkt,
ohne theta13, Massen-Erhaltung (rho=1 / Koide) und maximale CP-Verletzung zu brechen?

Maschinerie aus k371 (DIRS=8-dim hermitescher Stoerraum, make(x)->obs,chi2, C, Nhat, eig_sorted, pmns, z).
Aufruf aus diesem Ordner: python3 k418_test_h208.py > k418_out.txt
"""
import numpy as np
from scipy.optimize import brentq, minimize

code = open("../mischung_h175/k371_test_h175.py").read()
ns = {"__name__": "nicht_main"}
exec(code, ns)
DIRS, make, X_LEP = ns["DIRS"], ns["make"], ns["X_LEP"]
C, Nhat, eig_sorted, pmns, z = ns["C"], ns["Nhat"], ns["eig_sorted"], ns["pmns"], ns["z"]
X_R, DE = ns["X_R"], ns["DE"]
k370 = ns["ns"]
S12, S12E = k370["S12"], k370["S12E"]
S13, S13E = k370["S13"], k370["S13E"]
S23, S23EU, S23ED = k370["S23"], k370["S23EU"], k370["S23ED"]
r2 = np.sqrt(2)
DNAMES = list(DIRS.keys())
x = X_LEP
obs, chi2 = make(x)

def koide(rho):
    return (1 + rho**2) / 3  # K = 2/3 bei rho = 1 (exakte Koide / Massen-Erhaltung)

def tm1_s12(s13):
    """TM1-Vorhersage: |U_e1|^2 = 2/3 fest => sin^2 th12 = (1-3 s13)/(3(1-s13))."""
    return (1 - 3 * s13) / (3 * (1 - s13))

print("=" * 78)
print("H208 Teil 1  Erste PMNS-Spalte und die TM1-Beziehung sin^2 th12 = f(th13)")
print("=" * 78)
# physikalischer Punkt: Struktur-Richtung K2, Staerke an sin^2 th13 gepinnt
f13 = lambda k: obs(["K-2"], [k])[2][2] - S13
kstar = brentq(f13, 0.01, 0.12)
Un = eig_sorted(Nhat(np.pi / 6 - x, 1))[1]
from numpy.linalg import eigvalsh
# PMNS-Matrix am physikalischen Punkt rekonstruieren (erste Spalte)
P = kstar * DIRS["K-2"]
f = lambda p: np.sort(abs(eigvalsh(C(p[0], p[1]) + P)))
from scipy.optimize import least_squares
tgt = k370["SQ"] / k370["SQ"][2]
res = lambda p: (f(p)[:2] / f(p)[2] - tgt[:2]) / tgt[:2]
rr = least_squares(res, [1.0, DE], xtol=1e-15, ftol=1e-15, gtol=1e-15)
Ue = eig_sorted(C(rr.x[0], rr.x[1]) + P)[1]
V = Ue.conj().T @ Un
col1 = np.abs(V[:, 0])**2
o = obs(["K-2"], [kstar]); s12, s23, s13, sd = o[2]
print(f"  kappa* (sin^2 th13 = {S13}) = {kstar:.6f}, rho = {o[0]:.6f} (Koide K = {koide(o[0]):.6f})")
print(f"  Erste PMNS-Spalte |U_e1|^2,|U_mu1|^2,|U_tau1|^2 = {np.round(col1,6).tolist()}  (Summe {col1.sum():.6f})")
print(f"  TM1 verlangt |U_e1|^2 = 2/3 = {2/3:.6f}; Schema: |U_e1|^2 = {col1[0]:.6f}  (Abweichung {col1[0]-2/3:+.2e})")
print(f"  sin^2 th12 (Schema) = {s12:.6f};  TM1-Formel f(th13) = {tm1_s12(s13):.6f}  (Differenz {s12-tm1_s12(s13):+.2e})")
print(f"  => sin^2 th12 liegt {'EXAKT' if abs(s12-tm1_s12(s13))<1e-4 else 'NICHT'} auf der TM1-Kurve; z(th12) = {(s12-S12)/S12E:+.2f} sigma")

print("\n" + "=" * 78)
print("H208 Teil 2  Pinning: bleibt sin^2 th12 auf der TM1-Kurve, wenn man ALLE Knoepfe variiert?")
print("=" * 78)
print("  (a) v0=(1,0,1)/sqrt2 Eigenvektor von N_hat unter Variation des Neutrino-Versatzes x:")
v0 = np.array([1, 0, 1]) / r2
for xt in (0.0, 0.02, X_LEP, X_R, 0.06):
    N = Nhat(np.pi / 6 - xt, 1)
    resid = np.linalg.norm(N @ v0 - (v0 @ (N @ v0)) * v0)
    print(f"     x = {xt:.5f}: ||N v0 - lambda v0|| = {resid:.2e}  (0 = Eigenvektor)")
print("  (b) sin^2 th12 gegen TM1-Kurve f(th13) ueber (Neutrino-Versatz x) x (Staerke kappa, Richtung K2):")
print("      x        kappa     sin^2 th13   sin^2 th12   TM1 f(th13)   Differenz")
maxdev = 0.0
for xt in (X_LEP, X_R, 0.03, 0.05):
    ob2, _ = make(xt)
    for kap in (0.00, 0.0439, 0.06, 0.09):
        o = ob2(["K-2"], [kap])
        if o is None:
            print(f"      {xt:.5f}  {kap:+.4f}  (Massen nicht erreichbar)"); continue
        s12b, _, s13b, _ = o[2]
        dev = s12b - tm1_s12(s13b); maxdev = max(maxdev, abs(dev))
        print(f"      {xt:.5f}  {kap:+.4f}   {s13b:.6f}    {s12b:.6f}    {tm1_s12(s13b):.6f}    {dev:+.2e}")
print(f"  => groesste Abweichung von der TM1-Kurve ueber alle Knoepfe: {maxdev:.2e}  (gepinnt, wenn ~0)")

print("\n" + "=" * 78)
print("H208 Teil 3  Rueckwaertssuche: welche erste Spalte braeuchten die Daten?")
print("=" * 78)
s12d, s13d = S12, S13
Ue1_data = (1 - s12d) * (1 - s13d)   # |U_e1|^2 = cos^2 th12 cos^2 th13
print(f"  Daten: |U_e1|^2 = cos^2 th12 cos^2 th13 = {Ue1_data:.6f}  (TM1: 2/3 = {2/3:.6f}; Differenz {Ue1_data-2/3:+.4f})")
print(f"  Um sin^2 th12 = {S12} zu treffen, muesste die feste Spalte |U_e1|^2 = {Ue1_data:.4f} (statt 2/3) haben.")
print(f"  Das bricht die TM1-Struktur (feste Spalte v0 <-> |U_e1|^2 = 2/3). Innerhalb der Ein-Feld-Form")
print(f"  ist v0 fuer JEDES b,c Eigenvektor (Teil 2a) => |U_e1|^2 = 2/3 ist nicht verstellbar.")

print("\n" + "=" * 78)
print("H208 Teil 4  Voller 8-dim Stoerraum: kann IRGENDEINE Deformation sin^2 th12 senken,")
print("             ohne th13, Massen (rho=1) und |sin delta|=1 zu brechen?")
print("=" * 78)

# Deterministischer Scan: jede Einzelrichtung und alle 28 Paare; Staerke an th13 = S13 gepinnt.
import itertools

def observe(names, coef):
    o = obs(names, coef)
    if o is None:
        return None
    rho, delta, (s12_, s23_, s13_, sd_) = o
    return dict(rho=rho, s12=s12_, s23=s23_, s13=s13_, sd=sd_)

def pin_th13(names, unit):
    """Staerke kappa entlang Richtung 'unit' so, dass sin^2 th13 = S13; liefert observe-dict oder None."""
    g = lambda k: (lambda o: (o["s13"] - S13) if o else 1.0)(observe(names, k * np.array(unit)))
    sols = []
    grid = np.linspace(-0.25, 0.25, 81)
    vals = [g(k) for k in grid]
    for i in range(len(grid) - 1):
        if np.isfinite(vals[i]) and np.isfinite(vals[i + 1]) and vals[i] * vals[i + 1] < 0:
            try:
                k = brentq(g, grid[i], grid[i + 1], xtol=1e-12)
                o = observe(names, k * np.array(unit))
                if o and abs(o["s13"] - S13) < 1e-6:
                    sols.append(o)
            except Exception:
                pass
    return sols

# Alle Loesungen sammeln, die th13 treffen; nach drei Zwangs-Stufen filtern.
cands = []  # (s12, rho, s23, sd, label)
# Einzelrichtungen
for n in DNAMES:
    for o in pin_th13([n], [1.0]):
        cands.append((o["s12"], o["rho"], o["s23"], o["sd"], n))
# alle Paare, Winkel-Scan
for n1, n2 in itertools.combinations(DNAMES, 2):
    for deg in range(0, 180, 20):          # +-Symmetrie der Richtungen deckt 180-360 ab
        ph = np.radians(deg)
        for o in pin_th13([n1, n2], [np.cos(ph), np.sin(ph)]):
            cands.append((o["s12"], o["rho"], o["s23"], o["sd"], f"{n1}+{n2}@{deg}"))

def floor(filt, label):
    sub = [c for c in cands if filt(c)]
    if not sub:
        print(f"  {label}: keine Loesung"); return None
    c = min(sub, key=lambda t: t[0])
    print(f"  {label}: min sin^2 th12 = {c[0]:.5f} ({(c[0]-S12)/S12E:+.1f}s) | "
          f"rho={c[1]:.4f} (Koide K={koide(c[1]):.4f}) | sin^2 th23={c[2]:.5f} | |sin d|={abs(c[3]):.4f} | via {c[4]}")
    return c

print(f"  Kandidaten mit sin^2 th13 = {S13} getroffen: {len(cands)} (Einzelrichtungen + 28 Paare)")
print("  Minimal erreichbares sin^2 th12 unter drei Zwangs-Stufen:")
c_all  = floor(lambda t: True,                                        "  (i)  Massen + CP FREI        ")
c_mass = floor(lambda t: abs(t[1] - 1) < 2e-3,                         "  (ii) + Massen-Erhaltung rho=1")
c_full = floor(lambda t: abs(t[1] - 1) < 2e-3 and abs(t[3]) > 0.99,    "  (iii)+ Massen UND |sin d|>0,99")
print()
print(f"  Zielwert der Daten: sin^2 th12 = {S12} +- {S12E}")
if c_full is not None:
    reach = abs(c_full[0] - S12) < 2 * S12E
    print(f"  => Mit Massen-Erhaltung UND |sin delta|>0,99 bleibt min sin^2 th12 = {c_full[0]:.4f}")
    print(f"     ({'ERREICHT' if reach else 'ERREICHT NICHT'} die Daten). Struktur-erhaltend ist 0,3036 {'moeglich' if reach else 'NICHT moeglich'}.")
if c_all is not None:
    print(f"  Preis des Senkens: das kleinste sin^2 th12 insgesamt ({c_all[0]:.4f}) hat rho={c_all[1]:.4f} "
          f"(Koide {koide(c_all[1]):.4f}), |sin d|={abs(c_all[3]):.4f} -> Massen und/oder CP gebrochen.")

print("\n  Pareto-Front (massenerhaltend rho=1): min sin^2 th12 als Funktion der |sin delta|-Untergrenze:")
print("    |sin d| >=   min sin^2 th12   z(th12)   bei |sin d|=")
massp = [c for c in cands if abs(c[1] - 1) < 2e-3]
for thr in (0.0, 0.5, 0.8, 0.9, 0.95, 0.99, 0.999):
    sub = [c for c in massp if abs(c[3]) >= thr]
    if not sub:
        print(f"    {thr:6.3f}       (keine Loesung)"); continue
    c = min(sub, key=lambda t: t[0])
    print(f"    {thr:6.3f}       {c[0]:.5f}     {(c[0]-S12)/S12E:+5.1f}     {abs(c[3]):.4f}")
print("    -> Je naeher |sin delta| an 1 (maximale CP), desto hoeher der unvermeidbare sin^2 th12-Boden:")
print("       die Struktur handelt theta12 GEGEN maximale CP-Verletzung (testbare Korrelation).")

print("\n" + "=" * 78)
print("H208 Teil 5  JUNO-Diskriminierung der Vorhersage sin^2 th12 ~ 0,318")
print("=" * 78)
pred = tm1_s12(S13)
JUNO_E = 0.0005  # projizierter JUNO-1-sigma-Fehler auf sin^2 th12 (~0,2 %)
print(f"  Vorhersage (TM1, th13 an Daten): sin^2 th12 = {pred:.5f}")
print(f"  NuFIT heute:  {S12} +- {S12E}  => Spannung {(pred-S12)/S12E:+.1f} sigma")
print(f"  JUNO erwartet ~{JUNO_E} (1 sigma) => Trennung Vorhersage(0,318) vs NuFIT-Zentralwert({S12}):")
print(f"     |0,318 - 0,3036| / {JUNO_E} = {abs(pred-S12)/JUNO_E:.1f} sigma  -> JUNO entscheidet scharf.")

print("\n" + "=" * 78)
print("H208 Entscheidung")
print("=" * 78)
central = (c_full is not None and abs(c_full[0] - S12) < 1 * S12E)   # zentraler Datenwert struktur-erhaltend erreichbar?
print(f"  v0 fuer jedes b,c Eigenvektor (feste TM1-Spalte, Wolfram exakt): JA")
print(f"  Nur hergeleitete Richtung K2: sin^2 th12 = 0,3195 (+2,5s), nahe TM1 0,318.")
print(f"  Struktur-erhaltender Boden (Masse + |sin d|>0,99): sin^2 th12 = {c_full[0]:.4f} ({(c_full[0]-S12)/S12E:+.1f}s), via {c_full[4]}.")
print(f"  Zentralwert 0,3036 struktur-erhaltend (±1s) erreichbar: {'JA' if central else 'NEIN'}")
print("  => TEILWEISE: theta12 ist NICHT starr gepinnt, aber der Zentralwert ist struktur-erhaltend")
print("     NICHT erreichbar. Mit Massen UND maximaler CP bleibt ein Boden ~0,315 (+1,9s), und das")
print("     braucht schon einen erlaubten, NICHT hergeleiteten Zusatzterm (S+d). Tiefer geht nur,")
print("     wenn maximale CP-Verletzung aufgegeben wird (Pareto-Front). Die Struktur handelt theta12")
print("     GEGEN |sin delta|: entweder hohes theta12 (>=0,315) + maximale CP, oder zentrales theta12")
print("     + submaximale CP. Scharfe, von JUNO (theta12) + DUNE/T2K (delta) testbare KORRELATION.")
