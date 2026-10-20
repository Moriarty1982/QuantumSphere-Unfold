"""k27: Test der Vorab-Notiz H10 (Commit a6b5bcb): Assoziator als Auswahlkriterium fuer den TM1-Lift."""
import numpy as np, contextlib, io, os
here = os.path.dirname(os.path.abspath(__file__))
with contextlib.redirect_stdout(io.StringIO()):
    exec(open(os.path.join(here, "k25_test_h7.py")).read())

E8 = np.eye(8)
def assoc(x, y, z): return omul(omul(x, y), z) - omul(x, omul(y, z))
def act(M, x):                       # M (7x7 auf e1..e7) auf ein Oktonion x (8 Komponenten)
    y = x.copy(); y[1:] = M @ x[1:]; return y
a = assoc(E8[4], E8[5], E8[6])
print("[e4,e5,e6] =", np.round(a, 6).tolist())

def im(v7): x = np.zeros(8); x[1:] = v7; return x
def null(A, tol=1e-9):
    _, s, Vt = np.linalg.svd(A); return Vt[np.sum(s > tol):].T

res_all = {}
for k, g3 in enumerate(lifts3):
    L_ = lifts_rel(g3)
    # g3-feste Richtung im reellen Triplett span(e4,e5,e6) (Indizes 3..5 in e1..e7)
    T = np.zeros((7, 3)); T[3, 0] = T[4, 1] = T[5, 2] = 1
    g3T = T.T @ g3 @ T
    fixT = null(g3T - np.eye(3)); sT = T @ fixT[:, 0] if fixT.shape[1] else None
    for t in ("TM1", "TBM3"):
        for M, C in L_[t]:
            s1 = all(np.allclose(assoc(E8[i], act(M, E8[i]), E8[7]), 0) for i in (4, 5, 6))
            u = unique_vec(C); u = u / u[np.argmax(abs(u))]          # Phase: groesste Komponente reell
            wR = np.zeros(7); wI = np.zeros(7)
            for kk, fk in enumerate([3, 4, 5]): wR[fk] = u[kk].real; wI[fk] = u[kk].imag
            if np.allclose(wI, 0): wI = np.concatenate([Jc @ wR[:6], [0]])   # reelle Spalte: J w_R nehmen
            s2 = np.allclose(assoc(im(wR), im(wI), E8[7]), 0)
            s3 = np.allclose(act(M, a), a)
            F = null(M - np.eye(7))                                  # feste Unteralgebra (Imaginaerteil)
            FT = null(np.hstack([F, -T]))                           # Schnitt F mit T
            inter = [F @ c[:F.shape[1]] for c in FT.T]
            s4 = sT is not None and any(abs(abs(v @ sT) - np.linalg.norm(v)*np.linalg.norm(sT)) < 1e-8 for v in inter if np.linalg.norm(v) > 1e-9)
            res_all.setdefault((k, t), []).append((s1, s2, s3, s4, F.shape[1], len(inter)))
for (k, t), rows in sorted(res_all.items()):
    cols = list(zip(*rows))
    f = lambda c: "alle" if all(c) else "keine" if not any(c) else f"{sum(c)}/{len(c)}"
    print(f"Lift {k} {t:4s}: S1={f(cols[0])}, S2={f(cols[1])}, S3={f(cols[2])}, S4={f(cols[3])}"
          f"  (dim fest={set(cols[4])}, dim Schnitt mit Triplett={set(cols[5])})")
def sep(ix):
    out = set()
    for k in range(4):
        tm = {r[ix] for r in res_all[(k, "TM1")]}; tb = {r[ix] for r in res_all[(k, "TBM3")]}
        out.add("TM1" if tm == {True} and tb == {False} else "TBM3" if tm == {False} and tb == {True} else "keine")
    return out
print("\nTrennung je Kriterium ueber alle Lifts:", {n: sep(i) for n, i in (("S1", 0), ("S2", 1), ("S3", 2), ("S4", 3))})
