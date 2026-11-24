"""k255 (Erkundung, nicht blind): r13 mit dem Wissen aus k253/k254.
(1) psi (S3-Drehung um 120 Grad aus k254b) fixiert e8 und vertauscht mit L_e8 -> Grund fuer das r13-Ergebnis.
(2) psi permutiert die drei Oktonionen-Kopien O_0 -> O_120 -> O_240 (k254c).
(3) Welche Ebenen-Winkel theta geben Unteralgebren O_theta = span{1, cos th e_i + sin th e_{i+8}}?
(4) Rahmen der drei Kopien: Summe der Projektoren auf Im O_k; Hauptwinkel zwischen Kopien.
(5) Nullteiler: Elemente der Kopien (Rang-1 in 7 x R^2) gegen verschraenkte (Rang 2).
(6) Produkte zwischen Kopien: wohin faellt x*y fuer x in Im O_0, y in Im O_120?
Aufruf aus diesem Ordner."""
import numpy as np
src = open("../k253_cayley_dickson_turm.py").read().split("for n in range(0, 6):")[0]
ns = {}; exec(src, ns); mul = ns["mul"]
rng = np.random.default_rng(255); E = np.eye(16); s3 = np.sqrt(3) / 2
def auto(lam, M):
    A = np.zeros((16, 16)); A[0, 0] = 1; A[8, 8] = lam
    for i in range(1, 8):
        A[i, i] = M[0][0]; A[i, i + 8] = M[0][1]; A[i + 8, i] = M[1][0]; A[i + 8, i + 8] = M[1][1]
    return A
psi = auto(1, [[-0.5, -s3], [s3, -0.5]])
# Automorphismus pruefen
err = max(np.abs(psi @ mul(x, y) - mul(psi @ x, psi @ y)).max() for x in E for y in E)
Le8 = np.array([mul(E[8], e) for e in E]).T
print(f"(1) psi Automorphismus: {err:.1e}; psi e8 = e8: {np.allclose(psi @ E[8], E[8])}; [psi, L_e8] = {np.abs(psi @ Le8 - Le8 @ psi).max():.1e}")
def copy(th):
    return np.array([E[0]] + [np.cos(th) * E[i] + np.sin(th) * E[i + 8] for i in range(1, 8)])
def proj(B):
    return B.T @ np.linalg.pinv(B.T)
P = {k: proj(copy(np.deg2rad(a))) for k, a in [(0, 0), (120, 120), (240, 240)]}
for k, kn in [(0, 120), (120, 240), (240, 0)]:
    print(f"(2) psi P_{k} psi^-1 = P_{kn}: {np.abs(psi @ P[k] @ psi.T - P[kn]).max():.1e}")
print("(3) Abgeschlossenheit von O_theta (max |(1-P) xy|):")
for a in [0, 15, 30, 45, 60, 90, 120, 135, 180]:
    B = copy(np.deg2rad(a)); Pt = proj(B)
    c = max(np.abs(mul(x, y) - Pt @ mul(x, y)).max() for x in B for y in B)
    print(f"    theta = {a:3d} Grad: {c:.3e}")
Pim = {k: proj(copy(np.deg2rad(k))[1:]) for k in (0, 120, 240)}
S = sum(Pim.values())
print(f"(4) Summe der Projektoren auf Im O_k = {np.round(np.linalg.eigvalsh(S)[::-1][:15], 6)} (Rahmen)")
sv = np.linalg.svd(copy(0)[1:] @ copy(np.deg2rad(120))[1:].T, compute_uv=False)
print(f"    Hauptwinkel Im O_0 / Im O_120: cos = {np.round(sv, 6)} -> {np.round(np.rad2deg(np.arccos(np.clip(sv, -1, 1))), 3)} Grad")
def minsv(a):
    L = np.array([mul(a, e) for e in E]).T; return np.linalg.svd(L, compute_uv=False).min() / np.linalg.norm(a)
r1 = min(minsv(np.concatenate([[0], np.cos(t) * w, [0], np.sin(t) * w])) for t, w in ((rng.uniform(0, np.pi), rng.normal(size=7)) for _ in range(500)))
r2 = []
for _ in range(500):
    W = rng.normal(size=(7, 2)); a = np.concatenate([[0], W[:, 0], [0], W[:, 1]]); r2.append(minsv(a))
print(f"(5) min. Singulaerwert/|a|: Rang-1-Elemente w(x)n (alle Winkel, 500 Stichproben) = {r1:.4f}; Rang-2 (verschraenkt): min {min(r2):.4f}, Median {np.median(r2):.4f}")
zd = (E[1] + E[10]) / np.sqrt(2)
print(f"    Nullteiler (e1+e10)/sqrt2 als Tensor in 7 x R^2: Rang {np.linalg.matrix_rank(np.stack([zd[1:8], zd[9:16]], 1))}")
dist = {"Re": 0, "e8": 0, "Im O_0": 0, "Im O_120": 0, "Im O_240": 0}; tot = 0
for _ in range(500):
    x = copy(0)[1:].T @ rng.normal(size=7); y = copy(np.deg2rad(120))[1:].T @ rng.normal(size=7)
    z = mul(x, y); n2 = z @ z; tot += n2
    dist["Re"] += z[0] ** 2; dist["e8"] += z[8] ** 2
    for k in (0, 120, 240): dist[f"Im O_{k}"] += z @ Pim[k] @ z
print("(6) Produkt x*y (x in Im O_0, y in Im O_120), Anteil von |xy|^2: " + ", ".join(f"{k} {v / tot:.4f}" for k, v in dist.items()))
x, y, z = (copy(np.deg2rad(a))[1:].T @ rng.normal(size=7) for a in (0, 120, 240))
print(f"    Assoziator ueber drei Kopien |(xy)z - x(yz)| / |x||y||z| = {np.linalg.norm(mul(mul(x, y), z) - mul(x, mul(y, z))) / (np.linalg.norm(x) * np.linalg.norm(y) * np.linalg.norm(z)):.4f}")
