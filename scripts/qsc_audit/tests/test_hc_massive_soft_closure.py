"""Massive charged local branches, independent HC response and hard constraint reactions."""
import importlib.util
import itertools
import json
from pathlib import Path
import unittest

import mpmath as mp
import numpy as np


ROOT = Path(__file__).resolve().parents[3]
SPEC = importlib.util.spec_from_file_location(
    "massive_soft_closure", ROOT / "analysis/HC_Massive_Soft_Closure.py")
model = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(model)


class HCMassiveSoftClosureTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.data = model.field_data()
        cls.report = model.evaluate()

    def assertClose(self, actual, expected, rtol=4e-8, atol=5e-10):
        np.testing.assert_allclose(actual, expected, rtol=rtol, atol=atol)

    def test_initial_first_jets_match_all_six_ODEs(self):
        y, dy, _ = model.series_jet(0)
        self.assertClose(y, model.DEFAULT_INITIAL)
        self.assertClose(dy, model.rhs(y))
        self.assertClose(dy, [0.158, -0.11, 0.03, -0.1664, 0, -0.64*0.216/0.49])

    def test_analytic_jacobian_against_independent_differences(self):
        state, _, _ = model.series_jet()
        step = 1e-6
        numerical = np.column_stack([(np.array(model.rhs(state+step*e))-np.array(model.rhs(state-step*e)))/(2*step)
                                     for e in np.eye(6)])
        self.assertClose(numerical, model.jacobian(state))

    def test_series_first_and_second_jets(self):
        z, step = 0.15, 1e-5
        y, dy, ddy = model.series_jet(z)
        plus, minus = model.series_jet(z+step), model.series_jet(z-step)
        self.assertClose((plus[0]-minus[0])/(2*step), dy)
        self.assertClose((plus[1]-minus[1])/(2*step), ddy)

    def test_high_order_defect_converges(self):
        defects = [model.series_defect(0.2, order=order) for order in (8, 16, 32)]
        self.assertGreater(defects[0], defects[1]*1e6)
        self.assertGreater(defects[1], defects[2]*1e12)
        self.assertLess(defects[-1], 1e-38)

    def test_series_matches_separate_installed_mpmath_ODE_implementation(self):
        with mp.workdps(40):
            p = tuple(mp.mpf(str(x)) for x in model.DEFAULT_PARAMETERS)
            y0 = [mp.mpf(str(x)) for x in model.DEFAULT_INITIAL]
            function = mp.odefun(lambda z, y: model.rhs(y, p), 0, y0, tol=mp.mpf("1e-32"), degree=20)
            expected = function(mp.mpf("0.15"))
            actual, _, _ = model.series_jet(0.15, high_precision=True)
            self.assertLess(float(max(abs(a-b) for a, b in zip(actual, expected))), 1e-30)

    def test_soft_vector_field_bounds_hold_on_all_reference_box_corners(self):
        box = model.existence_box()
        for corner in itertools.product(*zip(box["lower"], box["upper"])):
            self.assertTrue(np.all(np.abs(model.rhs(corner)) <= np.array(box["rhs_abs_bounds"])+1e-14))

    def test_soft_Jacobian_bound_on_reference_box(self):
        box = model.existence_box()
        for corner in itertools.product(*zip(box["lower"], box["upper"])):
            norm = np.max(np.sum(np.abs(model.jacobian(corner)), axis=1))
            self.assertLessEqual(norm, box["Jacobian_infinity_norm_bound"])

    def test_Picard_map_has_strict_box_and_contraction_margins(self):
        for box in (model.existence_box(), model.hard_existence_box()):
            self.assertLess(box["max_displacement_bound"], box["available_box_radius"])
            self.assertLess(box["Picard_contraction_bound"], 1)
            self.assertEqual(box["interval"], 0.2)

    def test_soft_positive_HC_and_scalar_bounds_are_retained_by_profiles(self):
        box = model.existence_box()
        for z in np.linspace(-0.2, 0.2, 9):
            y, _, _ = model.series_jet(float(z))
            self.assertTrue(np.all(y >= np.array(box["lower"])))
            self.assertTrue(np.all(y <= np.array(box["upper"])))
            self.assertGreaterEqual(y[4], box["h_lower_bound"])
            self.assertGreaterEqual(y[0]**2-y[1]**2, box["scalar_source_lower_bound"])

    def test_spatial_first_integral_is_conserved(self):
        values = [model.spatial_integral(model.series_jet(z)[0]) for z in (-0.2, -0.1, 0, 0.1, 0.2)]
        self.assertClose(values, np.repeat(-0.058096875, 5))

    def test_first_integral_gradient_annihilates_the_polynomial_vector_field(self):
        y, _, _ = model.series_jet()
        step = 1e-5
        gradient = np.array([(model.spatial_integral(y+step*e)-model.spatial_integral(y-step*e))/(2*step)
                             for e in np.eye(6)])
        self.assertClose(gradient @ np.array(model.rhs(y)), 0, atol=1e-9)

    def test_full_probe_first_jet_in_all_coordinates(self):
        point, step = self.data["point"], 1e-5
        for mu, direction in enumerate(np.eye(4)):
            plus, minus = model.field_data(point+step*direction), model.field_data(point-step*direction)
            self.assertClose((plus["psi"]-minus["psi"])/(2*step), self.data["psi_first"][mu])

    def test_full_connection_first_jet_in_all_coordinates(self):
        point, step = self.data["point"], 1e-5
        for mu, direction in enumerate(np.eye(4)):
            plus, minus = model.field_data(point+step*direction), model.field_data(point-step*direction)
            self.assertClose((plus["connection"]-minus["connection"])/(2*step), self.data["connection_first"][mu])

    def test_HC_first_jet_in_all_coordinates(self):
        point, step = self.data["point"], 1e-5
        for mu, direction in enumerate(np.eye(4)):
            plus, minus = model.field_data(point+step*direction), model.field_data(point-step*direction)
            self.assertClose((plus["H"]-minus["H"])/(2*step), self.data["H_first"][mu])

    def test_transport_is_closed_and_HC_has_positive_P_support(self):
        d, p = self.data, self.data["P"]
        self.assertClose(d["P_first"]+model.commutator(d["connection"], p), 0)
        self.assertClose(p @ d["H"] @ p, d["H"])
        self.assertGreater(np.linalg.eigvalsh(d["H"]).min(), -1e-13)
        self.assertGreater(np.trace(d["H"]).real, 0.19)

    def test_massive_current_and_scalar_are_computed_from_same_probe(self):
        d = self.data
        u, v = d["state"][:2]
        self.assertClose(d["current_up"][0], (u*u+v*v)*d["P"])
        self.assertClose(d["current_up"][1:], 0)
        self.assertClose(d["scalar_source"], (u*u-v*v)*d["P"])
        self.assertGreater(np.trace(d["scalar_source"]).real, 0.26)

    def test_current_is_timelike_not_the_previous_null_current(self):
        d = self.data
        vector = np.trace(d["current_up"], axis1=-2, axis2=-1).real
        square = vector @ d["bundle"]["metric"] @ vector
        self.assertLess(square, -0.07)

    def test_bare_and_effective_masses_are_nonzero_inputs(self):
        d = self.data
        m, _, _, _, gamma, _ = d["params"]
        self.assertEqual(m, 0.6)
        self.assertClose(d["mass_operator"] @ d["psi"], (m+gamma*d["state"][4])*d["psi"])
        self.assertGreater(m+gamma*d["state"][4], 0.67)

    def test_full_real_massive_probe_equation(self):
        self.assertLess(np.linalg.norm(model.probe_residual(self.data)), 1e-12)

    def test_full_sourced_gauge_HC_and_allowed_projector_equations(self):
        r = model.field_residuals()
        for name in ("gauge", "HC", "projector_tangent", "gauge_HC_commutator_force"):
            self.assertLess(np.linalg.norm(r[name]), 2e-8)

    def test_projector_normal_reaction_is_not_mistaken_for_tangent_failure(self):
        r, p = model.field_residuals(), self.data["P"]
        self.assertGreater(np.linalg.norm(r["projector_normal_reaction"]), 0.2)
        self.assertClose(model.commutator(r["projector_normal_reaction"], p), 0)
        self.assertClose(r["projector_tangent"], 0)

    def test_nonzero_HC_source_balances_curvature_and_matching_reaction(self):
        d, r = self.data, model.field_residuals()
        gamma, penalty = d["params"][4], d["params"][5]
        self.assertGreater(np.linalg.norm(gamma*d["scalar_source"]), 0.1)
        self.assertClose(r["HC_curvature"], 2*penalty*d["H"]+gamma*d["scalar_source"])

    def test_independent_probe_HC_Yukawa_source_by_finite_variation(self):
        d, step = self.data, 1e-5
        direction = d["P"]
        m, _, _, _, gamma, _ = d["params"]
        values = []
        for sign in (1, -1):
            values.append(model.source.probe.real_probe_density(
                d["psi"], d["psi_first"], -1j*d["unitary"], d["H"]+sign*step*direction,
                model.dirac.BETA @ d["bundle"]["gamma"], model.dirac.BETA, mass=m, yukawa=gamma))
        self.assertClose((values[0]-values[1])/(2*step), -gamma*np.trace(direction @ d["scalar_source"]).real)

    def test_independent_full_matrix_HC_Euler_variation(self):
        amplitude_step, coordinate_step = 2e-5, 2e-4

        def partial(d, momentum=False):
            values = []
            _, _, gauge, kappa, gamma, penalty = d["params"]
            for sign in (1, -1):
                eps = sign*amplitude_step
                h, dh = d["H"].copy(), d["H_first"].copy()
                if momentum:
                    dh[3] += eps*d["P"]
                else:
                    h += eps*d["P"]
                    dh += eps*d["P_first"]
                axis, eta = model.source.dynamics.AXIS, 0.7
                b = d["unitary"]+axis[:, None, None]*(kappa*h+eta*(np.eye(2)-d["P"]))
                db = d["unitary_first"]+(kappa*dh-eta*d["P_first"])[:, None]*axis[None, :, None, None]
                f = model.checks.connection_curvature(b, db)
                inv = model.source.load.inverse_metric(d["point"][1], d["radius"])
                value = -model.source.load.curvature_density(f, inv, gauge).real
                value -= penalty*np.vdot(h, h).real+gamma*np.trace(h @ d["scalar_source"]).real
                values.append(value)
            return (values[0]-values[1])/(2*amplitude_step)

        point = self.data["point"]
        direction = np.array([0, 0, 0, coordinate_step])
        euler = partial(self.data)-(partial(model.field_data(point+direction), True)
                                    -partial(model.field_data(point-direction), True))/(2*coordinate_step)
        self.assertClose(euler, 0, atol=4e-6)

    def test_native_ordered_probe_transport_is_still_a_nonzero_extra_term(self):
        d = self.data
        difference = model.probe_residual(d, ordered=True)-model.probe_residual(d)
        extra = 1j*np.einsum("mij,mrj->ri", d["bundle"]["gamma"],
                             (d["connection"]-d["unitary"]) @ d["psi"])
        self.assertClose(difference, extra)
        self.assertGreater(np.linalg.norm(difference), 0.1)

    def test_printed_complex_connection_equation_is_not_declared_solved(self):
        r = model.field_residuals()
        self.assertGreater(np.linalg.norm(r["printed_complex_extra"]), 0.2)

    def test_soft_H_is_not_hard_matching_even_though_M_closes(self):
        d = self.data
        target = model.source.transport.hessian.phase.minimal_native_closure(0.6*np.eye(2), d["P"])
        self.assertClose(target, 0)
        self.assertGreater(np.linalg.norm(d["H"]-target), 0.19)

    def test_soft_zero_boundary_initial_data_can_leave_the_positive_cone(self):
        y, dy, ddy = model.series_jet(0, initial=model.HARD_INITIAL)
        self.assertClose(y[4:], 0)
        self.assertLess(dy[5], -0.1)
        self.assertLess(model.series_jet(0.05, initial=model.HARD_INITIAL)[0][4], 0)

    def test_hard_dependent_profile_has_identically_zero_HC_without_zero_gamma(self):
        d = model.field_data(domain="hard")
        self.assertEqual(d["params"][4], 0.4)
        self.assertClose(d["state"][4:], 0)
        self.assertClose(d["H"], 0)
        self.assertGreater(np.trace(d["scalar_source"]).real, 0.26)

    def test_hard_dependent_massive_probe_and_gauge_equations(self):
        d, r = model.field_data(domain="hard"), model.field_residuals(domain="hard")
        self.assertClose(model.probe_residual(d), 0)
        self.assertClose(model.probe_residual(d, ordered=True), 0)
        self.assertClose(r["gauge"], 0)
        self.assertClose(r["projector_tangent"], 0)

    def test_hard_reduction_does_not_also_satisfy_independent_soft_HC_equation(self):
        d, r = model.field_data(domain="hard"), model.field_residuals(domain="hard")
        gamma = d["params"][4]
        self.assertGreater(np.linalg.norm(r["HC"]), 0.1)
        self.assertClose(r["HC"], -gamma*d["scalar_source"])

    def test_equality_multiplier_supplies_excluded_H_direction_reaction(self):
        d, r = model.field_data(domain="hard"), model.field_residuals(domain="hard")
        multiplier = d["params"][4]*d["scalar_source"]
        self.assertClose(r["HC"]+multiplier, 0)
        self.assertClose(d["P"] @ multiplier @ d["P"], multiplier)

    def test_minimal_target_has_no_missing_first_order_multiplier_chain_reaction(self):
        d = model.field_data(domain="hard")
        m, step = 0.6*np.eye(2), 1e-4
        direction = model.source.transport.PAULI[0]
        target = model.source.transport.hessian.phase.minimal_native_closure
        first = (target(m+step*direction, d["P"])-target(m-step*direction, d["P"])
                 )/(2*step)
        multiplier = d["params"][4]*d["scalar_source"]
        self.assertClose(first, 0)
        self.assertClose(np.trace(multiplier @ first), 0)

    def test_zero_scalar_source_at_one_point_is_not_a_preserved_hard_evolution_condition(self):
        initial = (0.2, 0.2, model.DEFAULT_PARAMETERS[1], 0, 0, 0)
        y0 = model.series_jet(0, initial=initial, domain="hard")[0]
        y1 = model.series_jet(0.1, initial=initial, domain="hard")[0]
        self.assertClose(y0[0]**2-y0[1]**2, 0)
        self.assertGreater(abs(y1[0]**2-y1[1]**2), 1e-6)

    def test_hard_four_dimensional_reference_box_bounds(self):
        box = model.hard_existence_box()
        for corner in itertools.product(*zip(box["lower"], box["upper"])):
            state = (*corner, 0, 0)
            self.assertTrue(np.all(np.abs(model.rhs(state, domain="hard")[:4]) <= np.array(box["rhs_abs_bounds"])+1e-14))
            jac = model.jacobian(state)[:4, :4]
            self.assertLessEqual(np.max(np.sum(abs(jac), axis=1)), box["Jacobian_infinity_norm_bound"])

    def test_hard_series_has_its_own_small_ODE_defect(self):
        for z in (-0.2, 0.2):
            self.assertLess(model.series_defect(z, initial=model.HARD_INITIAL, domain="hard"), 1e-35)

    def test_gamma_zero_control_is_distinct_from_hard_domain_choice(self):
        p = list(model.DEFAULT_PARAMETERS)
        p[4] = 0
        d = model.field_data(params=tuple(p), initial=model.HARD_INITIAL)
        r = model.field_residuals(params=tuple(p), initial=model.HARD_INITIAL)
        self.assertEqual(d["domain"], "soft")
        self.assertClose(d["H"], 0)
        self.assertClose(r["HC"], 0)
        self.assertGreater(np.trace(d["scalar_source"]).real, 0.26)

    def test_profiles_can_be_lifted_at_other_radii_and_angular_points(self):
        for point, radius in (([0.2, 0.5, -0.4, -0.1], 0.8), ([-0.3, 2.4, 1.2, 0.1], 1.7)):
            d, r = model.field_data(point, radius=radius), model.field_residuals(point, radius=radius)
            self.assertClose(model.probe_residual(d), 0)
            for name in ("gauge", "HC", "projector_tangent"):
                self.assertLess(np.linalg.norm(r[name]), 2e-8)

    def test_noncentral_scalar_source_is_not_a_free_compensating_current(self):
        d = self.data
        self.assertGreater(np.linalg.norm(d["scalar_source"]-np.trace(d["scalar_source"])*np.eye(2)/2), 0.1)
        self.assertClose(d["scalar_source"], (d["state"][0]**2-d["state"][1]**2)*d["P"])

    def test_eta_changes_do_not_drive_the_closed_probe_in_real_comparison(self):
        for eta in (-1, 0, 1.2):
            d, r = model.field_data(eta=eta), model.field_residuals(eta=eta)
            self.assertClose(model.probe_residual(d), 0)
            self.assertClose(r["gauge"], 0)
            self.assertClose(r["HC"], 0)

    def test_stationary_current_continuity_is_not_lost_when_density_varies(self):
        d = self.data
        self.assertGreater(abs(np.trace(d["current_up"][0]).real-0.26), 0.01)
        self.assertClose(d["current_up"][3], 0)
        self.assertClose(model.commutator(d["unitary"][0], d["current_up"][0]), 0)

    def test_invalid_parameters_orders_domains_and_intervals(self):
        for index, value in ((0, 0), (2, 0), (3, 0), (5, -1)):
            p = list(model.DEFAULT_PARAMETERS)
            p[index] = value
            with self.assertRaises(ValueError):
                model.parameters(p)
        for order in (True, 1, 81):
            with self.assertRaises(ValueError):
                model.coefficients(order)
        with self.assertRaises(ValueError):
            model.series_jet(0.21)
        with self.assertRaises(ValueError):
            model.coefficients(domain="other")
        with self.assertRaises(ValueError):
            model.coefficients(domain="hard")
        with self.assertRaises(ValueError):
            model.field_residuals(step=0)

    def test_domain_and_native_identification_limits_are_explicit(self):
        self.assertFalse(self.report["main_TeX_changed"])
        self.assertIn("NOT native hard H=Lambda", self.report["status"])
        self.assertTrue(self.report["hard_branch_boundary"]["not_a_no_go_for_all_massive_native_probes_or_nonstationary_currents"])
        self.assertTrue(self.report["hard_dependent_comparison"]["not_a_derivation_of_the_native_HC_domain_or_gauge_current_dictionary"])

    def test_report_reproduces_saved_results(self):
        saved = json.loads((ROOT / "analysis/HC_Massive_Soft_Closure.json").read_text(encoding="utf-8"))
        self.assertEqual(self.report, saved)


if __name__ == "__main__":
    unittest.main()
