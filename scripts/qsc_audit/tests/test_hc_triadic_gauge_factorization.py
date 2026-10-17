"""Channel/gauge separation, projected currents and a coherent hard comparison."""
import importlib.util
import itertools
import json
from pathlib import Path
import unittest

import mpmath as mp
import numpy as np


ROOT = Path(__file__).resolve().parents[3]
SPEC = importlib.util.spec_from_file_location(
    "triadic_gauge_factorization", ROOT / "analysis/HC_Triadic_Gauge_Factorization.py")
model = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(model)


class HCTriadicGaugeFactorizationTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.data = model.field_data()
        cls.report = model.evaluate()

    def assertClose(self, actual, expected, atol=1e-9):
        np.testing.assert_allclose(actual, expected, atol=atol, rtol=4e-8)

    def test_native_text_calls_the_entire_triad_closed(self):
        text = (ROOT / "sources/research/parts/v470/10_sphaera_and_physics.tex").read_text(encoding="utf-8")
        self.assertIn("closed triadic probe field", text)
        self.assertIn("color indices, not on the quaternion structure", text)
        text = (ROOT / "sources/research/parts/native-operator-link.tex").read_text(encoding="utf-8")
        self.assertIn("label probe channels,", text)
        self.assertIn("not the three generation coordinates", text)

    def test_gauge_generators_on_the_other_factor_commute_with_noncentral_triad(self):
        mass = np.kron(np.eye(2), model.TRIAD)
        for generator in (np.eye(2), *model.source.transport.PAULI):
            self.assertClose(model.commutator(np.kron(generator, np.eye(3)), mass), 0)

    def test_bare_channel_couplings_require_compatible_charges(self):
        self.assertClose(model.charge_intertwiner([1, 1, 1]), 0)
        self.assertClose(np.linalg.norm(model.charge_intertwiner([1, 1, 0])), np.sqrt(2*16.49))
        self.assertGreater(np.linalg.norm(model.charge_intertwiner([0, 1, 0])), 0.9)

    def test_partial_trace_and_projection_are_not_full_matrix_identity(self):
        a, b = np.array([[1, 0.2j], [-0.2j, 2]]), np.diag([1, 2, 4])
        matrix = np.kron(a, b)
        self.assertClose(model.partial_trace_channels(matrix), 7*a)
        projected = model.gauge_projection(matrix)
        self.assertClose(projected, np.kron(7*a/3, np.eye(3)))
        self.assertClose(model.gauge_projection(projected), projected)
        self.assertClose(np.trace(projected), np.trace(matrix))
        self.assertGreater(np.linalg.norm(matrix-projected), 1)

    def test_projection_is_orthogonal_to_all_allowed_gauge_variations(self):
        rng = np.random.default_rng(18)
        matrix = rng.normal(size=(6, 6))+1j*rng.normal(size=(6, 6))
        omitted = matrix-model.gauge_projection(matrix)
        for generator in (np.eye(2), *model.source.transport.PAULI):
            self.assertClose(np.vdot(np.kron(generator, np.eye(3)), omitted), 0)

    def test_projection_supports_batched_curvatures_and_currents(self):
        d = self.data
        self.assertEqual(model.gauge_projection(d["F"]).shape, (4, 4, 6, 6))
        self.assertEqual(model.partial_trace_channels(d["current"]).shape, (4, 2, 2))
        self.assertClose(model.gauge_projection(d["F"]), d["F"])

    def test_full_trace_action_has_the_explicit_multiplicity_three(self):
        d = self.data
        inv = model.source.load.inverse_metric(d["point"][1], d["radius"])
        f2 = model.partial_trace_channels(d["F"])/3
        full = model.source.load.curvature_density(d["F"], inv, model.GAUGE)
        reduced = model.source.load.curvature_density(f2, inv, model.GAUGE)
        self.assertClose(full, 3*reduced)

    def test_initial_jets_use_matrix_mixing_and_correct_charge_normalization(self):
        y, dy, _ = model.series_jet(0)
        self.assertClose(y, model.INITIAL)
        self.assertClose(dy, [0.15, 0, 0.4, -0.15, 0, 2, 0.03, -0.64*0.26/3])

    def test_analytic_jacobian_against_independent_differences(self):
        y = model.series_jet()[0]
        step = 1e-6
        numerical = np.column_stack([(model.rhs(y+step*e)-model.rhs(y-step*e))/(2*step) for e in np.eye(8)])
        self.assertClose(numerical, model.jacobian(y))

    def test_first_and_second_taylor_jets(self):
        z, step = 0.02, 1e-5
        _, dy, ddy = model.series_jet(z)
        plus, minus = model.series_jet(z+step), model.series_jet(z-step)
        self.assertClose((plus[0]-minus[0])/(2*step), dy)
        self.assertClose((plus[1]-minus[1])/(2*step), ddy)

    def test_taylor_defect_converges_and_is_small_on_proved_interval(self):
        defects = [model.series_defect(0.03, n) for n in (8, 16, 32)]
        self.assertGreater(defects[0], defects[1]*1e10)
        self.assertGreater(defects[1], defects[2]*1e15)
        self.assertLess(defects[-1], 1e-45)

    def test_taylor_matches_separate_installed_ode_implementation(self):
        with mp.workdps(40):
            mass = [[mp.mpf(str(x)) for x in row] for row in model.TRIAD]
            target = mp.odefun(lambda z, y: model._rhs(y, mass, mp.mpf(".9"), mp.mpf(".8"), 3),
                              0, [mp.mpf(str(x)) for x in model.INITIAL], tol=mp.mpf("1e-32"), degree=20)
            value = target(mp.mpf(".02"))
            actual = model.series_jet(0.02, high_precision=True)[0]
            self.assertLess(float(max(abs(a-b) for a, b in zip(value, actual))), 1e-30)

    def test_picard_component_and_lipschitz_bounds_on_all_box_corners(self):
        box = model.existence_box()
        for corner in itertools.product(*zip(box["lower"], box["upper"])):
            self.assertTrue(np.all(np.abs(model.rhs(corner)) <= np.array(box["rhs_abs_bounds"])+1e-13))
            norm = np.max(np.sum(abs(model.jacobian(corner)), axis=1))
            self.assertLessEqual(norm, box["Jacobian_infinity_norm_bound"]+1e-13)
        self.assertLess(box["max_displacement_bound"], box["available_box_radius"])
        self.assertLess(box["Picard_contraction_bound"], 1)

    def test_profiles_stay_in_the_proved_box_and_conserve_spatial_integral(self):
        box = model.existence_box()
        for z in np.linspace(-0.03, 0.03, 7):
            y = model.series_jet(float(z))[0]
            self.assertTrue(np.all(y >= np.array(box["lower"])))
            self.assertTrue(np.all(y <= np.array(box["upper"])))
            self.assertClose(model.spatial_integral(y), -0.087890625)

    def test_spatial_integral_gradient_annihilates_vector_field(self):
        y, step = self.data["state"], 1e-6
        gradient = np.array([(model.spatial_integral(y+step*e)-model.spatial_integral(y-step*e))/(2*step)
                             for e in np.eye(8)])
        self.assertClose(gradient @ model.rhs(y), 0)

    def test_simultaneous_channel_basis_change_does_not_change_gauge_density(self):
        y = self.data["state"]
        _, rotation = np.linalg.eigh(model.TRIAD)
        rotated = np.r_[rotation.T @ y[:3], rotation.T @ y[3:6], y[6:]]
        actual = model.rhs(rotated, mass=rotation.T @ model.TRIAD @ rotation)
        target = model.rhs(y)
        self.assertClose(actual, np.r_[rotation.T @ target[:3], rotation.T @ target[3:6], target[6:]])

    def test_solution_is_not_a_single_resonance_eigenmode(self):
        d = self.data
        _, vectors = np.linalg.eigh(model.TRIAD)
        u, v = vectors.T @ d["state"][:3], vectors.T @ d["state"][3:6]
        self.assertTrue(np.all(u*u+v*v > 0.007))
        torque = model.commutator(d["mass_operator"], d["scalar"])
        self.assertGreater(np.linalg.norm(torque), 1.3)
        self.assertClose(model.gauge_projection(torque), 0)

    def test_all_three_probe_channels_develop_nonzero_local_density(self):
        y = self.data["state"]
        self.assertTrue(np.all(y[:3]**2+y[3:6]**2 > 0))
        self.assertClose(np.linalg.norm(np.array(model.INITIAL)[1:3]), 0)
        self.assertGreater(abs(y[2]), 0.008)

    def test_probe_and_connection_first_jets_in_every_coordinate(self):
        d, step = self.data, 1e-5
        for mu, direction in enumerate(np.eye(4)):
            plus, minus = model.field_data(d["point"]+step*direction), model.field_data(d["point"]-step*direction)
            self.assertClose((plus["psi"]-minus["psi"])/(2*step), d["psi_first"][mu])
            self.assertClose((plus["connection"]-minus["connection"])/(2*step), d["connection_first"][mu])

    def test_current_partial_trace_is_the_same_probe_source_not_an_added_bath(self):
        d = self.data
        u, v = d["state"][:3], d["state"][3:6]
        p0 = model.partial_trace_channels(d["P"])/3
        self.assertClose(model.partial_trace_channels(d["current"])[0], (u @ u+v @ v)*p0)
        self.assertClose(model.partial_trace_channels(d["current"])[1:], 0)
        self.assertGreater(np.linalg.norm(d["current"][3]), 0.025)

    def test_closed_transport_does_not_imply_vanishing_internal_matrix_torque(self):
        d = self.data
        self.assertClose(d["P"] @ d["psi"], d["psi"])
        self.assertClose(d["P_first"]+model.commutator(d["connection"], d["P"]), 0)
        self.assertClose(model.commutator(d["mass_operator"], d["P"]), 0)
        self.assertGreater(np.linalg.norm(model.commutator(d["mass_operator"], d["scalar"])), 1.3)

    def test_full_curved_dirac_and_projected_gauge_ward_equations(self):
        result = model.residuals()
        for name in ("Dirac", "projected_gauge", "projected_current_divergence", "full_Ward"):
            self.assertLess(np.linalg.norm(result[name]), 2e-8, name)
        self.assertGreater(np.linalg.norm(result["unprojected_equation_not_imposed"]), 0.13)
        self.assertGreater(np.linalg.norm(result["full_current_divergence"]), 1.3)

    def test_curved_solution_at_other_radii_and_angles(self):
        for point, radius, eta in (([-0.3, 2.4, 1.2, -0.01], 1.6, -0.7),
                                   ([0.2, 0.5, -0.4, 0.01], 0.8, 0)):
            result = model.residuals(point, radius=radius, eta=eta)
            for name in ("Dirac", "projected_gauge", "projected_current_divergence", "full_Ward"):
                self.assertLess(np.linalg.norm(result[name]), 2e-8, name)

    def test_probe_action_variation_has_partial_trace_source(self):
        d, eps = self.data, 1e-5
        for generator in (np.eye(2), *model.source.transport.PAULI):
            lifted = np.kron(generator, np.eye(3))
            values = []
            for sign in (1, -1):
                b = d["connection"].copy()
                b[0] += 1j*sign*eps*lifted
                values.append(model.dirac.dirac_data(
                    d["psi"], d["psi_first"]+b @ d["psi"], d["mass_operator"],
                    gamma=d["bundle"]["gamma"], metric=d["bundle"]["metric"], spin=d["bundle"]["spin"])["lagrangian"])
            target = -np.trace(generator @ model.partial_trace_channels(d["current"])[0]).real
            self.assertClose((values[0]-values[1])/(2*eps), target)

    def test_full_curvature_action_variation_supplies_multiplicity_in_gauss_equation(self):
        d, eps = self.data, 1e-5
        p = d["P"]
        inv = model.source.load.inverse_metric(d["point"][1], d["radius"])
        values = []
        for sign in (1, -1):
            derivative = d["connection_first"].copy()
            derivative[3, 0] += 1j*sign*eps*p
            f = model.checks.connection_curvature(d["connection"], derivative)
            values.append(-model.source.load.curvature_density(f, inv, model.GAUGE).real)
        target = 3*d["state"][7]/model.GAUGE**2
        self.assertClose((values[0]-values[1])/(2*eps), target)
        rho = np.trace(d["current"][0]).real
        self.assertClose(-rho-3*d["state_first"][7]/model.GAUGE**2, 0)

    def test_changing_trace_multiplicity_is_a_changed_normalization(self):
        y = self.data["state"]
        wrong = model.rhs(y, multiplicity=1)
        right = model.rhs(y)
        self.assertClose(wrong[:7], right[:7])
        self.assertClose(wrong[7], 3*right[7])

    def test_invalid_shapes_parameters_orders_and_intervals(self):
        for bad in (np.eye(3), np.ones((6, 5))):
            with self.assertRaises(ValueError):
                model.partial_trace_channels(bad)
        for multiplicity in (0, 1.5, True):
            with self.assertRaises(ValueError):
                model.rhs(model.INITIAL, multiplicity=multiplicity)
        for order in (1, 81, True):
            with self.assertRaises(ValueError):
                model.coefficients(order)
        with self.assertRaises(ValueError):
            model.rhs(model.INITIAL, gauge=0)
        with self.assertRaises(ValueError):
            model.series_jet(0.031)
        with self.assertRaises(ValueError):
            model.residuals(step=0)

    def test_report_reproduces_results_and_preserves_native_identification_limits(self):
        saved = json.loads((ROOT / "analysis/HC_Triadic_Gauge_Factorization.json").read_text(encoding="utf-8"))
        self.assertEqual(self.report, saved)
        self.assertFalse(self.report["main_TeX_changed"])
        self.assertTrue(self.report["representation_gate"]["same_representations_are_assumed_not_derived"])
        self.assertIn("NOT native C7", self.report["status"])


if __name__ == "__main__":
    unittest.main()
