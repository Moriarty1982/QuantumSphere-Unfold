"""Compare the two-window persistence bit in MMA and both tape controllers."""

import argparse
from itertools import product
from pathlib import Path
import subprocess
from tempfile import TemporaryDirectory

from qam.examples.zuse_machine.hdl import check


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--iverilog", default="iverilog")
    parser.add_argument("--vvp", default="vvp")
    args = parser.parse_args()
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
    inputs = list(product((0, 1), repeat=2))
    cases = [
        check.Case(f"persistence {a},{b}", program, {"tape": [a, b], "head": 0, "state": "first"})
        for a, b in inputs
    ]
    reference = list(check.mma_references(cases))
    with TemporaryDirectory() as tmp:
        vectors = Path(tmp) / "cases.txt"
        executable = Path(tmp) / "tape.vvp"
        vectors.write_text(check.pack_cases(cases), encoding="ascii")
        subprocess.run(
            [args.iverilog, "-g2012", "-Wall", "-s", "tape_tb", "-o", str(executable),
             str(check.HDL / "tape_core.sv"), str(check.HDL / "tape_tb.sv")],
            check=True, timeout=60,
        )
        simulation = subprocess.run(
            [args.vvp, str(executable), f"+cases={vectors}"],
            text=True, capture_output=True, timeout=60,
        )
        if simulation.returncode:
            raise RuntimeError(simulation.stdout + simulation.stderr)
        cycles = check.compare(cases, reference, simulation.stdout)
    print("MMA vs direct and cyclic HDL: all traces and stop reasons match")
    results = {}
    for case_id, (key, result) in enumerate(zip(inputs, reference)):
        a, b = key
        assert result["stop"] == "halted", key
        assert result["steps"] == 1 + a, key
        assert result["trace"][1]["state"] == ("second" if a else "halt"), key
        assert result["trace"][1]["head"] == a, key
        survives = int(result["steps"] == 2 and result["final"]["tape"][1] == 1)
        assert survives == a * b, key
        results[key] = survives
        print(f"{a},{b}: steps={result['steps']} survives={survives} cycles="
              f"{cycles[case_id, 0][0]}/{cycles[case_id, 1][0]}")
    masks = list(product((0, 1), repeat=2))
    outcomes = {(0, 0): "blocked", (0, 1): "-45", (1, 0): "+45", (1, 1): "ambiguous"}
    for first, second in product(masks, repeat=2):
        active = tuple(results[pair] for pair in zip(first, second))
        print(f"{first} {second} => {active} {outcomes[active]}")


if __name__ == "__main__":
    main()
