"""Nachrechnung verworfener Tests mit spaeter berichtigter Grundannahme.  (Erkundung, nicht blind.)

H13 (Wigner-Holonomie der Triolen-Schleife): damals Geschwindigkeit je Frame 1/sqrt3 (Hopf/magischer Winkel).  Spaeter festgelegt
(Konvention F, r63/r68): Frame M hat beta_sym = tanh(eta), beta_sym = 0,549406.  Wigner-Winkel = Defekt des gleichseitigen hyperbolischen
Dreiecks; Seitenlaenge a mit cosh a = cosh^2 eta + 1/2 sinh^2 eta (Richtungen 120 Grad); Innenwinkel cos A = cosh a/(cosh a + 1).
Kriterium damals: f13 = cos(delta) gegen f(+) = 0,9436 +- 0,0083, widerlegt bei |z| >= 3.
H73 (Zustandsgleichung der Bezugszustaende): w = -p-/(3 p+) mit x = p-/p+; Materie-Frame x = beta^2, Tachyon-Frame 1/x.  Schranke |w+1| <= 0,05.
"""
import numpy as np

def wigner(v):
    eta = np.arctanh(v)
    ca = np.cosh(eta) ** 2 + 0.5 * np.sinh(eta) ** 2
    A = np.arccos(ca / (ca + 1))
    return np.pi - 3 * A

f_plus, s = 0.9436, 0.0083
for name, v in (("damals 1/sqrt3", 1 / np.sqrt(3)), ("Konvention F: beta_sym", 0.549406)):
    d = wigner(v); z = (np.cos(d) - f_plus) / s
    print(f"H13 {name:24s} v = {v:.6f}: delta = {np.degrees(d):.2f} Grad, cos delta = {np.cos(d):.4f}, z = {z:+.1f} -> {'widerlegt' if abs(z) >= 3 else 'vertraeglich'}")
# welche Geschwindigkeit braeuchte f(+)?
from scipy.optimize import brentq
vstar = brentq(lambda v: np.cos(wigner(v)) - f_plus, 0.05, 0.57)
print(f"H13 Geschwindigkeit fuer f(+): v = {vstar:.4f} (Rapiditaet {np.arctanh(vstar):.4f}); Bestandswerte: beta_sym 0,5494, 1/sqrt3 0,5774")
x = 0.549406 ** 2
print(f"H73 Materie-Frame w = {-x/3:.4f} (|w+1| = {abs(-x/3+1):.3f}); Tachyon-Frame w = {-1/(3*x):.4f} (|w+1| = {abs(-1/(3*x)+1):.3f}); Schranke 0,05")
