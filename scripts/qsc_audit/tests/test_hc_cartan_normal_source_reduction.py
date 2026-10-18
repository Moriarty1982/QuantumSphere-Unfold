"""Explicit compatible normal inverse, unresolved sources and current-jet controls."""
import importlib.util
import json
from pathlib import Path
import unittest

import numpy as np


ROOT = Path(__file__).resolve().parents[3]
SPEC = importlib.util.spec_from_file_location(
    "normal_source_reduction_test", ROOT / "analysis/HC_Cartan_Normal_Source_Reduction.py")
model = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(model)


class NormalSourceReductionTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.prepared, cls.point, cls.jets, _, _ = model.neighborhood.load_data()
        cls.reduction = model.build_reduction(cls.prepared, cls.point)
        cls.report = json.loads((ROOT / "analysis/HC_Cartan_Normal_Source_Reduction.json").read_text(encoding="utf-8"))
        cls.n, cls.inv, cls.g, cls.u, cls.left = [cls.reduction[key] for key in (
            "matrix", "inverse", "gauge", "sources", "left_null")]

    def test_fingerprints_and_saved_bases(self):
        self.assertEqual(self.report["input_sha256"], model.input_fingerprints())
        np.testing.assert_allclose(self.report["source_basis"], self.u, atol=1e-12)
        np.testing.assert_allclose(self.report["gauge_basis"], self.g, atol=1e-12)

    def test_dimensions_and_rank_gap(self):
        self.assertEqual(self.n.shape, (68, 56))
        self.assertEqual(self.reduction["rank"], 40)
        self.assertEqual(self.left.shape, (68, 28))
        self.assertGreater(self.reduction["singular"][39], .1)
        self.assertLess(self.reduction["singular"][40], 1e-10)

    def test_orthogonal_ten_plus_six_is_entire_normal_kernel(self):
        combined = np.c_[self.g, self.u]
        np.testing.assert_allclose(combined.T @ combined, np.eye(16), atol=1e-12)
        np.testing.assert_allclose(self.n @ combined, 0., atol=1e-11)
        np.testing.assert_allclose(combined @ combined.T, self.reduction["null_projector"], atol=1e-11)

    def test_inverse_satisfies_penrose_and_range_projectors(self):
        np.testing.assert_allclose(self.n @ self.inv @ self.n, self.n, atol=1e-10)
        np.testing.assert_allclose(self.inv @ self.n @ self.inv, self.inv, atol=1e-10)
        np.testing.assert_allclose(self.n @ self.inv, np.eye(68)-self.left @ self.left.T, atol=1e-11)
        np.testing.assert_allclose(self.inv @ self.n, np.eye(56)-self.g @ self.g.T-self.u @ self.u.T, atol=1e-11)

    def test_random_compatible_rhs_and_prescribed_source_coordinates(self):
        rng = np.random.default_rng(4283)
        for _ in range(6):
            rhs = self.n @ rng.normal(size=56)
            g, q = rng.normal(size=10), rng.normal(size=6)
            delta = model.solve(self.reduction, rhs, g, q)
            np.testing.assert_allclose(self.n @ delta, rhs, atol=1e-10)
            np.testing.assert_allclose(self.g.T @ delta, g, atol=1e-11)
            np.testing.assert_allclose(self.u.T @ delta, q, atol=1e-11)

    def test_source_parameterization_recovers_every_arbitrary_solution(self):
        x = np.random.default_rng(7820).normal(size=56)
        result = model.solve(self.reduction, self.n @ x, self.g.T @ x, self.u.T @ x)
        np.testing.assert_allclose(result, x, atol=1e-11)

    def test_incompatible_rhs_is_rejected_not_silently_solved(self):
        bad = self.left[:, 0]
        with self.assertRaisesRegex(ValueError, "compatibility"):
            model.solve(self.reduction, bad)
        projected = self.inv @ bad
        self.assertGreater(np.linalg.norm(self.n @ projected-bad), .99)

    def test_six_sources_have_zero_spinor_normal_and_temporal_multiplier_column(self):
        np.testing.assert_array_equal(self.u[16:40], np.zeros((24, 6)))
        np.testing.assert_array_equal(self.u[[40+4*a for a in range(4)]], np.zeros((4, 6)))
        projected = self.u[40:][model.remaining.SPATIAL_INDICES]
        self.assertEqual(np.linalg.matrix_rank(projected, tol=1e-9), 6)

    def test_all_68_equations_are_checked_on_actual_source_shifted_points(self):
        for q in (np.zeros(6), np.array([.01, -.005, .003, .002, .004, -.001])):
            delta = model.solve(self.reduction, np.zeros(68), source_values=q)
            changed = model.remaining.normal_point(self.point, delta)
            self.assertLess(np.linalg.norm(model.normal_equations(self.prepared, changed)), 1e-10)
            np.testing.assert_array_equal(changed["psi_first"], self.point["psi_first"])
            np.testing.assert_array_equal(changed["multiplier_first"][1:], self.point["multiplier_first"][1:])

    def test_six_sources_are_detected_by_latest_higher_equations(self):
        response, affinity = model.higher_source_response(self.prepared, self.point, self.jets, self.reduction)
        self.assertEqual(response.shape, (384, 6))
        self.assertEqual(np.linalg.matrix_rank(response, tol=1e-9), 6)
        self.assertGreater(np.linalg.svd(response, compute_uv=False)[-1], 16.)
        self.assertLess(np.linalg.norm(affinity), 1e-8)
        q = np.random.default_rng(7125).normal(size=6)*.01
        changed = model.remaining.normal_point(self.point, self.u @ q)
        base = model.regular.equations(self.prepared, self.point, self.jets)["vector"]
        actual = model.regular.equations(self.prepared, changed, self.jets)["vector"]
        np.testing.assert_allclose(actual-base, response @ q, atol=1e-9)

    def test_ten_plus_six_normalization_rows_give_unique_increment(self):
        augmented = np.vstack((self.n, self.g.T, self.u.T))
        self.assertEqual(augmented.shape, (84, 56))
        self.assertEqual(np.linalg.matrix_rank(augmented, tol=1e-9), 56)
        rng = np.random.default_rng(5142)
        actual = rng.normal(size=56)
        expected = np.linalg.lstsq(augmented, augmented @ actual, rcond=1e-10)[0]
        solved = model.solve(self.reduction, self.n @ actual, self.g.T @ actual, self.u.T @ actual)
        np.testing.assert_allclose(solved, expected, atol=1e-10)

    def test_scope_does_not_call_six_sources_gauge_or_claim_full_evolution(self):
        self.assertTrue(self.report["six_coordinates_not_proved_gauge_or_physical_modes"])
        self.assertTrue(self.report["zero_source_default_is_only_particular_solution_not_closure"])
        self.assertTrue(self.report["pointwise_reduction_not_regional_evolution_or_wellposedness"])
        self.assertFalse(self.report["main_TeX_PDF_changed"])

    def test_bad_coordinate_shapes_tolerances_and_dependent_columns(self):
        for rhs in (np.zeros(67), np.full(68, np.nan)):
            with self.assertRaises(ValueError):
                model.solve(self.reduction, rhs)
        with self.assertRaises(ValueError):
            model.solve(self.reduction, np.zeros(68), source_values=np.zeros(5))
        with self.assertRaises(ValueError):
            model.solve(self.reduction, np.zeros(68), tolerance=0.)
        with self.assertRaises(ValueError):
            model.orthonormal_columns(np.zeros((56, 6)))


if __name__ == "__main__":
    unittest.main()
