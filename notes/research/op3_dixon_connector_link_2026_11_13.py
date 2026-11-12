"""Erkundung (13.11.2026): Anbindung der Dixon-Platzkopplung an die Verbinder aus r44.1(b).

Nicht blind, kein Hypothesentest. Prueft den Nachtrag der Notiz
op3_dixon_slot_coupling_2026_11_13.md.
Aufruf: python op3_dixon_connector_link_2026_11_13.py
"""
import os
import sys
import numpy as np
from scipy.linalg import null_space

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import op3_dixon_slot_coupling_2026_11_13 as D  # noqa: E402

K, I4, I8, I32, C, N = D.K, D.I4, D.I8, D.I32, D.C, D.N
omul, E = D.omul, D.E

# Farb-su(3) wie in k85: Derivationen von O, die e7 festhalten
rows = []
for i in range(8):
    for j in range(8):
        p = omul(E[i], E[j]); A = np.zeros((8, 64))
        for k in range(8):
            for m in range(8):
                A[k, 8*k + m] += p[m]
                A[:, 8*k + m] -= omul(E[k], E[j]) * E[i][m]
                A[:, 8*k + m] -= omul(E[i], E[k]) * E[j][m]
        rows.append(A)
Der = null_space(np.vstack(rows))
Ds = [Der[:, c].reshape(8, 8) for c in range(Der.shape[1])]
S = null_space(np.array([Dm[:, 7] for Dm in Ds]).T)
su3 = [sum(S[k, c] * Ds[k] for k in range(len(Ds))) for c in range(S.shape[1])]

Tw = [-(0.5j) * K(D.Rh[a], I8) for a in (1, 2, 3)]
Q = K(I4, D.Q8)
Tp = [C @ t for t in Tw]
Y2 = Q - 0.5 * I32 + N @ Tw[2]
Qem = D.Qem
basis = [np.eye(32)[i].reshape(4, 8).astype(complex) for i in range(32)]


def form_matrix(h):
    """G mit F_b(x, y, h) = x^T G y."""
    return np.array([[D.Fb(bx, by, h) for by in basis] for bx in basis])


def connector(h):
    """Antilinearer Verbinder Phi = X o T, Kern -> Bild, zu F_b(., ., h)."""
    return C @ form_matrix(h).conj() @ C


def ad(G, X):
    return G @ X + X @ G.conj()


def charge(G, X):
    Y = ad(G, X)
    q = np.vdot(X, Y) / np.vdot(X, X)
    return q.real, np.linalg.norm(Y - q * X)


if __name__ == "__main__":
    hs = [D.hel(a, k) for a in range(4) for k in (0, 7)]
    Xs = [connector(h) for h in hs]
    comm = max(np.linalg.norm(A @ X - X @ A) for X in Xs
               for A in [K(I4, s) for s in su3] + [K(D.Lh[a], I8) for a in (1, 2, 3)])
    rank = np.linalg.matrix_rank(np.column_stack([X.ravel() for X in Xs]), 1e-9)
    print(f"Verbinder aus F_b: vertauschen mit Farbe und Lorentz-Drehungen (Rest {comm:.1e}); Rang ueber die 8 Elemente h: {rank}")

    e3, e7 = 3, 7
    def idem(sig, lam):       # (1 - i sig e3) (x) (1 - i lam e7)
        h = np.zeros((4, 8), complex)
        h[0, 0], h[0, e7], h[e3, 0], h[e3, e7] = 1, -1j * lam, -1j * sig, -sig * lam
        return h
    names = {(1, 1): "e", (-1, 1): "nu", (-1, -1): "u", (1, -1): "d"}
    for (sig, lam), s in names.items():
        h = idem(sig, lam)
        norms = {t: np.linalg.norm(D.mat(D.Fb, t, h)) for t in D.SECT}
        X = connector(h)
        qy, ry = charge(Y2, X); qq, rq = charge(Qem, X)
        cas = sum(ad(t, ad(t, X)) for t in Tp)
        qc = (np.vdot(X, cas) / np.vdot(X, X)).real
        print(f"h = (1 {'-' if sig > 0 else '+'} i e3)(x)(1 {'-' if lam > 0 else '+'} i e7): koppelt nur {s}: "
              + ", ".join(f"{t} {v:.1e}" for t, v in norms.items())
              + f"; Verbinder: Casimir {qc:.2f}, Y/2 = {qy:+.2f} (Rest {ry:.0e}), Q_em = {qq:+.2f} (Rest {rq:.0e})")

    # Hyperladung: Phase der Terme alpha_s (Koeffizient c_s) und beta_s (Koeffizient c_s', s' gespiegelt)
    th = 0.37
    w, V = np.linalg.eig(Y2)
    U = V @ np.diag(np.exp(1j * th * w)) @ np.linalg.inv(V)
    act = lambda x: (U @ x.ravel()).reshape(4, 8)
    mirror = {"e": "u", "u": "e", "nu": "d", "d": "nu"}
    hs_ = {s_: idem(sig, lam) for (sig, lam), s_ in names.items()}
    ph = {}
    for s_ in D.SECT:
        psi, chi = D.SECT[s_]
        pair = max(((p_, c_) for p_ in psi for c_ in chi), key=lambda pc: abs(D.Fb(pc[0], pc[1], hs_[s_])))
        al0, al1 = D.Fb(pair[0], pair[1], hs_[s_]), D.Fb(act(pair[0]), act(pair[1]), hs_[s_])
        be0 = D.Fb(pair[1], pair[0], hs_[mirror[s_]]); be1 = D.Fb(act(pair[1]), act(pair[0]), hs_[mirror[s_]])
        ph[s_] = (np.angle(al1 / al0) / th, np.angle(be1 / be0) / th)
    print("Hyperladungsphase der Terme (Einheit theta): " + "; ".join(
        f"alpha_{s_} {v[0]:+.2f}, beta_{s_} {v[1]:+.2f}" for s_, v in ph.items()))
    print("  alpha_u und beta_e haengen am selben Koeffizienten c_u, verlangen aber entgegengesetzte Phasen:",
          f"{-ph['u'][0]:+.2f} gegen {-ph['e'][1]:+.2f}")

    # Nur ein Umlaufsinn: M = a + alpha P
    rng = np.random.default_rng(5)
    Kroot = Klin = 0.0
    for _ in range(200000):
        a_, al_ = rng.normal() + 1j * rng.normal(), rng.normal() + 1j * rng.normal()
        sv = np.abs(a_ + al_ * np.exp(2j * np.pi * np.arange(3) / 3))
        Kroot = max(Kroot, (sv ** 2).sum() / sv.sum() ** 2)        # Singulaerwert = Wurzel der Masse
        Klin = max(Klin, sv.sum() / np.sqrt(sv).sum() ** 2)        # Singulaerwert = Masse
    print(f"Ein Umlaufsinn, M = a + alpha P: groesstes K bei 200000 Zufallspunkten: Wurzel-Lesart {Kroot:.4f}, Massen-Lesart {Klin:.4f}")
    sv = np.sort(np.abs(1 + np.exp(2j * np.pi * np.arange(3) / 3)))
    print(f"  ein gemeinsames Element (a = alpha): Singulaerwerte im Verhaeltnis {np.round(sv / sv[0], 6)}")
