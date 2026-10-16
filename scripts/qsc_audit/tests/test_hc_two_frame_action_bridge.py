"""Two-frame identities and the explicitly changed neutral parent's local equations."""
import importlib.util
import json
from pathlib import Path
import unittest

import numpy as np


ROOT = Path(__file__).resolve().parents[3]
SPEC = importlib.util.spec_from_file_location("two_frame", ROOT / "analysis/HC_Two_Frame_Action_Bridge.py")
bridge = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(bridge)


class HCTwoFrameActionBridgeTests(unittest.TestCase):
    def setUp(self):
        self.rng = np.random.default_rng(305)
        self.weights, self.beta = bridge.geometry.spin_weights()
        self.gamma = self.beta @ self.weights

    def assertClose(self, actual, expected, atol=4e-12):
        np.testing.assert_allclose(actual, expected, atol=atol, rtol=2e-9)

    def jet(self):
        psi = self.rng.normal(size=(3, 4))+1j*self.rng.normal(size=(3, 4))
        d = self.rng.normal(size=(4, 3, 4))+1j*self.rng.normal(size=(4, 3, 4))
        return psi, d, 0.6*psi

    def test_identity_reference_has_trace_four_and_zero_distance(self):
        result = bridge.relative_frame(np.eye(4), np.eye(4))
        self.assertEqual(result["trace"], 4)
        self.assertEqual(result["distance_frobenius"], 0)

    def test_trace_bounds_hold_for_general_real_frames(self):
        for _ in range(10):
            result = bridge.relative_frame(self.rng.normal(size=(4, 4)), np.eye(4))
            self.assertGreaterEqual(result["distance_frobenius"]+1e-12, result["trace_bound_frobenius"])
            self.assertGreaterEqual(result["distance_operator"]+1e-12, result["trace_bound_operator"])

    def test_sharp_bounds_are_approached_by_invertible_traceless_frames(self):
        result = bridge.relative_frame(1e-6*np.diag([1, 1, -1, -1]), np.eye(4))
        self.assertEqual(result["trace"], 0)
        self.assertAlmostEqual(result["distance_frobenius"], 2, places=10)
        self.assertAlmostEqual(result["distance_operator"], 1.000001, places=12)

    def test_pure_lorentz_negative_control_has_same_metric_but_zero_trace(self):
        relative = np.diag([1, 1, -1, -1])
        self.assertEqual(np.linalg.det(relative), 1)
        self.assertClose(relative.T @ bridge.geometry.ETA @ relative, bridge.geometry.ETA)
        self.assertEqual(bridge.relative_frame(relative, np.eye(4))["trace"], 0)

    def test_relative_trace_is_invariant_under_a_common_coordinate_change(self):
        e, theta = self.rng.normal(size=(4, 4)), np.eye(4)+0.1*self.rng.normal(size=(4, 4))
        chart = np.eye(4)+0.1*self.rng.normal(size=(4, 4))
        first, second = bridge.relative_frame(e, theta), bridge.relative_frame(e @ chart, theta @ chart)
        self.assertClose(first["relative"], second["relative"])

    def test_pure_coframe_conformality_cannot_have_zero_trace_unless_degenerate(self):
        theta = np.eye(4)+0.1*self.rng.normal(size=(4, 4))
        for c in [0.1, 1, 2, -1]:
            self.assertClose(bridge.relative_frame(c*theta, theta)["trace"], 4*c)

    def test_off_shell_reference_identity_including_nonreal_mass_image(self):
        psi, d, image = self.jet()
        theta = np.eye(4)+0.1*self.rng.normal(size=(4, 4))
        for scale in [0.5, 1, -2]:
            result = bridge.mixed_probe_trace(psi, d, self.gamma, self.beta, image+0.2j*psi,
                                               reference=theta, scale=scale)
            self.assertClose(result["scalar_residual"].imag, result["imaginary_residual_prediction"])

    def test_reference_on_shell_first_jet_has_zero_trace(self):
        for seed in [53, 54, 55]:
            result = bridge._on_shell_jet(seed)
            self.assertClose(result["residual"], np.zeros((3, 4)))
            self.assertClose(result["trace"], 0)

    def test_reference_on_shell_first_jet_can_have_a_full_rank_coframe(self):
        result = bridge._on_shell_jet()
        self.assertEqual(np.linalg.matrix_rank(result["coframe"]), 4)
        self.assertGreaterEqual(result["distance_frobenius"], 2-1e-12)
        self.assertGreaterEqual(result["distance_operator"], 1-1e-12)

    def test_affine_background_changes_the_trace_identity_by_its_actual_trace(self):
        psi, d, image = self.jet()
        theta = np.eye(4)+0.05*self.rng.normal(size=(4, 4))
        result = bridge.mixed_probe_trace(psi, d, self.gamma, self.beta, image,
                                           reference=theta, background=theta)
        self.assertClose(result["background_trace"], 4)
        self.assertClose(result["scalar_residual"].imag, result["trace"]-4)

    def test_same_induced_frame_affine_identity_has_a_background_contraction(self):
        psi, d, image = self.jet()
        first = bridge.mixed_probe_trace(psi, d, self.gamma, self.beta, image, background=np.eye(4))
        result = bridge.mixed_probe_trace(psi, d, self.gamma, self.beta, image,
                                           reference=first["coframe"], background=np.eye(4))
        self.assertClose(result["trace"], 4)
        self.assertClose(result["scalar_residual"].imag, 4-result["background_trace"])

    def test_multiplier_probe_weight_is_hermitian(self):
        lam = self.rng.normal(size=(4, 4))
        derivative = self.rng.normal(size=(4, 4, 4))
        weight = bridge.multiplier_probe_weight(lam, derivative, self.weights, 0.7, 0.4)
        self.assertClose(weight, weight.conj().T)

    def test_multiplier_probe_variation_matches_an_independent_periodic_action(self):
        count, step, coupling = 64, 1e-6, 0.4
        x = np.arange(count)*2*np.pi/count
        base = self.rng.normal(size=4)+1j*self.rng.normal(size=4)
        mode = self.rng.normal(size=4)+1j*self.rng.normal(size=4)
        psi = base+np.exp(1j*x[:, None])*mode
        variation = np.cos(2*x[:, None])*base+1j*np.sin(x[:, None])*mode
        lam0, lam1 = self.rng.normal(size=(4, 4)), self.rng.normal(size=(4, 4))
        lam = np.sin(x[:, None, None])*lam0+np.cos(2*x[:, None, None])*lam1
        derivative = np.zeros((count, 4, 4, 4))
        derivative[:, 1] = np.cos(x[:, None, None])*lam0-2*np.sin(2*x[:, None, None])*lam1
        h = 0.7+0.1*np.cos(x)

        def action(state):
            frequencies = np.fft.fftfreq(count, d=1/count)
            ds = np.fft.ifft(1j*frequencies[:, None]*np.fft.fft(state, axis=0), axis=0)
            current = np.einsum("ni,aij,nj->na", state.conj(), self.weights, state).real
            c = coupling*h[:, None, None]*np.einsum("na,m->nam", current, bridge.geometry.N_COV)
            c[:, :, 1] += np.einsum("ni,aij,nj->na", state.conj(), self.weights, ds).real
            return -float(np.einsum("nam,nam->", lam, c))*2*np.pi/count

        numerical = (action(psi+step*variation)-action(psi-step*variation))/(2*step)
        weighted = np.array([bridge.multiplier_probe_weight(a, da, self.weights, amplitude, coupling)
                             for a, da, amplitude in zip(lam, derivative, h)])
        analytic = 2*np.einsum("ni,nij,nj->", variation.conj(), weighted, psi).real*2*np.pi/count
        self.assertClose(numerical, analytic, atol=2e-7)

    def test_local_common_phase_does_not_change_the_real_dictionary(self):
        psi, d, image = self.jet()
        first = bridge.mixed_probe_trace(psi, d, self.gamma, self.beta, image)
        phase, gradient = np.exp(0.3j), self.rng.normal(size=4)
        second = bridge.mixed_probe_trace(phase*psi, phase*(d+1j*gradient[:, None, None]*psi),
                                           self.gamma, self.beta, phase*image)
        self.assertClose(second["coframe"], first["coframe"])

    def test_multiplier_elimination_equals_the_composite_chain_rule(self):
        q = np.array([0.2, -0.4])
        c = np.array([q[0]**2, q[0]*q[1]])
        jacobian = np.array([[2*q[0], 0], [q[1], q[0]]])
        target, background = np.array([0.3, 0.8]), np.array([1.0, -0.1])
        pi = background+c-target
        lam = -pi
        parent = q-jacobian.T @ lam

        def composite(v):
            e = background+[v[0]**2, v[0]*v[1]]
            return (v @ v+(e-target) @ (e-target))/2

        delta = 1e-6*np.eye(2)
        numerical = [(composite(q+d)-composite(q-d))/(2e-6) for d in delta]
        self.assertClose(parent, numerical, atol=2e-10)

    def test_composite_stationarity_does_not_require_zero_metric_euler_tensor(self):
        jacobian, pi = np.array([[1.0], [0.0]]), np.array([0.0, -1.0])
        self.assertClose(jacobian.T @ pi, [0])
        self.assertGreater(np.linalg.norm(pi), 0)
        self.assertClose(pi+(-pi), [0, 0])

    def test_zero_multiplier_does_not_add_an_uncomputed_probe_force(self):
        self.assertClose(bridge.multiplier_probe_weight(np.zeros((4, 4)), np.zeros((4, 4, 4)),
                                                        self.weights, 1.7, 0.4), np.zeros((4, 4)))

    def test_affine_branch_solves_the_full_coframe_constraint(self):
        branch = bridge.affine_neutral_branch()
        self.assertClose(branch["coframe_constraint_residual"], np.zeros((4, 4)))
        self.assertEqual(branch["relative_trace"], branch["background_trace"])

    def test_affine_branch_has_a_constant_massless_on_shell_reference_probe(self):
        branch = bridge.affine_neutral_branch()
        self.assertClose(branch["reference_probe_residual"], np.zeros((1, 4)))
        self.assertClose(branch["ordered_HC_transport_image_norm"], 0)

    def test_affine_branch_solves_all_independent_metric_components(self):
        branch = bridge.affine_neutral_branch()
        self.assertClose(branch["Einstein_residual"], np.zeros((4, 4)))
        self.assertClose(branch["coframe_EL_at_zero_multiplier"], np.zeros((4, 4)))

    def test_affine_branch_solves_the_curved_scalar_hc_equation(self):
        branch = bridge.affine_neutral_branch()
        self.assertClose(branch["scalar_EL"], 0)
        self.assertClose(branch["scalar_flux"], np.zeros(4))

    def test_reference_and_induced_currents_are_conserved_in_this_changed_branch(self):
        branch = bridge.affine_neutral_branch()
        self.assertClose(branch["reference_phase_current"], bridge.geometry.L_VECTOR)
        self.assertClose(branch["reference_phase_current_divergence"], 0)
        self.assertClose(branch["induced_current_divergence"], 0)

    def test_null_metric_is_curved_not_just_an_invertible_flat_coframe(self):
        branch = bridge.affine_neutral_branch()
        self.assertGreater(np.linalg.norm(branch["geometry"]["lower_riemann"]), 1e-4)
        self.assertClose(branch["geometry"]["scalar"], 0)

    def test_affine_branch_preserves_determinant_signature_and_null_axis(self):
        branch = bridge.affine_neutral_branch()
        self.assertClose(np.linalg.det(branch["coframe"]), 1)
        self.assertClose(np.linalg.det(branch["metric"]), -1)
        self.assertEqual(np.sum(np.linalg.eigvalsh(branch["metric"]) < 0), 1)
        self.assertClose(bridge.geometry.N_COV @ np.linalg.solve(branch["metric"], bridge.geometry.N_COV), 0)

    def test_neutral_solution_is_a_local_family_not_a_single_fitted_point(self):
        for xy, slope in [([0.2, 0.3], [0.1, 0]), ([-0.3, 0.4], [0.1, 0.07]),
                          ([1, -0.7], [-0.15, 0.1])]:
            branch = bridge.affine_neutral_branch(xy, slope=slope)
            self.assertClose(branch["Einstein_residual"], np.zeros((4, 4)))
            self.assertClose(branch["scalar_EL"], 0)
            self.assertClose(branch["reference_probe_residual"], np.zeros((1, 4)))

    def test_removing_added_background_makes_the_same_constant_probe_coframe_degenerate(self):
        original = bridge.affine_neutral_branch()["coframe"]-np.eye(4)
        self.assertEqual(np.linalg.matrix_rank(original), 1)

    def test_real_mass_and_yukawa_terms_restore_a_nonzero_probe_residual(self):
        branch = bridge.affine_neutral_branch()
        self.assertGreater(branch["native_mass_Yukawa_restoration_residual_norm"], 0.9)

    def test_restoring_a_charged_gauge_probe_does_not_solve_its_gauss_source(self):
        self.assertClose(bridge.affine_neutral_branch()["charged_zero_gauge_Gauss_source_norm"], 1)

    def test_nonzero_h_does_not_satisfy_the_zero_target_matching_penalty_equation(self):
        branch = bridge.affine_neutral_branch()
        self.assertClose(branch["zero_target_penalty_restoration_EL"], -branch["profile"]["amplitude"])
        self.assertGreater(abs(branch["zero_target_penalty_restoration_EL"]), 1)

    def test_curved_scalar_formula_reduces_to_the_flat_rank_one_principal_tensor(self):
        gradient = self.rng.normal(size=4)
        raw = self.rng.normal(size=(4, 4))
        hessian = (raw+raw.T)/2
        result = bridge.scalar_curvature_el(bridge.geometry.ETA, np.zeros((4, 4, 4)), gradient, hessian, 0.4)
        expected = bridge.checks.scalar_el(hessian, bridge.geometry.N_COV, [[1]], 0.4)
        self.assertClose(result["EL"], expected)

    def test_report_and_saved_calculation_keep_the_native_scope_boundary(self):
        report = bridge.evaluate()
        saved = json.loads((ROOT / "analysis/HC_Two_Frame_Action_Bridge.json").read_text(encoding="utf-8"))
        self.assertEqual(saved, report)
        self.assertFalse(report["main_TeX_changed"])
        self.assertIn("MODIFIED", report["status"])
        self.assertTrue(report["restoring_native_terms_is_not_free"]["nonzero_h_is_not_exact_minimal_HC_zero_closure"])
        self.assertTrue(report["two_frames_without_changing_the_coframe"]["not_a_Lorentz_invariant_metric_distance"])

    def test_bad_shapes_singular_references_and_invalid_profile_domains_are_rejected(self):
        with self.assertRaises(ValueError):
            bridge.relative_frame(np.eye(4), np.zeros((4, 4)))
        with self.assertRaises(ValueError):
            bridge.affine_neutral_branch(coupling=0)
        with self.assertRaises(ValueError):
            bridge.affine_neutral_branch(einstein_coupling=-1)
        with self.assertRaises(ValueError):
            bridge.affine_neutral_branch(intercept=-1)
        psi, d, image = self.jet()
        with self.assertRaises(ValueError):
            bridge.mixed_probe_trace(psi, d, self.gamma, self.beta, image, scale=0)


if __name__ == "__main__":
    unittest.main()
