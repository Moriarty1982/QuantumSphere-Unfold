"""k358 (Erkundung, Nachrechnung, kein Test): alle von beta_sym bzw. gamma_L abhaengigen Zahlen bei drei Werten.

  alt4  = 0.5493        (vierstellig, in vielen aelteren Skripten)
  alt7  = 0.5493482     (im Bestand gefuehrt, aus gerundeten Eingaben)
  exakt = Wurzel der Zaehlgleichung (Postulat r67.P), 0.5494056410

Je Groesse: Werte, Differenz exakt - alt7, relative Aenderung, logarithmische Empfindlichkeit d ln X / d ln beta
(zentrale Differenz bei exakt), und wo es eine Messung gibt der Abstand in sigma bei alt7 und exakt.
Messwerte wie im Bestand (k218, k33, k224, op4_status_audit, Physik-Artikel Tab. open-tests); keiner davon ist neu.
Aufruf: python k358_empfindlichkeit.py
"""
import importlib.util
import pathlib

import mpmath as mp

mp.mp.dps = 30
HERE = pathlib.Path(__file__).resolve().parent
REPO = HERE.parents[2]

c = lambda k: mp.sqrt(mp.mpf(k) * (k + 2) / 3)
GL = mp.findroot(lambda g: mp.nsum(lambda k: 2 ** (1 - g * c(k)), [1, mp.inf]) - 1, 1.9)
B_EX = mp.sqrt((GL - 1) / (GL + 1))
B_7, B_4 = mp.mpf("0.5493482"), mp.mpf("0.5493")
GAMMA_T = mp.log(2) / (mp.pi * mp.sqrt(3))
GAMMA_M = GL * GAMMA_T
deg = lambda x: x * 180 / mp.pi
gl = lambda b: (1 + b * b) / (1 - b * b)
MZ, SMZ = mp.mpf("91.1880"), mp.mpf("0.0020")

# (Name, Funktion von beta, Fundstelle)
Q = [
    ("beta_sym", lambda b: b, "OP2 Versatz, r66"),
    ("beta^2 = Omega_M (H96) = |U_e2|^2", lambda b: b * b, "H96, H9, H112, OP4, OP5"),
    ("1 - beta^2 = Omega_Lambda", lambda b: 1 - b * b, "r05"),
    ("Omega_Lambda/Omega_M", lambda b: (1 - b * b) / (b * b), "r05"),
    ("gamma_L = cot theta_W", gl, "H15, r61"),
    ("1/gamma_L", lambda b: 1 / gl(b), "r66"),
    ("gamma_L^2", lambda b: gl(b) ** 2, "Frame-Potenzen"),
    ("gamma_L^3", lambda b: gl(b) ** 3, "Frame-Potenzen"),
    ("gamma_L^5 (Vakuumquotient)", lambda b: gl(b) ** 5, "H159, r69.3"),
    ("gamma_L^(-3/2) (Photon-Planck)", lambda b: gl(b) ** mp.mpf("-1.5"), "r63 alt"),
    ("epsilon = eta = artanh beta (Maske)", mp.atanh, "H45, H46, H134"),
    ("2 eta", lambda b: 2 * mp.atanh(b), "r63"),
    ("tanh 2 eta", lambda b: mp.tanh(2 * mp.atanh(b)), "r63"),
    ("coth 2 eta (Spiegel-Boden)", lambda b: 1 / mp.tanh(2 * mp.atanh(b)), "r63.4"),
    ("1/beta (Tachyon)", lambda b: 1 / b, "r24.2"),
    ("theta_H [Grad]", lambda b: deg(2 * mp.asin(b)), "r61, r66"),
    ("pi - theta_H [Grad]", lambda b: 180 - deg(2 * mp.asin(b)), "H164"),
    ("2 alpha = 2 arctan beta [Grad]", lambda b: 2 * deg(mp.atan(b)), "r66"),
    ("Besetzung 1/(1+beta^2)", lambda b: 1 / (1 + b * b), "r66, H73"),
    ("Besetzung beta^2/(1+beta^2)", lambda b: b * b / (1 + b * b), "r66, H73"),
    ("(1+beta)/2", lambda b: (1 + b) / 2, "r66"),
    ("w = -beta^2/3 (H73)", lambda b: -b * b / 3, "H73"),
    ("tau*/delta = beta/(1+beta) (H81)", lambda b: b / (1 + b), "H81"),
    ("HC-Winkel arctan(beta^2) [Grad]", lambda b: deg(mp.atan(b * b)), "k297, k298"),
    ("K = (1+beta^4)/3", lambda b: (1 + b ** 4) / 3, "r63, H155"),
    ("kappa = (gamma_L+1/gamma_L)/2", lambda b: (gl(b) + 1 / gl(b)) / 2, "r64.4"),
    ("2^(1-gamma_L)", lambda b: 2 ** (1 - gl(b)), "H165"),
    ("Hopf-Luecke beta [%]", lambda b: (1 / mp.sqrt(3) / b - 1) * 100, "r61"),
    ("Hopf-Luecke gamma_L [%]", lambda b: (2 / gl(b) - 1) * 100, "r61"),
    ("sin^2 theta_W = 1/(1+gamma_L^2)", lambda b: 1 / (1 + gl(b) ** 2), "H15"),
    ("m_W = m_Z gamma_L/sqrt(1+gamma_L^2) [GeV]", lambda b: MZ * gl(b) / mp.sqrt(1 + gl(b) ** 2), "H15"),
    ("sin^2 theta_12 = beta^2/(1-s13), s13=0.02215", lambda b: b * b / (1 - mp.mpf("0.02215")), "H9 (NuFIT 6.0)"),
    ("sin^2 theta_12 = beta^2/(1-s13), s13=0.02248", lambda b: b * b / (1 - mp.mpf("0.02248")), "H9 (NuFIT 6.1)"),
]


