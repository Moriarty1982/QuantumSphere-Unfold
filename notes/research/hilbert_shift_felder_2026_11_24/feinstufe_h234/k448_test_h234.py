"""k448 (Test H234): Tragen alle Feinwerte eine gemeinsame Feinstufe eps?  F_i = c * eps^n.
Vorab-Notiz Vorab_H234_Gemeinsame_Feinstufe.md (vor der Rechnung committet).
Aufruf aus diesem Ordner: python3 k448_test_h234.py > k448_out.txt
"""
import math
import numpy as np

PHI, SPHI = math.pi / 12 - 0.2222220470731, 7.8e-7
F = {"F2 beta-1/2": (0.549405640974529 - 0.5, 1.8e-4), "F3 D/B-1": (0.0085, 0.001), "F4 x_nu-x": (0.04336 - PHI, 0.00213)}
C = {"1": 1, "2": 2, "3": 3, "4": 4, "1/2": .5, "1/3": 1 / 3, "1/4": .25, "2/3": 2 / 3, "3/2": 1.5, "sqrt2": math.sqrt(2),
     "1/sqrt2": 1 / math.sqrt(2), "sqrt3": math.sqrt(3), "1/sqrt3": 1 / math.sqrt(3), "pi": math.pi, "1/pi": 1 / math.pi}
NS = (1, 2, 3)
CV = np.array(list(C.values()))


def best(val, sig, eps):
    out = []
    for cn, c in C.items():
        for n in NS:
            p = c * eps ** n
            out.append((abs(val - p) / sig, cn, n, p))
    return min(out)


print("=" * 92)
print("H234 (k448)  gemeinsame Feinstufe: F = c * eps^n, c aus 15 Faktoren, n = 1..3")
print("=" * 92)
print(f"F1 phi = {PHI:.10f}")
for k, (v, s) in F.items():
    print(f"{k}: {v:.7f} +- {s:.1e} ({s/v*100:.2f} %)")

print("\nLesart A  eps = phi")
hitsA = {}
for k, (v, s) in F.items():
    z, cn, n, p = best(v, s, PHI)
    hitsA[k] = z <= 2
    print(f"  {k}: bestes c*phi^n = {cn}*phi^{n} = {p:.7f}, Abstand {z:.2f} sigma -> Treffer {z <= 2}")

print("\nLesart B  eps frei, phi = c1*eps^n1 (eps aus phi bestimmt), dann F2..F4")
rowsB = []
for c1n, c1 in C.items():
    for n1 in NS:
        eps = (PHI / c1) ** (1 / n1)
        if not (1e-3 < eps < 0.5):
            continue
        res = {k: best(v, s, eps) for k, (v, s) in F.items()}
        nsharp = sum(res[k][0] <= 2 for k in ("F2 beta-1/2", "F3 D/B-1"))
        nall = sum(r[0] <= 2 for r in res.values())
        rowsB.append((nsharp, nall, c1n, n1, eps, res))
rowsB.sort(key=lambda r: (-r[0], -r[1]))
for r in rowsB[:6]:
    print(f"  phi = {r[2]}*eps^{r[3]}, eps = {r[4]:.6f}: scharfe Treffer {r[0]}, alle {r[1]};  " +
          "; ".join(f"{k.split()[0]} {v[1]}*eps^{v[2]} ({v[0]:.1f}s)" for k, v in r[5].items()))
bestB = rowsB[0]

# ---- Monte Carlo ----
print("\nZufallsabschaetzung (1e5 Durchlaeufe, log-gleichverteilt in [1e-3, 1e-1], gleiche relative Fehler)")
rng = np.random.default_rng(234)
N = 100000
rel = {k: s / v for k, (v, s) in F.items()}
keys = list(F)
vals = 10 ** rng.uniform(-3, -1, size=(N, 3))


def hits_for_eps(eps, vals):
    # fuer jede Zufallsgroesse: gibt es c, n mit |v - c eps^n| <= 2 sigma, sigma = rel*v
    grid = np.array([c * eps ** n for c in CV for n in NS])  # (45,)
    h = np.zeros(vals.shape, bool)
    for j, k in enumerate(keys):
        v = vals[:, j:j + 1]
        h[:, j] = (np.abs(v - grid[None, :]) <= 2 * rel[k] * v).any(axis=1)
    return h


hA = hits_for_eps(PHI, vals)
obsA_sharp = hitsA["F2 beta-1/2"] + hitsA["F3 D/B-1"]
obsA_all = sum(hitsA.values())
pA_sharp = np.mean(hA[:, 0].astype(int) + hA[:, 1] >= obsA_sharp) if obsA_sharp else 1.0
pA_all = np.mean(hA.sum(axis=1) >= obsA_all) if obsA_all else 1.0
print(f"  A: Trefferrate je Groesse {hA.mean(axis=0).round(4)}; beobachtet scharf {obsA_sharp}, alle {obsA_all};"
      f" p(scharf) = {pA_sharp:.4f}, p(alle) = {pA_all:.4f}")
# B: ueber alle eps-Wahlen das Maximum
epsB = [(PHI / c1) ** (1 / n1) for c1 in CV for n1 in NS if 1e-3 < (PHI / c1) ** (1 / n1) < 0.5]
sub = vals[:20000]
best_sharp = np.zeros(len(sub), int)
best_all = np.zeros(len(sub), int)
for e in epsB:
    h = hits_for_eps(e, sub)
    best_sharp = np.maximum(best_sharp, h[:, 0].astype(int) + h[:, 1])
    best_all = np.maximum(best_all, h.sum(axis=1))
pB_sharp = np.mean(best_sharp >= bestB[0]) if bestB[0] else 1.0
pB_all = np.mean(best_all >= bestB[1]) if bestB[1] else 1.0
print(f"  B ({len(epsB)} eps-Wahlen, 2e4 Durchlaeufe): beobachtet scharf {bestB[0]}, alle {bestB[1]}; p(scharf) = {pB_sharp:.4f}, p(alle) = {pB_all:.4f}")

print("\nNachtraeglich (nicht gewertet): (beta - 1/2)/phi =", f"{F['F2 beta-1/2'][0]/PHI:.6f}",
      f"(5/4 = 1,25; Abstand {(F['F2 beta-1/2'][0] - 1.25*PHI)/F['F2 beta-1/2'][1]:+.2f} sigma_beta)")
# Zufall fuer 'irgendein einfacher Bruch p/q, q<=4, liegt innerhalb 2 sigma des Verhaeltnisses'
r = F["F2 beta-1/2"][0] / PHI
fr = sorted({p / q for q in range(1, 5) for p in range(1, 4 * q + 1)})
sr = 2 * F["F2 beta-1/2"][1] / PHI
cover = sum(2 * sr for _ in fr) / (4 - 0.25)
print(f"  Brueche p/q (q <= 4) im Bereich [1/4, 4]: {len(fr)}; Fenster +-{sr:.4f}; Zufallsanteil ~ {cover:.3f}")

print("\n" + "=" * 92)
sharpA = obsA_sharp == 2 and pA_sharp < 0.01
sharpB = bestB[0] == 2 and pB_sharp < 0.01
partA = obsA_sharp >= 1 and pA_sharp < 0.05
partB = bestB[0] >= 1 and pB_sharp < 0.05
v = "TRAEGT" if (sharpA or sharpB) else ("TRAEGT TEILWEISE" if (partA or partB) else "WIDERLEGT")
print(f"H234 Gesamturteil: {v}")
