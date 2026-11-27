"""Takt und Flaeche der Coprozessor-Varianten auf einem FPGA messen (Yosys synth_ecp5 + nextpnr-ecp5).

Vom Stammverzeichnis des Repositorys (dauert einige Minuten je Variante, nicht Teil der CI):

    python -m qam.examples.coprocessor.timing_check --report qam/examples/coprocessor/timing_out.md

Braucht yosys und nextpnr-ecp5 (oder yowasp-yosys und yowasp-nextpnr-ecp5 aus pip). Gemessen wird der Kern in
einem Messrahmen (hdl/qcop2_bench.sv, hdl/qcop2p_bench.sv) mit registrierten Ein- und Ausgaengen auf einem
ECP5-85k (CABGA381), ein Platzierungslauf mit festem Seed. Die Zahlen schwanken mit dem Seed um einige Prozent;
"Gatter/s" = Fmax mal Gatter je Takt bei voller Belegung (bei der Pipeline: mindestens 4 Kontexte im Wechsel).
"""

import argparse
import re
import shutil
import subprocess
from pathlib import Path

REPO = Path(__file__).resolve().parents[3]
H = Path("qam/examples/coprocessor/hdl")
COMMON = [H / "qcfg.sv", H / "qgate2.sv", H / "qnorm2.sv"]
VARIANTS = [
    ("ein Takt je Gatter (qstep2)", "qcop2_bench", COMMON + [H / "qstep2.sv", H / "qcop2_top.sv", H / "qcop2_bench.sv"], {}, 1),
    ("Pipeline, 4 Kontexte (qstep2p)", "qcop2p_bench",
     COMMON + [H / "qstep2p.sv", H / "qcop2p_top.sv", H / "qcop2p_bench.sv"], {"CTX": 4}, 1),
    ("Pipeline, 8 Kontexte (qstep2p)", "qcop2p_bench",
     COMMON + [H / "qstep2p.sv", H / "qcop2p_top.sv", H / "qcop2p_bench.sv"], {"CTX": 8}, 1),
    ("2 Spuren x 4 Kontexte mit Bandregister (qcop2m_top)", "qcop2m_bench",
     COMMON + [H / "qstep2p.sv", H / "qband.sv", H / "qcop2m_top.sv", H / "qcop2m_bench.sv"], {"LANES": 2, "CTX": 4}, 2),
    ("4 Spuren x 4 Kontexte mit Bandregister (qcop2m_top)", "qcop2m_bench",
     COMMON + [H / "qstep2p.sv", H / "qband.sv", H / "qcop2m_top.sv", H / "qcop2m_bench.sv"], {"LANES": 4, "CTX": 4}, 4),
]


def tool(names):
    for name in names:
        if shutil.which(name):
            return name
    raise SystemExit(f"nicht gefunden: {' oder '.join(names)}")


def measure(yosys, nextpnr, top, sources, params, tag):
    out = Path("build/timing")
    (REPO / out).mkdir(parents=True, exist_ok=True)
    json = out / f"{tag}.json"
    chparam = "".join(f"chparam -set {k} {v} {top}; " for k, v in params.items())
    syn = subprocess.run([yosys, "-p", f"read_verilog -sv {' '.join(map(str, sources))}; {chparam}"
                          f"synth_ecp5 -top {top} -json {json}; tee -q -o {out}/{tag}_stat.txt stat"],
                         cwd=REPO, capture_output=True, text=True)
    if syn.returncode:
        raise SystemExit(syn.stdout[-2000:] + syn.stderr[-2000:])
    stat = (REPO / out / f"{tag}_stat.txt").read_text()
    lut = re.findall(r"^\s+(\d+)\s+LUT4\s*$", stat, re.M)
    ff = re.findall(r"^\s+(\d+)\s+TRELLIS_FF\s*$", stat, re.M)
    pnr = subprocess.run([nextpnr, "--85k", "--package", "CABGA381", "--json", str(json), "--freq", "50",
                          "--timing-allow-fail", "--seed", "1"], cwd=REPO, capture_output=True, text=True)
    (REPO / out / f"{tag}_pnr.log").write_text(pnr.stdout + pnr.stderr)
    fmax = re.findall(r"Max frequency for clock[^:]*: ([0-9.]+) MHz", pnr.stdout + pnr.stderr)
    return int(lut[-1]), int(ff[-1]), float(fmax[-1])


def main():
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--report", default=None)
    ap.add_argument("--only", default=None, help="nur Varianten, deren Name diesen Text enthaelt")
    args = ap.parse_args()
    yosys = tool(["yosys", "yowasp-yosys"])
    nextpnr = tool(["nextpnr-ecp5", "yowasp-nextpnr-ecp5"])
    rows = []
    for n, (name, top, sources, params, rate) in enumerate(VARIANTS):
        if args.only and args.only not in name:
            continue
        lut, ff, fmax = measure(yosys, nextpnr, top, sources, params, f"v{n}")
        rows.append((name, lut, ff, fmax, fmax * rate))
        print(f"{name}: {lut} LUT4, {ff} FF, Fmax {fmax:.1f} MHz, {fmax * rate:.1f} Mio. Gatter/s bei voller Belegung")
    if args.report:
        lines = ["| Variante | LUT4 | FF | Fmax (MHz) | Mio. Gatter/s bei voller Belegung |", "|---|---:|---:|---:|---:|"]
        lines += [f"| {r[0]} | {r[1]} | {r[2]} | {r[3]:.1f} | {r[4]:.1f} |" for r in rows]
        Path(args.report).write_text("\n".join(lines) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
