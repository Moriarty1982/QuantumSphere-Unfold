"""H216 (k429) Umkehrschleifen und H217 (k430) Flaechenvarianten.

Vorab-Notizen: notes/research/predictions/Vorab_Notiz_H216_Umkehrschleifen.md, ..._H217_Flaechenvarianten.md
Nutzt Klasse und Fixpunktsuche aus k428 (H215). Aufruf: python k429_test_h216.py > k429_out.txt
"""
import itertools
import os
import sys

import numpy as np
from mpmath import mp, mpf, sqrt as msqrt, nsum, findroot, inf

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "stabilitaet_rueckwaerts_h215"))
import k428_test_h215 as K  # noqa: E402

mp.dps = 30
REL = K.REL
CACHE = os.path.join(HERE, "k429_katalog.npz")


def beta_variant(a):
    g = findroot(lambda g: nsum(lambda k: 2 ** (1 - g * a(k)), [1, inf]) - 1, 1.8)
    return g, msqrt((g - 1) / (g + 1))


VARIANTS = {
    "Casimir sqrt(j(j+1))": lambda k: msqrt(k * (k + 2) / mpf(3)),
    "glatt j+1/2": lambda k: (k + 1) / mpf(2),
    "linear j": lambda k: mpf(k),
}


def catalog():
    if os.path.exists(CACHE):
        z = np.load(CACHE)
        return list(z["W"]), z["X"], z["D"], int(z["deg"])
    words = [w for L in range(1, 6) for w in ("".join(t) for t in itertools.product(K.NAMES, repeat=L))]
    W, X, D, deg = [], [], [], 0
    for w in words:
        fp = K.fixpoints(w)
        if fp is None:
            deg += 1
            continue
        for p, d in fp:
            if 1e-6 < p < 1 - 1e-6:
                W.append(w); X.append(p); D.append(d)
    np.savez(CACHE, W=np.array(W), X=np.array(X), D=np.array(D), deg=deg)
    return W, np.array(X), np.array(D), deg


def main():
    W, X, D, deg = catalog()
    W = np.array(W)
    att = np.abs(D) < 1 - 1e-9
    rep = np.abs(D) > 1 + 1e-9
    print("Katalog: Fixpunkte in (0,1)", len(X), " anziehend", att.sum(), " abstossend", rep.sum(),
          " identitaetsartig ausgeschlossen", deg)

    def N(x0, mask, excl=("E",)):
        m = mask & (np.abs(X - x0) <= REL * x0) & ~np.isin(W, excl)
        return len(set(W[m]))

    def hits(x0m, mask):
        x0 = float(x0m)
        m = mask & (np.abs(X - x0) <= REL * x0)
        out = []
        for w in sorted(set(W[m])):
            i = np.nonzero(m & (W == w))[0]
            j = i[np.argmin(np.abs(X[i] - x0))]
            r = abs(K.mapply(w, x0m) - x0m)
            out.append((w, X[j], D[j], r))
        return sorted(out, key=lambda t: t[3])

    rng = np.random.default_rng(215)
    ctrl = rng.uniform(0.35, 0.75, 2000)
    stats = {}
    for name, mask in (("vorwaerts (H215-Klasse)", att), ("umkehr (H216)", rep)):
        nc = np.array([N(x, mask) for x in ctrl])
        stats[name] = (nc, *np.percentile(nc, [95, 99]))
        print(f"Kontrollen {name}: Mittel {nc.mean():.2f}, Median {np.median(nc):.0f}, 95. P. {stats[name][1]:.1f}, "
              f"99. P. {stats[name][2]:.1f}, Max {nc.max()}")

    B = K.BETA_M
    print("\n================ H216 (k429): Umkehrschleifen ================")
    print(f"beta_sym = {mp.nstr(B, 20)}")
    nc, p95, p99 = stats["umkehr (H216)"]
    nb = N(float(B), rep)
    print(f"N_inv(beta_sym) ohne E: {nb}   mit E: {N(float(B), rep, ())}   Anteil Kontrollen >= : {np.mean(nc >= nb):.4f}")
    hb = hits(B, rep)
    for w, p, d, r in hb[:20]:
        print(f"  {w:6s} x*={p:.9f}  f'={d:+.4f} (Umkehr {1/d:+.4f})  |f(beta)-beta|={mp.nstr(r, 3)}")
    ex = [w for w, p, d, r in hb if r < mpf(10) ** -20 and w != "E"]
    print("exakte Treffer (ohne E):", ex if ex else "keine")
    for w, p, d, r in hb:
        if w == "E":
            print(f"Einzelwort E (nicht blind): x*={p:.10f}, E'={d:+.5f}, (E^-1)'={1/d:+.5f}, Abstand {p-float(B):+.3e}")
    named = {"1/2": 0.5, "1/3": 1 / 3, "1/sqrt3": 3 ** -0.5, "1/sqrt2": 2 ** -0.5,
             "1/gamma_L": float(1 / K.GL), "2^(1-gamma_L)": float(2 ** (1 - K.GL))}
    for k, v in named.items():
        print(f"  N_inv({k} = {v:.7f}) = {N(v, rep)}")
    if ex:
        v = "traegt"
    elif nb > p99:
        v = "traegt teilweise"
    else:
        v = "widerlegt"
    print("Urteil H216:", v)

    print("\n================ H217 (k430): Flaechenvarianten ================")
    res = {}
    for vname, a in VARIANTS.items():
        g, b = beta_variant(a)
        print(f"\n{vname}: gamma = {mp.nstr(g, 15)}, beta = {mp.nstr(b, 15)}")
        res[vname] = []
        for cname, mask in (("vorwaerts (H215-Klasse)", att), ("umkehr (H216)", rep)):
            nc, p95, p99 = stats[cname]
            n = N(float(b), mask)
            h = hits(b, mask)
            ex = [(w, r) for w, p, d, r in h if r < mpf(10) ** -20 and w != "E"]
            above = n > p99
            res[vname].append(bool(ex) or above)
            print(f"  {cname}: N = {n}, Anteil Kontrollen >= {np.mean(nc >= n):.4f}, ueber 99. P.: {above}, "
                  f"exakte Treffer: {len(ex)}")
            for w, r in ex[:8]:
                print(f"     exakt: {w}  (Rest {mp.nstr(r, 3)})")
            if not ex and h:
                w, p, d, r = h[0]
                print(f"     naechster: {w}  Rest {mp.nstr(r, 3)}")
    cas = any(res["Casimir sqrt(j(j+1))"])
    others = any(any(v) for k, v in res.items() if not k.startswith("Casimir"))
    print("\nUrteil H217:", "Casimir ausgezeichnet (traegt)" if cas and not others else
          "nicht trennscharf: die Suche waehlt die Casimir-Flaeche nicht")


if __name__ == "__main__":
    main()
