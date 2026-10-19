"""Known first identities and prescribed-higher attribution controls."""
import importlib.util
import json
from pathlib import Path
import unittest

import numpy as np


ROOT = Path(__file__).resolve().parents[3]
SPEC = importlib.util.spec_from_file_location(
    "first_attribution_test", ROOT / "analysis/HC_Cartan_First_Compatibility_Attribution.py")
model = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(model)


class KnownIdentityTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.prepared, cls.point, cls.jets, _, cls.full, _ = model.general.domain.load_data()

    def test_nonzero_lower_residuals_are_retained_in_identity_sources(self):
        x = np.array([1., 2., -1., 1.])/16384
        fields = model.general.domain.temporal.fields(self.prepared, self.point, self.jets, self.full, x)
        rng = np.random.default_rng(20261020)
        changed = model.general.with_normal_values(fields,
            model.general.normal_values(fields)+rng.normal(size=56)*.03)
        higher = model.previous.translated_higher(self.jets, self.full, x)
        evaluated = model.general.equations(self.prepared, changed)
        rhs = model.known_rhs(changed, evaluated)
        derivative = model.previous.first_prolongation(self.prepared, changed, higher)
        self.assertGreater(np.linalg.norm(rhs[24:]), .001)
        np.testing.assert_allclose(model.known_rows(changed) @ derivative, rhs, atol=2e-8, rtol=1e-7)

    def test_mixed_constitutive_curls_match_primary_equations(self):
        fields = model.general.domain.temporal.fields(self.prepared, self.point, self.jets, self.full, np.eye(4)[0]/16384)
        evaluated = model.general.equations(self.prepared, fields)
        curls = model.constitutive_curls(fields, evaluated)
        self.assertEqual(curls.shape, (24,))
        np.testing.assert_allclose(curls[:12], evaluated["mixed_curl"].ravel(), atol=1e-12)


class AttributionReportTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.report = json.loads((ROOT / "analysis/HC_Cartan_First_Compatibility_Attribution.json").read_text(encoding="utf-8"))

    def test_fingerprints(self):
        self.assertEqual(self.report["input_sha256"], model.input_fingerprints())

    def test_known_rows_exhaust_all_higher_left_space_in_samples(self):
        for sample in self.report["samples"]:
            self.assertEqual((sample["all_higher_rank"], sample["normal_higher_rank"]), (220, 160))
            self.assertEqual((sample["known_row_rank"], sample["left_nullity"]), (52, 52))
            self.assertLess(sample["known_rows_annihilation_error"], 1e-8)
            self.assertLess(sample["known_span_left_space_error"], 1e-8)

    def test_actual_identities_and_reconstruction(self):
        for sample in self.report["samples"]:
            self.assertLess(sample["known_identity_error"], 1e-8)
            self.assertLess(sample["known_identity_half_step_error"], 1e-8)
            self.assertLess(sample["projected_reconstruction_error"], 1e-8)

    def test_prescribed_data_release_reduces_but_does_not_remove_off_origin_rest(self):
        for sample in self.report["samples"][1:]:
            self.assertGreater(sample["normal_only_compatibility_norm"], .004)
            self.assertLess(sample["all_higher_compatibility_norm"], 1e-6)
            self.assertGreater(sample["all_higher_compatibility_norm"], 1e-7)
            self.assertGreater(sample["prescribed_higher_increment_norm"], .01)

    def test_unprojected_corrected_derivatives_match_affine_prediction(self):
        for sample in self.report["samples"]:
            self.assertLess(sample["direct_higher_affinity_error"], 1e-8)
            self.assertAlmostEqual(sample["corrected_direct_first_prolongation_norm"],
                                   sample["all_higher_compatibility_norm"], delta=2e-9)

    def test_scope_and_coordinate_count(self):
        self.assertEqual((self.report["normal_coordinates"], self.report["additional_prescribed_coordinates"]), (224, 496))
        self.assertEqual(sum(self.report["known_row_blocks"].values()), 52)
        self.assertTrue(self.report["no_regional_solution_or_nonlinear_lower_repair"])
        self.assertFalse(self.report["main_TeX_PDF_changed"])


if __name__ == "__main__":
    unittest.main()
