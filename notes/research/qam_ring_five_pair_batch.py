"""Enumerate all five-edge subsets of an eight-point marked ring."""

import argparse
import json
import subprocess
import sys
from collections import Counter
from itertools import combinations
from math import factorial
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]


def expected_count(edges):
    neighbors = [set() for _ in range(8)]
    for left, right in edges:
        neighbors[left].add(right)
        neighbors[right].add(left)
    isolated = sum(not adjacent for adjacent in neighbors)
    single_edges = sum(len(neighbors[a]) == len(neighbors[b]) == 1 for a, b in edges)
    return factorial(isolated) * 2**single_edges


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--db", required=True, type=Path)
    parser.add_argument("--workers", type=int, choices=range(1, 5), default=2)
    args = parser.parse_args()
    requests = []
    expected = {}
    for indices in combinations(range(8), 5):
        edges = [(i, (i + 1) % 8) for i in indices]
        key = "edges-" + "".join(map(str, indices))
        expected[key] = expected_count(edges)
        requests.append({
            "id": key,
            "instruction": "READOUT",
            "guards": [],
            "arguments": {
                "recipe": "op1.marked-ring-pair-search",
                "pair_constraints": [
                    {"source": [a, b], "target": [(a + 1) % 8, (b + 1) % 8]}
                    for a, b in edges
                ],
            },
        })
    run = subprocess.run(
        [sys.executable, "-m", "qam.tools.readout_db", "--db", str(args.db.resolve()),
         "mma-batch", "scripts/qsc_audit/examples/framework_context.json",
         "-", "--workers", str(args.workers)],
        cwd=ROOT, input=json.dumps({"requests": requests}), text=True, encoding="utf-8",
        stdout=subprocess.PIPE, check=True,
    )
    report = json.loads(run.stdout)
    observed = {entry["id"]: entry["candidate_count"] for entry in report["entries"]}
    if observed != expected:
        raise RuntimeError("MMA counts differ from the independent graph count.")
    print(json.dumps({
        "report_hash": report["report_hash"],
        "batch_hash": report["batch_hash"],
        "cases": len(observed),
        "histogram": dict(sorted(Counter(observed.values()).items())),
        "unique_examples": [key for key, count in observed.items() if count == 1][:3],
    }))


if __name__ == "__main__":
    main()
