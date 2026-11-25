"""k283 (Test H128, Vorab-Notiz 2b53bbd vom 25.11.2026 09:48 UTC): Kollaps beim Hilbert-Shift HS(4).
H3(A_n) = hermitesche 3x3-Matrizen ueber der Cayley-Dickson-Algebra A_n, Produkt X o Y = (XY + YX)/2.
Teil A: dim Der(H3(A_n)), n = 0..4 (n = 5 mit Argument 5, Erkundung); Zerlegung in Der(A_n) + so(3).
Teil B: Massenform K(W) = sum_b ||[L_b, L_W]||^2 auf dem spurfreien Teil von H3(C_u); Verhaeltnis r = K(Spin 1)/K(Spin 2).
Alle Rechnungen in einer Orthonormalbasis der Spurform Re Tr(X o Y). Konvention des Turms wie k253.
Aufruf: python3 k283_test_h128.py [nmax]   (Standard nmax = 4)
"""
import sys, itertools, numpy as np
rng = np.random.default_rng(283)
NMAX = int(sys.argv[1]) if len(sys.argv) > 1 else 4


def conj(x):
    y = -x.copy(); y[0] = x[0]; return y


def cdmul(x, y):
    n = len(x)
    if n == 1: return x * y
    h = n // 2
    a, b, c, d = x[:h], x[h:], y[:h], y[h:]
    return np.concatenate([cdmul(a, c) - cdmul(conj(d), b), cdmul(d, a) + cdmul(b, conj(c))])


def cd_table(d):
    E = np.eye(d)
    return np.array([[cdmul(E[i], E[j]) for j in range(d)] for i in range(d)])


def albert(n):
    """Strukturtensor J[a,b,c] = (Phi_a o Phi_b)_c in der Orthonormalbasis; dazu Basis-Matrizen (N,3,3,d)."""
    d = 2 ** n; T = cd_table(d); N = 3 + 3 * d
    pos = [(1, 2), (2, 0), (0, 1)]
    B = np.zeros((N, 3, 3, d))
    for k in range(3): B[k, k, k, 0] = 1.0
    for k, (i, j) in enumerate(pos):
        for p in range(d):
            a = 3 + k * d + p; e = np.zeros(d); e[p] = 1 / np.sqrt(2)
            B[a, i, j] = e; B[a, j, i] = conj(e)
    P = np.einsum('aikp,bkjq,pqr->abijr', B, B, T, optimize=True)
    P = 0.5 * (P + P.transpose(1, 0, 2, 3, 4))
    J = np.zeros((N, N, N))
    for k in range(3): J[:, :, k] = P[:, :, k, k, 0]
    for k, (i, j) in enumerate(pos):
        J[:, :, 3 + k * d:3 + (k + 1) * d] = np.sqrt(2) * P[:, :, i, j, :]
    return J, T, d, N


def nullspace(M, tol=1e-8):
    u, s, vt = np.linalg.svd(M, full_matrices=M.shape[0] < M.shape[1])
    del u
    s = np.concatenate([s, np.zeros(vt.shape[0] - len(s))])
    k = int((s < tol * s[0]).sum())
    gap = s[len(s) - k - 1] / max(s[len(s) - k:].max(), 1e-300) if k else np.inf
    return vt[len(s) - k:], gap


def der_alg(J, N, pairs):
    """Derivationen D mit D(x o y) = Dx o y + x o Dy; Unbekannte D[p,q] -> p*N+q. Zufallspaare, danach Probe auf allen Basispaaren."""
    I = np.eye(N); rows = []
    for _ in range(pairs):
        x, y = rng.normal(size=N), rng.normal(size=N)
        Lx = np.einsum('a,abc->cb', x, J); Ly = np.einsum('a,abc->cb', y, J)
        z = Lx @ y
        rows.append(np.kron(I, z[None, :]) - np.kron(Ly, x[None, :]) - np.kron(Lx, y[None, :]))
    V, gap = nullspace(np.vstack(rows))
    Ds = V.reshape(-1, N, N)
    res = 0.0
    for D in Ds:  # Probe: D(a o b) - Da o b - a o Db auf allen Basispaaren
        R = np.einsum('abc,mc->abm', J, D) - np.einsum('pa,pbm->abm', D, J) - np.einsum('pb,apm->abm', D, J)
        res = max(res, np.abs(R).max())
    return Ds, gap, res


def der_cd(T, d):
    I = np.eye(d); rows = []
    for i in range(d):
        for j in range(d):
            Li = T[i].T; Rj = T[:, j, :].T      # L_{e_i}, R_{e_j}
            z = T[i, j]
            rows.append(np.kron(I, z[None, :]) - np.kron(Rj, I[i][None, :]) - np.kron(Li, I[j][None, :]))
    V, _ = nullspace(np.vstack(rows))
    return V.reshape(-1, d, d)


def known_ders(T, d, N):
    """so(3): X -> [A, X] mit A reell antisymmetrisch; Der(A_n) eintragsweise. In Orthonormalkoordinaten."""
    out = []
    for Dd in der_cd(T, d):
        M = np.zeros((N, N))
        for k in range(3): M[3 + k * d:3 + (k + 1) * d, 3 + k * d:3 + (k + 1) * d] = Dd
        out.append(M)
    return out


