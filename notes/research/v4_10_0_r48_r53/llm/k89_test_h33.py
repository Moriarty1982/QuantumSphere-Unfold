"""k89: Test der Vorab-Notiz H33 (Commit ec06de3): Ist e7 die Photon-Achse? Singulett-Ebene span(1, e7), Ladung der e7-Achse auf einer
Generation (B - L), und ob Q_em aus L_e7, R_e7 allein gebaut werden kann."""
import numpy as np, os, sys
from fractions import Fraction as Fr
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from k69_test_h17 import omul

TOL = 1e-9
E = np.eye(8)
L7 = np.array([omul(E[7], E[j]) for j in range(8)]).T
R7 = np.array([omul(E[j], E[7]) for j in range(8)]).T
iL, iR = 1j*L7, 1j*R7
def P(l, r): return 0.25*(np.eye(8) + l*iL)@(np.eye(8) + r*iR)

# H33a
B = np.zeros((8, 2)); B[0, 0] = 1; B[7, 1] = 1          # span_C(1, e7)
Pspan = B@B.T
Psing = P(1, 1) + P(-1, -1)
d_span = abs(Pspan - Psing).max()
d_LR = abs((L7 - R7)@B).max()
ok_a = d_span < TOL and d_LR < TOL
print(f"H33a: |P_span(1,e7) - (P(1,1) + P(-1,-1))| = {d_span:.1e}; |(L_e7 - R_e7) auf span(1,e7)| = {d_LR:.1e}"
      f" -> {'bestaetigt' if ok_a else 'widerlegt'}")

# H33b: Zustaende einer Generation (r42.1(b)): Sektor (l, r), 2 T3, Chiralitaet C = 1 auf iL = +1, Teilchen, B - L
gen = [  # (l, r), 2T3, Name, B - L
    ((1, 1), 1, "nu", Fr(-1)), ((1, 1), -1, "e", Fr(-1)),
    ((-1, 1), 1, "d^c", Fr(-1, 3)), ((-1, 1), -1, "u^c", Fr(-1, 3)),
    ((1, -1), 1, "u", Fr(1, 3)), ((1, -1), -1, "d", Fr(1, 3)),
    ((-1, -1), 1, "e^c", Fr(1)), ((-1, -1), -1, "nu^c", Fr(1))]
ok_b = True; rows = []
for (l, r), t2, name, bl in gen:
    Q = Fr(3 - l - 2*r, 6); T3 = Fr(t2, 2); C = 1 if l == 1 else 0
    Y2 = Q - Fr(1, 2) + (1 - C)*T3
    Qem = T3 + Q - Fr(1, 2)
    T3L, T3R = C*T3, (1 - C)*T3
    ok_b &= (2*(Q - Fr(1, 2)) == bl) and (Y2 == bl/2 + T3R) and (Qem == T3L + T3R + bl/2)
    rows.append(f"{name}: Q={Q}, 2(Q-1/2)={2*(Q-Fr(1,2))}, B-L={bl}, Y/2={Y2}, Q_em={Qem}")
print("\nH33b: " + "; ".join(rows) + f" -> {'bestaetigt' if ok_b else 'widerlegt'}")

# H33c: jede Funktion von 1, iL, iR ist auf einem Sektor konstant: f = a + b l + c r + d l r; bester Fit an Q_em
A = np.array([[1, l, r, l*r] for (l, r), *_ in gen], dtype=float)
q = np.array([float(Fr(t2, 2) + Fr(3 - l - 2*r, 6) - Fr(1, 2)) for (l, r), t2, *_ in gen])
coef, res, *_ = np.linalg.lstsq(A, q, rcond=None)
resid = abs(A@coef - q).max()
ok_c = resid > 0.1
print(f"\nH33c: bester Fit von Q_em durch a + b iL + c iR + d iL iR: max. Abweichung {resid:.3f} (= 1/2: die T3-Aufspaltung im Dublett)"
      f" -> {'bestaetigt' if ok_c else 'widerlegt'}")
