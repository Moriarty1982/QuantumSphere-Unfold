"""Time-dependent matrix equations, pointwise hard closure and real-action countermodels."""
import importlib.util
import json
from pathlib import Path
import unittest

import numpy as np


ROOT = Path(__file__).resolve().parents[3]
SPEC = importlib.util.spec_from_file_location(
    "null_dynamical_closure", ROOT / "analysis/HC_Null_Axis_Dynamical_Closure.py")
model = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(model)


class HCNullAxisDynamicalClosureTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.report = model.evaluate()

    def assertClose(self, actual, expected, rtol=4e-8, atol=4e-10):
        np.testing.assert_allclose(actual, expected, rtol=rtol, atol=atol)

    def matrix_action_el(self, name, profile=model.polynomial_profile, radius=1.0, coupling=1.0):
        """Euler variation from matrix quadrature, not from the reduced formula."""
        amplitude_step, coordinate_step = 2e-5, 2e-4

        def partial(jet, key, index=None):
            samples = []
            for sign in (1, -1):
                shifted = {key: value.copy() if isinstance(value, np.ndarray) else value
                           for key, value in jet.items()}
                if index is None:
                    shifted[key] += sign*amplitude_step
                else:
                    shifted[key][index] += sign*amplitude_step
                result = model.integrated_action(profile=lambda t, z: shifted,
                                                 radius=radius, coupling=coupling)
                samples.append(np.array([result[k] for k in
                                         ("dagger_L", "real_literal_L", "literal_imaginary_L")]))
            return (samples[0]-samples[1])/(2*amplitude_step)

        point = np.array([0.4, -0.2])
        euler = partial(profile(*point), name)
        for mu, direction in enumerate(np.eye(2)):
            plus = partial(profile(*(point+coordinate_step*direction)), "d"+name, mu)
            minus = partial(profile(*(point-coordinate_step*direction)), "d"+name, mu)
            euler -= (plus-minus)/(2*coordinate_step)
        return euler

    def test_polynomial_profile_first_and_second_jets(self):
        x, step = np.array([0.4, -0.2]), 1e-5
        j = model.polynomial_profile(*x)
        for mu, direction in enumerate(np.eye(2)):
            plus, minus = model.polynomial_profile(*(x+step*direction)), model.polynomial_profile(*(x-step*direction))
            for name in ("w", "v"):
                self.assertClose((plus[name]-minus[name])/(2*step), j["d"+name][mu])
                self.assertClose((plus["d"+name]-minus["d"+name])/(2*step), j["dd"+name][mu])

    def test_pulse_jets_are_independent_derivatives(self):
        step, r = 1e-5, 1.7
        for t in (-2, -0.3, 0, 0.4, 2):
            j = model.pulse_profile(t, radius=r)
            plus, minus = model.pulse_profile(t+step, radius=r), model.pulse_profile(t-step, radius=r)
            self.assertClose((plus["w"]-minus["w"])/(2*step), j["dw"][0])
            self.assertClose((plus["dw"]-minus["dw"])/(2*step), j["ddw"][0])

    def test_pulse_is_finite_at_large_times(self):
        for t in (-1000, 1000):
            j = model.pulse_profile(t)
            self.assertTrue(np.isfinite(j["w"]))
            self.assertEqual(j["w"], 0)

    def test_growing_profile_derivative_jets(self):
        point, step = np.array([0.4, -0.2]), 1e-5
        j = model.growing_profile(*point)
        for mu, direction in enumerate(np.eye(2)):
            plus, minus = model.growing_profile(*(point+step*direction)), model.growing_profile(*(point-step*direction))
            self.assertClose((plus["w"]-minus["w"])/(2*step), j["dw"][mu])
            self.assertClose((plus["dw"]-minus["dw"])/(2*step), j["ddw"][mu])

    def test_full_connection_jets_in_all_four_coordinates(self):
        point, step = np.array([0.4, 0.9, 0.4, -0.2]), 1e-5
        d = model.field_data(point)
        for mu, direction in enumerate(np.eye(4)):
            plus, minus = model.field_data(point+step*direction), model.field_data(point-step*direction)
            self.assertClose((plus["connection"]-minus["connection"])/(2*step), d["connection_first"][mu])
            self.assertClose((plus["unitary"]-minus["unitary"])/(2*step), d["unitary_first"][mu])

    def test_unitary_connection_has_both_real_polarizations(self):
        d = model.field_data()
        self.assertNotEqual(d["jet"]["w"], 0)
        self.assertNotEqual(d["jet"]["v"], 0)
        self.assertClose(d["unitary"], -d["unitary"].conj().swapaxes(-1, -2))

    def test_transport_matches_the_two_mode_formula(self):
        d = model.field_data()
        j = d["jet"]
        self.assertClose(d["W"], -j["w"]*d["P_first"]-1j*j["v"]*d["geometric"])
        self.assertClose(d["W"], d["W"].conj().swapaxes(-1, -2))

    def test_angular_curvature_is_quadratic_in_both_polarizations(self):
        d = model.field_data()
        j = d["jet"]
        self.assertClose(d["G"][1, 2], (1-j["w"]**2-j["v"]**2)*0.5j*np.sin(0.9)*(2*d["P"]-np.eye(2)))

    def test_normal_angular_curvature_retains_time_and_space_derivatives(self):
        d = model.field_data()
        for mu, rho in enumerate((0, 3)):
            self.assertClose(d["G"][rho], d["jet"]["dw"][mu]*d["geometric"]
                             +1j*d["jet"]["dv"][mu]*d["P_first"])
        self.assertClose(d["G"][0, 3], 0)

    def test_full_mixed_curvature_is_not_replaced_by_unitary_curvature(self):
        d = model.field_data()
        self.assertClose(d["F"], d["G"]+d["X"])
        self.assertGreater(np.linalg.norm(d["X"]), 0.1)

    def test_full_dynamic_residual_matches_the_closed_formula(self):
        point = [0.2, 1.2, -0.5, 0.3]
        for radius, eta in ((0.7, -0.4), (1, 0), (1.7, 0.7)):
            actual = model.residuals(point, eta=eta, radius=radius)
            expected = model.expected_residuals(point, eta=eta, radius=radius)
            self.assertClose(actual["printed"], expected["printed"])
            self.assertClose(actual["unitary"], expected["unitary"])

    def test_normal_unitary_Gauss_equations_are_not_discarded(self):
        d, r = model.field_data(), model.residuals()
        k, j = 2*d["P"]-np.eye(2), d["jet"]
        for mu, rho in enumerate((0, 3)):
            self.assertClose(r["unitary"][rho], 1j*(j["v"]*j["dw"][mu]-j["w"]*j["dv"][mu])*k)
        self.assertGreater(np.linalg.norm(r["unitary"][[0, 3]]), 0.01)

    def test_printed_normal_Hermitian_part_enforces_nonzero_mode_constraint(self):
        d, r = model.field_data(), model.residuals()
        h = (r["printed"]+r["printed"].conj().swapaxes(-1, -2))/2
        j, k = d["jet"], 2*d["P"]-np.eye(2)
        self.assertClose(h[[0, 3]], 0.7*(j["w"]**2+j["v"]**2)*model.AXIS[[0, 3], None, None]*k)

    def test_null_contraction_would_miss_the_normal_constraint(self):
        r = model.residuals()["printed"]
        hermitian = (r+r.conj().swapaxes(-1, -2))/2
        self.assertGreater(np.linalg.norm(hermitian[[0, 3]]), 0.01)
        self.assertClose(hermitian[0]+hermitian[3], 0)

    def test_projector_pointwise_identity(self):
        d = model.projector_identity()
        self.assertClose(d["trace_P_laplacian"], -d["positive_transport_norm_squared"])
        self.assertGreater(d["positive_transport_norm_squared"], 0)

    def test_projector_identity_is_not_limited_to_symmetric_connection_jets(self):
        rng = np.random.default_rng(821)
        b = rng.normal(size=(2, 2, 2))+1j*rng.normal(size=(2, 2, 2))
        db = rng.normal(size=(2, 2, 2, 2))+1j*rng.normal(size=(2, 2, 2, 2))
        b, db = b-b.conj().swapaxes(-1, -2), db-db.conj().swapaxes(-1, -2)
        d = model.projector_identity(angular_addition=b, angular_first=db, radius=1.7)
        self.assertClose(d["trace_P_laplacian"], -d["positive_transport_norm_squared"])
        self.assertGreater(d["positive_transport_norm_squared"], 1)

    def test_normal_source_trace_obligation_matches_positive_leakage(self):
        r, d = model.residuals(), model.field_data()
        hermitian = (r["printed"]+r["printed"].conj().swapaxes(-1, -2))/2
        norm = model.projector_identity()["positive_transport_norm_squared"]
        for rho in (0, 3):
            self.assertClose(np.trace(d["P"] @ hermitian[rho]), 0.7*model.AXIS[rho]*norm)

    def test_two_mode_transport_norm_is_positive(self):
        d = model.field_data()
        norm = model.projector_identity(radius=2)["positive_transport_norm_squared"]
        self.assertClose(norm, (d["jet"]["w"]**2+d["jet"]["v"]**2)/4)

    def test_full_real_action_load_forces_vanish_after_variation(self):
        r = model.residuals()
        self.assertClose(r["load_force"], 0)
        self.assertClose(r["projector_EL"], 0)
        self.assertClose(r["dagger_unitary_EL"], r["unitary"])
        self.assertClose(r["real_literal_unitary_EL"], -r["unitary"])

    def test_integrated_matrix_action_matches_all_three_reduced_parts(self):
        for radius, coupling, eta in ((1, 1, 0.7), (1.7, 0.8, -0.3)):
            actual = model.integrated_action(radius=radius, coupling=coupling, eta=eta)
            expected = model.reduced_action(model.polynomial_profile(0.4, -0.2), radius, coupling, eta)
            for key in actual:
                self.assertClose(actual[key], expected[key])

    def test_real_actions_are_opposite_only_on_the_declared_null_sector(self):
        d = model.integrated_action()
        self.assertClose(d["real_literal_L"], -d["dagger_L"])
        self.assertGreater(abs(d["literal_imaginary_L"]), 0.1)

    def test_zero_imaginary_action_value_does_not_remove_v_variation(self):
        j, step = model.pulse_profile(0.4), 1e-5
        self.assertClose(model.reduced_action(j)["literal_imaginary_L"], 0)
        plus, minus = {**j, "v": step}, {**j, "v": -step}
        variation = (model.reduced_action(plus)["literal_imaginary_L"]
                     -model.reduced_action(minus)["literal_imaginary_L"])/(2*step)
        self.assertGreater(abs(variation), 1)

    def test_independent_matrix_action_variation_matches_real_mode_equations(self):
        radius, coupling = 1.3, 0.8
        j = model.polynomial_profile(0.4, -0.2)
        height = 1-j["w"]**2-j["v"]**2
        for name in ("w", "v"):
            euler = self.matrix_action_el(name, radius=radius, coupling=coupling)
            expected = 4*np.pi*(-j["dd"+name][0, 0]+j["dd"+name][1, 1]+height*j[name]/radius**2)/coupling**2
            self.assertClose(euler[:2], [expected, -expected], rtol=3e-6, atol=4e-6)

    def test_independent_matrix_imaginary_variation_detects_both_transport_conditions(self):
        j = model.polynomial_profile(0.4, -0.2)
        expected = {"w": 8*np.pi*0.7*sum(j["dv"]), "v": -8*np.pi*0.7*sum(j["dw"])}
        for name in ("w", "v"):
            self.assertClose(self.matrix_action_el(name)[2], expected[name], rtol=3e-6, atol=4e-6)

    def test_independent_pulse_variation_separates_real_and_complex_stationarity(self):
        euler = self.matrix_action_el("v", model.pulse_profile)
        self.assertClose(euler[:2], 0, atol=5e-6)
        self.assertClose(euler[2], -8*np.pi*0.7*model.pulse_profile(0.4)["dw"][0], rtol=3e-6, atol=4e-6)
        self.assertGreater(abs(euler[2]), 1)

    def test_linear_growth_rate_has_the_derived_dispersion(self):
        for radius, k in ((1, 0), (1, 0.4), (2, 0.3)):
            j = model.growing_profile(0.4, -0.2, radius=radius, wavenumber=k)
            self.assertClose(j["ddw"][0, 0]-j["ddw"][1, 1]-j["w"]/radius**2, 0)

    def test_real_full_residual_of_linear_mode_starts_cubically(self):
        amplitudes = (0.08, 0.04, 0.02)
        norms = []
        for epsilon in amplitudes:
            profile = lambda t, z: model.growing_profile(t, z, epsilon=epsilon)
            norms.append(np.linalg.norm(model.residuals(profile=profile)["dagger_unitary_EL"]))
        self.assertClose(norms[0]/norms[1], 8, rtol=2e-5)
        self.assertClose(norms[1]/norms[2], 8, rtol=2e-5)

    def test_printed_complex_angular_residual_detects_linear_growth(self):
        norms = []
        for epsilon in (0.04, 0.02):
            profile = lambda t, z: model.growing_profile(t, z, epsilon=epsilon)
            r = model.residuals(profile=profile)["printed"][1:3]
            hermitian = (r+r.conj().swapaxes(-1, -2))/2
            norms.append(np.linalg.norm(hermitian))
        self.assertClose(norms[0]/norms[1], 2)

    def test_zero_eta_removes_extra_complex_constraints(self):
        r = model.residuals(eta=0)
        self.assertClose(r["printed"], r["unitary"])

    def test_nonzero_eta_constraint_is_not_a_small_damping_perturbation(self):
        j = model.growing_profile(0.4, -0.2)
        self.assertGreater(abs(sum(j["dw"])), 0.01)
        for eta in (1e-3, 0.7):
            expected = model.expected_residuals(profile=model.growing_profile, eta=eta)
            extra = expected["printed"]-expected["unitary"]
            self.assertGreater(np.linalg.norm(extra), 0)

    def test_pulse_solves_the_nonlinear_reduced_equation(self):
        for radius in (0.7, 1, 1.7):
            for t in (-2, -0.4, 0, 0.4, 2):
                j = model.pulse_profile(t, radius=radius)
                self.assertClose(j["ddw"][0, 0], j["w"]*(1-j["w"]**2)/radius**2)

    def test_pulse_solves_all_four_real_gauge_components(self):
        for radius, time in ((0.7, -0.4), (1, 0), (1.7, 0.8)):
            profile = lambda t, z: model.pulse_profile(t, z, radius=radius)
            r = model.residuals([time, 0.9, 0.4, -0.2], profile, radius=radius)
            self.assertLess(np.linalg.norm(r["dagger_unitary_EL"]), 2e-8)
            self.assertLess(np.linalg.norm(r["real_literal_unitary_EL"]), 2e-8)
            self.assertClose(r["projector_EL"], 0)

    def test_pulse_normal_unitary_constraint_is_exactly_satisfied(self):
        r = model.residuals(profile=model.pulse_profile)
        self.assertClose(r["unitary"][[0, 3]], 0)

    def test_same_exact_pulse_fails_printed_complex_equation(self):
        r = model.residuals(profile=model.pulse_profile)
        self.assertGreater(np.linalg.norm(r["printed"]), 2)

    def test_pulse_peak_still_fails_normal_complex_equations(self):
        point = [0, 0.9, 0.4, -0.2]
        r = model.residuals(point, model.pulse_profile)["printed"]
        self.assertLess(np.linalg.norm(r[1:3]), 2e-8)
        self.assertGreater(np.linalg.norm(r[[0, 3]]), 2)

    def test_pulse_reduced_energy_is_conserved(self):
        for radius, coupling in ((1, 1), (1.7, 0.8)):
            for t in (-4, -1, 0, 1, 4):
                j = model.pulse_profile(t, radius=radius)
                energy = 2*np.pi*j["dw"][0]**2/coupling**2+np.pi*(1-j["w"]**2)**2/(coupling**2*radius**2)
                self.assertClose(energy, np.pi/(coupling**2*radius**2))

    def test_exact_trajectory_approaches_closed_background_in_the_past(self):
        self.assertLess(model.pulse_profile(-10)["w"], 0.00013)
        self.assertGreater(model.pulse_profile(0)["w"], 1.4)

    def test_nonzero_transport_norm_is_not_a_unitary_gauge_artifact(self):
        d = model.field_data(profile=model.pulse_profile)
        p = d["P"]
        unitary = np.array([[1, 1j], [1j, 1]])/np.sqrt(2)
        transported = unitary @ d["W"] @ unitary.conj().T
        self.assertClose(np.linalg.norm(transported), np.linalg.norm(d["W"]))
        self.assertClose(unitary @ p @ unitary.conj().T @ transported @ unitary @ p @ unitary.conj().T, 0)
        self.assertGreater(np.linalg.norm(d["W"]), 1)

    def test_pointwise_projector_identity_needs_no_compact_integral(self):
        for theta, phi in ((0.4, -0.7), (0.9, 0.4), (2.4, 1.3)):
            d = model.projector_identity([0.4, theta, phi, -0.2])
            self.assertClose(d["trace_P_laplacian"], -d["positive_transport_norm_squared"])

    def test_invalid_profile_and_derivative_inputs(self):
        with self.assertRaises(ValueError):
            model.mode_jet(0, 0, [0], [0, 0], np.zeros((2, 2)), np.zeros((2, 2)))
        with self.assertRaises(ValueError):
            model.mode_jet(0, 0, [0, 0], [0, 0], [[0, 1], [0, 0]], np.zeros((2, 2)))
        with self.assertRaises(ValueError):
            model.growing_profile(0, 0, wavenumber=1)
        with self.assertRaises(ValueError):
            model.pulse_profile(0, radius=0)
        with self.assertRaises(ValueError):
            model.residuals(step=0)
        with self.assertRaises(ValueError):
            model.field_data([0, 0, 0, 0])
        for nodes in (True, 4, 8.5):
            with self.assertRaises(ValueError):
                model.integrated_action(nodes=nodes)

    def test_invalid_nonsymmetric_connection_controls(self):
        with self.assertRaises(ValueError):
            model.projector_identity(angular_addition=np.ones((2, 2, 2)), angular_first=np.zeros((2, 2, 2, 2)))
        with self.assertRaises(ValueError):
            model.projector_identity(angular_addition=np.zeros((2, 2, 2)), angular_first=np.ones((2, 2, 2, 2)))

    def test_native_field_equation_anchors_remain_present(self):
        source = (ROOT / "sources/research/parts/v470/10_sphaera_and_physics.tex").read_text(encoding="utf-8")
        for label in ("thm:resonance-field-eq", "thm:variational-form", "thm:closed-master-system"):
            self.assertIn("\\label{"+label+"}", source)

    def test_no_native_action_stability_or_metric_is_claimed(self):
        self.assertFalse(self.report["main_TeX_changed"])
        self.assertIn("NOT native C7 stability", self.report["status"])
        self.assertTrue(self.report["constraint_theorem"]["not_a_general_native_or_sourced_superselection_theorem"])
        self.assertTrue(self.report["exact_real_action_pulse"]["not_a_native_on_shell_probe_metric_solution"])
        self.assertTrue(self.report["linearized_dynamics"]["not_damping_of_arbitrary_Cauchy_data"])

    def test_report_reproduces_saved_results(self):
        saved = json.loads((ROOT / "analysis/HC_Null_Axis_Dynamical_Closure.json").read_text(encoding="utf-8"))
        self.assertEqual(self.report, saved)


if __name__ == "__main__":
    unittest.main()
