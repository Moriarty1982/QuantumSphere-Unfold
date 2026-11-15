"""Zwei Klassen auf der untersten Ebene: "liegt im Nullzustand oder nicht" (Erkundung, nicht blind).

Lesart B, z = E + iB, s = z.z (bilinear), 2u = E^2 + B^2, Boden phi = |s|/2u = |b|.
Baut auf k220 (Bahnen von SO(3,C) x Dualitaet: Schalen |s| = r, punktierter Nullkegel, {0}) auf.
(1) Mit der Skala (z -> lambda z, lambda komplex != 0: Dualitaetsphase und Dilatation) bilden alle nicht lichtartigen Felder
    EINE Bahn: zu z1, z2 mit s1, s2 != 0 wird lambda und L in SO(3,C) mit z2 = lambda L z1 konstruiert.
(2) Der punktierte Nullkegel ist eine Bahn schon von SO(3,C): zu lichtartigen n1, n2 != 0 wird L mit n2 = L n1 konstruiert.
(3) Jede Klasse hat einen ausgezeichneten Vertreter: nicht lichtartig -> Boost in den Frame E || B gibt phi = 1 (reiner Zustand,
    Bezugsframe R von v4.9.0-r24.3); lichtartig -> phi = 0 in jedem Frame (Photonpunkt P).  Boosts geben phi in (0, 1].
(4) Rapiditaet des Boosts nach R: phi = sech(2 eta_R).  Entlang des Nullaugenblicks (Beispiel r20.1) divergiert eta_R:
    die freie Zeitentwicklung erreicht in endlicher Zeit, was Boosts erst bei unendlicher Rapiditaet erreichen.
"""
import numpy as np

rng = np.random.default_rng(1117)
dot = lambda a, b: a @ b
cvec = lambda: rng.normal(size=3) + 1j * rng.normal(size=3)


def frame(w):
    e1 = w / np.sqrt(dot(w, w))
    while True:
        v = cvec(); v = v - dot(v, e1) * e1
        if abs(dot(v, v)) > 1e-3:
            break
    e2 = v / np.sqrt(dot(v, v))
    return np.column_stack([e1, e2, np.cross(e1, e2)])


def null_frame(n):
    while True:
        v = cvec()
        if abs(dot(n, v)) > 1e-2:
            break
    a = 1 / dot(n, v); m = a * v - a * a * dot(v, v) / 2 * n      # m.m = 0, n.m = 1
    return n, m, 1j * np.cross(n, m)                              # k.k = 1, k.n = k.m = 0


def null_vec():
    a = rng.normal(size=3); b = rng.normal(size=3); b = b - (a @ b) / (a @ a) * a
    return a + 1j * b * np.linalg.norm(a) / np.linalg.norm(b)


def boost(E, B, v, n):
    n = n / np.linalg.norm(n); g = 1 / np.sqrt(1 - v * v); vv = v * n
    return (g * (E + np.cross(vv, B)) - (g - 1) * np.dot(E, n) * n,
            g * (B - np.cross(vv, E)) - (g - 1) * np.dot(B, n) * n)


def phi(E, B):
    z = E + 1j * B
    return abs(z @ z) / (E @ E + B @ B)


# (1)
res = orth = det = 0.0
for _ in range(2000):
    z1, z2 = cvec(), cvec() * rng.uniform(0.1, 10)
    lam = np.sqrt(dot(z2, z2) / dot(z1, z1))
    L = frame(z2) @ frame(lam * z1).T
    res = max(res, np.abs(L @ (lam * z1) - z2).max() / np.abs(z2).max())
    orth = max(orth, np.abs(L.T @ L - np.eye(3)).max()); det = max(det, abs(np.linalg.det(L) - 1))
print(f"(1) nicht lichtartig, mit Skala: z2 = lambda L z1 fuer 2000 Paare, rel. Residuum {res:.1e},"
      f" |L^T L - 1| {orth:.1e}, |det L - 1| {det:.1e} -> eine Bahn")

# (2)
res = orth = det = 0.0
for _ in range(2000):
    n1, n2 = null_vec(), null_vec() * rng.uniform(0.1, 10)
    (a1, m1, k1), (a2, m2, k2) = null_frame(n1), null_frame(n2)
    L = np.outer(a2, m1) + np.outer(m2, a1) + np.outer(k2, k1)
    if np.linalg.det(L).real < 0:
        L = np.outer(a2, m1) + np.outer(m2, a1) - np.outer(k2, k1)
    res = max(res, np.abs(L @ n1 - n2).max() / np.abs(n2).max())
    orth = max(orth, np.abs(L.T @ L - np.eye(3)).max()); det = max(det, abs(np.linalg.det(L) - 1))
print(f"(2) lichtartig: n2 = L n1 fuer 2000 Paare, rel. Residuum {res:.1e}, |L^T L - 1| {orth:.1e},"
      f" |det L - 1| {det:.1e} -> eine Bahn")

# (3)
dev1 = 0.0; lo, hi = 1.0, 0.0; dev0 = 0.0
for _ in range(1000):
    E, B = rng.normal(size=3), rng.normal(size=3)
    S = np.cross(E, B); u2 = E @ E + B @ B
    eta = 0.5 * np.arctanh(2 * np.linalg.norm(S) / u2)
    Er, Br = boost(E, B, np.tanh(eta), S)
    dev1 = max(dev1, abs(phi(Er, Br) - 1), np.linalg.norm(np.cross(Er, Br)) / (Er @ Er + Br @ Br))
    Eb, Bb = boost(E, B, rng.uniform(0, 0.999), rng.normal(size=3)); p = phi(Eb, Bb); lo, hi = min(lo, p), max(hi, p)
    n = null_vec(); En, Bn = boost(n.real, n.imag, rng.uniform(0, 0.99), rng.normal(size=3))
    dev0 = max(dev0, phi(En, Bn))
print(f"(3) nicht lichtartig: Boost nach E || B gibt phi = 1 (Abw. {dev1:.1e}); beliebige Boosts: phi in [{lo:.4f}, {hi:.4f}];"
      f" lichtartig: phi = 0 in jedem Frame (max {dev0:.1e})")

# (4)
E, B = np.array([1, 0, 0.3j]), np.array([0.7j, 1, 0])
print("(4) Beispielfeld r20.1: Boden und Rapiditaet des Boosts nach R, phi = sech(2 eta_R)")
for t in (-0.6, -0.2, -0.05, -0.01, -0.001, 0.0):
    e, b = (E * np.exp(-1j * t)).real, (B * np.exp(-1j * t)).real; p = phi(e, b)
    S = np.cross(e, b); eta = 0.5 * np.arctanh(min(2 * np.linalg.norm(S) / (e @ e + b @ b), 1.0))
    chk = abs(p - 1 / np.cosh(2 * eta)) if np.isfinite(eta) else 0.0
    print(f"    t = {t:+.3f}: phi = {p:.5f}, eta_R = {eta:.3f} (|phi - sech 2 eta_R| = {chk:.0e})")
