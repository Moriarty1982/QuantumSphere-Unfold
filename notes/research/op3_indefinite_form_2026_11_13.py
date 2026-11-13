"""Erkundung (13.11.2026): Lorentz-invariante bilineare Form und Vorzeichen der Gram-Eigenwerte.

Nicht blind, kein Hypothesentest; rechnet keine Neutrinomassen.
Prueft die Aussagen der Notiz op3_indefinite_form_2026_11_13.md.
Aufruf: python op3_indefinite_form_2026_11_13.py
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

if __name__ == "__main__":
    # (1) Lesart B: z = E + iB in C^3, s(z) = sum z_k^2; Re s = E^2 - B^2 hat Signatur (3,3)
    sig = np.linalg.eigvalsh(np.diag([1, 1, 1, -1, -1, -1.]))
    print(f"Re s auf R^6: Signatur ({(sig > 0).sum()}, {(sig < 0).sum()}); Triole z = c(1, w, w^2): s = "
          f"{abs(sum((np.exp(2j * np.pi * k / 3)) ** 2 for k in range(3))):.1e}; s(iz) = -s(z)")

    # (2) Dixon-Raum: bilineare Gram-Matrix dreier Zustaende, Eigenwerte unter den Wirkungen
    Tw = [-(0.5j) * K(D.Rh[a], I8) for a in (1, 2, 3)]
    gens = {"Lorentz-Drehung": -(0.5j) * K(D.Lh[1], I8), "Lorentz-Boost": 0.5 * K(D.Lh[1], I8),
            "Q_em": D.Qem, "Y/2": K(I4, D.Q8) - 0.5 * I32 + N @ Tw[2]}
    psi = rng.normal(size=(3, 32)) + 1j * rng.normal(size=(3, 32))
    ev = lambda p: np.sort_complex(np.linalg.eigvals(p @ p.T))
    e0 = ev(psi)
    for name, G in gens.items():
        p1 = psi @ expm(0.7j * G).T
        print(f"  bilineare Gram-Eigenwerte unter {name:16s}: relative Aenderung {abs(ev(p1) - e0).max() / abs(e0).max():.1e}")
    # Q_em ist i mal eine reelle antisymmetrische Matrix: die Ladung wirkt als reelle Drehung
    print(f"  Q_em + Q_em^T = {abs(D.Qem + D.Qem.T).max():.1e} (Ladung paart +q mit -q)")
    w, V = np.linalg.eig(D.Qem)
    for q, name in ((-1, "geladene Leptonen/Zustaende mit Q = -1"), (0, "neutrale Zustaende")):
        sub = V[:, abs(w - q) < 1e-8]
        pn = (rng.normal(size=(3, sub.shape[1])) + 1j * rng.normal(size=(3, sub.shape[1]))) @ sub.T
        print(f"  bilineare Gram-Matrix auf {name} (Dimension {sub.shape[1]}): Norm {np.linalg.norm(pn @ pn.T):.2e}")

    # (3) Drei reelle Einheitsvektoren (Norm +1) in einem Raum der Signatur (2,1): ein Eigenwert negativ moeglich
    eta = np.diag([1, 1, -1.])
    cnt = {(3, 0): 0, (2, 1): 0}
    for _ in range(20000):
        X = rng.normal(size=(3, 3))
        nrm = np.einsum('ai,ij,aj->a', X, eta, X)
        if (nrm <= 0).any():
            continue
        X /= np.sqrt(nrm)[:, None]
        S = X @ eta @ X.T
        e = np.linalg.eigvalsh(S)
        rho2 = (S[0, 1] ** 2 + S[0, 2] ** 2 + S[1, 2] ** 2) / 3
        assert abs((e ** 2).sum() / 9 - (1 + 2 * rho2) / 3) < 1e-9
        cnt[((e > 0).sum(), (e < 0).sum())] = cnt.get(((e > 0).sum(), (e < 0).sum()), 0) + 1
    print(f"Raumartige Einheitsvektoren in Signatur (2,1): Vorzeichenmuster der Eigenwerte {cnt}; K = (1 + 2 rho^2)/3 gilt weiter")
    print(f"Bei rho^2 = 1/2: det S = -1/2 + cos(3 theta)/sqrt2 < 0 genau fuer |theta| > pi/12 = {np.pi / 12:.6f}")
