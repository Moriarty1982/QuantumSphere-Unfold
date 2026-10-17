"""Existing eta load: exact penalties, null stress, static residual and real-form controls."""
import importlib.util
import json
from pathlib import Path
import unittest

import numpy as np


ROOT = Path(__file__).resolve().parents[3]
SPEC = importlib.util.spec_from_file_location(
    "load_stability", ROOT / "analysis/HC_Closure_Load_Stability.py")
model = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(model)


class HCClosureLoadStabilityTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.report = model.evaluate()

    def assertClose(self, actual, expected, rtol=3e-8, atol=3e-10):
        np.testing.assert_allclose(actual, expected, rtol=rtol, atol=atol)

    def test_native_load_and_penalty_anchors(self):
        source = (ROOT / "sources/research/parts/v470/10_sphaera_and_physics.tex").read_text(encoding="utf-8")
        for label in ("thm:variational-form", "thm:closed-master-system", "thm:resonance-field-eq"):
            self.assertIn("\\label{"+label+"}", source)
        self.assertIn("\\eta\\,(\\mathbf 1-\\hat P_{C_7})", source)

    def test_both_native_penalties_vanish_on_closed_matching_data(self):
        for alpha in (0, 0.8, 1, 1.2, 2):
            d = model.probe_penalty_and_leakage(alpha)
            self.assertLess(d["U_C7_unit_coefficient"], 1e-28)
            self.assertLess(d["H_equals_Lambda_norm"], 1e-28)
            self.assertEqual(d["U_HC_on_matching_branch"], 0)

    def test_leakage_exists_despite_zero_amplitude_penalties(self):
        d = model.probe_penalty_and_leakage(0.8)
        self.assertClose(d["normal_operator_norm_squared"], 0.08)
        self.assertGreater(d["normal_operator_norm_squared"], 0)

    def test_normal_leakage_is_independent_of_eta(self):
        for eta in (-2, 0, 0.7, 3):
            self.assertClose(model.probe_penalty_and_leakage(0.8, eta)["normal_operator_norm_squared"], 0.08)

    def test_normal_leakage_radius_and_alpha_scaling(self):
        for radius, alpha in ((0.5, 0.7), (1, 1), (2, 1.3)):
            d = model.probe_penalty_and_leakage(alpha, radius=radius)
            self.assertClose(d["normal_operator_norm_squared"], 2*(1-alpha)**2/radius**2)

    def test_native_load_commutes_with_the_projector(self):
        d = model.product_data(alpha=0.8)
        self.assertClose(model.commutator(d["connection"]-d["unitary_connection"], d["P"]), 0)

    def test_full_connection_retains_both_Hermiticity_parts(self):
        d = model.product_data(alpha=0.8)
        b, u = d["connection"], d["unitary_connection"]
        self.assertClose((b-b.conj().swapaxes(-1, -2))/2, u)
        self.assertClose((b+b.conj().swapaxes(-1, -2))/2, b-u)
        self.assertGreater(np.linalg.norm(b+b.conj().swapaxes(-1, -2)), 1)

    def test_full_connection_first_derivative(self):
        angles, step = np.array([0.9, 0.4]), 1e-5
        d = model.product_data(*angles, alpha=0.8)
        for index, e in enumerate(np.eye(2)):
            plus = model.product_data(*(angles+step*e), alpha=0.8)
            minus = model.product_data(*(angles-step*e), alpha=0.8)
            self.assertClose((plus["connection"]-minus["connection"])/(2*step),
                             d["connection_first"][index+1])

    def test_full_curvature_decomposes_exactly(self):
        for alpha, eta in ((0, 0.7), (0.8, -0.4), (1, 2), (2, 0.7)):
            d = model.product_data(alpha=alpha, eta=eta)
            self.assertClose(d["curvature"], d["unitary_curvature"]+d["load_curvature"])

    def test_load_curvature_is_Hermitian(self):
        f = model.product_data(alpha=0.8)["load_curvature"]
        self.assertClose(f, f.conj().swapaxes(-1, -2))

    def test_full_curvature_is_antisymmetric(self):
        f = model.product_data(alpha=0.8)["curvature"]
        self.assertClose(f, -f.swapaxes(0, 1))

    def test_nonzero_load_curvature_at_old_flat_unitary_endpoints(self):
        for alpha in (0, 2):
            d = model.product_data(alpha=alpha)
            self.assertClose(d["unitary_curvature"], 0)
            self.assertGreater(np.linalg.norm(d["curvature"]), 1)

    def test_compatible_background_has_zero_load_curvature(self):
        for eta in (-3, 0, 2):
            self.assertClose(model.product_data(eta=eta)["load_curvature"], 0)

    def test_null_axis_and_transversality(self):
        d = model.product_data(alpha=0.8)
        n_up = model.inverse_metric()*d["axis"]
        self.assertClose(n_up @ d["axis"], 0)
        self.assertClose(np.einsum("m,mij->ij", n_up, d["projector_transport"]), 0)

    def test_nonzero_load_has_zero_Lorentz_scalar_in_both_pairings(self):
        f = model.product_data(alpha=0.8)["load_curvature"]
        for pairing in ("literal", "dagger"):
            self.assertClose(model.curvature_density(f, model.inverse_metric(), pairing=pairing), 0)

    def test_static_Lorentz_contraction_is_independent_of_eta(self):
        for eta in (0, 0.7, 2):
            d = model.surface_action(0.8, eta)
            self.assertClose(d["plus_dagger_contraction"], np.pi*0.96**2)
            self.assertClose(d["minus_literal_contraction"], np.pi*0.96**2)
            self.assertClose(d["literal_imaginary_part"], 0)

    def test_load_stress_is_explicitly_nonzero_despite_zero_scalar(self):
        d = model.product_data(alpha=0.8)
        t = model.dagger_stress(d["load_curvature"], model.inverse_metric())
        self.assertClose(t, 0.7**2*0.2**2*np.outer(model.NULL_AXIS, model.NULL_AXIS))
        self.assertGreater(t[0, 0], 0)

    def test_load_stress_is_traceless_and_null_directed(self):
        d = model.product_data(alpha=0.8)
        inv = model.inverse_metric()
        t = model.dagger_stress(d["load_curvature"], inv)
        self.assertClose(np.dot(inv, np.diag(t)), 0)
        self.assertClose(t @ (inv*model.NULL_AXIS), 0)
        self.assertEqual(np.linalg.matrix_rank(t, tol=1e-12), 1)

    def test_load_stress_radius_and_coupling_scaling(self):
        d = model.product_data(alpha=0.8)
        t = model.dagger_stress(d["load_curvature"], model.inverse_metric(radius=2), coupling=3)
        self.assertClose(t[0, 0], 0.7**2*0.2**2/36)

    def test_integrated_null_load_stress_matches_analytic_value(self):
        d = model.surface_action(0.8, 0.7, radius=2, coupling=3)
        self.assertClose(d["dagger_load_T00_integral"], 4*np.pi*0.7**2*0.2**2/9)

    def test_dagger_stress_matches_independent_inverse_metric_variation(self):
        d, inv = model.product_data(alpha=0.8), model.inverse_metric()
        f = d["load_curvature"]
        t = model.dagger_stress(f, inv)
        step = 1e-5
        base_l = -model.curvature_density(f, inv).real
        for mu, e in enumerate(np.eye(4)):
            plus = -model.curvature_density(f, inv+step*e).real
            minus = -model.curvature_density(f, inv-step*e).real
            self.assertClose(-2*(plus-minus)/(2*step)+base_l/inv[mu], t[mu, mu])

    def test_projector_divergence_has_quadratic_not_linear_order(self):
        for alpha in (0, 0.8, 1, 1.2, 2):
            d = model.product_data(alpha=alpha)
            self.assertClose(model.projector_divergence(alpha=alpha, radius=2),
                             -(1-alpha)**2*(2*d["P"]-np.eye(2))/4)

    def test_full_printed_static_equation_matches_curved_coordinate_differentiation(self):
        for alpha, eta in ((0, 0.7), (0.8, -0.4), (1, 2), (1.2, 0.7), (2, 0.7)):
            actual = model.static_residual(alpha=alpha, eta=eta, radius=1.7)
            expected = model.expected_static_residual(alpha=alpha, eta=eta, radius=1.7)
            self.assertClose(actual, expected)

    def test_background_solves_printed_source_free_connection_equation(self):
        for theta, phi in ((0.6, -0.3), (0.9, 0.4), (2.4, 1.2)):
            self.assertLess(np.linalg.norm(model.static_residual(theta, phi)), 2e-8)

    def test_restored_flat_unitary_endpoints_are_not_source_free_full_solutions(self):
        for alpha in (0, 2):
            self.assertGreater(np.linalg.norm(model.static_residual(alpha=alpha)), 1)

    def test_angular_printed_residual_is_independent_of_eta(self):
        reference = model.static_residual(alpha=0.8, eta=0)[1:3]
        for eta in (-2, 0.7, 3):
            self.assertClose(model.static_residual(alpha=0.8, eta=eta)[1:3], reference)

    def test_normal_printed_residual_is_quadratic_in_leakage(self):
        norms = [np.linalg.norm(model.static_residual(alpha=1-delta)[[0, 3]])
                 for delta in (0.1, 0.05, 0.025)]
        self.assertClose(norms[0]/norms[1], 4)
        self.assertClose(norms[1]/norms[2], 4)

    def test_general_real_Euclidean_axis_gives_the_derived_energy(self):
        axis = np.array([2.0, 0, 0, -0.5])
        r, g, eta, alpha = 1.7, 0.8, 0.6, 0.8
        d = model.surface_action(alpha, eta, r, g, axis, "Euclidean")
        ym = np.pi*(2*alpha-alpha**2)**2/(g*g*r*r)
        load = 2*np.pi*eta*eta*np.dot(axis, axis)*(1-alpha)**2/(g*g)
        self.assertClose(d["plus_dagger_contraction"], ym+load)
        self.assertClose(d["minus_literal_contraction"], ym-load)

    def test_real_Euclidean_dagger_Hessian_threshold(self):
        step = 1e-3
        for eta in (0, 0.7, 1):
            energies = [model.surface_action(1+s, eta, signature="Euclidean")["plus_dagger_contraction"]
                        for s in (-step, 0, step)]
            second = (energies[2]-2*energies[1]+energies[0])/step**2
            self.assertClose(second, 4*np.pi*(2*eta*eta-1), rtol=2e-6, atol=7e-6)

    def test_threshold_equality_is_quartic_along_the_selected_path(self):
        eta = 1/np.sqrt(2)
        differences = [model.surface_action(1+s, eta, signature="Euclidean")["plus_dagger_contraction"]-np.pi
                       for s in (0.2, 0.1)]
        self.assertClose(differences, [np.pi*0.2**4, np.pi*0.1**4])
        self.assertClose(differences[0]/differences[1], 16)

    def test_no_dagger_Euclidean_control_strengthens_negative_curvature(self):
        step, eta = 1e-3, 0.7
        energies = [model.surface_action(1+s, eta, signature="Euclidean")["minus_literal_contraction"]
                    for s in (-step, 0, step)]
        second = (energies[2]-2*energies[1]+energies[0])/step**2
        self.assertClose(second, -4*np.pi*(1+2*eta*eta), rtol=1e-6)
        self.assertLess(second, -4*np.pi)

    def test_zero_eta_recovers_previous_global_energy(self):
        for alpha in (0, 0.8, 1, 1.2, 2):
            previous = model.flux.surface_integrals(alpha=alpha)["energy"]
            self.assertClose(model.surface_action(alpha, 0)["plus_dagger_contraction"], previous)

    def test_invalid_inputs_are_rejected(self):
        for kwargs in ({"eta": np.nan}, {"axis": [1, 1, 0, 1]}, {"axis": [1, 0, 0]}):
            with self.assertRaises(ValueError):
                model.product_data(**kwargs)
        for kwargs in ({"radius": 0}, {"signature": "other"}, {"theta": 0}):
            with self.assertRaises(ValueError):
                model.inverse_metric(**kwargs)
        for nodes in (True, 4, 8.5):
            with self.assertRaises(ValueError):
                model.surface_action(nodes=nodes)
        with self.assertRaises(ValueError):
            model.static_residual(step=0)
        with self.assertRaises(ValueError):
            model.expected_static_residual(axis=[1, 0, 0, 0])
        with self.assertRaises(ValueError):
            model.curvature_density(model.product_data()["curvature"], [0, 1, 1, 1])
        with self.assertRaises(ValueError):
            model.curvature_density(model.product_data()["curvature"], model.inverse_metric(), pairing="other")

    def test_no_native_stability_Wick_or_VSI_identification_is_claimed(self):
        self.assertFalse(self.report["main_TeX_changed"])
        self.assertIn("NOT a full native stability", self.report["status"])
        self.assertTrue(self.report["Euclidean_real_axis_comparison"]["not_a_derived_Wick_rotation"])
        self.assertTrue(self.report["printed_complex_resonance"]["not_a_complete_hyperbolic_stability_analysis"])
        self.assertTrue(self.report["not_claimed_to_be_a_universal_or_VSI_Yang_Mills_solution"])

    def test_report_reproduces_saved_results(self):
        saved = json.loads((ROOT / "analysis/HC_Closure_Load_Stability.json").read_text(encoding="utf-8"))
        self.assertEqual(self.report, saved)


if __name__ == "__main__":
    unittest.main()
