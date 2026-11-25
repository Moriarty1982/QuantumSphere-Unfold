"""k258 (Test H130, Vorab-Notiz 3137c5f vom 25.11.2026 10:23 UTC): Ladungsrichtung relativ zur Verdopplungseinheit.
Gesucht: su(3)_c-stabile achtdimensionale Unteralgebren A = span(1, u) + V der Sedenionen, u in span(e7, e8, e15), V = V(a,b,c,d) im Triplett-Teil.
Abschlussdefekt per kleinster Quadrate aus Zufallsstarts; je Loesung u8^2, Alternativitaet, Normmultiplikativitaet, flache Richtungen.
Konvention des Turms wie k253. Aufruf: python3 k258_test_h130.py
"""
import numpy as np
from scipy.optimize import least_squares
rng = np.random.default_rng(258)
d = 16


def conj(x):
    y = -x.copy(); y[0] = x[0]; return y


def cdmul(x, y):
    n = len(x)
    if n == 1: return x * y
    h = n // 2
    a, b, c, dd = x[:h], x[h:], y[:h], y[h:]
    return np.concatenate([cdmul(a, c) - cdmul(conj(dd), b), cdmul(dd, a) + cdmul(b, conj(c))])


E = np.eye(d)
T = np.array([[cdmul(E[i], E[j]) for j in range(d)] for i in range(d)])
mul = lambda x, y: np.einsum('i,j,ijk->k', x, y, T)
L7 = T[7].T                      # x -> e7 x
R8 = T[:, 8, :].T                # x -> x e8
X6 = E[1:7]                      # e1 .. e6


def nullspace(M, tol=1e-9):
    u, s, vt = np.linalg.svd(M, full_matrices=M.shape[0] < M.shape[1])
    s = np.concatenate([s, np.zeros(vt.shape[0] - len(s))])
    return vt[(s < tol * s[0])]


def der_S(fix=None):
    I = np.eye(d); rows = []
    for i in range(d):
        for j in range(d):
            rows.append(np.kron(I, T[i, j][None, :]) - np.kron(T[:, j, :].T, I[i][None, :]) - np.kron(T[i].T, I[j][None, :]))
    if fix is not None:
        rows.append(np.kron(I, E[fix][None, :]))
    return nullspace(np.vstack(rows)).reshape(-1, d, d)


def basis(p):
    """p = (u7, u8, u15, a, b, c, d) -> Basis von A (8 x 16, nicht orthonormiert) und u."""
    u = np.zeros(d); u[7], u[8], u[15] = p[:3] / np.linalg.norm(p[:3])
    a, b, c, dd = p[3:] / np.linalg.norm(p[3:])
    V = np.array([a * x + b * (L7 @ x) + R8 @ (c * x + dd * (L7 @ x)) for x in X6])
    return np.vstack([E[0], u, V]), u


def defect(p):
    B, u = basis(p)
    Q, _ = np.linalg.qr(B.T)
    P = np.einsum('pi,qj,ijk->pqk', B, B, T)
    return (P - (P @ Q) @ Q.T).ravel()


def props(p):
    B, u = basis(p)
    alt = nm = 0.0
    for _ in range(40):
        x, y = rng.normal(size=8) @ B, rng.normal(size=8) @ B
        alt = max(alt, np.abs(mul(mul(x, x), y) - mul(x, mul(x, y))).max(), np.abs(mul(mul(y, x), x) - mul(y, mul(x, x))).max())
        nm = max(nm, abs(np.linalg.norm(mul(x, y)) - np.linalg.norm(x) * np.linalg.norm(y)))
    return alt, nm


