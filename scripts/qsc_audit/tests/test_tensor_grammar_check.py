"""Semantic boundary tests for explicit role checks and reproducible receipts."""

import copy
import importlib.util
from pathlib import Path
import unittest
from unittest.mock import patch

MODULE_PATH = Path(__file__).resolve().parents[1] / "tensor_grammar_check.py"
SPEC = importlib.util.spec_from_file_location("tensor_grammar_check", MODULE_PATH)
audit = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(audit)
EXAMPLE = MODULE_PATH.parent / "examples" / "tensor_roles_valid.json"


class TensorGrammarTests(unittest.TestCase):
    def setUp(self):
        self.document = audit.load_json(EXAMPLE)

    def report(self):
        return audit.check_document(self.document)

    def operation(self, name):
        return next(op for op in self.document["operations"] if op["id"] == name)

    def receipt(self, name):
        return next(r for r in self.report()["receipts"] if r["operation_id"] == name)

    def test_sandwich_comparison_and_selection(self):
        report = self.report()
        self.assertEqual(report["counts"], {"accepted": 7, "rejected": 0, "unresolved": 0})
        self.assertFalse(report["mathematical_admissibility_proved"])
        self.assertFalse(report["closure_proved"])

    def test_two_upper_indices_cannot_contract_raw(self):
        self.document["operations"] = [{"id": "raw", "type": "contract", "guards": [],
            "left": {"object": "X", "index": "alpha"}, "right": {"object": "Y", "index": "beta"}}]
        self.assertEqual(self.receipt("raw")["status"], "rejected")

    def test_two_lower_indices_need_dual_comparison(self):
        for name, slot in (("X", "alpha"), ("Y", "beta")):
            self.document["objects"][name]["indices"][slot]["variance"] = "lower"
            self.document["objects"]["G"]["indices"][slot]["variance"] = "upper"
        self.assertEqual(self.receipt("active_comparison")["status"], "accepted")
        self.document["objects"]["G"]["indices"]["alpha"]["variance"] = "lower"
        self.assertEqual(self.receipt("active_comparison")["status"], "rejected")

    def test_comparison_object_cannot_be_arbitrary_state(self):
        self.document["objects"]["G"]["kind"] = "state"
        self.assertEqual(self.receipt("active_comparison")["status"], "rejected")

    def test_comparison_cannot_reuse_one_slot(self):
        self.operation("active_comparison")["comparison_slots"] = ["alpha", "alpha"]
        self.assertEqual(self.receipt("active_comparison")["status"], "rejected")

    def test_comparison_preserves_additional_front_role(self):
        self.document["objects"]["G"]["indices"]["frame"] = {
            "label": "F", "side": "front", "variance": "upper", "role": "frame", "space": "V"
        }
        receipt = self.receipt("active_comparison")
        self.assertEqual(receipt["status"], "accepted")
        self.assertIn("frame", receipt["result"]["comparison"]["indices"])

    def test_wrong_space_and_dummy_label(self):
        self.document["spaces"]["W"] = {"dimension": 3}
        self.document["objects"]["B"]["indices"]["nu"]["space"] = "W"
        self.assertEqual(self.receipt("sandwich_action")["status"], "rejected")
        self.document["objects"]["B"]["indices"]["nu"]["space"] = "V"
        self.document["objects"]["B"]["indices"]["nu"]["label"] = "xi"
        self.assertEqual(self.receipt("sandwich_action")["status"], "rejected")

    def test_invalid_front_back_role(self):
        self.document["objects"]["X"]["indices"]["alpha"]["side"] = "front"
        with self.assertRaises(audit.InputError):
            self.report()

    def test_self_pair_rejected(self):
        self.operation("sandwich_action")["right"] = {"object": "T", "index": "nu"}
        self.assertEqual(self.receipt("sandwich_action")["status"], "rejected")

    def test_mixed_primitive_tensor_rejected(self):
        self.operation("state_tensor")["right"] = "R"
        self.assertEqual(self.receipt("state_tensor")["status"], "rejected")

    def test_typing_does_not_imply_admissibility(self):
        self.operation("state_tensor")["guards"] = []
        self.assertEqual(self.receipt("state_tensor")["status"], "unresolved")

    def test_false_and_unknown_guards(self):
        guard = self.document["guards"]["example_tensor_admissibility"]
        guard["status"] = None
        self.assertEqual(self.receipt("state_tensor")["status"], "unresolved")
        guard["status"] = False
        self.assertEqual(self.receipt("state_tensor")["status"], "rejected")

    def test_undeclared_guard_rejected(self):
        self.operation("state_tensor")["guards"] = ["not_declared"]
        with self.assertRaises(audit.InputError):
            self.report()

    def test_mask_boolean_algebra(self):
        op = self.operation("menu_union")
        for operator, left, right, expected in (
            ("union", 1, 2, 3), ("intersection", 3, 2, 2), ("xor", 3, 1, 2)
        ):
            op.update(operator=operator, left=left, right=right)
            self.assertEqual(self.receipt("menu_union")["result"]["value"], expected)
        self.assertEqual(self.receipt("menu_complement")["result"]["value"], 2)

    def test_mask_bits_outside_universe_and_boolean_rejected(self):
        for value in (4, -1, True):
            self.operation("menu_union")["left"] = value
            self.assertEqual(self.receipt("menu_union")["status"], "rejected")

    def test_zero_mask_selects_nothing_without_mutation(self):
        before = copy.deepcopy(self.document)
        self.operation("selected_readout")["mask"] = 0
        result = self.receipt("selected_readout")["result"]
        self.assertEqual(result["selected_components"], [])
        self.assertEqual(before["objects"], self.document["objects"])
        self.assertFalse(result["aggregation_evaluated"])

    def test_selected_payload_hash_is_original(self):
        result = self.receipt("selected_readout")["result"]
        self.assertEqual(result["selected_components"], [{"object": "R", "payload_hash": audit.digest(self.document["objects"]["R"]["payload"])}])

    def test_mixed_readout_needs_guard_and_readout_components(self):
        self.operation("selected_readout")["guards"] = []
        self.assertEqual(self.receipt("selected_readout")["status"], "unresolved")
        self.document["objects"]["R"]["kind"] = "state"
        self.assertEqual(self.receipt("selected_readout")["status"], "rejected")

    def test_mask_cannot_select_an_undeclared_component_kind(self):
        self.document["mask_universes"]["readout_menu"].append("phase")
        self.operation("selected_readout")["mask"] = 4
        self.assertEqual(self.receipt("selected_readout")["status"], "rejected")

    def test_duplicate_operation_and_component_rejected(self):
        self.document["operations"].append(copy.deepcopy(self.document["operations"][0]))
        with self.assertRaises(audit.InputError):
            self.report()
        self.document["operations"].pop()
        components = self.operation("selected_readout")["components"]
        components.append(copy.deepcopy(components[0]))
        self.assertEqual(self.receipt("selected_readout")["status"], "rejected")

    def test_replay_and_dictionary_order(self):
        first = self.report()
        self.document["objects"] = dict(reversed(list(self.document["objects"].items())))
        self.assertEqual(first, self.report())
        self.assertTrue(audit.verify_report(self.document, first))

    def test_tampered_receipt_rejected_even_if_rehashed(self):
        report = self.report()
        report["receipts"][0]["status"] = "rejected"
        body = {key: value for key, value in report["receipts"][0].items() if key != "receipt_hash"}
        report["receipts"][0]["receipt_hash"] = audit.digest(body)
        report["report_hash"] = audit.digest({key: value for key, value in report.items() if key != "report_hash"})
        self.assertFalse(audit.verify_report(self.document, report))

    def test_changed_input_guard_or_rule_sources_invalidates_report(self):
        first = self.report()
        self.document["guards"]["example_tensor_admissibility"]["evidence"] += " changed"
        self.assertFalse(audit.verify_report(self.document, first))
        altered = audit.check_document(self.document, {"different_rule_source": "0" * audit.HASH_HEX_LENGTH})
        self.assertFalse(audit.verify_report(self.document, altered))

    def test_duplicate_json_keys_and_nonfinite_payloads(self):
        for text in ('{"a": 1, "a": 2}', '{"a": NaN}'):
            with patch.object(Path, "read_text", return_value=text):
                with self.assertRaises(audit.InputError):
                    audit.load_json(Path("bad.json"))
        self.document["objects"]["X"]["payload"] = float("inf")
        with self.assertRaises(ValueError):
            self.report()

    def test_unknown_operation_field_is_not_silently_ignored(self):
        self.operation("sandwich_action")["comparision"] = "G"
        self.assertEqual(self.receipt("sandwich_action")["status"], "rejected")

    def test_sha512_known_vector_and_all_report_fingerprints(self):
        self.assertEqual(audit.digest_bytes(b"abc"),
            "ddaf35a193617abacc417349ae20413112e6fa4e89a97ea20a9eeee64b55d39a"
            "2192992a274fc1a836ba3c23a3feebbd454d4423643ce80e2a9ac94fa54ca49f")
        report = self.report()
        self.assertEqual(report["hash_algorithm"], "sha512")
        values = [report[key] for key in ("input_hash", "implementation_hash", "final_chain_hash", "report_hash")]
        values += list(report["rule_sources"].values())
        for receipt in report["receipts"]:
            values += [receipt[key] for key in ("operation_hash", "previous_hash", "receipt_hash")]
        self.assertTrue(all(len(value) == 128 for value in values))

    def test_legacy_schema_rejected(self):
        self.document["schema"] = "qam-role-audit/1"
        with self.assertRaises(audit.InputError):
            self.report()


if __name__ == "__main__":
    unittest.main()
