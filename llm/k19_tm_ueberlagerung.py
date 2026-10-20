"""k19: TM1 und TM2 gleichzeitig bzw. ueberlagert (zu K16). Reine Strukturrechnung, kein Datenfit."""
import numpy as np
from scipy.optimize import brentq
c1 = np.array([2, -1, -1])/np.sqrt(6)   # TBM-Spalte 1 (TM1 erhaelt sie)
c2 = np.array([1, 1, 1])/np.sqrt(3)     # TBM-Spalte 2 (TM2 erhaelt sie)
c3 = np.array([0, 1, -1])/np.sqrt(2)    # TBM-Spalte 3
s13_obs, s12_obs = 0.02215, 0.308

# (a) Beide Spalten exakt erhalten -> dritte Spalte durch Unitaritaet festgelegt
print("(a) beide erhalten: dritte Spalte = c1 x c2 =", np.round(np.cross(c1, c2), 4), "-> |U_e3|^2 =",
      round(abs(np.cross(c1, c2)[0])**2, 6), "(gemessen 0.02215)")

# (b) Ueberlagerung: erhalten bleibt w = cos(a) c2 - sin(a) e^{ib} c1  (a=0: TM2, a=90 Grad: TM1)
def ue2(a, b):
    w = np.cos(a)*c2 - np.sin(a)*np.exp(1j*b)*c1
    return abs(w[0])**2
for b in (0, np.pi/2, np.pi):
    print(f"(b) 1:1 (a=45 Grad), Phase b={np.degrees(b):.0f} Grad: |U_e|^2 der erhaltenen Spalte = {ue2(np.pi/4, b):.4f}")
print(f"    Ziel: nu1 braucht c12^2 c13^2 = {(1-s12_obs)*(1-s13_obs):.4f}, nu2 braucht s12^2 c13^2 = {s12_obs*(1-s13_obs):.4f}")
print(f"    Abstand 1:1-Wert zu |U_e3|^2: ({ue2(np.pi/4,0):.4f} - {s13_obs}) / 0.00057 = {(ue2(np.pi/4,0)-s13_obs)/0.00057:.1f} sigma")
# (c) Welches Gewicht a braucht man (b=0), damit die erhaltene Spalte nu1 bzw. nu2 ist?
for name, tgt, lo, hi in (("nu1", (1-s12_obs)*(1-s13_obs), np.radians(90), np.radians(135)),
                          ("nu2", s12_obs*(1-s13_obs), np.radians(0), np.radians(20))):
    a = brentq(lambda x: ue2(x, 0) - tgt, lo, hi)
    print(f"(c) erhaltene Spalte = {name}: a = {np.degrees(a):.2f} Grad  (TM1 = 90, TM2 = 0)")
