"""Parallele Rechenwerke je Band (hdl/qcop2m_top.sv) gegen die exakte Referenz pruefen und Durchsatz messen.

Vom Stammverzeichnis des Repositorys:

    python -m qam.examples.coprocessor.lanes_check --cases 1200 --seed 9

Fuer (Spuren, Kontexte) = (2, 4) und (4, 4): das Bandregister wird in PARTS gleich lange Baender geteilt
(8 x 16 bzw. 16 x 8), manchmal fehlt ein Band, manchmal ist die Aufteilung absichtlich ungueltig. Jede Gruppe
verteilt bis zu PARTS Faelle auf zufaellige Baender. Gatter fuer ein ungueltiges Band muessen verworfen werden
(Zustand |00>, null Gatter); alle anderen Faelle muessen bitgenau gleich der Referenz sein.
"""

import argparse
import random
import shutil
import subprocess
from pathlib import Path
from tempfile import TemporaryDirectory

from .check import CFG, default_cfg, make_cases, reference

HDL = Path(__file__).resolve().parent / "hdl"
SOURCES = ("qcfg.sv", "qgate2.sv", "qnorm2.sv", "qstep2p.sv", "qband.sv", "qcop2m_top.sv", "qcop2m_tb.sv")
SET_PART = 1


def run(stim_lines, lanes, ctx, tmp):
    stim = Path(tmp) / f"m_{lanes}_{ctx}.txt"
    stim.write_text("\n".join(stim_lines) + "\n", encoding="ascii")
    sim = Path(tmp) / f"m_{lanes}_{ctx}.vvp"
    subprocess.run([shutil.which("iverilog") or "iverilog", "-g2012", f"-Pqcop2m_tb.LANES={lanes}",
                    f"-Pqcop2m_tb.CTX={ctx}", "-o", str(sim), *[str(HDL / f) for f in SOURCES]], check=True)
    out = subprocess.run([shutil.which("vvp") or "vvp", "-n", str(sim), f"+stim={stim}"], check=True,
                         capture_output=True, text=True).stdout
    rows, groups = [], []
    for line in out.splitlines():
        f = line.split()
        if line.startswith("case "):
            rows.append((int(f[3]), int(f[5]), int(f[7]), [int(x) for x in f[11:27]]))
        elif line.startswith("group "):
            groups.append((int(f[1]), int(f[3]), int(f[5]), int(f[7])))
    return rows, groups


def main():
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--cases", type=int, default=1200)
    ap.add_argument("--seed", type=int, default=9)
    args = ap.parse_args()
    rng = random.Random(args.seed)
    cases = make_cases(rng, args.cases)
    L = 7
    with TemporaryDirectory() as tmp:
        for lanes, ctx in ((2, 4), (4, 4)):
            parts = lanes * ctx
            order = L - (parts.bit_length() - 1)
            lines, expect = [], []
            pos = 0
            while pos < len(cases):
                valid = [True] * parts
                bad_layout = False
                r = rng.random()
                if r < 0.15:
                    valid[rng.randrange(parts)] = False
                elif r < 0.22:
                    bad_layout = True
                for p in range(parts):
                    base = p << order
                    word = ((1 if valid[p] else 0) << (L + 4)) | (order << L) | base
                    if bad_layout and p == 1:
                        word = (1 << (L + 4)) | (order << L) | 0          # ueberlappt Band 0
                    lines.append(f"B {SET_PART} {p} {word} 0")
                cfg = default_cfg(16)
                if rng.random() < 0.3:
                    cfg.update(allow=rng.choice([0x1FF, rng.getrandbits(16)]), w_eff=rng.randint(2, 18),
                               k_max=rng.choice([255, rng.randint(0, 10)]),
                               budget=rng.choice([0, rng.randint(0, 30)]), flags=rng.choice([0, 1]))
                lines += [f"C {CFG[key]} {value}" for key, value in cfg.items()]
                n = min(rng.randint(1, parts), len(cases) - pos)
                chosen = rng.sample(range(parts), n)
                lines.append(f"G {n}")
                for p in chosen:
                    gates = cases[pos]
                    pos += 1
                    lines.append(f"L {p} {len(gates)} " + " ".join(f"{o} {t}" for o, t in gates))
                    usable = valid[p] and not bad_layout
                    expect.append((gates, cfg, usable))
            rows, groups = run(lines, lanes, ctx, tmp)
            if len(rows) != len(expect):
                raise SystemExit(f"{lanes}x{ctx}: {len(rows)} Ergebnisse fuer {len(expect)} Faelle")
            blocked_cases = 0
            for n, ((gates, cfg, usable), row) in enumerate(zip(expect, rows)):
                ref = reference(gates, 16, cfg) if usable else (0, 0, 0, [1] + [0] * 15)
                blocked_cases += not usable
                if row != ref:
                    raise SystemExit(f"{lanes}x{ctx} Fall {n}: HDL {row} != Referenz {ref}; usable {usable}")
            cycles = sum(g[1] for g in groups)
            gates = sum(g[2] for g in groups)
            blocked = sum(g[3] for g in groups)
            full = [(g[2], g[1]) for g in groups if g[0] == parts]
            fr = sum(a for a, _ in full) / max(1, sum(b for _, b in full))
            print(f"{lanes} Spuren x {ctx} Kontexte ({parts} Baender zu {1 << order}): {len(expect)} Faelle = Referenz, "
                  f"davon {blocked_cases} auf ungueltigem Band verworfen ({blocked} Gatter); {gates} Gatter in "
                  f"{cycles} Takten = {gates / cycles:.2f} Gatter/Takt, bei voll belegten Gruppen {fr:.2f}")


if __name__ == "__main__":
    main()
