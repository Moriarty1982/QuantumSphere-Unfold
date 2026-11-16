"""k233: Test H111 (Vorab-Notiz Vorab_Notiz_H111_Zeitoktant_durch_Frames.md).

Zeit-Oktant: g_l bei theta = arccos(1/sqrt3) um +-z, Azimut phi0 + 120 l; phi0 in {30, 90} Grad.
Frame-Oktant: e_R, e_T, e_J = +1-Eigenzustaende von sigma_z, sigma_x, sigma_y.
Kreuz-Gram A_kl = <e_k|g_l>; sqrt m := Singulaerwerte; K = sum s^2 / (sum s)^2; 3 delta aus der Fourier-Zerlegung.
Treffer: |K - 2/3| <= 1e-3 und |3 delta - 0.666674| <= 2e-4.
"""
import numpy as np

TARGET, TOL, KTOL = 0.666674, 2e-4, 1e-3


def coh(n):
    n = np.asarray(n, float) / np.linalg.norm(n)
    th, ph = np.arccos(np.clip(n[2], -1, 1)), np.arctan2(n[1], n[0])
    return np.array([np.cos(th / 2), np.exp(1j * ph) * np.sin(th / 2)])


def koide(sv):
    r = np.sort(np.asarray(sv, float))
    K = np.sum(r ** 2) / np.sum(r) ** 2
    F = np.fft.fft(r) / 3
    d = abs(np.angle(F[1])) % (2 * np.pi / 3)
    d = min(d, 2 * np.pi / 3 - d)
    return K, 3 * d


E = [coh([0, 0, 1]), coh([1, 0, 0]), coh([0, 1, 0])]
th = np.arccos(1 / np.sqrt(3))

# Kontrolle: Frame-Oktant gegen sich selbst
A0 = np.array([[np.vdot(a, b) for b in E] for a in E])
print("Kontrolle (Frame-Oktant gegen sich selbst): K = %.6f, 3 delta = %.6f" % koide(np.linalg.svd(A0, compute_uv=False)))

hits, attempts = [], 0
for axis in (+1, -1):
    for phi0 in (30, 90):
        g = []
        for l in range(3):
            ph = np.radians(phi0 + 120 * l)
            n = np.array([np.sin(th) * np.cos(ph), np.sin(th) * np.sin(ph), axis * np.cos(th)])
            g.append(coh(n))
        A = np.array([[np.vdot(e, x) for x in g] for e in E])
        sv = np.linalg.svd(A, compute_uv=False)
        K, ph3 = koide(sv); attempts += 1
        ok = abs(K - 2 / 3) <= KTOL and abs(ph3 - TARGET) <= TOL
        name = f"Achse {'+z' if axis > 0 else '-z'}, phi0 = {phi0}"
        if ok: hits.append(name)
        print(f"{name}: Singulaerwerte {np.round(np.sort(sv), 6)}, K = {K:.6f}, 3 delta = {ph3:.6f}, 3 delta - Ziel = {ph3 - TARGET:+.6f}"
              + ("  -> TREFFER" if ok else ""))
verdict = "bestaetigt" if len(hits) == 1 else ("mehrdeutig" if hits else "widerlegt")
print(f"Versuche: {attempts}; Treffer: {hits}; Urteil: {verdict}")
