"""Quartic fields, uniform temporal estimates, and geometric-domain checks."""
import importlib.util
import json
from pathlib import Path
import unittest

import numpy as np


ROOT = Path(__file__).resolve().parents[3]
SPEC = importlib.util.spec_from_file_location(
    "cartan_joint_neighborhood", ROOT / "analysis/HC_Cartan_Joint_Neighborhood.py")
model = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(model)


class JointNeighborhoodTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.prepared, cls.point, cls.jets, cls.extras, cls.input = model.load_data()
        cls.data = model.coefficient_norms(cls.prepared, cls.point, cls.jets, cls.extras)
        cls.estimate = model.select_radius(cls.data)
        cls.report = json.loads((ROOT / "analysis/HC_Cartan_Joint_Neighborhood.json").read_text(encoding="utf-8"))
        cls.samples = model.sample_checks(cls.prepared, cls.point, cls.jets, cls.extras, cls.estimate["radius"])

    def test_all_pinned_sources_are_current(self):
        self.assertEqual(self.report["input_sha256"], model.input_fingerprints())

    def test_fourth_tensor_reconstruction_counts_repeated_indices(self):
        values = np.arange(35*2).reshape(35, 2)
        tensor = model.unpack_fourth(values)
        for indices, value in zip(model.third.diagnostic.QUADS, values):
            np.testing.assert_array_equal(tensor[indices], value)
        np.testing.assert_array_equal(tensor, tensor.swapaxes(0, 3))
        self.assertGreater(np.linalg.norm(tensor), np.linalg.norm(values))

    def test_invalid_fourth_tensor_and_radius_are_rejected(self):
        with self.assertRaises(ValueError):
            model.unpack_fourth(np.zeros((34, 4, 4)))
        for radius in (-1., np.nan, np.inf):
            with self.assertRaises(ValueError):
                model.bound(self.data, radius)

    def test_fourth_and_cubic_terms_enter_bounds_with_actual_factorials(self):
        radius = .03
        changed = dict(self.data, coframe_fourth=self.data["coframe_fourth"]+24,
                       spinor_fourth=self.data["spinor_fourth"]+48,
                       multiplier_third_temporal_column=self.data["multiplier_third_temporal_column"]+6)
        actual = np.array(model.polynomial_changes(changed, radius))-model.polynomial_changes(self.data, radius)
        np.testing.assert_allclose(actual, [radius**4, 2*radius**4, radius**3], atol=1e-13)

    def test_origin_retains_exact_temporal_margins(self):
        zero = model.bound(self.data, 0)
        self.assertEqual(zero["probe_eigenvalue_lower_bound"], self.data["minimum_base_probe_eigenvalue"])
        self.assertEqual(zero["constraint_singular_value_lower_bound"], self.data["minimum_base_constraint_singular_value"])
        self.assertEqual(zero["coordinate_time_timelike_margin"], 1)

    def test_every_actual_highest_jet_is_retained(self):
        actual = model.fields(self.prepared, self.point, self.jets, self.extras, np.array([.0004, -.0002, .0003, .0001]))
        conn = np.array(self.input["connection_coordinates"])
        p4 = np.array([model.prior.complexify(v, (3, 4)) for v in self.input["fourth_spinor_real"]])
        independent = model.third.diagnostic.extended_constraint(self.prepared, self.point, self.jets,
            np.array([.0004, -.0002, .0003, .0001]), conn[:560].reshape(35, 4, 4), conn[560:].reshape(20, 4, 4), p4)
        np.testing.assert_allclose(actual["constraint"], independent, atol=1e-12)

    def test_zero_highest_terms_reduce_to_existing_cubic_evaluator(self):
        extras = {key: np.zeros_like(value) for key, value in self.extras.items()}
        x = np.array([.0002, -.0001, .0003, .0004])
        actual = model.fields(self.prepared, self.point, self.jets, extras, x)
        previous = model.regular.taylor_fields(self.prepared, self.point, self.jets, x)
        for key in ("coframe", "coframe_first", "coframe_second", "psi", "psi_first", "multiplier", "omega", "constraint", "probe"):
            np.testing.assert_allclose(actual[key], previous[key], atol=2e-12)

    def test_changed_coefficients_are_not_assigned_the_old_radius(self):
        self.assertEqual(self.estimate["radius"], 1/16384)
        parent = model.bound(self.data, 2*self.estimate["radius"])
        self.assertLess(parent["constraint_singular_value_lower_bound"], self.data["minimum_base_constraint_singular_value"]/2)
        self.assertGreaterEqual(self.estimate["constraint_singular_value_lower_bound"], self.data["minimum_base_constraint_singular_value"]/2)

    def test_smaller_radii_improve_both_temporal_margins(self):
        smaller = model.bound(self.data, self.estimate["radius"]/2)
        self.assertGreater(smaller["probe_eigenvalue_lower_bound"], self.estimate["probe_eigenvalue_lower_bound"])
        self.assertGreater(smaller["constraint_singular_value_lower_bound"], self.estimate["constraint_singular_value_lower_bound"])

    def test_noninvertible_coframe_bound_is_not_a_positive_result(self):
        result = model.bound(self.data, 1)
        self.assertFalse(result["resolved"])
        self.assertIn("coframe", result["reason"])

    def test_probe_and_constraint_failure_cases_remain_distinct(self):
        bad = dict(self.data, multiplier_first_temporal_column=1e9)
        self.assertIn("probe", model.bound(bad, .001)["reason"])
        bad = dict(self.data, minimum_base_constraint_singular_value=0)
        self.assertIn("constraint", model.bound(bad, self.estimate["radius"])["reason"])

    def test_sampled_field_changes_obey_uniform_norm_estimates(self):
        for sample in self.samples:
            self.assertLessEqual(sample["coframe_change"], self.estimate["coframe_change_bound"]+1e-14)
            self.assertLessEqual(sample["spinor_change"], self.estimate["spinor_change_bound"]+1e-13)
            self.assertLessEqual(sample["temporal_multiplier_change"], self.estimate["temporal_multiplier_change_bound"]+1e-13)

    def test_sampled_blocks_obey_uniform_perturbation_estimates(self):
        for sample in self.samples:
            self.assertLessEqual(sample["probe_weight_change"], self.estimate["probe_weight_change_bound"]+1e-12)
            self.assertLessEqual(sample["constraint_block_change"], self.estimate["constraint_block_change_bound"]+1e-12)
            self.assertGreaterEqual(sample["probe_minimum_eigenvalue"], self.estimate["probe_eigenvalue_lower_bound"]-1e-12)
            self.assertGreaterEqual(sample["constraint_minimum_singular_value"], self.estimate["constraint_singular_value_lower_bound"]-1e-12)

    def test_metric_time_and_spatial_slices_obey_bounds(self):
        for sample in self.samples:
            self.assertLessEqual(sample["metric_inverse_time_component"], -self.estimate["coordinate_time_timelike_margin"]+1e-12)
            self.assertGreaterEqual(sample["spatial_metric_minimum_eigenvalue"], self.estimate["spatial_metric_eigenvalue_lower_bound"]-1e-12)

    def test_all_1114_point_components_remain_small(self):
        self.assertLess(self.report["full_1114_origin_residual_norm"], 1e-8)

    def test_regular_neighborhood_is_not_mistaken_for_a_solution(self):
        self.assertGreater(max(s["probe_residual"] for s in self.samples), 1e-10)
        self.assertTrue(self.report["not_neighborhood_solution_or_Cauchy_existence"])
        self.assertTrue(self.report["not_full_normal_rank_or_PDE_hyperbolicity"])
        self.assertTrue(self.report["not_interval_certified"])
        self.assertTrue(self.report["no_physical_length_units"])
        self.assertFalse(self.report["main_TeX_PDF_changed"])


if __name__ == "__main__":
    unittest.main()
