"""k23: Auswertung der Vorab-Notiz H6 (Commit e1e2393): Kriterien A-H fuer TM1-Lift gegen theta13=0-Lift."""
import numpy as np, contextlib, io, os
src = open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "k22_oktonion_triplett.py")).read().split("# Mischung:")[0]
with contextlib.redirect_stdout(io.StringIO()):
    exec(src)

def perm_of(M): return tuple(int(np.argmax(abs(M[:, i]))) + 1 for i in range(7))
def signs_on(M, idx): return [int(M[perm_of(M)[i-1]-1, i-1]) for i in idx]
def gen_order(gens):
    els = [np.eye(7)]; frontier = [np.eye(7)]; seen = {tuple(np.eye(7).flatten())}
    while frontier:
        new = []
        for x in frontier:
            for g in gens:
                y = g @ x; k = tuple(np.round(y).flatten())
                if k not in seen: seen.add(k); new.append(y)
        frontier = new
    return len(seen)
kernel = [M for M in H if perm_of(M) == tuple(range(1, 8)) and not np.allclose(M, np.eye(7))]
L = (1, 2, 3)

lifts3 = [M for M in H if perm_of(M)[3:6] == (5, 6, 4) and ordn(cmat(M)) == 3]
print(f"Lifts der Ordnung 3 von e4->e5->e6 (e7 fest): {len(lifts3)}")
for k, g in enumerate(lifts3):
    sf = all(s == 1 for s in signs_on(g, range(1, 8)))
    print(f"  Lift {k}: Bilder " + ", ".join(f"e{i}->{'+' if g[perm_of(g)[i-1]-1, i-1] > 0 else '-'}e{perm_of(g)[i-1]}"
                                         for i in range(1, 8)) + ("   <- vorzeichenfrei" if sf else ""))

def classify(g3):
    C3 = cmat(g3); w, V = np.linalg.eig(C3); i1 = int(np.argmin(abs(w - 1)))
    fixvec = V[:, i1]
    out = []
    for M, C in zip(H, R):
        if ordn(C) != 2: continue
        p = perm_of(M); moved = [i for i in range(1, 8) if p[i-1] != i]
        if not moved: continue
        cen = [c for c in range(1, 8) if p[c-1] == c and all(T[i, p[i-1]][1] == c for i in moved)]
        if not cen or cen[0] not in L: continue
        ev, EV = np.linalg.eig(C); vals = np.round(ev.real).astype(int)
        s = [i for i in range(3) if list(vals).count(vals[i]) == 1][0]
        coef = np.linalg.solve(V, EV[:, s]); mod = np.abs(coef)**2/np.sum(np.abs(coef)**2)
        typ = "TM1" if np.isclose(mod[i1], 2/3, atol=1e-6) else ("TBM3" if np.isclose(mod[i1], 0, atol=1e-6) else f"?{mod[i1]:.3f}")
        crit = {
            "A": np.allclose(M @ g3 @ M, np.linalg.inv(g3)),
            "B": np.allclose(M @ g3, g3 @ M),
            "C": gen_order([g3, M]) == 24,
            "D": np.allclose(C.imag, 0) and all(np.count_nonzero(np.round(abs(C[:, j]), 6)) == 1 for j in range(3)),
            "E": all(s == 1 for s in signs_on(M, (1, 2, 3))),
            "F": all(s == 1 for s in signs_on(M, (4, 5, 6))),
            "G": all(np.allclose(M @ K, K @ M) for K in kernel),
            "H": np.allclose(C @ fixvec, (fixvec.conj() @ C @ fixvec) * fixvec, atol=1e-8),
        }
        out.append((cen[0], typ, crit, gen_order([g3, M])))
    return out

summary = []
for k, g in enumerate(lifts3):
    res = classify(g)
    print(f"\n=== Dreier-Lift {k} ===")
    for cen, typ, crit, go in sorted(res, key=lambda r: (r[1], r[0])):
        print(f"  Zentrum e{cen}  {typ:5s}  " + " ".join(f"{c}={'ja ' if v else 'nein'}" for c, v in crit.items()) + f"  |<g3,h>|={go}")
    verdict = {}
    for c in "ABCDEFGH":
        tm1 = {r[2][c] for r in res if r[1] == "TM1"}; tb = {r[2][c] for r in res if r[1] == "TBM3"}
        if tm1 == {True} and tb == {False}: verdict[c] = "TM1"
        elif tm1 == {False} and tb == {True}: verdict[c] = "TBM3"
        elif tm1 == tb and len(tm1) == 1: verdict[c] = "beide" if True in tm1 else "keine"
        else: verdict[c] = "gemischt"
    print("  Trennung: " + ", ".join(f"{c}: {v}" for c, v in verdict.items()))
    summary.append(verdict)
print("\nHaengt das Ergebnis vom Lift ab?",
      {c: sorted({v[c] for v in summary}) for c in "ABCDEFGH"})

# Zusatz: Ist <g3, h_TM1> mit Ordnung 24 isomorph zu S4? (Ordnungsstatistik), und <g3, h_TBM3> zu S3?
from collections import Counter
def gen_elems(gens):
    seen = {tuple(np.round(np.eye(7)).flatten()): np.eye(7)}; frontier = [np.eye(7)]
    while frontier:
        new = []
        for x in frontier:
            for g in gens:
                y = g @ x; k = tuple(np.round(y).flatten())
                if k not in seen: seen[k] = y; new.append(y)
        frontier = new
    return list(seen.values())
def ord7(M):
    X = M.copy(); k = 1
    while not np.allclose(X, np.eye(7)): X = X @ M; k += 1
    return k
g3 = lifts3[3]                       # vorzeichenfreier Companion-Lift
hs = {}
w, V = np.linalg.eig(cmat(g3)); i1 = int(np.argmin(abs(w - 1)))
for M, C in zip(H, R):
    if ordn(C) != 2: continue
    ev, EV = np.linalg.eig(C); vals = np.round(ev.real).astype(int)
    s = [i for i in range(3) if list(vals).count(vals[i]) == 1][0]
    coef = np.linalg.solve(V, EV[:, s]); mod = np.abs(coef)**2/np.sum(np.abs(coef)**2)
    t = "TM1" if np.isclose(mod[i1], 2/3) else "TBM3" if np.isclose(mod[i1], 0) else None
    if t and t not in hs: hs[t] = M
for t, M in hs.items():
    els = gen_elems([g3, M])
    print(f"<g3, h_{t}>: Ordnung {len(els)}, Elementordnungen {sorted(Counter(ord7(x) for x in els).items())}")
print("S4: [(1,1),(2,9),(3,8),(4,6)];  S3: [(1,1),(2,3),(3,2)]")
