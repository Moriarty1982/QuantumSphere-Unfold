"""Static minima, phase gradients, inertial trapping and canonical modes are distinct."""
from pathlib import Path
import importlib.util
import json
import math
import unittest
from unittest.mock import patch

import numpy as np


ROOT = Path(__file__).resolve().parents[3]
SPEC = importlib.util.spec_from_file_location("hc_root_dynamics", ROOT / "analysis/HC_Root_Phase_Dynamics.py")
dynamics = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(dynamics)
readout = dynamics.readout
backreaction = dynamics.backreaction


class HCRootPhaseDynamicsTests(unittest.TestCase):
    def assertClose(self, actual, expected, atol=3e-12):
        np.testing.assert_allclose(actual, expected, atol=atol, rtol=2e-9)

    def density(self, phi=0.3):
        chi = dynamics.aligned_mode(phi)
        return np.outer(chi, chi.conj())

    def test_normalized_quadratic_root_equals_the_previous_cyclic_matrix(self):
        for phi in [-math.pi/4, -0.3, 0, 0.3, math.pi/4]:
            expected = backreaction.cyclic_root_with_radius(phi, 1/math.sqrt(2))
            for amplitude in [0.3, 1, 2]:
                chi = dynamics.aligned_mode(phi, amplitude)
                l = readout.quadratic_root(chi)
                self.assertClose(l/(math.sqrt(2)*amplitude**2), expected)

    def test_phase_dictionary_reproduces_the_same_normalized_gram(self):
        for phi in [-0.5, 0, 0.6]:
            l = readout.quadratic_root(dynamics.aligned_mode(phi))
            q = l @ l/np.vdot(l, l).real
            self.assertClose(q, backreaction.cyclic_gram_and_derivative(phi)[0])

    def test_all_three_chambers_have_the_same_symmetric_spectral_energy(self):
        for phi in [-0.4, 0.1, 0.6]:
            expected = dynamics.phase_energy(phi, 0.05)[0]
            for chamber in range(3):
                chi = dynamics.aligned_mode(phi, chamber=chamber)
                rho = np.outer(chi, chi.conj())
                energy, _, _ = dynamics.density_energy_gradient(rho, 0.05)
                self.assertAlmostEqual(energy, expected)

    def test_edge_energy_is_exact_and_the_phase_force_vanishes(self):
        for k in [0.041, 0.05, 0.065]:
            for phi in [-math.pi/4, math.pi/4]:
                energy, prime = dynamics.phase_energy(phi, k)
                self.assertAlmostEqual(energy, 2*k-2*k*k)
                self.assertAlmostEqual(prime, 0)

    def test_one_sided_edge_curvature_has_the_derived_negative_value(self):
        step = 1e-6
        for k in [0.041, 0.05, 0.065]:
            edge_force = dynamics.phase_energy(math.pi/4, k)[1]
            inner_force = dynamics.phase_energy(math.pi/4-step, k)[1]
            self.assertAlmostEqual((edge_force-inner_force)/step, -2*k/27, delta=4e-8)

    def test_positive_phase_gradient_points_toward_the_unique_positive_minimum(self):
        for k in [0.041, 0.05, 0.065]:
            phi_star = backreaction.solve_positive_cone_phase(k)["phase_radians"]
            for phi in [phi_star/3, 2*phi_star/3]:
                self.assertGreater(dynamics.gradient_phase_rhs(phi, k), 0)
            for phi in [(phi_star+math.pi/4)/2, (phi_star+3*math.pi/4)/4]:
                self.assertLess(dynamics.gradient_phase_rhs(phi, k), 0)

    def test_negative_phase_gradient_is_the_odd_reflection(self):
        for phi in [0.1, 0.3, 0.65]:
            self.assertAlmostEqual(dynamics.gradient_phase_rhs(-phi, 0.05),
                                   -dynamics.gradient_phase_rhs(phi, 0.05))

    def test_center_edges_and_selected_phases_are_equilibria_of_the_gradient_law(self):
        k = 0.05
        phi_star = backreaction.solve_positive_cone_phase(k)["phase_radians"]
        for phi in [0, -math.pi/4, math.pi/4, -phi_star, phi_star]:
            self.assertAlmostEqual(dynamics.gradient_phase_rhs(phi, k), 0)

    def test_gradient_energy_rate_is_negative_and_mobility_only_rescales_time(self):
        phi, k, mobility = 0.3, 0.05, 2.7
        prime = dynamics.phase_energy(phi, k)[1]
        velocity = dynamics.gradient_phase_rhs(phi, k, mobility)
        self.assertAlmostEqual(velocity, mobility*dynamics.gradient_phase_rhs(phi, k))
        self.assertAlmostEqual(prime*velocity, -mobility*prime**2)
        self.assertLess(prime*velocity, 0)

    def test_gradient_lift_is_tangent_to_the_fixed_norm_odd_mode_circle(self):
        phi, amplitude = 0.3, 1.7
        for chamber in range(3):
            chi = dynamics.aligned_mode(phi, amplitude, chamber)
            rhs = dynamics.gradient_mode_rhs(phi, 0.05, amplitude, chamber)
            self.assertAlmostEqual(np.vdot(chi, rhs).real, 0)
            self.assertClose(rhs.conj(), -rhs)
            step = 1e-5
            tangent = (dynamics.aligned_mode(phi+step, amplitude, chamber)
                       -dynamics.aligned_mode(phi-step, amplitude, chamber))/(2*step)
            self.assertClose(rhs, dynamics.gradient_phase_rhs(phi, 0.05)*tangent)

    def test_monotone_implicit_gradient_steps_stay_on_the_initial_admitted_branch(self):
        # Implicit steps are solved inside the invariant basin; they are a check, not the proof.
        k, step = 0.05, 20
        phi_star = backreaction.solve_positive_cone_phase(k)["phase_radians"]
        for initial in [0.1, 0.7]:
            phi, previous = initial, dynamics.phase_energy(initial, k)[0]
            for _ in range(20):
                lower, upper = sorted([phi, phi_star])
                for _ in range(45):
                    mid = (lower+upper)/2
                    residual = mid-phi-step*dynamics.gradient_phase_rhs(mid, k)
                    if residual < 0:
                        lower = mid
                    else:
                        upper = mid
                phi = (lower+upper)/2
                energy = dynamics.phase_energy(phi, k)[0]
                self.assertGreater(phi, 0)
                self.assertLess(phi, math.pi/4)
                self.assertLessEqual(energy, previous+1e-13)
                previous = energy
            self.assertLess(abs(phi-phi_star), abs(initial-phi_star))

    def test_any_nonzero_constant_extra_drift_breaks_at_least_one_boundary_guard(self):
        for drift in [-1e-3, 1e-3]:
            left = dynamics.gradient_phase_rhs(-math.pi/4, 0.05)+drift
            right = dynamics.gradient_phase_rhs(math.pi/4, 0.05)+drift
            self.assertTrue(left < 0 or right > 0)

    def test_phase_barrier_is_positive_throughout_sampled_strict_threshold_window(self):
        for k in np.linspace(backreaction.LOWER_THRESHOLD+1e-4, backreaction.UPPER_THRESHOLD-1e-4, 9):
            data = dynamics.barrier_audit(float(k))
            self.assertGreater(data["barrier_above_minimum"], 0)
            self.assertAlmostEqual(data["edge_energy"]-data["minimum_energy"], data["barrier_above_minimum"])

    def test_barrier_example_and_critical_speed_are_dimensionless_not_mass_predictions(self):
        data = dynamics.barrier_audit()
        self.assertAlmostEqual(data["barrier_above_minimum"], 0.00010876474258235402)
        self.assertAlmostEqual(data["critical_speed_at_minimum"]**2/2, data["barrier_above_minimum"])
        self.assertTrue(data["energy_gap_is_in_units_lambda_H_t_squared"])

    def test_inertial_energy_rate_equals_minus_damping_times_velocity_squared(self):
        phi, velocity, k, inertia = 0.3, 0.02, 0.05, 1.8
        prime = dynamics.phase_energy(phi, k)[1]
        for damping in [0, 0.2]:
            rhs = dynamics.mechanical_phase_rhs(phi, velocity, k, inertia, damping)
            self.assertAlmostEqual(inertia*velocity*rhs[1]+prime*rhs[0], -damping*velocity**2)

    def test_below_barrier_initial_data_have_no_energetically_accessible_edge(self):
        data = dynamics.barrier_audit()
        phi = data["positive_minimum_phase"]
        velocity = 0.9*data["critical_speed_at_minimum"]
        energy = dynamics.mechanical_energy(phi, velocity, 0.05)
        self.assertLess(energy, data["edge_energy"])
        self.assertLess(2*(energy-data["edge_energy"]), 0)

    def test_above_barrier_outward_undamped_motion_has_positive_speed_along_the_exit_path(self):
        data = dynamics.barrier_audit()
        witness = data["undamped_escape_witness"]
        initial = data["positive_minimum_phase"]
        energy = witness["total_energy"]
        for phi in np.linspace(initial, math.pi/4, 50):
            self.assertGreater(2*(energy-dynamics.phase_energy(float(phi), 0.05)[0]), 0)
        self.assertGreater(witness["speed_at_edge"], 0)
        self.assertTrue(math.isfinite(witness["time_to_edge_upper_bound"]))

    def test_zero_force_at_the_edge_does_not_stop_outward_inertial_velocity(self):
        rhs = dynamics.mechanical_phase_rhs(math.pi/4, 0.01, 0.05)
        self.assertGreater(rhs[0], 0)
        self.assertAlmostEqual(rhs[1], 0)

    def test_phase_barrier_tends_to_zero_near_the_upper_threshold(self):
        far = dynamics.barrier_audit(backreaction.UPPER_THRESHOLD-0.001)["barrier_above_minimum"]
        near = dynamics.barrier_audit(backreaction.UPPER_THRESHOLD-0.0001)["barrier_above_minimum"]
        self.assertGreater(far, near)
        self.assertGreater(near, 0)

    def test_density_extension_equals_the_old_phase_energy_on_the_real_plane(self):
        for phi in [-0.5, 0, 0.3, 0.7]:
            energy, _, _ = dynamics.density_energy_gradient(self.density(phi), 0.05)
            self.assertAlmostEqual(energy, dynamics.phase_energy(phi, 0.05)[0])

    def test_hermitian_density_gradient_matches_independent_finite_differences(self):
        rho = np.array([[0.6, 0.1+0.04j], [0.1-0.04j, 0.4]])
        _, h, _ = dynamics.density_energy_gradient(rho, 0.05)
        directions = [np.eye(2), readout.SIGMA_Z, readout.SIGMA_X, dynamics.SIGMA_Y]
        step = 1e-5
        for direction in directions:
            plus = dynamics.density_energy_gradient(rho+step*direction, 0.05)[0]
            minus = dynamics.density_energy_gradient(rho-step*direction, 0.05)[0]
            self.assertAlmostEqual((plus-minus)/(2*step), np.trace(h @ direction).real, delta=3e-10)

    def test_canonical_hamiltonian_is_real_symmetric_and_has_no_sigma_y_component(self):
        _, h, _ = dynamics.density_energy_gradient(self.density(), 0.05)
        self.assertClose(h, h.conj().T)
        self.assertClose(h.imag, np.zeros((2, 2)))
        self.assertAlmostEqual(np.trace(dynamics.SIGMA_Y @ h).real, 0)

    def test_canonical_density_rhs_conserves_trace_purity_and_this_energy(self):
        rho = self.density()
        _, h, _ = dynamics.density_energy_gradient(rho, 0.05)
        rhs = dynamics.canonical_density_rhs(rho, 0.05)
        self.assertAlmostEqual(np.trace(rhs).real, 0)
        self.assertAlmostEqual(2*np.trace(rho @ rhs).real, 0)
        self.assertAlmostEqual(np.trace(h @ rhs).real, 0)

    def test_angular_energy_derivative_is_three_times_the_invariant_phase_derivative(self):
        for phi in [0.1, 0.3, 0.6]:
            rho = self.density(phi)
            x1, x2 = np.trace(readout.SIGMA_Z @ rho).real, np.trace(readout.SIGMA_X @ rho).real
            _, h, _ = dynamics.density_energy_gradient(rho, 0.05)
            hz, hx = np.trace(readout.SIGMA_Z @ h).real/2, np.trace(readout.SIGMA_X @ h).real/2
            self.assertAlmostEqual(-hz*x2+hx*x1, 3*dynamics.phase_energy(phi, 0.05)[1])

    def test_canonical_energy_gradient_generates_the_missing_imaginary_bilinear(self):
        for phi in [-0.4, 0.1, 0.3, 0.65]:
            rho = self.density(phi)
            self.assertAlmostEqual(np.trace(dynamics.SIGMA_Y @ rho).real, 0)
            rhs = dynamics.canonical_density_rhs(rho, 0.05)
            actual = np.trace(dynamics.SIGMA_Y @ rhs).real
            expected = -6*dynamics.phase_energy(phi, 0.05)[1]
            self.assertAlmostEqual(actual, expected)
            self.assertGreater(abs(actual), 1e-5)

    def test_a_common_mode_phase_cannot_remove_the_generated_relative_bilinear(self):
        chi = dynamics.aligned_mode(0.3)
        _, h, _ = dynamics.density_energy_gradient(self.density(), 0.05)
        values, vectors = np.linalg.eigh(h)
        evolved = (vectors*np.exp(-1j*values*0.01)) @ vectors.conj().T @ chi
        x3 = readout.quadratic_coordinates(evolved)[3]
        self.assertGreater(abs(x3), 1e-6)
        for phase in [0.2, 0.9, math.pi/2]:
            self.assertAlmostEqual(readout.quadratic_coordinates(np.exp(1j*phase)*evolved)[3], x3)

    def test_initial_canonical_step_has_the_derived_second_order_koide_deficit(self):
        # Frozen H has the same first-order tangent as the self-consistent law.
        phi, step = 0.3, 0.01
        chi = dynamics.aligned_mode(phi)
        _, h, _ = dynamics.density_energy_gradient(self.density(phi), 0.05)
        values, vectors = np.linalg.eigh(h)
        evolved = (vectors*np.exp(-1j*values*step)) @ vectors.conj().T @ chi
        actual = 2/3-readout.root_diagnostic(readout.quadratic_root(evolved))["Koide_ratio"]
        expected = 12*dynamics.phase_energy(phi, 0.05)[1]**2*step**2
        self.assertAlmostEqual(actual/expected, 1, delta=2e-5)

    def test_canonical_flow_is_stationary_at_the_selected_real_plane_extremum(self):
        phi = backreaction.solve_positive_cone_phase(0.05)["phase_radians"]
        self.assertClose(dynamics.canonical_density_rhs(self.density(phi), 0.05), np.zeros((2, 2)))

    def test_invalid_chambers_kinetics_and_density_data_are_rejected(self):
        for phi in [math.nan, 1]:
            with self.assertRaises(ValueError):
                dynamics.phase_energy(phi, 0.05)
        for k in [0, backreaction.LOWER_THRESHOLD, backreaction.UPPER_THRESHOLD, math.nan]:
            with self.assertRaises(ValueError):
                dynamics.phase_energy(0.3, k)
        for amplitude, chamber in [(0, 1), (-1, 1), (1, 3), (1, True)]:
            with self.assertRaises(ValueError):
                dynamics.aligned_mode(0.3, amplitude, chamber)
        with self.assertRaises(ValueError):
            dynamics.gradient_phase_rhs(0.3, 0.05, 0)
        for velocity, inertia, damping in [(math.inf, 1, 0), (0, 0, 0), (0, 1, -1)]:
            with self.assertRaises(ValueError):
                dynamics.mechanical_phase_rhs(0.3, velocity, 0.05, inertia, damping)
        for rho in [np.zeros((2, 2)), np.eye(3), np.diag([1, -1])]:
            with self.assertRaises(ValueError):
                dynamics.density_energy_gradient(rho, 0.05)

    def test_report_marks_the_native_dynamic_and_shape_obligations_as_open(self):
        data = dynamics.evaluate()
        boundary = data["source_boundary"]
        self.assertFalse(boundary["main_TeX_changed"])
        self.assertTrue(boundary["eta_one_norm_transfer_still_assumed"])
        self.assertTrue(boundary["phase_kinetic_and_mobility_not_derived_from_native_action"])
        self.assertTrue(boundary["radius_and_scale_are_held_fixed_and_have_prior_descent_obstructions"])
        self.assertTrue(data["different_canonical_two_mode_law"]["nonstationary_odd_plane_is_not_invariant_under_this_canonical_law"])

    def test_saved_report_reproduces_without_historical_masses(self):
        before = dynamics.evaluate()
        with patch.object(backreaction.phase.candidate, "HISTORICAL_MASSES_MEV", np.array([1, 2, 3])):
            self.assertEqual(dynamics.evaluate(), before)
        self.assertFalse(before["source_boundary"]["historical_masses_or_target_phase_used"])
        saved = json.loads((ROOT / "analysis/HC_Root_Phase_Dynamics.json").read_text(encoding="utf-8"))
        self.assertEqual(saved, before)

    def test_transverse_density_is_pure_with_the_specified_imaginary_bilinear(self):
        for y in [-0.3, 0, 0.4]:
            rho = dynamics.pure_mode_density(0.3, y)
            self.assertClose(rho @ rho, rho)
            self.assertAlmostEqual(np.trace(rho).real, 1)
            self.assertAlmostEqual(np.trace(dynamics.SIGMA_Y @ rho).real, y)

    def test_transverse_pure_modes_change_the_root_radius_at_fixed_readout_eta(self):
        phi = 0.3
        for y in [0, 0.2, 0.4]:
            rho = dynamics.pure_mode_density(phi, y)
            l = readout.density_root(rho)
            root_data = readout.root_diagnostic(l)
            self.assertAlmostEqual(root_data["Koide_ratio"], (2-y*y)/3)
            energy = dynamics.density_energy_gradient(rho, 0.05)[0]
            ratio = math.sqrt(1-y*y)/math.sqrt(2)
            expected = backreaction.radius_energy_and_derivative(phi, ratio, 0.05)[0]
            self.assertAlmostEqual(energy, expected)

    def test_transverse_curvature_matches_the_old_radial_descent_and_finite_differences(self):
        data = dynamics.canonical_saddle_audit()
        phi, step = data["stationary_phase"], 1e-4
        center = dynamics.density_energy_gradient(dynamics.pure_mode_density(phi), 0.05)[0]
        plus = dynamics.density_energy_gradient(dynamics.pure_mode_density(phi, step), 0.05)[0]
        minus = dynamics.density_energy_gradient(dynamics.pure_mode_density(phi, -step), 0.05)[0]
        self.assertLess(data["transverse_curvature"], 0)
        self.assertAlmostEqual((plus-2*center+minus)/step**2, data["transverse_curvature"], delta=5e-8)

    def test_canonical_coordinate_linearization_is_the_predicted_hyperbolic_saddle(self):
        data = dynamics.canonical_saddle_audit()
        phi, step = data["stationary_phase"], 1e-5
        phase_column = (dynamics.canonical_coordinate_rhs(phi+step, 0, 0.05)
                        -dynamics.canonical_coordinate_rhs(phi-step, 0, 0.05))/(2*step)
        transverse_column = (dynamics.canonical_coordinate_rhs(phi, step, 0.05)
                             -dynamics.canonical_coordinate_rhs(phi, -step, 0.05))/(2*step)
        jacobian = np.column_stack([phase_column, transverse_column])
        self.assertClose(jacobian, data["linearization"], atol=4e-10)
        self.assertClose(np.sort(np.linalg.eigvals(jacobian).real), data["linearized_growth_and_decay_rates"], atol=4e-10)

    def test_canonical_coordinate_equations_match_the_energy_gradient_off_the_real_plane(self):
        phi, y, step = 0.3, 0.1, 1e-5
        def energy(p, transverse):
            return dynamics.density_energy_gradient(dynamics.pure_mode_density(p, transverse), 0.05)[0]
        phi_prime = (energy(phi+step, y)-energy(phi-step, y))/(2*step)
        y_prime = (energy(phi, y+step)-energy(phi, y-step))/(2*step)
        self.assertClose(dynamics.canonical_coordinate_rhs(phi, y, 0.05), [6*y_prime, -6*phi_prime], atol=3e-10)

    def test_transverse_coordinate_guard_does_not_hide_the_phase_poles(self):
        for y in [-1, 1, math.nan]:
            with self.assertRaises(ValueError):
                dynamics.pure_mode_density(0.3, y)
