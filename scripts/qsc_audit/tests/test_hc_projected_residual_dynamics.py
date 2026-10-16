"""Projection preserves odd output typing, not automatically its phase cone or autonomy."""
from pathlib import Path
import importlib.util
import json
import math
import unittest
from unittest.mock import patch

import numpy as np


ROOT = Path(__file__).resolve().parents[3]
SPEC = importlib.util.spec_from_file_location("hc_projected", ROOT / "analysis/HC_Projected_Residual_Dynamics.py")
projected = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(projected)
phase, readout = projected.phase, projected.readout
T = projected.IMAGINARY_READOUT


class HCProjectedResidualDynamicsTests(unittest.TestCase):
    def assertClose(self, actual, expected, atol=3e-12):
        np.testing.assert_allclose(actual, expected, atol=atol, rtol=2e-9)

    def test_time_generator_satisfies_the_original_first_order_equation(self):
        rng = np.random.default_rng(81)
        matrices = [rng.normal(size=(3, 3))+1j*rng.normal(size=(3, 3)) for _ in range(4)]
        gamma, omega, connection, spatial = matrices
        g = projected.temporal_generator(gamma, omega, connection, spatial)
        self.assertClose(1j*gamma @ (g+connection)+1j*spatial-omega, np.zeros((3, 3)))

    def test_temporal_compensator_connection_can_supply_damping_with_declared_sign(self):
        d, omega = np.diag([0.2, 0.4]), phase.SIGMA_Y
        g = projected.temporal_generator(np.eye(2), omega, d, np.zeros((2, 2)))
        self.assertClose(g, -d-1j*omega)
        state = np.array([0.3+0.2j, 0.4-0.1j])
        self.assertAlmostEqual(2*np.vdot(state, g @ state).real, -2*np.vdot(state, d @ state).real)
        self.assertLess(2*np.vdot(state, g @ state).real, 0)

    def test_time_chart_guards_reject_singular_or_mismatched_operators(self):
        with self.assertRaises(ValueError):
            projected.temporal_generator(np.zeros((2, 2)), np.eye(2), np.eye(2), np.eye(2))
        with self.assertRaises(ValueError):
            projected.temporal_generator(np.eye(2), np.eye(3), np.eye(2), np.eye(2))

    def test_realification_matches_complex_linear_transport(self):
        g = np.array([[0.2+0.4j, -0.3j], [0.1+0.5j, -0.7]])
        state = np.array([0.1+0.3j, -0.2+0.4j])
        self.assertClose(projected.realification(g) @ projected.real_state(state), projected.real_state(g @ state))

    def test_imaginary_readout_is_the_real_form_of_the_antiunitary_odd_projection(self):
        f = np.array([0.1+0.3j, -0.2+0.4j])
        r = T @ projected.real_state(f)
        self.assertClose(1j*r, readout.odd_residual(f))
        self.assertClose((1j*r).conj(), -1j*r)

    def test_full_row_rank_transfer_factorization_keeps_the_exact_hidden_term(self):
        rng = np.random.default_rng(82)
        transfer, transfer_rate = rng.normal(size=(2, 6)), rng.normal(size=(2, 6))
        generator, state = rng.normal(size=(6, 6)), rng.normal(size=6)
        blocks = projected.projected_blocks(transfer, transfer_rate, generator)
        result = projected.projected_rhs(state, transfer, transfer_rate, generator)
        self.assertClose(transfer @ blocks["right_inverse"], np.eye(2))
        self.assertClose(transfer @ blocks["kernel_projector"], np.zeros((2, 6)))
        self.assertClose(result["rate"], (transfer_rate+transfer @ generator) @ state)
        self.assertClose(result["rate"], result["local_rate"]+result["hidden_rate"])

    def test_autonomous_factorization_annihilates_every_kernel_lift(self):
        k = np.array([[0, -0.2], [0.2, 0]])
        g = np.block([[np.eye(2), np.eye(2)], [np.zeros((2, 2)), k]])
        blocks = projected.projected_blocks(T, np.zeros_like(T), g)
        self.assertClose(blocks["local_generator"], k)
        self.assertClose(blocks["hidden_coupling"], np.zeros((2, 4)))
        r = np.array([0.3, 0.4])
        for x in [np.zeros(2), np.array([1, -2])]:
            result = projected.projected_rhs(np.r_[x, r], T, np.zeros_like(T), g)
            self.assertClose(result["rate"], k @ r)

    def test_same_residual_and_same_full_norm_can_have_opposite_phase_velocities(self):
        rows = projected.evaluate()["fixed_frame_Hermitian_case"]["same_normalized_state_norm_and_same_residual_different_velocity"]
        self.assertClose(rows[0]["same_residual"], rows[1]["same_residual"])
        self.assertAlmostEqual(rows[0]["full_norm_squared"], 1)
        self.assertAlmostEqual(rows[1]["full_norm_squared"], 1)
        self.assertAlmostEqual(rows[0]["Phi_rate"], -rows[1]["Phi_rate"])
        self.assertGreater(abs(rows[0]["Phi_rate"]), 1)

    def test_Hermitian_split_gives_the_derived_even_odd_block_equations(self):
        h = np.array([[2, 0.4-0.3j], [0.4+0.3j, 1]])
        f = np.array([0.1+0.5j, -0.2+0.7j])
        s, b, x, r = h.real, h.imag, f.real, f.imag
        full_rate = projected.mode_generator(h) @ f
        self.assertClose(full_rate.real, b @ x+s @ r)
        self.assertClose(full_rate.imag, b @ r-s @ x)

    def test_autonomy_of_the_full_odd_readout_requires_the_real_Hamiltonian_block_to_vanish(self):
        for h in [phase.SIGMA_Y, np.eye(2), np.diag([1, 2])]:
            blocks = projected.projected_blocks(T, np.zeros_like(T), projected.realification(projected.mode_generator(h)))
            self.assertClose(blocks["local_generator"], h.imag)
            self.assertClose(blocks["hidden_coupling"][:, :2], -h.real)

    def test_commutation_with_conjugation_is_not_same_time_odd_invariance(self):
        h, f = np.diag([1, 2]), phase.aligned_mode(0)
        self.assertClose(h.conj(), h)
        later = projected.unitary_state(h, f, 0.3)
        self.assertGreater(np.linalg.norm(later.real), 0.1)
        self.assertGreater(np.linalg.norm(later.conj()+later), 0.1)

    def test_pure_imaginary_Hamiltonian_preserves_oddness_but_rotates_the_angle(self):
        h = 0.2*phase.SIGMA_Y
        f = phase.aligned_mode(0)
        later = projected.unitary_state(h, f, 0.3)
        self.assertClose(later.conj(), -later)
        result = projected.residual_angle_rate(f.imag, (projected.mode_generator(h) @ f).imag)
        self.assertAlmostEqual(result["norm_squared_rate"], 0)
        self.assertAlmostEqual(result["theta_rate"], 0.4)
        self.assertAlmostEqual(result["Phi_rate"], 1.2)

    def test_pure_odd_initial_data_do_not_make_a_real_Hamiltonian_autonomous(self):
        h, f = np.diag([1, 2]), phase.aligned_mode(0)
        self.assertClose((projected.mode_generator(h) @ f).imag, np.zeros(2))
        later = projected.unitary_state(h, f, 0.3)
        self.assertClose(later.imag, f.imag*np.cos(np.array([1, 2])*0.3))
        self.assertGreater(np.linalg.norm(later.imag-f.imag), 0.1)

    def test_second_derivative_contains_the_return_from_the_even_sector(self):
        h, f, step = np.diag([1, 2]), phase.aligned_mode(0), 1e-4
        plus, minus = projected.unitary_state(h, f, step), projected.unitary_state(h, f, -step)
        self.assertClose((plus.imag-2*f.imag+minus.imag)/step**2, -h @ h @ f.imag, atol=5e-8)

    def test_exact_memory_integral_reproduces_the_projected_velocity(self):
        b, s = 0.2*projected.ROTATION, np.diag([1, 2])
        h, time = s+1j*b, 0.4
        initial = np.array([0.1, -0.2])+phase.aligned_mode(0)
        state = projected.unitary_state(h, initial, time)
        def rotation(t):
            angle = 0.2*t
            return np.array([[math.cos(angle), -math.sin(angle)], [math.sin(angle), math.cos(angle)]])
        count = 100
        integrand = np.array([s @ rotation(time-t) @ s @ projected.unitary_state(h, initial, t).imag
                              for t in np.linspace(0, time, count+1)])
        integral = (time/count)/3*(integrand[0]+integrand[-1]
                                  +4*integrand[1:-1:2].sum(axis=0)+2*integrand[2:-1:2].sum(axis=0))
        memory_rate = b @ state.imag-s @ rotation(time) @ initial.real-integral
        self.assertClose(memory_rate, (projected.mode_generator(h) @ state).imag, atol=5e-11)

    def test_scalar_unitary_phase_can_drive_the_projected_scale_to_zero(self):
        f = phase.aligned_mode(0)
        state = projected.unitary_state(np.eye(2), f, math.pi/2)
        self.assertAlmostEqual(np.vdot(state, state).real, 1)
        self.assertClose(state.imag, np.zeros(2))

    def test_moving_frame_connection_is_required_even_for_a_scalar_Hamiltonian(self):
        f, h, v = phase.aligned_mode(0), np.eye(2), np.eye(2)
        result = projected.moving_frame_residual_rhs(f, h, v, -1j*v)
        self.assertClose(result["local_hamiltonian"], np.zeros((2, 2)))
        self.assertClose(result["residual_rate"], np.zeros(2))

    def test_moving_extraction_derivative_matches_the_direct_frame_chain_rule(self):
        f = np.array([0.2+0.4j, 0.3-0.1j])
        h, frame_h = readout.SIGMA_X, 0.4*readout.SIGMA_Z
        v, vp = np.eye(2), -1j*frame_h
        transfer, transfer_rate = T @ projected.realification(v.conj().T), T @ projected.realification(vp.conj().T)
        g = projected.realification(projected.mode_generator(h))
        result = projected.projected_rhs(projected.real_state(f), transfer, transfer_rate, g)
        direct = projected.moving_frame_residual_rhs(f, h, v, vp)
        self.assertClose(result["rate"], direct["residual_rate"])

    def test_damping_and_Hamiltonian_parts_cannot_cancel_the_odd_hidden_block_nontrivially(self):
        s = np.array([[1, 0.4], [0.4, 2]])
        e = np.array([[0, -0.3], [0.3, 0]])
        h, damping = s+0.2j*projected.ROTATION, np.eye(2)+1j*e
        blocks = projected.projected_blocks(T, np.zeros_like(T), projected.realification(projected.mode_generator(h, damping)))
        self.assertClose(blocks["hidden_coupling"][:, :2], -s-e)
        self.assertAlmostEqual(np.vdot(s+e, s+e).real, np.vdot(s, s).real+np.vdot(e, e).real)

    def test_real_damping_and_imaginary_Hamiltonian_give_a_closed_real_generator(self):
        h, d = 0.2*phase.SIGMA_Y, np.diag([0.1, 0.3])
        blocks = projected.projected_blocks(T, np.zeros_like(T), projected.realification(projected.mode_generator(h, d)))
        self.assertClose(blocks["hidden_coupling"], np.zeros((2, 4)))
        self.assertClose(blocks["local_generator"], h.imag-d)

    def test_isotropic_damping_changes_only_the_common_amplitude(self):
        r = phase.aligned_mode(0.2).imag
        rate = -0.3*r
        result = projected.residual_angle_rate(r, rate)
        self.assertAlmostEqual(result["norm_squared_rate"], -0.6)
        self.assertAlmostEqual(result["theta_rate"], 0)

    def test_exact_angle_formula_agrees_with_finite_differentiation_of_the_residual(self):
        r, rate = np.array([0.5, 0.8]), np.array([-0.2, 0.3])
        step = 1e-6
        plus, minus = r+step*rate, r-step*rate
        theta_prime = 2*(math.atan2(plus[1], plus[0])-math.atan2(minus[1], minus[0]))/(2*step)
        self.assertAlmostEqual(projected.residual_angle_rate(r, rate)["theta_rate"], theta_prime)

    def test_any_fixed_real_generator_has_only_the_derived_first_angular_harmonic(self):
        k = np.array([[0.2, -0.4], [0.3, -0.1]])
        omega, c, d = (k[1, 0]-k[0, 1])/2, (k[1, 0]+k[0, 1])/2, (k[1, 1]-k[0, 0])/2
        for theta in np.linspace(0, 2*math.pi, 31):
            expected = 2*(omega+c*math.cos(theta)+d*math.sin(theta))
            self.assertAlmostEqual(projected.linear_angle_rate(k, float(theta)), expected)

    def test_scalar_generators_satisfy_all_three_boundary_guards_with_zero_angular_velocity(self):
        for scalar in [-0.3, 0, 0.2]:
            for row in projected.chamber_boundary_rates(scalar*np.eye(2)):
                self.assertAlmostEqual(row["left_theta_rate"], 0)
                self.assertAlmostEqual(row["right_theta_rate"], 0)

    def test_nonzero_rotation_violates_a_boundary_guard_in_every_chamber(self):
        for omega in [-0.1, 0.2]:
            for row in projected.chamber_boundary_rates(omega*projected.ROTATION):
                self.assertTrue(row["left_theta_rate"] < 0 or row["right_theta_rate"] > 0)

    def test_anisotropic_damping_can_preserve_one_chamber_without_preserving_the_other_two(self):
        rows = projected.chamber_boundary_rates(-np.diag([0, 1]))
        self.assertGreater(rows[0]["left_theta_rate"], 0)
        self.assertLess(rows[0]["right_theta_rate"], 0)
        for row in rows[1:]:
            self.assertTrue(row["left_theta_rate"] < 0 or row["right_theta_rate"] > 0)

    def test_three_distinct_angular_zeros_force_the_scalar_linear_generator(self):
        # The written IVT argument supplies one zero in each admitted chamber.
        rows = []
        basis = [np.array([[1, 0], [0, 0]]), np.array([[0, 1], [0, 0]]),
                 np.array([[0, 0], [1, 0]]), np.array([[0, 0], [0, 1]])]
        for theta in [0, 2*math.pi/3, 4*math.pi/3]:
            rows.append([projected.linear_angle_rate(k, theta) for k in basis])
        matrix = np.array(rows)
        self.assertEqual(np.linalg.matrix_rank(matrix), 3)
        self.assertClose(matrix @ np.eye(2).ravel(), np.zeros(3))

    def test_closed_rotation_witness_preserves_closure_norm_oddness_and_zero_defect(self):
        model = projected.closed_rotation_witness()
        p, m, h = model["P"], model["M"], model["H"]
        self.assertClose(p @ m-m @ p, np.zeros((3, 3)))
        self.assertClose(p @ h-h @ p, np.zeros((3, 3)))
        self.assertClose(model["defect"], np.zeros((3, 3)))
        for key in ["initial_state", "evolved_state"]:
            f = model[key]
            self.assertClose(p @ f, f)
            self.assertClose(f.conj(), -f)
            self.assertAlmostEqual(np.vdot(f, f).real, 1)
        self.assertGreater(model["minimum_root_before"], 0)
        self.assertLess(model["minimum_signed_root_after"], 0)

    def test_a_slower_rotation_delays_exit_but_does_not_prevent_it(self):
        fast, slow = projected.closed_rotation_witness(1), projected.closed_rotation_witness(0.1)
        self.assertAlmostEqual(slow["exit_time"], 10*fast["exit_time"])
        self.assertAlmostEqual(slow["minimum_signed_root_after"], fast["minimum_signed_root_after"])

    def test_projected_output_has_zero_relative_imaginary_bilinear_even_if_full_state_is_not_odd(self):
        f = projected.unitary_state(np.diag([1, 2]), phase.aligned_mode(0), 0.3)
        self.assertGreater(np.linalg.norm(f.real), 0)
        chi = readout.odd_residual(f)
        self.assertAlmostEqual(readout.quadratic_coordinates(chi)[3], 0)

    def test_bounded_hidden_force_has_the_derived_angular_error_bound(self):
        rng = np.random.default_rng(83)
        epsilon = 0.02
        for _ in range(20):
            r, q = rng.normal(size=2), rng.normal(size=2)
            q *= epsilon*np.linalg.norm(r)/np.linalg.norm(q)
            result = projected.residual_angle_rate(r, q)
            self.assertLessEqual(abs(result["theta_rate"]), 2*epsilon+1e-12)
            self.assertLessEqual(abs(result["Phi_rate"]), 6*epsilon+1e-12)

    def test_tangential_hidden_force_saturates_the_bound(self):
        r, epsilon = np.array([0.3, 0.4]), 0.02
        result = projected.residual_angle_rate(r, epsilon*projected.ROTATION @ r)
        self.assertAlmostEqual(result["theta_rate"], 2*epsilon)
        self.assertAlmostEqual(result["Phi_rate"], 6*epsilon)

    def test_old_phase_gradient_has_no_nonzero_uniform_hidden_force_margin_at_the_edge(self):
        phi, epsilon = math.pi/4, 0.001
        r = phase.aligned_mode(phi).imag
        gradient = phase.gradient_mode_rhs(phi, 0.05).imag
        forced = gradient+epsilon*projected.ROTATION @ r
        self.assertGreater(projected.residual_angle_rate(r, forced)["Phi_rate"], 0)

    def test_gradient_mode_matching_requires_a_phase_dependent_rotation_coefficient(self):
        coefficients = []
        for phi in [0.1, 0.3, 0.65]:
            r = phase.aligned_mode(phi).imag
            coefficient = phase.gradient_phase_rhs(phi, 0.05)/6
            coefficients.append(coefficient)
            self.assertClose(phase.gradient_mode_rhs(phi, 0.05).imag, coefficient*projected.ROTATION @ r)
        self.assertGreater(max(coefficients)-min(coefficients), 1e-5)

    def test_guards_reject_invalid_extractions_states_and_angles(self):
        for transfer in [np.zeros((2, 4)), np.eye(3), T+1j*T]:
            with self.assertRaises(ValueError):
                projected.projected_blocks(transfer, np.zeros_like(transfer), np.eye(4))
        with self.assertRaises(ValueError):
            projected.projected_rhs(np.ones(3), T, np.zeros_like(T), np.eye(4))
        for r, rate in [([0, 0], [0, 0]), ([1, 2, 3], [0, 0, 0]), ([1, math.nan], [0, 0])]:
            with self.assertRaises(ValueError):
                projected.residual_angle_rate(r, rate)
        with self.assertRaises(ValueError):
            projected.linear_angle_rate(np.eye(2), math.inf)

    def test_guards_reject_invalid_Hamiltonians_damping_frames_and_times(self):
        for h, d in [(np.eye(3), None), (np.eye(2), -np.eye(2)), ([[1, 1], [0, 1]], None)]:
            with self.assertRaises(ValueError):
                projected.mode_generator(h, d)
        with self.assertRaises(ValueError):
            projected.moving_frame_residual_rhs([1, 0], np.eye(2), np.eye(2), np.eye(2))
        with self.assertRaises(ValueError):
            projected.unitary_state(np.eye(2), [1, 0], math.nan)
        with self.assertRaises(ValueError):
            projected.closed_rotation_witness(0)

    def test_saved_report_reproduces_without_empirical_masses_or_a_native_claim(self):
        data = projected.evaluate()
        with patch.object(projected.backreaction.phase.candidate,
                          "HISTORICAL_MASSES_MEV", np.array([1, 2, 3])):
            self.assertEqual(projected.evaluate(), data)
        self.assertFalse(data["main_TeX_changed"])
        self.assertFalse(data["historical_masses_or_target_phase_used"])
        self.assertTrue(data["source_dictionary"]["f_equals_native_Psi_and_two_mode_extraction_are_not_given"])
        saved = json.loads((ROOT / "analysis/HC_Projected_Residual_Dynamics.json").read_text(encoding="utf-8"))
        self.assertEqual(saved, data)

    def test_complete_HC_generator_includes_temporal_spatial_and_resonance_terms_in_order(self):
        gamma0, gamma1 = readout.SIGMA_Z, 1j*phase.SIGMA_Y
        hc, kappa, coupling = np.diag([1, 4]), 0.3, 0.2
        n0, n1 = 1, 1
        g = projected.temporal_generator(gamma0, coupling*hc, kappa*n0*hc, kappa*gamma1 @ hc*n1)
        expected = projected.compensator_generator(gamma0, n0*gamma0+n1*gamma1, hc, kappa, coupling)
        self.assertClose(g, expected)

    def test_positive_mismatch_field_needs_a_commutation_or_adjoint_guard_for_attenuation(self):
        # An algebraic 1+1 Clifford witness, not native spin/internal factorization.
        gamma0, gamma1, hc = readout.SIGMA_Z, 1j*phase.SIGMA_Y, np.diag([1, 4])
        self.assertClose(gamma0 @ gamma1+gamma1 @ gamma0, np.zeros((2, 2)))
        self.assertClose(gamma0 @ gamma0, np.eye(2))
        self.assertClose(gamma1 @ gamma1, -np.eye(2))
        g = projected.compensator_generator(gamma0, gamma0+gamma1, hc)
        self.assertGreater(np.linalg.eigvalsh((g+g.conj().T)/2)[-1], 0)
        # A scalar internal field commutes and gives the expected semidefinite attenuation.
        commuting = projected.compensator_generator(gamma0, gamma0+gamma1, np.eye(2))
        self.assertLessEqual(np.linalg.eigvalsh((commuting+commuting.conj().T)/2)[-1], 1e-12)

    def test_complete_HC_generator_vanishes_at_zero_field_and_checks_its_domain(self):
        self.assertClose(projected.compensator_generator(np.eye(2), readout.SIGMA_X, np.zeros((2, 2))), np.zeros((2, 2)))
        for gamma0, gamma_n, hc in [(np.zeros((2, 2)), np.eye(2), np.eye(2)),
                                   (np.eye(2), np.eye(3), np.eye(2)),
                                   (np.eye(2), np.eye(2), -np.eye(2))]:
            with self.assertRaises(ValueError):
                projected.compensator_generator(gamma0, gamma_n, hc)
