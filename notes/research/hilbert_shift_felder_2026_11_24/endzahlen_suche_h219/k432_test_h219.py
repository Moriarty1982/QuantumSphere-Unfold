"""H219 (k432): Endzahlen-Suche (symbolische Regression) mit Bausteinen des Rahmens und Zufallskontrollen.

Vorab-Notiz: notes/research/predictions/Vorab_Notiz_H219_Endzahlen_Suche.md. Alle Treffer sind "angepasst".
Aufruf: python k432_test_h219.py > k432_out.txt
"""
import math
import os
import sys

import numpy as np

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import enum_h219 as E  # noqa: E402

SMAX, STMAX = 9, 8
NCTRL = 1000

# Zielkatalog wie k235 (Werte, sigma oben, sigma unten), dazu beta_sym (k358-Fenster) und m_e/m_mu (Polmassen k427)
mW, smW, mZ = 80.3692, 0.0133, 91.1880
cot = mW / math.sqrt(mZ ** 2 - mW ** 2)
scot = smW * mZ ** 2 / (mZ ** 2 - mW ** 2) ** 1.5
me, sme, mmu, smmu = 0.51099895, 1.5e-10, 105.6583755, 2.3e-6
r_emu = me / mmu
s_emu = r_emu * math.hypot(sme / me, smmu / mmu)
TARGETS = [
    ("sin2 t12", 0.3088, 0.0067, 0.0066), ("sin2 t23", 0.470, 0.017, 0.014), ("sin2 t13", 0.02248, 0.00056, 0.00056),
    ("dm21/dm31", 0.03002, 0.00046, 0.00046), ("cot tW onshell", cot, scot, scot), ("sin2 tW MSbar", 0.23129, 4e-5, 4e-5),
    ("mH/mZ", 1.3730, 0.0012, 0.0012), ("mt/mW", 2.1472, 0.0037, 0.0037), ("mmu/mtau", 0.059464, 4e-6, 4e-6),
    ("alpha_s", 0.1180, 0.0009, 0.0009), ("|Vus|", 0.2243, 0.0008, 0.0008), ("|Vcb|", 0.0408, 0.0014, 0.0014),
    ("|Vub|", 0.00382, 0.0002, 0.0002), ("Omega_m DESI", 0.2975, 0.0086, 0.0086), ("n_s", 0.9649, 0.0042, 0.0042),
    ("Omega_b h2", 0.02237, 0.00015, 0.00015),
    ("beta_sym (k358)", 0.5494056410, (0.54978 - 0.5494056410) / 2, (0.5494056410 - 0.54907) / 2),
    ("me/mmu", r_emu, s_emu, s_emu),
]
FAMILIES = [("Leptonen", ["me/mmu", "mmu/mtau"]), ("CKM", ["|Vus|", "|Vcb|", "|Vub|"]),
            ("PMNS", ["sin2 t12", "sin2 t23", "sin2 t13"])]
TD = {t[0]: t for t in TARGETS}


def window(t, x=None):
    _, v, su, sd = t
    if x is None:
        x = v
    return x * (1 - 2 * sd / v), x * (1 + 2 * su / v)


