"""k435 (Test H222): Waehlt das Vorzeichen der kubischen Spektralinvariante cos 3delta den Zweig in beiden Lepton-Sektoren, ohne Skala?
Vorab-Notiz Vorab_H222_Zweigwahl_skalenfrei.md (vor der Rechnung committet). Modell wie H221/k434.
Aufruf aus diesem Ordner: python3 k435_test_h222.py > k435_out.txt
"""
import numpy as np
from scipy.optimize import minimize_scalar

DSTAR = 0.2222220470731
X_LEP = np.pi / 12 - DSTAR
DM21, S21, DM31, S31 = 7.537e-5, 0.097e-5, 2.511e-3, 0.0205e-3
DM32_IO, S32_IO = 2.498e-3, 0.025e-3
ROBS = DM21 / DM31; SR = ROBS * np.hypot(S21 / DM21, S31 / DM31)
RIO = DM21 / DM32_IO; SRIO = RIO * np.hypot(S21 / DM21, S32_IO / DM32_IO)
GRID = np.linspace(0, 2 * np.pi, 20001)


def fold(d):
    d = d % (2 * np.pi / 3)
    return min(d, 2 * np.pi / 3 - d)


def V(d, alphap, chi, q):
    return -alphap * np.cos(2 * (d - chi)) + q * np.cos(3 * d)


def minima(alphap, chi, q, tol=1e-12):
    f = lambda d: V(d, alphap, chi, q)
    v = f(GRID)
    idx = np.where((v[1:-1] <= v[:-2]) & (v[1:-1] <= v[2:]))[0] + 1
    ms = []
    for j in idx:
        r = minimize_scalar(f, bracket=(GRID[j - 1], GRID[j], GRID[j + 1]), tol=1e-15)
        ms.append((r.fun, r.x))
    vmin = min(m[0] for m in ms)
    out = []
    for val, x in sorted(ms):
        if val < vmin + tol:
            fx = fold(x)
            if all(abs(fx - o) > 1e-7 for o in out):
                out.append(fx)
    return sorted(out)


def roots(d, a=np.sqrt(2)):
    return np.array([1 + a * np.cos(d + 2 * np.pi * k / 3) for k in range(3)])


def detY(d):
    return np.prod(roots(d))


def R_NO(d):
    m = np.sort(roots(d) ** 2)
    return (m[1] ** 2 - m[0] ** 2) / (m[2] ** 2 - m[0] ** 2)


def R_IO(d):
    m = np.sort(roots(d) ** 2)
    m3, m1, m2 = m
    return (m2 ** 2 - m1 ** 2) / abs(m2 ** 2 - m3 ** 2)


SECT = {"Im (c=1, alphap=+1)": (+1.0, np.pi / 4, lambda p: np.pi / 12 - p),
        "Re (c=0, alphap=-1)": (-1.0, 0.0, lambda p: np.pi / 6 - p)}

print("=" * 86)
print("H222 a/b  Regel 'max cos 3delta' unter den entarteten Minima nach gemeinsamer Drehung phi (q = 0)")
print("=" * 86)
ok = {"Im (c=1, alphap=+1)": True, "Re (c=0, alphap=-1)": True}
for phi in (0.01, 0.02, X_LEP, 0.05, 0.06):
    for nm, (ap, chi0, target) in SECT.items():
        br = minima(ap, chi0 + phi, 0.0)
        c3 = [np.cos(3 * b) for b in br]
        pick = br[int(np.argmax(c3))]
        hit = abs(pick - target(phi)) < 1e-6
        ok[nm] &= hit and len(br) == 2
        det = [detY(b) for b in br]
        neg = [int(np.sum(roots(b) < 0)) for b in br]
        print(f"  phi={phi:.6f} {nm:20s}: Zweige {np.round(br, 7)}  cos3d {np.round(c3, 5)}  detY/mu^3 {np.round(det, 5)}  neg. Wurzeln {neg}"
              f"  -> Wahl {pick:.7f} (Ziel {target(phi):.7f}) {'JA' if hit else 'nein'}")
