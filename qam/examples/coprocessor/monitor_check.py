"""Selbstueberwachung (hdl/qmon.sv, hdl/qcop2s_top.sv): Normwaechter und Anhalten bei Verletzung pruefen.

Vom Stammverzeichnis des Repositorys:

    python -m qam.examples.coprocessor.monitor_check --cases 800 --seed 13

Je Fall eine zufaellige Konfiguration (Waechter an oder aus, Kuerzen aus, durch 2 oder kanonisch durch sqrt(2)).
Bei etwa der Haelfte der Faelle wird an zufaelliger Stelle ein Bit eines Koeffizienten am Eingang des Waechters
gekippt (unterhalb des Vorzeichenbits). Erwartung: ohne Einspeisung nie ein Fehlalarm und Ergebnis = Referenz;
mit Einspeisung und Waechter an haelt der Kern sofort an (Ergebnis = Referenz der Gatter davor, fault = 1);
mit Waechter aus laeuft er weiter. Dazu die Norm sum |x|^2 = 2^k nach jedem Fall in Python nachgerechnet.
"""

import argparse
import random
import shutil
import subprocess
from pathlib import Path
from tempfile import TemporaryDirectory

from .check import CFG, default_cfg, make_cases, reference

HDL = Path(__file__).resolve().parent / "hdl"
SOURCES = ("qcfg.sv", "qgate2.sv", "qnorm2.sv", "qstep2.sv", "qmon.sv", "qcop2s_top.sv", "qcop2s_tb.sv")


def norm_parts(flat):
    p = q = 0
    for i in range(4):
        a = flat[4 * i:4 * i + 4]
        p += sum(x * x for x in a)
        q += a[0] * a[1] + a[1] * a[2] + a[2] * a[3] - a[3] * a[0]
    return p, q


def main():
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--cases", type=int, default=800)
    ap.add_argument("--seed", type=int, default=13)
    args = ap.parse_args()
    width = 16
    rng = random.Random(args.seed)
    cases = make_cases(rng, args.cases)
    lines, expect = [], []
    for gates in cases:
        cfg = default_cfg(width)
        mon = rng.random() < 0.8
        cfg["flags"] = rng.choice([0, 1, 2, 3]) | (4 if mon else 0)
        if rng.random() < 0.3:
            cfg.update(w_eff=rng.randint(3, 16), k_max=rng.choice([255, rng.randint(0, 10)]))
        inj = rng.randrange(len(gates) + 1) if rng.random() < 0.5 else None
        lines += [f"C {CFG[key]} {value}" for key, value in cfg.items()] + ["B"]
        for n, (op, tgt) in enumerate(gates):
            if n == inj:
                lines.append(f"I {rng.randrange(16)} {rng.randrange(width - 1)}")
            lines.append(f"G {op} {tgt}")
        if inj == len(gates):
            lines.append(f"I {rng.randrange(16)} {rng.randrange(width - 1)}")
        lines.append("E")
        halted = inj is not None and mon
        ref = reference(gates[:inj] if halted else gates, width, cfg)
        expect.append((ref, int(halted), cfg, inj, gates))
    with TemporaryDirectory() as tmp:
        stim = Path(tmp) / "mon.txt"
        stim.write_text("\n".join(lines) + "\n", encoding="ascii")
        sim = Path(tmp) / "mon.vvp"
        subprocess.run([shutil.which("iverilog") or "iverilog", "-g2012", "-o", str(sim),
                        *[str(HDL / f) for f in SOURCES]], check=True)
        out = subprocess.run([shutil.which("vvp") or "vvp", "-n", str(sim), f"+stim={stim}"], check=True,
                             capture_output=True, text=True).stdout
    rows = []
    for line in out.splitlines():
        f = line.split()
        if line.startswith("case "):
            rows.append(((int(f[3]), int(f[5]), int(f[7]), [int(x) for x in f[13:29]]), int(f[9]), int(f[11])))
    if len(rows) != len(expect):
        raise SystemExit(f"{len(rows)} Ergebnisse fuer {len(expect)} Faelle")
    stats = {"ohne": 0, "angehalten": 0, "weiter (Waechter aus)": 0}
    for n, ((got, fault, faults), (ref, halted, cfg, inj, gates)) in enumerate(zip(rows, expect)):
        if got != ref or fault != halted:
            raise SystemExit(f"Fall {n}: HDL {got} fault {fault} != Referenz {ref} fault {halted}; cfg {cfg}; "
                             f"Einspeisung vor Gatter {inj}; Gatter {gates}")
        p, q = norm_parts(ref[3])
        if (p, q) != (1 << ref[1], 0):
            raise SystemExit(f"Fall {n}: Norm verletzt in der Referenz: P {p}, Q {q}, k {ref[1]}")
        stats["ohne" if inj is None else "angehalten" if halted else "weiter (Waechter aus)"] += 1
    print(f"Selbstueberwachung W={width}: {len(rows)} Faelle = Referenz; ohne Einspeisung {stats['ohne']} "
          f"(kein Fehlalarm), mit Einspeisung sofort angehalten {stats['angehalten']}, bei Waechter aus "
          f"weitergerechnet {stats['weiter (Waechter aus)']}; Norm sum P = 2^k, sum Q = 0 in allen Faellen")


if __name__ == "__main__":
    main()
