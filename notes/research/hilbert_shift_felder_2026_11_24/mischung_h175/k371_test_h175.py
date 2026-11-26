"""k371 (Test H175, Vorab-Notiz 9135e83 vom 26.11.2026): Term aus der Ladungsrichtung (s-v-Kopplung) fuer die kleine Drehung der geladenen Leptonen.
Aufruf aus diesem Ordner: python3 k371_test_h175.py > k371_out.txt
"""
import numpy as np
from scipy.optimize import least_squares, minimize
src = open("../mischung_h174/k370_test_h174.py").read().split('print("== Kontrolle')[0]
ns = {}; exec(src, ns)
C, Nhat, eig_sorted, pmns, z, line, SQ = (ns[k] for k in ("C", "Nhat", "eig_sorted", "pmns", "z", "line", "SQ"))
X_LEP, X_R, DSTAR = ns["X_LEP"], ns["X_R"], ns["DSTAR"]
DE = DSTAR + 2 * np.pi / 3
tgt = SQ / SQ[2]
r2 = np.sqrt(2)


def E(i, j):
    M = np.zeros((3, 3)); M[i, j] = 1; return M


DIRS = {  # hermitesche Richtungen: reell symmetrisch S oder i*K mit K reell antisymmetrisch
    "S+b": (E(0, 1) + E(1, 0) - E(1, 2) - E(2, 1)) / r2,
    "S+c": E(0, 2) + E(2, 0),
    "S+d": E(1, 1),
    "S-p": (E(0, 1) + E(1, 0) + E(1, 2) + E(2, 1)) / r2,
    "S-q": (E(0, 0) - E(2, 2)) / r2,
    "K+":  1j * (E(0, 1) - E(1, 0) + E(1, 2) - E(2, 1)) / r2,
    "K-1": 1j * (E(0, 2) - E(2, 0)),
    "K-2": 1j * (-E(0, 1) + E(1, 0) + E(1, 2) - E(2, 1)) / r2,
}
CLASSES = {"antisymmetrisch A-ungerade (Ladungsrichtung, Hypothese)": ["K-1", "K-2"], "antisymmetrisch A-gerade": ["K+"],
           "symmetrisch A-gerade": ["S+b", "S+c", "S+d"], "symmetrisch A-ungerade": ["S-p", "S-q"]}


def solve(P, x, start=(1.0, None)):
    """Massen exakt anpassen; gibt (rho, delta, Ue) oder None."""
    f = lambda p: np.sort(abs(np.linalg.eigvalsh(C(p[0], p[1]) + P)))
    res = lambda p: (f(p)[:2] / f(p)[2] - tgt[:2]) / tgt[:2]
    r = least_squares(res, [start[0], DE if start[1] is None else start[1]], xtol=1e-15, ftol=1e-15, gtol=1e-15)
    if np.max(abs(r.fun)) > 1e-8 or abs(r.x[1] - DE) > 0.5:
        return None
    return r.x[0], r.x[1], eig_sorted(C(r.x[0], r.x[1]) + P)[1]


def make(x):
    Un = eig_sorted(Nhat(np.pi / 6 - x, 1))[1]
    def obs(names, coef):
        P = sum(c * DIRS[n] for n, c in zip(names, coef))
        s = solve(P, x)
        if s is None: return None
        return s[0], s[1], pmns(s[2], Un)
    def chi2(names, coef):
        o = obs(names, coef)
        return 1e6 if o is None else float(sum(np.array(z(*o[2][:3]))**2))
    return obs, chi2


def ok(zz): return abs(zz[0]) < 2 and abs(zz[1]) < 2 and abs(zz[2]) < 3


if __name__ == "__main__":
    rng = np.random.default_rng(371)
    for name, x in (("x", X_LEP), ("x_R (Kontrolle)", X_R)):
        obs, chi2 = make(x)
        print(f"===== Versatz {name} = {x} =====")
        o = obs([], []); print("Kontrolle ohne Term: " + line(o[2]))
        print("== H175a: Anpassung je Symmetrieklasse ==")
        for cl, names in CLASSES.items():
            best = None
            starts = [np.zeros(len(names))] + [rng.normal(0, 0.05, len(names)) for _ in range(40)]
            for s0 in starts:
                r = minimize(lambda c: chi2(names, c), s0, method='Nelder-Mead', options={'xatol': 1e-9, 'fatol': 1e-10, 'maxiter': 4000})
                if best is None or r.fun < best.fun - 1e-9: best = r
            o = obs(names, best.x); zz = z(*o[2][:3])
            print(f"   {cl}: {dict(zip(names, np.round(best.x, 5)))}, chi2 = {best.fun:.2f} ({len(names)} Parameter); rho = {o[0]:.5f} (K = {(1 + o[0]**2)/3:.5f}); " + line(o[2]) + f"; 2s/2s/3s: {ok(zz)}")
        print("== H175b: je eine Richtung allein, Staerke frei ==")
        for n in DIRS:
            ks = np.linspace(-0.3, 0.3, 601); v = np.array([chi2([n], [k]) for k in ks])
            # alle lokalen Minima
            mins = [i for i in range(1, len(ks) - 1) if v[i] < v[i - 1] and v[i] <= v[i + 1] and v[i] < 1e5]
            out = []
            for i in mins:
                r = minimize(lambda c: chi2([n], c), [ks[i]], method='Nelder-Mead', options={'xatol': 1e-10, 'fatol': 1e-11})
                out.append((r.fun, r.x[0]))
            out.sort()
            for c2, k in out[:2]:
                o = obs([n], [k]); zz = z(*o[2][:3])
                print(f"   {n}: kappa = {k:+.5f}, chi2 = {c2:.2f}; rho = {o[0]:.5f}; " + line(o[2]) + f"; 2s/2s/3s: {ok(zz)}")
        print("== H175c: feste Staerke in der Ladungsrichtung (16 Faelle; die Vorab-Notiz nennt irrtuemlich 24, festgelegt waren 4 Staerken mal 4 Richtungen) ==")
        nf = n3 = nok = 0; rows = []
        for lab, k0 in (("tan x", np.tan(x)), ("tan 2x", np.tan(2 * x))):
            for sg in (1, -1):
                for dn, vec in (("K-1", (1, 0)), ("K-2", (0, 1)), ("(K-1 + K-2)/sqrt2", (1 / r2, 1 / r2)), ("(K-1 - K-2)/sqrt2", (1 / r2, -1 / r2))):
                    o = obs(["K-1", "K-2"], sg * k0 * np.array(vec)); nf += 1
                    if o is None:
                        print(f"   kappa = {'+' if sg > 0 else '-'}{lab}, {dn}: Massen nicht erreichbar"); continue
                    zz = z(*o[2][:3]); n3 += abs(zz[0]) < 3; nok += ok(zz)
                    print(f"   kappa = {'+' if sg > 0 else '-'}{lab} = {sg*k0:+.5f}, {dn}: rho = {o[0]:.5f}; " + line(o[2]))
        print(f"   Faelle: {nf}; vertraeglich 2s/2s/3s: {nok}; th13 innerhalb 3 sigma: {n3}")
