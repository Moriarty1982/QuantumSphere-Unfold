"""k391 (Test H188): Ableitungsterme der Feldgleichung und die Quarkmassen.
Vorab: Vorab_Notiz_H188_Ableitungsterme_und_Quarkmassen.md (Commit bb9da71).
Aufruf: python k391_test_h188.py > k391_out.txt"""
import itertools
import numpy as np
import sympy as sp
rng = np.random.default_rng(391)
def conj(x):
    y = -x.copy(); y[0] = x[0]; return y
def mul(x, y):
    n = len(x)
    if n == 1: return x * y
    h = n // 2; a, b, c, d = x[:h], x[h:], y[:h], y[h:]
    return np.concatenate([mul(a, c) - mul(conj(d), b), mul(d, a) + mul(b, conj(c))])
e = np.eye(8); C = np.array([[mul(e[i], e[j]) for j in range(8)] for i in range(8)])
cj = np.diag([1.0] + [-1.0] * 7)
PAIRS = [(0, 1), (1, 2), (2, 0)]
def toW(v):
    W = np.zeros((3, 3, 8))
    for i in range(3): W[i, i, 0] = v[i]
    for s, (i, j) in enumerate(PAIRS):
        x = v[3 + 8 * s: 11 + 8 * s]; W[i, j] = x; W[j, i] = cj @ x
    return W
mm = lambda X, Y: np.einsum('ija,jkb,abc->ikc', X, Y, C)
N = lambda X: np.sum(X * X)                                            # Normquadrat (Summe der Betragsquadrate der Eintraege)
ip = lambda X, Y: np.sum(X * Y)
K1 = lambda X, Y: N(X) * N(Y) - ip(X, Y)**2                             # Flaechenterm
K2 = lambda X, Y: N(mm(X, Y) - mm(Y, X))                               # Kommutatorterm
def assoc(X, Y, Z): return mm(mm(X, Y), Z) - mm(X, mm(Y, Z))
K3 = lambda X, Y: N(assoc(X, Y, X)) + N(assoc(X, X, Y))                # Assoziatorterm (zwei Richtungen)
K4 = lambda X, Y: N(mm(X, Y)) - N(X) * N(Y)                             # Normdefekt
def W0(a, r, delta):
    v = np.zeros(27); v[:3] = a
    for s in range(3): v[3 + 8 * s] = r * np.cos(delta); v[3 + 8 * s + 7] = r * np.sin(delta)
    return v

print("== H188a: Ordnung von K1 bis K4 in der Stoerung (ruhendes, homogenes Vakuum) ==")
print("   X_mu = d_mu W = d_mu (W0 + eps dW) = eps d_mu dW, weil d_mu W0 = 0. Ganzzahlige Zufallsrichtungen A = d_t dW, B = d_x dW (exakt in float64).")
eps = sp.Symbol('eps'); pts = [1, 2, 3, 4, 5, 6, 7]
A = toW(rng.integers(-3, 4, size=27).astype(float)); B = toW(rng.integers(-3, 4, size=27).astype(float))
ok_a = True
for name, K in (("K1", K1), ("K2", K2), ("K3", K3), ("K4", K4)):
    vals = [sp.Integer(int(round(K(p * A, p * B)))) for p in pts]
    pol = sp.Poly(sp.interpolate(list(zip(pts, vals)), eps), eps); co = pol.all_coeffs()[::-1]; co += [0] * (7 - len(co))
    low = co[:4]; ok_a &= all(c == 0 for c in low)
    print(f"   {name}(eps A, eps B) = {sp.factor(pol.as_expr())};  Koeffizienten eps^0..eps^3: {low}")
