"""k218: H98 (Vorab-Notiz 0cad2d8). Sonderstellung des Zaehlregel-Paars DL/M + ABCK im festgelegten Regelraum S.

Regel = Spinbereich x Gewicht; gamma = positive Loesung von sum_j g(j) exp(-2 pi gamma a(j)) = 1, a(j) = sqrt(j(j+1)).
Paare (M, T) mit gamma_M > gamma_T, gamma_L = gamma_M/gamma_T. Fenster: beta in [0.545, 0.570]; m_W 2 sigma PDG 2025;
Omega_M 2 sigma DESI DR2.
"""
from mpmath import mp, mpf, sqrt, exp, pi, findroot, log

mp.dps = 30
JMAX = 4000

def a(k):  # k = 2j
    j = mpf(k) / 2
    return sqrt(j * (j + 1))

SPINS = {
    "A": list(range(1, 2 * JMAX + 1)),            # alle j >= 1/2
    "H": list(range(1, 2 * JMAX + 1, 2)),         # halbzahlig
    "I": list(range(2, 2 * JMAX + 1, 2)),         # ganzzahlig >= 1
    "S1/2": [1],
    "S1": [2],
}
WEIGHTS = {"g=2": lambda k: 2, "g=2j+1": lambda k: k + 1}


def solve(ks, w):
    f = lambda g: sum(w(k) * exp(-2 * pi * g * a(k)) for k in ks) - 1
    if sum(w(k) for k in ks[:1]) <= 1 and len(ks) == 1:
        return None
    # Startwert: Einzelterm-Loesung des kleinsten Spins
    k0 = ks[0]
    g0 = log(w(k0)) / (2 * pi * a(k0)) if w(k0) > 1 else mpf("0.2")
    try:
        g = findroot(f, g0 + mpf("0.05"))
    except Exception:
        return None
    return g if g > 0 and abs(f(g)) < mpf("1e-20") else None


rules = {}
for sn, ks in SPINS.items():
    for wn, w in WEIGHTS.items():
        g = solve(ks, w)
        if g is None:
            continue
        # Duplikate (S1/2: beide Gewichte gleich)
        if any(abs(g - h) < mpf("1e-20") for h in rules.values()):
            continue
        rules[f"{sn},{wn}"] = g

mZ, mW0, smW = mpf("91.1880"), mpf("80.3692"), mpf("0.0133")
Om0, sOm = mpf("0.2975"), mpf("0.0086")
print("Regeln:")
for n, g in rules.items():
    print(f"  {n:14s} gamma = {mp.nstr(g, 12)}")

pairs = []
names = list(rules)
for nm in names:
    for nt in names:
        if nm == nt or rules[nm] <= rules[nt]:
            continue
        gl = rules[nm] / rules[nt]
        b2 = (gl - 1) / (gl + 1)
        b = sqrt(b2)
        mW = mZ * gl / sqrt(1 + gl * gl)
        hit_l = mpf("0.545") <= b <= mpf("0.570")
        hit_w = abs(mW - mW0) <= 2 * smW
        hit_o = abs(b2 - Om0) <= 2 * sOm
        pairs.append((nm, nt, gl, b, mW, b2, hit_l, hit_w, hit_o))

print(f"\ngueltige Paare: {len(pairs)}")
print(f"{'M':14s} {'T':14s} {'gamma_L':>9s} {'beta':>7s} {'m_W':>9s} {'Om_M':>7s}  L W O")
for p in sorted(pairs, key=lambda p: p[2]):
    nm, nt, gl, b, mW, b2, hl, hw, ho = p
    mark = " <==" if (hl and hw and ho) else ""
    print(f"{nm:14s} {nt:14s} {mp.nstr(gl,7):>9s} {mp.nstr(b,5):>7s} {mp.nstr(mW,7):>9s} {mp.nstr(b2,4):>7s}  "
          f"{int(hl)} {int(hw)} {int(ho)}{mark}")

nl = sum(p[6] for p in pairs); nw = sum(p[7] for p in pairs); no = sum(p[8] for p in pairs)
alle = [p for p in pairs if p[6] and p[7] and p[8]]
print(f"\nTreffer: Leptonfenster {nl}, m_W {nw}, Omega_M {no}, alle drei {len(alle)}")
for p in alle:
    print("  alle drei:", p[0], "/", p[1])
ziel = ("A,g=2", "S1/2,g=2")
ok = len(alle) == 1 and (alle[0][0], alle[0][1]) == ziel
print("H98:", "BESTAETIGT" if ok else "WIDERLEGT")
