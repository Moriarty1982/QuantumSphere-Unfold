"""k248: Drei-Mulden-Modell I th'' = -3K sin(3 th) - eta th' + tau (I = K = 1).
Erkundung 24.11.2026, nicht blind. Schwelle Libration -> Rotation und Rueckhalt-Drehmoment (Stewart-McCumber).
Aufruf: python3 k248_drei_mulden_schwelle.py
"""
import numpy as np
from scipy.integrate import solve_ivp


def run(w0, eta=0.0, tau=0.0, T=200):
    f = lambda t, y: [y[1], -3 * np.sin(3 * y[0]) - eta * y[1] + tau]
    s = solve_ivp(f, (0, T), [0, w0], rtol=1e-10, atol=1e-12, max_step=0.05)
    return s.y[0][-1], s.y[1][-1]


lo, hi = 0, 5
for _ in range(50):
    m = (lo + hi) / 2
    th, _ = run(m, T=60)
    (lo, hi) = (m, hi) if abs(th) < 2 * np.pi / 3 else (lo, m)
print("Schwelle omega_c =", hi, " analytisch 2*sqrt(K/I) = 2 ; omega_lib = 3 ; Verhaeltnis", hi / 3)
for eta in [0.05, 0.1, 0.2]:
    lo, hi = 0, 3
    for _ in range(30):
        m = (lo + hi) / 2
        th, w = run(6.0, eta, m, T=400)
        (lo, hi) = (lo, m) if abs(w) > 0.5 else (m, hi)
    Q = 3 / eta
    print(f"eta={eta}: Rueckhalt tau_r = {hi:.4f}, in Einheiten 3K: {hi/3:.4f}, Stewart-McCumber 4/(pi Q) = {4/(np.pi*Q):.4f}")
