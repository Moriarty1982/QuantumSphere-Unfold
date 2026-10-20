"""k25: Test der Vorab-Notiz H7 (Commit e6da7db): Heisenberg-Kompensator J als Auswahlkriterium."""
import numpy as np, contextlib, io, os
here = os.path.dirname(os.path.abspath(__file__))
with contextlib.redirect_stdout(io.StringIO()):
    exec(open(os.path.join(here, "k23_test_h6.py")).read())

signs = [M for M in G if perm_of(M) == tuple(range(1, 8)) and not np.allclose(M, np.eye(7))]
def fixed_line(Jk):
    d = np.diag(Jk); return tuple(i for i in range(1, 8) if d[i-1] == 1)
print("Vorzeichen-Automorphismen:", [fixed_line(Jk) for Jk in signs])
J_haupt = [Jk for Jk in signs if Jk[0, 0] == -1 and Jk[6, 6] == 1]
print("J-Haupt (negiert e1, haelt e7):", [fixed_line(Jk) for Jk in J_haupt])

def unique_vec(C):
    ev, EV = np.linalg.eig(C); vals = np.round(ev.real).astype(int)
    s = [i for i in range(3) if list(vals).count(vals[i]) == 1][0]
    return EV[:, s]

def lifts_rel(g3):
    w, Vv = np.linalg.eig(cmat(g3)); i1 = int(np.argmin(abs(w - 1)))
    out = {"TM1": [], "TBM3": []}
    for M, C in zip(H, R):
        if ordn(C) != 2: continue
        coef = np.linalg.solve(Vv, unique_vec(C)); mod = np.abs(coef)**2/np.sum(np.abs(coef)**2)
        if np.isclose(mod[i1], 2/3): out["TM1"].append((M, C))
        elif np.isclose(mod[i1], 0): out["TBM3"].append((M, C))
    return out

overall = {}
for k, g3 in enumerate(lifts3):
    L_ = lifts_rel(g3)
    print(f"\n=== Dreier-Lift {k} ===")
    for Jk in signs:
        tag = ("J-Haupt " if any(np.allclose(Jk, x) for x in J_haupt) else "J-Neben ") + str(fixed_line(Jk))
        inStab = Jk[6, 6] == 1
        row = {"K4": np.allclose(g3 @ Jk, Jk @ g3)}
        for t in ("TM1", "TBM3"):
            k1 = [np.allclose(M @ Jk, Jk @ M) for M, C in L_[t]]
            if inStab:
                CJ = cmat(Jk)
                k2 = [np.allclose(CJ @ (u := unique_vec(C)), (u.conj() @ CJ @ u) * u, atol=1e-8) for M, C in L_[t]]
                k3 = [k2_ and np.isclose((u := unique_vec(C)).conj() @ CJ @ u, 1) for (M, C), k2_ in zip(L_[t], k2)]
            else:
                k2 = k3 = None
            row[t] = (k1, k2, k3)
        def s(x): return "n/a" if x is None else ("alle" if all(x) else "keine" if not any(x) else f"{sum(x)}/{len(x)}")
        print(f"  {tag:22s} K4(g3,J kommutieren)={'ja ' if row['K4'] else 'nein'} | "
              f"TM1: K1={s(row['TM1'][0])}, K2={s(row['TM1'][1])}, K3={s(row['TM1'][2])} | "
              f"TBM3: K1={s(row['TBM3'][0])}, K2={s(row['TBM3'][1])}, K3={s(row['TBM3'][2])}")
        overall.setdefault(tag, []).append((s(row['TM1'][0]), s(row['TBM3'][0]), s(row['TM1'][1]), s(row['TBM3'][1]),
                                            s(row['TM1'][2]), s(row['TBM3'][2])))
print("\nTrennt K1 (Haupt) irgendwo? ",
      any(a != b for v in overall.values() for (a, b, *_ ) in v))
print("Trennen K2/K3 irgendwo?     ",
      any((c != d) or (e != f) for v in overall.values() for (_, _, c, d, e, f) in v))

# Zusatz: der Vorzeichen-Automorphismus mit fester Linie (1,2,3) = Cayley-Dickson-Involution p + q l -> p - q l?
Jcd = [Jk for Jk in signs if fixed_line(Jk) == (1, 2, 3)][0]
print("\nZusatz: J mit fester Linie (1,2,3):", np.diag(Jcd).astype(int).tolist(),
      "= Cayley-Dickson-Involution (e1,e2,e3 fest, e4..e7 negiert)")
print(f"  kommutiert mit {sum(np.allclose(Jcd @ M, M @ Jcd) for M in H)} von 96 Elementen von Stab(+e7)")
print("  kommutiert mit allen vier Triolen-Lifts:", all(np.allclose(Jcd @ g, g @ Jcd) for g in lifts3))
alle = lifts_rel(lifts3[3]); inv = [M for t in alle for M, C in alle[t]]
print(f"  kommutiert mit allen {len(inv)} TM1- und theta13=0-Involutionen:", all(np.allclose(Jcd @ M, M @ Jcd) for M in inv))
Jc = np.zeros((6, 6))
for kk in range(1, 7):
    s_, m_ = T[7, kk]; Jc[m_-1, kk-1] = s_
A = Jcd[:6, :6]
print("  antikommutiert mit der komplexen Struktur (also antilinear auf dem Triplett):", np.allclose(A @ Jc, -Jc @ A))
