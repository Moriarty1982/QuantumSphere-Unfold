"""Aufzaehlung fuer H219: alle Ausdruecke aus Bausteinen des Rahmens bis zur Groesse S, Werte dedupliziert.

Blaetter: 1, 2, 3, pi, ln2 (optional n fuer Vorlagen). Einstellig: sqrt, x^2, 1/x, 2^(-x). Zweistellig: + - * /.
Groesse = Zahl der Knoten. Werte, die (relativ 1e-11) gleich sind, werden zusammengefasst; die kleinste Groesse gewinnt.
"""
import numpy as np

LEAVES = {"1": 1.0, "2": 2.0, "3": 3.0, "pi": np.pi, "ln2": np.log(2.0)}
UN = {"sqrt": np.sqrt, "sq": np.square, "inv": lambda x: 1.0 / x, "e2": lambda x: np.exp2(-x)}
BIN = {"+": np.add, "-": np.subtract, "*": np.multiply, "/": np.divide}
LO, HI = 1e-7, 1e7


def _key(v):
    # relativer Schluessel auf 1e-11; v hat Form (N,) oder (N,k)
    v = np.atleast_2d(v.T).T if v.ndim == 1 else v
    return np.round(np.log(np.abs(v)) * 1e11).astype(np.int64)


def enumerate_exprs(smax, leaves=LEAVES, vec=None):
    """vec: None (Zahlen) oder Array der n-Werte fuer Vorlagen (dann Wert = Vektor ueber n, Blatt 'n')."""
    lv = dict(leaves)
    k = 1 if vec is None else len(vec)
    levels = {}  # s -> (vals (N,k), exprs list)
    seen = set()

    def add(s, vals, exprs, store):
        vals = np.asarray(vals, float).reshape(len(exprs), k)
        ok = np.all(np.isfinite(vals) & (np.abs(vals) > LO) & (np.abs(vals) < HI), axis=1)
        vals, exprs = vals[ok], [e for e, o in zip(exprs, ok) if o]
        if len(exprs) == 0:
            return
        keys = _key(vals)
        kt = [tuple(r) for r in keys]
        _, idx = np.unique(keys, axis=0, return_index=True)
        for i in sorted(idx):
            if kt[i] not in seen:
                seen.add(kt[i]); store[0].append(vals[i]); store[1].append(exprs[i])

    st = ([], [])
    for name, v in lv.items():
        add(1, np.full((1, k), v), [name], st)
    if vec is not None:
        add(1, np.asarray(vec, float).reshape(1, k), ["n"], st)
    levels[1] = (np.array(st[0]).reshape(-1, k), st[1])
    for s in range(2, smax + 1):
        st = ([], [])
        pv, pe = levels[s - 1]
        with np.errstate(all="ignore"):
            for u, f in UN.items():
                add(s, f(pv), [f"{u}({e})" for e in pe], st)
            for a in range(1, s - 1):
                b = s - 1 - a
                av, ae = levels[a]
                bv, be = levels[b]
                if len(ae) * len(be) > 4e7:
                    raise RuntimeError(f"zu gross bei s={s}")
                for o, f in BIN.items():
                    if o in "+*" and a > b:
                        continue
                    r = f(av[:, None, :], bv[None, :, :]).reshape(-1, k)
                    ex = [f"({x}{o}{y})" for x in ae for y in be] if len(ae) * len(be) < 3e6 else None
                    if ex is None:
                        # lazy: Ausdruck aus Indizes
                        ii, jj = np.meshgrid(np.arange(len(ae)), np.arange(len(be)), indexing="ij")
                        ex = _Lazy(ae, be, o, ii.ravel(), jj.ravel())
                    add(s, r, ex, st)
        levels[s] = (np.array(st[0]).reshape(-1, k) if st[0] else np.zeros((0, k)), st[1])
    return levels


class _Lazy(list):
    def __init__(self, ae, be, o, ii, jj):
        super().__init__()
        self.ae, self.be, self.o, self.ii, self.jj = ae, be, o, ii, jj

    def __len__(self):
        return len(self.ii)

    def __iter__(self):
        for i, j in zip(self.ii, self.jj):
            yield f"({self.ae[i]}{self.o}{self.be[j]})"

    def __getitem__(self, t):
        return f"({self.ae[self.ii[t]]}{self.o}{self.be[self.jj[t]]})"


if __name__ == "__main__":
    import sys, time
    smax = int(sys.argv[1]) if len(sys.argv) > 1 else 7
    t = time.time()
    L = enumerate_exprs(smax)
    for s in sorted(L):
        print(s, len(L[s][1]), f"{time.time()-t:.1f}s")
