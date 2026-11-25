"""k322c (nachtraeglich, Erkundung): Welche Elemente der nicht alternativen O_v auf HS(5) sind Nullteiler von A5?
Liest k322_nullteiler_kopien.py nicht ein (dort laeuft alles beim Import); Definitionen kopiert."""
import numpy as np
rng = np.random.default_rng(3223)
def conj(x):
    y = -x.copy(); y[0] = x[0]; return y
def mul(x, y):
    n = len(x)
    if n == 1: return x * y
    h = n // 2; a, b, c, d = x[:h], x[h:], y[:h], y[h:]
    return np.concatenate([mul(a, c) - mul(conj(d), b), mul(d, a) + mul(b, conj(c))])
E = np.eye(32); C = np.zeros((32, 32, 32))
for i in range(32):
    for j in range(32): C[i, j] = mul(E[i], E[j])
L = lambda x: np.einsum('i,ijk->kj', x, C)
r2 = np.sqrt(2)
for v in ([-1/r2, 0, 0, -1/r2], [-1/(2*r2), -np.sqrt(1.5)/2, -np.sqrt(1.5)/2, 1/(2*r2)]):
    v = np.array(v)
    def emb(a):
        x = np.zeros(32)
        for k in range(4): x[8*k+1:8*k+8] = v[k]*a
        return x
    s_im = []; s_mix = []; kd = []
    for _ in range(200):
        a = rng.normal(size=7); x = emb(a); x /= np.linalg.norm(x)
        s = np.linalg.svd(L(x), compute_uv=False); s_im.append(s[-1]); kd.append(int(np.sum(s < 1e-9)))
        y = x + rng.normal()*E[0]; y /= np.linalg.norm(y); s_mix.append(np.linalg.svd(L(y), compute_uv=False)[-1])
    print(f"v = {np.round(v,4)}: rein imaginaer: max smin {max(s_im):.1e}, Kerndimension {sorted(set(kd))}; mit Realteil: min smin {min(s_mix):.3f}")
    # Profil in R^4 der Imaginaerelemente: M = a v^T, Rang 1 -- aber v ist in R^4 'zwischen' Bloecken; Gewicht in den 9 oktonionischen Richtungen
