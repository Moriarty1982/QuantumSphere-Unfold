"""Compare two synthesizable tape controllers with MMA and emit a Markdown report."""

import argparse
from collections import defaultdict
from contextlib import closing
from copy import deepcopy
from dataclasses import dataclass
from itertools import product
import json
from pathlib import Path
import re
import shutil
import subprocess
from tempfile import TemporaryDirectory

from qam.tools import readout_db


HDL = Path(__file__).resolve().parent
STATES = 3
CELLS = 8
STOP = ("running", "halted", "boundary", "stuck", "step_limit", "cell_limit")
CONTROLLERS = ("Direkt", "Zyklisch")


@dataclass
class Case:
    name: str
    program: dict
    initial: dict
    mode: str = "fixed"
    max_cells: int = CELLS
    max_steps: int = 6


def read_example(name):
    return json.loads((HDL.parent / name).read_text(encoding="utf-8"))


def make_cases():
    carry = read_example("mma_context.json")["qam"]["objects"]["unary_increment"]["payload"]
    carry["rules"][0]["write"] = 0
    ones = {"tape": [1, 1, 1], "head": 0, "state": "scan"}
    cases = [
        Case("7 + 1", carry, ones, "grow"),
        Case("7 + 1, festes Band", carry, ones),
        Case("7 + 1, Zelllimit", carry, ones, "grow", max_cells=3),
        Case("7 + 1, Schrittlimit", carry, ones, "grow", max_steps=1),
        Case("Schrittlimit null", carry, ones, "grow", max_steps=0),
    ]
    branches = {
        "states": ["a", "b", "halt"], "halt": "halt",
        "rules": [
            {"state": "a", "read": 0, "write": 1, "move": -1, "next": "b"},
            {"state": "a", "read": 1, "write": 0, "move": 1, "next": "b"},
            {"state": "b", "read": 0, "write": 1, "move": 0, "next": "halt"},
        ],
    }
    for width in range(1, 4):
        combinations = product(product(range(2), repeat=width), range(width),
                               branches["states"], ("fixed", "grow"))
        for tape, head, state, mode in combinations:
            name = f"Band {tape}, Kopf {head}, Zustand {state}, Modus {mode}"
            cases.append(Case(name, branches, {"tape": list(tape), "head": head, "state": state}, mode))
    return cases


def mma_references(cases):
    template_context = read_example("mma_context.json")
    template_request = read_example("run_tape_mml.json")
    with closing(readout_db.connect(":memory:")) as db:
        for i, case in enumerate(cases):
            context, request = deepcopy(template_context), deepcopy(template_request)
            objects = context["qam"]["objects"]
            objects["unary_increment"].update(payload=case.program, source="HDL comparison program")
            objects["edge"].update(payload=case.initial, source="HDL comparison initial configuration")
            request["id"] = f"hdl_comparison_{i}"
            request["arguments"].update(mode=case.mode, max_cells=case.max_cells, max_steps=case.max_steps)
            receipt = readout_db.execute_mml(db, context, request)
            if receipt["mma_status"] != "continue":
                raise ValueError(f"{case.name}: MMA rejected or guarded the vector: {receipt}")
            yield receipt["result"]


def pack_cases(cases):
    rows = [str(len(cases))]
    for case in cases:
        ids = {name: i for i, name in enumerate(case.program["states"])}
        tape = case.initial["tape"]
        bits = sum(bit << address for address, bit in enumerate(tape))
        # Dirty the inactive cells so growth must really initialize a new blank.
        bits |= ((1 << CELLS) - 1) ^ ((1 << len(tape)) - 1)
        header = (f"{bits:x}", len(tape), case.initial["head"], ids[case.initial["state"]],
                  ids[case.program["halt"]], int(case.mode == "grow"), case.max_cells, case.max_steps)
        slots = [0] * (2 * STATES)
        for rule in case.program["rules"]:
            move = {-1: 2, 0: 0, 1: 1}[rule["move"]]
            slots[ids[rule["state"]] * 2 + rule["read"]] = (
                (1 << 5) | (rule["write"] << 4) | (move << 2) | ids[rule["next"]]
            )
        rows.append(" ".join(map(str, header)) + " " + " ".join(f"{slot:x}" for slot in slots))
    return "\n".join(rows) + "\n"


def read_simulation(output, cases):
    traces, done = defaultdict(list), {}
    for line in output.splitlines():
        if not line.startswith(("TRACE ", "DONE ")):
            continue
        kind, case_number, controller, *fields = line.split()
        case_id, variant = int(case_number), int(controller)
        key = case_id, variant
        if kind == "DONE":
            ticks = int(fields.pop(0))
        step, bits, length, head, state, stop = fields
        reason = STOP[int(stop)]
        snapshot = {
            "tape": [(int(bits, 16) >> address) & 1 for address in range(int(length))],
            "head": int(head), "state": cases[case_id].program["states"][int(state)],
            "status": "running" if reason in ("step_limit", "cell_limit") else reason,
        }
        if kind == "TRACE":
            traces[key].append((int(step), snapshot))
        else:
            if key in done:
                raise ValueError(f"Duplicate DONE row for case {key}")
            done[key] = ticks, int(step), reason, snapshot
    return traces, done


