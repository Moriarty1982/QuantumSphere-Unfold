"""k191c: H76a halbanalytisch. Lorentz-invarianter Cutoff s < 1; Konfiguration im Ruhesystem von P = p1 + p2,
Boost-Volumen auf H^3 mit allen |k_i| < L exakt pro Richtung. Gleiche Normierung wie k191 (Kontrolle bei L = 1, 2, 4).
Ausgabe k191c_out.json im aktuellen Ordner.
"""
import json, sys
import numpy as np
src = open('k191_vakuumzerfall.py').read().split('def sample')[0]
g = {}; exec(src, g)
tmunu, contract, trace = g['tmunu'], g['contract'], g['trace']
rng = np.random.default_rng(1913)

def unit(n):
    v = rng.normal(size=(n, 3)); return v / np.linalg.norm(v, axis=1)[:, None]

def run(Ls, N=2_000_000, chunk=200_000):
    acc = {L: [] for L in Ls}
    for _ in range(N // chunk):
        s = rng.random(chunk); E = np.sqrt(s) / 2
        n1, n3, Om = unit(chunk), unit(chunk), unit(chunk)
        p1 = np.c_[E, E[:, None] * n1]; p2 = np.c_[E, -E[:, None] * n1]
        q3 = np.c_[E, E[:, None] * n3]; q4 = np.c_[E, -E[:, None] * n3]
        p3, p4 = -q3, -q4                                    # negative Energie
        T12, T34 = tmunu(p1, p2), tmunu(p3, p4)
        A = (contract(T12, T34) - 0.5 * trace(T12) * trace(T34)) / s
        c = np.max(np.abs(np.c_[np.einsum('ni,ni->n', n1, Om), np.einsum('ni,ni->n', n3, Om)]), axis=1)
        for L in Ls:
            r = L / E
            x = (r + np.sqrt(np.maximum(r ** 2 - (1 - c ** 2), 0))) / (1 + c)
            Y = np.log(np.maximum(x, 1.0))
            V = 4 * np.pi * (np.sinh(2 * Y) / 4 - Y / 2)       # int_0^Y sinh^2
            V = np.where(E < L, V, 0.0)
            # dPhi = ds (s/2) * (1/8 dOmega*)^2 ; Mittel ueber Omega* -> (4pi/8)^2
            w = (s / 2) * (np.pi / 2) ** 2 * A ** 2 * V
            acc[L].append(w)
    pref = 0.25 / (2 * np.pi) ** 8
    out = {}
    for L in Ls:
        w = np.concatenate(acc[L]) * pref
        out[L] = (float(w.mean()), float(w.std() / np.sqrt(len(w))))
    return out

Ls = [1, 2, 4, 8, 16, 32, 64, 128]
res = run(Ls)
ratios = {str(L): res[L][0] / res[L // 2][0] for L in Ls[1:]}
out = {'I': {str(L): v for L, v in res.items()}, 'ratios': ratios,
       'Kontrolle_k191_I': {'1': 5.751e-09, '2': 4.050e-08, '4': 1.940e-07}}
json.dump(out, open('k191c_out.json', 'w'), indent=1)
print(json.dumps(out, indent=1))
