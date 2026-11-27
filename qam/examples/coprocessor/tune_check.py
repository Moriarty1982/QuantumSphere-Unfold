"""Selbstjustierung (hdl/qtune.sv, hdl/qcop2t_top.sv) gegen ein bitgenaues Python-Modell pruefen.

Vom Stammverzeichnis des Repositorys:

    python -m qam.examples.coprocessor.tune_check --runs 400 --seed 17

Zufaellige Polynome f(x) = c0 + c1 x + c2 x^2 (Q2.30), Fixpunktsuche und Halbierung mit zufaelligen Grenzen,
Toleranzen und Schrittzahlen, dazu die logistische Abbildung x' = 1,5 x (1 - x) (Fixpunkt 1/3). Mit Rueckschreiben
landet das Ergebnis im Register 0x10 + n und wird als angepasst markiert; schreibt der Host das Register selbst,
verschwindet die Markierung. Jedes Ergebnis (Status, x, Schritte, letzte Schritte) muss bitgenau gleich sein.
"""

import argparse
import random
import shutil
import subprocess
from pathlib import Path
from tempfile import TemporaryDirectory

HDL = Path(__file__).resolve().parent / "hdl"
SOURCES = ("qcfg.sv", "qgate2.sv", "qnorm2.sv", "qstep2.sv", "qcop2_top.sv", "qtune.sv", "qcop2t_top.sv",
           "qcop2t_tb.sv")
ONE = 1 << 30


def s32(v):
    v &= 0xFFFFFFFF
    return v - (1 << 32) if v >> 31 else v


def shr30(p):
    """p[61:30] als vorzeichenbehaftete 32-Bit-Zahl (p ist das volle Produkt)."""
    return s32(p >> 30)


def f(c, x):
    c0, c1, c2 = (s32(v) for v in c)
    xx = shr30(x * x)
    return s32(c0 + shr30(c1 * x) + shr30(c2 * xx))


def tune(mode, c, x0, hi, target, tol, max_iter):
    """Modell von qtune: (status, x, iters, d_last, d_prev)."""
    sat = lambda v: min(abs(v), 0xFFFFFFFF)
    if mode == 0:
        x, it, dl, dp = x0, 0, 0, 0
        while True:
            fx = f(c, x)
            adx = abs(fx - x)
            it += 1
            dp, dl, x = dl, sat(adx), fx
            if adx <= tol:
                return 0, x, it, dl, dp
            if it >= max_iter:
                return 1, x, it, dl, dp
    lo = x0
    g = lambda v: f(c, v) - target
    glo = g(lo)
    if glo == 0:
        return 0, lo, 0, 0, 0
    ghi = g(hi)
    if ghi == 0:
        return 0, hi, 0, 0, 0
    if (ghi < 0) == (glo < 0) or hi <= lo:
        return 2, x0, 0, 0, 0
    neg_lo, it = glo < 0, 0
    while True:
        mid = (lo + hi) >> 1
        gm = g(mid)
        it += 1
        if gm == 0:
            return 0, mid, it, 0, 0
        right = (gm < 0) == neg_lo
        w = hi - mid if right else mid - lo
        if right:
            lo = mid
        else:
            hi = mid
        if w <= tol:
            return 0, mid, it, 0, 0
        if it >= max_iter:
            return 1, mid, it, 0, 0


def q(v):
    return int(round(v * ONE))


def make_runs(rng, n):
    # Logistische Abbildung x' = 1,5 x (1 - x): Fixpunkt 1/3, Steigung dort 0,5 (die HC-Schleife b' = 1 - 2b + 2b^2
    # braucht c2 = 2 und passt nicht in Q2.30).
    runs = [(0, (0, q(1.5), q(-1.5)), q(0.9), 0, 0, 1 << 8, 200),
            (0, (0, q(1.5), q(-1.5)), q(0.1), 0, 0, 0, 200),
            (1, (0, 0, ONE), q(0.0), q(1.0), q(0.5), 0, 64)]          # x^2 = 1/2 -> 1/sqrt(2)
    for _ in range(n):
        mode = rng.randrange(2)
        c = tuple(rng.choice([0, q(rng.uniform(-1.5, 1.5))]) for _ in range(3))
        if mode == 0 and rng.random() < 0.5:
            c = (q(rng.uniform(-0.5, 0.5)), q(rng.uniform(-0.9, 0.9)), q(rng.uniform(-0.4, 0.4)))  # meist kontrahierend
        x0 = q(rng.uniform(-1.5, 1.5))
        hi = q(rng.uniform(-1.5, 1.9))
        target = q(rng.uniform(-1, 1))
        if mode == 1 and rng.random() < 0.7:                              # meist gueltige Klammer
            x0, hi = sorted((x0, hi))
            target = f(c, rng.randint(x0, hi))
        tol = rng.choice([0, 1, rng.randrange(1, 1 << 20)])
        max_iter = rng.choice([1, 5, rng.randrange(1, 300)])
        runs.append((mode, c, x0, hi, target, tol, max_iter))
    return runs