print("   Urteil H188a:", "BESTAETIGT (nicht blind): niedrigste Ordnung ist eps^4, kein Beitrag zu kleinen Schwingungen" if ok_a else "WIDERLEGT")
print("\n   Gegenstueck (nachtraeglich, nur Ordnungsabzaehlung, keine Loesung der Feldgleichung): Hintergrund mit X_t = B0 != 0 (rotierendes Vakuum)")
w0 = toW(W0(1.0, 1 / np.sqrt(2), 2.0 / 9.0)); B0i = np.zeros((3, 3, 8)); B0i[:, :, 7] = np.round(4 * w0[:, :, 0]); B0i[:, :, 0] = -np.round(4 * w0[:, :, 7])   # ~ U W0, ganzzahlig gerundet
for name, K in (("K1", K1), ("K2", K2), ("K3", K3), ("K4", K4)):
    vals = [sp.Integer(int(round(K(B0i + p * A, p * B)))) for p in pts]
    pol = sp.Poly(sp.interpolate(list(zip(pts, vals)), eps), eps); co = pol.all_coeffs()[::-1]
    print(f"   {name}(B0 + eps A, eps B): Koeffizient eps^2 = {co[2] if len(co) > 2 else 0}")

print("\n== H188b, c: kinetische Form aus dem Vakuum, X = h/z je Paar ==")
def ls(a, r, d): return np.sort([a + 2 * r * np.cos(d + 2 * np.pi * k / 3) for k in range(3)])
l0 = ls(1.0, 1 / np.sqrt(2), 2.0 / 9.0); print(f"   Eigenwerte des Vakuums l = {np.round(l0, 6)}")
prs = [(0, 1, 2), (0, 2, 1), (1, 2, 0)]
Rdef = [("l_k", lambda i, j, k: k), ("l_k^2", lambda i, j, k: k * k), ("l_i l_j", lambda i, j, k: i * j), ("l_i l_j - l_k^2/2", lambda i, j, k: i * j - k * k / 2),
        ("1", lambda i, j, k: 1.0), ("l_i + l_j", lambda i, j, k: i + j), ("l_i^2 + l_j^2", lambda i, j, k: i * i + j * j),
        ("(l_i^2 + l_j^2)/2 + l_i l_j", lambda i, j, k: (i * i + j * j) / 2 + i * j), ("l_k (l_i + l_j)", lambda i, j, k: k * (i + j))]
names = [n for n, _ in Rdef]; FR = np.array([[f(l0[i], l0[j], l0[k]) for (i, j, k) in prs] for _, f in Rdef]); nR = len(Rdef)
print("   Funktionsmenge R (wie H187), Werte je Paar (e mu), (e tau), (mu tau):")
for n_, (nm, v) in enumerate(zip(names, FR)): print(f"      f{n_ + 1} = {nm:28s} {np.array2string(v, precision=6)}{'   (wechselt das Vorzeichen: als kinetische Form nicht positiv)' if v.min() < 0 < v.max() else ''}")
md_ = np.array([1.54e-5, 3.06e-4, 1.630e-2]); sd_ = np.array([0.02e-5, 0.04e-4, 0.009e-2]); mu_ = np.array([7.04e-6, 3.56e-3, 0.967]); su_ = np.array([0.15e-6, 0.06e-3, 0.004])
les = {"X = sqrt(m)": (np.sqrt, lambda m: 0.5 / np.sqrt(m)), "X = m": (lambda m: m, lambda m: np.ones_like(m)), "X = m^2": (lambda m: m**2, lambda m: 2 * m)}
zu = {"A": [0, 1, 2], "B": [2, 1, 0]}
quo = [(f, z) for f in range(nR) for z in range(nR) if f != z]
tri = [(f, g, z) for z in range(nR) for f, g in itertools.combinations(range(nR), 2)]
Fq = np.array(quo); Ft = np.array(tri)
def quot(X, sX, Fm):
    """je Quotient f/z: groesster Abstand der zwei Verhaeltnisse in sigma."""
    r = X[:2] / X[2]; sr = np.abs(r) * np.sqrt((sX[:2] / X[:2])**2 + (sX[2] / X[2])**2)
    Q = Fm[Fq[:, 0]] / Fm[Fq[:, 1]]
    with np.errstate(divide='ignore', invalid='ignore'): d = np.abs((Q[:, :2] / Q[:, 2:3] - r) / sr).max(axis=1)
    return np.where(np.isfinite(d), d, np.inf)
