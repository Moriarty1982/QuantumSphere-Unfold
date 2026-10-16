"""Full parent variation, curved derived-coordinate branch and native HC obstruction."""
import importlib.util
import json
from pathlib import Path
import unittest

import numpy as np


ROOT = Path(__file__).resolve().parents[3]
SPEC = importlib.util.spec_from_file_location("derived_curved_parent", ROOT / "analysis/HC_Derived_Background_Curved_Parent.py")
parent = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(parent)


class HCDerivedBackgroundCurvedParentTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.point = np.array([0.01, 0.02, -0.03, 0.01])
        cls.branch = parent.evaluate_branch(cls.point)

    def setUp(self):
        self.rng = np.random.default_rng(361)

    def assertClose(self, actual, expected, atol=5e-11):
        np.testing.assert_allclose(actual, expected, atol=atol, rtol=3e-8)

    def test_first_probe_jets_match_the_existing_exact_solution(self):
        bg, jets = parent.probe_jets(self.point)
        self.assertClose(jets[0], bg["psi"])
        self.assertClose(jets[1], bg["derivatives"])

    def test_second_probe_jets_match_finite_differences(self):
        _, jets = parent.probe_jets(self.point)
        step = 1e-6
        for mu, delta in enumerate(step*np.eye(4)):
            plus, minus = parent.probe_jets(self.point+delta)[1], parent.probe_jets(self.point-delta)[1]
            self.assertClose(jets[2][mu], (plus[1]-minus[1])/(2*step), atol=2e-9)

    def test_third_probe_jets_match_finite_differences(self):
        _, jets = parent.probe_jets(self.point)
        step = 1e-6
        for mu, delta in enumerate(step*np.eye(4)):
            plus, minus = parent.probe_jets(self.point+delta)[1], parent.probe_jets(self.point-delta)[1]
            self.assertClose(jets[3][mu], (plus[2]-minus[2])/(2*step), atol=5e-9)

    def test_multiple_spatial_probe_derivatives_vanish_for_the_affine_class(self):
        _, jets = parent.probe_jets(self.point)
        self.assertClose(jets[2][1:, 1:], np.zeros((3, 3, 3, 4)))
        self.assertClose(jets[3][1:, 1:], np.zeros((3, 3, 4, 3, 4)))

    def test_cross_coordinate_gradient_matches_the_prepared_coframe(self):
        bg, y = parent.coordinate_jets(self.point)
        self.assertClose(y[1].T, bg["symmetric_cross_coframe"])

    def test_art_coordinate_gradient_matches_its_channel_coframe(self):
        bg, y = parent.coordinate_jets(self.point, "ART")
        self.assertClose(y[1].T, bg["coframes"][0])

    def test_coordinate_hessians_and_third_jets_are_symmetric(self):
        y = self.branch["coordinate_jets"]
        self.assertClose(y[2], y[2].swapaxes(0, 1))
        self.assertClose(y[3], y[3].swapaxes(0, 2))

    def test_coordinate_higher_derivatives_match_independent_differences(self):
        y, step = self.branch["coordinate_jets"], 1e-6
        for mu, delta in enumerate(step*np.eye(4)):
            plus = parent.coordinate_jets(self.point+delta)[1]
            minus = parent.coordinate_jets(self.point-delta)[1]
            self.assertClose(y[2][mu], (plus[1]-minus[1])/(2*step), atol=2e-9)
            self.assertClose(y[3][mu], (plus[2]-minus[2])/(2*step), atol=2e-8)

    def test_degenerate_initial_cross_patch_is_rejected(self):
        with self.assertRaises(ValueError):
            parent.coordinate_jets([0, 0, 0, 0])

    def test_metric_is_the_exact_null_pullback_coframe_metric(self):
        branch = self.branch
        expected = branch["coframe"].T @ parent.geometry.ETA @ branch["coframe"]
        self.assertClose(branch["metric_jets"]["metric"], expected)

    def test_metric_first_jets_match_independent_differences(self):
        step = 1e-6
        for mu, delta in enumerate(step*np.eye(4)):
            plus, minus = parent.evaluate_branch(self.point+delta), parent.evaluate_branch(self.point-delta)
            numerical = (plus["metric_jets"]["metric"]-minus["metric_jets"]["metric"])/(2*step)
            self.assertClose(self.branch["metric_jets"]["first"][mu], numerical, atol=2e-8)

    def test_metric_second_jets_match_independent_differences(self):
        step = 1e-6
        for mu, delta in enumerate(step*np.eye(4)):
            plus, minus = parent.evaluate_branch(self.point+delta), parent.evaluate_branch(self.point-delta)
            numerical = (plus["metric_jets"]["first"]-minus["metric_jets"]["first"])/(2*step)
            self.assertClose(self.branch["metric_jets"]["second"][mu], numerical, atol=5e-7)

    def test_independent_levi_civita_einstein_tensor_matches_the_pullback(self):
        self.assertClose(self.branch["direct_geometry"]["einstein"], self.branch["expected_Einstein"], atol=5e-10)

    def test_direct_scalar_stress_matches_the_tensor_pullback(self):
        self.assertClose(self.branch["scalar"]["stress"], self.branch["expected_stress"])

    def test_all_independent_einstein_components_match_not_only_a_null_contraction(self):
        self.assertClose(self.branch["Einstein_residual"], np.zeros((4, 4)), atol=5e-10)

    def test_coframe_multiplier_equation_is_satisfied_at_zero_multiplier(self):
        self.assertClose(self.branch["coframe_EL_density"], np.zeros((4, 4)), atol=5e-11)

    def test_full_coframe_constraint_is_satisfied(self):
        self.assertClose(self.branch["coframe_constraint"], np.zeros((4, 4)))

    def test_derived_axis_is_exact_and_null_in_the_effective_metric(self):
        y = self.branch["coordinate_jets"]
        q = y[1] @ parent.geometry.N_COV
        q_first = np.einsum("a,lsa->ls", parent.geometry.N_COV, y[2])
        self.assertClose(q_first-q_first.T, np.zeros((4, 4)))
        self.assertClose(q @ np.linalg.solve(self.branch["metric_jets"]["metric"], q), 0)

    def test_derived_axis_is_parallel_on_the_transverse_null_branch(self):
        y = self.branch["coordinate_jets"]
        q = y[1] @ parent.geometry.N_COV
        partial = np.einsum("a,lsa->ls", parent.geometry.N_COV, y[2])
        connection = self.branch["direct_geometry"]["connection"]
        self.assertClose(partial-np.einsum("a,alm->lm", q, connection), np.zeros((4, 4)), atol=2e-9)

    def test_h_and_axis_potential_equations_are_both_satisfied(self):
        self.assertClose(self.branch["scalar"]["h_EL"], 0)
        self.assertClose(self.branch["scalar"]["u_EL"], 0)

    def test_independent_axis_reaction_is_not_set_to_zero_by_hand(self):
        reaction = self.branch["scalar"]["axis_reaction_if_independent"]
        self.assertGreater(np.linalg.norm(reaction), 0.1)
        self.assertClose(self.branch["scalar"]["u_EL"], 0)

    def test_curvature_is_nonzero_despite_zero_scalar_curvature(self):
        self.assertGreater(np.linalg.norm(self.branch["direct_geometry"]["lower_riemann"]), 1e-9)
        self.assertClose(self.branch["direct_geometry"]["scalar"], 0, atol=2e-9)

    def test_both_supported_readouts_have_joint_local_branches(self):
        for readout in ["ART", "symmetric_cross"]:
            branch = parent.evaluate_branch(self.point, readout)
            self.assertClose(branch["scalar"]["h_EL"], 0)
            self.assertClose(branch["scalar"]["u_EL"], 0)
            self.assertClose(branch["Einstein_residual"], np.zeros((4, 4)), atol=5e-10)

    def test_massive_coupled_reference_probes_remain_on_shell_on_the_joint_branch(self):
        self.assertClose(self.branch["background"]["reference_residual"], np.zeros((3, 4)))
        self.assertGreater(np.linalg.norm(self.branch["background"]["mass_operator"]), 1)

    def test_total_reference_current_stays_conserved(self):
        self.assertClose(np.sum(self.branch["background"]["channel_divergence"]), 0)

    def test_readout_probe_source_has_the_correct_wirtinger_factors(self):
        psi = self.branch["background"]["psi"]
        weights = self.branch["background"]["weights"]
        variation = self.rng.normal(size=psi.shape)+1j*self.rng.normal(size=psi.shape)
        w = self.rng.normal(size=4)
        step = 1e-6
        for readout in ["ART", "symmetric_cross"]:
            def action(p):
                left, right = (0, 0) if readout == "ART" else (0, 1)
                return sum(a*np.vdot(p[left], k @ p[right]).real/2 for a, k in zip(w, weights))
            numerical = (action(psi+step*variation)-action(psi-step*variation))/(2*step)
            source = parent.readout_probe_source(psi, weights, w, readout)
            self.assertClose(numerical, 2*np.vdot(variation, source).real, atol=3e-10)

    def test_nonzero_off_shell_readout_coefficient_generates_a_real_probe_force(self):
        source = parent.readout_probe_source(self.branch["background"]["psi"],
                                             self.branch["background"]["weights"], [1, 0, 0, 0])
        self.assertGreater(np.linalg.norm(source), 0.01)

    def test_zero_multipliers_remove_the_readout_force_on_this_branch(self):
        source = parent.readout_probe_source(self.branch["background"]["psi"],
                                             self.branch["background"]["weights"], np.zeros(4))
        self.assertClose(source, np.zeros((3, 4)))

    def test_scalar_h_and_u_equations_match_independent_periodic_action_variations(self):
        count, coupling, step = 16, 0.4, 1e-6
        x, y = np.meshgrid(np.arange(count)*2*np.pi/count, np.arange(count)*2*np.pi/count, indexing="ij")
        h, u = np.sin(x)+0.3*np.cos(y)+0.2*np.sin(x+y), np.cos(x)+0.4*np.sin(y)+0.1*np.cos(x-y)
        dh, du = np.cos(2*x)+0.2*np.sin(x-y), np.sin(2*y)+0.3*np.cos(x+y)
        frequencies = np.fft.fftfreq(count, d=1/count)

        def derivative(f, axis):
            shape = [1, 1]
            shape[axis] = count
            return np.fft.ifft(1j*frequencies.reshape(shape)*np.fft.fft(f, axis=axis), axis=axis).real

        def jets(f):
            p, pp = np.zeros((count, count, 4)), np.zeros((count, count, 4, 4))
            for i in range(2):
                p[:, :, i+1] = derivative(f, i)
                for j in range(2):
                    pp[:, :, i+1, j+1] = derivative(derivative(f, i), j)
            return p, pp

        metric = np.broadcast_to(parent.geometry.ETA, (count, count, 4, 4)).copy()
        first = np.zeros((count, count, 4, 4, 4))
        metric[:, :, 1, 1], metric[:, :, 2, 2] = np.exp(0.1*np.sin(x)), np.exp(0.1*np.cos(y))
        first[:, :, 1, 1, 1] = 0.1*np.cos(x)*metric[:, :, 1, 1]
        first[:, :, 2, 2, 2] = -0.1*np.sin(y)*metric[:, :, 2, 2]
        volume = np.sqrt(-np.linalg.det(metric))
        p, pp = jets(h)
        q, qq = jets(u)
        eh, eu = np.zeros((count, count)), np.zeros((count, count))
        for index in np.ndindex((count, count)):
            result = parent.paired_scalar_equations(metric[index], first[index], p[index], pp[index], q[index], qq[index], coupling)
            eh[index], eu[index] = result["h_EL"], result["u_EL"]

        def action(hh, uu):
            a, b = jets(hh)[0], jets(uu)[0]
            inverse = np.linalg.inv(metric)
            f = coupling*(a[..., :, None]*b[..., None, :]-b[..., :, None]*a[..., None, :])
            raised = inverse @ f @ inverse
            return -np.sum(volume*np.sum(f*raised, axis=(-2, -1)))/4*(2*np.pi/count)**2

        numerical_h = (action(h+step*dh, u)-action(h-step*dh, u))/(2*step)
        numerical_u = (action(h, u+step*du)-action(h, u-step*du))/(2*step)
        self.assertClose(numerical_h, np.sum(volume*eh*dh)*(2*np.pi/count)**2, atol=3e-8)
        self.assertClose(numerical_u, np.sum(volume*eu*du)*(2*np.pi/count)**2, atol=3e-8)
        self.assertGreater(np.linalg.norm(eu), 0.1)

    def test_constraint_multiplier_signs_match_a_periodic_parent_variation(self):
        count, coupling, step = 32, 0.4, 1e-6
        x = np.arange(count)*2*np.pi/count
        freq = np.fft.fftfreq(count, d=1/count)

        def derivative(f):
            return np.fft.ifft(1j*freq[:, None]*np.fft.fft(f.reshape(count, -1), axis=0), axis=0).real.reshape(f.shape)

        y = np.sin(x[:, None])*self.rng.normal(size=4)
        h, u, zeta = 0.7+0.1*np.cos(x), np.sin(2*x), np.cos(3*x)
        lam = np.sin(x[:, None, None])*self.rng.normal(size=(4, 4))
        lam += np.cos(2*x[:, None, None])*self.rng.normal(size=(4, 4))
        vy, vh, vu = np.cos(2*x[:, None])*self.rng.normal(size=4), np.sin(x), np.cos(x)
        n, l = parent.geometry.N_COV, parent.geometry.L_VECTOR

        def action(yy, hh, uu):
            value = -np.einsum("na,na->n", lam[:, :, 1], derivative(yy))
            value -= coupling*hh*np.einsum("na,a->n", lam[:, :, 1], l)*derivative(uu)
            value += zeta*(uu-yy @ n)
            return np.sum(value)*2*np.pi/count

        wy = derivative(lam[:, :, 1])-zeta[:, None]*n
        wh = -coupling*(lam[:, :, 1] @ l)*derivative(u)
        wu = coupling*derivative(h*(lam[:, :, 1] @ l))+zeta
        for numerical, expected in [
            ((action(y+step*vy, h, u)-action(y-step*vy, h, u))/(2*step), np.sum(wy*vy)*2*np.pi/count),
            ((action(y, h+step*vh, u)-action(y, h-step*vh, u))/(2*step), np.sum(wh*vh)*2*np.pi/count),
            ((action(y, h, u+step*vu)-action(y, h, u-step*vu))/(2*step), np.sum(wu*vu)*2*np.pi/count)]:
            self.assertClose(numerical, expected, atol=2e-8)

    def test_native_positive_axis_gap_matches_its_analytic_value(self):
        expected = 1-abs(self.point[3])/np.linalg.norm(self.point[1:])
        self.assertClose(self.branch["native_axis_gap"]["gap"], expected)
        self.assertGreater(expected, 0.7)

    def test_every_sampled_positive_hc_obeys_the_axis_inequality(self):
        bg = self.branch["background"]
        gap = self.branch["native_axis_gap"]["gap"]
        for _ in range(12):
            raw = self.rng.normal(size=(3, 3))+1j*self.rng.normal(size=(3, 3))
            h = raw.conj().T @ raw
            v = np.array([np.vdot(bg["psi"], h @ bg["psi"] @ k.T).real for k in bg["weights"]])
            self.assertGreaterEqual(v[0]-v[3]+1e-12, gap*v[0])

    def test_target_null_direction_violates_the_positive_gap_bound(self):
        target = self.branch["profile"]["amplitude"]*parent.geometry.L_VECTOR
        self.assertGreater(target[0], 0)
        self.assertClose(target[0]-target[3], 0)
        self.assertGreater(self.branch["native_axis_gap"]["gap"]*target[0], 1)

    def test_current_span_cannot_fit_the_fixed_axis_even_with_indefinite_hc(self):
        bg = self.branch["background"]
        result = parent.current_span_test(bg["psi"], bg["weights"])
        self.assertEqual(result["rank"], 3)
        self.assertGreater(result["target_residual_norm"], 0.9)

    def test_all_hermitian_current_vectors_obey_the_explicit_spatial_plane_relation(self):
        bg = self.branch["background"]
        x, y, z = self.point[1:]
        for _ in range(8):
            raw = self.rng.normal(size=(3, 3))+1j*self.rng.normal(size=(3, 3))
            h = (raw+raw.conj().T)/2
            v = np.array([np.vdot(bg["psi"], h @ bg["psi"] @ k.T).real for k in bg["weights"]])
            self.assertClose(z*(x*v[1]+y*v[2])-(x*x+y*y)*v[3], 0)

    def test_axis_obstruction_is_not_claimed_for_every_possible_axis(self):
        axis = self.point[1:]/np.linalg.norm(self.point[1:])
        bg = self.branch["background"]
        result = parent.positive_hc_axis_gap(bg["psi"], bg["weights"], axis=axis)
        self.assertClose(result["gap"], 0)

    def test_axis_gap_can_vanish_for_a_collinear_probe_point(self):
        bg = parent.background.polynomial_background([0.01, 0, 0, 0.03])
        self.assertClose(parent.positive_hc_axis_gap(bg["psi"], bg["weights"])["gap"], 0)

    def test_effective_null_axis_is_not_automatically_reference_null(self):
        self.assertClose(self.branch["effective_axis_square"], 0)
        self.assertLess(self.branch["reference_axis_square"], -0.1)

    def test_reference_axis_slash_has_no_dark_spinor_when_its_reference_norm_is_nonzero(self):
        slash = self.branch["reference_axis_slash"]
        self.assertClose(slash @ slash, -self.branch["reference_axis_square"]*np.eye(4))
        self.assertEqual(np.linalg.matrix_rank(slash), 4)
        self.assertGreater(self.branch["reference_axis_slash_min_singular_value"], 0.1)

    def test_native_ordered_hc_transport_obeys_the_invertible_axis_lower_bound(self):
        bg = self.branch["background"]
        raw = self.rng.normal(size=(3, 3))+1j*self.rng.normal(size=(3, 3))
        hc = raw.conj().T @ raw
        image = hc @ bg["psi"]
        transport = image @ self.branch["reference_axis_slash"].T
        self.assertGreater(np.linalg.norm(transport), 0.1)
        self.assertGreaterEqual(np.linalg.norm(transport)+1e-12,
                                self.branch["reference_axis_slash_min_singular_value"]*np.linalg.norm(image))

    def test_cross_background_has_a_uniform_separation_bound_for_its_null_update_axes(self):
        result = parent.background_axis_separation(self.branch["theta"])
        self.assertTrue(result["strict_separation"])
        self.assertLess(result["reference_square_upper_bound"], -0.05)
        for _ in range(20):
            direction = self.rng.normal(size=3)
            direction /= np.linalg.norm(direction)
            q = self.branch["theta"].T @ np.r_[-1, direction]
            square = q @ parent.geometry.ETA @ q
            self.assertLessEqual(square, result["reference_square_upper_bound"]+1e-12)

    def test_uniform_axis_bound_is_not_a_universal_two_metric_no_go(self):
        result = parent.background_axis_separation(np.eye(4))
        self.assertFalse(result["strict_separation"])
        self.assertClose(result["reference_square_upper_bound"], 0)

    def test_local_family_works_at_other_nondegenerate_points(self):
        for point in [[0.012, 0.01, 0.02, -0.03], [0.02, -0.01, 0.02, 0.02]]:
            branch = parent.evaluate_branch(point, readout="ART")
            self.assertClose(branch["scalar"]["h_EL"], 0)
            self.assertClose(branch["scalar"]["u_EL"], 0)
            self.assertClose(branch["Einstein_residual"], np.zeros((4, 4)), atol=5e-10)

    def test_report_keeps_reference_stress_native_fields_and_free_axis_limitations(self):
        report = parent.evaluate()
        self.assertFalse(report["main_TeX_changed"])
        self.assertTrue(report["remaining_scope"]["reference_probe_mass_energy_is_not_an_effective_metric_stress_in_this_declared_two_frame_action"])
        self.assertTrue(report["remaining_scope"]["an_independently_variable_axis_would_add_an_equation_that_this_branch_does_not_solve"])
        self.assertTrue(report["common_parent"]["native_Yukawa_projector_Gauss_and_matching_terms_not_included"])

    def test_saved_report_matches_the_reproducible_calculation(self):
        saved = json.loads((ROOT / "analysis/HC_Derived_Background_Curved_Parent.json").read_text(encoding="utf-8"))
        self.assertEqual(saved, parent.evaluate())

    def test_bad_readouts_degenerate_coordinates_and_nonunit_axes_are_rejected(self):
        with self.assertRaises(ValueError):
            parent.coordinate_jets(self.point, "unknown")
        with self.assertRaises(ValueError):
            parent.evaluate_branch([0, 0, 0, 0])
        with self.assertRaises(ValueError):
            parent.positive_hc_axis_gap(self.branch["background"]["psi"], self.branch["background"]["weights"], axis=[1, 1, 1])


if __name__ == "__main__":
    unittest.main()