def sens(f, b):
    h = mp.mpf("1e-8")
    lo, hi = f(b * (1 - h)), f(b * (1 + h))
    return (hi - lo) / (2 * h * f(b))


print("== 0. Eingaben ==")
print("gamma_L (Wurzel) =", mp.nstr(GL, 14), "; beta exakt =", mp.nstr(B_EX, 14), "; gamma_T =", mp.nstr(GAMMA_T, 12), "; gamma_M =", mp.nstr(GAMMA_M, 14))
print("beta alt7 = 0.5493482 (gamma_L =", mp.nstr(gl(B_7), 10), "); beta alt4 = 0.5493 (gamma_L =", mp.nstr(gl(B_4), 10), ")")
print("rel. Aenderung beta: exakt/alt7 - 1 =", mp.nstr(B_EX / B_7 - 1, 4), "; exakt/alt4 - 1 =", mp.nstr(B_EX / B_4 - 1, 4))

print("\n== 1. Abgeleitete Zahlen ==")
print(f"{'Groesse':46s} {'alt4 0.5493':>14s} {'alt7 0.5493482':>15s} {'exakt':>14s} {'exakt-alt7':>12s} {'rel.':>10s} {'dlnX/dlnb':>10s}  Fundstelle")
rows = []
for n, f, src in Q:
    a4, a7, ex = f(B_4), f(B_7), f(B_EX)
    s = sens(f, B_EX)
    rows.append((n, abs(s)))
    print(f"{n:46s} {mp.nstr(a4, 9):>14s} {mp.nstr(a7, 9):>15s} {mp.nstr(ex, 9):>14s} {mp.nstr(ex - a7, 3):>12s} {mp.nstr(ex / a7 - 1, 3):>10s} {mp.nstr(s, 4):>10s}  {src}")
print("\nNach Empfindlichkeit geordnet (|d ln X / d ln beta|, die sechs groessten):")
for n, s in sorted(rows, key=lambda r: -r[1])[:6]:
    print(f"  {mp.nstr(s, 4):>8s}  {n}")

print("\n== 2. Abstand zur Messung (Messwerte aus dem Bestand; keiner zaehlt als neue Pruefung) ==")
M = [
    ("H96 Omega_M = beta^2", lambda b: b * b, 0, [("DESI DR2 BAO", "0.2975", "0.0086"), ("Planck 2018", "0.315", "0.007")]),
    ("H15 m_W [GeV]", lambda b: MZ * gl(b) / mp.sqrt(1 + gl(b) ** 2), None, [("PDG 2024", "80.3692", "0.0133"), ("PDG 2026", "80.3625", "0.0077")]),
    ("H9 sin^2 theta_12 (s13 = 0.02215)", lambda b: b * b / (1 - mp.mpf("0.02215")), 0, [("JUNO 2026", "0.3036", "0.0064"), ("NuFIT 6.1", "0.3088", "0.0067")]),
    ("H9 sin^2 theta_12 (s13 = 0.02248)", lambda b: b * b / (1 - mp.mpf("0.02248")), 0, [("JUNO 2026", "0.3036", "0.0064"), ("NuFIT 6.1", "0.3088", "0.0067")]),
]
print(f"{'Vorhersage':36s} {'Messung':14s} {'Wert':>20s} {'alt7':>10s} {'exakt':>10s} {'z alt7':>8s} {'z exakt':>8s} {'Delta z':>8s}")
for n, f, sp, data in M:
    for dn, v, s in data:
        v, s = mp.mpf(v), mp.mpf(s)
        if sp is None:  # Unsicherheit der Vorhersage aus m_Z
            sp7 = abs(f(B_7)) * SMZ / MZ
            s_tot = mp.sqrt(s * s + sp7 * sp7)
        else:
            s_tot = s
        z7, zx = (f(B_7) - v) / s_tot, (f(B_EX) - v) / s_tot
        print(f"{n:36s} {dn:14s} {mp.nstr(v, 7) + ' +- ' + mp.nstr(s, 2):>20s} {mp.nstr(f(B_7), 7):>10s} {mp.nstr(f(B_EX), 7):>10s} {mp.nstr(z7, 3):>8s} {mp.nstr(zx, 3):>8s} {mp.nstr(zx - z7, 2):>8s}")

