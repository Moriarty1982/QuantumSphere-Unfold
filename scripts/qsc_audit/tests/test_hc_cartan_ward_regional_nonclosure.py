"""Ward-only smooth nonuniqueness controls and a separate actual-point gate."""
import importlib.util
import json
from pathlib import Path
import unittest

import numpy as np


ROOT = Path(__file__).resolve().parents[3]
SPEC = importlib.util.spec_from_file_location(
    "ward_regional_nonclosure_test", ROOT / "analysis/HC_Cartan_Ward_Regional_Nonclosure.py")
model = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(model)


class WardRegionalNonclosureTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.matrix = model.load_gate()
        cls.report = json.loads((ROOT / "analysis/HC_Cartan_Ward_Regional_Nonclosure.json").read_text(encoding="utf-8"))
        cls.prepared, cls.point, _, _, _ = model.second.neighborhood.load_data()

    def test_current_fingerprints(self):
        self.assertEqual(self.report["input_sha256"], model.input_fingerprints())
        np.testing.assert_array_equal(self.report["gate_matrix"], self.matrix)

    def test_reused_gate_rows_do_not_mean_reused_parent_background(self):
        data = model.fields(self.matrix, 0., np.zeros(3))
        np.testing.assert_array_equal(data["multiplier"][:, 0], self.point["multiplier"][:, 0])
        np.testing.assert_array_equal(data["multiplier_first"][1:, :, 0], self.point["multiplier_first"][1:, :, 0])
        self.assertEqual(np.linalg.norm(data["multiplier_first"][:, :, 1:]), 0.)
        self.assertGreater(np.linalg.norm(self.point["multiplier_first"][1:, :, 1:]), 2.)
        self.assertTrue(self.report["spatial_multiplier_columns_identically_zero_not_saved_parent_jets"])

    def test_temporal_column_and_multiplier_divergence_are_identically_zero(self):
        for t in (0., .125, .25):
            data = model.fields(self.matrix, t, [.002, -.003, .001])
            np.testing.assert_array_equal(data["constraint"][:, 0], np.zeros(4))
            np.testing.assert_array_equal(data["constraint_first"][:, :, 0], np.zeros((4, 4)))
            np.testing.assert_array_equal(data["constraint_second"][:, :, :, 0], np.zeros((4, 4, 4)))
            np.testing.assert_array_equal(np.einsum("mam->a", data["multiplier_first"]), np.zeros(4))

    def test_gate_has_uniform_positive_margin_and_constant_determinant(self):
        rng = np.random.default_rng(2172)
        bound = self.report["uniform_gate_singular_lower_bound"]
        self.assertGreater(bound, .0085)
        for _ in range(30):
            x = rng.normal(size=3)
            x *= model.RADIUS/np.linalg.norm(x)
            ell, _, _, _ = model.projected_vector(self.matrix, x)
            actual = np.vstack((ell, self.matrix[1:]))
            transform = np.eye(4)
            transform[0, 1:] = x
            np.testing.assert_allclose(actual, transform @ self.matrix, atol=1e-16)
            self.assertAlmostEqual(np.linalg.det(actual), np.linalg.det(self.matrix), places=16)
            self.assertGreaterEqual(np.linalg.svd(actual, compute_uv=False)[-1], bound)
            self.assertGreaterEqual(np.linalg.norm(ell), self.report["temporal_multiplier_lower_norm"])

    def test_projection_and_spatial_derivative_orthogonality(self):
        ell, v, dv, _ = model.projected_vector(self.matrix, [.002, -.003, .001])
        self.assertLess(abs(ell @ v), 1e-16)
        np.testing.assert_allclose(dv @ ell+self.matrix[1:] @ v, 0., atol=1e-15)
        self.assertGreater(np.linalg.norm(v), .5)

    def test_analytic_first_and_second_field_derivatives(self):
        z = np.array([.125, .002, -.003, .001])
        step = 1e-6
        def field(at):
            return model.fields(self.matrix, at[0], at[1:])
        center = field(z)
        d1 = np.array([(field(z+step*v)["constraint"]-field(z-step*v)["constraint"])/(2*step)
                       for v in np.eye(4)])
        d2 = np.array([(field(z+step*v)["constraint_first"]-field(z-step*v)["constraint_first"])/(2*step)
                       for v in np.eye(4)])
        np.testing.assert_allclose(d1, center["constraint_first"], atol=1e-7)
        np.testing.assert_allclose(d2, center["constraint_second"], atol=1e-5)
        np.testing.assert_allclose(center["constraint_second"], center["constraint_second"].swapaxes(0, 1), atol=1e-14)

    def test_all_necessary_coordinate_and_Lorentz_identities_hold(self):
        for kind in ("linear", "flat"):
            for t in (0., .125, .25):
                data = model.fields(self.matrix, t, [.002, -.003, .001], kind)
                self.assertLess(np.linalg.norm(model.coordinate.ward(data)), 1e-13)
                for generator in model.lorentz.generators():
                    self.assertEqual(np.sum(data["constraint"]*(generator.T @ data["multiplier"])), 0.)
                a, b = model.differentiated_coordinate_terms(data)
                self.assertLess(np.linalg.norm(a+b), 1e-12)

    def test_second_constitutive_source_cannot_be_silently_omitted(self):
        data = model.fields(self.matrix, 0., np.zeros(3), "linear")
        first, second = model.differentiated_coordinate_terms(data)
        self.assertGreater(np.linalg.norm(first), .5)
        np.testing.assert_allclose(first, -second, atol=1e-14)
        self.assertGreater(np.linalg.norm(data["constraint_second"]), 10.)

    def test_sourced_multiplier_gate_recovers_nonzero_initial_time_drift(self):
        data = model.fields(self.matrix, 0., np.zeros(3), "linear")
        _, second = model.differentiated_coordinate_terms(data)
        drift = data["constraint_first"][0, :, 1:]
        source = np.vstack((np.zeros((1, 3)), -second[1:, 1:]))
        np.testing.assert_allclose(self.matrix @ drift, source, atol=1e-14)
        np.testing.assert_allclose(np.linalg.solve(self.matrix, source), drift, atol=1e-13)
        self.assertGreater(np.linalg.norm(drift), 1.)

    def test_flat_profile_has_zero_initial_jets_but_nonzero_later_residual(self):
        for x in (np.zeros(3), np.array([.002, -.003, .001])):
            initial = model.fields(self.matrix, 0., x, "flat")
            for key in ("constraint", "constraint_first", "constraint_second"):
                self.assertEqual(np.linalg.norm(initial[key]), 0.)
            later = model.fields(self.matrix, .25, x, "flat")
            self.assertGreater(np.linalg.norm(later["constraint"]), .3)
        np.testing.assert_array_equal(model.profile(-.1, "flat"), np.zeros(3))

    def test_synthetic_fields_are_not_claimed_to_be_parent_solutions(self):
        self.assertTrue(self.report["formal_zero_Euler_and_probe_residuals_not_evaluated_parent_equations"])
        self.assertTrue(self.report["not_a_parent_solution_or_parent_nonuniqueness_counterexample"])
        self.assertFalse(self.report["main_TeX_PDF_changed"])

    def test_actual_point_Lorentz2_gate_has_full_column_rank(self):
        gate = model.actual_point_lorentz_gate()
        self.assertEqual(gate.shape, (18, 12))
        singular = np.linalg.svd(gate, compute_uv=False)
        self.assertGreater(singular[-1], .085)
        self.assertEqual(model.second.first.matrix_rank(gate)[0], 12)
        normal = model.second.spatial.normal_curl_system(self.prepared, self.point)
        self.assertEqual(model.second.first.matrix_rank(gate @ normal["induced_curl"])[0], 6)

    def test_actual_Lorentz2_gate_matches_direct_bilinear_mixed_derivative(self):
        rng = np.random.default_rng(1813)
        spatial = rng.normal(size=(4, 3))
        f = np.zeros((4, 4))
        f[:, 1:] = spatial
        expected = []
        step = 1e-4
        for generator in model.lorentz.generators():
            for j in range(1, 4):
                def scalar(t, x):
                    lam = (self.point["multiplier"]+t*self.point["multiplier_first"][0]
                           +x*self.point["multiplier_first"][j])
                    return np.sum(t*f*(generator.T @ lam))
                mixed = (scalar(step, step)-scalar(step, -step)-scalar(-step, step)+scalar(-step, -step))/(4*step**2)
                expected.append(mixed)
        np.testing.assert_allclose(model.actual_point_lorentz_gate() @ spatial.T.reshape(-1), expected, atol=1e-10)

    def test_temporal_F_value_at_one_point_does_not_remove_mixed_F2_source(self):
        # F_0=t*x1*y vanishes initially, but its mixed derivative is y.
        y = np.array([1., 2., 3., 4.])
        derivative = np.zeros((4, 4))
        derivative[:, 0] = y
        sources = [np.sum(derivative*(g.T @ self.point["multiplier"])) for g in model.lorentz.generators()]
        self.assertGreater(np.linalg.norm(sources), .1)

    def test_away_from_special_locus_spatial_F2_source_returns(self):
        lam0 = self.point["multiplier"]
        nearby = lam0+.001*self.point["multiplier_first"][1]
        f2 = np.zeros((4, 4))
        f2[:, 1:] = np.random.default_rng(7931).normal(size=(4, 3))
        base = [np.sum(f2*(g.T @ lam0)) for g in model.lorentz.generators()]
        source = [np.sum(f2*(g.T @ nearby)) for g in model.lorentz.generators()]
        np.testing.assert_array_equal(base, np.zeros(6))
        self.assertGreater(np.linalg.norm(source), .0001)

    def test_invalid_profiles_and_spatial_inputs(self):
        for bad in (float("nan"), float("inf")):
            with self.assertRaises(ValueError):
                model.profile(bad, "flat")
        with self.assertRaises(ValueError):
            model.profile(0., "other")
        with self.assertRaises(ValueError):
            model.projected_vector(self.matrix, [0., 0.])


if __name__ == "__main__":
    unittest.main()
