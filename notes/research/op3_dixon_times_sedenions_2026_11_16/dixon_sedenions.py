"""OP3/Atlas: Was passiert bei C x H x O x S (Dixon-Algebra mal Sedenionen)?  Erkundung, nicht blind (Struktursaetze, nachgerechnet).

(1) Stufe: Dimensionen der Kette C, H, O, S und der Tensorprodukte -> HS(n).
(2) Cayley-Dickson-Basis: e_a e_b = +- e_(a XOR b) fuer C, H, O, S (Einheiten = verdrehte Gruppe Z2^k).
(3) Was S von O unterscheidet: Alternativitaet, Normmultiplikativitaet, Nullteiler.
(4) Linksmultiplikationen L_ei: Quadrat -1?  Groesste Menge paarweise antivertauschender L_ei (Clifford-Erzeuger) auf R^8 bzw. R^16.
(5) Die Einheiten von H = Kleinsche Vierergruppe = Frame-Abbildungen auf chi (bis auf Phase): Bezug zum Kopienregister von HS(8).
"""
import itertools
import numpy as np


def cd_mult(a, b):
    n = len(a)
    if n == 1:
        return a * b
    h = n // 2
    p, q, r, s = a[:h], a[h:], b[:h], b[h:]
    conj = lambda x: np.concatenate([x[:1], -x[1:]])
    return np.concatenate([cd_mult(p, r) - cd_mult(conj(s), q), cd_mult(s, p) + cd_mult(q, conj(r))])


def unit(n, i):
    v = np.zeros(n); v[i] = 1.0; return v


print("(1) Dimensionen (reell) und Stufe HS(n) = 2^n:")
for name, d in (("C x H x O (Dixon)", 2 * 4 * 8), ("C x H x O x C", 2 * 4 * 8 * 2), ("C x H x O x H", 2 * 4 * 8 * 4),
                ("C x H x O x O", 2 * 4 * 8 * 8), ("C x H x O x S", 2 * 4 * 8 * 16), ("C x H x S (O durch S ersetzt)", 2 * 4 * 16)):
    print(f"     {name:32s} {d:5d} = HS({int(np.log2(d))})")

for n, name in ((2, "C"), (4, "H"), (8, "O"), (16, "S")):
    ok = True
    for a in range(n):
        for b in range(n):
            p = cd_mult(unit(n, a), unit(n, b)); k = int(np.argmax(np.abs(p)))
            ok &= (k == a ^ b) and abs(abs(p[k]) - 1) < 1e-12 and np.count_nonzero(np.abs(p) > 1e-12) == 1
    print(f"(2) {name}: e_a e_b = +- e_(a XOR b) fuer alle Basiseinheiten: {ok}")

rng = np.random.default_rng(7)
for n, name in ((8, "O"), (16, "S")):
    alt = norm = 0
    for _ in range(2000):
        x, y = rng.normal(size=n), rng.normal(size=n)
        alt = max(alt, np.linalg.norm(cd_mult(x, cd_mult(x, y)) - cd_mult(cd_mult(x, x), y)))
        norm = max(norm, abs(np.linalg.norm(cd_mult(x, y)) - np.linalg.norm(x) * np.linalg.norm(y)))
    print(f"(3) {name}: max Abweichung Alternativitaet {alt:.2e}, Normmultiplikativitaet {norm:.2e}")

zd = None
for i, j, k, l in itertools.product(range(1, 16), repeat=4):
    if len({i, j, k, l}) < 4 or not (i < j and k < l):
        continue
    for s in (1, -1):
        a = unit(16, i) + unit(16, j); b = unit(16, k) + s * unit(16, l)
        if np.linalg.norm(cd_mult(a, b)) < 1e-12:
            zd = (i, j, k, l, s); break
    if zd: break
print(f"(3) S: Nullteiler (e_{zd[0]} + e_{zd[1]}) (e_{zd[2]} {'+' if zd[4] > 0 else '-'} e_{zd[3]}) = 0" if zd else "(3) S: kein Nullteiler gefunden")

for n, name in ((8, "O"), (16, "S")):
    L = [np.column_stack([cd_mult(unit(n, i), unit(n, j)) for j in range(n)]) for i in range(1, n)]
    sq = all(np.allclose(M @ M, -np.eye(n)) for M in L)
    anti = np.array([[np.allclose(L[i] @ L[j] + L[j] @ L[i], 0) for j in range(n - 1)] for i in range(n - 1)])
    best = []
    for r in range(n - 1, 0, -1):
        for c in itertools.combinations(range(n - 1), r):
            if all(anti[a, b] for a, b in itertools.combinations(c, 2)):
                best = c; break
        if best: break
    print(f"(4) {name}: alle L_ei^2 = -1: {sq}; groesste antivertauschende Menge: {len(best)} von {n-1}"
          f" (Radon-Hurwitz-Grenze auf R^{n}: {7 if n == 8 else 8})")

X = np.array([[0, 1], [1, 0]], complex); Y = np.array([[0, -1j], [1j, 0]]); Z = np.diag([1, -1]).astype(complex)
q = {1: -1j * Z, 2: -1j * X, 3: -1j * Y}
ok = True
for a in (1, 2, 3):
    for b in (1, 2, 3):
        p = cd_mult(unit(4, a), unit(4, b)); k = int(np.argmax(np.abs(p))); sgn = p[k]
        rhs = sgn * (np.eye(2) if k == 0 else q[k])
        ok &= np.allclose(q[a] @ q[b], rhs) or np.allclose(q[a] @ q[b], -rhs)
print(f"(5) Einheiten von H <-> -i sigma (R = sigma_z, T = sigma_x, J_B = sigma_y): Produkte stimmen bis auf Vorzeichen: {ok}")
