"""Coefficient-space response, full residual and frozen-order controls."""
import importlib.util
import json
from pathlib import Path
import unittest

import numpy as np


ROOT = Path(__file__).resolve().parents[3]
SPEC = importlib.util.spec_from_file_location("quartic_coefficient_test", ROOT / "analysis/HC_Cartan_Quartic_Coefficient_Refinement.py")
model = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(model)


class QuarticCoefficientMapTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        rng = np.random.default_rng(191940)
        cls.jacobian, cls.coordinates = rng.normal(size=(80, 440)), rng.normal(size=(16, 440))
        cls.matrix = model.coefficient_response(cls.jacobian, cls.coordinates)

    def test_coefficient_map_matches_independent_node_builder(self):
        rng = np.random.default_rng(191941)
        increment = rng.normal(size=model.quartic.COUNT)*1e-5
        coefficients = (self.matrix @ increment).reshape(35, 96)
        for y in (np.eye(4)[0], np.eye(4)[3], np.array([.2, -.3, .1, .4])):
            monomials = np.array([np.prod(y**np.asarray(p)) for p in model.QUARTICS])
            primary, coordinate = model.quartic.leading_response(self.jacobian, self.coordinates, y)
            expected = np.r_[primary @ increment, coordinate @ increment]
            np.testing.assert_allclose(monomials @ coefficients, expected, atol=1e-16, rtol=1e-12)

    def test_selected_real_imaginary_and_coframe_columns(self):
        e_stop = 16*len(model.quartic.E6)
        for column in (0, 15, 1311, e_stop+12, e_stop+24*17+23, model.quartic.COUNT-1):
            increment = np.zeros(model.quartic.COUNT)
            increment[column] = 1.
            for y in (np.array([.1, .2, -.3, .4]), np.eye(4)[3]):
                primary, coordinate = model.quartic.leading_response(self.jacobian, self.coordinates, y)
                weights = np.array([np.prod(y**np.asarray(p)) for p in model.QUARTICS])
                expected = np.r_[primary[:, column], coordinate[:, column]]
                actual = weights @ self.matrix[:, column].reshape(35, 96)
                np.testing.assert_allclose(actual, expected, atol=1e-14, rtol=1e-12)

    def test_rejects_invalid_shapes_and_nonfinite_inputs(self):
        for a, b in ((self.jacobian[:1], self.coordinates), (self.jacobian, self.coordinates[:1]),
                (self.jacobian*np.nan, self.coordinates)):
            with self.assertRaises(ValueError):
                model.coefficient_response(a, b)

    def test_compact_fit_preserves_incompatible_component(self):
        matrix = np.array([[1., 0., 0., 0.], [0., 2., 0., 0.], [0., 0., 0., 0.]])
        target = np.array([3., -4., .125])
        result = model.compact_fit(matrix, target, NumPyBackend())
        self.assertEqual(int(result["primary_rank"]), 2)
        np.testing.assert_allclose(result["primary_increment"], [-3., 2., 0., 0.])
        np.testing.assert_allclose(result["primary_residual"], [0., 0., .125])
        self.assertAlmostEqual(np.linalg.norm(result["primary_left_target"]), .125)

    def test_cutoff_sensitivity_is_kept_as_a_separate_solution(self):
        matrix = np.diag([100., 1e-7, 2e-9])
        result = model.compact_fit(matrix, np.ones(3)*1e-10, NumPyBackend())
        self.assertEqual(int(result["primary_rank"]), 2)
        self.assertEqual(int(result["tighter_cutoff_rank"]), 3)
        self.assertGreater(np.linalg.norm(result["primary_increment"]-result["tighter_cutoff_increment"]), .01)
        self.assertGreater(np.linalg.norm(result["primary_residual"]), 0.)

    def test_known_source_attribution_does_not_hide_a_nonclosed_change(self):
        before, after = np.zeros((70, 80)), np.zeros((70, 80))
        row = model.core.INDEX[(4, 0, 0, 0)]
        before[row, 1] = 1.
        after[:] = before
        unchanged = model.constraint_source_audit(before, after)
        self.assertGreater(unchanged["frozen_source_minimum_constitutive_norm_estimate"], 0.)
        self.assertEqual(unchanged["d_C4_change_norm"], 0.)
        after[row, 1] = 0.
        changed = model.constraint_source_audit(before, after)
        self.assertGreater(changed["d_C4_change_norm"], 0.)


