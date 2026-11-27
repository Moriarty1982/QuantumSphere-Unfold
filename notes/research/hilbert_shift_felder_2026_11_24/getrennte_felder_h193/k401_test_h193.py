"""k401 (Test H193): Getrennte Felder je HS-Stufe gegen die sechs Quarkmassen.
Vorab: notes/research/predictions/Vorab_Notiz_H193_Getrennte_Felder_je_HS_Stufe.md (Commit 74ecdb6).
Aufruf: python k401_test_h193.py > k401_out.txt

Modell: m = Einheit * S(Stufe) * Sektorfaktor. Drei Generationen eines Sektors auf drei aufsteigenden Stufen.
Lesart (i) stufenfest: S folgt einer festen Regel aus einer stufeneigenen Groesse, kein Fit je Feld,
hoechstens eine Gesamteinheit je Sektor. Pruefstein sind die zwei dimensionslosen Generationsverhaeltnisse
je Sektor; die Einheit faellt heraus.
"""
import numpy as np
from itertools import product
rng = np.random.default_rng(401)

# --- Daten (wie H187/H190) ---------------------------------------------------
# Up / Down, jeweils PDG-Standardskalen und laufende M_Z-Werte (Yukawa).
DATA = {
    "up PDG":   (np.array([2.16e-3, 1.2730, 172.4]),  np.array([0.04e-3, 0.0028, 0.7])),
    "down PDG": (np.array([4.70e-3, 93.5e-3, 4.183]), np.array([0.09e-3, 0.5e-3, 0.007])),
    "up MZ":    (np.array([7.04e-6, 3.56e-3, 0.967]), np.array([0.15e-6, 0.06e-3, 0.004])),
    "down MZ":  (np.array([1.54e-5, 3.06e-4, 1.630e-2]), np.array([0.02e-5, 0.04e-4, 0.009e-2])),
}

def ratios(m):
    return np.array([m[1] / m[0], m[2] / m[1]])

print("=== Beobachtete Generationsverhaeltnisse (einheitsfrei) ===")
for name, (m, s) in DATA.items():
    r = ratios(m)
    print(f"  {name:9s}: r1 (g2/g1) = {r[0]:9.2f}   r2 (g3/g2) = {r[1]:8.2f}")

# --- Stufeneigene Groessen (HS(1..4) = C, H, O, S) ---------------------------
# k = Stufenindex 1..4
def casimir(k):  # a_k = sqrt(k(k+2)/3), r67
    return np.sqrt(k * (k + 2) / 3.0)
GAMMA_L = 1.8646997646  # r67
def weight(k):   # 2^(1 - gamma_L a_k)
    return 2.0 ** (1.0 - GAMMA_L * casimir(k))
def dim(k):      # Dimension 2^k
    return 2.0 ** k

KS = [1, 2, 3, 4]
print("\n=== Stufeneigene Groessen je Stufe (C,H,O,S = k 1..4) ===")
print("  k   dim    casimir a_k   gewicht w_k")
for k in KS:
    print(f"  {k}  {dim(k):5.0f}   {casimir(k):10.6f}   {weight(k):10.6f}")

# --- Vorab festgelegte Skalenregeln S(k) -------------------------------------
# S in {d, d^2, 2^d, exp(a), a, w, k, k!} und Kehrwerte.
import math
def fact(k): return float(math.factorial(int(round(k))))
RULES = {
    "d":        lambda k: dim(k),
    "d^2":      lambda k: dim(k) ** 2,
    "2^d":      lambda k: 2.0 ** dim(k),
    "exp(a)":   lambda k: math.exp(casimir(k)),
    "a":        lambda k: casimir(k),
    "w":        lambda k: weight(k),
    "k":        lambda k: float(k),
    "k!":       lambda k: fact(k),
}
# Kehrwerte dazu
ALL_RULES = {}
for nm, f in RULES.items():
    ALL_RULES[nm] = f
    ALL_RULES["1/" + nm] = (lambda f: (lambda k: 1.0 / f(k)))(f)