def compare(cases, references, output):
    traces, done = read_simulation(output, cases)
    for case_id, (case, reference) in enumerate(zip(cases, references)):
        for variant, controller in enumerate(CONTROLLERS):
            key = case_id, variant
            label = f"{case.name}, {controller}"
            expected = list(enumerate(reference["trace"]))
            for i, (want, got) in enumerate(zip(expected, traces[key])):
                if want != got:
                    raise ValueError(f"{label}, Schritt {i}: MMA {want}, HDL {got}")
            if len(expected) != len(traces[key]):
                raise ValueError(f"{label}: MMA hat {len(expected)} Spurpunkte, HDL {len(traces[key])}")
            want_final = reference["steps"], reference["stop"], reference["final"]
            if key not in done or done[key][1:] != want_final:
                raise ValueError(f"{label}: MMA-Ende {want_final}, HDL-Ende {done.get(key)}")
            attempts = reference["steps"] + int(reference["stop"] == "cell_limit")
            expected_ticks = attempts * (2 * STATES if variant else 1)
            if done[key][0] != expected_ticks:
                raise ValueError(f"{label}: erwartet {expected_ticks} Takte, erhalten {done[key][0]}")
    return done


def report(cases, references, done):
    lines = [
        "# Vergleich von MMA und SystemVerilog",
        "",
        f"Beide HDL-Steuerungen stimmten in allen {len(cases)} Fällen mit MMA überein.",
        "Das umfasst 204 Startkombinationen aus allen Binärbändern der Längen 1–3, "
        "allen Kopfpositionen, drei Zuständen und zwei Bandmodi eines Verzweigungsprogramms.",
        "",
        "Takte ab geladener Startkonfiguration bis zur Stopmeldung",
        "",
        "| Fall | Stop | Gezählt in MMA | Direkt | Zyklisch |",
        "|---|---|---:|---:|---:|",
    ]
    for i, case in enumerate(cases[:5]):
        result = references[i]
        lines.append(f"| {case.name} | `{result['stop']}` | {result['steps']} | {done[i, 0][0]} | {done[i, 1][0]} |")
    lines += ["", "Bandspur für 7 + 1 mit wachsendem Band", "",
              " → ".join(f"`{row['tape']}`" for row in references[0]["trace"]), ""]
    return "\n".join(lines)


def synthesize(executable):
    path = shutil.which(executable)
    if path is None:
        raise ValueError(f"Yosys executable not found: {executable}")
    counts = []
    for scan in range(2):
        commands = (
            "read_verilog -sv tape_core.sv; "
            f"chparam -set CELLS {CELLS} -set STATES {STATES} -set SCAN {scan} tape_core; "
            "synth -top tape_core -noabc; stat"
        )
        completed = subprocess.run([str(Path(path).resolve()), "-Q", "-T", "-p", commands],
                                   cwd=HDL, text=True, stdout=subprocess.PIPE,
                                   check=True, timeout=60)
        counts_found = re.findall(r"^\s*(?:Number of cells:\s*(\d+)|(\d+)\s+cells)\s*$",
                                  completed.stdout, flags=re.MULTILINE)
        if not counts_found:
            raise ValueError("Yosys did not report a generic cell count")
        counts.append(int(next(value for value in counts_found[-1] if value)))
    return counts


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--iverilog", default="iverilog")
    parser.add_argument("--vvp", default="vvp")
    parser.add_argument("--yosys", nargs="?", const="yosys", help="Add generic cell counts from Yosys")
    parser.add_argument("--report", type=Path, help="Write the checked Markdown report")
    parser.add_argument("--wave", type=Path, help="Write a VCD waveform for the simulation")
    args = parser.parse_args()
    cases = make_cases()
    references = list(mma_references(cases))
    with TemporaryDirectory() as directory:
        vectors, executable = (Path(directory) / name for name in ("cases.txt", "tape.vvp"))
        vectors.write_text(pack_cases(cases), encoding="ascii")
        subprocess.run([args.iverilog, "-g2012", "-Wall", "-s", "tape_tb", "-o", str(executable),
                        str(HDL / "tape_core.sv"), str(HDL / "tape_tb.sv")], check=True, timeout=60)
        command = [args.vvp, str(executable), f"+cases={vectors}"]
        if args.wave:
            args.wave.parent.mkdir(parents=True, exist_ok=True)
            command.append(f"+wave={args.wave.resolve()}")
        simulation = subprocess.run(command, text=True, stdout=subprocess.PIPE, timeout=60)
        if simulation.returncode:
            raise RuntimeError(simulation.stdout)
        done = compare(cases, references, simulation.stdout)
    markdown = report(cases, references, done)
    if args.yosys:
        direct, scan = synthesize(args.yosys)
        markdown += ("\nGenerische Yosys-Zellen (synth -noabc, ohne FPGA-Mapping)\n\n"
                     f"| Direkt | Zyklisch |\n|---:|---:|\n| {direct} | {scan} |\n")
    print(markdown, end="")
    if args.report:
        args.report.parent.mkdir(parents=True, exist_ok=True)
        args.report.write_text(markdown, encoding="utf-8")


if __name__ == "__main__":
    main()
