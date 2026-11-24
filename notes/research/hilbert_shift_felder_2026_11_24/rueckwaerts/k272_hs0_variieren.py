"""k272 (Erkundung, nicht blind, 24.11.2026): Das Ursprungsfeld HS(0) variieren und die Wirkung nach oben verfolgen.
Die HS(0)-Gleichung psi'' = g w^2 psi legt fest, was die neue Einheit des ersten Shifts quadriert: l^2 = g.
g = -1: Schwingung (Standardturm), g = 0: freie Drift (duale Zahlen), g = +1: Wachstum (gespaltene Zahlen, Tachyon-Lesart).
Verallgemeinerter Cayley-Dickson-Schritt: (a,b)(c,d) = (ac + g d* b, d a + b c*); g je Stufe (g1, g2, g3).
Je Muster fuer A_3 (dim 8): Norm-Signatur, Nullteiler, Einheiten mit e^2 = -1/0/+1, dim Der und Kompaktheit (Spurform),
Stabilisator der Einheit e7 (und e1), Kompaktheit.
Zusaetzlich: Amplitude, Frequenz und Phase von HS(0) (Skalierung) aendern oben nichts.
Aufruf: python3 k272_hs0_variieren.py
"""
import itertools
import numpy as np

rng = np.random.default_rng(272)


def conj(x):
    y = -x.copy(); y[0] = x[0]; return y


def mul(x, y, gs):
    n = len(x)
    if n == 1:
        return x * y
    h = n // 2
    g = gs[int(np.log2(n)) - 1]
    a, b, c, d = x[:h], x[h:], y[:h], y[h:]
    return np.concatenate([mul(a, c, gs) + g * mul(conj(d), b, gs), mul(d, a, gs) + mul(b, conj(c), gs)])


def table(N, gs):
    E = np.eye(N); C = np.zeros((N, N, N))
    for i in range(N):
        for j in range(N):
            C[i, j] = mul(E[i], E[j], gs)
    return C


def der_basis(C, fixed=()):
    N = C.shape[0]; rows = []
    for i in range(N):
        for j in range(N):
            for m in range(N):
                r = np.zeros(N * N)
                for k in range(N):
                    if C[i, j, k]:
                        r[m * N + k] += C[i, j, k]
                for p in range(N):
                    if C[p, j, m]:
                        r[p * N + i] -= C[p, j, m]
                    if C[i, p, m]:
                        r[p * N + j] -= C[i, p, m]
                if r.any():
                    rows.append(r)
    for f in fixed:
        for m in range(N):
            r = np.zeros(N * N); r[m * N + f] = 1.0; rows.append(r)
    _, s, vt = np.linalg.svd(np.array(rows))
    return [v.reshape(N, N) for v in vt[(s > 1e-9).sum():]]


def sig(B):
    if not B:
        return "-"
    G = np.array([[np.trace(X @ Y) for Y in B] for X in B])
    ev = np.linalg.eigvalsh(G)
    neg, pos = int((ev < -1e-9).sum()), int((ev > 1e-9).sum())
    zero = len(B) - neg - pos
    tag = "kompakt" if pos == 0 and zero == 0 else ("NICHT halbeinfach" if zero else "nicht kompakt")
    return f"({neg}-,{pos}+,{zero}0) {tag}"


N = 8
E = np.eye(N)
print("Muster (g1,g2,g3) | e^2: -1/0/+1 | Norm: -/+/0 | Nullteiler | dim Der, Spurform | Stab(e7) | Stab(e1)")
rows = []
for gs in itertools.product((-1, 0, 1), repeat=3):
    C = table(N, gs)
    sq = [mul(E[i], E[i], gs)[0] for i in range(1, N)]
    nm = np.array([mul(E[i], conj(E[i]), gs)[0] for i in range(N)])  # Norm x x* diagonal in der Basis
    # Nullteiler: kleinster Singulaerwert von L_x fuer x = e_i und x = 1 + e_i (deckt nilpotente und Null-Richtungen ab)
    cand = [E[i] for i in range(1, N)] + [E[0] + E[i] for i in range(1, N)]
    smin = min(np.linalg.svd(np.einsum('ijk,i->kj', C, x), compute_uv=False).min() for x in cand)
    D = der_basis(C)
    S7 = der_basis(C, (7,))
    S1 = der_basis(C, (1,))
    line = (f"{str(gs):13s} | {sq.count(-1)}/{sq.count(0)}/{sq.count(1)} | {int((nm < 0).sum())}/{int((nm > 0).sum())}/{int((nm == 0).sum())}"
            f" | {'ja' if smin < 1e-9 else 'nein'} | {len(D):2d} {sig(D)} | {len(S7)} {sig(S7)} | {len(S1)} {sig(S1)}")
    print(line)

print()
print("Skalierung: psi -> lam psi, t -> t/w, Phase t -> t + t0 kommutieren mit der linearen Regel psi' = u w psi.")
for lam in (0.5, 3.0):
    x, y = rng.normal(size=8), rng.normal(size=8)
    gs = (-1, -1, -1)
    print(f"   lam={lam}: |(lam x)(lam y) - lam^2 xy| = {np.abs(mul(lam * x, lam * y, gs) - lam ** 2 * mul(x, y, gs)).max():.1e}"
          "  -> Struktur (Der, Stab, Nullteiler) haengt nicht von Amplitude/Frequenz/Phase ab")
