"""Erkundung (nicht blind, nachtraeglich zu H103): warum i R_f auf dem neutralen Qubit N den magischen Winkel trifft.

Prueft: (1) R_u (u in Im H_n) laesst N invariant, L_e7/L_e15 fuehren heraus, L_e8 ist auf N skalar;
(2) i R_e7, i R_e15, i R_e8 sind auf N ein Pauli-Tripel (e8 = psi-Achse);
(3) alle acht Vorzeichen-Diagonalen geben c = 1/sqrt3; allgemein c = |<u, e8>| fuer Einheitsvektoren u in Im H_n.
Aufruf: python op3_rf_reference_2026_11_14.py
"""
import importlib.util
import itertools
import os
import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
spec = importlib.util.spec_from_file_location("k225", os.path.join(HERE, "predictions", "k225_test_h103.py"))
k = importlib.util.module_from_spec(spec)
spec.loader.exec_module(k)
B, R, L, su, c_op = k.B, k.R, k.L, k.su, k.c_op
rng = np.random.default_rng(1114)

if __name__ == "__main__":
    PN = B @ B.conj().T
    for u in (7, 8, 15):
        Ru, Lu = R(su(u)).astype(complex), L(su(u)).astype(complex)
        print(f"(1) e{u}: R_u laesst N invariant {np.allclose(PN @ Ru @ B, Ru @ B)}; L_u laesst N invariant "
              f"{np.allclose(PN @ Lu @ B, Lu @ B)}; L_u auf N {np.round(B.conj().T @ Lu @ B, 6).tolist()}")
    S = [B.conj().T @ (1j * R(su(u))).astype(complex) @ B for u in (7, 15, 8)]
    sq = all(np.allclose(s @ s, np.eye(2)) for s in S)
    anti = all(np.allclose(S[i] @ S[j] + S[j] @ S[i], 0) for i, j in ((0, 1), (0, 2), (1, 2)))
    print(f"(2) Pauli-Tripel: Quadrate 1 {sq}, Antikommutatoren 0 {anti}; i R_e8 diagonal (psi-Achse) {np.allclose(S[2], np.diag(np.diag(S[2])))}")
    cs = []
    for s in itertools.product((1, -1), repeat=3):
        f = (s[0] * su(7) + s[1] * su(8) + s[2] * su(15)) / np.sqrt(3)
        cs.append(c_op(1j * R(f)))
    print(f"(3) acht Diagonalen: c = {sorted(set(round(float(c), 10) for c in cs))} (1/sqrt3 = {1 / np.sqrt(3):.10f})")
    err = 0
    for _ in range(200):
        v = rng.normal(size=3); v /= np.linalg.norm(v)
        u = v[0] * su(7) + v[1] * su(8) + v[2] * su(15)
        err = max(err, abs(c_op(1j * R(u)) - abs(v[1])))
    print(f"    zufaellige u in Im H_n: max |c - |<u,e8>|| = {err:.1e}")
