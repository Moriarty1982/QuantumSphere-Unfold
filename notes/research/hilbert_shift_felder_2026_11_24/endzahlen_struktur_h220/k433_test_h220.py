"""H220 (k433): Endzahlen-Suche mit strukturellen Bausteinen, Groessengrenze nach Dichte-Regel.

Vorab-Notiz: notes/research/predictions/Vorab_Notiz_H220_Endzahlen_Struktur.md. Alle Treffer sind "angepasst".
Aufruf: python k433_test_h220.py > k433_out.txt
"""
import math
import os
import sys

import numpy as np

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import bausteine_h220 as B  # noqa: E402

SCAP, NCTRL = 8, 1000
me, sme, mmu, smmu = 0.51099895, 1.5e-10, 105.6583755, 2.3e-6
mW, smW, mZ = 80.3692, 0.0133, 91.1880
TARGETS = [  # Name, Wert, sigma, gewertet
    ("me/mmu", me / mmu, me / mmu * math.hypot(sme / me, smmu / mmu), True),
    ("mmu/mtau", 0.059464, 4e-6, True),
    ("sin2 tW MSbar", 0.23129, 4e-5, True),
    ("1/alpha_em(0)", 137.035999177, 2.1e-8, True),
    ("mW/mZ (nicht blind, H15)", mW / mZ, smW / mZ, False),
]


def main():
    L = B.enumerate_struct(SCAP)
    sv, se = {}, {}
    for s in range(1, SCAP + 1):
        v = L[s][0][:, 0]
        o = np.argsort(v)
        sv[s], se[s] = v[o], (L[s][1], o)
    print("H220 (k433): Endzahlen-Suche, strukturelle Bausteine:", ", ".join(B.LEAVES), "; Operationen + - * / sqrt sq inv")
    print(f"gamma_L = {B.GL:.12f}")
    print("neue Werte je Groesse:", {s: len(sv[s]) for s in sv})

    def smin(lo, hi, smax, want=False):
        for s in range(1, smax + 1):
            i = np.searchsorted(sv[s], lo)
            if i < len(sv[s]) and sv[s][i] <= hi:
                if want:
                    ex, o = se[s]
                    return s, ex[o[i]], sv[s][i]
                return s
        return (99, None, None) if want else 99

    rng = np.random.default_rng(220)
    ctrl = {t[0]: t[1] * np.exp(rng.uniform(math.log(1 / 3), math.log(3), NCTRL)) for t in TARGETS}

    def win(x, t):
        r = 2 * t[2] / t[1]
        return x * (1 - r), x * (1 + r)

    # Groessengrenze nach Regel: breitestes Fenster, hoechstens die Haelfte der Kontrollen getroffen
    wide = max(TARGETS, key=lambda t: t[2] / t[1])
    print(f"\nbreitestes Fenster: {wide[0]} (rel. +-{2*wide[2]/wide[1]:.2e})")
    smax = 0
    for s in range(1, SCAP + 1):
        frac = np.mean([smin(*win(x, wide), s) < 99 for x in ctrl[wide[0]]])
        print(f"  S = {s}: Anteil getroffener Kontrollen {frac:.3f}")
        if frac <= 0.5:
            smax = s
    print(f"S_max nach Regel = {smax}")

    print(f"\n--- Ziele (Fenster 2 sigma, Suche bis Groesse {smax}) ---")
    pv = {}
    for t in TARGETS:
        lo, hi = win(t[1], t)
        s, ex, val = smin(lo, hi, smax, True)
        n = sum(int(np.searchsorted(sv[k], hi, "right") - np.searchsorted(sv[k], lo)) for k in range(1, smax + 1))
        sc = np.array([smin(*win(x, t), smax) for x in ctrl[t[0]]])
        p = float(np.mean(sc <= s)) if s < 99 else 1.0
        pv[t[0]] = (p, t[3])
        print(f"{t[0]:26s} Wert {t[1]:.12g}  rel.Fenster {4*t[2]/t[1]:.2e}  s_min {s if s<99 else '-'}  N {n}  p {p:.3f}  "
              f"Kontrollen getroffen {np.mean(sc<99):.3f}")
        if ex:
            print(f"{'':26s} kuerzester Treffer (angepasst): {ex} = {val:.12g}  (Abstand {(val-t[1])/t[2]:+.2f} sigma)")
        # naechster Wert bis S_max, zur Einordnung
        best = None
        for k in range(1, smax + 1):
            i = np.searchsorted(sv[k], t[1])
            for j in (i - 1, i):
                if 0 <= j < len(sv[k]):
                    d = abs(sv[k][j] - t[1]) / t[2]
                    if best is None or d < best[0]:
                        ex2, o2 = se[k]
                        best = (d, k, ex2[o2[j]], sv[k][j])
        print(f"{'':26s} naechster Wert bis S_max: {best[2]} = {best[3]:.12g} (Groesse {best[1]}, {best[0]:.1f} sigma)")

    print("\n--- Urteil nach Vorab-Notiz (gewertet: 4 Ziele ohne mW/mZ) ---")
    g = {k: p for k, (p, w) in pv.items() if w}
    sig = [k for k, p in g.items() if p < 0.05 / 4]
    n05 = sum(p < 0.05 for p in g.values())
    print("p-Werte:", {k: round(p, 3) for k, p in g.items()}, "  signifikant (p<0,0125):", sig, "  p<0,05:", n05)
    v = "traegt" if sig else ("traegt teilweise" if n05 >= 2 else "widerlegt")
    print("Urteil H220:", v, "(alle Treffer angepasst)")


if __name__ == "__main__":
    main()
