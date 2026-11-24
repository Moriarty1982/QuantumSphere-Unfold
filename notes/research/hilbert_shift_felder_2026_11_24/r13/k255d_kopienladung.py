"""k255d: Kann eine Ladung, die jede Kopie O_k als eine Generation liest, mit psi vertauschen?
Q_S = 1/2 - (i/6) L_e7 - (i/3) R_e7 auf C(x)S (k85-Form, ueber e7 fortgesetzt). Kopienladung Q^(k) = psi^k Q_S psi^-k,
symmetrisiert Qbar = (1/3) sum_k Q^(k). Spektren und Generationsinhalt. Aufruf aus diesem Ordner."""
import numpy as np
src = open("../k253_cayley_dickson_turm.py").read().split("for n in range(0, 6):")[0]
ns = {}; exec(src, ns); mul = ns["mul"]
E = np.eye(16); s3 = np.sqrt(3) / 2
def auto(lam, M):
    A = np.zeros((16, 16)); A[0, 0] = 1; A[8, 8] = lam
    for i in range(1, 8):
        A[i, i] = M[0][0]; A[i, i + 8] = M[0][1]; A[i + 8, i] = M[1][0]; A[i + 8, i + 8] = M[1][1]
    return A
psi = auto(1, [[-0.5, -s3], [s3, -0.5]])
L7 = np.array([mul(E[7], e) for e in E]).T; R7 = np.array([mul(e, E[7]) for e in E]).T
QS = 0.5 * np.eye(16) - 1j / 6 * L7 - 1j / 3 * R7
def spec(Q):
    ev = np.round(np.linalg.eigvals(Q).real, 6) + 0
    u, c = np.unique(ev, return_counts=True); return dict(zip(u.tolist(), c.tolist()))
print("Q_S hermitesch:", np.allclose(QS, QS.conj().T), "; Spektrum auf C(x)S:", spec(QS))
B0 = np.array([E[i] for i in range(8)]).T  # O_0 = erste Haelfte
print("Q_S auf C(x)O_0 (eine Generation erwartet):", spec(B0.T @ QS @ B0), "; O_0 invariant:", np.allclose((np.eye(16) - B0 @ B0.T) @ QS @ B0, 0))
Qk = [np.linalg.matrix_power(psi, k) @ QS @ np.linalg.matrix_power(psi, k).T for k in range(3)]
print("[Q_S, psi] =", f"{np.abs(QS @ psi - psi @ QS).max():.3f}", "; [Q^(0), Q^(1)] =", f"{np.abs(Qk[0] @ Qk[1] - Qk[1] @ Qk[0]).max():.3f}")
Qbar = sum(Qk) / 3
print("Qbar = (1/3) sum Q^(k): [Qbar, psi] =", f"{np.abs(Qbar @ psi - psi @ Qbar).max():.1e}", "; Spektrum:", spec(Qbar))
print("Erlaubt (N3): {0, 1/3, 2/3, 1}; Qbar in diesem Spektrum:", set(spec(Qbar)) <= {0.0, 0.333333, 0.666667, 1.0})
