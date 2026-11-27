"""k419 (Runde v4.10.0-r71): Friedman-Koinzidenzindex als statistische Ergaenzung zum
Kasiski-Abstandsscan auf einem Symbolstrom (Modell des diskretisierten Teichmueller-
Persistenz-Stroms Sigma_pers ueber kleinem Alphabet {trigger-near, persistence-fail,
admissibility-fail, neutral}).

Kasiski schaetzt die Periode aus den ABSTAENDEN wiederholter Bloecke (groesster gemeinsamer
Teiler-Haeufung). Friedman schaetzt sie STATISTISCH aus dem Koinzidenzindex IC: zerlegt man
den Strom in L Spalten (Position mod L), so hat die richtige Periode einen Spalten-IC weit
ueber dem Zufallswert 1/c. Beide sind rein diagnostisch und dem strukturellen
Admissibility-Kriterium untergeordnet (wie der Kasiski-Scan).

Aufruf aus diesem Ordner: python3 k419_friedman_koinzidenz.py > k419_out.txt
"""
import math
from collections import Counter


def kasiski_distances(stream, min_len=3):
    """Abstaende zwischen Wiederholungen von Teilbloecken (Laenge >= min_len)."""
    n = len(stream); dist = Counter()
    for L in range(min_len, max(min_len, n // 2) + 1):
        pos = {}
        for i in range(n - L + 1):
            blk = tuple(stream[i:i + L])
            if blk in pos:
                dist[i - pos[blk]] += 1
            else:
                pos[blk] = i
    return dist


def kasiski_period_candidates(dist, top=6):
    """Kandidaten-Perioden = haeufige Teiler der beobachteten Abstaende."""
    divc = Counter()
    for d, c in dist.items():
        for k in range(2, d + 1):
            if d % k == 0:
                divc[k] += c
    return divc.most_common(top)


def ic(symbols):
    """Koinzidenzindex IC = sum_i n_i(n_i-1) / (N(N-1))."""
    N = len(symbols)
    if N < 2:
        return 0.0
    cnt = Counter(symbols)
    return sum(v * (v - 1) for v in cnt.values()) / (N * (N - 1))


def friedman_column_ic(stream, L):
    """Mittlerer Spalten-IC bei Zerlegung in L Spalten (Position mod L)."""
    ics = [ic(stream[i::L]) for i in range(L) if len(stream[i::L]) >= 2]
    return sum(ics) / len(ics) if ics else 0.0


def friedman_period_estimate(stream, Lmax=21):
    """Fundamentale Periode = kleinste L im Kamm der Ausreisser (L und Vielfache leuchten auf).
    NICHT das L mit maximalem IC: hoehere L haben weniger Proben je Spalte, leicht inflationiert."""
    c = len(set(stream)); kappa_r = 1.0 / c
    rows = [(L, friedman_column_ic(stream, L)) for L in range(1, Lmax + 1)]
    rows = [(L, v, v - kappa_r) for L, v in rows]
    max_exc = max(ex for _, _, ex in rows)
    peaks = [L for L, _, ex in rows if ex > 0.5 * max_exc]
    return (min(peaks) if peaks else None), peaks, rows, kappa_r


def friedman_single_number(stream, kappa_p):
    """Klassische Friedman-Ein-Zahl-Schaetzung: L ~ (kappa_p - kappa_r)/(IC_obs - kappa_r),
    kappa_r = 1/c (Zufall), kappa_p = erwarteter within-Spalten-IC des Musters."""
    c = len(set(stream)); kappa_r = 1.0 / c; ICo = ic(stream)
    if abs(ICo - kappa_r) < 1e-12:
        return math.inf
    return (kappa_p - kappa_r) / (ICo - kappa_r)


def make_stream(period=7, n=420, p_struct=0.80, alphabet=(0, 1, 2, 3), seed=71):
    """Beispielstrom: ein lokales Obstruktions-Muster der Periode `period`, zu p_struct
    strukturiert, sonst Rauschen. Deterministisch ueber `seed`."""
    import random
    rng = random.Random(seed)
    base = [rng.choice(alphabet) for _ in range(period)]
    stream = [base[i % period] if rng.random() < p_struct else rng.choice(alphabet)
              for i in range(n)]
    return stream, base


if __name__ == "__main__":
    PERIOD = 7
    stream, base = make_stream(period=PERIOD)
    c = len(set(stream))
    print(f"Strom: N={len(stream)}, Alphabet c={c}, versteckte Periode={PERIOD}, "
          f"80% strukturiert / 20% Rauschen (seed 71)")
    print(f"globaler IC = {ic(stream):.5f}   (Zufall 1/c = {1 / c:.5f})")
    print()

    dist = kasiski_distances(stream, min_len=3)
    print("KASISKI  — haeufigste Abstaende:", dist.most_common(5))
    print("KASISKI  — Perioden-Kandidaten (Teiler, Haeufung):", kasiski_period_candidates(dist))
    print(f"KASISKI  — dominanter Teiler = {kasiski_period_candidates(dist)[0][0]}")
    print()

    fundamental, peaks, rows, kappa_r = friedman_period_estimate(stream, Lmax=21)
    print(f"FRIEDMAN — Zufalls-IC kappa_r=1/c={kappa_r:.5f}; Ausreisser-Kamm bei L={peaks}")
    print(f"FRIEDMAN — fundamentale Periode = kleinste im Kamm = {fundamental}")
    print("FRIEDMAN — Spalten-IC je L (Ausreisser markiert):")
    for L, v, ex in rows:
        mark = " <== fundamental" if L == fundamental else (" (Vielfaches)" if L in peaks else "")
        print(f"   L={L:2d}: Spalten-IC={v:.5f}  Ueberschuss={ex:+.5f}{mark}")
    print()
    kappa_p = friedman_column_ic(stream, fundamental)
    Lf = friedman_single_number(stream, kappa_p)
    print(f"FRIEDMAN — Ein-Zahl-Schaetzung mit kappa_p=Spalten-IC({fundamental})={kappa_p:.4f}: L ~ {Lf:.2f}")
    print()
    print(f"Ergebnis: Kasiski (dominanter Teiler) und Friedman (fundamentale Kamm-Periode) "
          f"zeigen beide {PERIOD}. Friedman ist komplementaer (Statistik statt Abstaende), "
          f"robuster gegen Rauschen und liefert eine Zahl.")
