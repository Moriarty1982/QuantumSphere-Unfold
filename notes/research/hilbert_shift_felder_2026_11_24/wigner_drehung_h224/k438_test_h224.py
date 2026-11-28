"""k438 (Test H224): Ist der gemeinsame Drehwinkel phi eine Wigner-Drehung aus zwei Frame-Boosts?
Vorab-Notiz Vorab_H224_Wigner_Drehung.md (vor der Rechnung committet). Kandidatenliste dort vollstaendig festgelegt (48).
Aufruf aus diesem Ordner: python3 k438_test_h224.py > k438_out.txt
"""
import itertools
import numpy as np
from scipy.linalg import polar

BETA = 0.5494056410; GL = 1.8646997646
EPS = np.arctanh(BETA); E2 = np.arccosh(GL)
X_J, S_J = np.pi / 12 - 0.2222220470731, 7.8e-7
X_NU, S_NU = 0.043359, 0.002128


def omega_formula(a, b, th):
    return 2 * np.arctan(np.sin(th) / (1 / np.tanh(a / 2) / np.tanh(b / 2) + np.cos(th)))


def boost(rap, th):
    n = np.array([np.cos(th), np.sin(th), 0.0]); g, bg = np.cosh(rap), np.sinh(rap)
    L = np.eye(4); L[0, 0] = g; L[0, 1:] = L[1:, 0] = bg * n
    L[1:, 1:] += (g - 1) * np.outer(n, n)
    return L


def omega_matrix(a, b, th):
    """Komposition B(b, th) B(a, 0) = B' R; Drehwinkel aus R (Polarzerlegung mit Minkowski-Metrik ueber Boost-Abspaltung)."""
    L = boost(b, th) @ boost(a, 0.0)
    g = L[0, 0]; v = L[1:, 0] / g                      # Geschwindigkeit des Gesamtboosts
    rap = np.arctanh(np.linalg.norm(v)); n = v / np.linalg.norm(v)
    Bp = boost(rap, np.arctan2(n[1], n[0]))
    R = np.linalg.inv(Bp) @ L
    return abs(np.arctan2(R[2, 1], R[1, 1]))


print(f"eps = artanh beta_sym = {EPS:.10f};  2 eps = {2*EPS:.10f};  arcosh gamma_L = {E2:.10f}  (Kontrolle 2eps - arcosh gamma_L = {2*EPS-E2:+.1e})")
print(f"Ziel x (unter J) = {X_J:.10f} +- {S_J:.1e};  x_nu = {X_NU} +- {S_NU}")
pairs = {"(eps, eps)": (EPS, EPS), "(2eps, 2eps)": (2 * EPS, 2 * EPS), "(eps, 2eps)": (EPS, 2 * EPS)}
thetas = {"pi/2": np.pi / 2, "pi/4": np.pi / 4, "2pi/3": 2 * np.pi / 3, "pi/3": np.pi / 3}
rows = []; maxdiff = 0.0
print(f"\n{'Paar':14s} {'theta':6s} {'omega':>12s}  " + "  ".join(f"{'omega/'+str(n):>12s}" for n in (1, 2, 3, 6)))
for (pn, (a, b)), (tn, th) in itertools.product(pairs.items(), thetas.items()):
    w = omega_formula(a, b, th); wm = omega_matrix(a, b, th); maxdiff = max(maxdiff, abs(w - wm))
    vals = [w / n for n in (1, 2, 3, 6)]
    print(f"{pn:14s} {tn:6s} {w:12.8f}  " + "  ".join(f"{v:12.8f}" for v in vals))
    for n, v in zip((1, 2, 3, 6), vals):
        rows.append((pn, tn, n, v))
print(f"\nFormel gegen Matrix-Komposition: groesste Abweichung {maxdiff:.1e}")

strict = [r for r in rows if abs(r[3] - X_J) < 3 * S_J]
loose = [r for r in rows if abs(r[3] - X_J) / X_J < 0.01]
nu2 = [r for r in rows if abs(r[3] - X_NU) < 2 * S_NU]
vals = np.array([r[3] for r in rows]); lo, hi = vals.min(), vals.max()
exp_loose = len(rows) * (2 * 0.01 * X_J) / (hi - lo)
best = min(rows, key=lambda r: abs(r[3] - X_J))
print(f"naechster Kandidat: {best[0]}, theta = {best[1]}, n = {best[2]}: {best[3]:.8f} (relativ {(best[3]-X_J)/X_J:+.3%}, {(best[3]-X_J)/S_J:+.0f} sigma unter J)")
print(f"strenge Treffer (3 sigma unter J): {len(strict)}  {strict}")
print(f"lockere Treffer (< 1 %): {len(loose)}  {[(r[0], r[1], r[2], round(r[3], 6)) for r in loose]};  Zufallserwartung {exp_loose:.3f} (Bereich {lo:.4f} bis {hi:.4f})")
print(f"innerhalb 2 sigma von x_nu (nur Bericht): {len(nu2)}")
from scipy.stats import poisson
pval = poisson.sf(len(loose) - 1, exp_loose) if loose else 1.0
print(f"Poisson-Wahrscheinlichkeit fuer >= {len(loose)} lockere Treffer bei Erwartung {exp_loose:.3f}: {pval:.3f}")
v = "TRAEGT" if strict else ("TRAEGT TEILWEISE (nur locker, Wortlaut der Vorab: ueber der Zufallserwartung)" if len(loose) > exp_loose else "WIDERLEGT")
print(f"\nUrteil nach Vorab: {v}")
