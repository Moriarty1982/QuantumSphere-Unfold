"""General-coframe normal equations checked against original and differential data."""
import importlib.util
import json
from pathlib import Path
import unittest

import numpy as np


ROOT = Path(__file__).resolve().parents[3]
SPEC = importlib.util.spec_from_file_location(
    "general_normal_chart_test", ROOT / "analysis/HC_Cartan_General_Normal_Chart.py")
model = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(model)


class GeneralNormalChartTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.report = json.loads((ROOT / "analysis/HC_Cartan_General_Normal_Chart.json").read_text(encoding="utf-8"))
        cls.prepared, cls.point, cls.jets, _, cls.full, _ = model.domain.load_data()
        cls.radius = cls.report["radius_used_for_samples"]
        cls.services = model.prior.create_container().services()
        cls.coordinate_rows = np.array(cls.report["fixed_coordinate_rows"])

    def fields(self, x):
        return model.domain.temporal.fields(self.prepared, self.point, self.jets, self.full, x)

    def test_fingerprints(self):
        self.assertEqual(self.report["input_sha256"], model.input_fingerprints())

    def test_normal_point_reproduces_existing_equations_and_matrix(self):
        fields = self.fields(np.zeros(4))
        actual = model.equations(self.prepared, fields)["vector"]
        old = model.prior.source.normal.normal_equations(self.prepared, self.point)
        np.testing.assert_allclose(actual, old, atol=1e-10)
        matrix = model.normal_system(self.prepared, fields, services=self.services)["matrix"]
        original = model.prior.source.normal.build_reduction(self.prepared, self.point)["matrix"]
        np.testing.assert_allclose(matrix, original, atol=1e-11)
        self.assertLess(self.report["origin_matrix_match_error"], 1e-10)

    def test_normal_value_round_trip_and_input_preservation(self):
        fields = self.fields(np.zeros(4))
        values = model.normal_values(fields)
        clone = model.with_normal_values(fields, values)
        np.testing.assert_array_equal(model.normal_values(clone), values)
        model.with_normal_values(fields, np.zeros(56))
        np.testing.assert_array_equal(model.normal_values(fields), values)

    def test_actual_affinity_away_from_origin(self):
        fields = self.fields(self.radius*np.array([.4, -.3, .2, .1]))
        system = model.normal_system(self.prepared, fields, services=self.services)
        values = model.normal_values(fields)+np.random.default_rng(191068).normal(size=56)*.05
        actual = model.equations(self.prepared, model.with_normal_values(fields, values))["vector"]
        np.testing.assert_allclose(actual, system["base"]+system["matrix"] @ values, atol=1e-10)

    def test_general_connection_derivative_against_independent_Taylor_fields(self):
        x = self.radius*np.array([.3, -.2, .4, .1])
        fields = self.fields(x)
        first = model.connection_jets(self.prepared, fields)["first"]
        step = 1e-7
        difference = np.array([(self.fields(x+step*e)["omega"]-self.fields(x-step*e)["omega"])/(2*step)
                               for e in np.eye(4)])
        np.testing.assert_allclose(first, difference, atol=1e-7, rtol=1e-8)

    def test_mixed_curl_against_independent_constraint_derivative(self):
        x = self.radius*np.array([.3, -.2, .4, .1])
        step = 1e-7
        derivative = np.array([(self.fields(x+step*e)["constraint"]-self.fields(x-step*e)["constraint"])/(2*step)
                               for e in np.eye(4)])
        actual = model.equations(self.prepared, self.fields(x))["mixed_curl"]
        expected = np.array([derivative[0, :, i]-derivative[i, :, 0] for i in (1, 2, 3)])
        np.testing.assert_allclose(actual, expected, atol=1e-7)

    def test_general_probe_matches_independent_existing_evaluator(self):
        fields = self.fields(self.radius*np.array([-.3, .2, .4, -.1]))
        actual = model.equations(self.prepared, fields)
        np.testing.assert_allclose(actual["probe"], fields["probe"], atol=1e-12)
        np.testing.assert_allclose(actual["connection"]["omega"], fields["omega"], atol=1e-12)

    def test_all_sampled_ranks_and_augmented_charts(self):
        self.assertEqual(len(self.report["samples"]), 13)
        for sample in self.report["samples"]:
            self.assertEqual(sample["rank"], 40)
            self.assertGreater(sample["singular_40"], .1)
            self.assertLess(sample["singular_41"], 1e-10)
            self.assertGreater(sample["augmented_minimum_singular"], .1)
            self.assertLess(sample["augmented_inverse_error"], 1e-10)
            self.assertLess(sample["affine_error"], 1e-10)

    def test_chart_rejects_singular_or_malformed_input(self):
        with self.assertRaises(ValueError):
            model.chart_report(np.zeros((68, 56)), np.zeros((16, 56)))
        with self.assertRaises(ValueError):
            model.chart_report(np.zeros((56, 56)), np.zeros((16, 56)))

    def test_varying_coefficients_and_remaining_compatibility_not_hidden(self):
        self.assertGreater(max(s["matrix_change_norm"] for s in self.report["samples"]), .01)
        self.assertGreater(max(s["origin_chart_compatibility_residual"] for s in self.report["samples"]), 1e-8)
        self.assertGreater(max(s["proposed_actual_equations_norm"] for s in self.report["samples"]), 1e-8)
        self.assertTrue(self.report["not_uniform_rank_certificate_or_regional_solution"])
        self.assertTrue(self.report["fixed_rows_are_not_a_transported_gauge_or_source_classification"])
        self.assertTrue(self.report["qualitative_augmented_chart_openness_not_quantified_radius"])
        self.assertFalse(self.report["main_TeX_PDF_changed"])


if __name__ == "__main__":
    unittest.main()
