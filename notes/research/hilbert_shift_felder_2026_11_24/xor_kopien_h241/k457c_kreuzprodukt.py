"""k457c (nachtraeglich, Identitaet): Produkt ueber Kreuz zweier Richtungen des Kreises.
Behauptung: u_a(p) u_b(q) = -(p.q) [cos(a-b)? ...] + u_g(p x q) mit g = -(a+b); geprueft numerisch, Formel fuer Real- und e8-Teil wird gefittet.
Aufruf aus diesem Ordner: python3 k457c_kreuzprodukt.py > k457c_out.txt
"""
import numpy as np
from k457_test_h241 import mul, E, e8, rand_im8, u  # noqa: E402

rng = np.random.default_rng(4571)
print("k457c: u_a(p) u_b(q) zerlegt in Realteil (e0), e8-Teil und Imaginaerteil; Test Imaginaerteil = u_g(Im(pq)+ (p.q)) mit g = -(a+b)")
worst = 0.0; fits = []
for _ in range(200):
    a, b = rng.uniform(0, 2 * np.pi, 2)
    p = rand_im8(); q = rand_im8()
    z = mul(u((np.cos(a), np.sin(a)), p), u((np.cos(b), np.sin(b)), q))
    r = mul(p, q); r[0] = 0.0  # p x q
    g = -(a + b)
    pred_im = u((np.cos(g), np.sin(g)), r)
    im = z.copy(); im[0] = 0.0; im[8] = 0.0
    worst = max(worst, np.abs(im - pred_im).max())
    fits.append((z[0] / (-(p @ q)), z[8] / (-(p @ q)), a, b))
f = np.array(fits)
print(f"  max |Imaginaerteil - u_(-(a+b))(p x q)| = {worst:.1e}")
print(f"  Realteil/(-(p.q)) - cos(b-a): max {np.abs(f[:,0] - np.cos(f[:,3]-f[:,2])).max():.1e};  e8-Teil/(-(p.q)) - sin(b-a): max {np.abs(f[:,1] - np.sin(f[:,3]-f[:,2])).max():.1e}")
print("  => u_a(p) u_b(q) = -(p.q) [cos(b-a) + sin(b-a) e8] + u_(-(a+b))(p x q)")
print("  Kopien a, b in {0, 120, 240 Grad}: -(a+b) mod 180 ist wieder eine Kopie; fuer a != b die dritte, fuer a = b dieselbe (Z3-Gesetz k1+k2+k3 = 0 mod 3).")
for k1 in range(3):
    row = []
    for k2 in range(3):
        g = (-(k1 + k2) * 120) % 360
        row.append(f"V{k1+1}*V{k2+1} -> V{[0,120,240].index(g)+1}" if g in (0, 120, 240) else "?")
    print("   " + ";  ".join(row))
