"""k290 (Erkundung, nicht blind): rekursiver Ansatz einer Feldgleichung fuer den Hilbert-Shift-Turm.
Feld psi in A_n (Cayley-Dickson, Dimension 2^n). Verdopplung mit Vorzeichen g_n (frei gelassen):
    (a,b)(c,d) = (ac + g d* b, d a + b c*),   (a,b)* = (a*, -b),   l^2 = g.
Teil S (sympy, exakt): Rekursion der Norm, Automorphismus b -> -b, Bewegungsregel erster Ordnung,
    Verschwinden der Zusatzterme K_k auf der Vorstufe, HS(1)-Ellipse, sigma-Identitaet aus k282.
Teil N (numpy): Symmetrie-Algebra der Terme je Stufe (Dimensionen), Stabilisator einer Einheit, HS(4).
Aufruf: python k290_rekursive_feldgleichung.py > k290_out.txt
"""
import itertools
import numpy as np
import sympy as sp

# ---------------------------------------------------------------- Algebra (Listen, beliebige Skalare)
def conj(x):
    return [x[0]] + [-c for c in x[1:]]

def add(x, y): return [a + b for a, b in zip(x, y)]
def sub(x, y): return [a - b for a, b in zip(x, y)]
def scal(s, x): return [s * a for a in x]

def mul(x, y, g):
    """g = Liste der Vorzeichen (g_0, ..., g_{n-1}); g[-1] gehoert zur aeussersten Verdopplung."""
    n = len(x)
    if n == 1:
        return [x[0] * y[0]]
    h = n // 2
    a, b, c, d = x[:h], x[h:], y[:h], y[h:]
    gi, gg = g[:-1], g[-1]
    return add(mul(a, c, gi), scal(gg, mul(conj(d), b, gi))) + add(mul(d, a, gi), mul(b, conj(c), gi))

def norm(x, g):
    return mul(x, conj(x), g)[0]

def inner(x, y, g):
    return mul(conj(x), y, g)[0]

def comm(x, y, g): return sub(mul(x, y, g), mul(y, x, g))
def assoc(x, y, z, g): return sub(mul(mul(x, y, g), z, g), mul(x, mul(y, z, g), g))

def K1(x, y, g): return norm(x, g) * norm(y, g) - inner(x, y, g) ** 2          # Flaeche (Gram)
def K2(x, y, g): return norm(comm(x, y, g), g)                                  # Kommutator
def K3(x, y, z, g): return norm(assoc(x, y, z, g), g)                           # Assoziator
def K4(x, y, g): return norm(mul(x, y, g), g) - norm(x, g) * norm(y, g)         # Normdefekt

def syms(name, N): return list(sp.symbols(f"{name}0:{N}", real=True))
def ex(v): return [sp.expand(c) for c in v]
def iszero(v): return all(sp.expand(c) == 0 for c in (v if isinstance(v, list) else [v]))

print("== k290 Teil S (sympy, exakt) ==")
gs = list(sp.symbols("g0:4"))          # freie Vorzeichen der vier Verdopplungen

