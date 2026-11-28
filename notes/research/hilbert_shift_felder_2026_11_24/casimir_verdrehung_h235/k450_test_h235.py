"""k450 (Test H235): Casimir-Verdrehungsenergie mit Sektorgewichten als Brecher des Sektortauschs.
Vorab-Notiz Vorab_H235_Casimir_Verdrehung.md (vor der Rechnung committet, 13cf65b).
E(phi; kappa) = e_Im(phi) + e_Re(phi) + kappa [w_I S(alpha_I) + w_R S(alpha_R)],  alpha_R = 2 phi, alpha_I = pi/2 - 2 phi,
S(a) = sum cos(n a)/n^4 (Bernoulli-Form), Baum wie H225 (q = -0,0852, r = 0).
Aufruf aus diesem Ordner: python3 k450_test_h235.py > k450_out.txt
"""
import numpy as np
from scipy.optimize import brentq

X = np.pi / 12 - 0.2222220470731
SIG = 7.8e-7
XNU, SXNU = 0.04336, 0.00213
Q0 = -0.0852
DG = np.linspace(0, 2 * np.pi, 8001)[:-1]
TP = 2 * np.pi


def V(d, sec, phi, q):
    P = q * np.cos(3 * d)
    return (-np.cos(2 * (d - np.pi / 4 - phi)) if sec == "Im" else np.cos(2 * (d - phi))) + P


def dV(d, sec, phi, q):
    dP = -3 * q * np.sin(3 * d)
    return (2 * np.sin(2 * (d - np.pi / 4 - phi)) if sec == "Im" else -2 * np.sin(2 * (d - phi))) + dP


def dmin(sec, phi, q):
    v = V(DG, sec, phi, q)
    h = DG[1] - DG[0]
    best = (np.inf, None)
    for k in np.argsort(v)[:10]:
        a, b = DG[k] - h, DG[k] + h
        if dV(a, sec, phi, q) * dV(b, sec, phi, q) > 0:
            continue
        d = brentq(lambda t: dV(t, sec, phi, q), a, b, xtol=1e-15)
        e = V(d, sec, phi, q)
        if e < best[0] - 1e-15:
            best = (e, d)
    return best


def fold(d):
    d = d % (2 * np.pi / 3)
    return min(d, 2 * np.pi / 3 - d)


def tree(phi, q=Q0):
    eI, dI = dmin("Im", phi, q)
    eR, dR = dmin("Re", phi, q)
    dE = -2 * np.sin(2 * (dI - np.pi / 4 - phi)) + 2 * np.sin(2 * (dR - phi))  # Einhuellende
    return eI + eR, dE, np.pi / 12 - fold(dI), np.pi / 6 - fold(dR)


def S(a):
    a = a % TP
    return np.pi ** 4 / 90 - np.pi ** 2 * a ** 2 / 12 + np.pi * a ** 3 / 12 - a ** 4 / 48


def Sp(a):
    a = a % TP
    return -np.pi ** 2 * a / 6 + np.pi * a ** 2 / 4 - a ** 3 / 12


def C(phi, wI, wR):
    return wI * S(np.pi / 2 - 2 * phi) + wR * S(2 * phi)


def Cp(phi, wI, wR):
    return -2 * wI * Sp(np.pi / 2 - 2 * phi) + 2 * wR * Sp(2 * phi)


def E(phi, kap, wI, wR):
    return tree(phi)[0] + kap * C(phi, wI, wR)


print("=" * 96)
print("H235 (k450)  Casimir-Verdrehung mit Sektorgewichten: legt sie phi = x fest?")
print("=" * 96)

# Pruefung: Tausch der Verdrehungswinkel und Baum-Tausch
print("\nVorpruefung: Baum E_tree(phi) = E_tree(pi/4 - phi) und C mit w_I = w_R symmetrisch")
for p in (0.03, 0.1, 0.25):
    print(f"  phi = {p}: E_tree Diff {tree(p)[0] - tree(np.pi/4 - p)[0]:+.1e};  C(1,1) Diff {C(p,1,1) - C(np.pi/4-p,1,1):+.1e};"
          f"  C(2,1) Diff {C(p,2,1) - C(np.pi/4-p,2,1):+.3e}")

