"""Pipeline-Fassung (hdl/qstep2p.sv) gegen die exakte Referenz pruefen und Gatter je Takt messen.

Vom Stammverzeichnis des Repositorys:

    python -m qam.examples.coprocessor.pipe_check --cases 1200 --seed 5

Je Kontextzahl CTX = 1, 3, 4, 8 laufen Gruppen aus CTX Faellen gleichzeitig; jede Gruppe hat eine eigene
(zufaellige oder Vorgabe-)Konfiguration. Jeder Fall muss bitgenau gleich der Referenz sein (gleiche Regeln wie
qstep2). Ausgabe: Gatter je Takt (Durchsatz) je Kontextzahl.
"""

import argparse
import random
import shutil
import subprocess
from pathlib import Path
from tempfile import TemporaryDirectory

from .check import CFG, default_cfg, make_cases, reference

HDL = Path(__file__).resolve().parent / "hdl"
SOURCES = ("qcfg.sv", "qgate2.sv", "qnorm2.sv", "qstep2p.sv", "qcop2p_top.sv", "qstep2p_tb.sv")


def run(groups, ctx, tmp, width=16):
    """groups: Liste (cfg, [gates, ...]) mit hoechstens ctx Faellen je Gruppe."""
    lines = []
    for cfg, cases in groups:
        lines += [f"C {CFG[key]} {value}" for key, value in cfg.items()]
        lines.append(f"G {len(cases)}")
        for gates in cases:
            lines.append(f"L {len(gates)} " + " ".join(f"{op} {tgt}" for op, tgt in gates))
    stim = Path(tmp) / f"pipe_{ctx}.txt"
    stim.write_text("\n".join(lines) + "\n", encoding="ascii")
    sim = Path(tmp) / f"pipe_{ctx}.vvp"
    iverilog = shutil.which("iverilog") or "iverilog"
    vvp = shutil.which("vvp") or "vvp"
    subprocess.run([iverilog, "-g2012", f"-Pqstep2p_tb.W={width}", f"-Pqstep2p_tb.CTX={ctx}", "-o", str(sim),
                    *[str(HDL / f) for f in SOURCES]], check=True)
    out = subprocess.run([vvp, "-n", str(sim), f"+stim={stim}"], check=True, capture_output=True, text=True).stdout
    rows, cycles, gates = [], 0, 0
    for line in out.splitlines():
        f = line.split()
        if line.startswith("case "):
            rows.append((int(f[3]), int(f[5]), int(f[7]), [int(x) for x in f[11:27]]))
        elif line.startswith("group "):
            cycles += int(f[3])
            gates += int(f[5])
    return rows, cycles, gates


def main():
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--cases", type=int, default=1200)
    ap.add_argument("--seed", type=int, default=5)
    args = ap.parse_args()
    width = 16
    rng = random.Random(args.seed)
    cases = make_cases(rng, args.cases)
    with TemporaryDirectory() as tmp:
        for ctx in (1, 4, 8):
            groups, flat = [], []
            for start in range(0, len(cases), ctx):
                cfg = default_cfg(width)
                if rng.random() < 0.4:
                    cfg.update(allow=rng.choice([0x1FF, rng.getrandbits(16)]), w_eff=rng.randint(2, 18),
                               k_max=rng.choice([255, rng.randint(0, 10)]),
                               budget=rng.choice([0, rng.randint(0, 30)]), flags=rng.choice([0, 1, 2, 3]))
                group = cases[start:start + ctx]
                groups.append((cfg, group))
                flat += [(g, cfg) for g in group]
            rows, cycles, gates = run(groups, ctx, tmp, width)
            if len(rows) != len(flat):
                raise SystemExit(f"CTX={ctx}: {len(rows)} Ergebnisse fuer {len(flat)} Faelle")
            for n, ((g, cfg), row) in enumerate(zip(flat, rows)):
                ref = reference(g, width, cfg)
                if row != ref:
                    raise SystemExit(f"CTX={ctx} Fall {n}: HDL {row} != Referenz {ref}; cfg {cfg}; Gatter {g}")
            print(f"CTX={ctx}: {len(flat)} Faelle = exakte Referenz; {gates} Gatter in {cycles} Takten "
                  f"= {gates / cycles:.3f} Gatter/Takt")


if __name__ == "__main__":
    main()
