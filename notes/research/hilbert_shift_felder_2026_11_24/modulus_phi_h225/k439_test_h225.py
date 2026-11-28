"""k439 (Test H225): Legt sich der gemeinsame Drehwinkel phi als Modulus fest, wenn die Vakuumenergie beider Lepton-Sektoren minimal ist?
Vorab-Notiz Vorab_H225_Modulus_phi.md (vor der Rechnung committet). Modell wie H221/H222 (k434/k435).
Aufruf aus diesem Ordner: python3 k439_test_h225.py > k439_out.txt
"""
import numpy as np
from scipy.optimize import minimize_scalar

DSTAR = 0.2222220470731
X = np.pi / 12 - DSTAR            # 0,0395773
SXNU, XNU = 0.00213, 0.04336
DGRID = np.linspace(0, 2 * np.pi, 4001)
SECT = {"Im": (+1.0, np.pi / 4), "Re": (-1.0, 0.0)}


def V(d, ap, chi, q, r):
    return -ap * np.cos(2 * (d - chi)) + q * np.cos(3 * d) + r * np.cos(6 * d)


def vmin(ap, chi, q, r):
    f = lambda d: V(d, ap, chi, q, r)
    v = f(DGRID)
    j = int(np.argmin(v))
    best = np.inf
    for k in np.argsort(v)[:12]:
        lo, hi = DGRID[max(k - 1, 0)], DGRID[min(k + 1, len(DGRID) - 1)]
        res = minimize_scalar(f, bounds=(lo, hi), method="bounded", options={"xatol": 1e-13})
        best = min(best, res.fun)
    return best


def E(phi, q, r=0.0, w=1.0):
    (a1, c1), (a2, c2) = SECT["Im"], SECT["Re"]
    return w * vmin(a1, c1 + phi, q, r) + vmin(a2, c2 + phi, q, r)


def minima_E(q, r=0.0, w=1.0, n=721):
    ph = np.linspace(0, np.pi / 3, n, endpoint=False)
    e = np.array([E(p, q, r, w) for p in ph])
    out = []
    for i in range(n):
        if e[i] <= e[i - 1] and e[i] <= e[(i + 1) % n]:
            res = minimize_scalar(lambda p: E(p, q, r, w), bounds=(ph[i] - np.pi / 3 / n, ph[i] + np.pi / 3 / n),
                                  method="bounded", options={"xatol": 1e-11})
            out.append((res.fun, res.x % (np.pi / 3)))
    out.sort()
    emin = out[0][0]
    glob = sorted({round(p, 9) for val, p in out if val < emin + 1e-12})
    return glob, out, ph, e


def verdict(phis):
    rel = [abs(p - X) / X for p in phis]
    return min(rel) if rel else np.inf


print("=" * 88)
print("H225 a  fuehrende Ordnung: E = -(1+w) + q [w |cos(pi/4-3phi)| + |sin 3phi|],  q<0 -> tan 3phi* = 1 + sqrt2/w")
print("=" * 88)
for w in (0.5, 1 / np.sqrt(2), 1.0, np.sqrt(2), 2.0):
    pa = np.arctan(1 + np.sqrt(2) / w) / 3
    S = lambda p: -(w * abs(np.cos(np.pi / 4 - 3 * p)) + abs(np.sin(3 * p)))
    ph = np.linspace(0, np.pi / 3, 200001)
    pn = ph[np.argmin(S(ph))]
    print(f"  w={w:.4f}: analytisch phi* = {pa:.7f} ({pa/np.pi:.5f} pi), numerisch {pn:.7f}; im Fenster (pi/12, pi/6): {np.pi/12 < pa < np.pi/6};"
          f" Abstand zu x {abs(pa-X)/X*100:.0f} %")
print(f"  w=1: phi* - pi/8 = {np.arctan(1+np.sqrt(2))/3 - np.pi/8:.1e}")
S1 = lambda p: abs(np.cos(np.pi / 4 - 3 * p)) + abs(np.sin(3 * p))
h = 1e-6
print(f"  Datenpunkt phi = x: S = {S1(X):.6f} (Maximum {S1(np.pi/8):.6f}), dS/dphi = {(S1(X+h)-S1(X-h))/(2*h):.4f} (kein stationaerer Punkt)")
hit_a = verdict([np.arctan(1 + np.sqrt(2)) / 3]) < 0.01