# Teil A: phi_x aus o_Im(phi) = x
print("\nTeil A (teilweise blind)  phi_x mit o_Im(phi_x) = x; x_nu,pred = o_Re(phi_x)")
grid = np.linspace(0.0, 0.2, 201)
f = np.array([tree(p)[2] - X for p in grid])
roots = [brentq(lambda p: tree(p)[2] - X, grid[i], grid[i + 1], xtol=1e-15)
         for i in range(len(grid) - 1) if f[i] * f[i + 1] < 0 and abs(f[i] - f[i + 1]) < 0.05]
print(f"  Nullstellen in [0, 0,2]: {[round(r, 10) for r in roots]}")
px = roots[0]
Et, dEt, oI, oR = tree(px)
zA = (oR - XNU) / SXNU
okA = abs(zA) <= 2
print(f"  phi_x = {px:.10f}  (x = {X:.10f}, phi_x - x = {px - X:+.3e})")
print(f"  o_Im = {oI:.10f}, o_Re = x_nu,pred = {oR:.7f}  ->  {zA:+.2f} sigma  (A bestanden: {okA})")
print(f"  E_tree(phi_x) = {Et:.10f}, dE_tree/dphi = {dEt:+.6e}")

# Teil B
print("\nTeil B (blind)  kappa* aus dE/dphi = 0 bei phi_x, Hauptfall w_I = 2, w_R = 1 (Fermionen: kappa > 0)")


def analyse(wI, wR, label, report=True):
    cp = Cp(px, wI, wR)
    if abs(cp) < 1e-14:
        if report:
            print(f"  {label}: dC/dphi = 0 bei phi_x, kein kappa*")
        return None
    k = -dEt / cp
    h = 1e-5
    d2 = (E(px + h, k, wI, wR) - 2 * E(px, k, wI, wR) + E(px - h, k, wI, wR)) / h ** 2
    ph = np.linspace(0, 2 * np.pi / 3, 1441, endpoint=False)
    ev = np.array([E(p, k, wI, wR) for p in ph])
    i = int(np.argmin(ev))
    glob = abs(ev[i] - E(px, k, wI, wR)) < 1e-10 or E(px, k, wI, wR) <= ev.min() + 1e-12
    if report:
        print(f"  {label}: kappa* = {k:+.6e}  (kappa*/|q| = {k/abs(Q0):+.5f}), d2E/dphi2 = {d2:+.4e} ({'Minimum' if d2 > 0 else 'kein Minimum'})")
        print(f"     globales Minimum auf Gitter bei phi = {ph[i]:.5f} (E = {ev[i]:.10f}); E(phi_x) = {E(px, k, wI, wR):.10f}; phi_x global: {glob}")
        print(f"     Vergleich: 1/(16 pi^2) = {1/(16*np.pi**2):.5e}, alpha = {1/137.036:.5e}, alpha |q| = {abs(Q0)/137.036:.5e}")
    return k, d2, glob


res = analyse(2, 1, "(w_I, w_R) = (2, 1)")
k, d2, glob = res
okB1 = k > 0 and d2 > 0
okB2 = okB1 and glob
print(f"  B1 (kappa* > 0 und lokales Minimum): {okB1};  B2 (zusaetzlich global): {okB2}")

print("\nNur Bericht")
for wI, wR, lab in ((1, 0, "(1, 0) nur geladen"), (2, 2, "(2, 2) Dirac-Neutrinos"), (1, 2, "(1, 2) vertauscht"), (4, 1, "(4, 1)")):
    analyse(wI, wR, lab)
print("  Lage des globalen Minimums als Funktion von kappa, (2, 1):")
ph = np.linspace(0, 2 * np.pi / 3, 721, endpoint=False)
et = np.array([tree(p)[0] for p in ph])
c21 = np.array([C(p, 2, 1) for p in ph])
for kk in (-1e-1, -1e-2, -1e-3, 0.0, 1e-3, 1e-2, 3e-2, 1e-1, 1.0):
    i = int(np.argmin(et + kk * c21))
    print(f"    kappa = {kk:+.0e}: phi_min = {ph[i]:.5f}  (o_Im dort {tree(ph[i])[2]:+.5f})")

print("\n" + "=" * 96)
v = "TRAEGT" if (okA and okB2) else ("TRAEGT TEILWEISE" if (okA and okB1) else "WIDERLEGT")
print(f"H235 Gesamturteil: {v}   (A {okA}, B1 {okB1}, B2 {okB2})")
