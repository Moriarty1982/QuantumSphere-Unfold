"""Erkundung (13.11.2026): eichinvariante Dreifachauslesung als Eigenwerte der Platz-Gram-Matrix.

Nicht blind, kein Hypothesentest. Prueft die Aussagen der Notiz
op3_gram_eigen_readout_2026_11_13.md.
Aufruf: python op3_gram_eigen_readout_2026_11_13.py
"""
import os
import sys
import numpy as np
from scipy.linalg import expm

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import op3_dixon_slot_coupling_2026_11_13 as D  # noqa: E402

K, I4, I8, I32, C, N, omul, E = D.K, D.I4, D.I8, D.I32, D.C, D.N, D.omul, D.E
rng = np.random.default_rng(20261113)
unit = lambda v: v / np.linalg.norm(v)


def brannen(S):
    c = np.array([S[0, 1], S[0, 2], S[1, 2]])
    rho = np.sqrt((c ** 2).sum() / 3)
    cos3 = np.prod(c) / rho ** 3
    th = np.arccos(np.clip(cos3, -1, 1)) / 3
    return rho, cos3, np.sort(1 + 2 * rho * np.cos(th + 2 * np.pi * np.arange(3) / 3))


def check_formula(n=8, trials=2000):
    err = errK = 0.0
    for _ in range(trials):
        X = np.array([unit(rng.normal(size=n)) for _ in range(3)])
        S = X @ X.T
        rho, cos3, s = brannen(S)
        ev = np.sort(np.linalg.eigvalsh(S))
        err = max(err, abs(ev - s).max())
        errK = max(errK, abs((ev ** 2).sum() / 9 - (1 + 2 * rho ** 2) / 3),
                   abs(np.linalg.det(S) - (1 - 3 * rho ** 2 + 2 * rho ** 3 * cos3)))
    return err, errK


def mean_K(n, trials=200000):
    X = rng.normal(size=(trials, 3, n))
    X /= np.linalg.norm(X, axis=2, keepdims=True)
    S = X @ X.transpose(0, 2, 1)
    c2 = S[:, 0, 1] ** 2 + S[:, 0, 2] ** 2 + S[:, 1, 2] ** 2
    Kv = (1 + 2 * c2 / 3) / 3
    return Kv.mean(), Kv.std() / np.sqrt(trials)


def gauge_invariance():
    """Hermitesche Gram-Matrix dreier Zustaende in C(x)H(x)O unter den Eichwirkungen."""
    psi = rng.normal(size=(3, 32)) + 1j * rng.normal(size=(3, 32))
    ev0 = np.linalg.eigvalsh(psi.conj() @ psi.T)
    Tw = [-(0.5j) * K(D.Rh[a], I8) for a in (1, 2, 3)]
    gens = {"Lorentz-Drehung": -(0.5j) * K(D.Lh[1], I8), "Q_em": D.Qem, "schwach T'_1": C @ Tw[0],
            "Y/2": K(I4, D.Q8) - 0.5 * I32 + N @ Tw[2], "Lorentz-Boost": 0.5 * K(D.Lh[1], I8)}
    out = {}
    for name, G in gens.items():
        U = expm(0.7j * G)
        p1 = psi @ U.T
        out[name] = abs(np.linalg.eigvalsh(p1.conj() @ p1.T) - ev0).max() / ev0.max()
    return out


def hopf_carrier(trials=200000):
    """r15: Einheitsoktonionen a, b, c mit (ab)c = 1; Bereich von K = (1 + 2 rho^2)/3."""
    Ks, dets = [], []
    for _ in range(trials):
        a, b = unit(rng.normal(size=8)), unit(rng.normal(size=8))
        ab = omul(a, b)
        c = ab * D.sO                      # c = conj(ab), dann (ab)c = 1
        X = np.array([a, b, c])
        S = X @ X.T
        Ks.append((1 + 2 * (S[0, 1] ** 2 + S[0, 2] ** 2 + S[1, 2] ** 2) / 3) / 3)
        dets.append(np.linalg.det(S))
    Ks = np.array(Ks)
    al = rng.uniform(0, 2 * np.pi, (trials, 2))
    a3 = -al.sum(1)
    c2 = np.cos(al[:, 0] - al[:, 1]) ** 2 + np.cos(al[:, 0] - a3) ** 2 + np.cos(al[:, 1] - a3) ** 2
    Kt = (1 + 2 * c2 / 3) / 3
    return (Ks.min(), Ks.max(), Ks.mean()), (Kt.min(), Kt.max(), Kt.mean())


if __name__ == "__main__":
    err, errK = check_formula()
    print(f"Eigenwerte der Gram-Matrix dreier Einheitsvektoren = 1 + 2 rho cos(theta + 2 pi k/3): Fehler {err:.1e};"
          f" K und det: {errK:.1e}")
    for n in (2, 4, 6, 8):
        m, se = mean_K(n)
        print(f"  Mittel von K ueber zufaellige Einheitsvektoren im R^{n}: {m:.5f} +- {se:.5f}; (1 + 2/n)/3 = {(1 + 2 / n) / 3:.5f}")
    rho = 1 / np.sqrt(2)
    print(f"Koide (rho^2 = 1/2): det S = -1/2 + cos(3 theta)/sqrt2 >= 0  <=>  |theta| <= pi/12 = {np.pi / 12:.6f};"
          f" am Rand Eigenwerte {np.round(1 + 2 * rho * np.cos(np.pi / 12 + 2 * np.pi * np.arange(3) / 3), 4)}")
    m = np.sqrt(np.array([0.51099895, 105.6583755, 1776.86]))
    s = 3 * m / m.sum()
    print(f"Leptonen als Eigenwerte gelesen (nachtraeglich): rho^2 = {((s - 1) ** 2).sum() / 6:.6f}, det S = {np.prod(s):.5f}")
    for name, v in gauge_invariance().items():
        print(f"  hermitesche Gram-Eigenwerte unter {name}: relative Aenderung {v:.1e}")
    full, torus = hopf_carrier()
    print(f"Hopf-Traeger (ab)c = 1, allgemein: K von {full[0]:.4f} bis {full[1]:.4f}, Mittel {full[2]:.4f}")
    print(f"Hopf-Traeger, farbfester Torus:    K von {torus[0]:.4f} bis {torus[1]:.4f}, Mittel {torus[2]:.4f}")
