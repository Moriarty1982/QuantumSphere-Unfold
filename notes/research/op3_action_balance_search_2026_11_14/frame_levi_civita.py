"""Erkundung: Levi-Civita auf den Frames. Kreuzprodukt [X_i, X_j]/2 = c_ijk X_k unter zyklischer Rotation des Tupels.
Levi-Civita heisst: c ist unter zyklischer Rotation invariant und unter Vertauschung ungerade."""
import itertools
import numpy as np
R = np.array([[0, -1], [1, 0]], complex); T = np.diag([1, -1]).astype(complex); JB = R @ T
sx = np.array([[0, 1], [1, 0]], complex); sy = np.array([[0, -1j], [1j, 0]]); sz = np.diag([1, -1]).astype(complex)

def consts(trip):
    names, X = zip(*trip); out = {}
    for i, j, k in ((0, 1, 2), (1, 2, 0), (2, 0, 1)):
        C = (X[i] @ X[j] - X[j] @ X[i]) / 2
        c = np.vdot(X[k].flatten(), C.flatten()) / np.vdot(X[k].flatten(), X[k].flatten())
        assert np.allclose(C, c * X[k]); out[f"[{names[i]},{names[j]}]"] = complex(np.round(c, 12))
    return out

print("Frame-Abbildungen (R, T, J_B):", consts([("R", R), ("T", T), ("J_B", JB)]))
print("mit i*R statt R (unabh. i)    :", consts([("iR", 1j * R), ("T", T), ("J_B", JB)]))
print("su(2) (sx, sy, sz)/i zum Vergleich:", consts([("sx/i", sx / 1j), ("sy/i", sy / 1j), ("sz/i", sz / 1j)]))
# reelle Umskalierung kann die Signatur nicht aendern: Killing-Form-Vorzeichen
for lam in itertools.product((1, -1, 2, -0.5), repeat=3):
    c = consts([("a", lam[0] * R), ("b", lam[1] * T), ("c", lam[2] * JB)])
    v = [x.real for x in c.values()]
    assert not (np.allclose(v, v[0]) and abs(v[0]) > 0 and all(abs(x.imag) < 1e-12 for x in c.values())), lam
print("keine reelle Umskalierung macht (R, T, J_B) zyklisch invariant: geprueft (64 Faelle)")
# Oktanten-Tripel bei su(2): +1-Eigenzustaende der drei Achsen, Bahn unter zyklischer Rotation
st = [np.linalg.eigh(A)[1][:, 1] for A in (sx, sy, sz)]
f = np.mean([abs(np.vdot(st[i], st[(i + 1) % 3])) ** 2 for i in range(3)])
b = np.vdot(st[0], st[1]) * np.vdot(st[1], st[2]) * np.vdot(st[2], st[0])
print("su(2)-Achsenzustaende: mittlere Treue", round(f, 12), "K =", round((1 + 2 * f) / 3, 12), "Bargmann/pi =", round(np.angle(b) / np.pi, 12))
w = [np.array(v) for v in ((0.5 * (1 + 1 / 1.8647), 0.5 * (1 - 1 / 1.8647)), (0.5 * (1 - 1 / 1.8647), 0.5 * (1 + 1 / 1.8647)), (0.5, 0.5))]
print("Gewichtsvektoren M, T, P in der (a,b)-Ebene: Rang", np.linalg.matrix_rank(np.array(w)), "(kein 3D-Kreuzprodukt)")
