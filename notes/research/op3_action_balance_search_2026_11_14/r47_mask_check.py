"""Erkundung: r47-Leptonmaske W_l = diag(0,0,-3) als Einslot-Projektor und Codex-H.
Kopplung nach r47: M + eps(WM + MW) mit M = -R (rang-eins-Zirkulante, tau-Mittel).
Gesucht: eps mit K_orb = 2/3 (Slot 3 ausgezeichnet). Zum Vergleich additiv (r46): M + delta*D_S."""
import numpy as np
from scipy.optimize import brentq
W = np.exp(2j*np.pi/3)
R = np.ones((3, 3))/3
Q3 = np.diag([0, 0, 1.0])
Wl = -3*Q3
def K(H, slot=2):
    v, U = np.linalg.eigh(H); psi = U[:, 0]
    S = W*np.eye(3) + (1-W)*np.diag(np.eye(3)[slot])
    d = np.vdot(psi, S@psi); return (1+2*abs(d)**2)/3, v[1]-v[0], np.angle(d**3)/np.pi
for sign in (+1, -1):
    f = lambda e: K(sign*(-R) + e*(Wl@(sign*-R) + (sign*-R)@Wl))[0] - 2/3
    xs = np.linspace(-3, 3, 6001); vals = [f(x) for x in xs]
    roots = [brentq(f, xs[i], xs[i+1]) for i in range(len(xs)-1) if vals[i]*vals[i+1] < 0]
    print("anticommutator, M = %+d*(-R): eps roots" % sign, [round(r, 6) for r in roots],
          [tuple(round(float(x), 5) for x in K(sign*(-R) + r*(Wl@(sign*-R)+(sign*-R)@Wl))) for r in roots])
f = lambda d: K(-R + d*Wl)[0] - 2/3
print("additive -R + delta*W_l: delta =", round(brentq(f, 0.01, 2), 6), "(balance a=b means delta = 1/3)")
