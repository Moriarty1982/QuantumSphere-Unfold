"""Readout gauge contracts, inconsistent common truncation and spectral response."""
import importlib.util
import itertools
import json
from pathlib import Path
import unittest

import mpmath as mp
import numpy as np


ROOT = Path(__file__).resolve().parents[3]
SPEC = importlib.util.spec_from_file_location(
    "spectral_gauge_completion", ROOT / "analysis/HC_Spectral_Gauge_Completion.py")
model = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(model)


class HCSpectralGaugeCompletionTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.data = model.field_data()
        cls.report = model.evaluate()

    def assertClose(self, actual, expected, atol=1e-9):
        np.testing.assert_allclose(actual, expected, atol=atol, rtol=4e-8)

    def test_analytic_modal_basis_preserves_the_signed_prepared_operator(self):
        mass, rotation = model.modal_basis()
        self.assertClose(rotation.T @ rotation, np.eye(3))
        self.assertClose(rotation @ np.diag(mass) @ rotation.T, model.factor.TRIAD)
        self.assertLess(mass[0], 0)

    def test_spectral_projectors_resolve_identity_and_commute_with_resonance(self):
        projectors = model.modal_projectors()
        self.assertClose(sum(projectors), np.eye(6))
        mass = np.kron(np.eye(2), model.factor.TRIAD)
        for i, p in enumerate(projectors):
            self.assertClose(p @ p, p)
            self.assertClose(np.trace(p), 2)
            self.assertClose(model.commutator(p, mass), 0)
            for j, q in enumerate(projectors):
                self.assertClose(p @ q, p if i == j else np.zeros((6, 6)))

    def test_centralizer_projection_is_trace_preserving_and_idempotent(self):
        rng = np.random.default_rng(10)
        x = rng.normal(size=(6, 6))+1j*rng.normal(size=(6, 6))
        projected = model.spectral_projection(x)
        self.assertClose(model.spectral_projection(projected), projected)
        self.assertClose(np.trace(projected), np.trace(x))
        self.assertClose(model.commutator(projected, self.data["mass_operator"]), 0)

    def test_common_gauge_algebra_is_a_proper_subalgebra_of_spectral_one(self):
        x = np.kron(model.intertwiners.PAULI[0], np.outer(model.modal_basis()[1][:, 0], model.modal_basis()[1][:, 0]))
        self.assertClose(model.spectral_projection(x), x)
        self.assertGreater(np.linalg.norm(x-model.factor.gauge_projection(x)), 1)
        self.assertEqual(model.intertwiners.commutant([self.data["mass_operator"]])["dimension"], 12)

    def test_previous_common_solution_fails_the_additional_spectral_gauss_equations(self):
        old = model.factor.residuals()
        self.assertLess(np.linalg.norm(old["projected_gauge"]), 2e-8)
        extra = model.spectral_projection(old["unprojected_equation_not_imposed"])
        self.assertGreater(np.linalg.norm(extra), 0.063)
        y = model.factor.field_data()["state"]
        _, rotation = model.modal_basis()
        density = (rotation.T @ y[:3])**2+(rotation.T @ y[3:6])**2
        expected_norm = model.GAUGE**2*np.linalg.norm(density-np.mean(density))
        self.assertClose(np.linalg.norm(extra), expected_norm)

    def test_equal_initial_modal_density_does_not_remain_equal_generically(self):
        initial = np.tile([0.5/np.sqrt(3), 0.1/np.sqrt(3), 0, 0.03], (3, 1))
        first = model.rhs(initial)
        density = np.sum(initial[:, :2]**2, axis=1)
        rate = 2*np.sum(initial[:, :2]*first[:, :2], axis=1)
        self.assertClose(density, np.repeat(0.26/3, 3))
        self.assertGreater(np.ptp(rate), 0.5)
        self.assertClose(rate, 4*model.modal_basis()[0]*initial[:, 0]*initial[:, 1])

    def test_new_branch_starts_with_identical_full_probe_and_connection_data(self):
        point = np.array([0.4, 0.9, 0.4, 0])
        d, old = model.field_data(point), model.factor.field_data(point)
        for name in ("psi", "psi_first", "connection", "connection_first", "F", "current"):
            self.assertClose(d[name], old[name])

    def test_sourced_second_potential_derivatives_split_without_new_free_parameters(self):
        y, dy, ddy = model.series_jet(0)
        density = y[:, 0]**2+y[:, 1]**2
        self.assertClose(dy[:, 3], -model.GAUGE**2*density)
        self.assertClose(ddy[:, 2], -model.GAUGE**2*density)
        self.assertGreater(np.ptp(dy[:, 3]), 0.07)
        self.assertClose(y[:, 2], 0)
        self.assertClose(y[:, 3], 0.03)

    def test_analytic_jacobian_matches_independent_differences(self):
        y, step = self.data["state"], 1e-6
        directions = np.eye(12).reshape(12, 3, 4)
        numerical = np.column_stack([((model.rhs(y+step*e)-model.rhs(y-step*e))/(2*step)).ravel() for e in directions])
        self.assertClose(numerical, model.jacobian(y))

    def test_taylor_first_and_second_jets(self):
        _, first, second = model.series_jet()
        plus, minus = model.series_jet(0.02001), model.series_jet(0.01999)
        self.assertClose((plus[0]-minus[0])/0.00002, first)
        self.assertClose((plus[1]-minus[1])/0.00002, second)

    def test_taylor_defect_converges_on_signed_modes(self):
        defects = [model.series_defect(0.03, n) for n in (8, 16, 32)]
        self.assertGreater(defects[0], defects[1]*1e10)
        self.assertGreater(defects[1], defects[2]*1e15)
        self.assertLess(defects[-1], 1e-44)

    def test_taylor_matches_independent_installed_ode_implementation_for_all_modes(self):
        with mp.workdps(40):
            masses, rotation = model.modal_basis(high_precision=True)
            actual = model.series_jet(high_precision=True)[0]
            for i, mass in enumerate(masses):
                def rates(z, y):
                    u, v, a, electric = y
                    return [(mp.mpf(".9")-a+mass)*v, (mass-mp.mpf(".9")+a)*u,
                            electric, -mp.mpf(".64")*(u*u+v*v)]
                y0 = [mp.mpf(".5")*rotation[0][i], mp.mpf(".1")*rotation[0][i], 0, mp.mpf(".03")]
                expected = mp.odefun(rates, 0, y0, tol=mp.mpf("1e-32"), degree=20)(mp.mpf(".02"))
                self.assertLess(float(max(abs(a-b) for a, b in zip(actual[i], expected))), 1e-30)

    def test_picard_bounds_on_each_separable_modal_box(self):
        box = model.existence_box()
        lower, upper, bounds = (np.array(box[name]) for name in ("lower", "upper", "rhs_abs_bounds"))
        for i in range(3):
            for corner in itertools.product(*zip(lower[i], upper[i])):
                y = model.initial_modes()
                y[i] = corner
                self.assertTrue(np.all(abs(model.rhs(y)[i]) <= bounds[i]+1e-13))
                self.assertLessEqual(np.max(np.sum(abs(model.jacobian(y)), axis=1)), box["Jacobian_infinity_norm_bound"]+1e-13)
        self.assertLess(box["max_displacement_bound"], 0.06)
        self.assertLess(box["Picard_contraction_bound"], 0.18)

    def test_profiles_stay_inside_the_reference_box_and_conserve_each_spatial_integral(self):
        box = model.existence_box()
        initial = model.spatial_integrals(model.initial_modes())
        for z in np.linspace(-0.03, 0.03, 7):
            y = model.series_jet(float(z))[0]
            self.assertTrue(np.all(y >= np.array(box["lower"])))
            self.assertTrue(np.all(y <= np.array(box["upper"])))
            self.assertClose(model.spatial_integrals(y), initial)
        self.assertClose(np.sum(initial), -0.087890625)

    def test_source_induced_potential_commutes_with_resonance_but_not_channel_labels(self):
        a = self.data["potential_channel_matrix"]
        self.assertClose(model.commutator(a, model.factor.TRIAD), 0)
        self.assertGreater(np.linalg.norm(model.commutator(a, np.diag([1, 0, 0]))), 3e-6)
        self.assertGreater(np.linalg.norm(a-np.trace(a)*np.eye(3)/3), 1e-5)

    def test_full_probe_and_connection_jets_at_every_coordinate(self):
        d, step = self.data, 1e-5
        for mu, direction in enumerate(np.eye(4)):
            plus, minus = model.field_data(d["point"]+step*direction), model.field_data(d["point"]-step*direction)
            self.assertClose((plus["psi"]-minus["psi"])/(2*step), d["psi_first"][mu])
            self.assertClose((plus["connection"]-minus["connection"])/(2*step), d["connection_first"][mu])

    def test_same_probe_supplies_all_three_spectral_charge_densities(self):
        d = self.data
        density = np.sum(d["state"][:, :2]**2, axis=1)
        for i, p in enumerate(model.modal_projectors()):
            self.assertClose(p @ d["current"][0] @ p, density[i]*p @ d["P"])
            self.assertClose(p @ d["current"][3] @ p, 0)
        self.assertTrue(np.all(density > 0.007))

    def test_full_curved_probe_and_all_fixed_resonance_gauge_equations(self):
        result = model.residuals()
        for name in ("Dirac", "spectral_gauge", "spectral_current_divergence", "full_Ward"):
            self.assertLess(np.linalg.norm(result[name]), 2e-8, name)
        self.assertGreater(np.linalg.norm(result["unprojected_U6_equation_not_imposed"]), 0.12)

    def test_curved_solution_at_other_radii_and_null_loads(self):
        for point, radius, eta in (([-0.3, 2.4, 1.2, -0.01], 1.6, -0.7), ([0.2, 0.5, -0.4, 0.01], 0.8, 0)):
            result = model.residuals(point, radius=radius, eta=eta)
            for name in ("Dirac", "spectral_gauge", "spectral_current_divergence", "full_Ward"):
                self.assertLess(np.linalg.norm(result[name]), 2e-8, name)

    def test_closed_sector_transport_is_retained_without_channel_label_locks(self):
        d = self.data
        self.assertClose(d["P_first"]+model.commutator(d["connection"], d["P"]), 0)
        self.assertClose(d["P"] @ d["psi"], d["psi"])
        self.assertClose(model.commutator(d["mass_operator"], d["P"]), 0)

    def test_each_modal_curvature_action_has_unit_channel_multiplicity(self):
        d, eps = self.data, 1e-5
        inverse = model.source.load.inverse_metric(d["point"][1], d["radius"])
        for i, p in enumerate(model.modal_projectors()):
            charged = p @ d["P"]
            values = []
            for sign in (1, -1):
                derivative = d["connection_first"].copy()
                derivative[3, 0] += 1j*sign*eps*charged
                f = model.checks.connection_curvature(d["connection"], derivative)
                values.append(-model.source.load.curvature_density(f, inverse, model.GAUGE).real)
            self.assertClose((values[0]-values[1])/(2*eps), d["state"][i, 3]/model.GAUGE**2)

    def test_modal_probe_action_variations_have_their_own_source(self):
        d, eps = self.data, 1e-5
        for i, p in enumerate(model.modal_projectors()):
            charged = p @ d["P"]
            values = []
            for sign in (1, -1):
                b = d["connection"].copy()
                b[0] += 1j*sign*eps*charged
                values.append(model.dirac.dirac_data(d["psi"], d["psi_first"]+b @ d["psi"], d["mass_operator"],
                    gamma=d["bundle"]["gamma"], metric=d["bundle"]["metric"], spin=d["bundle"]["spin"])["lagrangian"])
            density = np.sum(d["state"][i, :2]**2)
            self.assertClose((values[0]-values[1])/(2*eps), -density)
            self.assertClose(-density-d["state_first"][i, 3]/model.GAUGE**2, 0)

    def test_source_covariance_does_not_require_source_invariance(self):
        d = self.data
        generator = model.modal_projectors()[0]
        unitary = np.eye(6)+(np.exp(0.4j)-1)*generator
        self.assertClose(model.commutator(generator, d["mass_operator"]), 0)
        self.assertGreater(np.linalg.norm(model.commutator(generator, d["current"][0])), 0.15)
        transformed = unitary @ d["current"][0] @ unitary.conj().T
        self.assertClose(model.spectral_projection(transformed), model.spectral_projection(d["current"][0]))

    def test_native_cross_readout_is_present_but_gauge_law_is_not_assumed_proved(self):
        text = (ROOT / "sources/research/parts/v470/12_structural_core.tex").read_text(encoding="utf-8")
        self.assertIn("Cross-bilinear geometry channel", text)
        self.assertIn("and similarly with probes exchanged", text)
        self.assertTrue(self.report["native_cross_readout_gate"]["state_independent_fixed_observable_invariance_is_a_condition_not_yet_a_native_gauge_law"])

    def test_fixed_cross_readout_reduces_resonance_commutant_without_assuming_label_projectors(self):
        cross = model.cross_readout_operator()
        basis = model.intertwiners.commutant([self.data["mass_operator"], cross])["basis"]
        self.assertEqual(len(basis), 4)
        for generator in basis:
            self.assertClose(model.factor.gauge_projection(generator), generator)
        self.assertEqual(self.report["native_cross_readout_gate"]["resonance_only_dimension"], 12)

    def test_cross_operator_and_resonance_generate_the_channel_matrix_units(self):
        cross, mass = model.cross_readout_operator(), self.data["mass_operator"]
        p1, p2 = cross @ cross.conj().T, cross.conj().T @ cross
        p3 = np.eye(6)-p1-p2
        e13, e23 = np.zeros((3, 3)), np.zeros((3, 3))
        e13[0, 2], e23[1, 2] = 1, 1
        self.assertClose(p1 @ mass @ p3/4, np.kron(np.eye(2), e13))
        self.assertClose(p2 @ mass @ p3/0.7, np.kron(np.eye(2), e23))

    def test_fixed_and_covariantly_transformed_cross_readouts_are_distinct_contracts(self):
        gate = self.report["native_cross_readout_gate"]
        self.assertClose(gate["fixed_readout_before"], 1)
        self.assertGreater(abs(gate["fixed_readout_after"]-1), 0.03)
        self.assertClose(gate["covariantly_transformed_readout_after"], 1)
        self.assertGreater(gate["same_generator_fixed_readout_commutator_norm"], 0.98)

    def test_invalid_shapes_orders_intervals_and_steps(self):
        with self.assertRaises(ValueError):
            model.spectral_projection(np.eye(3))
        with self.assertRaises(ValueError):
            model.rhs(np.zeros(12))
        for order in (1, 81, True):
            with self.assertRaises(ValueError):
                model.coefficients(order)
        with self.assertRaises(ValueError):
            model.series_jet(0.031)
        with self.assertRaises(ValueError):
            model.residuals(step=0)

    def test_saved_results_reproduce_with_explicit_native_scope_limits(self):
        saved = json.loads((ROOT / "analysis/HC_Spectral_Gauge_Completion.json").read_text(encoding="utf-8"))

        def compare(actual, expected):
            if isinstance(expected, float):
                self.assertClose(actual, expected)
            elif isinstance(expected, dict):
                self.assertEqual(actual.keys(), expected.keys())
                for key, value in expected.items():
                    compare(actual[key], value)
            elif isinstance(expected, list):
                self.assertEqual(len(actual), len(expected))
                for a, b in zip(actual, expected):
                    compare(a, b)
            else:
                self.assertEqual(actual, expected)

        compare(self.report, saved)
        self.assertFalse(self.report["main_TeX_changed"])
        self.assertTrue(self.report["gauge_field_space"]["maximal_compatible_algebra_is_a_declared_choice_not_the_native_gauge_group"])
        self.assertIn("NOT native gauge selection", self.report["status"])


if __name__ == "__main__":
    unittest.main()