class NumPyBackend:
    def svd(self, matrix, *, full_matrices=False):
        return np.linalg.svd(matrix, full_matrices=full_matrices)


class QuarticRefinementReportTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.report = json.loads((ROOT / "analysis/HC_Cartan_Quartic_Coefficient_Refinement.json").read_text(encoding="utf-8"))

    def test_fingerprints_and_scientific_boundaries(self):
        self.assertEqual(self.report["input_sha256"], model.input_fingerprints())
        self.assertFalse(self.report["main_TeX_PDF_changed"])
        for flag in ("target_from_Taylor_coefficients_not_finite_difference_extraction",
                "frozen_origin_highest_derivative_jacobian_is_still_binary64", "coordinate_increment_fixed_to_zero_not_released",
                "no_previous_regional_bound_reused_for_changed_polynomial", "candidate_does_not_replace_authoritative_parent_polynomial",
                "no_exact_zero_low_order_closure_or_regional_existence_claim", "inherited_rounded_origin_failure_not_repaired_or_hidden"):
            self.assertTrue(self.report[flag])
        self.assertEqual(self.report["origin_field_change"], 0.)
        self.assertEqual(self.report["origin_higher_change"], 0.)
        self.assertEqual(self.report["matrix_shape"], [3360, 3584])
        self.assertGreater(self.report["left_compatibility_target_norm"], 0.)

    def test_full_coefficient_response_and_nonzero_lower_defects(self):
        for report in self.report["reports"]:
            self.assertLess(report["after_quartic_norm"], report["before_quartic_norm"])
            self.assertLess(report["lower_order_coefficient_change"], 1e-14)
            self.assertLess(report["coefficient_response_prediction_error"], max(1e-15, report["before_quartic_norm"]*1e-3))
            self.assertGreater(report["refreshed_combined_enclosure"]["coefficient_level_bounds"][3], 1e-12)
            source = report["known_constitutive_source_attribution"]
            self.assertEqual(source["numerical_rank_per_constitutive_component"], 84)
            self.assertLess(source["d_C4_change_norm"], source["unchanged_d_C4_source_norm"]*1e-4)
            self.assertLess(source["remaining_constitutive_minus_known_source_norm"], source["actual_remaining_constitutive_norm"]*.01)
            for check in report["sample_controls_not_a_regional_proof"]:
                self.assertLess(check["Taylor_tail_discrepancy"], report["refreshed_combined_enclosure"]["tail_bound"])
                self.assertLess(check["new_coordinate_drift"], 1e-12)
        for check in self.report["coefficient_to_node_response_controls"]:
            self.assertLess(check["independent_node_map_discrepancy"], 1e-10)

    def test_shared_field_candidate_reproduces_original_equation_witness(self):
        case = model.control.load_case()
        candidate = (*case[:-1], np.asarray(self.report["candidate_quartic_field_coefficients"]))
        np.testing.assert_allclose(candidate[-1]-case[-1], self.report["increment"], atol=1e-20)
        saved = self.report["reports"][0]["sample_controls_not_a_regional_proof"][0]
        fields, _ = model.control.fields_and_higher(candidate, model.common.RADIUS*np.asarray(saved["direction"]))
        actual = np.linalg.norm(model.common.lower.lower_residual(case[0], fields))
        self.assertAlmostEqual(actual, saved["after_norm"], delta=1e-12)


if __name__ == "__main__":
    unittest.main()
