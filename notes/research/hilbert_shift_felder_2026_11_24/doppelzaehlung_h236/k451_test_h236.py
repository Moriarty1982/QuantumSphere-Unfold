"""k451 (Test H236): Wer traegt den Versatz, q-Fit (H167) oder phi? Vorab Vorab_H236_Doppelzaehlung.md (Commit 14c5f3f).
Baum wie H225: V_Im = -cos2(d - pi/4 - phi) + q cos3d, V_Re = cos2(d - phi) + q cos3d.
Aufruf aus diesem Ordner: python3 k451_test_h236.py > k451_out.txt
"""
import numpy as np
from scipy.optimize import brentq

X = np.pi / 12 - 0.2222220470731
XNU, SXNU = 0.04336, 0.00213
DG = np.linspace(0, 2 * np.pi, 8001)[:-1]


def V(d, sec, phi, q):
    return (-np.cos(2 * (d - np.pi / 4 - phi)) if sec == "Im" else np.cos(2 * (d - phi))) + q * np.cos(3 * d)


def dV(d, sec, phi, q):
    return (2 * np.sin(2 * (d - np.pi / 4 - phi)) if sec == "Im" else -2 * np.sin(2 * (d - phi))) - 3 * q * np.sin(3 * d)


def dmin(sec, phi, q):
    v = V(DG, sec, phi, q)
    h = DG[1] - DG[0]
    best = (np.inf, None)
    for k in np.argsort(v)[:10]:
        a, b = DG[k] - h, DG[k] + h
        if dV(a, sec, phi, q) * dV(b, sec, phi, q) > 0:
            continue
        d = brentq(lambda t: dV(t, sec, phi, q), a, b, xtol=1e-15)
        if V(d, sec, phi, q) < best[0] - 1e-15:
            best = (V(d, sec, phi, q), d)
    return best


def fold(d):
    d = d % (2 * np.pi / 3)
    return min(d, 2 * np.pi / 3 - d)


def offs(phi, q):
    return np.pi / 12 - fold(dmin("Im", phi, q)[1]), np.pi / 6 - fold(dmin("Re", phi, q)[1])


def phi_of_q(q):
    """phi mit o_Im(phi, q) = x, Suche in [-0,1, 0,1]"""
    g = np.linspace(-0.1, 0.1, 201)
    f = [offs(p, q)[0] - X for p in g]
    for i in range(200):
        if f[i] * f[i + 1] < 0 and abs(f[i] - f[i + 1]) < 0.05:
            return brentq(lambda p: offs(p, q)[0] - X, g[i], g[i + 1], xtol=1e-15)
    return None


def oRe_at(q):
    p = phi_of_q(q)
    return p, offs(p, q)[1]


print("=" * 92)
print("H236 (k451)  Doppelzaehlung: Lesarten Q, Phi, M")
print("=" * 92)
p, oR = oRe_at(-0.0852)
print(f"\nLesart Q (nicht blind): q = -0,0852 -> phi = {p:+.3e}, x_nu,pred = {oR:.6f} ({(oR - XNU)/SXNU:+.2f} sigma)")
oI0, oR0 = offs(X, -1e-9)
print(f"Lesart Phi (nicht blind): q -> 0-, phi = x -> o_Im = {oI0:.8f}, x_nu,pred = {oR0:.8f} ({(oR0 - XNU)/SXNU:+.2f} sigma)")

print("\nLesart M (blind): o_Re - x als Funktion von q (phi jeweils aus o_Im = x)")
qs = [-0.06, -0.04, -0.03, -0.02, -0.015, -0.01, -0.005, -0.002, -1e-3, -1e-4, -1e-6]
for q in qs:
    p, oR = oRe_at(q)
    print(f"  q = {q:+.1e}: phi = {p:.7f}, o_Re = {oR:.7f}, o_Re - x = {oR - X:+.3e}")


def solve_q(target):
    if target <= X:
        return None
    return brentq(lambda q: oRe_at(q)[1] - target, -0.06, -1e-7, xtol=1e-12)


qc = solve_q(XNU)
qhi = solve_q(XNU + 2 * SXNU)
qlo = solve_q(XNU - 2 * SXNU)
pc = phi_of_q(qc)
print(f"\n  Mittelwert x_nu = {XNU}: q* = {qc:+.6f}, phi* = {pc:.7f}  (Anteil von q am Im-Versatz: {(X - pc)/X*100:.1f} %)")
print(f"  x_nu + 2 sigma = {XNU + 2*SXNU:.5f}: q = {qhi:+.6f}")
if qlo is None:
    print(f"  x_nu - 2 sigma = {XNU - 2*SXNU:.5f} < x: mit q <= 0 nicht erreichbar (braucht o_Re < o_Im, also q > 0 = anderer Zweig nach H222);"
          f" Untergrenze q = 0")
    lo = 0.0
else:
    print(f"  x_nu - 2 sigma: q = {qlo:+.6f}")
    lo = qlo
print(f"  2-sigma-Bereich: q in [{qhi:+.5f}, {lo:+.5f}]")
in0 = True  # Grenze q = 0 eingeschlossen (x_nu - 2 sigma < x)
inQ = qhi <= -0.0852
print(f"  q = 0 im Bereich: {in0};  q = -0,0852 im Bereich: {inQ}  ->  Kriterium A (phi traegt): {in0 and not inQ}")
print(f"  q = -0,0852 liegt {(-0.0852)/qhi:.1f}-mal weiter draussen als die 2-sigma-Grenze")
