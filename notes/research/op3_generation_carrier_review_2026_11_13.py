"""Erkundung (13.11.2026): Gram-Labels aus r33 unter den heutigen Eichwirkungen.

Nicht blind, kein Hypothesentest. Prueft die Aussagen der Notiz
op3_generation_carrier_review_2026_11_13.md. Aufbau wie k85.
Aufruf: python op3_generation_carrier_review_2026_11_13.py
"""
import os
import sys
import numpy as np
from scipy.linalg import expm

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import op3_dixon_slot_coupling_2026_11_13 as D  # noqa: E402

K, I4, I8, I32, C, N = D.K, D.I4, D.I8, D.I32, D.C, D.N
rng = np.random.default_rng(20261113)


def label_matrix(x):
    """N_ij = sum_cd (A_i)_cd (A_j)_cd mit G_cd = conj(h_c) h_d, h_c die Quaternionenspalten (r33)."""
    G = np.einsum('ac,bd,abe->ecd', x * D.sH[:, None], x, D.mH)
    A = G[1:]
    return np.einsum('icd,jcd->ij', A, A)


def encode(xs):
    """E(x) = i (x) x1 + j (x) x2 + k (x) x3."""
    x = np.zeros((4, 8), complex)
    x[1:] = xs
    return x


Tw = [-(0.5j) * K(D.Rh[a], I8) for a in (1, 2, 3)]
Y2 = K(I4, D.Q8) - 0.5 * I32 + N @ Tw[2]
GENS = {"Lorentz-Drehung": -(0.5j) * K(D.Lh[1], I8), "Lorentz-Boost": 0.5 * K(D.Lh[1], I8),
        "Q_em": D.Qem, "schwach T'_1": C @ Tw[0], "schwach T'_3": C @ Tw[2], "Y/2": Y2}
inv = lambda M: np.array([np.trace(M), np.trace(M @ M), np.linalg.det(M)])

if __name__ == "__main__":
    xs = rng.normal(size=(3, 8))
    x0 = encode(xs)
    N0 = label_matrix(x0)
    S = xs @ xs.T
    print(f"N = 2 adj(S), S die Gram-Matrix der drei Plaetze: Fehler {abs(N0 - 2 * np.linalg.det(S) * np.linalg.inv(S)).max():.1e}")
    for name, G in GENS.items():
        N1 = label_matrix((expm(0.7j * G) @ x0.ravel()).reshape(4, 8))
        d_mu = abs(np.diag(N1) - np.diag(N0)) / abs(np.diag(N0)).max()
        d_inv = (abs(inv(N1) - inv(N0)) / abs(inv(N0))).max()
        print(f"  {name:16s} relative Aenderung der Labels mu_1..3: {np.round(d_mu, 3)}; der Invarianten von N: {d_inv:.1e}")
    # Q_em dreht die Quaternionenrichtungen i und j ineinander, k bleibt
    U = expm(0.7j * D.Qem)
    for a, nm in ((1, "i"), (2, "j"), (3, "k")):
        v = D.hel(a, 0)
        w = (U @ v.ravel()).reshape(4, 8)
        print(f"  Q_em-Drehung von {nm}(x)1: Betraege der Anteile an 1, i, j, k: {np.round(np.abs(w[:, 0]) , 3)}")
    al = rng.uniform(0, 2 * np.pi, 3)
    xs2 = np.array([np.cos(a) * D.E[0] + np.sin(a) * D.E[7] for a in al])
    N2 = label_matrix(encode(xs2)).real
    print(f"Farbfeste Ebene span(1, e7): Labels mu = {np.round(np.diag(N2), 4)}, Eigenwerte von N = {np.round(np.linalg.eigvalsh(N2), 4)}")