print("\n" + "=" * 88)
print("H225 b  endliches q (w = 1), exakte Minimierung in delta, phi-Gitter ueber eine Periode pi/3")
print("=" * 88)
best_b = np.inf
for q in (-0.001, -0.01, -0.05, -0.0852, -0.2, -0.3):
    glob, allm, ph, e = minima_E(q)
    rel = verdict(glob)
    best_b = min(best_b, rel)
    ex = E(X, q)
    rank = float(np.mean(e < ex))
    loc = ", ".join(f"{p:.6f}" for v_, p in allm)
    print(f"  q={q:+.4f}: globale Minima phi* = {[f'{g:.7f}' for g in glob]}  (pi/8 = {np.pi/8:.7f}); alle lokalen Minima [{loc}]")
    print(f"           E(phi*) = {allm[0][0]:.9f}, E(x) = {ex:.9f}, Anteil Gitterpunkte unter E(x): {rank:.3f};"
          f" naechstes globales Minimum zu x: {rel*100:.1f} % bzw. {min(abs(g-XNU) for g in glob)/SXNU:.0f} sigma(x_nu)")
hit_b = best_b < 0.01

print("\n" + "=" * 88)
print("H225 c  Ordnung 6 allein: r cos 6delta, r = +-1e-3 (q = 0)")
print("=" * 88)
best_c = np.inf
for r in (+1e-3, -1e-3):
    glob, allm, ph, e = minima_E(0.0, r)
    rel = verdict(glob)
    best_c = min(best_c, rel)
    print(f"  r={r:+.0e}: globale Minima phi* = {[f'{g:.7f}' for g in glob]}  (in pi: {[round(g/np.pi, 5) for g in glob]});"
          f" alle lokalen {[round(p, 6) for v_, p in allm]}; naechstes zu x: {rel*100:.1f} %")
hit_c = best_c < 0.01

print("\n" + "=" * 88)
print("H225 d (nachtraeglich, nicht in der Vorab-Notiz)  Sektor-Tausch: V_Re(-delta; pi/4 - phi) = V_Im(delta; phi) fuer alle q, r")
print("=" * 88)
rng = np.random.default_rng(225); mx = 0.0
for _ in range(1000):
    d, p, q, r = rng.uniform(0, 2*np.pi), rng.uniform(0, np.pi), rng.uniform(-1, 1), rng.uniform(-1, 1)
    mx = max(mx, abs(V(-d, -1.0, np.pi/4 - p, q, r) - V(d, 1.0, np.pi/4 + p, q, r)))
print(f"  groesste Abweichung (1000 Stichproben): {mx:.1e}  -> E(phi) = e_Im(phi) + e_Im(pi/4 - phi) ist spiegelsymmetrisch um phi = pi/8")
def roots(d, a=np.sqrt(2)):
    return np.sort(np.array([1 + a*np.cos(d + 2*np.pi*k/3) for k in range(3)])**2)
for lab, phi in (("phi* = pi/8", np.pi/8), ("phi = x (Daten)", X)):
    dI, dR = np.pi/12 - phi, np.pi/6 - phi
    mI, mR = roots(dI), roots(dR)
    print(f"  {lab}: delta_Im = {dI:+.6f}, delta_Re = {dR:+.6f};  m/m_max Im {np.round(mI/mI[-1], 6)}  Re {np.round(mR/mR[-1], 6)}")

print("\n" + "=" * 88)
print("H225 Gesamturteil (Kriterium: globales Minimum innerhalb 1 % von x = 0,0395773)")
print("=" * 88)
print(f"  a (w=1, nicht blind) Treffer: {hit_a};  b (endliches q) Treffer: {hit_b} (bester {best_b*100:.1f} %);  c (Ordnung 6) Treffer: {hit_c} (bester {best_c*100:.1f} %)")
if hit_b:
    v = "TRAEGT"
elif hit_c:
    v = "TRAEGT TEILWEISE"
else:
    v = "WIDERLEGT"
print("  ->", v)
