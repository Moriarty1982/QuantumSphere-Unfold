"""Lower/spatial finite-jet repair with coordinate and identity controls."""
import importlib.util
import json
from pathlib import Path
import unittest

import numpy as np


ROOT = Path(__file__).resolve().parents[3]
SPEC = importlib.util.spec_from_file_location(
    "lower_spatial_repair_test", ROOT / "analysis/HC_Cartan_Lower_Spatial_Repair.py")
model = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(model)


class LowerCoordinateTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.prepared, cls.point, cls.jets, _, cls.full, _ = model.general.domain.load_data()
        _, original, _, _, _ = model.source.neighborhood.load_data()
        reduction = model.source.normal.build_reduction(cls.prepared, original)
        cls.rows = np.column_stack((reduction["gauge"], reduction["sources"])).T
        cls.fields = model.general.domain.temporal.fields(cls.prepared, cls.point, cls.jets, cls.full, np.eye(4)[0]/16384)

    def test_coordinate_round_trip_and_mixed_partials(self):
        rng = np.random.default_rng(20261022)
        values = model.lower_values(self.fields)+rng.normal(size=320)*.01
        changed = model.with_lower_values(self.fields, values)
        np.testing.assert_allclose(model.lower_values(changed), values, atol=1e-14)
        np.testing.assert_array_equal(changed["coframe_second"], changed["coframe_second"].swapaxes(0, 1))
        for key in ("coframe", "coframe_first", "psi", "multiplier"):
            np.testing.assert_array_equal(changed[key], self.fields[key])

    def test_normal_selector_and_fixed_coordinate_kernel(self):
        values = model.lower_values(self.fields)
        np.testing.assert_allclose(model.normal_selector() @ values, model.general.normal_values(self.fields), atol=1e-14)
        basis = model.free_basis(self.rows)
        self.assertEqual(basis.shape, (320, 304))
        np.testing.assert_allclose(self.rows @ model.normal_selector() @ basis, 0, atol=1e-14)
        np.testing.assert_allclose(basis.T @ basis, np.eye(304), atol=1e-13)

    def test_polynomial_directional_jacobian_has_no_small_step_noise(self):
        values = model.lower_values(self.fields)
        direction = model.free_basis(self.rows) @ np.random.default_rng(20261023).normal(size=304)
        results = []
        for step in (.5, 16.):
            plus = model.lower_residual(self.prepared, model.with_lower_values(self.fields, values+step*direction))
            minus = model.lower_residual(self.prepared, model.with_lower_values(self.fields, values-step*direction))
            results.append((plus-minus)/(2*step))
        np.testing.assert_allclose(results[0], results[1], atol=1e-10, rtol=1e-10)


class RepairedJetTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.report = json.loads((ROOT / "analysis/HC_Cartan_Lower_Spatial_Repair.json").read_text(encoding="utf-8"))

    def test_fingerprints(self):
        self.assertEqual(self.report["input_sha256"], model.input_fingerprints())

    def test_lower_repair_resolves_all_rows_without_coordinate_drift(self):
        for sample in self.report["samples"]:
            lower = sample["lower_repair"]
            self.assertGreater(lower["initial_norm"], 1e-7)
            self.assertLess(lower["final_norm"], 1e-10)
            self.assertLess(lower["fixed_coordinate_error"], 1e-11)
            self.assertLess(sample["primary_residual_norm"], 1e-10)
            self.assertLess(sample["all_constitutive_curls_norm"], 1e-10)

    def test_known_sources_and_first_prolongation_resolve_numerically(self):
        for sample in self.report["samples"]:
            self.assertLess(sample["known_identity_sources_norm"], 1e-9)
            self.assertEqual(sample["higher_rank"], 220)
            self.assertLess(sample["attribution"]["span_error"], 1e-8)
            self.assertLess(sample["first_after_higher_correction"], 1e-8)
            self.assertLess(sample["first_after_half_step"], 1e-8)
            self.assertLess(sample["higher_direct_affinity_error"], 1e-8)

    def test_saved_coordinates_reproduce_actual_unprojected_equations(self):
        prepared, point, jets, _, full, _ = model.general.domain.load_data()
        for sample in self.report["samples"]:
            x = np.asarray(sample["coordinate"])
            fields = model.general.domain.temporal.fields(prepared, point, jets, full, x)
            repaired = model.with_lower_values(fields, sample["lower_repair"]["fitted_lower_coordinates"])
            self.assertLess(np.linalg.norm(model.lower_residual(prepared, repaired)), 1e-10)
            higher = model.prior.previous.translated_higher(jets, full, x)
            delta = model.source.regular.unpack(np.r_[sample["higher_increment"], np.zeros(480)])
            changed = {key: higher[key]+delta[key] for key in higher}
            self.assertLess(np.linalg.norm(model.prior.previous.first_prolongation(prepared, repaired, changed)), 1e-8)

    def test_scope_excludes_regional_and_full_higher_claims(self):
        self.assertEqual((self.report["lower_coordinates"], self.report["free_lower_coordinates"]), (320, 304))
        self.assertEqual(self.report["fixed_normal_coordinates"], 16)
        self.assertTrue(self.report["no_integrable_regional_field_or_1114_completion"])
        self.assertFalse(self.report["main_TeX_PDF_changed"])


if __name__ == "__main__":
    unittest.main()
