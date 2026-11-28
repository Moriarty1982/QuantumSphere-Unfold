"""k454 (Test H238): Leck-Energie auf dem Kreis der wellenfaehigen Richtungsraeume; Brannen-Form als Ueberlapp; Lage der Brannen-Phasen.
Vorab Vorab_H238_Kreis_Energie.md (Commit siehe Ergebnis-Notiz). Produkt wie k253/k321/k453.
Aufruf aus diesem Ordner: python3 k454_test_h238.py > k454_out.txt
"""
import numpy as np

N = 16


def conj(x):
    y = -x.copy(); y[0] = x[0]; return y


def mul(x, y):
    n = len(x)
    if n == 1:
        return x * y
    h = n // 2
    a, b, c, d = x[:h], x[h:], y[:h], y[h:]
    return np.concatenate([mul(a, c) - mul(conj(d), b), mul(d, a) + mul(b, conj(c))])


E = np.eye(N)


def U(t):
    return [np.cos(t) * E[i] + np.sin(t) * E[8 + i] for i in range(1, 8)]


def leak(t):
    u = U(t)
    B = np.array([E[0]] + u)
    P = B.T @ B
    return sum(np.sum((mul(a, b) - P @ mul(a, b)) ** 2) for a in u for b in u)


print("=" * 96)
print("H238 (k454)  Leck-Energie L(theta) auf dem Kreis U_theta = {cos t e_i + sin t e_(8+i)}")
print("=" * 96)
ts = np.linspace(0, 2 * np.pi, 360, endpoint=False)
L = np.array([leak(t) for t in ts])
s2 = np.sin(3 * ts) ** 2
A = (L @ s2) / (s2 @ s2)
res = np.abs(L - A * s2).max()
print(f"\nTeil A: Fit L = A sin^2(3 theta): A = {A:.12f}, max Restabweichung = {res:.2e} (Kriterium < 1e-10)")
# Fourier-Kontrolle
c = np.fft.rfft(L) / len(L)
print("  Fourier-Anteile |c_m| (m = 0..8): " + ", ".join(f"{abs(c[m]):.2e}" for m in range(9)))
# Minima
mins = [ts[i] for i in range(360) if L[i] <= L[i - 1] and L[i] <= L[(i + 1) % 360] and L[i] < 1e-9]
print(f"  Minima (Grad): {[round(np.degrees(m), 6) for m in mins]}  -> Klassen mod 180 Grad: {sorted({round(np.degrees(m) % 180, 6) for m in mins})}")
h = 1e-4
for m in [0.0, 2 * np.pi / 3, 4 * np.pi / 3]:
    d2 = (leak(m + h) - 2 * leak(m) + leak(m - h)) / h ** 2
    print(f"  L''({np.degrees(m):.0f} Grad) = {d2:.6f}  (18 A = {18*A:.6f})")
other = [ts[i] for i in range(360) if L[i] <= L[i - 1] and L[i] <= L[(i + 1) % 360] and L[i] >= 1e-9]
print(f"  weitere lokale Minima: {len(other)}")
okA = res < 1e-10 and len({round(np.degrees(m) % 180, 6) for m in mins}) == 3 and not other
print(f"  Teil A: {'TRAEGT' if okA else 'nicht erfuellt'}")

print("\nTeil B (nicht blind): Ueberlapp und Brannen-Form")
tk = [0.0, 2 * np.pi / 3, 4 * np.pi / 3]
copies = [U(t) for t in tk]
for t in (0.3, 1.1):
    ov = [sum(np.dot(a, b) for a, b in zip(U(t), ck)) / 7 for ck in copies]
    print(f"  theta = {t}: Ueberlapp mit Kopien = {np.round(ov, 12).tolist()}, cos(theta - theta_k) = {np.round([np.cos(t - x) for x in tk], 12).tolist()}")
for w in (1.0, np.sqrt(2), 2.0):
    Ks = []
    for t in np.linspace(0, 2 * np.pi, 13):
        a = np.array([1 + w * np.cos(t - x) for x in tk])
        Ks.append(np.sum(a ** 2) / np.sum(a) ** 2)
    print(f"  w = {w:.6f}: K ueber theta = [{min(Ks):.12f}, {max(Ks):.12f}]  (2/3 = {2/3:.12f})")
print("  Kopien-Winkel: V1 = 0, V2 = 120, V3 = 240 Grad (mit v -> -v gewaehlt); Ueberlapp der Kopien untereinander cos 120 = -1/2 (H138)")

print("\nTeil C (blind): Leck-Energie an den gemessenen Brannen-Phasen (theta = +-delta)")
okC = True
for name, d in (("delta_Im (geladen)", 0.2222220470731), ("delta_Re (neutral)", 0.48399)):
    r = leak(d) / A
    okC &= r < 0.01
    print(f"  {name} = {d}: L/max L = sin^2(3 delta) = {r:.6f}  ({np.degrees(d):.3f} Grad; naechste Kopie bei 0 bzw. 120 Grad)")
print(f"  Teil C: {'Phasen im Minimum' if okC else 'Phasen abseits der Minima'}")
print("\n" + "=" * 96)
print(f"H238 Urteil (Teil A): {'TRAEGT' if okA else 'WIDERLEGT/TEILWEISE (siehe oben)'}")
