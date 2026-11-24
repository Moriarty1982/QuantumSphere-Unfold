"""k245: Hopf-Luecke als Nullpunkt der Flaeche (Erkundung, nicht blind, 23.11.2026).

Zaehlgleichung sum_j g(j) exp(-2 pi gamma a(j)) = 1.
M: alle j >= 1/2 mit Gewicht 2 (DL/M); T: nur j = 1/2 mit Gewicht 2 (ABCK).
Flaeche je Punktierung a(j) in Einheiten 8 pi gamma l_P^2: sqrt(j(j+1)), j + 1/2, j, sqrt(j), j/2.
Variante 1: nur T wechselt das Spektrum (gamma_M fest), Variante 2: beide Frames gleich.
Aufruf: python k245_hopf_gap.py
"""
from math import exp, log, pi, sqrt

GAMMA_M_TODAY = 0.2375329580  # r17.3


def solve(f, lo, hi, it=200):
    for _ in range(it):
        mid = (lo + hi) / 2
        if f(lo) * f(mid) <= 0:
            hi = mid
        else:
            lo = mid
    return (lo + hi) / 2


def gamma_m(a, nmax=6000):
    return solve(lambda g: sum(2 * exp(-2 * pi * g * a(n / 2)) for n in range(1, nmax)) - 1, 1e-2, 5)


def gamma_t(a):
    return log(2) / (2 * pi * a(0.5))


def beta(gl):
    return sqrt((gl - 1) / (gl + 1)) if gl > 1 else float("nan")


SPECTRA = {
    "sqrt(j(j+1)) (heute)": lambda j: sqrt(j * (j + 1)),
    "j + 1/2 (Nullpunkt)": lambda j: j + 0.5,
    "j (ohne Unschaerfe)": lambda j: j,
    "sqrt(j) (Querunschaerfe)": lambda j: sqrt(j),
    "j/2 (Robertson)": lambda j: j / 2,
}

if __name__ == "__main__":
    print(f"{'Spektrum':28s} {'Variante':10s} {'gamma_T':>9s} {'gamma_M':>9s} {'gamma_L':>9s} {'beta':>8s} {'beta^2':>8s}")
    for name, a in SPECTRA.items():
        gt = gamma_t(a)
        for lab, gm in (("M fest", GAMMA_M_TODAY), ("M gleich", gamma_m(a))):
            gl = gm / gt
            b = beta(gl)
            print(f"{name:28s} {lab:10s} {gt:9.6f} {gm:9.6f} {gl:9.6f} {b:8.6f} {b*b:8.6f}")
    print()
    print("Kontrollen gegen geschlossene Formen:")
    a = SPECTRA["j + 1/2 (Nullpunkt)"]
    print("  j+1/2: gamma_M - ln2/pi =", gamma_m(a) - log(2) / pi, " gamma_L - 2 =", gamma_m(a) / gamma_t(a) - 2)
    a = SPECTRA["j (ohne Unschaerfe)"]
    print("  j:     gamma_M - ln3/pi =", gamma_m(a) - log(3) / pi, " gamma_L - log2(3) =", gamma_m(a) / gamma_t(a) - log(3) / log(2))