def so3_ders(J, N, d):
    # [A, X] = 2 * (A' o X) geht nicht (A nicht hermitesch) -> direkt ueber Basis-Matrizen
    pos = [(1, 2), (2, 0), (0, 1)]
    B = np.zeros((N, 3, 3, d))
    for k in range(3): B[k, k, k, 0] = 1.0
    for k, (i, j) in enumerate(pos):
        for p in range(d):
            e = np.zeros(d); e[p] = 1 / np.sqrt(2); B[3 + k * d + p, i, j] = e; B[3 + k * d + p, j, i] = conj(e)
    out = []
    for (i, j) in pos:
        A = np.zeros((3, 3)); A[i, j] = 1; A[j, i] = -1
        C = np.einsum('ik,akjp->aijp', A, B) - np.einsum('aikp,kj->aijp', B, A)
        M = np.zeros((N, N))
        for k in range(3): M[k] = C[:, k, k, 0]
        for k, (ii, jj) in enumerate(pos): M[3 + k * d:3 + (k + 1) * d] = np.sqrt(2) * C[:, ii, jj, :].T
        out.append(M)
    return out


def field_basis(d, N, u):
    """Orthonormalbasis des spurfreien Teils von H3(C_u): 5 x Spin 2 (reell symmetrisch), 3 x Spin 1 (u * antisymmetrisch)."""
    S = []
    v = np.zeros(N); v[0], v[1] = 1, -1; S.append(v / np.sqrt(2))
    v = np.zeros(N); v[0], v[1], v[2] = 1, 1, -2; S.append(v / np.sqrt(6))
    for k in range(3): v = np.zeros(N); v[3 + k * d] = 1; S.append(v)
    V = []
    for k in range(3): v = np.zeros(N); v[3 + k * d:3 + (k + 1) * d] = u; V.append(v)
    return np.array(S), np.array(V)


def forms(J, N, F):
    """K(X,Y) = sum_b Tr([L_b,L_X]^T [L_b,L_Y]) und Q(X,Y) = Tr(L_X^T L_Y), T2(X,Y) = Tr(L_X L_Y) auf den Feldern F."""
    Lb = J.transpose(0, 2, 1)                       # Lb[a] = L_{Phi_a}
    LF = np.einsum('fa,acb->fcb', F, Lb)
    Cm = np.einsum('bij,fjk->fbik', Lb, LF) - np.einsum('fij,bjk->fbik', LF, Lb)
    K = np.einsum('fbik,gbik->fg', Cm, Cm)
    T2 = np.einsum('fij,gji->fg', LF, LF)
    return K, T2


def report(tag, K, T2):
    kS, kV = np.diag(K)[:5], np.diag(K)[5:]
    off = np.abs(K - np.diag(np.diag(K))).max() / np.abs(K).max()
    spread = max(np.ptp(kS) / kS.mean(), np.ptp(kV) / kV.mean())
    r = kV.mean() / kS.mean()
    tS, tV = np.diag(T2)[:5], np.diag(T2)[5:]
    print(f"   {tag}: K(Spin 2) = {kS.mean():.12f}  K(Spin 1) = {kV.mean():.12f}  r = {r:.12f}  r-1 = {r - 1:+.3e}")
    print(f"      Kontrollen: Mischterm/Nebendiag. {off:.1e}  Streuung im Spin-Raum {spread:.1e}  Tr(L_W^2): V/S - 1 = {tV.mean() / tS.mean() - 1:+.1e}")
    return r


if __name__ == '__main__':
    for n in range(0, NMAX + 1):
        J, T, d, N = albert(n)
        x, y = rng.normal(size=N), rng.normal(size=N)
        jo = lambda a, b: np.einsum('a,b,abc->c', a, b, J)
        x2 = jo(x, x)
        jid = np.abs(jo(jo(x, y), x2) - jo(x, jo(y, x2))).max()
        print(f"n = {n}: A_n dim {d}, H3(A_n) dim {N}; Jordan-Identitaet Rest {jid:.1e}")
        Ds, gap, res = der_alg(J, N, pairs=N + 25)
        kn = known_ders(T, d, N) + so3_ders(J, N, d)
        kn_flat = np.array([m.ravel() for m in kn])
        rk = np.linalg.matrix_rank(kn_flat, tol=1e-9)
        chk = 0.0
        for m in kn:
            R = np.einsum('abc,mc->abm', J, m) - np.einsum('pa,pbm->abm', m, J) - np.einsum('pb,apm->abm', m, J)
            chk = max(chk, np.abs(R).max())
        # Rest der gefundenen Derivationen ausserhalb span(Der(A_n) + so(3))
        Q, _ = np.linalg.qr(kn_flat.T)
        Dflat = Ds.reshape(len(Ds), -1)
        out = np.abs(Dflat - (Dflat @ Q) @ Q.T).max() if len(Ds) else 0.0
        print(f"   dim Der(H3(A_n)) = {len(Ds)}  (Luecke {gap:.1e}, Probe auf allen Basispaaren {res:.1e})")
        print(f"   Der(A_n) + so(3): dim {rk} (Derivationsprobe {chk:.1e}); Anteil von Der ausserhalb davon: {out:.1e}")
        if n >= 1:
            units = {}
            if n == 3: units = {'u = e7': 7}
            elif n == 4: units = {'u = e7': 7, 'u = e8': 8, 'u = e15': 15}
            elif n == 5: units = {'u = e7': 7, 'u = e8': 8, 'u = e16': 16, 'u = e31': 31}
            else: units = {f'u = e{d - 1}': d - 1}
            for tag, i in units.items():
                u = np.zeros(d); u[i] = 1
                S, V = field_basis(d, N, u)
                K, T2 = forms(J, N, np.vstack([S, V]))
                report(tag, K, T2)
            if n >= 4:  # Erkundung: schiefe Einheit (Nullteiler-Richtung)
                u = np.zeros(d); u[1] = u[10] = 1 / np.sqrt(2)
                S, V = field_basis(d, N, u)
                K, T2 = forms(J, N, np.vstack([S, V]))
                report('u = (e1+e10)/sqrt2 [Erkundung]', K, T2)
        sys.stdout.flush()
