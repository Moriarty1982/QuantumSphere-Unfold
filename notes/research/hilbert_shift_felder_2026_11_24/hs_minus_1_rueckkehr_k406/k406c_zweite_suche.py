"""k406c: zweite, unabhaengige exakte Suche nach der groessten Menge antikommutierender L_(e_i) fuer n = 4..8.
Anderer Weg als k406: dichte Matrizen aus der rekursiven Multiplikation (k253) bis n = 6, Vorzeichentabelle ab n = 7;
Suche per Verzweigung mit Faerbungsschranke (Tomita-Seki-Art) statt Bron-Kerbosch mit Pivot.
Aufruf: python k406c_zweite_suche.py > k406c_out.txt
"""
import numpy as np

def cd_sign_table(n):
    if n == 0: return np.ones((1, 1), dtype=np.int8)
    S = cd_sign_table(n - 1); h = S.shape[0]
    cj = -np.ones(h, dtype=np.int8); cj[0] = 1            # Konjugation auf Basis
    T = np.zeros((2 * h, 2 * h), dtype=np.int8)
    idx = np.arange(h)
    for a in range(h):
        for b in range(h):
            x = a ^ b
            T[a, b] = S[a, b]                              # (a,0)(c,0) = (ac,0)
            T[a, b + h] = S[b, a]                          # (a,0)(0,d) = (0, d a)
            T[a + h, b] = S[a, b] * cj[b]                  # (0,b)(c,0) = (0, b c*)
            T[a + h, b + h] = -cj[b] * S[b, a]             # (0,b)(0,d) = (-d* b, 0)
    return T

def radon_hurwitz(N):     # rho(N), N = 2^(4d+c) * ungerade: rho = 8d + 2^c
    b = 0
    while N % 2 == 0: N //= 2; b += 1
    return 8 * (b // 4) + 2 ** (b % 4)


def conj(x):
    y = -x.copy(); y[0] = x[0]; return y
def mul(x, y):
    m = len(x)
    if m == 1: return x * y
    h = m // 2; a, b, c, d = x[:h], x[h:], y[:h], y[h:]
    return np.concatenate([mul(a, c) - mul(conj(d), b), mul(d, a) + mul(b, conj(c))])

def adjacency(n):
    N = 2 ** n
    if n <= 6:
        E = np.eye(N)
        L = [np.array([mul(E[i], E[k]) for k in range(N)]).T for i in range(1, N)]
        return [[i != j and np.allclose(L[i] @ L[j] + L[j] @ L[i], 0) for j in range(N - 1)] for i in range(N - 1)]
    T = cd_sign_table(n).astype(np.int64); k = np.arange(N)
    A = [[False] * (N - 1) for _ in range(N - 1)]
    for i in range(1, N):
        for j in range(1, i):
            lij = T[j, k] * T[i, k ^ j]; lji = T[i, k] * T[j, k ^ i]
            A[i - 1][j - 1] = A[j - 1][i - 1] = bool(np.all(lij == -lji))
    return A

def maxclique(A):
    m = len(A); nb = [set(j for j in range(m) if A[i][j]) for i in range(m)]; best = []
    def expand(R, P):
        nonlocal best
        # Faerbung als obere Schranke
        order, colors, classes = [], [], []
        for v in sorted(P, key=lambda v: -len(nb[v] & P)):
            for ci, cl in enumerate(classes):
                if not (nb[v] & cl): cl.add(v); break
            else: classes.append({v})
        for ci, cl in enumerate(classes):
            for v in cl: order.append(v); colors.append(ci + 1)
        for idx in range(len(order) - 1, -1, -1):
            if len(R) + colors[idx] <= len(best): return
            v = order[idx]
            R2 = R + [v]
            if len(R2) > len(best): best = R2
            expand(R2, P & nb[v]); P = P - {v}
    expand([], set(range(m)))
    return best

for n in range(4, 9):
    cl = maxclique(adjacency(n))
    print(f"n = {n}: groesste antikommutierende Menge a = {len(cl)}; n + 4 = {n + 4}; Radon-Hurwitz - 1 = {radon_hurwitz(2**n) - 1}; Einheiten {sorted(i + 1 for i in cl)}")