def main():
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--runs", type=int, default=400)
    ap.add_argument("--seed", type=int, default=17)
    args = ap.parse_args()
    rng = random.Random(args.seed)
    runs = make_runs(rng, args.runs)
    lines, expect, adj = [], [], 0
    for mode, c, x0, hi, target, tol, max_iter in runs:
        for a, v in zip(range(1, 9), (*c, x0, hi, target, tol, max_iter)):
            lines.append(f"T {a} {v}")
        wb = rng.random() < 0.5
        dest = rng.randrange(16)
        lines.append(f"S {1 | mode << 1 | (4 if wb else 0) | dest << 4}")
        res = tune(mode, c, x0, hi, target, tol, max_iter)
        if wb and res[0] == 0:
            adj |= 1 << dest
        expect.append(("tune", res, adj))
        if wb and res[0] == 0:
            lines.append(f"R {16 + dest}")
            expect.append(("cfg", 16 + dest, res[1], adj))
            if rng.random() < 0.3:                                    # Host setzt den Wert selbst
                lines.append(f"C {16 + dest} 12345")
                adj &= ~(1 << dest)
                lines.append(f"R {16 + dest}")
                expect.append(("cfg", 16 + dest, 12345, adj))
    with TemporaryDirectory() as tmp:
        stim = Path(tmp) / "tune.txt"
        stim.write_text("\n".join(lines) + "\n", encoding="ascii")
        sim = Path(tmp) / "tune.vvp"
        subprocess.run([shutil.which("iverilog") or "iverilog", "-g2012", "-o", str(sim),
                        *[str(HDL / f) for f in SOURCES]], check=True)
        out = subprocess.run([shutil.which("vvp") or "vvp", "-n", str(sim), f"+stim={stim}"], check=True,
                             capture_output=True, text=True).stdout
    got = []
    for line in out.splitlines():
        t = line.split()
        if t and t[0] == "tune":
            got.append(("tune", (int(t[2]), int(t[4]), int(t[6]), int(t[8]), int(t[10])), int(t[12])))
        elif t and t[0] == "cfg":
            got.append(("cfg", int(t[1]), int(t[2]), int(t[4])))
    if len(got) != len(expect):
        raise SystemExit(f"{len(got)} Ausgaben fuer {len(expect)} erwartete")
    counts = {0: 0, 1: 0, 2: 0}
    for n, (a, b) in enumerate(zip(got, expect)):
        if a != b:
            raise SystemExit(f"Ausgabe {n}: HDL {a} != Modell {b}")
        if a[0] == "tune":
            counts[a[1][0]] += 1
    tunes = [e[1] for e in expect if e[0] == "tune"]
    hc, root = tunes[0], tunes[2]
    print(f"Selbstjustierung: {len(runs)} Laeufe = Modell (konvergiert {counts[0]}, max_iter {counts[1]}, "
          f"ungueltige Klammer {counts[2]}); Rueckschreiben und Markierung 'angepasst' wie erwartet.")
    print(f"Logistisch r = 1,5 ab 0,9: x = {hc[1] / ONE:.9f} nach {hc[2]} Schritten (Fixpunkt 1/3), "
          f"Verhaeltnis der letzten Schritte {hc[3] / max(1, hc[4]):.3f} (|f'(1/3)| = 0,5); "
          f"Halbierung x^2 = 1/2: x = {root[1] / ONE:.9f} (1/sqrt 2 = 0.707106781) nach {root[2]} Schritten")


if __name__ == "__main__":
    main()
