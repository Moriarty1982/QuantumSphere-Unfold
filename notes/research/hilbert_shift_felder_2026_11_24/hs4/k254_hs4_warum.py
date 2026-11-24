"""k254 (Erkundung, nicht blind): Warum bringt HS(4) (Sedenionen) nichts Neues?
Teil A: Identitaeten je Stufe. Teil B: Nullteiler (Kern von L_a, G2-Bahn eines Nullteilers).
Teil C: groesste Menge paarweise antikommutierender L_{e_i} (verträgliche Kreisachsen) gegen Radon-Hurwitz rho(2^n)-1.
Konvention wie k253: (a,b)(c,d) = (ac - d* b, d a + b c*). Aufruf aus diesem Ordner."""
import itertools, numpy as np
src = open("../k253_cayley_dickson_turm.py").read().split("for n in range(0, 6):")[0]
ns = {}; exec(src, ns); mul, table = ns["mul"], ns["table"]
rng = np.random.default_rng(254)
def assoc(x, y, z): return mul(mul(x, y), z) - mul(x, mul(y, z))
print("Teil A: max. Verletzung ueber 300 Zufallstripel")
for n in range(1, 7):
    N = 2 ** n; w = dict(alt=0, flex=0, moufang=0, potenz=0, norm=0)
    for _ in range(300):
        x, y, z = (rng.normal(size=N) for _ in range(3))
        w["alt"] = max(w["alt"], np.abs(assoc(x, x, y)).max())
        w["flex"] = max(w["flex"], np.abs(assoc(x, y, x)).max())
        w["moufang"] = max(w["moufang"], np.abs(mul(mul(z, x), mul(y, z)) - mul(mul(z, mul(x, y)), z)).max())
        x2 = mul(x, x); w["potenz"] = max(w["potenz"], np.abs(mul(x2, x) - mul(x, x2)).max())
        w["norm"] = max(w["norm"], abs(np.linalg.norm(mul(x, y)) - np.linalg.norm(x) * np.linalg.norm(y)))
    print(f"  n={n} dim={N:2d} " + " ".join(f"{k}={v:.1e}" for k, v in w.items()))

print("Teil B: Nullteiler in S (n=4)")
N = 16; C = table(N); E = np.eye(N)
a = (E[1] + E[10]) / np.sqrt(2)
La = np.array([mul(a, e) for e in E]).T
sv = np.linalg.svd(La, compute_uv=False)
print(f"  a=(e1+e10)/sqrt2: Singulaerwerte von L_a = {np.round(sv, 6)}; dim Kern = {int(np.sum(sv < 1e-9))}")
# Derivationsbasis von S
rows = []
for i in range(N):
    for j in range(N):
        for m in range(N):
            r = np.zeros(N * N)
            for k in range(N):
                r[m * N + k] += C[i, j, k]
            for p in range(N):
                r[p * N + i] -= C[p, j, m]; r[p * N + j] -= C[i, p, m]
            if r.any(): rows.append(r)
A = np.array(rows); _, s, Vt = np.linalg.svd(A)
null = Vt[np.sum(s > 1e-9):]
Ds = [v.reshape(N, N) for v in null]
print(f"  dim Der(S) = {len(Ds)}")
orbit = np.array([D @ a for D in Ds])
print(f"  Dimension der G2-Bahn des Nullteilers a: {np.linalg.matrix_rank(orbit, tol=1e-9)} (Moreno: Menge der Einheits-Nullteiler ~ V_2(R^7), dim 11)")
# zufaelliger Punkt: liegt ein generisches Element auf der Nullteilermenge?
gen = rng.normal(size=N); gen[0] = 0; gen /= np.linalg.norm(gen)
Lg = np.array([mul(gen, e) for e in E]).T
print(f"  generische Einheits-Imaginaere: kleinster Singulaerwert von L = {np.linalg.svd(Lg, compute_uv=False).min():.3f} (kein Nullteiler)")

print("Teil C: verträgliche Kreisachsen = groesste Menge paarweise antikommutierender L_{e_i}, i>=1")
def rho(N):
    c = 0
    while N % 2 == 0: N //= 2; c += 1
    a, b = divmod(c, 4)
    return 8 * a + 2 ** b
for n in range(1, 6):
    N = 2 ** n; E = np.eye(N)
    L = [np.array([mul(E[i], e) for e in E]).T for i in range(1, N)]
    anti = [[np.abs(L[i] @ L[j] + L[j] @ L[i]).max() < 1e-9 for j in range(N - 1)] for i in range(N - 1)]
    sq = all(np.abs(Li @ Li + np.eye(N)).max() < 1e-9 for Li in L)
    # groesste Clique (gierig + exakt fuer kleine N)
    best = 0
    idx = list(range(N - 1))
    def grow(cl, cand):
        global best
        best = max(best, len(cl))
        for k, c in enumerate(cand):
            if len(cl) + len(cand) - k <= best: return
            grow(cl + [c], [d for d in cand[k + 1:] if anti[c][d]])
    grow([], idx)
    print(f"  n={n} dim={N:2d}: alle L_ei^2=-1: {sq}; groesste antikommutierende Menge = {best}; Radon-Hurwitz rho(N)-1 = {rho(N)-1}; Imaginaere = {N-1}")
print("  Radon-Hurwitz rho(2^n)-1 fuer n=0..9:", [rho(2 ** n) - 1 for n in range(10)])
