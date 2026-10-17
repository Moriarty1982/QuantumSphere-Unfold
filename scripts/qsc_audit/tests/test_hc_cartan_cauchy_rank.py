"""Rank-changing temporal constraint branch and limits of finite-jet compatibility."""
import hashlib
import importlib.util
import json
from pathlib import Path
import unittest

import numpy as np


ROOT = Path(__file__).resolve().parents[3]
SPEC = importlib.util.spec_from_file_location("cartan_cauchy_rank", ROOT / "analysis/HC_Cartan_Cauchy_Rank.py")
model = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(model)


class HCCartanCauchyRankTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.prepared, cls.jets = model.load_data()
        cls.psi = cls.prepared["data"]["psi"]
        cls.multiplier = model.temporal_selector(0.1*model.DIRECTION)
        cls.regular = model.regular_point(cls.prepared, cls.multiplier)
        cls.zero_normal = model.normal_matrix(cls.prepared, cls.jets)
        cls.regular_normal = model.normal_matrix(cls.prepared, cls.jets, cls.multiplier)
        cls.report = model.evaluate()

    def assertClose(self, actual, expected, atol=2e-10, rtol=3e-8):
        np.testing.assert_allclose(actual, expected, atol=atol, rtol=rtol)

    def test_sigma_matrices_are_hermitian_and_obey_alpha_product_identity(self):
        self.assertClose(model.SIGMA, model.SIGMA.conj().swapaxes(-1, -2))
        for i, j, k in ((1, 2, 3), (2, 3, 1), (3, 1, 2)):
            self.assertClose(model.WEIGHTS[i] @ model.WEIGHTS[j], 1j*model.SIGMA[k-1])

    def test_wrong_spinor_shape_is_rejected(self):
        with self.assertRaises(ValueError):
            model.probe_constraint_block(np.eye(4), self.psi.T, self.multiplier)

    def test_complex_multiplier_column_is_rejected(self):
        with self.assertRaises(ValueError):
            model.temporal_selector(np.ones(4)*(1+1j))

    def test_nonpositive_probe_weight_is_not_inverted(self):
        with self.assertRaises(ValueError):
            model.probe_constraint_block(np.eye(4), self.psi, model.temporal_selector(np.array([3., 0, 0, 0])))

    def test_temporal_constraint_block_is_real_antisymmetric(self):
        block = model.probe_constraint_block(np.eye(4), self.psi, self.multiplier)["block"]
        self.assertClose(block, -block.T)

    def test_zero_multiplier_block_matches_exact_spin_cross_product_formula(self):
        block = model.probe_constraint_block(np.eye(4), self.psi, np.zeros((4, 4)))["block"]
        self.assertClose(block, model.zero_multiplier_formula(self.psi))

    def test_singular_branch_has_time_and_spin_aligned_null_vectors(self):
        block = model.zero_multiplier_formula(self.psi)
        spin = model.spin_vectors(self.psi)["weighted_second"]
        self.assertClose(block @ np.array([1., 0, 0, 0]), 0)
        self.assertClose(block @ np.concatenate(([0.], spin)), 0)
        self.assertEqual(np.linalg.matrix_rank(block), 2)

    def test_two_nonzero_singular_values_are_half_the_weighted_spin_norm(self):
        sv = np.linalg.svd(model.zero_multiplier_formula(self.psi), compute_uv=False)
        expected = np.linalg.norm(model.spin_vectors(self.psi)["weighted_second"])/2
        self.assertClose(sv[:2], expected)
        self.assertClose(sv[2:], 0)

    def test_zero_weighted_spin_is_a_more_singular_exception_not_rank_two(self):
        _, basis = np.linalg.eigh(model.Q)
        channels = np.zeros((3, 4), complex)
        channels[0, 0], channels[2, 1] = 1, 1
        psi = basis @ channels
        self.assertClose(model.zero_multiplier_formula(psi), 0)
        self.assertEqual(np.linalg.matrix_rank(model.normal_probe_matrix(psi, np.zeros((4, 4)))), 24)

    def test_positive_probe_form_does_not_remove_singular_constraint_block(self):
        result = model.probe_constraint_block(np.eye(4), self.psi, np.zeros((4, 4)))
        self.assertClose(result["weight_eigenvalues"], 1)
        self.assertClose(result["pfaffian"], 0)
        self.assertEqual(np.linalg.matrix_rank(model.normal_probe_matrix(self.psi, np.zeros((4, 4)))), 26)

    def test_exact_pfaffian_formula_matches_generic_positive_temporal_columns(self):
        rng = np.random.default_rng(7124)
        for ell in rng.normal(size=(8, 4))*0.1:
            actual = model.probe_constraint_block(np.eye(4), self.psi, model.temporal_selector(ell))["pfaffian"]
            self.assertClose(actual, model.pfaffian_formula(self.psi, ell))

    def test_constraint_determinant_is_pfaffian_squared(self):
        result = model.probe_constraint_block(np.eye(4), self.psi, self.multiplier)
        self.assertClose(np.linalg.det(result["block"]), result["pfaffian"]**2)

    def test_regular_block_has_rank_four_while_probe_form_stays_positive(self):
        result = model.probe_constraint_block(np.eye(4), self.psi, self.multiplier)
        self.assertEqual(np.linalg.matrix_rank(result["block"]), 4)
        self.assertGreater(result["weight_eigenvalues"][0], 0.96)
        self.assertGreater(result["singular_values"][-1], 0.03)

    def test_full_probe_temporal_block_rank_is_24_plus_schur_rank(self):
        for multiplier in (np.zeros((4, 4)), self.multiplier):
            t = model.probe_constraint_block(np.eye(4), self.psi, multiplier)["block"]
            self.assertEqual(np.linalg.matrix_rank(model.normal_probe_matrix(self.psi, multiplier)), 24+np.linalg.matrix_rank(t))

    def test_pure_temporal_scalar_multiplier_does_not_regularize_the_block(self):
        ell = np.array([0.1, 0, 0, 0])
        block = model.probe_constraint_block(np.eye(4), self.psi, model.temporal_selector(ell))
        self.assertClose(block["pfaffian"], 0)
        self.assertEqual(np.linalg.matrix_rank(block["block"]), 2)

    def test_parallel_channel_spin_polarizations_cannot_give_nonzero_pfaffian(self):
        _, basis = np.linalg.eigh(model.Q)
        channels = np.zeros((3, 4), complex)
        channels[0, 0], channels[2, 0] = 1, 2
        psi = basis @ channels
        result = model.probe_constraint_block(np.eye(4), psi, self.multiplier)
        self.assertClose(result["pfaffian"], 0)
        self.assertLessEqual(np.linalg.matrix_rank(result["block"]), 2)

    def test_spatial_multiplier_orthogonal_to_spin_triple_product_remains_singular(self):
        spin = model.spin_vectors(self.psi)
        ell = np.concatenate(([0.01], 0.01*spin["plus"]/np.linalg.norm(spin["plus"])))
        self.assertClose(model.pfaffian_formula(self.psi, ell), 0)
        result = model.probe_constraint_block(np.eye(4), self.psi, model.temporal_selector(ell))
        self.assertLess(np.linalg.svd(result["block"], compute_uv=False)[-1], 1e-12)

    def test_modal_scalar_phases_alone_do_not_change_this_rank_criterion(self):
        _, basis = np.linalg.eigh(model.Q)
        phases = basis @ np.diag(np.exp(1j*np.array([0.4, -0.1, 0.7]))) @ basis.conj().T
        original = model.probe_constraint_block(np.eye(4), self.psi, self.multiplier)
        rotated = model.probe_constraint_block(np.eye(4), phases @ self.psi, self.multiplier)
        self.assertClose(rotated["block"], original["block"])

    def test_inverse_constraint_norm_diverges_while_probe_weights_stay_near_one(self):
        samples = self.report["positive_weight_rank_change"]
        self.assertGreater(samples[1]["minimum_temporal_probe_eigenvalue"], 0.999)
        self.assertGreater(samples[1]["inverse_constraint_norm"], 20000)
        self.assertGreater(samples[1]["inverse_constraint_norm"]/samples[2]["inverse_constraint_norm"], 9.9)

    def test_full_temporal_normal_matrix_has_reported_ranks(self):
        self.assertEqual(self.zero_normal["matrix"].shape, (56, 56))
        self.assertEqual(self.zero_normal["rank"], 32)
        self.assertEqual(self.regular_normal["rank"], 34)

    def test_twelve_spatial_constitutive_rows_have_no_highest_normal_unknowns(self):
        rows = [4*a+i for a in range(4) for i in range(1, 4)]
        self.assertClose(self.regular_normal["matrix"][rows], 0)

    def test_coframe_normal_acceleration_block_has_rank_six_not_sixteen(self):
        self.assertEqual(np.linalg.matrix_rank(self.regular_normal["matrix"][:, :16], tol=1e-10), 6)

    def test_regular_normal_kernel_still_contains_spatial_multiplier_velocities(self):
        self.assertEqual(self.report["regular_normal_kernel_dimension"], 22)
        self.assertEqual(self.report["normal_kernel_spatial_multiplier_projection_rank"], 12)

    def test_normal_equation_map_is_affine_in_actual_highest_time_derivatives(self):
        x = np.random.default_rng(115).normal(size=56)*0.1
        expected = self.regular_normal["base"]+self.regular_normal["matrix"] @ x
        self.assertClose(self.regular_normal["evaluate"](x), expected)

    def test_zero_multiplier_normal_rhs_matches_the_prior_solved_point(self):
        self.assertLess(self.zero_normal["best_residual"], 1e-9)
        data = model.point_equations(self.prepared, self.prepared["data"]["first"], self.jets["e2"],
                                     np.zeros((4, 4)), self.jets["l1"])
        old = model.prolong.evaluate_jets(self.prepared, self.jets)
        self.assertClose(data["constraint"], old["constraint"])
        self.assertClose(data["probe"], old["probe"])
        self.assertClose(data["coframe"], old["coframe_Euler"])

    def test_singular_temporal_source_obeys_both_left_null_compatibility_conditions(self):
        data = self.prepared["data"]
        base = model.normal_probe_source(self.prepared, data["first"], self.jets["e2"], np.zeros((4, 4)), self.jets["l1"])
        time = 1j*model.prior.complexify(base[:24], (12,))
        p = self.psi.reshape(-1)
        f = base[24:]+np.array([np.vdot(p, a @ time).imag for a in model.A])
        w = model.spin_vectors(self.psi)["weighted_second"]
        self.assertClose(f[0], 0)
        self.assertClose(np.dot(w, f[1:]), 0)

    def test_regular_coefficient_control_is_not_mislabeled_as_initial_data(self):
        self.assertGreater(self.regular_normal["best_residual"], 1.)
        self.assertTrue(self.report["regular_control_is_off_shell_not_reprepared_initial_data"])

    def test_reprepared_regular_point_satisfies_every_original_euler_component(self):
        self.assertClose(self.regular["equations"]["vector"], 0)
        self.assertEqual(self.regular["matrix"].shape, (56, 320))
        self.assertEqual(self.regular["rank"], 50)

    def test_regular_point_has_positive_probe_weight_and_invertible_temporal_schur_block(self):
        result = model.probe_constraint_block(np.eye(4), self.psi, self.regular["multiplier"])
        self.assertGreater(result["weight_eigenvalues"][0], 0.96)
        self.assertGreater(abs(result["pfaffian"]), 0.04)

    def test_regular_probe_temporal_equations_uniquely_recover_the_prepared_velocities(self):
        p1, e2, l1 = (self.regular[k] for k in ("psi_first", "coframe_second", "multiplier_first"))
        base = model.normal_probe_source(self.prepared, p1, e2, self.multiplier, l1)
        matrix = model.normal_probe_matrix(self.psi, self.multiplier)
        solution = np.linalg.solve(matrix, -base)
        self.assertClose(solution[:24], model.prior.realify(p1[0]))
        self.assertClose(solution[24:], l1[0, :, 0])

    def test_regular_point_full_normal_rhs_is_compatible_but_not_unique(self):
        result = self.report["reprepared_regular_point"]
        self.assertEqual(result["full_normal_rank"], 34)
        self.assertLess(result["full_normal_best_residual"], 1e-9)

    def test_second_scalar_gate_is_symmetric_and_far_from_zero(self):
        value = model.scalar_second_gate(self.prepared, self.jets)
        self.assertClose(value, value.T)
        self.assertGreater(np.linalg.norm(value), 200.)
        self.assertLess(value[0, 0], -68.)

    def test_second_scalar_gate_is_checked_on_the_actual_previous_taylor_fields(self):
        self.assertLess(self.report["second_scalar_gate_independent_difference_error"], 0.001)

    def test_third_coframe_probe_jets_do_not_change_the_second_scalar_gate(self):
        changed = dict(self.jets)
        rng = np.random.default_rng(98)
        changed["e3"] = model.prolong.unpack_third(rng.normal(size=320))
        changed["p3"] = model.prolong.unpack_third(rng.normal(size=480), True)
        self.assertClose(model.scalar_second_gate(self.prepared, changed), model.scalar_second_gate(self.prepared, self.jets))

    def test_old_finite_order_claim_is_preserved_despite_new_extension_obstruction(self):
        result = model.prolong.evaluate_jets(self.prepared, self.jets)
        self.assertLess(np.linalg.norm(result["vector"]), 1e-8)
        self.assertGreater(np.linalg.norm(model.scalar_second_gate(self.prepared, self.jets)), 200.)

    def test_regular_saved_coordinates_reproduce_the_point_equations(self):
        saved = json.loads((ROOT / "analysis/HC_Cartan_Cauchy_Rank.json").read_text(encoding="utf-8"))
        vector = np.array(saved["reprepared_regular_point"]["point_coordinates"])
        p1 = model.prior.complexify(vector[:96], (4, 3, 4))
        e2, l1 = model.prior.unpack_second(vector[96:256]), vector[256:].reshape(4, 4, 4)
        result = model.point_equations(self.prepared, p1, e2, self.multiplier, l1)
        self.assertClose(result["vector"], 0)

    def test_source_fingerprint_preserves_the_previous_numerical_jet(self):
        value = hashlib.sha256((ROOT / "analysis/HC_Cartan_Prolongation.json").read_bytes()).hexdigest()
        self.assertEqual(self.report["previous_input_sha256"], value)

    def test_reprepared_point_has_not_been_promoted_to_surface_data(self):
        self.assertTrue(self.report["reprepared_regular_point"]["not_surface_data_or_first_constraint_prolongation"])
        self.assertFalse(self.report["main_TeX_changed"])
        self.assertIn("not a full Cauchy or native solution", self.report["status"])
        self.assertIn("propagation", " ".join(self.report["remaining"]))


if __name__ == "__main__":
    unittest.main()
