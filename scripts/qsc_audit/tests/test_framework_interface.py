"""Framework/adapter boundary and preserved mathematical context tests."""

from pathlib import Path
import unittest
from unittest.mock import patch

from scripts.qsc_audit import tensor_grammar_check as tensor
from scripts.qsc_audit.framework_interface import FrameworkInterface

EXAMPLES = Path(__file__).resolve().parents[1] / "examples"


class FrameworkInterfaceTests(unittest.TestCase):
    def setUp(self):
        self.context = tensor.load_json(EXAMPLES / "framework_context.json")
        self.request = tensor.load_json(EXAMPLES / "framework_tensor_request.json")
        self.export = tensor.load_json(EXAMPLES / "framework_export_request.json")

    def interface(self):
        return FrameworkInterface(self.context)

    def receipt(self):
        return self.interface().execute(self.request)

    def operation(self, name):
        return next(op for op in self.request["arguments"]["operations"] if op["id"] == name)

    def test_framework_adapter_passes_without_discarding_open_residuals(self):
        receipt = self.receipt()
        self.assertEqual(receipt["mma_status"], "continue")
        self.assertEqual(receipt["result"]["report"]["counts"]["accepted"], 7)
        self.assertEqual(receipt["result"]["residuals"]["rho"]["status"], "open")
        self.assertFalse(receipt["closure_proved"])
        self.assertFalse(receipt["mathematical_relations_proved"])

    def test_export_retains_relations_and_scope(self):
        receipt = self.interface().execute(self.export)
        framework = receipt["result"]["framework"]
        self.assertEqual(framework, self.context)
        self.assertIsNone(framework["qam"]["relations"]["XY_equivalent"]["status"])
        self.assertEqual(receipt["scope"]["regime"], "local")

    def test_interface_isolated_from_input_and_output_mutation(self):
        interface = self.interface()
        fingerprint = interface.context_hash
        self.context["qam"]["objects"]["X"]["payload"] = {"changed": True}
        exported = interface.execute(self.export)
        exported["result"]["framework"]["qam"]["objects"].clear()
        self.assertEqual(interface.context_hash, fingerprint)
        self.assertEqual(len(interface.context["qam"]["objects"]), 9)

    def test_active_unresolved_guard_is_preserved(self):
        self.context["qam"]["guards"]["global"] = {"status": None, "evidence": "Open global assumption"}
        self.context["qam"]["active_guards"] = ["global"]
        self.assertEqual(self.receipt()["mma_status"], "guard")

    def test_failed_object_guard_reaches_adapter(self):
        self.context["qam"]["guards"]["X_guard"] = {"status": False, "evidence": "Declared failing precondition"}
        self.context["qam"]["objects"]["X"]["guards"] = ["X_guard"]
        receipt = self.receipt()
        self.assertEqual(receipt["mma_status"], "guard")
        rows = receipt["result"]["report"]["receipts"]
        comparison = next(row for row in rows if row["operation_id"] == "active_comparison")
        self.assertEqual(comparison["status"], "rejected")
        self.assertIn("X_guard", comparison["declared_guards"])

    def test_unknown_tensor_relation_remains_guarded(self):
        self.context["qam"]["relations"]["XY_admissible"]["status"] = None
        self.assertEqual(self.receipt()["mma_status"], "guard")

    def test_wrong_relation_pair_cannot_authorize_operation(self):
        self.operation("state_tensor")["right"] = "B"
        self.assertEqual(self.receipt()["mma_status"], "reject")

    def test_unrelated_guard_does_not_supply_tensor_admissibility(self):
        op = self.operation("state_tensor")
        del op["admissibility_relation"]
        self.request["guards"] = ["example_tensor_admissibility"]
        receipt = self.receipt()
        self.assertEqual(receipt["mma_status"], "guard")
        row = next(r for r in receipt["result"]["report"]["receipts"] if r["operation_id"] == "state_tensor")
        self.assertEqual(row["status"], "unresolved")

    def test_one_operations_guard_does_not_leak_into_another(self):
        self.context["qam"]["guards"]["only_first"] = {"status": False, "evidence": "First operation only"}
        self.operation("sandwich_action")["guards"] = ["only_first"]
        rows = self.receipt()["result"]["report"]["receipts"]
        second = next(row for row in rows if row["operation_id"] == "sandwich_readout")
        self.assertEqual(second["status"], "accepted")
        self.assertNotIn("only_first", second["declared_guards"])

    def test_no_equivalence_inferred_from_equal_payload_hashes(self):
        self.context["qam"]["objects"]["Y"]["payload"] = self.context["qam"]["objects"]["X"]["payload"]
        receipt = self.interface().execute(self.export)
        relation = receipt["result"]["framework"]["qam"]["relations"]["XY_equivalent"]
        self.assertIsNone(relation["status"])

    def test_replay_binds_context_and_request(self):
        interface = self.interface()
        receipt = interface.execute(self.request)
        self.assertTrue(interface.verify(self.request, receipt))
        self.request["id"] = "changed_request"
        self.assertFalse(interface.verify(self.request, receipt))
        self.context["qam"]["residuals"]["rho"]["evidence"] = "Updated residual record"
        self.assertFalse(self.interface().verify(tensor.load_json(EXAMPLES / "framework_tensor_request.json"), receipt))

    def test_tampered_receipt_rejected_after_rehashing(self):
        interface = self.interface()
        receipt = interface.execute(self.request)
        receipt["closure_proved"] = True
        receipt["receipt_hash"] = tensor.digest({k: v for k, v in receipt.items() if k != "receipt_hash"})
        self.assertFalse(interface.verify(self.request, receipt))

    def test_unknown_instruction_and_unknown_guard_rejected(self):
        self.request["instruction"] = "RUN_ARBITRARY_CODE"
        self.assertEqual(self.receipt()["mma_status"], "reject")
        self.request["instruction"] = "SCRUB"
        self.request["guards"] = ["absent"]
        self.assertEqual(self.receipt()["mma_status"], "reject")

    def test_relation_kind_and_dangling_residual_reference_rejected(self):
        self.context["qam"]["relations"]["XY_equivalent"]["arguments"]["source"] = "R"
        with self.assertRaises(tensor.InputError):
            self.interface()
        self.context["qam"]["relations"]["XY_equivalent"]["arguments"]["source"] = "X"
        self.context["qam"]["residuals"]["rho"]["witness"] = "absent"
        with self.assertRaises(tensor.InputError):
            self.interface()

    def test_framework_scrub_inspects_registry_without_evaluating_truth(self):
        self.request["arguments"] = {"view": "framework"}
        receipt = self.receipt()
        self.assertEqual(receipt["mma_status"], "continue")
        self.assertFalse(receipt["result"]["structural_truth_evaluated"])
        self.assertEqual(receipt["result"]["relations_registered"], 2)

    def test_sha512_receipt_and_parent_reference(self):
        self.context["provenance"]["parent_context_hash"] = "a" * 128
        receipt = self.receipt()
        self.assertEqual(receipt["hash_algorithm"], "sha512")
        for key in ("context_hash", "request_hash", "receipt_hash", "implementation_hash", "tensor_adapter_hash"):
            self.assertEqual(len(receipt[key]), 128)
        self.assertTrue(all(len(value) == 128 for value in receipt["source_hashes"].values()))
        for invalid in ("a" * 64, "a" * 127, "G" * 128):
            self.context["provenance"]["parent_context_hash"] = invalid
            with self.assertRaises(tensor.InputError):
                self.interface()

    def test_framework_standalone_binding_is_explicit(self):
        with patch.object(tensor, "ROOT", tensor.ROOT / "build" / "absent-source-checkout"):
            receipt = self.receipt()
            self.assertEqual(receipt["mma_status"], "continue")
            self.assertEqual(receipt["source_binding"]["mode"], "bundled_rule_catalog")
            self.assertFalse(receipt["source_binding"]["source_text_available"])
            self.assertEqual(len(receipt["source_hashes"]), 4)


if __name__ == "__main__":
    unittest.main()
