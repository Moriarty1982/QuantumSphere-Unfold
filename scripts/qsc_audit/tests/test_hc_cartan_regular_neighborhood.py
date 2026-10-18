"""Norm bounds for temporal regularity, not full normal-symbol hyperbolicity."""
import hashlib
import importlib.util
import json
from pathlib import Path
import unittest

import numpy as np


ROOT = Path(__file__).resolve().parents[3]
SPEC = importlib.util.spec_from_file_location("cartan_regular_neighborhood", ROOT / "analysis/HC_Cartan_Regular_Neighborhood.py")
model = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(model)


class HCCartanRegularNeighborhoodTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.prepared, cls.point, cls.jets = model.load_data()
        cls.data = model.coefficients(cls.prepared, cls.point, cls.jets)
        cls.estimate = model.select_radius(cls.data)
        cls.samples = model.samples(cls.prepared, cls.point, cls.jets, cls.estimate["radius"])["samples"]
        cls.report = json.loads((ROOT / "analysis/HC_Cartan_Regular_Neighborhood.json").read_text(encoding="utf-8"))

    def test_input_fingerprint_matches_regular_jet(self):
        actual = hashlib.sha256((ROOT / "analysis/HC_Cartan_Regular_Gravity.json").read_bytes()).hexdigest()
        self.assertEqual(actual, self.report["regular_gravity_input_sha256"])

    def test_zero_radius_has_exact_base_margins(self):
        result = model.bound(self.data, 0)
        self.assertEqual(result["probe_weight_change_bound"], 0)
        self.assertEqual(result["constraint_block_change_bound"], 0)
        self.assertEqual(result["probe_eigenvalue_lower_bound"], self.data["minimum_base_probe_eigenvalue"])
        self.assertEqual(result["constraint_singular_value_lower_bound"], self.data["minimum_base_constraint_singular_value"])

    def test_negative_radius_is_rejected(self):
        with self.assertRaises(ValueError):
            model.bound(self.data, -.001)

    def test_nonfinite_radius_is_rejected(self):
        with self.assertRaises(ValueError):
            model.bound(self.data, np.inf)

    def test_nonzero_selected_radius_resolves_both_inverse_estimates(self):
        self.assertGreater(self.estimate["radius"], 0)
        self.assertTrue(self.estimate["resolved"])
        self.assertGreater(self.estimate["probe_eigenvalue_lower_bound"], .96)
        self.assertGreater(self.estimate["constraint_singular_value_lower_bound"], .016)

    def test_selected_radius_retains_half_of_each_base_margin(self):
        self.assertGreaterEqual(self.estimate["probe_eigenvalue_lower_bound"], self.data["minimum_base_probe_eigenvalue"]/2)
        self.assertGreaterEqual(self.estimate["constraint_singular_value_lower_bound"], self.data["minimum_base_constraint_singular_value"]/2)

    def test_smaller_radii_improve_the_estimates(self):
        previous = self.estimate
        for factor in (.5, .25, .125):
            current = model.bound(self.data, self.estimate["radius"]*factor)
            self.assertLess(current["probe_weight_change_bound"], previous["probe_weight_change_bound"])
            self.assertLess(current["constraint_block_change_bound"], previous["constraint_block_change_bound"])
            previous = current

    def test_coframe_inverse_failure_is_not_a_positive_result(self):
        result = model.bound(self.data, 1)
        self.assertFalse(result["resolved"])
        self.assertIn("coframe inverse", result["reason"])

    def test_probe_failure_is_not_a_constraint_regularity_claim(self):
        data = dict(self.data, multiplier_first_temporal_column=1e6)
        result = model.bound(data, .001)
        self.assertFalse(result["resolved"])
        self.assertIn("probe", result["reason"])

    def test_constraint_failure_is_distinct_from_probe_positivity(self):
        result = model.bound(self.data, .01)
        self.assertGreater(result["probe_eigenvalue_lower_bound"], 0)
        self.assertFalse(result["resolved"])
        self.assertIn("constraint", result["reason"])

    def test_singular_base_constraint_cannot_be_regularized_by_the_bound(self):
        data = dict(self.data, minimum_base_constraint_singular_value=0)
        with self.assertRaises(ValueError):
            model.select_radius(data)

    def test_clifford_temporal_norm_inequality_is_valid(self):
        rng = np.random.default_rng(340)
        weights = model.gravity.prior.WEIGHTS
        for row in rng.normal(size=(10, 4)):
            actual = np.linalg.norm(np.einsum("a,aij->ij", row, weights), 2)
            self.assertAlmostEqual(actual, abs(row[0])+np.linalg.norm(row[1:]), places=12)
            self.assertLessEqual(actual, np.sqrt(2)*np.linalg.norm(row)+1e-12)

    def test_fixed_readout_weights_have_half_unit_operator_norm(self):
        for a in model.rank_model.A:
            self.assertAlmostEqual(np.linalg.norm(a, 2), .5, places=12)

    def test_sampled_coframes_obey_the_uniform_change_bound(self):
        for sample in self.samples:
            self.assertLessEqual(sample["coframe_change"], self.estimate["coframe_change_bound"]+1e-14)

    def test_sampled_spinors_obey_the_uniform_change_bound(self):
        for sample in self.samples:
            self.assertLessEqual(sample["spinor_change"], self.estimate["spinor_change_bound"]+1e-14)

    def test_sampled_probe_weights_obey_the_uniform_operator_bound(self):
        for sample in self.samples:
            self.assertLessEqual(sample["probe_weight_change"], self.estimate["probe_weight_change_bound"]+1e-12)

    def test_sampled_constraint_blocks_obey_the_uniform_operator_bound(self):
        for sample in self.samples:
            self.assertLessEqual(sample["constraint_block_change"], self.estimate["constraint_block_change_bound"]+1e-12)

    def test_sampled_inverse_margins_exceed_the_analytic_estimates(self):
        for sample in self.samples:
            self.assertGreaterEqual(sample["probe_minimum_eigenvalue"], self.estimate["probe_eigenvalue_lower_bound"])
            self.assertGreaterEqual(sample["constraint_minimum_singular_value"], self.estimate["constraint_singular_value_lower_bound"])

    def test_inverse_norm_estimates_use_the_derived_margins(self):
        self.assertAlmostEqual(self.estimate["probe_inverse_norm_upper_bound"], 1/self.estimate["probe_eigenvalue_lower_bound"])
        self.assertAlmostEqual(self.estimate["constraint_inverse_norm_upper_bound"], 1/self.estimate["constraint_singular_value_lower_bound"])

    def test_new_coefficients_can_be_bounded_without_using_the_old_saved_radius(self):
        data = dict(self.data, spinor_second=4*self.data["spinor_second"])
        result = model.select_radius(data)
        self.assertTrue(result["resolved"])
        self.assertLessEqual(result["radius"], self.estimate["radius"])

    def test_regular_taylor_fields_are_not_claimed_on_shell(self):
        self.assertGreater(max(s["constraint_equation_residual"] for s in self.samples), 1e-9)
        self.assertIn("finite Taylor fields", self.report["status"])

    def test_full_pde_interval_and_native_claims_are_explicitly_excluded(self):
        self.assertTrue(self.report["not_interval_certified_input_norms"])
        self.assertTrue(self.report["not_full_normal_rank_control"])
        self.assertTrue(self.report["not_Cauchy_existence_or_physical_scale"])
        self.assertFalse(self.report["main_TeX_changed"])


if __name__ == "__main__":
    unittest.main()
