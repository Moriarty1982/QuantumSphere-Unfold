"""k255c: (7) Spiegelungen aus S3 (det M = -1, e8 -> -e8) kehren L_e8 um, Drehungen nicht.
(8) Die Generationsbasis g_k = 1/sqrt3 + sqrt(2/3) w(x)f_k liegt in der Kopie O_k. Aufruf aus diesem Ordner."""
import numpy as np
src = open("../k253_cayley_dickson_turm.py").read().split("for n in range(0, 6):")[0]
ns = {}; exec(src, ns); mul = ns["mul"]
E = np.eye(16); s3 = np.sqrt(3) / 2
def auto(lam, M):
    A = np.zeros((16, 16)); A[0, 0] = 1; A[8, 8] = lam
    for i in range(1, 8):
        A[i, i] = M[0][0]; A[i, i + 8] = M[0][1]; A[i + 8, i] = M[1][0]; A[i + 8, i + 8] = M[1][1]
    return A
Le8 = np.array([mul(E[8], e) for e in E]).T
els = {"Drehung 120": auto(1, [[-0.5, -s3], [s3, -0.5]]), "Spiegelung diag(1,-1)": auto(-1, [[1, 0], [0, -1]]),
       "Spiegelung 60": auto(-1, [[-0.5, s3], [s3, 0.5]])}
for k, A in els.items():
    print(f"(7) {k}: A L_e8 A^-1 = +L_e8: {np.allclose(A @ Le8 @ A.T, Le8)}, = -L_e8: {np.allclose(A @ Le8 @ A.T, -Le8)}")
w = np.zeros(7); w[2] = 1  # w = e3 (beliebig)
for k, th in enumerate([0, 2 * np.pi / 3, 4 * np.pi / 3]):
    g = np.concatenate([[1 / np.sqrt(3)], np.sqrt(2 / 3) * np.cos(th) * w, [0], np.sqrt(2 / 3) * np.sin(th) * w])
    # Kopie mit Linie bei th (mod 180)
    B = np.array([E[0]] + [np.cos(th) * E[i] + np.sin(th) * E[i + 8] for i in range(1, 8)])
    P = B.T @ np.linalg.pinv(B.T)
    print(f"(8) g_{k}: |g| = {np.linalg.norm(g):.6f}, Abstand zur Kopie O_{int(np.rad2deg(th))}: {np.linalg.norm(g - P @ g):.1e}, g^2 = {np.round(mul(g, g)[[0]], 6)} (Realteil)")