# --- Zuordnungen: drei aufeinanderfolgende Stufen, beide Reihenfolgen --------
STARTS = [1, 2]  # Startstufe C oder H (O-Start waere 3,4,5 -> keine 5. HS-Stufe mit a_k hier; S=4 ist Ende)
# drei aufeinanderfolgende: (s, s+1, s+2) fuer s in {1,2}; S-Turm hat 4 Stufen -> s in {1,2}
ASSIGN = []
for s in STARTS:
    ks = [s, s + 1, s + 2]
    ASSIGN.append(("auf", tuple(ks)))       # Generation 1->s, 2->s+1, 3->s+2
    ASSIGN.append(("ab",  tuple(ks[::-1])))  # Generation 1->s+2, ...

def model_ratios(rule, ks):
    """Dimensionslose Verhaeltnisse der Regel ueber die zugeordneten Stufen."""
    S = np.array([ALL_RULES[rule](k) for k in ks], dtype=float)
    if np.any(~np.isfinite(S)) or np.any(S <= 0):
        return None
    return np.array([S[1] / S[0], S[2] / S[1]])

def ratio_mismatch(rmod, robs):
    """log-Abstand der zwei Verhaeltnisse (Faktor), max ueber die zwei Schritte."""
    return np.max(np.abs(np.log(rmod / robs)))

# --- H193b: stufenfest, kein Fit je Feld. Pruefung je Sektor -----------------
# Einheit je Sektor ist frei -> wir pruefen die zwei dimensionslosen Verhaeltnisse.
# Zusaetzlich: bester sigma-Abstand mit genau einer Gesamteinheit (1 Fit je Sektor).
def best_unit_sigma(Svals, m, s):
    """m_i = U * S_i ; U = argmin chi2 ; gib max sigma-Abweichung der 3 Massen."""
    Svals = np.asarray(Svals, float)
    # gewichteter LS fuer U
    w = 1.0 / s ** 2
    U = np.sum(w * m * Svals) / np.sum(w * Svals ** 2)
    pred = U * Svals
    return np.max(np.abs((pred - m) / s)), U

print("\n=== H193b: stufenfeste Regeln, Verhaeltnis-Abstand (Faktor) je Sektor ===")
SECT = {"up": ("up PDG", "up MZ"), "down": ("down PDG", "down MZ")}
# Fuer jeden Sektor: ueber alle Regeln+Zuordnungen den besten Verhaeltnis-Fit (Faktor) finden.
summary = {}
for sect, (nmP, nmZ) in SECT.items():
    mP, sP = DATA[nmP]; robsP = ratios(mP)
    best = None
    for rule in ALL_RULES:
        for tag, ks in ASSIGN:
            rmod = model_ratios(rule, ks)
            if rmod is None:
                continue
            mm = ratio_mismatch(rmod, robsP)
            if best is None or mm < best[0]:
                best = (mm, rule, tag, ks, rmod)
    summary[sect] = best
    mm, rule, tag, ks, rmod = best
    print(f"  {sect:4s} PDG: beste Regel '{rule}' ({tag}, Stufen {ks}): "
          f"Modell-Verhaeltnisse [{rmod[0]:.3g}, {rmod[1]:.3g}] vs beob. [{robsP[0]:.3g}, {robsP[1]:.3g}] "
          f"-> max Faktor {math.exp(mm):.2f}x")

# --- Gemeinsame Regel fuer BEIDE Sektoren (eine Regel, je Sektor nur Einheit) ---
print("\n=== H193b: eine Regel fuer beide Sektoren, sigma-Abstand (1 Einheit je Sektor) ===")
best_joint = None
for rule in ALL_RULES:
    for tag, ks in ASSIGN:
        Svals = np.array([ALL_RULES[rule](k) for k in ks], float)
        if np.any(~np.isfinite(Svals)) or np.any(Svals <= 0):
            continue
        # gleiche Stufenzuordnung fuer up und down (die Stufe legt die Generation fest)
        sigU, _ = best_unit_sigma(Svals, *DATA["up PDG"])
        sigD, _ = best_unit_sigma(Svals, *DATA["down PDG"])
        worst = max(sigU, sigD)
        if best_joint is None or worst < best_joint[0]:
            best_joint = (worst, rule, tag, ks, sigU, sigD)
worst, rule, tag, ks, sigU, sigD = best_joint
print(f"  beste gemeinsame Regel '{rule}' ({tag}, Stufen {ks}): up {sigU:.1f} sigma, down {sigD:.1f} sigma "
      f"-> schlechtester {worst:.1f} sigma")
