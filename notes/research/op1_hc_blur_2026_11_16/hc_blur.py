"""Verwischte HC-Maske und Gegen-HC (Erkundung, analytisch, numerisch bestaetigt; Ideen des Autors vom 16.11.2026).
(1) HC-Maske P = Projektor auf m = +-j laengs einer Achse; Mittel ueber alle Achsen (Haar, 4000 Drehungen) = c * I mit c = 2/(2j+1).
(2) Robertson: Dx Dy = (j(j+1) - m^2)/2 >= |m|/2, Gleichheit nur bei m = +-j (r63.2).
(3) gamma aus den Zaehlgewichten: verwischte Maske (2), volle Zaehlung (2j+1), Komplement allein (2j-1)."""
import numpy as np
from scipy.linalg import expm
from scipy.spatial.transform import Rotation
from scipy.optimize import brentq
def ops(j):
    m = np.arange(j, -j-1, -1); d = len(m)
    Jz = np.diag(m).astype(complex); Jp = np.zeros((d, d), complex)
    for k in range(1, d): Jp[k-1, k] = np.sqrt(j*(j+1) - m[k]*(m[k]+1))
    return (Jp+Jp.conj().T)/2, (Jp-Jp.conj().T)/2j, Jz, m
rng = np.random.default_rng(0)
print("j | Spur HC-Maske | HC nach Verwischen (Mittel ueber Achsen) = c*I, c | 2/(2j+1) | Robertson-Saettigung nur m=+-j")
for j in (0.5, 1, 1.5, 2, 3):
    Jx, Jy, Jz, m = ops(j)
    P = np.diag([1.0 if abs(abs(x)-j) < 1e-12 else 0 for x in m]).astype(complex)
    acc = np.zeros_like(P)
    N = 4000
    for _ in range(N):
        a = Rotation.random(random_state=rng.integers(1e9)).as_rotvec()
        U = expm(-1j*(a[0]*Jx + a[1]*Jy + a[2]*Jz)); acc += U @ P @ U.conj().T
    E = acc/N
    c = np.trace(E).real/len(m)
    sat = [abs(0.5*(j*(j+1)-x*x) - 0.5*abs(x)) < 1e-12 for x in m]
    print(f"{j} | {np.trace(P).real:.0f} | Abweichung von c*I {np.max(np.abs(E - c*np.eye(len(m)))):.3f}, c = {c:.4f} | {2/(2*j+1):.4f} | {[float(x) for x,s in zip(m,sat) if s]}")
js = np.arange(1, 4000)/2; a = np.sqrt(js*(js+1))
g = lambda w: brentq(lambda x: np.sum(w*np.exp(-2*np.pi*x*a)) - 1, 0.01, 2)
print("gamma aus Spur der verwischten Maske (2 je j):", round(g(2*np.ones_like(js)), 6), "| volle Zaehlung (2j+1):", round(g(2*js+1), 6))
print("Gegen-HC (Komplement, 2j-1 Zustaende) allein:", round(g(np.maximum(2*js-1, 1e-300)), 6) if True else "")
