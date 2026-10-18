"""Spatial curl compatibility and its limited first-order regular-branch completion."""
import hashlib
import importlib.util
import json
from pathlib import Path
import unittest

import numpy as np


ROOT = Path(__file__).resolve().parents[3]
SPEC = importlib.util.spec_from_file_location("cartan_spatial_propagation", ROOT / "analysis/HC_Cartan_Spatial_Propagation.py")
model = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(model)


class HCCartanSpatialPropagationTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.prepared, cls.old = model.load_point()
        cls.frozen_normal = model.normal_curl_system(cls.prepared, cls.old)
        cls.frozen_first = model.first_completion(cls.prepared, cls.old)
        cls.restricted = model.reprepare_curls(cls.prepared, cls.old)
        cls.solved = model.prepare_integrable_point(cls.prepared, cls.old)
        cls.point = cls.solved["point"]
        cls.first = model.first_completion(cls.prepared, cls.point)
        cls.normal = model.normal_curl_system(cls.prepared, cls.point)
        cls.report = json.loads((ROOT / "analysis/HC_Cartan_Spatial_Propagation.json").read_text(encoding="utf-8"))

    def assertClose(self, actual, expected, atol=2e-9, rtol=3e-8):
        np.testing.assert_allclose(actual, expected, atol=atol, rtol=rtol)

    def test_input_fingerprint_matches_saved_regular_point(self):
        fingerprint = hashlib.sha256((ROOT / "analysis/HC_Cartan_Cauchy_Rank.json").read_bytes()).hexdigest()
        self.assertEqual(self.report["previous_input_sha256"], fingerprint)

    def test_old_point_satisfies_original_point_equations(self):
        p = self.old
        r = model.rank_model.point_equations(self.prepared, p["psi_first"], p["coframe_second"], p["multiplier"], p["multiplier_first"])
        self.assertLess(np.linalg.norm(r["vector"]), 1e-9)

    def test_old_point_has_nonzero_spatial_and_mixed_curls(self):
        curls = model.curl_constraints(self.prepared, self.old)
        self.assertGreater(np.linalg.norm(curls[:3]), 40)
        self.assertGreater(np.linalg.norm(curls[3:]), 30)

    def test_explicit_coordinate_product_rule_matches_constraint_derivative(self):
        for p in (self.old, self.point):
            self.assertClose(model.explicit_curl(self.prepared, p), model.curl_constraints(self.prepared, p))

    def test_symmetric_spinor_hessians_cancel_from_all_curls(self):
        x = np.random.default_rng(518).normal(size=240)
        p2 = model.prior.unpack_second(x, True)
        first = model.constraint_first(self.prepared, self.old, p2)
        curls = np.array([first[r, :, s]-first[s, :, r] for r, s in model.PAIRS])
        self.assertClose(curls, model.curl_constraints(self.prepared, self.old))

    def test_principal_spinor_map_is_surjective(self):
        principal = model.constraint_principal_map(self.prepared["data"]["psi"])
        self.assertEqual(principal.shape, (4, 24))
        self.assertEqual(np.linalg.matrix_rank(principal), 4)

    def test_zero_spinor_is_not_assumed_to_have_surjective_principal_map(self):
        p = dict(self.prepared, data=dict(self.prepared["data"], psi=np.zeros((3, 4), complex)))
        with self.assertRaises(ValueError):
            model.symmetric_constraint_completion(p, self.old)

    def test_symmetric_completion_produces_holonomic_second_derivatives(self):
        result = model.symmetric_constraint_completion(self.prepared, self.old)
        self.assertClose(result["psi_second"], result["psi_second"].swapaxes(0, 1))

    def test_irreducible_constraint_residual_is_the_antisymmetric_part(self):
        result = model.symmetric_constraint_completion(self.prepared, self.old)
        residual = result["residual"]
        self.assertClose(residual, -residual.transpose(2, 1, 0))
        curl_norm = np.linalg.norm(model.curl_constraints(self.prepared, self.old))
        self.assertAlmostEqual(np.linalg.norm(residual), curl_norm/np.sqrt(2), places=9)

    def test_symmetric_second_jet_constraint_map_has_rank_forty(self):
        base = model.constraint_first(self.prepared, self.old)
        matrix = np.column_stack([(model.constraint_first(self.prepared, self.old, model.prior.unpack_second(e, True))-base).reshape(-1)
                                  for e in np.eye(240)])
        self.assertEqual(np.linalg.matrix_rank(matrix, tol=1e-9), 40)

    def test_original_normal_system_gains_six_independent_rows(self):
        self.assertEqual(self.normal["original_rank"], 34)
        self.assertEqual(self.normal["rank"], 40)
        self.assertEqual(self.normal["matrix"].shape, (68, 56))

    def test_mixed_curl_on_old_normal_kernel_has_rank_six(self):
        self.assertEqual(self.normal["original_kernel"].shape, (56, 22))
        self.assertEqual(self.normal["induced_rank"], 6)
        self.assertEqual(np.linalg.matrix_rank(self.normal["induced_curl"], tol=1e-9), 6)

    def test_six_left_null_projections_are_secondary_compatibility_conditions(self):
        self.assertEqual(self.normal["left_null"].shape, (12, 6))
        self.assertClose(self.normal["left_null"].T @ self.normal["induced_curl"], 0)

    def test_old_data_fail_secondary_normal_compatibility(self):
        self.assertGreater(np.linalg.norm(self.frozen_normal["compatibility_projection"]), 1)
        self.assertGreater(np.linalg.norm(self.frozen_normal["residual"]), 1)

    def test_regular_completion_has_sixteen_remaining_normal_directions(self):
        self.assertEqual(self.normal["remaining_kernel"].shape, (56, 16))
        self.assertClose(self.normal["matrix"] @ self.normal["remaining_kernel"], 0)

    def test_six_spatial_multiplier_velocity_directions_remain(self):
        self.assertEqual(self.normal["remaining_spatial_multiplier_rank"], 6)

    def test_normal_curl_equations_are_affine_in_normal_unknowns(self):
        x = np.random.default_rng(519).normal(size=56)*.03
        self.assertClose(self.normal["evaluate"](x), self.normal["base"]+self.normal["matrix"] @ x)

    def test_higher_spinor_jets_cannot_repair_frozen_first_constraints(self):
        self.assertEqual(self.frozen_first["rank"], 136)
        self.assertGreater(np.linalg.norm(self.frozen_first["residual"]), 40)

    def test_fixed_first_spinor_geometry_multiplier_repair_is_affine(self):
        x = np.random.default_rng(520).normal(size=224)*.03
        r = self.restricted
        self.assertClose(r["evaluate"](x), r["base"]+r["matrix"] @ x)

    def test_fixed_first_spinor_repair_cannot_satisfy_the_full_system(self):
        self.assertEqual(self.restricted["rank"], 28)
        self.assertGreater(np.linalg.norm(self.restricted["residual"]), 7)

    def test_full_new_preparation_has_exact_quadratic_form(self):
        x = np.random.default_rng(521).normal(size=320)*.03
        p = model.point_fields(self.point["multiplier"], x)
        equations = model.rank_model.point_equations(self.prepared, p["psi_first"], p["coframe_second"], p["multiplier"], p["multiplier_first"])["vector"]
        actual = np.concatenate((equations, model.curl_constraints(self.prepared, p).reshape(-1)))
        expected = self.solved["base"]+self.solved["linear"] @ x
        expected[56:] += model.curl_quadratic(x)
        self.assertClose(actual, expected)

    def test_quadratic_jacobian_matches_independent_differences(self):
        x = self.solved["solution"]
        direction = np.random.default_rng(522).normal(size=320)
        step = 1e-5
        actual = self.solved["linear"] @ direction
        actual[56:] += (model.curl_quadratic(x+step*direction)-model.curl_quadratic(x-step*direction))/(2*step)
        self.assertClose(actual, self.solved["jacobian"] @ direction, atol=2e-7)

    def test_repreparation_reduces_all_unprojected_residuals(self):
        history = self.solved["history"]
        self.assertGreater(history[0]["residual_norm"], 60)
        self.assertTrue(all(a["residual_norm"] > b["residual_norm"] for a, b in zip(history, history[1:])))
        self.assertLess(np.linalg.norm(self.solved["residual"]), 1e-10)

    def test_reprepared_original_point_equations_and_all_curls_hold(self):
        residual = self.solved["residual"]
        for block in (residual[:16], residual[16:40], residual[40:56], residual[56:]):
            self.assertLess(np.linalg.norm(block), 1e-10)

    def test_multiplier_value_and_temporal_probe_regularity_do_not_change(self):
        self.assertClose(self.point["multiplier"], self.old["multiplier"])
        block = model.rank_model.probe_constraint_block(np.eye(4), self.prepared["data"]["psi"], self.point["multiplier"])
        self.assertGreater(block["weight_eigenvalues"][0], .96)
        self.assertGreater(block["singular_values"][-1], .03)

    def test_saved_point_coordinates_reproduce_new_preparation(self):
        self.assertClose(self.report["reprepared_first_jet"]["point_coordinates"], self.solved["solution"])
        self.assertClose(self.report["reprepared_first_jet"]["higher_coordinates"], self.first["solution"])

    def test_curl_free_data_admit_constructive_symmetric_constraint_completion(self):
        r = model.symmetric_constraint_completion(self.prepared, self.point)
        self.assertLess(np.linalg.norm(r["residual"]), 1e-10)

    def test_first_constraint_probe_system_has_reported_size_and_rank(self):
        self.assertEqual(self.first["matrix"].shape, (160, 400))
        self.assertEqual(self.first["rank"], 136)

    def test_all_first_constraint_and_probe_equations_hold(self):
        self.assertLess(np.linalg.norm(model.constraint_first(self.prepared, self.point, self.first["psi_second"])), 1e-9)
        self.assertLess(np.linalg.norm(model.first_probe(self.prepared, self.point, self.first["psi_second"], self.first["multiplier_second"])), 1e-9)

    def test_second_multiplier_and_spinor_jets_are_holonomic(self):
        for key in ("psi_second", "multiplier_second"):
            self.assertClose(self.first[key], self.first[key].swapaxes(0, 1))

    def test_first_completion_map_is_affine(self):
        x = np.random.default_rng(523).normal(size=400)*.02
        self.assertClose(self.first["evaluate"](x), self.first["base"]+self.first["matrix"] @ x)

    def test_full_normal_rhs_is_compatible_on_new_data(self):
        self.assertLess(np.linalg.norm(self.normal["residual"]), 1e-9)
        self.assertLess(np.linalg.norm(self.normal["compatibility_projection"]), 1e-9)

    def test_independent_connection_constraint_probe_differences_agree(self):
        differences = model.independent_checks(self.prepared, self.point, self.first)
        for key in ("connection_first_difference_error", "constraint_first_difference_error", "probe_first_difference_error"):
            self.assertLess(differences[key], 2e-5)

    def test_independent_first_differences_converge_quadratically(self):
        a = model.independent_checks(self.prepared, self.point, self.first, step=2e-5)
        b = model.independent_checks(self.prepared, self.point, self.first, step=1e-5)
        for key in ("connection_first_difference_error", "constraint_first_difference_error", "probe_first_difference_error"):
            self.assertGreater(a[key]/b[key], 3.5)

    def test_taylor_fields_retain_nonzero_quadratic_off_shell_remainders(self):
        samples = self.report["independent_checks"]["samples_not_evolved_solutions"]
        for key in ("constraint_norm", "probe_norm"):
            self.assertGreater(samples[-1][key], 1e-5)
            for a, b in zip(samples, samples[1:]):
                self.assertGreater(a[key]/b[key], 3.8)
                self.assertLess(a[key]/b[key], 4.2)

    def test_cartan_source_is_retained_off_origin(self):
        for x in (np.zeros(4), np.array([.001, -.002, .001, .0005])):
            fields = model.taylor_fields(self.prepared, self.point, self.first, x)
            self.assertLess(np.linalg.norm(fields["Cartan"]), 1e-10)

    def test_unchanged_mass_selector_and_native_status_are_not_fitted(self):
        self.assertClose(model.prior.MASS, model.odd.background.triadic_mass())
        self.assertClose(model.Q, model.odd.Q_PHASE)
        self.assertFalse(self.report["main_TeX_changed"])
        self.assertTrue(self.report["not_first_coframe_Euler_or_second_constraint_completion"])

    def test_finite_taylor_fields_are_not_presented_as_full_solutions(self):
        self.assertIn("not a full propagation", self.report["status"])
        self.assertTrue(self.report["E2_lambda1_only_repair_first_completion"]["not_a_successful_repair"])


if __name__ == "__main__":
    unittest.main()