print("\nS1 Rekursion der Norm: N_{n+1}(a + b l) = N_n(a) - g_n N_n(b), g symbolisch")
for n in (1, 2, 3):
    N = 2 ** n; x = syms("x", N); g = gs[:n]
    lhs = norm(x, g); rhs = norm(x[:N // 2], g[:-1]) - g[-1] * norm(x[N // 2:], g[:-1])
    print(f"  n={n}: Rest = {sp.expand(lhs - rhs)}")
print("  Norm der acht Einheiten (n=3):", [sp.expand(norm([1 if i == j else 0 for i in range(8)], gs[:3])) for j in range(8)])

print("\nS2 sigma_n: (a,b) -> (a,-b) ist Automorphismus (g symbolisch); Folge: Anhang ist gerade in b")
for n in (1, 2, 3):
    N = 2 ** n; x = syms("x", N); y = syms("y", N); g = gs[:n]
    sg = lambda v: v[:N // 2] + [-c for c in v[N // 2:]]
    print(f"  n={n}: sigma(xy) - sigma(x)sigma(y) = 0 ? {iszero(sub(sg(mul(x, y, g)), mul(sg(x), sg(y), g)))}")

print("\nS3 Bewegungsregel erster Ordnung: L1 = 1/2 <psi', u psi> + s w/2 N(psi)")
for n in (1, 2, 3):
    N = 2 ** n; g = gs[:n]; x = syms("x", N); y = syms("y", N)
    u = [0] + syms("u", N)[1:]                                    # beliebige imaginaere Richtung
    anti = sp.expand(inner(mul(u, x, g), y, g) + inner(x, mul(u, y, g), g))
    sq = sub(mul(u, mul(u, x, g), g), scal(-norm(u, g), x))       # u(ux) = u^2 x, u^2 = -N(u)
    print(f"  n={n}: <ux,y> + <x,uy> = {anti};  u(ux) + N(u) x = 0 ? {iszero(sq)}")
t, w, s = sp.symbols("t omega s", real=True)
for n in (1, 2):
    N = 2 ** n; g = [-1] * n
    psi = [sp.Function(f"p{i}")(t) for i in range(N)]
    u = [0] * N; u[N // 2] = 1                                     # u = neue Einheit l
    dpsi = [sp.diff(p, t) for p in psi]
    L1 = sp.Rational(1, 2) * inner(dpsi, mul(u, psi, g), g) + s * w / 2 * norm(psi, g)
    EL = [sp.diff(L1, p) - sp.diff(sp.diff(L1, dp), t) for p, dp in zip(psi, dpsi)]
    target = sub(dpsi, scal(w, mul(u, psi, g)))                    # psi' - w u psi
    sol = sp.solve([e.subs(s, -1) for e in EL], dpsi, dict=True)[0]
    print(f"  n={n}, g=-1, s=-1: Euler-Lagrange gibt psi' = w u psi ? "
          f"{iszero([sol[dp] - (dp - tg) for dp, tg in zip(dpsi, target)])}"
          f"  => psi'' = u^2 w^2 psi = g w^2 psi")
# n = 4: Regel bricht fuer allgemeines u
g4 = [-1] * 4
u = [0] + [sp.Rational(k, 7) for k in (1, -2, 3, 1, 2, -1, 1, 3, -2, 1, 1, 2, -3, 1, 2)]
x = [sp.Rational(k, 5) for k in (1, 2, -1, 3, 1, -2, 2, 1, -1, 3, 2, 1, -2, 1, 3, -1)]
res = sub(mul(u, mul(u, x, g4), g4), scal(-norm(u, g4), x))
print(f"  n=4 (rational, exakt): |u(ux) + N(u)x|^2 / (N(u)^2 N(x)) = {sp.nsimplify(norm(res, g4) / (norm(u, g4) ** 2 * norm(x, g4)))}  (ungleich 0: Regel bricht)")

print("\nS4 Zusatzterme: K_k verschwindet identisch auf A_{k-1} und nicht auf A_k (g symbolisch bis n=3)")
x1, y1 = syms("x", 1), syms("y", 1)
print("  K1 (Flaeche)     auf R:", sp.expand(K1(x1, y1, [])), "| auf C:", sp.factor(K1(syms("x", 2), syms("y", 2), gs[:1])))
print("  K2 (Kommutator)  auf C:", sp.expand(K2(syms("x", 2), syms("y", 2), gs[:1])),
      "| auf H, x=e1,y=e2:", sp.expand(K2([0, 1, 0, 0], [0, 0, 1, 0], gs[:2])))
print("  K3 (Assoziator)  auf H:", iszero(assoc(syms("x", 4), syms("y", 4), syms("z", 4), gs[:2])),
      "(Assoziator = 0) | auf O, e1,e2,e4:",
      sp.expand(K3([0, 1, 0, 0, 0, 0, 0, 0], [0, 0, 1, 0, 0, 0, 0, 0], [0, 0, 0, 0, 1, 0, 0, 0], gs[:3])))
x8, y8 = syms("x", 8), syms("y", 8)
print("  K4 (Normdefekt)  auf O:", sp.expand(K4(x8, y8, gs[:3])), end=" ")
e = lambda i: [1 if j == i else 0 for j in range(16)]
zd = (add(e(1), e(10)), sub(e(4), e(15)))
print("| auf S, (e1+e10)(e4-e15):", K4(zd[0], zd[1], g4), " Produkt =", mul(zd[0], zd[1], g4) == [0] * 16 and "0 (Nullteiler)")
print("  K2 auf H allgemein = 4*Gram(Im x, Im y)?",
      iszero(K2(syms("x", 4), syms("y", 4), [-1, -1]) - 4 * K1([0] + syms("x", 4)[1:], [0] + syms("y", 4)[1:], [-1, -1])))

print("\nS5 Freie Lagrangedichte (1+1 Dim.), Rekursion und Bewegungsgleichung")
xx, m = sp.symbols("x m", real=True)
for n in (1, 2):
    N = 2 ** n; g = gs[:n]
    f = [sp.Function(f"f{i}")(t, xx) for i in range(N)]
    L0 = lambda v, gg: sp.Rational(1, 2) * (norm([sp.diff(c, t) for c in v], gg) - norm([sp.diff(c, xx) for c in v], gg)
                                            - m ** 2 * norm(v, gg))
    rest = sp.expand(L0(f, g) - L0(f[:N // 2], g[:-1]) + g[-1] * L0(f[N // 2:], g[:-1]))
    eom = [sp.simplify((sp.diff(L0(f, g), c) - sp.diff(sp.diff(L0(f, g), sp.diff(c, t)), t)
                        - sp.diff(sp.diff(L0(f, g), sp.diff(c, xx)), xx))) for c in f]
    kg = [sp.diff(c, t, 2) - sp.diff(c, xx, 2) + m ** 2 * c for c in f]
    ratio = [sp.simplify(a / b) for a, b in zip(eom, kg)]
    print(f"  n={n}: L0_(n)[a+bl] - L0_(n-1)[a] + g L0_(n-1)[b] = {rest};  EL_i / (Box+m^2)f_i = {ratio}")
print("  => jede Komponente: (Box + m^2) f = 0 fuer g != 0; Vorzeichen g steht nur vor der Energie des Anhangs.")

print("\nS6 HS(0)/HS(1): Ellipse loest die Gleichung zweiter Ordnung; Ladung und Zeitumkehr")
a, b = sp.symbols("a b", positive=True)
psi = [(a + b) * sp.cos(w * t), (a - b) * sp.sin(w * t)]           # a e^{iwt} + b e^{-iwt}
print("  psi'' + w^2 psi =", [sp.simplify(sp.diff(c, t, 2) + w ** 2 * c) for c in psi])
Q = sp.simplify(psi[0] * sp.diff(psi[1], t) - psi[1] * sp.diff(psi[0], t))
print("  Noether-Ladung der so(2):  Q =", sp.factor(Q), "; HS(0) (a=b): Q =", Q.subs(a, b))
Kfl = sp.simplify(K1(psi, [sp.diff(c, t) for c in psi], [-1]))
print("  K1(psi, psi') = Q^2 ?", sp.simplify(Kfl - Q ** 2) == 0, "; Zeitumkehr t->-t vertauscht a,b:",
      [sp.simplify(c.subs(t, -t) - c.subs({a: b, b: a}, simultaneous=True)) for c in psi])
print("  u aus der Bahn bei b=0: psi' psi^-1 / w =",
      [sp.simplify(c.subs(b, 0)) for c in scal(1 / (w * a ** 2), mul([sp.diff(c, t) for c in psi], conj(psi), [-1]))], "(= i)")

print("\nS7 Familienteil H3(A_n): Dimensionen und sigma-Identitaet (k282)")
print("  dim H3(A_n) = 3 + 3*2^n:", [3 + 3 * 2 ** n for n in range(4)], " Anhang je Stufe (drei Eintraege b_k l):", [3 * 2 ** n for n in range(3)])
d = sp.symbols("d1:4", real=True); sv = sp.symbols("s1:4", real=True); v = sp.symbols("v1:4", real=True)
W = sp.Matrix([[d[0], sv[2] + sp.I * v[2], sv[1] - sp.I * v[1]],
               [sv[2] - sp.I * v[2], d[1], sv[0] + sp.I * v[0]],
               [sv[1] + sp.I * v[1], sv[0] - sp.I * v[0], d[2]]])
print("  Tr W^2 =", sp.expand((W * W).trace()))
print("  Tr(W sigma W) - (Tr W^2 - 4|v|^2) =", sp.expand((W * W.conjugate()).trace() - (W * W).trace() + 4 * sum(c ** 2 for c in v)))

# ---------------------------------------------------------------- Teil N
print("\n== k290 Teil N (numpy): Symmetrie-Algebren der Terme je Stufe ==")
rng = np.random.default_rng(290)

def table(n, g=None):
    N = 2 ** n; g = g or [-1] * n
    C = np.zeros((N, N, N))
    for i in range(N):
        for j in range(N):
            ei = [1.0 if k == i else 0.0 for k in range(N)]; ej = [1.0 if k == j else 0.0 for k in range(N)]
            C[i, j] = mul(ei, ej, g)
    return C

def funcs(C):
    N = C.shape[0]
    M = lambda x, y: np.einsum("i,j,ijk->k", x, y, C)
    cj = lambda x: np.concatenate([x[:1], -x[1:]])
    nr = lambda x: (x * x).sum()                                   # g = -1: euklidisch; kein komplexes Konjugieren
    F = {
        "N": (1, lambda x: nr(x)),
        "Re": (1, lambda x: x[0]),
        "K1": (2, lambda x, y: nr(x) * nr(y) - (x * y).sum() ** 2),
        "K2": (2, lambda x, y: nr(M(x, y) - M(y, x))),
        "K3": (3, lambda x, y, z: nr(M(M(x, y), z) - M(x, M(y, z)))),
        "K4": (2, lambda x, y: nr(M(x, y)) - nr(x) * nr(y)),
        # Stromvariante: J = psi* d psi statt d psi
        "K2J": (3, lambda p, x, y: nr(M(M(cj(p), x), M(cj(p), y)) - M(M(cj(p), y), M(cj(p), x)))),
        "K3J": (4, lambda p, x, y, z: nr(M(M(M(cj(p), x), M(cj(p), y)), M(cj(p), z)) - M(M(cj(p), x), M(M(cj(p), y), M(cj(p), z))))),
    }
    return F, M

def so_basis(N):
    B = []
    for i, j in itertools.combinations(range(N), 2):
        X = np.zeros((N, N)); X[i, j] = 1; X[j, i] = -1; B.append(X)
    return B

def sym_dim(n, names, fix_u=False, samples=None, uidx=None):
    """Dimension der Unteralgebra von so(2^n), die alle genannten Terme (und ggf. die Einheit u = e_{N/2}) erhaelt."""
    N = 2 ** n; C = table(n); F, M = funcs(C); B = so_basis(N)
    if not B: return 0
    samples = samples or (3 * len(B) // max(1, len(names)) + 10)
    rows = []
    for name in names:
        k, f = F[name]
        for _ in range(samples):
            xs = [rng.normal(size=N) for _ in range(k)]
            rows.append([sum(np.imag(f(*[x + (1e-30j) * (X @ x) if i == j else x for j, x in enumerate(xs)])) for i in range(k)) / 1e-30
                         for X in B])
    if fix_u:
        u = np.zeros(N); u[N // 2 if uidx is None else uidx] = 1
        for r in range(N):
            rows.append([(X @ u)[r] for X in B])
    A = np.array(rows)
    return len(B) - np.linalg.matrix_rank(A, tol=1e-8)

print("Dimension der Symmetrie-Algebra in so(2^n) (kinetischer Term und N(psi) lassen ganz so(2^n) zu):")
sets = [("nur N, K1", ["N", "K1"]), ("+ K2", ["N", "K1", "K2"]), ("+ K3", ["N", "K1", "K2", "K3"]),
        ("+ K4", ["N", "K1", "K2", "K3", "K4"]), ("+ K4 + Re", ["N", "K1", "K2", "K3", "K4", "Re"])]
print("  Terme".ljust(14) + "".join(f"n={n}".rjust(7) for n in range(5)))
for lab, names in sets:
    print(("  " + lab).ljust(14) + "".join(str(sym_dim(n, names)).rjust(7) for n in range(5)))
print("  mit fester Einheit u = l (Stabilisator), alle Terme:")
print("  ".ljust(14) + "".join(str(sym_dim(n, ["N", "K1", "K2", "K3", "K4", "Re"], fix_u=True)).rjust(7) for n in range(5)))
print("  mit fester Einheit u = e1 (aus der untersten Stufe), alle Terme:")
print("  ".ljust(14) + "      -" + "".join(str(sym_dim(n, ["N", "K1", "K2", "K3", "K4", "Re"], fix_u=True, uidx=1)).rjust(7) for n in range(1, 5)))
print("  Vergleich k253: dim Der = 0,0,3,14,14; Stabilisator = 0,0,1,8,8")

print("  Stromvariante (J = psi* d psi): N, K1, Kommutator der Stroeme / dazu Assoziator der Stroeme:")
print("  K2J".ljust(14) + "".join(str(sym_dim(n, ["N", "K1", "K2J"])).rjust(7) for n in range(5)))
print("  K2J + K3J".ljust(14) + "".join(str(sym_dim(n, ["N", "K1", "K2J", "K3J"])).rjust(7) for n in range(5)))

print("\nNur der Term erster Ordnung <psi', u psi> (Zentralisator von L_u in so(2^n)):")
for n in range(1, 5):
    N = 2 ** n; C = table(n); B = so_basis(N); u = np.zeros(N); u[N // 2] = 1
    Lu = np.einsum("i,ijk->kj", u, C)
    A = np.array([(X @ Lu - Lu @ X).ravel() for X in B]).T
    print(f"  n={n}: dim = {len(B) - np.linalg.matrix_rank(A, tol=1e-9)}  (u(2^(n-1)) haette {4 ** (n - 1)}),  |L_u^2 + 1| = {np.abs(Lu @ Lu + np.eye(N)).max():.1e}")

print("\nHS(4): Regel fuer allgemeines u und Groesse der Zusatzterme (1000 Zufallspaare, normiert)")
for n in (3, 4):
    N = 2 ** n; C = table(n); F, M = funcs(C); dv = []; k4 = []
    for _ in range(1000):
        u = rng.normal(size=N); u[0] = 0; u /= np.linalg.norm(u)
        x = rng.normal(size=N); x /= np.linalg.norm(x); y = rng.normal(size=N); y /= np.linalg.norm(y)
        dv.append(np.linalg.norm(M(u, M(u, x)) + x)); k4.append(F["K4"][1](x, y))
    print(f"  n={n}: max|u(ux)+x| = {max(dv):.2e};  K4 in [{min(k4):.3f}, {max(k4):.3f}]")

print("\nVorzeichenmuster g (n=3): Zahl der Richtungen mit negativer Norm = negativer Bewegungsenergie im Anhang")
for g in itertools.product((-1, 1), repeat=3):
    sig = [norm([1 if i == j else 0 for i in range(8)], list(g)) for j in range(8)]
    print(f"  g = {g}: (+,-) = ({sig.count(1)},{sig.count(-1)})")

print("\nGeradheit des Anhangs (exakt, rational): Terme(a + b l) = Terme(a - b l), n = 1..4")
import fractions
for n in range(1, 5):
    N = 2 ** n; g = [-1] * n
    rv = lambda: [fractions.Fraction(int(k), 3) for k in rng.integers(-5, 6, size=N)]
    x, y, z = rv(), rv(), rv(); sg = lambda v: v[:N // 2] + [-c for c in v[N // 2:]]
    ok = (K1(x, y, g) == K1(sg(x), sg(y), g) and K2(x, y, g) == K2(sg(x), sg(y), g)
          and K3(x, y, z, g) == K3(sg(x), sg(y), sg(z), g) and K4(x, y, g) == K4(sg(x), sg(y), g))
    low = [K1(x[:N // 2] + [0] * (N // 2), y[:N // 2] + [0] * (N // 2), g) == K1(x[:N // 2], y[:N // 2], g[:-1])]
    print(f"  n={n}: gerade in b: {ok}; Einschraenkung b=0 gibt den Term der Vorstufe: {all(low)}")