print(f"  Kriterium bestaetigt (beide < 3 sigma): {'JA' if worst < 3 else 'NEIN'}")

# --- H193c: Parameterzaehlung (freie Skala je Stufe) -------------------------
print("\n=== H193c: freie Skala je Stufe je Sektor (Lesart ii) ===")
for sect, (nmP, _) in SECT.items():
    m, s = DATA[nmP]
    # 3 freie Skalen treffen 3 Massen exakt (U_i = m_i): 0 Residuum
    print(f"  {sect:4s}: 3 Massen, 3 freie Skalen -> exakter Fit, Residuum 0, keine Aussage. "
          f"(Parameter = Daten)")

# --- Kontrolle: wie leicht trifft 'teilweise' zufaellig? ---------------------
print("\n=== Kontrolle: 2000 erfundene Massensaetze ===")
# Erfinde Hierarchien gleicher Groessenordnung: 3 Massen mit zufaelligen Verhaeltnissen 1..1000
def rand_set():
    base = 10 ** rng.uniform(-3, 0)
    r1 = 10 ** rng.uniform(0, 3); r2 = 10 ** rng.uniform(0, 3)
    m = np.array([base, base * r1, base * r1 * r2])
    s = 0.01 * m
    return m, s
hits_part = 0; hits_conf = 0
rules_list = list(ALL_RULES)
for _ in range(2000):
    mU, sU = rand_set(); mD, sD = rand_set()
    bj = None
    for rule in rules_list:
        for tag, ks in ASSIGN:
            Sv = np.array([ALL_RULES[rule](k) for k in ks], float)
            if np.any(~np.isfinite(Sv)) or np.any(Sv <= 0):
                continue
            sig = max(best_unit_sigma(Sv, mU, sU)[0], best_unit_sigma(Sv, mD, sD)[0])
            if bj is None or sig < bj:
                bj = sig
    # 'teilweise': ein Sektor < 3 sigma; 'bestaetigt': beide < 3 sigma
    # (hier als worst<3 fuer bestaetigt; ein-Sektor separat)
    if bj is not None and bj < 3:
        hits_conf += 1
    # ein Sektor allein:
    one = None
    for rule in rules_list:
        for tag, ks in ASSIGN:
            Sv = np.array([ALL_RULES[rule](k) for k in ks], float)
            if np.any(~np.isfinite(Sv)) or np.any(Sv <= 0):
                continue
            s1 = min(best_unit_sigma(Sv, mU, sU)[0], best_unit_sigma(Sv, mD, sD)[0])
            if one is None or s1 < one:
                one = s1
    if one is not None and one < 3:
        hits_part += 1
print(f"  ein Sektor < 3 sigma (frei gefittete Einheit): {hits_part/2000*100:.1f} %")
print(f"  beide Sektoren < 3 sigma (gemeinsame Regel):    {hits_conf/2000*100:.1f} %")

# --- Echte Daten durch dasselbe Raster (Vergleich) ---------------------------
print("\n=== Echte Daten: ein Sektor < 3 sigma? ===")
one_real = {}
for sect, (nmP, _) in SECT.items():
    m, s = DATA[nmP]
    best = min(best_unit_sigma(np.array([ALL_RULES[r](k) for k in ks], float), m, s)[0]
               for r in rules_list for _, ks in ASSIGN
               if np.all(np.isfinite([ALL_RULES[r](k) for k in ks])) and np.all(np.array([ALL_RULES[r](k) for k in ks]) > 0))
    one_real[sect] = best
    print(f"  {sect:4s} PDG: bester sigma-Abstand einer stufenfesten Regel = {best:.1f} sigma")

print("\n=== Urteil ===")
conf = best_joint[0] < 3
part = (min(one_real.values()) < 3)
if conf:
    print("  bestaetigt: eine stufenfeste Regel traegt beide Sektoren < 3 sigma.")
elif part:
    print("  teilweise: ein Sektor < 3 sigma stufenfest, der andere nicht.")
else:
    print("  widerlegt: keine stufenfeste Regel bringt auch nur einen Sektor < 3 sigma.")
print(f"  (bester gemeinsamer sigma = {best_joint[0]:.1f}; bester Einzelsektor-sigma = {min(one_real.values()):.1f})")
