"""Regression checks for the MML pair batch CLI and scheduler."""

import json
import sqlite3
import subprocess
import sys
import tempfile
import unittest
from concurrent.futures import Future
from contextlib import closing
from pathlib import Path
from unittest.mock import patch

from qam.tools import readout_db


ROOT = Path(__file__).resolve().parents[3]
CONTEXT = ROOT / "scripts/qsc_audit/examples/framework_context.json"
EXAMPLE = ROOT / "qam/examples/marked_ring_pair_batch_mml.json"


class PairBatchTests(unittest.TestCase):
    def setUp(self):
        directory = tempfile.TemporaryDirectory()
        self.addCleanup(directory.cleanup)
        self.db_path = Path(directory.name) / "qam.sqlite3"
        self.batch = json.loads(EXAMPLE.read_text(encoding="utf-8"))

    def cli(self, *args, expected_code=0, input_text=None):
        result = subprocess.run(
            [sys.executable, "-m", "qam.tools.readout_db", "--db", str(self.db_path), *args],
            cwd=ROOT, input=input_text, capture_output=True, text=True, encoding="utf-8",
            timeout=30,
        )
        self.assertEqual(result.returncode, expected_code, result.stderr)
        return result

    def run_batch(self, workers, expected_code=0):
        result = self.cli(
            "mma-batch", str(CONTEXT), "-", "--workers", str(workers),
            input_text=json.dumps(self.batch), expected_code=expected_code,
        )
        return json.loads(result.stdout)

    def test_parallel_report_matches_serial_and_replay(self):
        parallel = self.run_batch(2)
        self.assertEqual(parallel, self.run_batch(1))
        self.assertEqual([entry["candidate_count"] for entry in parallel["entries"]], [120, 0])
        replay = json.loads(
            self.cli("--read-only", "replay-batch", parallel["report_hash"]).stdout
        )
        self.assertTrue(replay["report_matches"])
        self.assertEqual(replay["changes"], [])
        with closing(sqlite3.connect(self.db_path)) as db:
            self.assertEqual(db.execute("SELECT count(*) FROM mma_batch_reports").fetchone(), (1,))
            self.assertEqual(db.execute("SELECT count(*) FROM mma_receipts").fetchone(), (2,))

    def test_zero_match_blocks_only_the_dependent_that_requires_it(self):
        compatible, conflicting = self.batch["requests"]
        predecessor = conflicting["id"]
        self.batch["requests"] += [
            dict(compatible, id="needs_match"),
            dict(compatible, id="waits_only"),
        ]
        self.batch["depends_on"] = {"needs_match": [predecessor], "waits_only": [predecessor]}
        self.batch["requires_match"] = {"needs_match": [predecessor]}
        report = self.run_batch(2, expected_code=1)
        self.assertEqual(
            [entry["mma_status"] for entry in report["entries"]],
            ["continue", "continue", "blocked", "continue"],
        )
        self.assertEqual(report["entries"][2]["blocked_by"], [predecessor])
        audit_args = ("--read-only", "audit-batch", report["report_hash"])
        audit = json.loads(self.cli(*audit_args).stdout)
        self.assertEqual((audit["verified_receipts"], audit["verified_blocked"]), (3, 1))
        with closing(sqlite3.connect(self.db_path)) as db, db:
            db.execute("DELETE FROM mma_receipts WHERE receipt_hash = ?",
                       (report["entries"][1]["receipt_hash"],))
        audit = json.loads(self.cli(*audit_args, expected_code=1).stdout)
        self.assertFalse(audit["verified"])
        self.assertEqual(audit["issues"], [{"id": predecessor, "error": "Missing individual receipt."}])

    def test_ready_child_can_start_while_another_branch_runs(self):
        fast, slow = self.batch["requests"]
        fast["id"] = "fast"
        slow["id"] = "slow"
        self.batch["requests"].append(dict(fast, id="child"))
        self.batch["depends_on"] = {"child": ["fast"]}
        test = self
        tasks = {}
        completion_order = iter(("fast", "child", "slow"))

        class ControlledPool:
            def __init__(self, max_workers):
                test.assertEqual(max_workers, 2)

            def __enter__(self):
                return self

            def __exit__(self, *exc):
                pass

            def submit(self, function, *args):
                future = Future()
                tasks[args[1]["id"]] = (future, function, args)
                return future

        def complete_one(running, *, return_when):
            self.assertEqual(return_when, readout_db.FIRST_COMPLETED)
            self.assertLessEqual(len(running), 2)
            key = next(completion_order)
            if key == "child":
                self.assertIn(tasks["slow"][0], running)
            future, function, args = tasks[key]
            self.assertIn(future, running)
            future.set_result(function(*args))
            return {future}, set(running) - {future}

        context = json.loads(CONTEXT.read_text(encoding="utf-8"))
        with closing(readout_db.connect(self.db_path)) as db:
            with patch.object(readout_db, "ProcessPoolExecutor", ControlledPool):
                with patch.object(readout_db, "wait", complete_one):
                    report = readout_db.execute_pair_batch(db, context, self.batch, 2)
        self.assertEqual([entry["id"] for entry in report["entries"]], ["fast", "slow", "child"])


if __name__ == "__main__":
    unittest.main()