print(f"  Kriterium a (Im-Sektor waehlt pi/12 - phi): {'JA' if ok['Im (c=1, alphap=+1)'] else 'nein'}")
print(f"  Kriterium b (Re-Sektor waehlt pi/6 - phi):  {'JA' if ok['Re (c=0, alphap=-1)'] else 'nein'}")

print("\n" + "=" * 86)
print("H222 c  verworfener Re-Zweig pi/6 + x_lepton gegen die Daten")
print("=" * 86)
for lab, d in (("gewaehlt  pi/6 - x_lepton", np.pi / 6 - X_LEP), ("verworfen pi/6 + x_lepton", np.pi / 6 + X_LEP)):
    rn, ri = R_NO(d), R_IO(d)
    print(f"  {lab}: delta = {d:.6f}, Wurzeln {np.round(roots(d), 5)}; R_NO = {rn:.6f} ({(rn-ROBS)/SR:+.1f} sigma), R_IO = {ri:.6f} ({(ri-RIO)/SRIO:+.1f} sigma)")
dr = np.pi / 6 + X_LEP
zc = min(abs(R_NO(dr) - ROBS) / SR, abs(R_IO(dr) - RIO) / SRIO)
print(f"  kleinster Abstand des verworfenen Zweigs: {zc:.1f} sigma -> Kriterium c: {'ausgeschlossen (> 3 sigma)' if zc > 3 else 'nicht ausgeschlossen'}")
# Bereich: fuer welche Versaetze x' liegt der verworfene Zweig pi/6 + x' innerhalb 2 sigma?
xs = np.linspace(0, 0.1, 100001)
inside = [x for x in xs if abs(R_NO(np.pi / 6 + x) - ROBS) / SR < 2 or abs(R_IO(np.pi / 6 + x) - RIO) / SRIO < 2]
print(f"  verworfener Zweig pi/6 + x' innerhalb 2 sigma fuer x' in [0, 0,1]: {'keines' if not inside else f'[{min(inside):.5f}, {max(inside):.5f}]'}")

print("\n" + "=" * 86)
print("H222 d (numerische Kontrolle, symbolisch in Wolfram)  det Y/mu^3 = 1 - 3a^2/4 + a^3/4 cos 3delta")
print("=" * 86)
rng = np.random.default_rng(222); mx = 0.0
for _ in range(1000):
    d, a = rng.uniform(0, 2 * np.pi), rng.uniform(0, 3)
    mx = max(mx, abs(np.prod(roots(d, a)) - (1 - 0.75 * a * a + a ** 3 / 4 * np.cos(3 * d))))
print(f"  groesste Abweichung (1000 Stichproben): {mx:.1e}")

print("\n" + "=" * 86)
print("H222 e  Robustheit: q = -eps, phi = x_lepton")
print("=" * 86)
oke = True
for eps in (1e-2, 1e-4, 1e-6):
    for nm, (ap, chi0, target) in SECT.items():
        br = minima(ap, chi0 + X_LEP, -eps)
        dev = abs(br[0] - target(X_LEP)) if len(br) == 1 else np.inf
        good = len(br) == 1 and (eps > 1e-5 or dev < 1e-5)
        oke &= good
        print(f"  eps={eps:.0e} {nm:20s}: globale Minima {np.round(br, 9)}  Abstand zum Zweig {dev:.2e}  {'ok' if good else 'NEIN'}")
    # Gegenprobe Vorzeichen: q = +eps waehlt den anderen Zweig
for nm, (ap, chi0, target) in SECT.items():
    print(f"  Gegenprobe q = +1e-4 {nm:20s}: globale Minima {np.round(minima(ap, chi0 + X_LEP, +1e-4), 7)}")
print(f"  Kriterium e: {'JA' if oke else 'nein'}")

print("\n" + "=" * 86)
print("H222 Gesamturteil")
print("=" * 86)
if not ok["Im (c=1, alphap=+1)"] or not ok["Re (c=0, alphap=-1)"]:
    v = "WIDERLEGT"
elif oke and mx < 1e-12 and zc > 3:
    v = "TRAEGT (Vorzeichen des kubischen Terms bleibt gesetzt)"
else:
    v = "TRAEGT TEILWEISE"
print("  ->", v)
