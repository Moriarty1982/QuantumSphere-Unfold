"""Stable parametric updates, input-rounding controls and independent symbol check."""
from copy import deepcopy
from fractions import Fraction
import importlib.util
import json
from pathlib import Path
import unittest

import mpmath
import numpy as np


ROOT = Path(__file__).resolve().parents[3]
SPEC = importlib.util.spec_from_file_location("kernel_stable_test", ROOT / "analysis/HC_Cartan_Kernel_Stable_Evaluation.py")
model = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(model)


class KernelRepresentationTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.case = model.load_case()

    def test_exact_reconstruction_and_fourth_update_preserve_readouts(self):
        _, readout, _, _, blocks, _, _, _, _, quads, triples = self.case
        updates = model.exact_fourth_update(blocks, quads)
        result = model.c3_entries(model.contract_readouts(readout, updates), quads, triples)
        self.assertEqual(len(result), 320)
        self.assertTrue(all(value == 0 for value in result))

    def test_malformed_or_tampered_certificate_is_rejected(self):
        certificate = deepcopy(self.case[0])
        certificate["pivot_columns"][0] = certificate["free_columns"][0]
        with self.assertRaisesRegex(ValueError, "partition"):
            model.reconstruct_certificate(certificate)
        certificate = deepcopy(self.case[0])
        certificate["pivot_map"][0][0] = str(Fraction(certificate["pivot_map"][0][0])+1)
        with self.assertRaisesRegex(ValueError, "kernel"):
            model.reconstruct_certificate(certificate)

    def test_non_kernel_perturbation_is_not_silently_erased(self):
        _, readout, _, _, blocks, _, _, _, _, quads, triples = self.case
        blocks = deepcopy(blocks)
        a, j = next((a, j) for a in range(4) for j in range(24) if readout[a][j])
        blocks[0][j] += Fraction(1, 1000)
        entries = model.c3_entries(model.contract_readouts(readout, model.exact_fourth_update(blocks, quads)), quads, triples)
        self.assertTrue(any(value != 0 for value in entries))
        self.assertGreater(model.rational_norm(entries), 1.)

    def test_private_precision_context_does_not_change_global_settings(self):
        certificate, readout, pm, free, _, old, rounded, anchor, _, quads, triples = self.case
        digits = mpmath.mp.dps
        model.precision_evaluation(50, certificate, readout, pm, free, old, rounded, anchor, quads, triples)
        self.assertEqual(mpmath.mp.dps, digits)

    def test_linear_update_matches_independent_actual_parent_evaluation(self):
        prepared, point, _, _, _, lift = model.general.domain.load_data()
        cauchy = model.common.lower.prior.previous.first.prior
        coordinates, highest = np.asarray(lift["fitted_coordinates"]), np.asarray(lift["fitted_highest"])
        lc = cauchy.joint.third.lc_cubic(prepared, point)
        before = cauchy.evaluate_fields(prepared, point, coordinates, highest, lc)["vector"]
        changed = highest.copy()
        changed[880:] += np.random.default_rng(20261028).normal(size=840)*.01
        after = cauchy.evaluate_fields(prepared, point, coordinates, changed, lc)["vector"]
        delta = [[Fraction.from_float(float(x))-Fraction.from_float(float(y)) for x, y in zip(new, old)]
                 for new, old in zip(changed[880:].reshape(35, 24), highest[880:].reshape(35, 24))]
        _, readout, _, _, _, _, _, _, _, quads, triples = self.case
        expected = np.array([float(value) for value in model.c3_entries(model.contract_readouts(readout, delta), quads, triples)])
        self.assertGreater(np.linalg.norm(expected), .001)
        np.testing.assert_array_equal((after-before)[:794], 0)
        np.testing.assert_allclose((after-before)[794:], expected, atol=2e-8, rtol=1e-7)


class StableEvaluationReportTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.report = json.loads((ROOT / "analysis/HC_Cartan_Kernel_Stable_Evaluation.json").read_text(encoding="utf-8"))

    def test_fingerprints(self):
        self.assertEqual(self.report["input_sha256"], model.input_fingerprints())

    def test_precision_improves_reconstruction_but_not_already_rounded_inputs(self):
        low, high = self.report["precision_checks"]
        self.assertEqual((low["decimal_digits"], high["decimal_digits"]), (40, 80))
        self.assertLess(float(low["parametric_direct_C3_update_norm"]), 1e-28)
        self.assertLess(float(high["parametric_direct_C3_update_norm"]), 1e-68)
        self.assertLess(float(high["direct_incremental_difference_norm"]), 1e-70)
        self.assertGreater(float(high["rounded_input_high_precision_C3_update_norm"]), 1e-8)
        self.assertAlmostEqual(float(low["rounded_input_high_precision_C3_update_norm"]),
                               float(high["rounded_input_high_precision_C3_update_norm"]), delta=1e-20)

    def test_stable_anchor_retains_existing_norm_without_claiming_fresh_solve(self):
        for check in self.report["precision_checks"]:
            self.assertAlmostEqual(float(check["stable_anchored_1114_norm"]), self.report["old_binary64_anchor_1114_norm"], delta=1e-24)
            self.assertLess(float(check["stable_anchored_1114_norm"]), 1e-8)
        self.assertTrue(self.report["anchor_is_binary64_residual_not_full_high_precision_recomputation"])
        self.assertTrue(self.report["not_an_independent_full_1114_high_precision_solve"])

    def test_exact_input_rounding_failure_remains_visible(self):
        self.assertTrue(self.report["exact_parametric_C3_update_zero"])
        self.assertFalse(self.report["rounded_input_exact_C3_update_zero"])
        self.assertGreater(self.report["rounded_input_exact_C3_update_norm"], 1e-8)
        self.assertGreater(self.report["rounded_binary64_recomputed_1114_norm"], 1e-8)
        self.assertTrue(self.report["no_regional_solution_or_new_order_solved"])
        self.assertFalse(self.report["main_TeX_PDF_changed"])


if __name__ == "__main__":
    unittest.main()
