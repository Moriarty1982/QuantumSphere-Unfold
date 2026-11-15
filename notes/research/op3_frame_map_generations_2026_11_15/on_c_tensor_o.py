"""Nachtrag zu r15.5: wirken die Frame-Abbildungen von r51 auf C x O als drei unverzerrte Basen?

Operatoren wie in k91 (v4.9.0-r51, Test H35): R = Multiplikation mit i (C-linear),
T = komplexe Konjugation (antilinear), J_B = R o T. Q, Sektoren P_(l,r) wie dort.
Aufruf: python on_c_tensor_o.py <Pfad zu notes/research/v4_10_0_r48_r55/llm>
"""
import sys, os
import numpy as np

sys.path.insert(0, os.path.abspath(sys.argv[1]))
from k69_test_h17 import omul  # noqa: E402

E = np.eye(8)
L7 = np.array([omul(E[7], E[j]) for j in range(8)]).T
R7 = np.array([omul(E[j], E[7]) for j in range(8)]).T
iL, iR = 1j * L7, 1j * R7
Q = 0.5 * np.eye(8) - (1j / 6) * L7 - (1j / 3) * R7
def P(l, r): return 0.25 * (np.eye(8) + l * iL) @ (np.eye(8) + r * iR)
S = [(1, 1), (-1, 1), (1, -1), (-1, -1)]
rng = np.random.default_rng(15)

# (1) R ist ein Skalar: jeder Zustand ist R-Eigenzustand
R = 1j * np.eye(8)
print("(1) R = i*1 auf C x O: jeder Zustand Eigenzustand (Eigenwert i); R zeichnet keine Basis aus")

# (2) Eigenstrahlen von T und J_B: Kv = lam v fuer antilineares K
#     T: conj(v) = lam v  <=>  v = e^{i a} * reell;  J_B: i conj(v) = lam v  <=>  ebenso
def is_T_eig(v):
    w = np.conj(v); lam = np.vdot(v, w) / np.vdot(v, v); return np.linalg.norm(w - lam * v) < 1e-10
def is_JB_eig(v):
    w = 1j * np.conj(v); lam = np.vdot(v, w) / np.vdot(v, v); return np.linalg.norm(w - lam * v) < 1e-10
same = 0
for _ in range(200):
    v = np.exp(1j * rng.uniform(0, 2 * np.pi)) * rng.normal(size=8)
    same += is_T_eig(v) and is_JB_eig(v)
print(f"(2) Zufaellige T-Eigenstrahlen (Phase * reell), auch J_B-Eigenstrahlen: {same}/200;"
      " T und J_B haben dieselben Eigenstrahlen, Ueberlappung 1 statt 1/2")

# (3) Ladung und Sektor von T-Eigenzustaenden
w_bal, q_def = 0.0, 0.0
for _ in range(500):
    v = rng.normal(size=8); v /= np.linalg.norm(v)
    w = {s: np.linalg.norm(P(*s) @ v) ** 2 for s in S}
    w_bal = max(w_bal, max(abs(w[(l, r)] - w[(-l, -r)]) for l, r in S))
    q = np.vdot(v, Q @ v).real
    q_def = max(q_def, abs(q - 0.5))
print(f"(3) Reelle Zustaende: Gewicht in P_(l,r) = Gewicht in P_(-l,-r) (max. Abweichung {w_bal:.1e});"
      f" <Q> = 1/2 fuer alle (max. Abweichung {q_def:.1e})")
print("    -> kein T- oder J_B-Eigenzustand hat eine bestimmte Ladung oder Chiralitaet")

# (4) Wo die drei unverzerrten Basen tatsaechlich leben: auf der reellen Ebene span(1, e7) bzw. der z-Ebene,
#     komplexifiziert. Auf C x O entspricht das zwei Kopien: die Ports (Eigenraeume von iL_e7).
Pp, Pm = 0.5 * (np.eye(8) + iL), 0.5 * (np.eye(8) - iL)
print(f"(4) Ports (Eigenraeume von iL_e7): Dimension {round(np.trace(Pp).real)} und {round(np.trace(Pm).real)};"
      f" conj tauscht sie: {np.allclose(np.conj(Pp), Pm)}")
