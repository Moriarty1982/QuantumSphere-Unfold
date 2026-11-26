"""k363 (H168): Skala und Sektoren. Ladungsmischung je Sektor, gemeinsamer Versatz, Neutrino-Daten.
Vorab-Notiz Vorab_Notiz_H168_Skala_und_Sektoren.md (Commit 27d4e39).
Aufruf: python3 k363_test_h168.py > k363_out.txt
"""
import numpy as np
from scipy.optimize import brentq

DSTAR = 0.2222220470731
X = np.pi / 12 - DSTAR
DM21, S21, DM31, S31 = 7.537e-5, 0.097e-5, 2.511e-3, 0.0205e-3     # NuFIT 6.1 wie H99b
ROBS = DM21 / DM31
SR = ROBS * np.hypot(S21 / DM21, S31 / DM31)


def fold(d):
    d = d % (2 * np.pi / 3)
    return min(d, 2 * np.pi / 3 - d)


def roots(d):
    return np.sort([1 + np.sqrt(2) * np.cos(d + 2 * np.pi * k / 3) for k in range(3)])


def R_of(d):
    m = np.sort(roots(d) ** 2)
    return (m[1] ** 2 - m[0] ** 2) / (m[2] ** 2 - m[0] ** 2)


print("== H168a: Minima des Spin-1-Terms je Ladungsmischung ==")
for c in (0.0, 1.0):
    chi = np.arctan(c)
    ms = sorted({round(fold(chi + k * np.pi / 2), 12) for k in range(4)})
    print(f"c = {c:.0f}: chi = {chi:.6f}; Minima chi + k pi/2, gefaltet: {ms}")
    for d in ms:
        print(f"    delta = {d:.6f}: Wurzeln {np.round(roots(d), 6)}")
print(f"pi/6 - pi/12 = {np.pi/6 - np.pi/12:.12f} = pi/12 = {np.pi/12:.12f}")

print("\n== H168b: gemeinsamer Versatz ==")
print(f"x = pi/12 - delta* = {X:.10f}; delta_e = pi/12 - x = {np.pi/12 - X:.10f}; delta_nu(H99) = delta* + pi/12 = {DSTAR + np.pi/12:.10f}; "
      f"pi/6 - x = {np.pi/6 - X:.10f}; Differenz {DSTAR + np.pi/12 - (np.pi/6 - X):.1e}")
print(f"als Mischung: chi_e = pi/4 - x -> c_e = {np.tan(np.pi/4 - X):.10f}; chi_nu = -x -> c_nu = {np.tan(-X):.10f}")

print("\n== H168c: gemeinsame Skala? ==")
print(f"R_obs = {ROBS:.6f} +- {SR:.6f}")
for nm, d in (("pi/6 (kein Versatz)", np.pi / 6), ("pi/6 - x (gleicher Versatz, H99)", np.pi / 6 - X), ("pi/12 (Oktant)", np.pi / 12)):
    print(f"  delta_nu = {nm}: R = {R_of(d):.6f}; Abstand {(R_of(d) - ROBS)/SR:+.2f} sigma")
MSUM_L = sum(np.sqrt([0.51099895, 105.6583755, 1776.93]))            # MeV^(1/2)
r = roots(np.pi / 6 - X); t2 = np.sqrt(DM31 / (r[2]**4 - r[0]**4))   # eV: m_i = t2 r_i^2
print(f"  Neutrinomassen bei pi/6 - x (meV): {np.round(1e3 * t2 * r**2, 3)}; Summe der Wurzeln {np.sqrt(t2)*3:.5f} eV^(1/2)")
ratio = (np.sqrt(t2) * 3 / (MSUM_L * 1e3)) ** 2
print(f"  (Summe sqrt m_nu / Summe sqrt m_l)^2 = {ratio:.2e}: Versatz aus Ordnung 6 bei gemeinsamem Lambda waere x_nu = {X * ratio:.1e}")

print("\n== H168d: acht Kandidaten (blind) ==")
within = []
for nm, base in (("0", 0.0), ("pi/12", np.pi / 12), ("pi/6", np.pi / 6), ("pi/4", np.pi / 4)):
    for sg in (-1, +1):
        d = fold(base + sg * X)
        Rv = R_of(d); z = (Rv - ROBS) / SR
        rt = roots(d)
        if abs(z) <= 3:
            within.append(f"{nm} {'-' if sg < 0 else '+'} x")
        print(f"  delta_nu = {nm:5s} {'-' if sg < 0 else '+'} x (gefaltet {d:.6f}): Wurzeln {np.round(rt, 4)}, R = {Rv:.6f}, {z:+.1f} sigma")
print(f"innerhalb 3 sigma: {within}")
f = lambda d: R_of(d) - ROBS
dn = brentq(f, np.pi / 12 + 1e-3, np.pi / 6)
dlo = brentq(lambda d: R_of(d) - (ROBS - SR), np.pi / 12 + 1e-3, np.pi / 6); dhi = brentq(lambda d: R_of(d) - (ROBS + SR), np.pi / 12 + 1e-3, np.pi / 6)
xn = np.pi / 6 - dn; sx = abs(dhi - dlo) / 2
print(f"Daten verlangen (Zweig zwischen pi/12 und pi/6): delta_nu = {dn:.6f}, x_nu = pi/6 - delta_nu = {xn:.6f} +- {sx:.6f}; x = {X:.6f}; ({X - xn:+.6f}, {(X - xn)/sx:+.2f} sigma)")
print(f"H168d: {'bestaetigt' if within == ['pi/6 - x'] else 'widerlegt'}")

print("\n== H168e: native Zahlen gegen den Versatz (blind) ==")
B = 0.5494056410; GL = 1.8646997646; GM = 0.237533
consts = {"beta": B, "beta^2": B * B, "1-beta^2": 1 - B * B, "eps0": np.arctanh(B), "gamma_L": GL, "1/gamma_L": 1 / GL, "gamma_L-1": GL - 1,
          "gamma_M": GM, "kappa": (GL + 1 / GL) / 2}
facs = {"1": 1, "1/2": 0.5, "1/3": 1 / 3, "1/4": 0.25, "1/6": 1 / 6, "1/12": 1 / 12, "1/(2pi)": 1 / (2 * np.pi), "1/(4pi)": 1 / (4 * np.pi)}
targets = {"x": X, "2x": 2 * X, "3x": 3 * X, "tan x": np.tan(X), "tan 2x": np.tan(2 * X)}
res = []
for cn, cv in consts.items():
    for fn, fv in facs.items():
        for tn, tv in targets.items():
            res.append((abs(cv * fv - tv) / tv, f"{cn} * {fn}", tn))
res.sort()
hits = [r_ for r_ in res if r_[0] < 1e-4]
print(f"{len(res)} Vergleiche; Treffer (relativ < 1e-4): {len(hits)}")
for rel, a, b in res[:6]:
    print(f"  {a:22s} gegen {b:6s}: relativ {rel:.2e}")
print(f"H168e: {'bestaetigt (kein Treffer)' if not hits else 'widerlegt (Treffer)'}")
