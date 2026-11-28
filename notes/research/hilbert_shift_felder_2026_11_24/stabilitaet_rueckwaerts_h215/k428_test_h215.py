"""H215 (k428): Rueckwaertssuche nach Schleifen aus Operationen des Rahmens, die beta_sym anziehen.

Vorab-Notiz: notes/research/predictions/Vorab_Notiz_H215_Stabilitaet_Rueckwaertssuche.md
Aufruf: python k428_test_h215.py  (Ausgabe nach k428_out.txt umleiten)
"""
import itertools
import numpy as np
from mpmath import mp, mpf, sqrt as msqrt, nsum, findroot, inf

mp.dps = 30

# Ziel aus der Zaehlregel r67
F = lambda g: nsum(lambda k: 2 ** (1 - g * msqrt(k * (k + 2) / mpf(3))), [1, inf]) - 1
GL = findroot(F, 1.86)
BETA_M = msqrt((GL - 1) / (GL + 1))
BETA = float(BETA_M)
REL = 6.5e-4

# Grundoperationen (numpy und mpmath)
def _E(b):
    g = (1 + b * b) / np.maximum(1 - b * b, 1e-300)
    return np.exp2(np.minimum(1 - g, 0.0)) * (b < 1)

OPS = {
    "H": lambda b: 1 - 2 * b * (1 - b),
    "S": lambda b: b * b,
    "R": lambda b: np.sqrt(b),
    "C": lambda b: 1 - b,
    "A": lambda b: 2 * b / (1 + b * b),
    "W": lambda b: b / (1 + np.sqrt(np.maximum(1 - b * b, 0.0))),
    "G": lambda b: (1 - b * b) / (1 + b * b),
    "D": lambda b: 2 * b * np.sqrt(np.maximum(1 - b * b, 0.0)),
    "E": _E,
}
MOPS = {
    "H": lambda b: 1 - 2 * b * (1 - b),
    "S": lambda b: b * b,
    "R": lambda b: msqrt(b),
    "C": lambda b: 1 - b,
    "A": lambda b: 2 * b / (1 + b * b),
    "W": lambda b: b / (1 + msqrt(1 - b * b)),
    "G": lambda b: (1 - b * b) / (1 + b * b),
    "D": lambda b: 2 * b * msqrt(1 - b * b),
    "E": lambda b: mpf(2) ** (1 - (1 + b * b) / (1 - b * b)),
}
NAMES = list(OPS)


def apply(word, x):
    # Wort wird von rechts nach links gelesen: "AB" = A(B(x))
    for c in reversed(word):
        x = np.clip(OPS[c](x), 0.0, 1.0)
    return x


def mapply(word, x):
    for c in reversed(word):
        x = MOPS[c](x)
    return x


N_GRID = 20001
XG = np.linspace(0, 1, N_GRID)[1:-1]


def fixpoints(word):
    y = apply(word, XG)
    d = y - XG
    if np.mean(np.abs(d) < 1e-12) > 0.01:
        return None  # identitaetsartig
    pts = []
    s = np.sign(d)
    idx = np.nonzero(s[:-1] * s[1:] < 0)[0]
    exact = np.nonzero(d == 0)[0]
    for i in idx:
        a, b = XG[i], XG[i + 1]
        fa = d[i]
        for _ in range(60):  # Bisektion, robust
            m = 0.5 * (a + b)
            fm = float(apply(word, np.array([m]))[0]) - m
            if (fm < 0) == (fa < 0):
                a, fa = m, fm
            else:
                b = m
        pts.append(0.5 * (a + b))
    for i in exact:
        pts.append(XG[i])
    out = []
    for p in pts:
        h = 1e-7
        lo, hi = max(p - h, 1e-12), min(p + h, 1 - 1e-12)
        fp = (float(apply(word, np.array([hi]))[0]) - float(apply(word, np.array([lo]))[0])) / (hi - lo)
        out.append((p, fp))
    return out


