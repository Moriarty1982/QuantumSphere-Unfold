"""k391c (nachtraeglich, kein Test): dieselbe Form fuer beide Sektoren. m = (a l_k + b l_k^2) / ((l_i + l_j)^2 / 2), Zuordnung B.
Aufruf: python k391c_nachtrag.py > k391c_out.txt"""
import itertools
import numpy as np
rng = np.random.default_rng(3911)
l = np.sort([1 + np.sqrt(2) * np.cos(2 / 9 + 2 * np.pi * k / 3) for k in range(3)]); prs = [(0, 1, 2), (0, 2, 1), (1, 2, 0)]
Rdef = [lambda i, j, k: k, lambda i, j, k: k * k, lambda i, j, k: i * j, lambda i, j, k: i * j - k * k / 2, lambda i, j, k: 1.0, lambda i, j, k: i + j,
        lambda i, j, k: i * i + j * j, lambda i, j, k: (i * i + j * j) / 2 + i * j, lambda i, j, k: k * (i + j)]
FR = np.array([[f(l[i], l[j], l[k]) for (i, j, k) in prs] for f in Rdef]); nR = 9
md = np.array([1.54e-5, 3.06e-4, 1.630e-2]); sd = np.array([0.02e-5, 0.04e-4, 0.009e-2]); mu = np.array([7.04e-6, 3.56e-3, 0.967]); su = np.array([0.15e-6, 0.06e-3, 0.004])
print("== Form m = (a l_k + b l_k^2) / z, z = (l_i + l_j)^2 / 2, Zuordnung B (Generation 1 = Paar (mu tau)) ==")
perm = [2, 1, 0]; f1, f2, z = FR[0, perm], FR[1, perm], FR[7, perm]
for nm, m, s in (("Up", mu, su), ("Down", md, sd)):
    A = np.stack([f1 / z, f2 / z], axis=1) / s[:, None]; co, *_ = np.linalg.lstsq(A, m / s, rcond=None); fit = (co[0] * f1 + co[1] * f2) / z
    print(f"   {nm:4s}: a = {co[0]:.6e}, b = {co[1]:.6e}, b/a = {co[1] / co[0]:.4f}; Massen Modell {np.array2string(fit, precision=4)} gegen Daten {np.array2string(m, precision=4)}; Abstaende {np.array2string((fit - m) / s, precision=2)} sigma; chi^2 = {np.sum(((fit - m) / s)**2):.2f} (1 Freiheitsgrad)")
print("   Je Sektor zwei angepasste Zahlen (a, b) fuer drei Massen: eine Vorhersage je Sektor. Down liegt nahe an l_k / z (b/a klein), Up nahe an l_k^2 / z.")
print("\n== Wie oft trifft dieselbe Form (gleiche zwei Potentialfunktionen bis auf lineare Abhaengigkeit, gleiches z, gleiche Lesart und Zuordnung) beide Sektoren zufaellig? ==")
les = {"sqrt": (np.sqrt, lambda m: 0.5 / np.sqrt(m)), "m": (lambda m: m, lambda m: np.ones_like(m)), "m2": (lambda m: m**2, lambda m: 2 * m)}
tri = np.array([(f, g, zz) for zz in range(nR) for f, g in itertools.combinations(range(nR), 2)])
def trip(X, sX, Fm):
    c = np.cross(Fm[tri[:, 0]], Fm[tri[:, 1]]); zz = Fm[tri[:, 2]]; nc = np.linalg.norm(c, axis=1)
    d = np.abs(np.sum(c * zz * X, axis=1)) / np.sqrt(np.sum(c**2 * zz**2 * sX**2, axis=1))
    return np.where(nc > 1e-9 * np.linalg.norm(Fm[tri[:, 0]], axis=1) * np.linalg.norm(Fm[tri[:, 1]], axis=1), d, np.inf)
def same(mu, su, md, sd):
    n = 0
    for fx, dfx in les.values():
        for p in ([0, 1, 2], [2, 1, 0]):
            Fm = FR[:, p]; tu = trip(fx(mu), np.abs(dfx(mu)) * su, Fm); td = trip(fx(md), np.abs(dfx(md)) * sd, Fm); n += int(((tu < 3) & (td < 3)).sum())
    return n
print(f"   echte Daten: {same(mu, su, md, sd)} Tripel treffen beide Sektoren zugleich (linear abhaengige Schreibweisen zaehlen einzeln)")
NF = 2000; hit = 0
for _ in range(NF):
    fake = []
    for s, m in ((su, mu), (sd, md)):
        m2 = 10 ** rng.uniform(-3.5, -0.5); m1 = m2 * 10 ** rng.uniform(-3.5, -0.5); mf = np.array([m1, m2, 1.0]); fake += [mf, mf * s / m]
    hit += same(*fake) > 0
print(f"   Zufallskontrolle ({NF} erfundene Datensaetze): mindestens ein gemeinsames Tripel in {hit / NF:.2%} der Faelle")
