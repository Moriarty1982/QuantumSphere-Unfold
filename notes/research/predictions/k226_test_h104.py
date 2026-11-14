"""k226: H104 (Vorab-Notiz Vorab_Notiz_H104_Zaehlregel_Flaechenspektren.md, Commit c58f449).

Sonderstellung des Zaehlregel-Paars DL/M + ABCK im erweiterten Regelraum S' (Flaechenspektrum x Spinbereich x Gewicht).
gamma = positive Loesung von sum_j g(j) exp(-2 pi gamma a(j)) = 1. Paare (M, T) mit gamma_M > gamma_T.
Fenster wie in H98: beta in [0.545, 0.570]; m_W 2 sigma PDG 2025; Omega_M 2 sigma DESI DR2.
Aufruf: python k226_test_h104.py  (Ausgabe nach k226_out.txt umleiten)
"""
from mpmath import mp, mpf, sqrt, exp, pi

mp.dps = 30
JMAX = 4000

SPECTRA = {
    "W": lambda k: sqrt((mpf(k) / 2) * (mpf(k) / 2 + 1)),     # sqrt(j(j+1)), k = 2j
    "E": lambda k: mpf(k) / 2 + mpf(1) / 2,                   # j + 1/2
    "L": lambda k: mpf(k) / 2,                                # j
}
SPINS = {
    "A": list(range(1, 2 * JMAX + 1)),
    "H": list(range(1, 2 * JMAX + 1, 2)),
    "I": list(range(2, 2 * JMAX + 1, 2)),
    "S1/2": [1],
    "S1": [2],
}
WEIGHTS = {"g=2": lambda k: 2, "g=2j+1": lambda k: k + 1}


def solve(avals, wvals):
    """Bisektion: f faellt streng monoton in gamma. (Lauf 1 nutzte findroot/anderson und verlor sieben Regeln.)"""
    f = lambda g: sum(w * exp(-2 * pi * g * a) for a, w in zip(avals, wvals)) - 1
    lo, hi = mpf("0.01"), mpf("3")
    if not (f(lo) > 0 > f(hi)):
        return None
    for _ in range(110):
        mid = (lo + hi) / 2
        if f(mid) > 0:
            lo = mid
        else:
            hi = mid
    g = (lo + hi) / 2
    return g if abs(f(g)) < mpf("1e-18") else None


if __name__ == "__main__":
    rules, dropped = {}, []
    for an, afun in SPECTRA.items():
        for sn, ks in SPINS.items():
            avals = [afun(k) for k in ks]
            for wn, w in WEIGHTS.items():
                g = solve(avals, [w(k) for k in ks])
                name = f"{an},{sn},{wn}"
                if g is None:
                    dropped.append((name, "keine Loesung")); continue
                same = [n for n, h in rules.items() if abs(g - h) < mpf("1e-18")]
                if same:
                    dropped.append((name, "gleich " + same[0])); continue
                rules[name] = g
    print(f"Regeln: {len(rules)} (entfallen: {len(dropped)})")
    for n, g in rules.items():
        print(f"  {n:16s} gamma = {mp.nstr(g, 12)}")
    for n, why in dropped:
        print(f"  entfaellt {n:16s} {why}")

    mZ, mW0, smW = mpf("91.1880"), mpf("80.3692"), mpf("0.0133")
    Om0, sOm = mpf("0.2975"), mpf("0.0086")
    pairs = []
    for nm in rules:
        for nt in rules:
            if nm == nt or rules[nm] <= rules[nt]:
                continue
            gl = rules[nm] / rules[nt]
            b2 = (gl - 1) / (gl + 1)
            b = sqrt(b2)
            mW = mZ * gl / sqrt(1 + gl * gl)
            pairs.append((nm, nt, gl, b, mW, b2, mpf("0.545") <= b <= mpf("0.570"),
                          abs(mW - mW0) <= 2 * smW, abs(b2 - Om0) <= 2 * sOm))
    nl = sum(p[6] for p in pairs); nw = sum(p[7] for p in pairs); no = sum(p[8] for p in pairs)
    print(f"\ngueltige Paare: {len(pairs)}; gamma_L von {mp.nstr(min(p[2] for p in pairs), 5)} bis "
          f"{mp.nstr(max(p[2] for p in pairs), 5)}")
    print(f"Treffer: Leptonfenster {nl}, m_W {nw}, Omega_M {no}; Anteil im m_W-Fenster {float(nw) / len(pairs):.4f}")
    print(f"\nPaare mit mindestens zwei Treffern:")
    print(f"{'M':16s} {'T':16s} {'gamma_L':>9s} {'beta':>7s} {'m_W':>9s} {'z(m_W)':>7s} {'Om_M':>7s}  L W O")
    for p in sorted(pairs, key=lambda p: p[2]):
        if p[6] + p[7] + p[8] >= 2:
            nm, nt, gl, b, mW, b2, hl, hw, ho = p
            mark = " <== alle drei" if (hl and hw and ho) else ""
            print(f"{nm:16s} {nt:16s} {mp.nstr(gl, 7):>9s} {mp.nstr(b, 5):>7s} {mp.nstr(mW, 7):>9s} "
                  f"{mp.nstr((mW - mW0) / smW, 3):>7s} {mp.nstr(b2, 4):>7s}  {int(hl)} {int(hw)} {int(ho)}{mark}")
    alle = [p for p in pairs if p[6] and p[7] and p[8]]
    print(f"\nalle drei Fenster: {len(alle)} Paar(e)")
    for p in alle:
        print("  ", p[0], "/", p[1])
    ziel = ("W,A,g=2", "W,S1/2,g=2")
    ok = len(alle) == 1 and (alle[0][0], alle[0][1]) == ziel
    print("Kontrolle H98-Paar enthalten:", any((p[0], p[1]) == ziel for p in alle))
    print("H104:", "BESTAETIGT" if ok else "WIDERLEGT")
