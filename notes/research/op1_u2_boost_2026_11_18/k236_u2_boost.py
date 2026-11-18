"""k236: OP1, U2 unter Lesart (B) (Methoden_Notiz.md, Commit 4ee7618). Erkundung, nicht blind.

Boost entlang der Normalen in der SL(2,C)-Hauptreihe (k, rho); Verbleib eines Zustands |k, m> im Block j = k.
"""
import numpy as np
from scipy.linalg import expm

GAMMA = 0.237533
ETA_M = np.arctanh(0.549412)


def k3_block(k, rho, m, jmax):
    js = np.arange(k, jmax + 1e-9, 1.0)
    js = js[js >= abs(m) - 1e-9]
    n = len(js)
    K = np.zeros((n, n), complex)
    for a, j in enumerate(js):
        K[a, a] = k * rho * m / (j * (j + 1))
        if a + 1 < n:  # Kopplung j -> j+1 mit -alpha_{j+1} sqrt((j+1)^2 - m^2)
            jp = j + 1
            alpha = 1j / jp * np.sqrt((jp ** 2 - k ** 2) * (jp ** 2 + rho ** 2) / (4 * jp ** 2 - 1))
            K[a + 1, a] = -alpha * np.sqrt(jp ** 2 - m ** 2)
            K[a, a + 1] = np.conj(K[a + 1, a])
    assert np.allclose(K, K.conj().T)
    return js, K


def stay(k, rho, m, eta, extra):
    js, K = k3_block(k, rho, m, k + extra)
    U = expm(-1j * eta * K)
    return abs(U[0, 0]) ** 2, js, K


def dispersion(k, rho, m):
    js, K = k3_block(k, rho, m, k + 4)
    v = np.zeros(len(js)); v[0] = 1
    A = K - GAMMA * m * np.eye(len(js))
    return float(np.real(v @ A.conj().T @ A @ v))


ok_scharf = True; gegen = False
for label, rhof in (("rho = gamma(k+1)", lambda k: GAMMA * (k + 1)), ("rho = gamma k (EPRL)", lambda k: GAMMA * k)):
    print(f"\n=== {label}, gamma = {GAMMA}")
    for eta in (0.2, ETA_M, 1.5):
        print(f"-- eta = {eta:.4f}")
        for k in np.arange(0.5, 3.01, 0.5):
            rho = rhof(k)
            ms = np.arange(-k, k + 1e-9, 1.0)
            P = []
            for m in ms:
                p60, _, _ = stay(k, rho, m, eta, 60)
                p120, _, _ = stay(k, rho, m, eta, 120)
                assert abs(p60 - p120) < 1e-9, (k, m, p60, p120)
                P.append(p60)
            P = np.array(P); ext = np.isclose(abs(ms), k)
            D = [dispersion(k, rho, m) for m in ms]
            line = "  ".join(f"m={m:+.1f}: P {p:.3f} D {d:.3f}" for m, p, d in zip(ms, P, D) if m >= 0)
            print(f"k={k:.1f}: {line}")
            if abs(eta - ETA_M) < 1e-12 and label.startswith("rho = gamma(k+1)"):
                if not (np.all(P[ext] >= 0.9) and (np.all(P[~ext] <= 0.5) if (~ext).any() else True)):
                    ok_scharf = False
                if (~ext).any() and P[~ext].max() > P[ext].min() + 1e-12:
                    gegen = True
            if abs(eta - ETA_M) < 1e-12 and (~ext).any():
                print(f"        Abstand P(extrem) - max P(|m|<k) = {P[ext].min() - P[~ext].max():+.4f}")
print("\nLesart bei eta_M (rho = gamma(k+1)):", "GEGEN U2" if gegen else ("SCHARF" if ok_scharf else "GRADUELL"))
