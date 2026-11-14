"""Erkundung: Kreuzprodukte der Frame-Abbildungen (r51) und Orthogonale der Frame-Gewichte (r85)."""
import numpy as np
R = np.array([[0, -1], [1, 0]], float)   # z -> iz auf der reellen Frame-Ebene
T = np.diag([1.0, -1.0])                  # z -> conj(z)
JB = R @ T                                # z -> i conj(z)
for n, A in (("R", R), ("T", T), ("J_B", JB)):
    print(n, "Quadrat =", np.round(A @ A, 12).tolist())
comm = lambda A, B: (A @ B - B @ A) / 2
for (a, A), (b, B) in (("R", R), ("T", T)), (("T", T), ("J_B", JB)), (("J_B", JB), ("R", R)):
    C = comm(A, B)
    name = [n for n, X in (("R", R), ("-R", -R), ("T", T), ("-T", -T), ("J_B", JB), ("-J_B", -JB)) if np.allclose(C, X)]
    print(f"[{a},{b}]/2 =", name)
g = 1.864700
aM = (1 + 1 / g) / 2; bM = (1 - 1 / g) / 2
eta = np.diag([1.0, -1.0])
M, Tw, P = np.array([aM, bM]), np.array([bM, aM]), np.array([0.5, 0.5])
print("<M,T> =", M @ eta @ Tw, " <P,P> =", P @ eta @ P, " <M,M> =", round(M @ eta @ M, 6), "= 1/gamma:", round(1 / g, 6))
