"""Synthesefest-Pruefung aller HDL-Bausteine mit Yosys (generische Zellen, kein FPGA-Mapping).

Vom Stammverzeichnis des Repositorys:

    python -m qam.examples.coprocessor.synth_check
    python -m qam.examples.coprocessor.synth_check --yosys yowasp-yosys --report build/synth.md

Fuer jeden Baustein: read_verilog -sv, synth -noabc -top ..., check -assert. Der Lauf scheitert,
wenn Yosys abbricht (z. B. Schleife mit variabler Grenze), wenn check -assert ein Strukturproblem
findet oder wenn eine Warnung auf konkurrierende Treiber, Latches oder unbelegte Signale zeigt.
Ausgabe: generische Zellenzahl je Baustein.
"""

import argparse
import re
import shutil
import subprocess
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parents[3]
# Relative Pfade ab dem Repo-Stamm: yowasp-yosys (WebAssembly) sieht nur das Arbeitsverzeichnis.
COP = Path("qam/examples/coprocessor/hdl")
ZUSE = Path("qam/examples/zuse_machine/hdl")

# (Name, Top-Modul, Quellen, Parameter)
TARGETS = [
    ("qcop2_top W=16", "qcop2_top", [COP / "qcfg.sv", COP / "qstep2.sv", COP / "qcop2_top.sv"], {"W": 16}),
    ("tape_core direkt", "tape_core", [ZUSE / "tape_core.sv"], {"SCAN": 0}),
    ("tape_core zyklisch", "tape_core", [ZUSE / "tape_core.sv"], {"SCAN": 1}),
    ("guard_stream", "guard_stream", [ZUSE / "guard_stream.sv"], {}),
    ("context_filter", "context_filter", [ZUSE / "context_filter.sv"], {}),
]

BAD_WARNING = re.compile(r"conflicting driver|latch|used but has no driver|is not constant", re.I)
CELLS = [re.compile(r"Number of cells:\s+(\d+)"), re.compile(r"^\s+(\d+)\s+cells\s*$", re.M)]


def find_yosys(explicit):
    if explicit:
        return explicit
    for name in ("yosys", "yowasp-yosys"):
        if shutil.which(name):
            return name
    raise SystemExit("Yosys nicht gefunden (yosys oder yowasp-yosys; pip install yowasp-yosys)")


def synth(yosys, top, sources, params):
    chparam = "".join(f"chparam -set {k} {v} {top}; " for k, v in params.items())
    script = (f"read_verilog -sv {' '.join(str(s) for s in sources)}; {chparam}"
              f"synth -noabc -top {top}; check -assert; stat")
    proc = subprocess.run([yosys, "-p", script], capture_output=True, text=True, cwd=REPO)
    text = proc.stdout + proc.stderr
    warnings = sorted({line.strip() for line in text.splitlines()
                       if line.startswith("Warning") and BAD_WARNING.search(line)})
    cells = None
    for pattern in CELLS:
        found = pattern.findall(text)
        if found:
            cells = int(found[-1])
            break
    error = None
    if proc.returncode != 0:
        errs = [l for l in text.splitlines() if "ERROR" in l]
        error = errs[0] if errs else f"Yosys-Rueckgabewert {proc.returncode}"
    return error, warnings, cells


def main():
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--yosys", default=None)
    ap.add_argument("--report", default=None, help="Markdown-Bericht schreiben")
    args = ap.parse_args()
    yosys = find_yosys(args.yosys)

    rows, failed = [], False
    for name, top, sources, params in TARGETS:
        error, warnings, cells = synth(yosys, top, sources, params)
        ok = error is None and not warnings
        failed |= not ok
        rows.append((name, ok, cells, error or "; ".join(warnings)))
        print(f"{'OK  ' if ok else 'FAIL'} {name}: {cells if cells is not None else '-'} Zellen"
              + (f"  {error or warnings}" if not ok else ""))

    if args.report:
        out = Path(args.report)
        out.parent.mkdir(parents=True, exist_ok=True)
        lines = ["| Baustein | synthesefest | generische Zellen (synth -noabc) |", "|---|---|---:|"]
        lines += [f"| {n} | {'ja' if ok else 'nein: ' + msg} | {c if c is not None else '-'} |"
                  for n, ok, c, msg in rows]
        out.write_text("\n".join(lines) + "\n", encoding="utf-8")
    sys.exit(1 if failed else 0)


if __name__ == "__main__":
    main()
