"""General-coordinate first source gate and independent Taylor translation checks."""
import importlib.util
import json
from pathlib import Path
import unittest

import numpy as np


ROOT = Path(__file__).resolve().parents[3]
SPEC = importlib.util.spec_from_file_location(
    "general_first_gate_test", ROOT / "analysis/HC_Cartan_General_First_Source_Gate.py")
model = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(model)


class TranslatedJetTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.prepared, cls.point, cls.jets, _, cls.full, _ = model.general.domain.load_data()

    def test_holonomic_derivatives_against_translated_taylor_fields(self):
        x = np.array([1., -2., 3., -1.])*1e-5
        fields = model.general.domain.temporal.fields(self.prepared, self.point, self.jets, self.full, x)
        higher = model.translated_higher(self.jets, self.full, x)
        derivatives = model.field_derivatives(fields, higher)
        step = 1e-6
        for r, direction in enumerate(np.eye(4)):
            plus = model.general.domain.temporal.fields(self.prepared, self.point, self.jets, self.full, x+step*direction)
            minus = model.general.domain.temporal.fields(self.prepared, self.point, self.jets, self.full, x-step*direction)
            for key in model.FIELD_KEYS:
                np.testing.assert_allclose((plus[key]-minus[key])/(2*step), derivatives[r][key], atol=3e-7, rtol=1e-7)

    def test_translation_at_origin_retains_higher_data(self):
        actual = model.translated_higher(self.jets, self.full, np.zeros(4))
        for key in ("e3", "p2", "l2"):
            np.testing.assert_array_equal(actual[key], self.jets[key])


class SampledSourceGateTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.report = json.loads((ROOT / "analysis/HC_Cartan_General_First_Source_Gate.json").read_text(encoding="utf-8"))

    def test_fingerprints(self):
        self.assertEqual(self.report["input_sha256"], model.input_fingerprints())

    def test_coordinate_kernel_sections(self):
        for sample in self.report["samples"]:
            self.assertEqual(sample["normal_rank"], 40)
            self.assertLess(sample["normal_kernel_error"], 1e-10)
            self.assertLess(sample["coordinate_transport_error"], 1e-10)

    def test_origin_recovers_previous_exact_affine_stage(self):
        origin = self.report["samples"][0]
        self.assertLess(origin["origin_higher_matrix_error"], 1e-9)
        self.assertLess(origin["origin_source_response_error"], 1e-6)
        self.assertLess(origin["origin_prolongation_error"], 1e-6)

    def test_source_gate_is_resolved_at_both_steps(self):
        for sample in self.report["samples"]:
            self.assertEqual(sample["higher_rank"], 160)
            self.assertEqual(sample["source_gate_rank"], 6)
            self.assertGreater(min(sample["gate_singular_values"]), .1)
            np.testing.assert_allclose(sample["gate_singular_values"], sample["half_step_gate_singular_values"], atol=1e-5)

    def test_differencing_changes_are_small_against_source_gate(self):
        for sample in self.report["samples"]:
            self.assertLess(sample["source_response_step_change"], 1e-6)
            self.assertLess(sample["first_prolongation_step_change"], 1e-7)

    def test_off_origin_remaining_compatibility_is_not_hidden(self):
        for sample in self.report["samples"][1:]:
            self.assertGreater(sample["projected_residual_after_linear_source_correction"], .004)
            self.assertLess(sample["projected_residual_after_linear_source_correction"], sample["projected_residual_before"])
            self.assertGreater(sample["primary_residual_norm"], 1e-8)

    def test_source_step_does_not_change_primary_equations(self):
        for sample in self.report["samples"]:
            self.assertLess(sample["primary_change_after_source_correction"], 1e-9)

    def test_scope_is_sampled_numerical_and_not_paper_integration(self):
        self.assertTrue(self.report["directional_derivatives_are_numerical"])
        self.assertTrue(self.report["source_directions_are_coordinate_kernel_sections_not_physical_classification"])
        self.assertFalse(self.report["main_TeX_PDF_changed"])


if __name__ == "__main__":
    unittest.main()
