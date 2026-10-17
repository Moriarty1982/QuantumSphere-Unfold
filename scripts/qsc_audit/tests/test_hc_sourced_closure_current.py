"""Current reality/support, sourced closure and one common charged massless local branch."""
import importlib.util
import json
from pathlib import Path
import unittest

import numpy as np


ROOT = Path(__file__).resolve().parents[3]
SPEC = importlib.util.spec_from_file_location(
    "sourced_closure_current", ROOT / "analysis/HC_Sourced_Closure_Current.py")
model = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(model)


class HCSourcedClosureCurrentTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.data = model.charged_data()
        cls.report = model.evaluate()

    def assertClose(self, actual, expected, rtol=4e-8, atol=4e-10):
        np.testing.assert_allclose(actual, expected, rtol=rtol, atol=atol)

    def test_probe_current_is_Hermitian_positive_time_and_nonzero(self):
        j = self.data["current_up"]
        self.assertClose(j, j.conj().swapaxes(-1, -2))
        self.assertGreater(np.trace(j[0]).real, 0)
        self.assertGreater(np.linalg.eigvalsh(j[0]).min(), -1e-14)

    def test_positive_time_trace_is_the_actual_probe_norm(self):
        d = self.data
        self.assertClose(np.trace(d["current_up"][0]), np.vdot(d["psi"], d["psi"]))
        self.assertClose(np.vdot(d["psi"], d["psi"]), d["density"])

    def test_closed_probe_current_is_supported_in_P(self):
        p, psi, j = self.data["P"], self.data["psi"], self.data["current_up"]
        self.assertClose(p @ psi, psi)
        self.assertClose(p @ j @ p, j)
        self.assertClose((np.eye(2)-p) @ j, 0)

    def test_scalar_source_is_zero_without_zero_probe(self):
        self.assertClose(self.data["scalar_source"], 0)
        self.assertGreater(np.linalg.norm(self.data["psi"]), 0.6)

    def test_current_components_match_the_exact_null_source(self):
        d = self.data
        self.assertClose(d["current_up"][[0, 3]], np.array([d["density"]*d["P"]]*2))
        self.assertClose(d["current_up"][[1, 2]], 0)
        self.assertClose(d["current_lower"][0], -d["current_up"][0])

    def test_current_is_null_with_the_same_product_metric(self):
        d = self.data
        vector = np.trace(d["current_up"], axis1=-2, axis2=-1).real
        self.assertClose(vector @ d["bundle"]["metric"] @ vector, 0)

    def test_fixed_M_closed_projector_has_zero_trace_gradient(self):
        d = self.data
        result = model.closure_trace_current(0.6*np.eye(2), np.zeros((4, 2, 2)), d["P"], d["P_first"])
        self.assertClose(result, 0)

    def test_fixed_M_identity_does_not_require_scalar_or_nondegenerate_M(self):
        p = np.diag([1.0, 0, 0])
        generator = np.array([[0, 1j, 0], [-1j, 0, 0], [0, 0, 0]])
        dp = np.zeros((4, 3, 3), complex)
        dp[1] = 1j*model.commutator(generator, p)
        m = np.diag([0.6, 0.6, 1.4])
        self.assertClose(model.commutator(m, p), 0)
        self.assertGreater(np.linalg.norm(dp), 1)
        self.assertClose(model.closure_trace_current(m, np.zeros_like(dp), p, dp), 0)

    def test_variable_M_term_cannot_be_discarded(self):
        d, dm = self.data, np.zeros((4, 2, 2))
        dm[0] = 0.3*np.eye(2)
        result = model.closure_trace_current(0.6*np.eye(2), dm, d["P"], d["P_first"])
        self.assertClose(result, [0.3, 0, 0, 0])

    def test_traceless_projection_evades_trace_but_not_preserves_support(self):
        p, j = self.data["P"], self.data["current_up"][0]
        projected = j-np.trace(j)*np.eye(2)/2
        self.assertClose(np.trace(projected), 0)
        self.assertLess(np.linalg.eigvalsh(projected).min(), 0)
        self.assertGreater(np.linalg.norm((np.eye(2)-p) @ projected), 0.1)

    def test_scalar_identity_lift_is_not_the_internal_probe_matrix_current(self):
        p, j = self.data["P"], self.data["current_lower"][0]
        scalar = np.trace(j)
        lifted = scalar*np.eye(2)
        self.assertClose(np.trace(lifted), 2*np.trace(j))
        self.assertGreater(np.linalg.norm((np.eye(2)-p) @ lifted), 0.3)
        self.assertGreater(np.linalg.norm(lifted-j), 0.3)

    def test_random_connection_trace_identity_includes_nonunitary_load(self):
        rng = np.random.default_rng(943)
        u = rng.normal(size=(4, 2, 2))+1j*rng.normal(size=(4, 2, 2))
        du = rng.normal(size=(4, 4, 2, 2))+1j*rng.normal(size=(4, 4, 2, 2))
        u, du = u-u.conj().swapaxes(-1, -2), du-du.conj().swapaxes(-1, -2)
        phi = rng.normal(size=(2, 2))+1j*rng.normal(size=(2, 2))
        dphi = rng.normal(size=(4, 2, 2))+1j*rng.normal(size=(4, 2, 2))
        phi, dphi = phi+phi.conj().T, dphi+dphi.conj().swapaxes(-1, -2)
        n, dn = rng.normal(size=4), rng.normal(size=(4, 4))
        b = u+n[:, None, None]*phi
        db = du+dphi[:, None]*n[None, :, None, None]+dn[:, :, None, None]*phi
        f = model.checks.connection_curvature(b, db)
        tr_dphi = np.trace(dphi, axis1=-2, axis2=-1).real
        expected = (np.outer(tr_dphi, n)-np.outer(n, tr_dphi)+(dn-dn.T)*np.trace(phi).real)
        self.assertClose(np.trace(f, axis1=-2, axis2=-1).real, expected)

    def test_constant_axis_hard_branch_has_zero_real_trace_resonance(self):
        e = model.resonance()
        self.assertClose(np.trace(e, axis1=-2, axis2=-1).real, 0)
        self.assertGreater(abs(np.trace(self.data["current_lower"][0]).real), 0.3)

    def test_direct_Hermitian_source_fails_but_unitary_phase_matches(self):
        d, e = self.data, model.resonance()
        self.assertLess(np.linalg.norm(e-1j*d["coupling"]**2*d["current_lower"]), 2e-8)
        self.assertClose(np.linalg.norm(e-d["coupling"]**2*d["current_lower"]), 0.8)

    def test_null_axis_can_vary_without_becoming_nonnull(self):
        d = model.charged_data(axis_shape=0.4)
        self.assertClose(d["axis"] @ np.linalg.solve(d["bundle"]["metric"], d["axis"]), 0)
        self.assertGreater(np.linalg.norm(d["axis_first"]-d["axis_first"].T), 0.1)

    def test_axis_trace_match_has_the_wrong_projector_support(self):
        d = self.data
        e = model.resonance(axis_shape=d["density"]/d["eta"])
        h = (e+e.conj().swapaxes(-1, -2))/2
        expected = -d["density"]*(np.eye(2)-d["P"])
        self.assertClose(h[0], expected)
        self.assertClose(np.trace(h[0]), np.trace(d["current_lower"][0]))
        self.assertClose(d["P"] @ h[0] @ d["P"], 0)
        self.assertClose(np.linalg.norm(h[0]-d["current_lower"][0]), np.sqrt(2)*d["density"])

    def test_variable_axis_full_resonance_matches_the_block_formula(self):
        kwargs = {"axis_shape": 0.3, "radius": 1.7, "density": 0.2, "coupling": 0.8}
        d = model.charged_data(**kwargs)
        self.assertClose(model.resonance(**kwargs), model.expected_resonance(d))

    def test_full_connection_preserves_P_with_or_without_variable_axis(self):
        for shape in (0, 0.4):
            d = model.charged_data(axis_shape=shape)
            self.assertClose(d["P_first"]+model.commutator(d["connection"], d["P"]), 0)

    def test_compatible_unitary_connection_has_a_nonzero_central_component(self):
        d = self.data
        self.assertClose(d["unitary"], -d["unitary"].conj().swapaxes(-1, -2))
        self.assertGreater(abs(np.trace(d["unitary"][3])), 0.05)
        self.assertGreater(abs(np.trace(d["G"][0, 3])), 0.2)

    def test_normal_potential_has_the_required_electric_field(self):
        d = self.data
        t, _, _, z = d["point"]
        self.assertClose(d["G"][0, 3], 1j*d["coupling"]**2*d["density"]*(z-t)*d["P"])

    def test_full_connection_derivative_in_all_coordinates(self):
        point, step = self.data["point"], 1e-5
        d = model.charged_data(point, axis_shape=0.3)
        for mu, direction in enumerate(np.eye(4)):
            plus = model.charged_data(point+step*direction, axis_shape=0.3)
            minus = model.charged_data(point-step*direction, axis_shape=0.3)
            self.assertClose((plus["connection"]-minus["connection"])/(2*step), d["connection_first"][mu])

    def test_actual_probe_first_jet_in_all_coordinates(self):
        point, step = self.data["point"], 1e-5
        for mu, direction in enumerate(np.eye(4)):
            plus, minus = model.charged_data(point+step*direction), model.charged_data(point-step*direction)
            self.assertClose((plus["psi"]-minus["psi"])/(2*step), self.data["psi_first"][mu])

    def test_south_patch_probe_and_jets_agree_on_overlap(self):
        south = model.charged_data(patch="south")
        self.assertClose(south["psi"], self.data["psi"])
        self.assertClose(south["psi_first"], self.data["psi_first"])
        self.assertClose(south["current_up"], self.data["current_up"])

    def test_spin_frame_half_angle_sign_does_not_change_bilinears(self):
        point = self.data["point"].copy()
        point[2] += 2*np.pi
        other = model.charged_data(point)
        self.assertClose(other["psi"], -self.data["psi"])
        self.assertClose(other["current_up"], self.data["current_up"])
        self.assertClose(other["F"], self.data["F"])

    def test_same_coframe_spin_lift_has_gamma_compatibility(self):
        b = self.data["bundle"]
        self.assertClose(b["gamma_compatibility"], 0)
        self.assertClose(np.diag(b["metric"]), [-1, 1, np.sin(0.9)**2, 1])

    def test_nonzero_spin_connection_is_not_omitted(self):
        self.assertGreater(np.linalg.norm(self.data["bundle"]["spin"]), 0.5)

    def test_full_charged_massless_probe_residual_is_zero(self):
        self.assertLess(np.linalg.norm(model.probe_residual(self.data)), 1e-12)
        self.assertLess(np.linalg.norm(model.probe_residual(self.data, ordered=False)), 1e-12)

    def test_omitting_spin_connection_breaks_angular_cancellation(self):
        d = self.data
        residual = model.dirac.dirac_data(d["psi"], d["psi_first"]+d["unitary"] @ d["psi"], np.zeros((2, 2)),
                                         gamma=d["bundle"]["gamma"], metric=d["bundle"]["metric"])["residual"]
        self.assertGreater(np.linalg.norm(residual), 0.1)

    def test_restoring_mass_breaks_the_same_probe_equation(self):
        for mass in (0.2, 0.6, 1.3):
            residual = model.probe_residual(self.data, mass=mass)
            self.assertClose(residual, -mass*self.data["psi"])
            self.assertClose(np.linalg.norm(residual), mass*np.sqrt(self.data["density"]))

    def test_both_real_action_signs_have_common_probe_and_gauge_branches(self):
        for sign in (-1, 1):
            d = model.charged_data(sign=sign)
            self.assertClose(model.probe_residual(d), 0)
            self.assertClose(model.resonance(sign=sign), 1j*sign*d["coupling"]**2*d["current_lower"])

    def test_common_solution_across_points_radii_and_couplings(self):
        for point, radius, coupling, density in (([0.2, 0.5, -0.4, 0.7], 0.8, 0.6, 0.3),
                                                ([-0.4, 2.4, 1.2, 0.3], 1.7, 1.2, 0.7)):
            kwargs = {"radius": radius, "coupling": coupling, "density": density}
            d = model.charged_data(point, **kwargs)
            self.assertClose(model.probe_residual(d), 0)
            self.assertClose(model.resonance(point, **kwargs), 1j*coupling**2*d["current_lower"])

    def test_probe_equation_remains_dark_to_eta_only_because_it_is_closed(self):
        for eta in (-2, 0, 0.7, 3):
            d = model.charged_data(eta=eta)
            self.assertClose(model.probe_residual(d), 0)
            self.assertClose((d["connection"]-d["unitary"]) @ d["psi"], 0)

    def test_zero_density_recovers_empty_probe_but_retains_geometric_flux(self):
        d = model.charged_data(density=0)
        self.assertClose(d["psi"], 0)
        self.assertClose(d["current_up"], 0)
        self.assertGreater(np.linalg.norm(d["G"][1, 2]), 0.5)
        self.assertClose(model.resonance(density=0), 0)

    def test_matrix_current_from_independent_probe_action_variations(self):
        for mu, generator in ((0, self.data["P"]), (3, np.eye(2)), (1, model.transport.PAULI[0])):
            value = model.source_variation(self.data, generator, component=mu)
            self.assertClose(value, -np.trace(generator @ self.data["current_up"][mu]).real)

    def test_current_covariant_divergence_with_coordinate_density(self):
        d, step = self.data, 1e-5
        total = np.sum(model.commutator(d["unitary"], d["current_up"]), axis=0)
        for mu, direction in enumerate(np.eye(4)):
            samples = []
            for sign in (1, -1):
                other = model.charged_data(d["point"]+sign*step*direction)
                samples.append(np.sin(other["point"][1])*other["current_up"][mu])
            total += (samples[0]-samples[1])/(2*step*np.sin(d["point"][1]))
        self.assertClose(total, 0)

    def test_gauge_residual_is_not_fitted_by_replacing_actual_current(self):
        d = self.data
        expected = model.expected_resonance(d)
        self.assertClose(expected[0], -1j*d["density"]*d["P"])
        self.assertClose(expected[3], 1j*d["density"]*d["P"])
        self.assertGreater(np.linalg.norm(expected), 0.5)

    def test_wrong_source_sign_fails_without_flipping_both_potential_and_phase(self):
        d, e = self.data, model.resonance()
        self.assertGreater(np.linalg.norm(e+1j*d["coupling"]**2*d["current_lower"]), 1)

    def test_state_matching_penalties_vanish_without_zero_current(self):
        d = self.data
        self.assertClose((np.eye(2)-d["P"]) @ d["psi"], 0)
        target = model.transport.hessian.phase.minimal_native_closure(0.6*np.eye(2), d["P"])
        self.assertClose(target, 0)
        self.assertGreater(np.trace(d["current_up"][0]).real, 0.3)

    def test_hard_load_has_zero_Hermitian_curvature_on_compatible_constant_axis_branch(self):
        d = self.data
        self.assertClose(d["F"], d["G"])
        self.assertClose(d["F"], -d["F"].conj().swapaxes(-1, -2))

    def test_independent_real_curvature_load_first_variations_vanish_pointwise(self):
        d, step = self.data, 1e-5
        direction = model.transport.PAULI[0]+0.3*np.eye(2)
        first = np.array([0.2, -0.1, 0.3, -0.4])[:, None, None]*model.transport.PAULI[1]
        inv = model.load.inverse_metric(d["point"][1], d["radius"])
        phi, dphi = d["eta"]*(np.eye(2)-d["P"]), -d["eta"]*d["P_first"]
        for pairing in ("literal", "dagger"):
            values = []
            for sign in (1, -1):
                eps = sign*step
                b = d["unitary"]+d["axis"][:, None, None]*(phi+eps*direction)
                db = d["unitary_first"]+(dphi+eps*first)[:, None]*d["axis"][None, :, None, None]
                f = model.checks.connection_curvature(b, db)
                values.append(-model.load.curvature_density(f, inv, d["coupling"], pairing).real
                              -0.3*eps*eps*np.vdot(direction, direction).real)
            self.assertClose((values[0]-values[1])/(2*step), 0, atol=2e-9)

    def test_free_chiral_phase_does_not_determine_an_energy_scale(self):
        d = {**self.data}
        t, _, _, z = d["point"]
        frequency = 1.3
        phase = np.exp(-1j*frequency*(t-z))
        covector = np.array([1, 0, 0, -1])
        d["psi_first"] = phase*(d["psi_first"]-1j*frequency*covector[:, None, None]*d["psi"])
        d["psi"] = phase*d["psi"]
        self.assertClose(model.probe_residual(d), 0)
        j = model.probe.probe_currents(d["psi"], d["weights"], model.dirac.BETA)["gauge"]
        self.assertClose(j, self.data["current_up"])

    def test_invalid_inputs_are_rejected(self):
        for kwargs in ({"density": -1}, {"radius": 0}, {"coupling": 0}, {"eta": np.nan},
                       {"sign": 0}, {"sign": True}, {"patch": "other"}):
            with self.assertRaises(ValueError):
                model.charged_data(**kwargs)
        with self.assertRaises(ValueError):
            model.resonance(step=0)
        with self.assertRaises(ValueError):
            model.source_variation(self.data, np.eye(2), component=4)
        with self.assertRaises(ValueError):
            model.closure_trace_current(np.eye(3), np.zeros((4, 3, 3)), self.data["P"], self.data["P_first"])

    def test_native_anchor_and_comparison_boundaries(self):
        text = (ROOT / self.report["native_audit"]["source_path"]).read_text(encoding="utf-8")
        for label in self.report["native_audit"]["source_labels"]:
            self.assertIn("\\label{"+label+"}", text)
        self.assertFalse(self.report["main_TeX_changed"])
        self.assertIn("NOT a native massive C7", self.report["status"])
        self.assertTrue(self.report["charged_comparison"]["infinite_homogeneous_normal_direction_not_a_global_finite_energy_configuration"])

    def test_report_reproduces_saved_results(self):
        saved = json.loads((ROOT / "analysis/HC_Sourced_Closure_Current.json").read_text(encoding="utf-8"))
        self.assertEqual(self.report, saved)


if __name__ == "__main__":
    unittest.main()
