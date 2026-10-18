"""Sourced regular-branch gravity derivatives, identities and finite-jet limits."""
import hashlib
import importlib.util
import itertools
import json
from pathlib import Path
import unittest

import numpy as np


ROOT = Path(__file__).resolve().parents[3]
SPEC = importlib.util.spec_from_file_location("cartan_regular_gravity", ROOT / "analysis/HC_Cartan_Regular_Gravity.py")
model = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(model)


class HCCartanRegularGravityTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.prepared, cls.point, cls.previous = model.load_data()
        cls.solved = model.solve(cls.prepared, cls.point)
        cls.jets = cls.solved["jets"]
        cls.result = cls.solved["result"]
        cls.frozen = model.frozen_completion(cls.prepared, cls.point, cls.previous, cls.solved)
        cls.dependencies = model.noether_dependencies(cls.prepared, cls.point)
        cls.normal = model.spatial.normal_curl_system(cls.prepared, cls.point)
        cls.report = json.loads((ROOT / "analysis/HC_Cartan_Regular_Gravity.json").read_text(encoding="utf-8"))
        cls.differences = model.independent_checks(cls.prepared, cls.point, cls.jets)

    def assertClose(self, actual, expected, atol=3e-9, rtol=3e-8):
        np.testing.assert_allclose(actual, expected, atol=atol, rtol=rtol)

    def test_input_fingerprint_matches_spatial_completion(self):
        value = hashlib.sha256((ROOT / "analysis/HC_Cartan_Spatial_Propagation.json").read_bytes()).hexdigest()
        self.assertEqual(self.report["previous_input_sha256"], value)

    def test_previous_first_constraint_and_probe_completion_is_retained_as_control(self):
        r = model.equations(self.prepared, self.point, self.previous)
        self.assertLess(np.linalg.norm(r["constraint_first"]), 1e-9)
        self.assertLess(np.linalg.norm(r["probe_first"]), 1e-9)

    def test_previous_first_gravitational_derivative_is_not_already_zero(self):
        r = model.equations(self.prepared, self.point, self.previous)
        self.assertGreater(np.linalg.norm(r["coframe_Euler_first"]), 3000)

    def test_original_point_equations_still_hold(self):
        p = self.point
        r = model.spatial.rank_model.point_equations(self.prepared, p["psi_first"], p["coframe_second"], p["multiplier"], p["multiplier_first"])
        self.assertLess(np.linalg.norm(r["vector"]), 1e-9)

    def test_wrong_higher_coordinate_count_is_rejected(self):
        with self.assertRaises(ValueError):
            model.unpack(np.zeros(1199))

    def test_precomputed_lc_linear_map_matches_direct_formula(self):
        value = np.random.default_rng(911).normal(size=(4, 4, 4))
        self.assertClose(value.reshape(-1) @ model.LC_LINEAR, model.prolong.normal_lorentz(value).reshape(-1))

    def test_connection_second_derivative_is_symmetric(self):
        c = self.result["connection"]
        for key in ("second", "response_second", "source_second", "hessian_second"):
            self.assertClose(c[key], c[key].swapaxes(0, 1))

    def test_second_cartan_equation_keeps_its_full_rhs(self):
        c = self.result["connection"]
        self.assertClose(c["k_second"] @ self.prepared["hessian"].T, c["rhs"])

    def test_nonzero_multiplier_value_reaction_cannot_be_omitted(self):
        self.assertGreater(np.linalg.norm(self.result["connection"]["lambda_value_reaction"]), 40)
        omitted = self.result["connection"]["lambda_value_reaction"] @ self.prepared["inverse_hessian"].T
        self.assertGreater(np.linalg.norm(omitted), 10)

    def test_cartan_response_hessian_agrees_with_independent_field_difference(self):
        step = 2e-5
        plus, minus = (model.taylor_fields(self.prepared, self.point, self.jets, sign*step*np.eye(4)[0]) for sign in (1, -1))
        psi = self.prepared["data"]["psi"]
        l0 = model.prolong.fast_cartan_data(self.prepared, np.eye(4), psi)[1]
        lp, lm = (model.prolong.fast_cartan_data(self.prepared, f["coframe"], f["psi"])[1] for f in (plus, minus))
        difference = (lp-2*l0+lm)/step**2
        self.assertClose(difference, self.result["connection"]["response_second"][0, 0].reshape(16, 24), atol=5e-4)

    def test_cartan_eh_hessian_second_derivative_agrees_with_field_difference(self):
        step = 2e-5
        fields = [model.taylor_fields(self.prepared, self.point, self.jets, sign*step*np.eye(4)[0]) for sign in (1, -1)]
        hp, hm = (model.prolong.fast_cartan_data(self.prepared, f["coframe"], f["psi"])[0] for f in fields)
        difference = (hp-2*self.prepared["hessian"]+hm)/step**2
        self.assertClose(difference, self.result["connection"]["hessian_second"][0, 0], atol=1e-4)

    def test_connection_second_difference_checks_source_and_lc_reactions(self):
        self.assertLess(self.differences["connection_second_fd_error"], 5e-4)

    def test_second_constraint_matches_independent_field_difference(self):
        self.assertLess(self.differences["constraint_second_fd_error"], 1e-3)

    def test_gravity_first_derivative_matches_independent_parent_variation(self):
        self.assertLess(self.differences["coframe_Euler_first_fd_error"], 5e-4)

    def test_all_fifty_two_derived_row_identities_are_independent(self):
        self.assertEqual(self.dependencies.shape, (52, 384))
        self.assertEqual(np.linalg.matrix_rank(self.dependencies, tol=1e-9), 52)

    def test_noether_and_curl_identities_hold_away_from_the_fitted_higher_jet(self):
        jets = model.unpack(np.random.default_rng(912).normal(size=1200)*.1)
        value = model.equations(self.prepared, self.point, jets)["vector"]
        self.assertLess(np.linalg.norm(self.dependencies @ value), 1e-8)

    def test_derived_identities_annihilate_the_equation_coefficient_matrix(self):
        self.assertLess(np.linalg.norm(self.dependencies @ self.solved["matrix"]), 1e-7)

    def test_affine_rhs_satisfies_all_derived_compatibility_relations(self):
        self.assertLess(np.linalg.norm(self.dependencies @ self.solved["base"]), 1e-8)

    def test_observed_rank_exhausts_the_derived_compatibility_bound(self):
        self.assertEqual(self.solved["matrix"].shape, (384, 1200))
        self.assertEqual(self.solved["rank"], 384-52)

    def test_full_higher_equation_map_is_affine(self):
        x = np.random.default_rng(913).normal(size=1200)*.1
        value = model.equations(self.prepared, self.point, model.unpack(x))["vector"]
        self.assertClose(value, self.solved["base"]+self.solved["matrix"] @ x, atol=2e-8)

    def test_first_equations_agree_with_prior_regular_branch_helpers(self):
        c1 = model.spatial.constraint_first(self.prepared, self.point, self.jets["p2"])
        r1 = model.spatial.first_probe(self.prepared, self.point, self.jets["p2"], self.jets["l2"])
        self.assertClose(self.result["constraint_first"], c1)
        self.assertClose(self.result["probe_first"], r1)

    def test_frozen_second_jet_higher_repair_is_a_failed_control(self):
        self.assertEqual(self.frozen["matrix"].shape, (384, 800))
        self.assertEqual(self.frozen["rank"], 140)
        self.assertGreater(np.linalg.norm(self.frozen["residual"]), 6000)

    def test_frozen_higher_map_matches_direct_equations(self):
        x = np.random.default_rng(914).normal(size=800)*.1
        jets = dict(self.previous, e3=model.prolong.unpack_third(x[:320]), p3=model.prolong.unpack_third(x[320:], True))
        actual = model.equations(self.prepared, self.point, jets)["vector"]
        self.assertClose(actual, self.frozen["base"]+self.frozen["matrix"] @ x, atol=2e-8)

    def test_frozen_control_does_not_silently_change_second_jets(self):
        self.assertClose(self.frozen["jets"]["p2"], self.previous["p2"])
        self.assertClose(self.frozen["jets"]["l2"], self.previous["l2"])

    def test_all_384_unprojected_equations_are_satisfied(self):
        self.assertLess(np.linalg.norm(self.result["vector"]), 1e-8)

    def test_all_first_gravitational_components_are_satisfied(self):
        self.assertLess(np.linalg.norm(self.result["coframe_Euler_first"]), 1e-8)

    def test_all_second_coframe_constraints_are_satisfied(self):
        self.assertLess(np.linalg.norm(self.result["constraint_second"]), 1e-8)

    def test_new_second_and_third_jets_are_holonomic(self):
        for key in ("p2", "l2"):
            self.assertClose(self.jets[key], self.jets[key].swapaxes(0, 1))
        for key in ("e3", "p3"):
            for permutation in itertools.permutations(range(3)):
                self.assertClose(self.jets[key], self.jets[key].transpose((*permutation, 3, 4)))

    def test_mass_selector_and_temporal_block_are_unchanged(self):
        self.assertClose(model.MASS, model.odd.background.triadic_mass())
        block = model.spatial.rank_model.probe_constraint_block(np.eye(4), self.prepared["data"]["psi"], self.point["multiplier"])
        self.assertGreater(block["weight_eigenvalues"][0], .96)
        self.assertGreater(block["singular_values"][-1], .03)

    def test_ten_leading_normal_gauge_directions_are_independent(self):
        gauge = model.coframe_normal_gauge_basis()
        self.assertEqual(gauge.shape, (56, 10))
        self.assertEqual(np.linalg.matrix_rank(gauge), 10)
        self.assertClose(gauge[16:], 0)

    def test_lorentz_generators_preserve_eta_to_first_order(self):
        for generator in model.coframe_normal_gauge_basis()[:16, 4:].T.reshape(6, 4, 4):
            self.assertClose(generator.T @ model.ETA+model.ETA @ generator, 0)

    def test_leading_coordinate_gauge_directions_have_only_temporal_columns(self):
        gauge = model.coframe_normal_gauge_basis()[:16, :4].T.reshape(4, 4, 4)
        self.assertClose(gauge[:, :, 1:], 0)
        self.assertClose(gauge[:, :, 0], np.eye(4))

    def test_appended_normal_system_annihilates_ten_leading_gauge_directions(self):
        self.assertClose(self.normal["matrix"] @ model.coframe_normal_gauge_basis(), 0)

    def test_six_normal_directions_remain_after_the_ten_leading_gauge_directions(self):
        kernel = self.normal["remaining_kernel"]
        gauge = model.coframe_normal_gauge_basis()
        self.assertEqual(kernel.shape[1]-np.linalg.matrix_rank(gauge), 6)
        self.assertClose(gauge-kernel @ kernel.T @ gauge, 0)
        self.assertEqual(self.normal["remaining_spatial_multiplier_rank"], 6)

    def test_cross_and_independent_coframe_curvature_match_at_the_point(self):
        self.assertLess(self.differences["analytic_cross_E_curvature_match_error"], 1e-8)

    def test_cross_curvature_match_has_an_independent_difference_control(self):
        self.assertLess(self.differences["difference_cross_E_curvature_match_error"], 2e-3)

    def test_constraint_remainders_are_cubic_not_zero(self):
        samples = self.differences["samples_not_evolved_solutions"]
        self.assertGreater(samples[-1]["constraint_norm"], 1e-7)
        for a, b in zip(samples, samples[1:]):
            self.assertGreater(a["constraint_norm"]/b["constraint_norm"], 7.7)
            self.assertLess(a["constraint_norm"]/b["constraint_norm"], 8.3)

    def test_probe_and_gravity_remainders_are_quadratic_not_zero(self):
        samples = self.differences["samples_not_evolved_solutions"]
        for key in ("probe_norm", "coframe_Euler_norm"):
            self.assertGreater(samples[-1][key], 1e-5)
            for a, b in zip(samples, samples[1:]):
                self.assertGreater(a[key]/b[key], 3.8)
                self.assertLess(a[key]/b[key], 4.2)

    def test_full_cartan_equation_remains_sourced_off_origin(self):
        for point in (np.zeros(4), np.array([.001, -.002, .001, -.0005])):
            fields = model.taylor_fields(self.prepared, self.point, self.jets, point)
            self.assertLess(np.linalg.norm(fields["Cartan"]), 1e-10)

    def test_saved_higher_coordinates_reproduce_all_equations(self):
        jets = model.unpack(np.array(self.report["joint_completion"]["jet_coordinates"]))
        self.assertLess(np.linalg.norm(model.equations(self.prepared, self.point, jets)["vector"]), 1e-8)

    def test_native_and_full_evolution_claims_are_not_made(self):
        self.assertFalse(self.report["main_TeX_changed"])
        self.assertIn("no full evolution or native", self.report["status"])

    def test_zero_multiplier_limit_reproduces_prior_cartan_connection_jets(self):
        prepared, old = model.spatial.rank_model.load_data()
        point = {"multiplier": np.zeros((4, 4)), "psi_first": prepared["data"]["first"],
                 "coframe_second": old["e2"], "multiplier_first": old["l1"]}
        result = model.connection_second(prepared, point, old)
        first, second = model.prolong.connection_jets(prepared, old)
        self.assertClose(result["first"], first)
        self.assertClose(result["second"], second)


if __name__ == "__main__":
    unittest.main()
