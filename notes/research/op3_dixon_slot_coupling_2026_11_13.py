"""Erkundung (13.11.2026): Platzkopplung auf dem vollen Dixon-Raum C(x)H(x)O.

Nicht blind, kein Hypothesentest. Prueft die Aussagen der Notiz
op3_dixon_slot_coupling_2026_11_13.md. Aufbau wie k85 (Chiralitaet C,
Ladungen Q8, Q_em, schwacher Isospin durch Rechtsmultiplikation in H).
Aufruf: python op3_dixon_slot_coupling_2026_11_13.py
"""
import os
import sys
import numpy as np
from scipy.linalg import null_space

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "v4_10_0_r32_r33", "llm"))
from k69_test_h17 import omul  # Konvention r04  # noqa: E402

E, E4 = np.eye(8), np.eye(4)
rng = np.random.default_rng(20261113)


def hmul(a, b):
    a0, a1, a2, a3 = a
    b0, b1, b2, b3 = b
    return np.array([a0*b0 - a1*b1 - a2*b2 - a3*b3, a0*b1 + a1*b0 + a2*b3 - a3*b2,
                     a0*b2 - a1*b3 + a2*b0 + a3*b1, a0*b3 + a1*b2 - a2*b1 + a3*b0])


mH = np.array([[hmul(E4[a], E4[b]) for b in range(4)] for a in range(4)])
mO = np.array([[omul(E[i], E[j]) for j in range(8)] for i in range(8)])
mul = lambda x, y: np.einsum('ai,bj,abc,ijk->ck', x, y, mH, mO, optimize=True)   # Dixon-Produkt
sH, sO = np.array([1, -1, -1, -1.]), np.array([1.] + [-1.] * 7)
cjH = lambda x: x * sH[:, None]
cjO = lambda x: x * sO[None, :]
sc = lambda x: x[0, 0]
Fb = lambda x, y, h: sc(mul(mul(cjO(cjH(x)), y), h))     # volle Dixon-Konjugation am ersten Eintrag
Fa = lambda x, y, h: sc(mul(mul(cjH(x), y), h))          # nur Quaternionen-Konjugation
F0 = lambda x, y, h: sc(mul(mul(x, y), h))               # ohne Konjugation

L7 = np.array([omul(E[7], E[j]) for j in range(8)]).T
R7 = np.array([omul(E[j], E[7]) for j in range(8)]).T
Lh = [np.array([hmul(E4[a], E4[j]) for j in range(4)]).T for a in range(4)]
Rh = [np.array([hmul(E4[j], E4[a]) for j in range(4)]).T for a in range(4)]
K, I4, I8, I32 = np.kron, np.eye(4), np.eye(8), np.eye(32)
Q8 = 0.5 * I8 - (1j / 6) * L7 - (1j / 3) * R7
C = 0.5 * (I32 + 1j * K(I4, L7))
N = I32 - C
Qem = -(0.5j) * K(Rh[3], I8) + K(I4, Q8) - 0.5 * I32
w8, V8 = np.linalg.eig(Q8)


def states(proj, qem, q8set):
    cols = np.array([V8[:, i] for i in range(8) if min(abs(w8[i] - q) for q in q8set) < 1e-8]).T
    Vs = np.linalg.qr(cols)[0]
    M = np.vstack([I32 - proj, Qem - qem * I32, I32 - K(I4, Vs @ Vs.conj().T)])
    ns = null_space(M, rcond=1e-9)
    return [ns[:, c].reshape(4, 8) for c in range(ns.shape[1])]


LEP, QRK = (0, 1), (1 / 3, 2 / 3)
SECT = {"e": (states(C, -1, LEP), states(N, 1, LEP)), "nu": (states(C, 0, LEP), states(N, 0, LEP)),
        "u": (states(C, 2 / 3, QRK), states(N, -2 / 3, QRK)), "d": (states(C, -1 / 3, QRK), states(N, 1 / 3, QRK))}


def hel(a, k):
    h = np.zeros((4, 8), complex)
    h[a, k] = 1
    return h


NEUTRAL = [(0, 0), (0, 7), (3, 0), (3, 7)]      # 1(x)1, 1(x)e7, e3(x)1, e3(x)e7
CHARGED = [(1, 0), (1, 7), (2, 0), (2, 7)]
mat = lambda F, s, h, swap=False: np.array([[F(c, p, h) if swap else F(p, c, h) for c in SECT[s][1]] for p in SECT[s][0]])


def kappa_table(F):
    tab = {}
    for s in SECT:
        J = mat(F, s, hel(0, 0))
        if np.linalg.norm(J) < 1e-9:
            tab[s] = None
            continue
        row, res = [], 0.0
        for a, k in NEUTRAL:
            M = mat(F, s, hel(a, k))
            kap = np.vdot(J, M) / np.vdot(J, J)
            res = max(res, np.linalg.norm(M - kap * J))
            row.append(kap)
        tab[s] = (np.array(row), res)
    return tab


def charged_zero(F):
    return max(np.linalg.norm(mat(F, s, hel(a, k))) for s in SECT for a, k in CHARGED)


def mirror_check(F, tab):
    """beta_s(h) = kappa_{s'}(h) mit e <-> u, nu <-> d, fuer zufaellige komplexe neutrale h."""
    err = 0.0
    for _ in range(50):
        c = rng.normal(size=4) + 1j * rng.normal(size=4)
        h = sum(ci * hel(a, k) for ci, (a, k) in zip(c, NEUTRAL))
        for s, sp in (("e", "u"), ("u", "e"), ("nu", "d"), ("d", "nu")):
            J = mat(F, s, hel(0, 0))
            beta = np.vdot(J, mat(F, s, h, swap=True)) / np.vdot(J, J)
            err = max(err, abs(beta - tab[sp][0] @ c))
    return err


def no_cyclic_spinor_form():
    """Trilineare Formen auf H^3, invariant unter gemeinsamer Linksmultiplikation: Dimension."""
    rows = []
    for a in (1, 2, 3):
        A = Lh[a]
        rows.append(K(K(A.T, I4), I4) + K(K(I4, A.T), I4) + K(K(I4, I4), A.T))
    return null_space(np.vstack(rows), rcond=1e-10).shape[1]


if __name__ == "__main__":
    for name, F in (("F0 ohne Konjugation", F0), ("Fa nur H-Konjugation", Fa), ("Fb volle Konjugation", Fb)):
        tab = kappa_table(F)
        print(f"{name}: geladene h tragen {charged_zero(F):.1e} bei" if name.startswith("Fb") else name + ":")
        for s, v in tab.items():
            print(f"   {s:3s}", "null" if v is None else f"kappa(1x1, 1xe7, e3x1, e3xe7) = {np.round(v[0], 6)}  Rest {v[1]:.0e}")
    tab = kappa_table(Fb)
    sig = {"e": 1, "nu": -1, "u": -1, "d": 1}
    lam = {"e": 1, "nu": 1, "u": -1, "d": -1}
    err = max(abs(tab[s][0] - np.array([1, 1j * lam[s], 1j * sig[s], -sig[s] * lam[s]])).max() for s in SECT)
    print(f"Fb: kappa_s = (a0 + i sigma a3)(o0 + i lambda o7), Fehler {err:.1e}")
    print(f"Fb: Spiegelung beta_s(h) = kappa_s'(h), e<->u, nu<->d: Fehler {mirror_check(Fb, tab):.1e}")
    print(f"Invariante trilineare Formen auf H^3 unter gemeinsamer Linksdrehung: Dimension {no_cyclic_spinor_form()}")
