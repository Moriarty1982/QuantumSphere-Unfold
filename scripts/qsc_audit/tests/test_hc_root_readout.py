"""The quadratic root candidate must not be confused with a native identification."""
from pathlib import Path
import importlib.util
import json
import math
import unittest
from unittest.mock import patch

import numpy as np


ROOT = Path(__file__).resolve().parents[3]
SPEC = importlib.util.spec_from_file_location("hc_root", ROOT / "analysis/HC_Root_Readout.py")
root = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(root)


class HCRootReadoutTests(unittest.TestCase):
    def assertClose(self, actual, expected, atol=3e-12):
        np.testing.assert_allclose(actual, expected, atol=atol, rtol=2e-10)

    def state(self, theta=2.25):
        return 1j*np.array([math.cos(theta/2), math.sin(theta/2)])

    def gram(self, weight=1.0):
        b = root.quadratic_root(self.state(), weight)
        return b @ b/np.vdot(b, b).real

    def test_principal_root_of_a_general_transition_is_explicit(self):
        rng = np.random.default_rng(71)
        a = rng.normal(size=(5, 3))+1j*rng.normal(size=(5, 3))
        b = root.transition_root(a)
        self.assertClose(b @ b, a.conj().T @ a)
        self.assertGreater(np.linalg.eigvalsh(b)[0], 0)

    def test_output_unitary_reversal_is_erased_by_the_gram_root(self):
        witness = root.balanced_hc_clock_witness(self.gram())
        a, j = witness["A"], witness["J"]
        self.assertClose(root.transition_root(j @ a), root.transition_root(a))

    def test_root_balance_is_the_actual_singlet_traceless_condition(self):
        for weight in [0, 0.5, 1]:
            b = root.quadratic_root(self.state(), weight)
            data = root.root_diagnostic(b)
            self.assertAlmostEqual(data["balance_difference"],
                                   data["gram_trace"]-2*data["root_trace"]**2/3)
            self.assertAlmostEqual(data["Koide_ratio"], (1+weight**2)/3)

    def test_circulant_bilinear_basis_is_orthonormal(self):
        basis = [root.E0, root.E1, root.E2]
        comparison = [[np.trace(a.conj().T @ b).real for b in basis] for a in basis]
        self.assertClose(comparison, np.eye(3))
        self.assertClose(root.E1 @ root.E2-root.E2 @ root.E1, np.zeros((3, 3)))
        sigma_x, sigma_z = np.array([[0, 1], [1, 0]]), np.diag([1, -1])
        self.assertGreater(np.linalg.norm(sigma_x @ sigma_z-sigma_z @ sigma_x), 0)

    def test_isometric_weight_is_a_separate_metric_transfer_condition(self):
        for weight in [0.5, 1]:
            basis = [root.E0, weight*root.E1, weight*root.E2]
            comparison = [[np.trace(a.conj().T @ b).real for b in basis] for a in basis]
            self.assertClose(comparison, np.diag([1, weight**2, weight**2]))

    def test_quadratic_coordinate_null_identity(self):
        rng = np.random.default_rng(72)
        for _ in range(20):
            chi = rng.normal(size=2)+1j*rng.normal(size=2)
            x0, x1, x2, x3 = root.quadratic_coordinates(chi)
            self.assertAlmostEqual(x0*x0, x1*x1+x2*x2+x3*x3)

    def test_aligned_antiunitary_odd_residual_has_no_third_bilinear(self):
        chi = root.odd_residual([0.1+0.7j, -0.2+0.4j])
        self.assertClose(chi.conjugate(), -chi)
        self.assertAlmostEqual(root.quadratic_coordinates(chi)[3], 0)

    def test_quadratic_map_is_not_a_linear_HC_output(self):
        chi = self.state()
        self.assertClose(root.quadratic_root(-chi), root.quadratic_root(chi))
        self.assertGreater(np.linalg.norm(root.quadratic_root(chi)), 0)
        self.assertClose((chi+chi.conjugate())/2, np.zeros(2))

    def test_raw_quadratic_map_preserves_a_common_mode_phase(self):
        chi = self.state()
        for alpha in [0.1, 0.7, math.pi/2]:
            self.assertClose(root.quadratic_root(np.exp(1j*alpha)*chi), root.quadratic_root(chi))

    def test_state_amplitude_is_not_an_already_derived_mass_scale(self):
        chi, scale = self.state(), 2.7
        b, changed = root.quadratic_root(chi), root.quadratic_root(scale*chi)
        self.assertClose(changed, scale**2*b)
        self.assertClose(changed @ changed, scale**4*(b @ b))

    def test_generic_complex_mode_deficit_formula_on_the_positive_cone(self):
        rng = np.random.default_rng(73)
        weight = 0.3
        for _ in range(15):
            chi = rng.normal(size=2)+1j*rng.normal(size=2)
            x0, _, _, x3 = root.quadratic_coordinates(chi)
            b = root.quadratic_root(chi, weight)
            self.assertGreater(np.linalg.eigvalsh(b)[0], 0)
            expected = (1+weight**2*(1-(x3/x0)**2))/3
            self.assertAlmostEqual(root.root_diagnostic(b)["Koide_ratio"], expected)

    def test_admitted_odd_modes_with_isometric_readout_obey_Koide(self):
        for theta in [0, 0.1, 2.1, 2.25, 4.2]:
            b = root.quadratic_root(root.odd_residual(self.state(theta)))
            data = root.root_diagnostic(b)
            self.assertAlmostEqual(data["Koide_ratio"], 2/3)
            self.assertAlmostEqual(data["balance_difference"], 0)

    def test_same_odd_HC_state_does_not_fix_the_relative_readout_weight(self):
        ratios = [root.root_diagnostic(root.quadratic_root(self.state(), w))["Koide_ratio"]
                  for w in [0, 0.5, 1]]
        self.assertClose(ratios, [1/3, 5/12, 2/3])

    def test_residual_law_vanishes_on_a_fixed_mode(self):
        fixed = np.array([0.3, 0.7])
        b = root.quadratic_root(root.odd_residual(fixed))
        self.assertClose(b, np.zeros((3, 3)))
        self.assertIsNone(root.root_diagnostic(b)["Koide_ratio"])

    def test_residual_quadratic_law_is_HC_dual_invariant(self):
        state = np.array([0.1+0.7j, 0.2+0.4j])
        opposite = root.antiunitary_reversal(state)
        self.assertClose(root.odd_residual(opposite), -root.odd_residual(state))
        self.assertClose(root.quadratic_root(root.odd_residual(opposite)),
                         root.quadratic_root(root.odd_residual(state)))

    def test_complex_linear_oddness_does_not_eliminate_the_third_bilinear(self):
        chi = np.array([1, 1j])/math.sqrt(2)
        self.assertClose(-np.eye(2) @ chi, -chi)
        self.assertAlmostEqual(root.quadratic_coordinates(chi)[3], 1)
        self.assertAlmostEqual(root.root_diagnostic(root.quadratic_root(chi))["Koide_ratio"], 1/3)

    def test_antiunitary_oddness_without_frame_alignment_does_not_fix_Koide(self):
        v = np.diag([1, 1j])
        chi = v @ self.state()
        self.assertClose(root.antiunitary_reversal(chi, v), -chi)
        self.assertGreater(abs(root.root_diagnostic(root.quadratic_root(chi))["Koide_ratio"]-2/3), 0.1)

    def test_joint_two_mode_frame_transport_restores_the_same_root(self):
        rng = np.random.default_rng(74)
        v, _ = np.linalg.qr(rng.normal(size=(2, 2))+1j*rng.normal(size=(2, 2)))
        chi = self.state()
        changed = root.odd_residual(v @ chi, v)
        self.assertClose(changed, v @ root.odd_residual(chi))
        self.assertClose(root.quadratic_root(changed, frame=v), root.quadratic_root(chi))

    def test_fixed_J_residual_readout_is_not_state_only_global_phase_invariant(self):
        chi = self.state()
        initial = root.quadratic_root(root.odd_residual(chi))
        changed = root.quadratic_root(root.odd_residual(1j*chi))
        self.assertGreater(np.linalg.norm(initial), 0)
        self.assertClose(changed, np.zeros_like(changed))

    def test_joint_phase_frame_change_does_not_change_the_candidate(self):
        chi = self.state()
        v = np.exp(0.7j)*np.eye(2)
        self.assertClose(root.quadratic_root(root.odd_residual(v @ chi, v), frame=v),
                         root.quadratic_root(root.odd_residual(chi)))

    def test_signed_root_outputs_are_not_silently_relabelled_principal_roots(self):
        b = root.quadratic_root([0, 1j])
        self.assertLess(np.linalg.eigvalsh(b)[0], 0)
        with self.assertRaises(ValueError):
            root.root_diagnostic(b)
        principal = root.transition_root(b)
        self.assertGreater(abs(root.root_diagnostic(principal)["Koide_ratio"]-2/3), 0.01)

    def test_quadratic_radius_law_does_not_select_the_phase(self):
        b1, b2 = (root.quadratic_root(self.state(theta)) for theta in [2.1, 2.25])
        self.assertAlmostEqual(root.root_diagnostic(b1)["Koide_ratio"], 2/3)
        self.assertAlmostEqual(root.root_diagnostic(b2)["Koide_ratio"], 2/3)
        self.assertGreater(np.linalg.norm(np.linalg.eigvalsh(b1)-np.linalg.eigvalsh(b2)), 0.01)

    def test_countermodels_keep_the_same_reversal_projector_and_millennium(self):
        first, second = (root.balanced_hc_clock_witness(self.gram(w)) for w in [0, 1])
        for key in ["P", "S", "J", "C", "M"]:
            self.assertClose(first[key], second[key])

    def test_countermodel_clock_is_selfadjoint_with_one_fixed_simple_spectrum(self):
        for weight in [0, 0.5, 1]:
            clock = root.balanced_hc_clock_witness(self.gram(weight))["R"]
            self.assertClose(clock, clock.conj().T)
            self.assertClose(np.linalg.eigvalsh(clock), [1, 2, 3, 4, 6, 8, 10, 11, 12])

    def test_countermodel_seeds_are_closed_odd_and_millennium_closure_is_exact(self):
        model = root.balanced_hc_clock_witness(self.gram())
        p, s, j, m = (model[key] for key in ["P", "S", "J", "M"])
        self.assertClose(s.conj().T @ s, np.eye(3))
        self.assertClose(p @ s, s)
        self.assertClose(j @ s, -s)
        self.assertClose(m @ p-p @ m, np.zeros_like(m))
        self.assertClose(j @ p-p @ j, np.zeros_like(j))

    def test_C_is_an_actual_full_millennium_eigenspace_projector_in_the_witness(self):
        model = root.balanced_hc_clock_witness(self.gram())
        c, m = model["C"], model["M"]
        values, states = np.linalg.eigh(m)
        selected = states[:, np.isclose(values, 1)]
        self.assertEqual(selected.shape[1], 3)
        self.assertClose(selected @ selected.conj().T, c)
        self.assertClose(c @ c, c)
        self.assertClose(m @ c, c)

    def test_countermodel_clock_and_seeds_are_cyclic_compatible(self):
        model = root.balanced_hc_clock_witness(self.gram())
        cycle = np.kron(np.eye(3), root.U)
        self.assertClose(cycle @ model["R"], model["R"] @ cycle)
        self.assertClose(cycle @ model["S"], model["S"] @ root.U)

    def test_countermodel_recovers_the_declared_gram_exactly(self):
        q = self.gram()
        a = root.balanced_hc_clock_witness(q)["A"]
        self.assertClose(a.conj().T @ a, q)

    def test_HC_channel_balance_holds_for_every_seed_not_only_the_total_trace(self):
        q = self.gram()
        model = root.balanced_hc_clock_witness(q)
        a, c, j = model["A"], model["C"], model["J"]
        self.assertClose(a.conj().T @ c @ a, q/2)
        self.assertClose(a.conj().T @ (np.eye(9)-c) @ a, q/2)
        self.assertClose(a.conj().T @ j @ a, np.zeros((3, 3)))

    def test_balanced_HC_projection_rescales_roots_without_fixing_ratios(self):
        model = root.balanced_hc_clock_witness(self.gram(0.5))
        a, c = model["A"], model["C"]
        self.assertClose(root.transition_root(c @ a), root.transition_root(a)/math.sqrt(2))
        self.assertAlmostEqual(root.root_diagnostic(root.transition_root(c @ a))["Koide_ratio"], 5/12)

    def test_stronger_HC_balance_still_admits_incompatible_Koide_values(self):
        report = root.evaluate()["strong_balance_countermodels"]
        self.assertClose([row["Koide_ratio"] for row in report["examples"]], [1/3, 5/12, 2/3])
        self.assertTrue(report["channel_balance_does_not_imply_root_singlet_doublet_balance"])

    def test_frame_covariant_reversal_is_an_antiunitary_involution(self):
        rng = np.random.default_rng(75)
        v, _ = np.linalg.qr(rng.normal(size=(2, 2))+1j*rng.normal(size=(2, 2)))
        chi = np.array([0.3+0.2j, 0.1-0.7j])
        self.assertClose(root.antiunitary_reversal(root.antiunitary_reversal(chi, v), v), chi)
        self.assertClose(root.antiunitary_reversal(1j*chi, v), -1j*root.antiunitary_reversal(chi, v))

    def test_state_and_readout_guards_reject_invalid_data(self):
        for chi, weight in [([1], 1), ([1, np.nan], 1), ([1, 0], -1), ([1, 0], np.inf)]:
            with self.subTest(chi=chi, weight=weight), self.assertRaises(ValueError):
                root.quadratic_root(chi, weight)
        with self.assertRaises(ValueError):
            root.quadratic_root([1, 0], frame=np.diag([1, 2]))
        with self.assertRaises(ValueError):
            root.transition_root(np.eye(2))
        with self.assertRaises(ValueError):
            root.root_diagnostic(np.eye(2))

    def test_countermodel_guards_reject_noncyclic_or_noncontractive_data(self):
        for q in [np.diag([0.1, 0.2, 0.3]), -np.eye(3), 2*np.eye(3), np.eye(2)]:
            with self.subTest(q=q), self.assertRaises(ValueError):
                root.balanced_hc_clock_witness(q)

    def test_native_identification_is_not_faked_with_historical_inputs(self):
        before = root.evaluate()
        with patch.object(root.backreaction.phase.candidate, "HISTORICAL_MASSES_MEV", np.array([1, 2, 3])):
            self.assertEqual(root.evaluate(), before)
        self.assertFalse(before["historical_masses_or_target_phase_used"])
        self.assertTrue(before["quadratic_two_mode_candidate"]["Koide_requires_independent_isometric_readout_eta_one"])
        self.assertTrue(before["source_dictionary"]["native_two_mode_extraction_and_readout_metric_not_evaluated"])

    def test_saved_root_readout_report_reproduces_the_calculation(self):
        saved = json.loads((ROOT / "analysis/HC_Root_Readout.json").read_text(encoding="utf-8"))
        self.assertEqual(saved, root.evaluate())

    def test_density_extension_agrees_with_the_quadratic_map_on_pure_modes(self):
        rng = np.random.default_rng(76)
        for weight in [0, 0.5, 1]:
            for _ in range(8):
                chi = rng.normal(size=2)+1j*rng.normal(size=2)
                rho = np.outer(chi, chi.conj())
                self.assertClose(root.density_root(rho, weight), root.quadratic_root(chi, weight))

    def test_density_extension_is_linear_without_assuming_all_outputs_positive(self):
        rho1 = np.array([[1, 0.2j], [-0.2j, 0.5]])
        rho2 = np.array([[0.3, 0.1], [0.1, 0.7]])
        self.assertClose(root.density_root(2*rho1+3*rho2),
                         2*root.density_root(rho1)+3*root.density_root(rho2))

    def test_normalized_root_forms_are_hermitian_and_sum_to_identity(self):
        for weight in [0, root.FULL_CONE_WEIGHT_BOUND, 1, 2]:
            forms = root.normalized_root_forms(weight)
            self.assertClose(forms.sum(axis=0), np.eye(2))
            self.assertClose(forms, forms.conj().transpose(0, 2, 1))

    def test_root_forms_reproduce_each_fourier_root_in_the_declared_order(self):
        rng = np.random.default_rng(77)
        for weight in [0.3, 1]:
            a = rng.normal(size=(2, 2))+1j*rng.normal(size=(2, 2))
            rho = a @ a.conj().T
            l = root.density_root(rho, weight)
            forms = root.normalized_root_forms(weight)
            expected = [math.sqrt(3)*np.trace(f @ rho).real for f in forms]
            self.assertClose(root.FOURIER.conj().T @ l @ root.FOURIER, np.diag(expected))

    def test_all_root_forms_have_the_exact_two_eigenvalues(self):
        for weight in [0, root.FULL_CONE_WEIGHT_BOUND, 1, 2]:
            expected = [(1-math.sqrt(2)*weight)/3, (1+math.sqrt(2)*weight)/3]
            for form in root.normalized_root_forms(weight):
                self.assertClose(np.linalg.eigvalsh(form), expected)

    def test_full_cone_bound_keeps_arbitrary_positive_density_inputs_positive(self):
        rng = np.random.default_rng(78)
        for weight in [0, 0.4, root.FULL_CONE_WEIGHT_BOUND]:
            for _ in range(25):
                a = rng.normal(size=(2, 2))+1j*rng.normal(size=(2, 2))
                self.assertGreaterEqual(np.linalg.eigvalsh(root.density_root(a @ a.conj().T, weight))[0], -1e-12)
            self.assertClose(root.density_root(np.zeros((2, 2)), weight), np.zeros((3, 3)))

    def test_the_positivity_bound_is_sharp_even_for_aligned_odd_inputs(self):
        chi = np.array([0, 1j])
        self.assertClose(root.antiunitary_reversal(chi), -chi)
        for weight in [root.FULL_CONE_WEIGHT_BOUND+1e-6, 1, 2]:
            expected = (1-math.sqrt(2)*weight)/math.sqrt(3)
            self.assertAlmostEqual(np.linalg.eigvalsh(root.quadratic_root(chi, weight))[0], expected)
            self.assertLess(expected, 0)

    def test_globally_positive_family_cannot_reach_a_ratio_above_one_half(self):
        rng = np.random.default_rng(79)
        for weight in [0, 0.3, root.FULL_CONE_WEIGHT_BOUND]:
            for _ in range(20):
                a = rng.normal(size=(2, 2))+1j*rng.normal(size=(2, 2))
                data = root.root_diagnostic(root.density_root(a @ a.conj().T, weight))
                self.assertGreaterEqual(data["Koide_ratio"], 1/3-1e-12)
                self.assertLessEqual(data["Koide_ratio"], 0.5+1e-12)
        saturated = root.quadratic_root(self.state(), root.FULL_CONE_WEIGHT_BOUND)
        self.assertAlmostEqual(root.root_diagnostic(saturated)["Koide_ratio"], 0.5)

    def test_metric_isometry_and_full_cone_positivity_have_no_common_weight(self):
        for weight in [0, 0.5, root.FULL_CONE_WEIGHT_BOUND, 1, 2]:
            comparison = np.diag([1, weight**2, weight**2])
            isometry = np.allclose(comparison, np.eye(3))
            positive_forms = np.linalg.eigvalsh(root.normalized_root_forms(weight)).min() >= -1e-12
            self.assertFalse(isometry and positive_forms)

    def test_boundary_weight_has_an_exact_zero_root_for_the_extremal_mode(self):
        l = root.quadratic_root([0, 1j], root.FULL_CONE_WEIGHT_BOUND)
        self.assertClose(np.linalg.eigvalsh(l), [0, math.sqrt(3)/2, math.sqrt(3)/2])
        self.assertAlmostEqual(root.root_diagnostic(l)["Koide_ratio"], 0.5)

    def test_aligned_angle_formula_matches_the_direct_matrix(self):
        for weight in [0, 0.8, 1, 1.5]:
            for theta in np.linspace(0, 2*math.pi, 19):
                l = root.quadratic_root(self.state(theta), weight)
                direct = root.FOURIER.conj().T @ l @ root.FOURIER
                self.assertClose(direct, np.diag(root.aligned_root_eigenvalues(theta, weight)))

    def test_general_aligned_chamber_formula_matches_the_positive_cone(self):
        for weight in [0, root.FULL_CONE_WEIGHT_BOUND, 0.8, 1, 1.3, math.sqrt(2), 1.5]:
            half_width = root.aligned_chamber_half_width(weight)
            for theta in np.linspace(-2*math.pi, 2*math.pi, 257):
                distance = abs((theta+math.pi/3) % (2*math.pi/3)-math.pi/3)
                expected = half_width is not None and distance <= half_width+1e-12
                actual = np.min(root.aligned_root_eigenvalues(theta, weight)) >= -1e-12
                self.assertEqual(actual, expected, (weight, theta))

    def test_isometric_chambers_cover_exactly_one_quarter_of_the_angle_circle(self):
        half_width = root.aligned_chamber_half_width()
        self.assertAlmostEqual(half_width, math.pi/12)
        self.assertAlmostEqual(3*2*half_width/(2*math.pi), 1/4)

    def test_isometric_chamber_edges_are_zero_roots_and_exterior_is_negative(self):
        half_width = math.pi/12
        for center in 2*math.pi*np.arange(3)/3:
            for sign in [-1, 1]:
                edge = center+sign*half_width
                self.assertAlmostEqual(np.min(root.aligned_root_eigenvalues(edge)), 0)
                self.assertGreater(np.min(root.aligned_root_eigenvalues(edge-sign*1e-5)), 0)
                self.assertLess(np.min(root.aligned_root_eigenvalues(edge+sign*1e-5)), 0)

    def test_positive_isometric_pure_odd_modes_are_not_closed_under_superposition(self):
        left = 1j*np.array([0.5, math.sqrt(3)/2])
        right = 1j*np.array([-0.5, math.sqrt(3)/2])
        for chi in [left, right]:
            self.assertGreater(np.linalg.eigvalsh(root.quadratic_root(chi))[0], 0)
        self.assertLess(np.linalg.eigvalsh(root.quadratic_root(left+right))[0], 0)
        self.assertClose(root.antiunitary_reversal(left+right), -(left+right))

    def test_incoherent_density_mixing_is_not_coherent_mode_superposition(self):
        left = 1j*np.array([0.5, math.sqrt(3)/2])
        right = 1j*np.array([-0.5, math.sqrt(3)/2])
        density_sum = np.outer(left, left.conj())+np.outer(right, right.conj())
        l = root.density_root(density_sum)
        self.assertGreater(np.linalg.eigvalsh(l)[0], 0)
        self.assertClose(l, root.quadratic_root(left)+root.quadratic_root(right))
        self.assertGreater(np.linalg.norm(l-root.quadratic_root(left+right)), 0.1)

    def test_absolute_value_repair_changes_the_exact_koide_ratio(self):
        signed = root.quadratic_root([0, 1j])
        principal = root.transition_root(signed)
        self.assertAlmostEqual(root.root_diagnostic(principal)["Koide_ratio"], 6/(1+2*math.sqrt(2))**2)
        self.assertLess(root.root_diagnostic(principal)["Koide_ratio"], 2/3)

    def test_nonzero_constant_angular_drift_exits_an_isometric_chamber(self):
        for sign in [-1, 1]:
            theta_before = sign*(math.pi/12-0.01)
            theta_after = theta_before+sign*0.02
            self.assertGreater(np.min(root.aligned_root_eigenvalues(theta_before)), 0)
            self.assertLess(np.min(root.aligned_root_eigenvalues(theta_after)), 0)

    def test_cyclic_coefficient_symmetry_does_not_equate_metric_weights(self):
        angle = 2*math.pi/3
        d = np.array([[1, 0, 0], [0, math.cos(angle), -math.sin(angle)],
                      [0, math.sin(angle), math.cos(angle)]])
        for singlet, doublet in [(1, 1), (2, 7), (8, 0.5)]:
            comparison = np.diag([singlet, doublet, doublet])
            self.assertClose(d.T @ comparison @ d, comparison)
            a, b = doublet, (singlet-doublet)/3
            basis = [root.E0, root.E1, root.E2]
            trace_form = [[(a*np.trace(x @ y)+b*np.trace(x)*np.trace(y)).real
                           for y in basis] for x in basis]
            self.assertClose(trace_form, comparison)

    def test_cyclic_average_has_two_independent_positive_metric_weights(self):
        angle = 2*math.pi/3
        d = np.array([[1, 0, 0], [0, math.cos(angle), -math.sin(angle)],
                      [0, math.sin(angle), math.cos(angle)]])
        a = np.array([[1, 2, 3], [0, 4, 5], [0, 0, 6]])
        comparison = a.T @ a
        average = sum(np.linalg.matrix_power(d, k).T @ comparison @ np.linalg.matrix_power(d, k)
                      for k in range(3))/3
        expected = np.diag([comparison[0, 0], np.trace(comparison[1:, 1:])/2,
                            np.trace(comparison[1:, 1:])/2])
        self.assertClose(average, expected)
        self.assertNotAlmostEqual(average[0, 0], average[1, 1])

    def test_slot_cycle_conjugation_is_not_the_coefficient_plane_rotation(self):
        for e in [root.E0, root.E1, root.E2]:
            self.assertClose(root.U @ e @ root.U.conj().T, e)

    def test_joint_passive_frame_covariance_holds_for_arbitrary_metric_weights(self):
        frame = np.diag([1, 1j])
        for weight in [0.3, root.FULL_CONE_WEIGHT_BOUND, 1]:
            chi = self.state()
            changed = root.odd_residual(frame @ chi, frame)
            self.assertClose(root.quadratic_root(changed, weight, frame=frame), root.quadratic_root(chi, weight))

    def test_density_and_positivity_helpers_reject_invalid_data(self):
        for density in [np.eye(3), np.diag([1, -1]), [[1, 1j], [0, 1]], [[1, 0], [0, np.nan]]]:
            with self.subTest(density=density), self.assertRaises(ValueError):
                root.density_root(density)
        for weight in [-1, math.inf, math.nan]:
            for operation in [root.normalized_root_forms, root.aligned_chamber_half_width]:
                with self.subTest(weight=weight, operation=operation), self.assertRaises(ValueError):
                    operation(weight)
            with self.assertRaises(ValueError):
                root.density_root(np.eye(2), weight)
        with self.assertRaises(ValueError):
            root.aligned_root_eigenvalues(math.nan)
        with self.assertRaises(ValueError):
            root.aligned_root_eigenvalues(0, -1)

    def test_report_scopes_the_positive_cone_obstruction_to_this_candidate(self):
        data = root.evaluate()
        obstruction = data["full_cone_positivity_obstruction"]
        self.assertAlmostEqual(obstruction["max_relative_weight"], 1/math.sqrt(2))
        self.assertEqual(obstruction["max_Koide_ratio_for_this_globally_positive_family"], 0.5)
        self.assertTrue(obstruction["isometric_eta_one_is_outside_this_bound"])
        self.assertTrue(data["restricted_isometric_cone"]["native_domain_and_invariance_not_derived"])
        self.assertTrue(data["comparison_tensor_freedom"]["declaring_the_pullback_metric_is_not_a_prediction_of_eta"])
        self.assertFalse(data["main_TeX_changed"])