def main():
    print("H215 (k428): Rueckwaertssuche, Schleifen aus 9 Grundoperationen, Laenge 1..5")
    print(f"gamma_L = {mp.nstr(GL, 20)}   beta_sym = {mp.nstr(BETA_M, 20)}")
    print(f"Fenster relativ +-{REL}  ->  [{BETA*(1-REL):.6f}, {BETA*(1+REL):.6f}]  (k358: [0,54907; 0,54978])")
    words = [w for L in range(1, 6) for w in ("".join(t) for t in itertools.product(NAMES, repeat=L))]
    print("Woerter:", len(words))

    attr = []  # (wort, x*, f')
    degenerate = 0
    for w in words:
        fp = fixpoints(w)
        if fp is None:
            degenerate += 1
            continue
        for p, d in fp:
            if abs(d) < 1 - 1e-9 and 1e-6 < p < 1 - 1e-6:
                attr.append((w, p, d))
    print("identitaetsartig ausgeschlossen:", degenerate)
    print("anziehende Fixpunkte in (0,1) gesamt:", len(attr))
    X = np.array([a[1] for a in attr])
    WD = np.array([a[0] for a in attr])

    def N(x0, exclude_E_alone=True):
        m = np.abs(X - x0) <= REL * x0
        if exclude_E_alone:
            m &= WD != "E"
        return len(set(WD[m]))

    nb = N(BETA)
    print("\n--- Ziel beta_sym ---")
    print("N(beta_sym) ohne Einzelwort E:", nb, "  mit E:", N(BETA, False))
    m = np.abs(X - BETA) <= REL * BETA
    hits = sorted({(WD[i], X[i], attr[i][2]) for i in np.nonzero(m)[0]}, key=lambda t: abs(t[1] - BETA))
    print("Treffer im Fenster (Wort, x*, f', |f(beta)-beta| mit 30 Stellen):")
    exact = []
    for w, p, d in hits:
        r = abs(mapply(w, BETA_M) - BETA_M)
        print(f"  {w:6s} x*={p:.9f}  f'={d:+.4f}  Abstand x*-beta={p-BETA:+.2e}  |f(beta)-beta|={mp.nstr(r,3)}")
        if r < mpf(10) ** -20 and w != "E":
            exact.append(w)
    print("exakte Treffer (ohne E allein):", exact if exact else "keine")

    print("\n--- Einzelwort E (nicht blind, getrennt) ---")
    for w, p, d in attr:
        if w == "E":
            print(f"  E: x*={p:.10f}  f'={d:+.5f}  Abstand zu beta_sym {p-BETA:+.3e} (relativ {(p-BETA)/BETA:+.2e})")

    rng = np.random.default_rng(215)
    ctrl = rng.uniform(0.35, 0.75, 2000)
    nc = np.array([N(x) for x in ctrl])
    p95, p99 = np.percentile(nc, [95, 99])
    print("\n--- Kontrollen ---")
    print(f"Zufall (2000, [0,35;0,75], Startwert 215): Mittel {nc.mean():.2f}, Median {np.median(nc):.0f}, "
          f"95. Perzentil {p95:.1f}, 99. Perzentil {p99:.1f}, Maximum {nc.max()}")
    print(f"Anteil Kontrollen mit N >= N(beta_sym): {np.mean(nc >= nb):.4f}")
    named = {"1/2": 0.5, "1/3": 1 / 3, "1/sqrt3": 3 ** -0.5, "1/sqrt2": 2 ** -0.5,
             "1/gamma_L": float(1 / GL), "2^(1-gamma_L)": float(2 ** (1 - GL))}
    for k, v in named.items():
        print(f"  N({k} = {v:.7f}) = {N(v)}")

    print("\n--- Urteil nach Vorab-Notiz ---")
    if exact:
        verdict = "traegt (exakter anziehender Treffer)"
    elif nb > p99:
        verdict = "traegt teilweise (keine exakten Treffer, aber N > 99. Perzentil)"
    else:
        verdict = "widerlegt (kein exakter Treffer, N nicht auffaellig)"
    print(verdict)

    # Nach Laenge, fuer die Wolfram-Gegenprobe (Laenge <= 3)
    m3 = np.array([len(w) <= 3 for w in WD])
    mm = (np.abs(X - BETA) <= REL * BETA) & m3 & (WD != "E")
    print("\nN(beta_sym) nur Laenge <= 3 (fuer Gegenprobe):", len(set(WD[mm])), sorted(set(WD[mm])))
    for name, v in [("1/2", 0.5), ("1/3", 1 / 3)]:
        mm = (np.abs(X - v) <= REL * v) & m3
        print(f"N({name}) Laenge <= 3: {len(set(WD[mm]))}")


if __name__ == "__main__":
    main()
