"""k458 (Test H242): alte Kernel-Definition K3 = K1 K2 (e3 = e1 e2, komplexe z_k) in S eingebettet: z e_k -> (Re z e_k, Im z e_k).
Schluss von span{1,K1,K2,K3}, Kopien-Belegungen, Zufallskontrolle. Vorab Vorab_H242_Kernel_XOR.md.
Produkt wie k253/k321/k453-k457. Aufruf aus diesem Ordner: python3 k458_test_h242.py > k458_out.txt
"""
import itertools
import numpy as np

N = 16
rng = np.random.default_rng(458)


def conj(x):
    y = -x.copy(); y[0] = x[0]; return y


def mul(x, y):
    n = len(x)
    if n == 1:
        return x * y
    h = n // 2
    a, b, c, d = x[:h], x[h:], y[:h], y[h:]
    return np.concatenate([mul(a, c) - mul(conj(d), b), mul(d, a) + mul(b, conj(c))])


E = np.eye(N); e8 = np.eye(8)
assert np.allclose(mul(e8[1], e8[2]), e8[3])  # e3 = e1 e2 in dieser Konvention


def K(alpha, k):
    return np.concatenate([np.cos(alpha) * e8[k], np.sin(alpha) * e8[k]])


def closure_residual(al):
    S = np.column_stack([E[0]] + [K(a, k) for a, k in zip(al, (1, 2, 3))])
    P = S @ S.T
    r = 0.0
    for i in range(4):
        for j in range(4):
            z = mul(S[:, i], S[:, j]); r = max(r, np.linalg.norm(z - P @ z))
    return r


def ang(a):
    return np.degrees(np.mod(a, np.pi))


print("=" * 96)
print("H242 (k458)  Kernel-Tripel K_k = u_(alpha_k)(e_k), e3 = e1 e2, in S;  Schluss von span{1,K1,K2,K3}")
print("=" * 96)

# C / N1: Orthogonalitaet und Phase von K1 K2
orth = 0.0; phase = 0.0
for _ in range(500):
    a1, a2 = rng.uniform(0, 2 * np.pi, 2)
    z = mul(K(a1, 1), K(a2, 2))
    orth = max(orth, abs(z @ K(a1, 1)), abs(z @ K(a2, 2)))
    phase = max(phase, np.linalg.norm(z - K(-(a1 + a2), 3)))
print(f"\nN1/C: max |<K1K2, K1>|, |<K1K2, K2>| = {orth:.1e};  max |K1K2 - u_(-(a1+a2))(e3)| = {phase:.1e}")

# A / N2
res = []
for _ in range(2000):
    al = rng.uniform(0, 2 * np.pi, 3)
    res.append((closure_residual(al), abs(np.sin(al.sum()))))
res = np.array(res)
corr = np.max(np.abs(res[:, 0] - res[:, 1]))
on_rule = 0.0
for _ in range(500):
    a1, a2 = rng.uniform(0, 2 * np.pi, 2); s = rng.integers(0, 2)
    on_rule = max(on_rule, closure_residual([a1, a2, -(a1 + a2) + s * np.pi]))
print(f"N2/A: auf der Regel a1+a2+a3 = 0 mod pi: max Schlussrest = {on_rule:.1e} (500 Stichproben)")
print(f"      zufaellige Tripel: Schlussrest / |sin(a1+a2+a3)|: min {np.min(res[:,0]/res[:,1]):.6f}, max {np.max(res[:,0]/res[:,1]):.6f}"
      f"  (Rest = |sin(Summe)|, max Abw. {corr:.1e})")
print(f"Zufallskontrolle: Anteil zufaelliger Tripel mit Schlussrest < 1e-6: {np.sum(res[:,0] < 1e-6)}/2000")

# N3: gemeinsame Phase
ths = np.linspace(0, np.pi, 3600, endpoint=False)
cl = [t for t in ths if closure_residual([t, t, t]) < 1e-9]
print(f"\nN3: gemeinsame Phase, Schluss bei (Grad, 3600 Stuetzstellen): {[round(np.degrees(t), 4) for t in cl]}")

# B / N4: Kopien-Belegungen
cop = [0.0, 2 * np.pi / 3, 4 * np.pi / 3]
closed = []
for g in itertools.product(range(3), repeat=3):
    r = closure_residual([cop[i] for i in g])
    if r < 1e-9:
        closed.append(g)
rule = [g for g in itertools.product(range(3), repeat=3) if sum(g) % 3 == 0]
print(f"\nN4/B: Kopien-Belegungen (g1,g2,g3), die schliessen: {len(closed)} von 27: {closed}")
print(f"      gleich der Menge g1+g2+g3 = 0 mod 3: {set(closed) == set(rule)}")

# Bericht: Tachyon-Abbildung J = i
print("\nNur Bericht: K2 = J K1 mit J = i (a2 = a1 + 90 Grad), K3 := K1 K2 -> a3 = -(2 a1 + 90 Grad)")
for a1d in (0, 30, 45, 60, 90, 120, 180):
    a1 = np.radians(a1d); a3 = -(2 * a1 + np.pi / 2)
    print(f"  a1 = {a1d:3d} Grad: a3 = {ang(a3):7.2f} Grad (mod 180), Re z3 = {np.cos(a3):+.4f}")
print("  -> Photon-Kriterium Re z3 = 0 genau fuer a1 = 0 mod 90 Grad")

# Bericht: Brannen-Phasen
print("\nNur Bericht: Brannen-Phasen theta_k = -delta + 2 pi k/3 als Kernel-Phasen")
for name, d in (("delta_Im", 0.2222220470731), ("delta_Re", 0.48399), ("delta = 0", 0.0)):
    al = [-d + 2 * np.pi * k / 3 for k in range(3)]
    print(f"  {name}: Summe mod pi = {ang(sum(al)):.4f} Grad, Schlussrest = {closure_residual(al):.4f} (= |sin 3 delta| = {abs(np.sin(3*d)):.4f})")
print("\n" + "=" * 96)
