"""Unabhaengige Nachrechnung von H47, r63, r64, r67 (eigener Code, nicht k102/k103)."""
import numpy as np
from scipy.optimize import brentq
from fractions import Fraction as Fr
print("== 1. Zaehlgleichungen (scipy brentq, Summe bis j = 2000) ==")
J = np.arange(1, 4001) / 2.0; a = np.sqrt(J*(J+1))
f = lambda g, w: np.sum(w*np.exp(-2*np.pi*g*a)) - 1
gT = brentq(lambda g: 2*np.exp(-2*np.pi*g*np.sqrt(0.75)) - 1, 0.01, 1)
gM = brentq(lambda g: f(g, 2.0), 0.05, 1); gG = brentq(lambda g: f(g, 2*J+1), 0.05, 1)
print(f"gamma_T = {gT:.12f}  (ln2/(pi sqrt3) = {np.log(2)/(np.pi*np.sqrt(3)):.12f})")
print(f"gamma_M = {gM:.12f}  gamma_GM = {gG:.12f}")
for n, g in [("DL/M", gM), ("GM", gG)]:
    L = g/gT; b = np.sqrt((L-1)/(L+1)); print(f"  {n}: gamma_L = {L:.6f}  beta = {b:.6f}  eta = {np.arctanh(b):.6f}  beta^2 = {b*b:.6f}")
print("== 2. Robertson: exakte Bruchrechnung fuer alle |j,m>, j <= 10 ==")
bad = 0
for tj in range(1, 21):
    j = Fr(tj, 2)
    for tm in range(-tj, tj+1, 2):
        m = Fr(tm, 2); prod = (j*(j+1) - m*m)/2; bound = abs(m)/2
        if prod < bound or ((prod == bound) != (abs(m) == j)): bad += 1
print("  Abweichungen:", bad)
print("== 3. Identitaeten ==")
L = gM/gT; eta = np.arctanh(np.sqrt((L-1)/(L+1)))
print(f"  cosh 2eta = {np.cosh(2*eta):.9f} vs gamma_L {L:.9f};  tanh 2eta = {np.tanh(2*eta):.6f} vs sqrt(1-1/gL^2) = {np.sqrt(1-1/L**2):.6f}")
print(f"  Omega_M = (gM-gT)/(gM+gT) = {(gM-gT)/(gM+gT):.6f};  2gT/(gM+gT) = {2*gT/(gM+gT):.6f};  gM+gT = {gM+gT:.6f};  -(0.12738+0.2375) = {-(0.127384+0.2375):.5f}")
print("== 4. Tachyon-Boden: numerischer Boost (Matrix), u = beta ==")
b = np.tanh(eta); g = 1/np.sqrt(1-b*b); B = np.array([[g, -g*b], [-g*b, g]])
E, p = B @ np.array([0.0, 1.0]); print(f"  E' = {E:.6f}, p' = {p:.6f}, v' = {p/E:.6f} (−1/beta = {-1/b:.6f}), E'^2-p'^2 = {E*E-p*p:.6f}")
u2 = np.tanh(2*eta); g2 = 1/np.sqrt(1-u2*u2); E2, p2 = np.array([[g2, -g2*u2], [-g2*u2, g2]]) @ np.array([0.0, 1.0])
print(f"  Boden des Spiegel-Frames (Relativgeschw. tanh 2eta) in M: v = {p2/E2:.6f} (−coth 2eta = {-1/u2:.6f})")
v = np.linspace(1.01, 50, 2000); Ev = 1/np.sqrt(v*v-1); print("  E(v) streng fallend:", bool(np.all(np.diff(Ev) < 0)), " E(1e6) =", 1/np.sqrt(1e12-1))
