"""Frozen-source reassembly, exact error vectors, and precision controls."""
from fractions import Fraction
import importlib.util
import json
from pathlib import Path
import unittest

import numpy as np


ROOT = Path(__file__).resolve().parents[3]
SPEC = importlib.util.spec_from_file_location("origin_rounding_test", ROOT / "analysis/HC_Cartan_Origin_Rounding_Attribution.py")
model = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(model)


class RoundingAlgebraTests(unittest.TestCase):
    def test_vector_attribution_is_exact_but_norms_are_not_additive(self):
        a = [Fraction(0), Fraction(0)]
        b = [Fraction(1), Fraction(0)]
        c = [Fraction(1), Fraction(2)]
        d = [Fraction(0), Fraction(2)]
        result = model.attribution(a, b, c, d)
        self.assertTrue(result["exact_vector_decomposition_verified"])
        self.assertEqual(result["rounded_input_vector"], [1, 0])
        self.assertEqual(result["rounded_matrix_vector"], [0, 2])
        self.assertEqual(result["arithmetic_vector"], [-1, 0])
        self.assertEqual(result["total_vector"], [0, 2])
        self.assertNotEqual(sum(model.stable.rational_norm(result[k]) for k in
            ("rounded_input_vector", "rounded_matrix_vector", "arithmetic_vector")), model.stable.rational_norm(result["total_vector"]))

    def test_binary64_rational_conversion_and_guards(self):
        self.assertEqual(model.rational_array(np.array([.1])), [Fraction.from_float(.1)])
        with self.assertRaises(ValueError):
            model.rational_array(np.array([np.nan]))
        with self.assertRaises(ValueError):
            model.rational_array(np.array([1j]))
        with self.assertRaises(ValueError):
            model.subtract([Fraction(0)], [])
        with self.assertRaises(ValueError):
            model.principal_vector([], [], [], [])

    def test_reassembly_does_not_hide_a_source_or_nonkernel_change(self):
        cauchy = model.common.lower.prior.previous.first.prior
        quads, triples = list(cauchy.joint.third.diagnostic.QUADS), list(cauchy.joint.third.TRIPLES)
        readout = [[Fraction(0)]*24 for _ in range(4)]
        readout[0][0] = Fraction(1)
        fourth = [[Fraction(0)]*24 for _ in range(35)]
        source = [Fraction(0)]*320
        baseline = model.reassemble(source, readout, fourth, quads, triples)
        source[17] = Fraction(3, 7)
        changed_source = model.reassemble(source, readout, fourth, quads, triples)
        self.assertEqual(changed_source[17]-baseline[17], Fraction(3, 7))
        fourth[0][0] = Fraction(1, 2**20)
        changed_highest = model.reassemble(source, readout, fourth, quads, triples)
        self.assertGreater(model.stable.rational_norm(model.subtract(changed_highest, changed_source)), 0.)


class OriginRoundingReportTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.report = json.loads((ROOT / "analysis/HC_Cartan_Origin_Rounding_Attribution.json").read_text(encoding="utf-8"))

    def test_fingerprints_and_no_anchor_or_nonlinear_precision_claim(self):
        self.assertEqual(self.report["input_sha256"], model.input_fingerprints())
        for flag in ("direct_parametric_matches_baseline_exactly", "other_794_rows_bitwise_unchanged",
                "exact_vector_decomposition_verified", "input_rounding_subdecomposition_verified", "no_residual_anchor_added",
                "nonlinear_source_terms_recomputed_in_binary64_then_frozen", "not_a_high_precision_nonlinear_source_or_full_1114_solve",
                "no_interval_certificate_regional_solution_or_native_identification", "parent_polynomials_reports_and_main_TeX_PDF_unchanged"):
            self.assertTrue(self.report[flag])

    def test_stored_fraction_vectors_reconstruct_each_error_row_exactly(self):
        vectors = {k: [Fraction(v) for v in values] for k, values in self.report["exact_attribution_vectors"].items()}
        for key, values in vectors.items():
            self.assertEqual(len(values), 320)
            self.assertAlmostEqual(model.stable.rational_norm(values),
                self.report["rounding_attribution_norms_not_additive"][key.replace("_vector", "_norm")], delta=1e-20)
        for i in range(320):
            self.assertEqual(vectors["total_vector"][i], vectors["rounded_input_vector"][i]
                +vectors["rounded_matrix_vector"][i]+vectors["arithmetic_vector"][i])
            self.assertEqual(vectors["rounded_input_vector"][i], vectors["monomial_rounding_vector"][i]+vectors["highest_assembly_vector"][i])

    def test_precision_promotion_does_not_fix_rounded_inputs(self):
        low, high = self.report["precision_controls"]
        self.assertEqual((low["digits"], high["digits"]), (40, 80))
        self.assertEqual(low["direct_frozen_source_C3_norm"], high["direct_frozen_source_C3_norm"])
        self.assertEqual(low["rounded_input_C3_norm"], high["rounded_input_C3_norm"])
        self.assertLess(float(high["parametric_minus_baseline_C3_norm"]), float(low["parametric_minus_baseline_C3_norm"]))
        self.assertGreater(float(high["rounded_input_C3_norm"]), 1e-8)

    def test_direct_source_reproduction_and_nonzero_baseline(self):
        data = model.load_inputs()
        actual = model.reassemble(data["source"], data["readout"], data["parametric"], data["quads"], data["triples"])
        self.assertAlmostEqual(model.stable.rational_norm(actual), self.report["direct_parametric_C3_norm"], delta=1e-22)
        self.assertGreater(self.report["direct_parametric_C3_norm"], 1e-12)
        self.assertGreater(self.report["raw_binary64_1114_norm"], self.report["direct_frozen_source_hybrid_1114_norm"]*100)
        self.assertEqual(self.report["rounding_attribution_norms_not_additive"]["rounded_matrix_norm"], 0.)
        self.assertGreater(self.report["nonkernel_perturbation_C3_change_norm"], 0.)


if __name__ == "__main__":
    unittest.main()
