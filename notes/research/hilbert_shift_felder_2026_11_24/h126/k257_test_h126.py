"""k257: Test H126 nach Vorab-Notiz (notes/research/predictions/Vorab_Notiz_H126_Kopplung_zweier_Richtungen.md, Commit 0a1bd3aa).
Aufruf aus diesem Ordner (liest ../k253_cayley_dickson_turm.py)."""
import numpy as np
src = open("../k253_cayley_dickson_turm.py").read().split("for n in range(0, 6):")[0]
ns = {}; exec(src, ns); mul = ns["mul"]
N = 16; E = np.eye(N)
Lb = np.array([np.array([mul(E[i], e) for e in E]).T for i in range(N)])  # L_{e_i}
def L(x): return np.tensordot(x, Lb, 1)
def conj(x): y = -x.copy(); y[0] = x[0]; return y
def tensf(X7, th):  # X in Im O (7 Komponenten, Index 1..7), f = (cos th, sin th)
    v = np.zeros(N); v[1:8] = np.cos(th) * X7; v[9:16] = np.sin(th) * X7; return v
TH = [0, 2 * np.pi / 3, 4 * np.pi / 3]
e1 = np.zeros(7); e1[0] = 1; e2 = np.zeros(7); e2[1] = 1
G = [E[0] / np.sqrt(3) + np.sqrt(2 / 3) * tensf(e1, t) for t in TH]
Lgc = [L(conj(g)) for g in G]
def M_of(chi, dnu, assoz=False):
    wn = np.cos(chi) * e1 + np.sin(chi) * e2
    Psi = (E[0] + tensf(wn, dnu)) / np.sqrt(2)
    LP = L(Psi)
    Op = L(mul(Psi, Psi)) if assoz else LP @ LP
    M = np.zeros((3, 3), complex)
    for k in range(3):
        y = Op @ G[k]
        for j in range(3):
            z = Lgc[j] @ y
            M[j, k] = z[0] + 1j * z[8]
    return M
def U_of(M):
    H = M @ M.conj().T; ev, V = np.linalg.eigh(H); return ev, V
# delta_e aus PDG-2024-Massen
m = np.array([0.51099895, 105.6583755, 1776.93]); r = np.sqrt(m) / np.sqrt(m).sum() * 3  # r_k = 1 + sqrt2 cos(...)
def fit_de(s):
    best = None
    for de in np.linspace(0, 2 * np.pi, 200001):
        c = 1 + np.sqrt(2) * np.cos(de - s * np.array(TH))
        srt = np.sort(c); err = np.sum((srt - r) ** 2)
        if best is None or err < best[0]: best = (err, de, c)
    return best
NU = dict(s12=(0.308, 0.012, 0.011), s13=(0.02215, 0.00056, 0.00058), s23=(0.470, 0.017, 0.013), d=(212.0, 26.0, 41.0))
def obs(U):
    P = np.abs(U) ** 2; s13 = P[0, 2]; c13 = 1 - s13
    s12 = P[0, 1] / c13; s23 = P[1, 2] / c13
    J = np.imag(U[0, 0] * U[1, 1] * np.conj(U[0, 1]) * np.conj(U[1, 0]))
    S12, C12, S23, C23, S13 = np.sqrt(s12), np.sqrt(1 - s12), np.sqrt(s23), np.sqrt(1 - s23), np.sqrt(s13)
    den = 2 * S12 * C12 * S23 * C23 * S13
    cosd = (P[1, 0] - s12 * (1 - s23) - (1 - s12) * s23 * s13) / den if den > 1e-12 else 0.0
    sind = J / (den / 2 * c13) if den > 1e-12 else 0.0
    d = np.rad2deg(np.arctan2(sind, np.clip(cosd, -1, 1))) % 360
    return s12, s13, s23, d
def chi2(o):
    t = 0
    for (k, (c, up, lo)), v in zip(NU.items(), o):
        dv = v - c
        if k == "d": dv = (dv + 180) % 360 - 180
        t += (dv / (up if dv > 0 else lo)) ** 2
    return t
def eval_point(chi, dnu, rows):
    M = M_of(chi, dnu); ev, V = U_of(M); U = V[rows, :]
    o = list(obs(U)); best = None
    for dsign in (1, -1):  # i <-> -i
        oo = o[:3] + [o[3] if dsign == 1 else (360 - o[3]) % 360]
        c = chi2(oo)
        if best is None or c < best[0]: best = (c, oo)
    return best, ev