print("\n== 3. Schwellen und Fenster ==")
mW = lambda b: MZ * gl(b) / mp.sqrt(1 + gl(b) ** 2)
for lab, b in (("alt4", B_4), ("alt7", B_7), ("exakt", B_EX)):
    print(f"{lab:6s} Leptonfenster [0.545; 0.570]: {0.545 <= b <= 0.570};  m_W in 2 sigma (PDG 2024, k218): {abs(mW(b) - mp.mpf('80.3692')) <= 2 * mp.mpf('0.0133')};"
          f"  Omega_M in 2 sigma (DESI DR2): {abs(b * b - mp.mpf('0.2975')) <= 2 * mp.mpf('0.0086')};"
          f"  eta im Trefferfenster [0.611; 0.647] (r61): {0.611 <= mp.atanh(b) <= 0.647}, Abstand zum unteren Rand {mp.nstr(mp.atanh(b) - mp.mpf('0.611'), 4)}")
print("Wie weit duerfte beta wandern, bis ein Urteil kippt (Abstand in Einheiten der Aenderung exakt - alt7 = %s):" % mp.nstr(B_EX - B_7, 4))
d = B_EX - B_7
edges = [("Leptonfenster unten 0.545", mp.mpf("0.545")), ("Leptonfenster oben 0.570", mp.mpf("0.570")),
         ("Omega_M 2 sigma oben (DESI): beta = sqrt(0.3147)", mp.sqrt(mp.mpf("0.2975") + 2 * mp.mpf("0.0086"))),
         ("m_W 2 sigma unten (PDG 2026, 80.3471)", mp.findroot(lambda b: mW(b) - (mp.mpf("80.3625") - 2 * mp.mpf("0.0077")), 0.549)),
         ("m_W 2 sigma oben (PDG 2026, 80.3779)", mp.findroot(lambda b: mW(b) - (mp.mpf("80.3625") + 2 * mp.mpf("0.0077")), 0.549)),
         ("Maske: eta = 0.611 (unterer Rand r61)", mp.tanh(mp.mpf("0.611"))), ("Maske: eta = 0.647 (oberer Rand r61)", mp.tanh(mp.mpf("0.647"))),
         ("H9 JUNO 2 sigma oben (0.3164, s13 = 0.02248)", mp.sqrt(mp.mpf("0.3164") * (1 - mp.mpf("0.02248"))))]
for n, e in edges:
    print(f"  {n:48s} beta = {mp.nstr(e, 8)}; Abstand von exakt {mp.nstr(e - B_EX, 3):>10s} = {mp.nstr((e - B_EX) / d, 4):>8s} Schritte")

print("\n== 4. H102: m_tau aus Phi_e = pi/4 - gamma_M/2 (Funktionen aus predictions/k224_test_h102.py) ==")
spec = importlib.util.spec_from_file_location("k224", REPO / "notes/research/predictions/k224_test_h102.py")
k224 = importlib.util.module_from_spec(spec)
spec.loader.exec_module(k224)
import numpy as np

mk = k224.mtau_koide(k224.ME, k224.MMU)
print(f"exaktes Koide: m_tau = {mk:.4f} MeV")
res = {}
for lab, g in (("gamma_M = 0.2375 (gerundet)", 0.2375), ("gamma_M = 0.237533 (Wortlaut H102)", 0.237533), ("gamma_M exakt = %s" % mp.nstr(GAMMA_M, 12), float(GAMMA_M)),
               ("gamma_M aus alt7: gamma_L(0.5493482)*gamma_T", float(gl(B_7) * GAMMA_T))):
    mt, r2 = k224.mtau_pred(k224.ME, k224.MMU, (np.pi / 4 - g / 2) / 3)
    res[lab] = mt
    print(f"  {lab:46s} m_tau = {mt:.4f} MeV; z gegen PDG 1776.93 +- 0.09: {(mt - 1776.93) / 0.09:+.3f}; Abstand zu Koide {mt - mk:+.4f} MeV")
g0 = float(GAMMA_M)
h = 1e-6
dm = (k224.mtau_pred(k224.ME, k224.MMU, (np.pi / 4 - (g0 + h) / 2) / 3)[0] - k224.mtau_pred(k224.ME, k224.MMU, (np.pi / 4 - (g0 - h) / 2) / 3)[0]) / (2 * h)
print(f"  d m_tau / d gamma_M = {dm:.3f} MeV; d ln m_tau / d ln gamma_M = {dm * g0 / res['gamma_M exakt = %s' % mp.nstr(GAMMA_M, 12)]:.5f}")
print(f"  gamma_M, das m_tau = 1776.93 traefe (linear): {g0 + (1776.93 - res['gamma_M exakt = %s' % mp.nstr(GAMMA_M, 12)]) / dm:.6f}; fuer exaktes Koide: {g0 + (mk - res['gamma_M exakt = %s' % mp.nstr(GAMMA_M, 12)]) / dm:.6f}")
