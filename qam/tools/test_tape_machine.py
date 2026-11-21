from pathlib import Path
import tempfile
import unittest

from qam.tools import readout_db
from scripts.qsc_audit import tensor_grammar_check as tensor
from scripts.qsc_audit.framework_interface import FrameworkInterface


EXAMPLES = Path(__file__).parents[1] / "examples" / "zuse_machine"


class TapeMmlTests(unittest.TestCase):
    def setUp(self):
        tmp = tempfile.TemporaryDirectory()
        self.addCleanup(tmp.cleanup)
        self.db = readout_db.connect(Path(tmp.name) / "qam.sqlite3")
        self.addCleanup(self.db.close)
        self.context = tensor.load_json(EXAMPLES / "mma_context.json")
        self.request = tensor.load_json(EXAMPLES / "run_tape_mml.json")
        self.objects = self.context["qam"]["objects"]

    def execute(self, **arguments):
        self.request["arguments"].update(arguments)
        return readout_db.execute_mml(self.db, self.context, self.request)

    def test_growth_persists_and_replays(self):
        receipt = self.execute()
        self.assertEqual(receipt["mma_status"], "continue")
        self.assertEqual(receipt["result"]["steps"], 3)
        self.assertEqual([row["tape"] for row in receipt["result"]["trace"]],
                         [[1, 1], [1, 1], [1, 1, 0], [1, 1, 1]])
        self.assertEqual(receipt["result"]["stop"], "halted")
        replay = readout_db.tape_mml(self.db, FrameworkInterface(self.context), self.request)
        self.assertEqual(replay, receipt)
        self.assertEqual(self.execute()["receipt_hash"], receipt["receipt_hash"])
        self.assertEqual(self.db.execute("SELECT count(*) FROM mma_receipts").fetchone(), (1,))

    def test_boundaries_do_not_commit_a_partial_write(self):
        self.objects["edge"]["payload"]["head"] = 1
        self.objects["unary_increment"]["payload"]["rules"][0]["write"] = 0
        for arguments, expected in [
            ({"mode": "fixed", "max_cells": 8, "max_steps": 6}, "boundary"),
            ({"mode": "grow", "max_cells": 2, "max_steps": 6}, "cell_limit"),
            ({"mode": "grow", "max_cells": 8, "max_steps": 0}, "step_limit"),
        ]:
            with self.subTest(expected=expected):
                result = self.execute(**arguments)["result"]
                self.assertEqual(result["stop"], expected)
                self.assertEqual(result["final"]["tape"], [1, 1])
                self.assertEqual(result["final"]["head"], 1)

    def test_guard_inherited_from_qam_program_blocks_execution(self):
        self.context["qam"]["guards"]["open"] = {"status": None, "evidence": "Pending"}
        self.objects["unary_increment"]["guards"] = ["open"]
        receipt = self.execute()
        self.assertEqual(receipt["mma_status"], "guard")
        self.assertIn("open", receipt["declared_guards"])
        self.assertEqual(receipt["request_hash"], tensor.digest(self.request))
        self.assertEqual(receipt["result"], {})

    def test_wrong_object_kind_and_duplicate_rules_are_rejected(self):
        self.assertEqual(self.execute(program="edge")["mma_status"], "reject")
        rules = self.objects["unary_increment"]["payload"]["rules"]
        rules.append(rules[0].copy())
        self.assertEqual(self.execute(program="unary_increment")["mma_status"], "reject")

    def test_stuck_program_is_a_successful_bounded_observation(self):
        self.objects["unary_increment"]["payload"]["rules"] = []
        receipt = self.execute(trace=False)
        self.assertEqual(receipt["mma_status"], "continue")
        self.assertEqual(receipt["result"]["stop"], "stuck")
        self.assertNotIn("trace", receipt["result"])
