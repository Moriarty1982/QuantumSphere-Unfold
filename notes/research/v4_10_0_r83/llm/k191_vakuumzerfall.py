"""k191: Test H76 - Vakuumzerfall 0 -> phi phi (M, E>0) + chi chi (T, E<0) ueber Gravitonaustausch.
Monte Carlo des Phasenraums; Ausgabe k191_out.json im aktuellen Ordner.
Einheiten: Gamma/V = c * Lambda^8 / M_P^4 mit kappa^2 = 32 pi / M_P^2, M_P = 1.22e19 GeV.
"""
import json, sys
import numpy as np

ETA = np.diag([1.0, -1.0, -1.0, -1.0])
rng = np.random.default_rng(int(sys.argv[1]) if len(sys.argv) > 1 else 191)

def ball(n, R):
    v = rng.normal(size=(n, 3)); v /= np.linalg.norm(v, axis=1)[:, None]
    return v * (R * rng.random(n) ** (1 / 3))[:, None]

def tmunu(p, q):
    pq = np.einsum('ni,ij,nj->n', p, ETA, q)
    T = np.einsum('ni,nj->nij', p, q) + np.einsum('ni,nj->nij', q, p)
    return T - pq[:, None, None] * np.linalg.inv(ETA)[None]   # obere Indizes

def contract(A, B):
    Bl = np.einsum('ia,nab,bj->nij', ETA, B, ETA)
    return np.einsum('nij,nij->n', A, Bl)

def trace(A):
    return np.einsum('ij,nij->n', ETA, A)

def sample(n, R, s_cut=None):
    k1, k2 = ball(n, R), ball(n, R)
    nv = rng.normal(size=(n, 3)); nv /= np.linalg.norm(nv, axis=1)[:, None]
    E1, E2 = np.linalg.norm(k1, axis=1), np.linalg.norm(k2, axis=1)
    K = k1 + k2; a = E1 + E2
    # g(r) = a - r - |K + r n| = 0  ->  (a-r)^2 = |K|^2 + 2 r K.n + r^2
    Kn = np.einsum('ni,ni->n', K, nv); K2 = np.einsum('ni,ni->n', K, K)
    r = (a ** 2 - K2) / (2 * (a + Kn))
    k3 = r[:, None] * nv; k4 = -(K + k3)
    E3, E4 = r, np.linalg.norm(k4, axis=1)
    J = 1 + np.einsum('ni,ni->n', nv, K + k3) / np.maximum(E4, 1e-300)
    ok = (r > 0) & (r < R) & (E4 < R) & (J > 0)
    p1 = np.c_[E1, k1]; p2 = np.c_[E2, k2]
    p3 = np.c_[-E3, k3]; p4 = np.c_[-E4, k4]        # negative Energie (F3)
    P = p1 + p2; s = np.einsum('ni,ij,nj->n', P, ETA, P)
    if s_cut is not None:
        ok &= s < s_cut
    T12, T34 = tmunu(p1, p2), tmunu(p3, p4)
    A = (contract(T12, T34) - 0.5 * trace(T12) * trace(T34)) / np.where(s > 0, s, 1)
    Vb = 4 / 3 * np.pi * R ** 3
    w = Vb ** 2 * 4 * np.pi * r ** 2 / np.where(J > 0, J, 1) * A ** 2 / np.maximum(E1 * E2 * E3 * E4, 1e-300)
    w = np.where(ok, w, 0.0)
    pref = 0.25 / ((2 * np.pi) ** 8 * 16)
    return pref * w

def integrate(R, s_cut=None, N=4_000_000, chunk=500_000):
    vals = np.concatenate([sample(chunk, R, s_cut) for _ in range(N // chunk)])
    return vals.mean(), vals.std() / np.sqrt(len(vals))

out = {}
# H76b: Rahmen-Cutoff, Exponent und c
res = {R: integrate(R) for R in (1.0, 2.0, 4.0)}
I1, dI1 = res[1.0]
c = 64 * np.pi ** 2 * I1          # (kappa^2/4)^2 = (8 pi)^2 / M_P^4
out['H76b'] = {
    'I': {str(R): v for R, v in res.items()},
    'exponent_1_2': float(np.log2(res[2.0][0] / I1)),
    'exponent_2_4': float(np.log2(res[4.0][0] / res[2.0][0])),
    'c': float(c), 'c_relerr': float(dI1 / I1),
}
# Kontrolle Kinematik: Energie- und Impulserhaltung an Stichproben
# H76a: nur Lorentz-invarianter Cutoff s < 1, Rahmen-Cutoff L wachsend
ra = {L: integrate(float(L), s_cut=1.0) for L in (1, 2, 4, 8, 16)}
out['H76a'] = {
    'I': {str(L): v for L, v in ra.items()},
    'ratios': {str(L): float(ra[L][0] / ra[L // 2][0]) for L in (2, 4, 8, 16)},
}
# H76c: Schranke nach Cline et al. (deren c ~ 1, Lambda < 3 MeV)
out['H76c'] = {'Lambda_bound_MeV': float(3.0 * c ** (-1 / 7)), 'factor_c^-1/7': float(c ** (-1 / 7))}
json.dump(out, open('k191_out.json', 'w'), indent=1, default=float)
print(json.dumps(out, indent=1, default=float))