def trip(X, sX, Fm):
    """det[X z, f, g] = 0: Abstand in sigma je Tripel (f, g, z)."""
    c = np.cross(Fm[Ft[:, 0]], Fm[Ft[:, 1]]); z = Fm[Ft[:, 2]]; nc = np.linalg.norm(c, axis=1)
    d = np.abs(np.sum(c * z * X, axis=1)) / np.sqrt(np.sum(c**2 * z**2 * sX**2, axis=1))
    return np.where(nc > 1e-9 * np.linalg.norm(Fm[Ft[:, 0]], axis=1) * np.linalg.norm(Fm[Ft[:, 1]], axis=1), d, np.inf)
def search(mu, su, md, sd, verbose=False):
    hb = hc = False; rows = []
    for ln, (fx, dfx) in les.items():
        for zn, perm in zu.items():
            Fm = FR[:, perm]; res = []
            for nm, m, s in (("Up", mu, su), ("Down", md, sd)):
                X = fx(m); sX = np.abs(dfx(m)) * s; q = quot(X, sX, Fm); t = trip(X, sX, Fm); res.append((nm, q, t))
            hb |= all(r[1].min() < 3 for r in res); hc |= all(r[2].min() < 3 for r in res)
            if verbose:
                print(f"   {ln}, Zuordnung {zn}:")
                for nm, q, t in res:
                    iq = int(np.argmin(q)); it = int(np.argmin(t))
                    print(f"      {nm:4s}: bester Quotient f{quo[iq][0] + 1}/f{quo[iq][1] + 1} {q[iq]:.2f} sigma ({int((q < 3).sum())} unter 3 sigma); bestes Tripel (f{tri[it][0] + 1}, f{tri[it][1] + 1})/f{tri[it][2] + 1} {t[it]:.2f} sigma ({int((t < 3).sum())} unter 3 sigma)")
                    for i_ in np.where(q < 3)[0]: print(f"            Quotient f{quo[i_][0] + 1}/f{quo[i_][1] + 1}: {q[i_]:.2f} sigma")
                    for i_ in np.where(t < 3)[0]: print(f"            Tripel (f{tri[i_][0] + 1}, f{tri[i_][1] + 1})/f{tri[i_][2] + 1}: {t[i_]:.2f} sigma")
                rows.append((ln, zn, [r[1].min() for r in res], [r[2].min() for r in res]))
    return hb, hc
hb, hc = search(mu_, su_, md_, sd_, verbose=True)
print(f"   verglichen: {len(quo)} Quotienten und {len(tri)} Tripel je Sektor, je 3 Lesarten und 2 Zuordnungen")
NF = 2000; cb_ = cc_ = 0
for _ in range(NF):
    fake = []
    for s, m in ((su_, mu_), (sd_, md_)):
        m2 = 10 ** rng.uniform(-3.5, -0.5); m1 = m2 * 10 ** rng.uniform(-3.5, -0.5); mf = np.array([m1, m2, 1.0]); fake += [mf, mf * s / m]
    b_, c_ = search(fake[0], fake[1], fake[2], fake[3]); cb_ += b_; cc_ += c_
print(f"   Zufallskontrolle ({NF} erfundene Datensaetze): Treffer mit einem Quotienten {cb_ / NF:.2%}, mit einem Tripel {cc_ / NF:.2%}")
for lab, h, q, txt in (("H188b", hb, cb_ / NF, "kein Quotient trifft beide Verhaeltnisse in beiden Sektoren"), ("H188c", hc, cc_ / NF, "kein Tripel trifft beide Sektoren innerhalb von 3 sigma")):
    if not h: print(f"   Urteil {lab}: WIDERLEGT ({txt})")
    elif q < 0.05: print(f"   Urteil {lab}: BESTAETIGT als Kandidat (Treffer, Zufallsquote unter 5 %); eigener Vorab-Test noetig")
    else: print(f"   Urteil {lab}: OHNE URTEIL (Treffer, aber mit Zufall vertraeglich)")