print("=== delta_e-Anpassung ===")
fits = {}
for s in (1, -1):
    err, de, c = fit_de(s); rows = list(np.argsort(c))  # Kopien nach aufsteigender Amplitude -> e, mu, tau
    fits[s] = rows
    print(f"Orientierung {s:+d}: delta_e = {de:.6f} rad, Restfehler {err:.2e}, Zeilen (e,mu,tau) = Kopien {rows}")
print("=== Stufe A ===")
chis = np.deg2rad(np.arange(0, 180.01, 0.5)); dnus = np.deg2rad(np.arange(0, 360, 0.5))
deg = 0; nonas = []; tot = 0
for chi in chis[::4]:
    for dnu in dnus[::4]:
        M = M_of(chi, dnu); ev, _ = U_of(M); tot += 1
        if np.min(np.diff(ev)) < 1e-9: deg += 1
        nonas.append(np.linalg.norm(M - M_of(chi, dnu, True)) / max(np.linalg.norm(M), 1e-15))
print(f"A1: entartete Punkte {deg}/{tot} ({deg / tot:.3f})")
nonas = np.array(nonas); print(f"A3: ||M - M_assoz||/||M|| min {nonas.min():.3e}, Median {np.median(nonas):.3e}, max {nonas.max():.3e}")
for c in (0.0, np.pi):
    for dnu in (0.0, np.deg2rad(45)):
        M = M_of(c, dnu); ev, V = U_of(M)
        print(f"A2: chi={np.rad2deg(c):.0f}, dnu={np.rad2deg(dnu):.0f}: Eigenwerte {np.round(ev, 6)}, |U|^2 (Kopienzeilen) = {np.round(np.abs(V) ** 2, 4).tolist()}")
print("=== Stufe B ===")
results = {}
for s, rows in fits.items():
    grid = np.zeros((len(chis), len(dnus))); bestp = None
    for i, chi in enumerate(chis):
        for j, dnu in enumerate(dnus):
            (c, oo), ev = eval_point(chi, dnu, rows); grid[i, j] = c
            if bestp is None or c < bestp[0]: bestp = (c, chi, dnu, oo)
    results[s] = (grid, bestp)
    print(f"Orientierung {s:+d}: Gitter-Minimum chi2 = {bestp[0]:.3f} bei chi = {np.rad2deg(bestp[1]):.2f} Grad, dnu = {np.rad2deg(bestp[2]):.2f} Grad; "
          f"Anteil chi2 <= 5.99: {np.mean(grid <= 5.99):.4f}")
s_best = min(results, key=lambda s: results[s][1][0]); grid, bp = results[s_best]
c0, chi0, d0, _ = bp; best = bp
for chi in chi0 + np.deg2rad(np.arange(-0.5, 0.501, 0.01)):
    for dnu in d0 + np.deg2rad(np.arange(-0.5, 0.501, 0.01)):
        (c, oo), ev = eval_point(chi, dnu, fits[s_best])
        if c < best[0]: best = (c, chi, dnu, oo)
c, chi, dnu, oo = best
print(f"Verfeinert (Orientierung {s_best:+d}): chi2_min = {c:.3f} bei chi = {np.rad2deg(chi):.3f} Grad, dnu = {np.rad2deg(dnu) % 360:.3f} Grad")
print(f"  sin2th12 = {oo[0]:.4f}, sin2th13 = {oo[1]:.5f}, sin2th23 = {oo[2]:.4f}, delta_CP = {oo[3]:.1f} Grad")
parts = []
for (k, (cc, up, lo)), v in zip(NU.items(), oo):
    dv = v - cc
    if k == "d": dv = (dv + 180) % 360 - 180
    parts.append(f"{k}: {(dv / (up if dv > 0 else lo)) ** 2:.3f}")
print("  Beitraege:", ", ".join(parts))
frac = np.mean(grid <= 5.99)
verdict = "traegt" if c <= 5.99 else ("Spannung" if c <= 9.21 else "widerlegt")
print(f"URTEIL: {verdict}; Anteil der Ebene mit chi2 <= 5.99 = {frac:.4f} ({'nicht scharf' if frac > 0.2 else 'scharf'})")
np.save("k257_grid.npy", grid)
