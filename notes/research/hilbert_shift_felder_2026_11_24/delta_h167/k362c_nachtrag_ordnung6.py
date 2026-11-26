"""k362c (H167, nachtraeglich, Erkundung): Auch der Term sechster Ordnung allein hebt das Elektron aus dem Oktanten.
c = 1, alpha = 0, K = 2/3 (A = B = v0): V_delta/v0^4 = -alphap sin 2 delta + q cos 3 delta, q = beta3 v0^2 (v0^2 in Einheiten Lambda^2).
Aufruf: python3 k362c_nachtrag_ordnung6.py > k362c_out.txt
"""
import numpy as np
DSTAR = 0.2222220470731


def fold(d):
    d = d % (2 * np.pi / 3)
    return min(d, 2 * np.pi / 3 - d)


grid = np.linspace(0, 2 * np.pi, 2000001)
print("q/alphap  globales Minimum (gefaltet)  m_klein/m_gross")
for q in (-0.2, -0.1, -0.0852, -0.05, -0.01, 0.01, 0.05, 0.1):
    V = -np.sin(2 * grid) + q * np.cos(3 * grid)
    d = grid[np.argmin(V)]
    ev = np.sort([1 + np.sqrt(2) * np.cos(d + 2 * np.pi * k / 3) for k in range(3)])
    print(f"{q:+.4f}   {fold(d):.6f}   {ev[0]**2/ev[2]**2:.3e}")
d = 5 * np.pi / 4 + (np.pi / 12 - DSTAR)
q = -2 * np.cos(2 * d) / (3 * np.sin(3 * d))
hess = 4 * np.sin(2 * d) - 9 * q * np.cos(3 * d)
print(f"delta* verlangt q/alphap = beta3 v0^2/alphap = {q:+.8f} (Zweig delta = 5 pi/4 + x, zweite Ableitung {hess:+.3f} > 0)")
print(f"Vergleich: Konjugationsterm allein verlangt alpha/alphap = {np.tan(np.pi/6 - 2*DSTAR):+.8f}")