if __name__ == '__main__':
    print("=" * 78); print("Kontrollen (i)")
    G2 = der_S(); SU3 = der_S(fix=7)
    print(f"   dim Der(S) = {len(G2)}, dim su(3)_c = Stab(e7) = {len(SU3)}")
    sing = nullspace(np.vstack(list(SU3)))
    idx = sorted(set(np.nonzero(np.abs(sing).max(axis=0) > 1e-9)[0]))
    print(f"   Singuletts: dim {len(sing)}, getragen von den Einheiten {idx}")
    worst = 0.0
    for _ in range(20):
        p = rng.normal(size=7); B, u = basis(p); Q, _ = np.linalg.qr(B.T)
        worst = max(worst, max(np.abs(D @ B.T - Q @ (Q.T @ (D @ B.T))).max() for D in SU3))
    print(f"   V(a,b,c,d) + span(1,u) ist su(3)_c-stabil: Rest {worst:.1e} (20 Zufallspunkte)")

    print("=" * 78); print("Suche: Abschlussdefekt = 0, 600 Zufallsstarts")
    sols = []
    for s in range(600):
        r = least_squares(defect, rng.normal(size=7), xtol=1e-15, ftol=1e-15, gtol=1e-15)
        D = float((r.fun ** 2).sum())
        if D < 1e-20: sols.append(r.x)
    print(f"   {len(sols)} von 600 Starts enden in einer abgeschlossenen Unteralgebra (D < 1e-20)")
    rows = []
    for p in sols:
        B, u = basis(p); alt, nm = props(p)
        # flache Richtungen: Jacobi-Rang auf der Mannigfaltigkeit S^2 x S^3 (Dimension 5, davon 1 Phase von CP^1)
        Jm = np.array([(defect(p + 1e-6 * e) - defect(p - 1e-6 * e)) / 2e-6 for e in np.eye(7)]).T
        sv = np.linalg.svd(Jm, compute_uv=False)
        flat = int((sv < 1e-5 * sv[0]).sum()) - 3      # 2 Normierungen + 1 Phase sind immer flach
        abcd = p[3:] / np.linalg.norm(p[3:])
        w1, w2 = abcd[0] ** 2 + abcd[1] ** 2, abcd[2] ** 2 + abcd[3] ** 2
        rows.append((round(u[8] ** 2, 6), round(u[7] ** 2, 4), round(u[15] ** 2, 4), round(w1, 4), alt < 1e-9 and nm < 1e-9, flat, alt, nm))
    from collections import Counter
    cnt = Counter((r[0], r[1], r[2], r[3], r[4], r[5]) for r in rows)
    print("   Klassen: u8^2, u7^2, u15^2, Gewicht der ersten Kopie in V, oktonionisch, flache Richtungen  ->  Anzahl")
    for kk, v in sorted(cnt.items()): print(f"   {kk}  ->  {v}")
    okt = [r for r in rows if r[4]]
    print(f"   oktonionisch: {len(okt)} Loesungen; Werte u8^2: {sorted(set(r[0] for r in okt))}; groesster Alternativ-/Normrest dort {max([max(r[6], r[7]) for r in okt], default=0):.1e}")
    nok = [r for r in rows if not r[4]]
    print(f"   abgeschlossen, aber nicht oktonionisch: {len(nok)}; Werte u8^2: {sorted(set(r[0] for r in nok))}")
    print("   r = 1 - (1 - u8^2)/10 je Wert:", {v: round(1 - (1 - v) / 10, 6) for v in sorted(set(r[0] for r in okt))})

    print("=" * 78); print("Kontrolle (ii): bekannte Kopien")
    for tag, ang in [('O_0', 0), ('O_120', 120), ('O_240', 240)]:
        c, s = np.cos(np.radians(ang)), np.sin(np.radians(ang))
        best = None
        for sg in (1, -1):
            p = np.array([c, 0, sg * s, c, 0, sg * s, 0]); D = (defect(p) ** 2).sum()
            if best is None or D < best[0]: best = (D, sg, p)
        alt, nm = props(best[2])
        print(f"   {tag}: u = {c:+.3f} e7 {best[1] * s:+.3f} e15, V = cos x + sin x e8: Defekt {best[0]:.1e}, alternativ {alt:.1e}, Norm {nm:.1e}")
    print("=" * 78); print("Gezielt: u = e8 mit V = {x + s (Jx) e8}")
    for sg in (1, -1):
        p = np.array([0, 1, 0, 1, 0, 0, sg]); D = (defect(p) ** 2).sum(); alt, nm = props(p)
        print(f"   s = {sg:+d}: Defekt {D:.1e}, alternativ {alt:.1e}, Norm {nm:.1e}")
