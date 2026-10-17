"""Candidate odd cross readout: analytic curvature jets and complete probe variation."""
import importlib.util
import json
from pathlib import Path
import unittest

import numpy as np


ROOT = Path(__file__).resolve().parents[3]
SPEC = importlib.util.spec_from_file_location(
    "antisymmetric_cross_geometry", ROOT / "analysis/HC_Antisymmetric_Cross_Geometry.py")
model = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(model)


class HCAntisymmetricCrossGeometryTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.geometry = model.reference_geometry()
        cls.data = cls.geometry["data"]
        cls.report = model.evaluate()

    def assertClose(self, actual, expected, atol=2e-10, rtol=3e-8):
        np.testing.assert_allclose(actual, expected, atol=atol, rtol=rtol)

    def random_jet(self, seed=171):
        rng = np.random.default_rng(seed)
        return (rng.normal(size=(3, 4))+1j*rng.normal(size=(3, 4)),
                rng.normal(size=(4, 3, 4))+1j*rng.normal(size=(4, 3, 4)))

    def direct_frame(self, point):
        data = model.background.polynomial_background(point)
        return (data["cross_ART_QFT"]-data["cross_QFT_ART"])/2

    def test_source_contains_both_cross_directions_but_not_this_adoption(self):
        source = (ROOT / self.report["source"]["path"]).read_text(encoding="utf-8")
        self.assertIn("Cross-bilinear geometry channel", source)
        self.assertIn("similarly with probes exchanged", source)
        self.assertIn("expression is heuristic", source)
        self.assertIn("additional", self.report["source"]["new_choice"])

    def test_odd_selector_is_antihermitian_and_phase_weight_hermitian(self):
        self.assertClose(model.R_MINUS.conj().T, -model.R_MINUS)
        self.assertClose(model.Q_PHASE.conj().T, model.Q_PHASE)
        self.assertClose(np.linalg.eigvalsh(model.Q_PHASE), [-0.5, 0, 0.5])

    def test_exchange_even_and_odd_are_formed_from_original_directed_readouts(self):
        psi, derivative = self.random_jet()
        channels = model.channels(psi, derivative)
        self.assertClose(channels["odd"], (channels["directed"]-channels["reverse"])/2)
        self.assertClose(channels["even"], (channels["directed"]+channels["reverse"])/2)

    def test_even_readout_is_half_gradient_of_cross_current_in_flat_reference(self):
        point, step = model.POINT, 1e-5
        h = (model.SELECTOR+model.SELECTOR.conj().T)/2

        def current(p):
            psi = model.background.polynomial_background(p)["psi"]
            return np.array([np.vdot(psi, h @ psi @ k.T).real for k in model.WEIGHTS])

        first = np.column_stack([(current(point+step*e)-current(point-step*e))/(2*step) for e in np.eye(4)])
        channels = model.channels(self.data["psi"], self.data["first"])
        self.assertClose(channels["even"], first/2)

    def test_odd_readout_is_not_closed_as_a_gradient(self):
        first = self.geometry["first"]
        self.assertGreater(np.linalg.norm(first-first.transpose(2, 1, 0)), 1)

    def test_common_local_phase_changes_odd_readout_by_derived_charge(self):
        psi, derivative = self.random_jet()
        alpha, gradient = np.exp(0.31j), np.array([0.2, -0.4, 0.3, 0.1])
        before = model.channels(psi, derivative)
        after = model.channels(alpha*psi, alpha*(derivative+1j*gradient[:, None, None]*psi))
        self.assertClose(after["odd"]-before["odd"], np.outer(before["phase_charge"], gradient))

    def test_common_local_phase_does_not_change_even_readout(self):
        psi, derivative = self.random_jet()
        gradient = np.array([0.2, -0.4, 0.3, 0.1])
        before = model.channels(psi, derivative)
        after = model.channels(psi, derivative+1j*gradient[:, None, None]*psi)
        self.assertClose(after["even"], before["even"])

    def test_simultaneous_common_gauge_connection_change_restores_odd_covariance(self):
        psi, derivative = self.random_jet()
        gradient = np.array([0.2, -0.4, 0.3, 0.1])
        phase = np.exp(0.31j)
        transformed_covariant = phase*(derivative+1j*gradient[:, None, None]*psi)-1j*gradient[:, None, None]*(phase*psi)
        self.assertClose(model.channels(phase*psi, transformed_covariant)["odd"], model.channels(psi, derivative)["odd"])

    def test_covariantly_transported_internal_selector_preserves_cross_metric(self):
        psi, derivative = self.random_jet()
        rng = np.random.default_rng(913)
        unitary, _ = np.linalg.qr(rng.normal(size=(3, 3))+1j*rng.normal(size=(3, 3)))
        before = model.channels(psi, derivative)["odd"]
        selector = unitary @ model.SELECTOR @ unitary.conj().T
        after = model.channels(unitary @ psi, unitary @ derivative, selector)["odd"]
        self.assertClose(after, before)
        self.assertClose(after.T @ model.ETA @ after, before.T @ model.ETA @ before)

    def test_fixed_bare_selector_need_not_preserve_cross_metric(self):
        psi, derivative = self.random_jet()
        unitary = np.diag(np.exp(1j*np.array([0.2, -0.4, 0.1])))
        before = model.channels(psi, derivative)["odd"]
        after = model.channels(unitary @ psi, unitary @ derivative)["odd"]
        self.assertGreater(np.linalg.norm(after.T @ model.ETA @ after-before.T @ model.ETA @ before), 1)

    def test_reference_example_is_actual_prepared_Dirac_solution(self):
        self.assertLess(np.linalg.norm(self.data["reference_residual"]), 3e-14)
        direct = model.dirac.dirac_data(self.data["psi"], self.data["first"], self.data["mass"])
        self.assertLess(np.linalg.norm(direct["residual"]), 3e-14)

    def test_probe_second_jets_match_independent_differences_of_exact_solution(self):
        step = 2e-6
        for r, axis in enumerate(np.eye(4)):
            plus = model.background.polynomial_background(model.POINT+step*axis)["derivatives"]
            minus = model.background.polynomial_background(model.POINT-step*axis)["derivatives"]
            self.assertClose(self.data["second"][r], (plus-minus)/(2*step), atol=3e-9)

    def test_probe_third_jets_match_differences_of_second_jets(self):
        step = 2e-6
        for r, axis in enumerate(np.eye(4)):
            plus = model.affine_probe_jet(model.POINT+step*axis)["second"]
            minus = model.affine_probe_jet(model.POINT-step*axis)["second"]
            self.assertClose(self.data["third"][r], (plus-minus)/(2*step), atol=3e-8)

    def test_cross_coframe_first_jets_match_direct_readout_differences(self):
        step = 2e-6
        for r, axis in enumerate(np.eye(4)):
            numerical = (self.direct_frame(model.POINT+step*axis)-self.direct_frame(model.POINT-step*axis))/(2*step)
            self.assertClose(self.geometry["first"][r], numerical, atol=2e-9)

    def test_cross_coframe_second_jets_match_first_jet_differences(self):
        step = 2e-6
        for r, axis in enumerate(np.eye(4)):
            plus = model.odd_coframe_jet(model.affine_probe_jet(model.POINT+step*axis))[1]
            minus = model.odd_coframe_jet(model.affine_probe_jet(model.POINT-step*axis))[1]
            self.assertClose(self.geometry["second"][r], (plus-minus)/(2*step), atol=3e-8)

    def test_reference_odd_coframe_is_rank_four_with_recorded_orientation(self):
        self.assertEqual(np.linalg.matrix_rank(self.geometry["frame"]), 4)
        self.assertLess(np.linalg.det(self.geometry["frame"]), 0)
        self.assertGreater(np.linalg.svd(self.geometry["frame"], compute_uv=False)[-1], 0.008)

    def test_candidate_metric_has_lorentz_signature(self):
        eigenvalues = np.linalg.eigvalsh(self.geometry["bundle"]["metric"])
        self.assertEqual(sum(eigenvalues < 0), 1)
        self.assertEqual(sum(eigenvalues > 0), 3)

    def test_candidate_Riemann_is_nonzero_not_a_gradient_coordinate_rewrite(self):
        self.assertGreater(np.linalg.norm(self.geometry["bundle"]["curvature"]["riemann"]), 100)
        self.assertGreater(abs(self.geometry["bundle"]["curvature"]["scalar"]), 1e5)

    def test_independent_metric_finite_differences_confirm_curvature(self):
        point, step = model.POINT, 2e-5

        def metric(p):
            frame = self.direct_frame(p)
            return frame.T @ model.ETA @ frame

        value = metric(point)
        first = np.array([(metric(point+step*e)-metric(point-step*e))/(2*step) for e in np.eye(4)])
        second = np.empty((4, 4, 4, 4))
        for r, e in enumerate(np.eye(4)):
            for s, f in enumerate(np.eye(4)):
                second[r, s] = ((metric(point+step*e)-2*value+metric(point-step*e))/step**2 if r == s else
                    (metric(point+step*e+step*f)-metric(point+step*e-step*f)-metric(point-step*e+step*f)+metric(point-step*e-step*f))/(4*step**2))
        independent = model.dirac.geometry.metric_curvature(value, first, second)
        self.assertClose(independent["scalar"], self.geometry["bundle"]["curvature"]["scalar"], atol=0.1, rtol=3e-6)

    def test_coordinate_derivative_change_transports_coframe_and_metric(self):
        psi, derivative = self.random_jet()
        jacobian = np.eye(4)
        jacobian[1, 2], jacobian[0, 0] = 0.2, 1.3
        before = model.channels(psi, derivative)["odd"]
        after = model.channels(psi, np.einsum("mn,nrs->mrs", jacobian, derivative))["odd"]
        self.assertClose(after, before @ jacobian.T)
        self.assertClose(after.T @ model.ETA @ after, jacobian @ (before.T @ model.ETA @ before) @ jacobian.T)

    def test_amplitude_scaling_changes_coframe_and_curvature_normalization(self):
        data = dict(self.data)
        for key in ("psi", "first", "second", "third"):
            data[key] = 2*data[key]
        frame, first, second = model.odd_coframe_jet(data)
        bundle = model.dirac.bundle(frame, first, second)
        self.assertClose(frame, 4*self.geometry["frame"])
        self.assertClose(bundle["curvature"]["scalar"], self.geometry["bundle"]["curvature"]["scalar"]/16)

    def test_sourced_stationary_branch_is_still_rank_two(self):
        result = self.report["existing_sourced_stationary_branch"]
        self.assertEqual(result["odd_rank"], 2)
        self.assertLess(result["angular_columns_norm"], 1e-14)

    def test_reference_success_is_not_promoted_to_same_induced_probe_solution(self):
        self.assertGreater(np.linalg.norm(self.geometry["induced_residual"]), 100)
        self.assertGreater(np.linalg.norm(self.geometry["rebuilt_with_induced_spin"]-self.geometry["frame"]), 0.001)

    def test_effective_parent_weights_are_hermitian(self):
        multiplier = np.random.default_rng(29).normal(size=(4, 4))
        weights = model.effective_weights(1.1, multiplier)
        self.assertClose(weights, weights.conj().swapaxes(-1, -2))

    def test_parent_phase_flux_is_standard_plus_constraint_current(self):
        psi, derivative = self.random_jet()
        multiplier = np.random.default_rng(13).normal(size=(4, 4))
        volume = 1.2
        weights = model.effective_weights(volume, multiplier)
        charge = model.channels(psi, derivative)["phase_charge"]
        ordinary = np.array([np.vdot(psi, psi @ k.T).real for k in model.WEIGHTS])
        total = np.einsum("i,mij,j->m", psi.reshape(-1).conj(), weights, psi.reshape(-1)).real
        self.assertClose(total, volume*ordinary+multiplier.T @ charge)

    def test_parent_local_phase_variation_matches_total_current(self):
        psi, derivative = self.random_jet()
        multiplier = np.random.default_rng(13).normal(size=(4, 4))
        volume, gradient = 1.2, np.array([0.3, -0.1, 0.2, 0.4])
        weights = model.effective_weights(volume, multiplier)
        vector, first = psi.reshape(-1), derivative.reshape(4, -1)
        zero, mass = np.zeros_like(weights), np.kron(np.eye(3), model.BETA)
        before = model.real_law.action_density(vector, first, weights, zero, mass)
        after = model.real_law.action_density(vector, first+1j*gradient[:, None]*vector, weights, zero, mass)
        current = np.einsum("i,mij,j->m", vector.conj(), weights, vector).real
        self.assertAlmostEqual(after-before, -current @ gradient)

    def test_direct_parent_constraint_action_equals_modified_kinetic_density(self):
        self.assertLess(self.report["parent_action_check"]["direct_parent_density_action_error"], 2e-11)

    def test_independently_varied_parent_probe_equation_agrees(self):
        self.assertLess(self.report["parent_action_check"]["independent_probe_variation_error"], 2e-7)

    def test_full_parent_off_shell_Ward_identity_is_retained(self):
        self.assertLess(self.report["parent_action_check"]["phase_Ward_identity_max_error"], 2e-11)

    def test_temporal_margin_is_exact_smallest_eigenvalue(self):
        rng = np.random.default_rng(82)
        for _ in range(8):
            multiplier = rng.normal(size=(4, 4))
            volume = rng.uniform(0.3, 2)
            self.assertAlmostEqual(np.linalg.eigvalsh(model.effective_weights(volume, multiplier)[0])[0], model.temporal_margin(volume, multiplier))

    def test_positive_temporal_domain_is_nonempty_in_variation_example(self):
        self.assertGreater(self.report["parent_action_check"]["minimum_temporal_weight_eigenvalue"], 0.85)

    def test_temporal_positivity_boundary_and_failure_are_real(self):
        multiplier = np.zeros((4, 4))
        multiplier[0, 0] = 2
        self.assertAlmostEqual(model.temporal_margin(1, multiplier), 0)
        self.assertAlmostEqual(np.linalg.eigvalsh(model.effective_weights(1, multiplier)[0])[0], 0)
        multiplier[1, 0] = 0.5
        self.assertLess(np.linalg.eigvalsh(model.effective_weights(1, multiplier)[0])[0], -0.24)

    def test_quadrature_copy_reduces_odd_readout_to_kinetic_bilinear(self):
        psi, derivative = self.random_jet()
        psi, derivative = psi[:1], derivative[:, :1]
        for delta in (0, 0.3, np.pi/2):
            pair = np.vstack((psi, np.exp(1j*delta)*psi, np.zeros_like(psi)))
            dpair = np.concatenate((derivative, np.exp(1j*delta)*derivative, np.zeros_like(derivative)), axis=1)
            self.assertClose(model.channels(pair, dpair)["odd"], -np.sin(delta)*model.readouts.pairing(psi, derivative).imag)

    def test_quadrature_is_not_automatically_preserved_by_prepared_mediator(self):
        psi, _ = self.random_jet()
        pair = np.vstack((psi[:1], 1j*psi[:1], np.zeros_like(psi[:1])))
        mass = model.background.triadic_mass()
        second = -mass @ mass @ pair
        self.assertGreater(np.linalg.norm(second[1]-1j*second[0]), 1)
        neutral_second = -0.6**2*pair
        self.assertClose(neutral_second[1]-1j*neutral_second[0], 0)

    def test_kinetic_self_dictionary_has_fixed_volume_contraction(self):
        result = model.kinetic_volume_control(self.data)
        self.assertLess(result["volume_identity_error"], 1e-12)
        self.assertAlmostEqual(result["probe"]["lagrangian"]+result["probe"]["mass_bilinear"].real, 4)

    def test_kinetic_self_dictionary_enforces_pure_trace_standard_stress(self):
        result = model.kinetic_volume_control(self.data)
        self.assertLess(result["pure_trace_stress_error"], 2e-12)
        self.assertClose(result["probe"]["stress"], (result["probe"]["lagrangian"]-1)*result["metric"])
        self.assertGreater(np.linalg.norm(result["probe"]["residual"]), 1)

    def test_invalid_points_volume_and_selector_shapes_are_rejected(self):
        with self.assertRaises(ValueError):
            model.reference_geometry((0, 0.02, -0.03, 0.01))
        for volume in (0, -1, np.nan, np.inf):
            with self.assertRaises(ValueError):
                model.effective_weights(volume, np.zeros((4, 4)))
        with self.assertRaises(ValueError):
            model.effective_weights(1, np.zeros((4, 4)), np.eye(2))

    def test_saved_report_retains_candidate_scope_and_reproducible_diagnostics(self):
        saved = json.loads((ROOT / "analysis/HC_Antisymmetric_Cross_Geometry.json").read_text(encoding="utf-8"))
        for key in ("status", "source", "identities", "remaining_obligations", "main_TeX_changed"):
            self.assertEqual(saved[key], self.report[key])
        self.assertFalse(saved["main_TeX_changed"])
        self.assertIn("NOT native", saved["status"])
        for key in ("coframe", "coframe_singular_values", "Ricci_scalar_not_physically_calibrated"):
            self.assertClose(saved["reference_on_shell_curved_diagnostic"][key], self.report["reference_on_shell_curved_diagnostic"][key])


if __name__ == "__main__":
    unittest.main()
