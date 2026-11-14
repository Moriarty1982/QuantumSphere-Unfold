"""Erkundung: geordnete Dreifachprodukte der Frames, MxTxP gegen MxPxT.
(1) Produkte der Frame-Abbildungen R, T, J_B in allen sechs Reihenfolgen.
(2) Orientierungsungerader Teil als Bargmann-Invariante <1|2><2|3><3|1> von Frame-Zustaenden."""
import itertools
import numpy as np
R = np.array([[0, -1], [1, 0]], float); T = np.diag([1.0, -1.0]); JB = R @ T
maps = {"R": R, "T": T, "J_B": JB}
for order in itertools.permutations(maps):
    P = maps[order[0]] @ maps[order[1]] @ maps[order[2]]
    print("x".join(order), "=", "+1" if np.allclose(P, np.eye(2)) else "-1" if np.allclose(P, -np.eye(2)) else P.tolist())

def bargmann(states):
    a, b, c = states
    B = np.vdot(a, b) * np.vdot(b, c) * np.vdot(c, a)
    return round(abs(B), 6), round(np.angle(B) / np.pi, 6)

# Frame-Zustaende in der reellen Frame-Ebene: Winkel arctan(b/a) nach r85.3
g = 1.8647; aM, bM = (1 + 1 / g) / 2, (1 - 1 / g) / 2
ang = {"M": np.arctan2(bM, aM), "T": np.arctan2(aM, bM), "P": np.pi / 4}
vec = {k: np.array([np.cos(t), np.sin(t)], complex) for k, t in ang.items()}
print("Winkel/Grad:", {k: round(np.degrees(t), 2) for k, t in ang.items()})
print("Frame-Ebene (kommutativ, r51.1(c)): M-T-P", bargmann([vec["M"], vec["T"], vec["P"]]), " M-P-T", bargmann([vec["M"], vec["P"], vec["T"]]))
# Zum Vergleich: Achsenzustaende einer su(2) (unabhaengiges i), Reihenfolge x-y-z gegen x-z-y
sx = np.array([[0, 1], [1, 0]], complex); sy = np.array([[0, -1j], [1j, 0]]); sz = np.diag([1, -1]).astype(complex)
st = {k: np.linalg.eigh(A)[1][:, 1] for k, A in (("x", sx), ("y", sy), ("z", sz))}
print("su(2)-Achsen: x-y-z", bargmann([st["x"], st["y"], st["z"]]), " x-z-y", bargmann([st["x"], st["z"], st["y"]]))
