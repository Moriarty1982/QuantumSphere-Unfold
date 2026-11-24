"""k253 (Erkundung, nicht blind): Cayley-Dickson-Turm A_n (dim 2^n) als Erzeugungsregel fuer HS(n).
Je Stufe: Derivationen Der(A_n), Stabilisator einer imaginaeren Einheit, Lie-Algebra der Linksmultiplikationen,
Kommutativitaet, Assoziativitaet, Alternativitaet, Normmultiplikativitaet, Nullteiler.
Konvention: (a,b)(c,d) = (ac - d* b, d a + b c*)."""
import itertools, numpy as np
rng = np.random.default_rng(253)

def conj(x):
    y = -x.copy(); y[0] = x[0]; return y

def mul(x, y):
    n = len(x)
    if n == 1: return x * y
    h = n // 2
    a, b, c, d = x[:h], x[h:], y[:h], y[h:]
    return np.concatenate([mul(a, c) - mul(conj(d), b), mul(d, a) + mul(b, conj(c))])

def table(N):
    E = np.eye(N); C = np.zeros((N, N, N))
    for i in range(N):
        for j in range(N): C[i, j] = mul(E[i], E[j])
    return C

def rank(M): return np.linalg.matrix_rank(M, tol=1e-9)

def der_dim(C, fix=None):
    N = C.shape[0]; rows = []
    # unknown D[m,i] -> index m*N+i ; condition for all i,j,m
    for i in range(N):
        for j in range(N):
            for m in range(N):
                r = np.zeros(N * N)
                for k in range(N):
                    if C[i, j, k]: r[m * N + k] += C[i, j, k]
                for p in range(N):
                    if C[p, j, m]: r[p * N + i] -= C[p, j, m]
                    if C[i, p, m]: r[p * N + j] -= C[i, p, m]
                if r.any(): rows.append(r)
    if fix is not None:
        for m in range(N):
            r = np.zeros(N * N); r[m * N + fix] = 1; rows.append(r)
    A = np.array(rows)
    return N * N - rank(A)

def lie_closure(gens):
    basis = []
    def add(M):
        nonlocal basis
        cand = basis + [M.ravel()]
        if rank(np.array(cand)) > len(basis): basis.append(M.ravel()); return True
        return False
    mats = []
    for g in gens:
        if add(g): mats.append(g)
    changed = True
    while changed:
        changed = False
        for a, b in itertools.combinations(list(mats), 2):
            c = a @ b - b @ a
            if add(c): mats.append(c); changed = True
    return len(basis)

for n in range(0, 6):
    N = 2 ** n; C = table(N)
    X = [rng.normal(size=N) for _ in range(3)]
    x, y, z = X
    comm = np.abs(mul(x, y) - mul(y, x)).max()
    assoc = np.abs(mul(mul(x, y), z) - mul(x, mul(y, z))).max()
    alt = np.abs(mul(mul(x, x), y) - mul(x, mul(x, y))).max()
    normm = abs(np.linalg.norm(mul(x, y)) - np.linalg.norm(x) * np.linalg.norm(y))
    # Nullteiler: kleinste Singulaerwert der Linksmultiplikation ueber Zufallseinheiten (+ bekanntes Paar fuer n>=4)
    zd = None
    if n >= 4:
        E = np.eye(N); a = E[1] + E[10]; b = E[4] - E[15]
        zd = np.abs(mul(a, b)).max()
    dD = der_dim(C) if n <= 5 else None
    dS = der_dim(C, fix=N - 1) if n >= 1 and n <= 5 else None
    L = [C[i].T for i in range(1, N)]  # L_{e_i}: matrix with (L x)_k = sum_j C[i,j,k] x_j
    dL = lie_closure(L) if n >= 1 and n <= 4 else None
    print(f"n={n} dim={N:2d} | komm {comm:.1e} assoz {assoc:.1e} altern {alt:.1e} |xy|-|x||y| {normm:.1e}"
          f" | Nullteiler(e1+e10)(e4-e15) {zd} | dim Der={dD} | dim Stab(e_last)={dS} | dim Lie<L_e_i>={dL}")
