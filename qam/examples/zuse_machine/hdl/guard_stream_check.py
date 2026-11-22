"""Exercise the streaming two-window guard with MMA and Icarus."""

import argparse
from itertools import product
import json
from pathlib import Path
import subprocess
from tempfile import TemporaryDirectory
from time import perf_counter

from qam.examples.zuse_machine.hdl import check


HDL = Path(__file__).resolve().parent
MAX_ROWS = 1_000_000


def mma_persistence():
    program = {
        "states": ["first", "second", "halt"],
        "halt": "halt",
        "rules": [
            {"state": "first", "read": 0, "write": 0, "move": 0, "next": "halt"},
            {"state": "first", "read": 1, "write": 1, "move": 1, "next": "second"},
            {"state": "second", "read": 0, "write": 0, "move": 0, "next": "halt"},
            {"state": "second", "read": 1, "write": 1, "move": 0, "next": "halt"},
        ],
    }
    bits = list(product((0, 1), repeat=2))
    cases = [check.Case(f"guard {first},{second}", program,
                        {"tape": [first, second], "head": 0, "state": "first"})
             for first, second in bits]
    result = {}
    for (first, second), receipt in zip(bits, check.mma_references(cases)):
        if receipt["stop"] != "halted" or receipt["steps"] != 1 + first:
            raise ValueError("Unexpected MMA trace for the two-window guard.")
        result[first, second] = int(receipt["steps"] == 2 and receipt["final"]["tape"][1] == 1)
    return result


def reference(rows, persistence):
    by_mask = {
        (first, second): sum(persistence[(first >> lane) & 1, (second >> lane) & 1] << lane
                             for lane in (0, 1))
        for first, second in product(range(4), repeat=2)
    }
    totals = [0] * 4
    selected = []
    for row_id, first, second in rows:
        next_mask = by_mask[first, second]
        totals[next_mask] += 1
        if next_mask in (1, 2):
            selected.append((row_id, int(next_mask == 1)))
    return selected, (sum(totals), len(selected), totals[0], totals[3])


def run_simulator(vvp, executable, source, stall):
    started = perf_counter()
    result = subprocess.run([vvp, str(executable), source, f"+stall={stall}"],
                            capture_output=True, text=True, timeout=90)
    elapsed_ms = (perf_counter() - started) * 1000
    if result.returncode:
        raise RuntimeError(f"Icarus failed: {(result.stderr + result.stdout)[-1600:]}")
    matches = []
    stats = None
    for line in result.stdout.splitlines():
        kind, *values = line.split()
        if kind == "MATCH" and len(values) == 2 and stats is None:
            matches.append(tuple(map(int, values)))
        elif kind == "STATS" and len(values) == 5 and stats is None:
            stats = tuple(map(int, values))
        else:
            raise ValueError(f"Unexpected simulator line: {line[:140]}")
    if stats is None:
        raise ValueError("Simulator did not return counters.")
    return matches, stats, elapsed_ms


def compare(label, expected, actual):
    matches, stats, _ = actual
    expected_matches, expected_stats = expected
    if stats[1:] != expected_stats:
        raise ValueError(f"{label}: MMA counters {expected_stats}, HDL counters {stats[1:]}")
    for index, (wanted, received) in enumerate(zip(expected_matches, matches)):
        if wanted != received:
            raise ValueError(f"{label}: first difference at output {index}: {wanted} vs {received}")
    if len(matches) != len(expected_matches):
        raise ValueError(f"{label}: MMA returned {len(expected_matches)} matches, HDL {len(matches)}")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--rows", type=int, default=65536)
    parser.add_argument("--iverilog", default="iverilog")
    parser.add_argument("--vvp", default="vvp")
    args = parser.parse_args()
    if not 16 <= args.rows <= MAX_ROWS or args.rows % 16:
        parser.error(f"--rows must be a multiple of 16 between 16 and {MAX_ROWS}")

    persistence = mma_persistence()
    started = perf_counter()
    expected = reference(((i, (i >> 2) & 3, i & 3) for i in range(args.rows)), persistence)
    reference_ms = (perf_counter() - started) * 1000
    report = {"mma_guard_cases": len(persistence), "mask_pairs": 16, "edge_cases": 0,
              "reference_ms": round(reference_ms, 3), "streams": {}}

    with TemporaryDirectory(prefix="qsc-guard-stream-") as tmp:
        executable = Path(tmp) / "guard_stream.vvp"
        compile_started = perf_counter()
        subprocess.run([args.iverilog, "-g2012", "-Wall", "-s", "guard_stream_tb", "-o", str(executable),
                        str(HDL / "guard_stream.sv"), str(HDL / "guard_stream_tb.sv")],
                       timeout=30, check=True)
        report["compile_ms"] = round((perf_counter() - compile_started) * 1000, 3)

        vector = Path(tmp) / "edges.txt"
        edges = [(4294967295, 3, 1), (0, 2, 2), (0, 1, 2), (1, 3, 3), (42, 3, 2)]
        for edge_rows in ([], edges):
            vector.write_text(str(len(edge_rows)) + "\n" +
                              "".join(f"{i} {a} {b}\n" for i, a, b in edge_rows), encoding="ascii")
            edge_expected = reference(edge_rows, persistence)
            for stall in (0, 1):
                compare(f"edge count {len(edge_rows)}, stall {stall}", edge_expected,
                        run_simulator(args.vvp, executable, f"+cases={vector}", stall))
                report["edge_cases"] += 1

        for label, stall in (("ready", 0), ("backpressure", 1)):
            actual = run_simulator(args.vvp, executable, f"+generate={args.rows}", stall)
            compare(label, expected, actual)
            _, (cycles, accepted, selected, blocked, ambiguous), elapsed_ms = actual
            if cycles < accepted or (not stall and cycles > accepted + 1):
                raise ValueError(f"{label}: unexpected aggregate initiation interval")
            report["streams"][label] = {
                "cycles": cycles,
                "accepted": accepted,
                "selected": selected,
                "blocked": blocked,
                "ambiguous": ambiguous,
                "candidates_per_cycle": round(accepted / cycles, 6),
                "input_payload_bits": accepted * 36,
                "output_payload_bits": selected * 33,
                "output_record_reduction_pct": round(100 * (accepted - selected) / accepted, 3),
                "payload_reduction_pct": round(100 * (1 - (selected * 33) / (accepted * 36)), 3),
                "icarus_ms": round(elapsed_ms, 3),
                "icarus_candidates_per_second": round(1000 * accepted / elapsed_ms),
            }

    print(json.dumps(report, indent=2))


if __name__ == "__main__":
    main()