def main():
    L = E.enumerate_exprs(SMAX)
    sv, se = {}, {}
    for s in range(1, SMAX + 1):
        v = L[s][0][:, 0]
        o = np.argsort(v)
        sv[s], se[s] = v[o], (L[s][1], o)
    print("H219 (k432): Endzahlen-Suche; Blaetter 1,2,3,pi,ln2; sqrt, x^2, 1/x, 2^-x; + - * /")
    print("verschiedene Werte je Groesse:", {s: len(sv[s]) for s in sv}, " gesamt", sum(len(sv[s]) for s in sv))

    def smin(lo, hi, want_expr=False):
        for s in range(1, SMAX + 1):
            i = np.searchsorted(sv[s], lo)
            if i < len(sv[s]) and sv[s][i] <= hi:
                if want_expr:
                    ex, o = se[s]
                    return s, ex[o[i]], sv[s][i]
                return s
        return (99, None, None) if want_expr else 99

    def count(lo, hi):
        return sum(int(np.searchsorted(sv[s], hi, "right") - np.searchsorted(sv[s], lo)) for s in sv)

    rng = np.random.default_rng(219)
    print("\n--- Einzelziele (Fenster 2 sigma; p = Anteil Kontrollen mit s_min <= s_min(Ziel)) ---")
    print(f"{'Ziel':18s} {'Wert':>12s} {'rel. Fenster':>12s} {'s_min':>5s} {'N':>7s} {'p':>7s}  kuerzester Treffer (angepasst)")
    pvals = {}
    for t in TARGETS:
        lo, hi = window(t)
        s, ex, val = smin(lo, hi, True)
        n = count(lo, hi)
        xs = t[1] * np.exp(rng.uniform(np.log(1 / 3), np.log(3), NCTRL))
        sc = np.array([smin(*window(t, x)) for x in xs])
        p = float(np.mean(sc <= s))
        pvals[t[0]] = p
        exs = f"{ex} = {val:.10g}" if ex else "-"
        print(f"{t[0]:18s} {t[1]:12.6g} {(hi-lo)/t[1]:12.2e} {s if s<99 else '-':>5} {n:7d} {p:7.3f}  {exs}")
        print(f"{'':18s} Kontrollen: s_min Median {np.median(sc):.0f}, Anteil ohne Treffer {np.mean(sc==99):.3f}")

    print("\n--- Familien f(n), n = 1, 2, 3 (Vorlagen bis Groesse", STMAX, ") ---")
    LT = E.enumerate_exprs(STMAX, vec=[1.0, 2.0, 3.0])
    V = np.concatenate([LT[s][0] for s in LT])
    SZ = np.concatenate([np.full(len(LT[s][1]), s) for s in LT])
    EX = [(s, i) for s in LT for i in range(len(LT[s][1]))]
    o = np.argsort(V[:, 0]); V, SZ = V[o], SZ[o]; EX = [EX[i] for i in o]
    print("Vorlagen (verschiedene Wertvektoren):", len(V))

    def fam_smin(wins):
        lo, hi = wins[0]
        a, b = np.searchsorted(V[:, 0], lo), np.searchsorted(V[:, 0], hi, "right")
        if a >= b:
            return 99, None
        ok = np.ones(b - a, bool)
        for k, (l2, h2) in enumerate(wins[1:], start=1):
            ok &= (V[a:b, k] >= l2) & (V[a:b, k] <= h2)
        if not ok.any():
            return 99, None
        j = a + np.nonzero(ok)[0][np.argmin(SZ[a:b][ok])]
        s, i = EX[j]
        return int(SZ[j]), (LT[s][1][i], V[j, :len(wins)])

    fp = {}
    for fname, members in FAMILIES:
        wins = [window(TD[m]) for m in members]
        s, info = fam_smin(wins)
        sc = []
        for _ in range(NCTRL):
            wc = [window(TD[m], TD[m][1] * math.exp(rng.uniform(math.log(1 / 3), math.log(3)))) for m in members]
            sc.append(fam_smin(wc)[0])
        sc = np.array(sc)
        p = float(np.mean(sc <= s))
        fp[fname] = p
        print(f"{fname}: s_min = {s if s<99 else '-'}, p = {p:.3f}, Kontrollen mit Treffer {np.mean(sc<99):.3f}"
              + (f"; Treffer (angepasst): f(n) = {info[0]}, Werte {np.array2string(info[1], precision=6)}" if info else ""))

    print("\n--- Urteil nach Vorab-Notiz ---")
    n05 = sum(p < 0.05 for p in pvals.values())
    sig_t = [k for k, p in pvals.items() if p < 0.05 / len(TARGETS)]
    sig_f = [k for k, p in fp.items() if p < 0.05 / len(FAMILIES)]
    print(f"Ziele mit p < 0,05: {n05} von {len(TARGETS)} ({[k for k,p in pvals.items() if p<0.05]})")
    print(f"nach Bonferroni signifikant: Ziele {sig_t}, Familien {sig_f}")
    if sig_t or sig_f:
        v = "traegt"
    elif n05 >= 4:
        v = "traegt teilweise"
    else:
        v = "widerlegt"
    print("Urteil H219:", v, "(alle Treffer angepasst)")


if __name__ == "__main__":
    main()
