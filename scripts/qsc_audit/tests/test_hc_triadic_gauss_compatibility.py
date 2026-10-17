"""Fixed triadic Ward torque, Gauss propagation and a curved eigenmode comparison."""
import importlib.util
import itertools
import json
from pathlib import Path
import unittest

import numpy as np


ROOT = Path(__file__).resolve().parents[3]
SPEC = importlib.util.spec_from_file_location(
    "triadic_gauss_compatibility", ROOT / "analysis/HC_Triadic_Gauss_Compatibility.py")
model = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(model)


class HCTriadicGaussCompatibilityTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.data = model.lifted_data()
        cls.report = model.evaluate()

    def assertClose(self, actual, expected, atol=1e-9):
        np.testing.assert_allclose(actual, expected, atol=atol, rtol=3e-8)

    def test_prepared_triad_is_not_millennium_and_has_signed_spectrum(self):
        self.assertClose(model.TRIAD, [[0.6, 0, 4], [0, 0.6, 0.7], [4, 0.7, 0.6]])
        root = np.sqrt(16.49)
        self.assertClose(np.linalg.eigvalsh(model.TRIAD), [0.6-root, 0.6, 0.6+root])
        self.assertTrue(self.report["prepared_resonance"]["not_native_M16_or_measured_masses"])

    def test_selected_eigenvector_has_both_couplings_and_nonzero_mediator(self):
        mass, vector, q = model.eigenmode()
        self.assertClose(vector, np.array([4/np.sqrt(16.49), 0.7/np.sqrt(16.49), 1])/np.sqrt(2))
        self.assertClose(model.TRIAD @ vector, mass*vector)
        self.assertClose(q @ q, q)
        self.assertClose(vector*vector, [8/16.49, 0.245/16.49, 0.5])

    def test_a_weak_basis_state_is_not_repaired_by_relabeling_its_mass(self):
        e = np.array([1, 0, 0])
        leftover = model.TRIAD @ e-0.6*e
        self.assertClose(leftover, [0, 0, 4])
        self.assertClose(np.linalg.norm(leftover), 4)

    def test_dirac_and_temporal_gauss_jets_do_not_impose_spatial_constraint(self):
        jet = model.mixed_initial_jet()
        self.assertClose(jet["constraint"], 0)
        self.assertGreater(np.linalg.norm(jet["constraint_first"]), 0.86)
        self.assertClose(jet["electric_first"], -0.8**2*jet["rho"])

    def test_independent_flat_spinor_solves_matrix_dirac_equation(self):
        probe = model.flat_probe_checks(model.mixed_initial_jet())
        self.assertClose(probe["probe_residual"], 0)

    def test_matrix_bilinears_agree_with_reduced_density_scalar_and_current(self):
        jet = model.stationary_jet([0.4, 0.2, 0.1], [-0.1, 0.3, 0.2],
                                   np.diag([0.1, 0, -0.2]), np.eye(3))
        probe = model.flat_probe_checks(jet)
        self.assertClose(probe["current"][0], jet["rho"])
        self.assertClose(probe["current"][1:3], 0)
        self.assertClose(probe["current"][3], 1j*jet["wedge"])
        self.assertClose(probe["scalar"], jet["scalar"])
        self.assertGreater(np.linalg.norm(probe["current"][3]), 0.1)

    def test_gauss_constraint_derivative_has_exact_commutator_source(self):
        rng = np.random.default_rng(42)
        for _ in range(12):
            matrices = [rng.normal(size=(3, 3)) for _ in range(3)]
            mass, a, electric = [(x+x.T)/2 for x in matrices]
            jet = model.stationary_jet(rng.normal(size=3), rng.normal(size=3), a, electric, mass=mass)
            self.assertClose(jet["constraint_first"], jet["gauge"]**2*jet["torque"])
            probe = model.flat_probe_checks(jet)
            self.assertClose(probe["current_divergence"], -1j*jet["torque"])

    def test_constraint_first_jet_by_independent_finite_variation(self):
        jet = model.stationary_jet([0.4, 0.2, 0.1], [-0.1, 0.3, 0.2],
                                   np.diag([0.1, 0, -0.2]), 0.1*np.eye(3))
        eps = 1e-5
        values = []
        for sign in (1, -1):
            values.append(model.stationary_jet(
                jet["u"]+sign*eps*jet["u_first"], jet["v"]+sign*eps*jet["v_first"],
                jet["a"]+sign*eps*jet["a_first"], jet["electric"]+sign*eps*jet["electric_first"])["constraint"])
        self.assertClose((values[0]-values[1])/(2*eps), jet["constraint_first"])

    def test_scalar_mass_has_no_internal_ward_torque(self):
        jet = model.stationary_jet([0.4, 0.2, 0.1], [-0.1, 0.3, 0.2],
                                   np.diag([0.1, 0, -0.2]), np.eye(3), mass=0.6*np.eye(3))
        self.assertClose(jet["torque"], 0)
        self.assertClose(jet["constraint_first"], 0)

    def test_trace_continuity_does_not_certify_matrix_continuity(self):
        jet = model.mixed_initial_jet()
        divergence = model.flat_probe_checks(jet)["current_divergence"]
        self.assertClose(np.trace(divergence), 0)
        self.assertGreater(np.linalg.norm(divergence), 1.35)

    def test_basis_rotation_cannot_remove_a_nonzero_torque(self):
        jet = model.mixed_initial_jet()
        _, rotation = np.linalg.eigh(model.TRIAD)
        transformed = model.commutator(rotation.T @ model.TRIAD @ rotation,
                                        rotation.T @ jet["scalar"] @ rotation)
        self.assertClose(np.linalg.norm(transformed), np.linalg.norm(jet["torque"]))

    def test_stabilizer_projection_retains_trace_and_removes_commutator_torque(self):
        jet = model.mixed_initial_jet()
        projected = model.centralizer_projection(jet["scalar"])
        self.assertClose(model.commutator(model.TRIAD, projected), 0)
        self.assertClose(np.trace(projected), np.trace(jet["scalar"]))
        self.assertClose(model.centralizer_projection(jet["torque"]), 0)
        self.assertClose(model.centralizer_projection(projected), projected)

    def test_degenerate_stabilizer_keeps_within_eigenspace_coherences(self):
        mass = np.diag([0.6, 0.6, 2])
        matrix = np.ones((3, 3))
        self.assertClose(model.centralizer_projection(matrix, mass), [[1, 1, 0], [1, 1, 0], [0, 0, 1]])
        self.assertClose(model.centralizer_projection(matrix, 0.6*np.eye(3)), matrix)

    def test_initial_zero_torque_is_not_a_preserved_condition_for_arbitrary_gauge_data(self):
        _, vector, _ = model.eigenmode()
        jet = model.stationary_jet(0.5*vector, 0.1*vector, np.diag([0.1, 0.2, 0.3]), np.zeros((3, 3)))
        self.assertClose(jet["constraint"], 0)
        self.assertClose(jet["torque"], 0)
        scalar_first = (np.outer(jet["u_first"], jet["u"])+np.outer(jet["u"], jet["u_first"])
                        -np.outer(jet["v_first"], jet["v"])-np.outer(jet["v"], jet["v_first"]))
        self.assertGreater(np.linalg.norm(model.commutator(model.TRIAD, scalar_first)), 0.1)

    def test_eigenmode_current_and_gauge_remain_in_one_common_commuting_algebra(self):
        _, e, q = model.eigenmode()
        jet = model.stationary_jet(0.5*e, 0.1*e, 0.2*q, 0.03*q)
        for name in ("constraint", "constraint_first", "torque"):
            self.assertClose(jet[name], 0)
        self.assertClose(jet["u_first"], q @ jet["u_first"])
        self.assertClose(jet["v_first"], q @ jet["v_first"])

    def test_new_eigenvalue_has_its_own_valid_picard_box(self):
        box = model.eigenmode_box()
        self.assertEqual(box["interval"], 0.03)
        self.assertLess(box["max_displacement_bound"], 0.07)
        self.assertLess(box["Picard_contraction_bound"], 0.18)
        mass, _, _ = model.eigenmode()
        params = (mass, *model.massive.DEFAULT_PARAMETERS[1:])
        for corner in itertools.product(*zip(box["lower"], box["upper"])):
            state = (*corner, 0, 0)
            bound = np.array(box["rhs_abs_bounds"])
            self.assertTrue(np.all(np.abs(model.massive.rhs(state, params, "hard")[:4]) <= bound+1e-13))
            jacobian = model.massive.jacobian(state, params)[:4, :4]
            self.assertLessEqual(np.max(np.sum(np.abs(jacobian), axis=1)), box["Jacobian_infinity_norm_bound"]+1e-13)

    def test_excluding_the_third_component_has_nonzero_operator_leakage(self):
        gate = model.carrier_gate()
        self.assertClose(gate["leakage"], [[0, 0, 0], [0, 0, 0], [4, 0.7, 0]])
        self.assertClose(np.linalg.norm(gate["leakage"]), np.sqrt(16.49))
        self.assertGreater(np.linalg.norm(model.commutator(model.TRIAD, gate["visible"])), 5)

    def test_positive_eigenmode_is_not_in_a_two_component_visible_sector(self):
        gate = model.carrier_gate()
        self.assertClose(gate["selected_outside_probability"], 0.5)
        self.assertTrue(self.report["carrier_gate"]["native_C7_assignment_of_the_orthogonal_triadic_component_remains_unknown"])

    def test_one_dark_state_is_invariant_but_does_not_close_the_whole_visible_sector(self):
        gate = model.carrier_gate()
        self.assertClose(gate["dark_eigen_residual"], 0)
        self.assertClose(gate["visible"] @ gate["dark_vector"], gate["dark_vector"])
        self.assertClose(model.commutator(model.TRIAD, gate["dark_projector"]), 0)
        self.assertGreater(np.linalg.norm(gate["leakage"]), 4)

    def test_new_series_has_small_defect_on_its_proved_interval(self):
        mass, _, _ = model.eigenmode()
        params = (mass, *model.massive.DEFAULT_PARAMETERS[1:])
        for z in (-0.03, 0.03):
            defect = model.massive.series_defect(z, params=params, initial=model.massive.HARD_INITIAL, domain="hard")
            self.assertLess(defect, 1e-35)

    def test_lifted_projector_and_probe_have_correct_joint_carrier(self):
        d = self.data
        self.assertEqual(d["psi"].shape, (6, 4))
        self.assertClose(d["P"] @ d["P"], d["P"])
        self.assertClose(np.trace(d["P"]), 3)
        self.assertClose(d["P"] @ d["psi"], d["psi"])
        self.assertClose(d["charged_projector"] @ d["psi"], d["psi"])

    def test_lifted_resonance_transport_and_scalar_support_are_compatible(self):
        d = self.data
        self.assertClose(d["P_first"]+model.commutator(d["connection"], d["P"]), 0)
        self.assertClose(model.commutator(d["mass_operator"], d["P"]), 0)
        self.assertClose(model.commutator(d["mass_operator"], d["scalar"]), 0)
        self.assertClose(d["mass_operator"] @ d["psi"], d["eigenvalue"]*d["psi"])

    def test_lifted_probe_and_connection_first_jets_in_all_coordinates(self):
        d, step = self.data, 1e-5
        for mu, direction in enumerate(np.eye(4)):
            plus = model.lifted_data(d["point"]+step*direction)
            minus = model.lifted_data(d["point"]-step*direction)
            self.assertClose((plus["psi"]-minus["psi"])/(2*step), d["psi_first"][mu])
            self.assertClose((plus["connection"]-minus["connection"])/(2*step), d["connection_first"][mu])

    def test_curvature_has_no_hidden_HC_load_residual_on_hard_branch(self):
        self.assertClose(self.data["F"], self.data["G"])
        self.assertGreater(np.linalg.norm(self.data["F"][1, 2]), 0.8)
        self.assertGreater(np.linalg.norm(self.data["F"][3, 0]), 0.02)

    def test_same_probe_yields_all_three_populated_generation_components(self):
        d = self.data
        u, v = d["base"]["state"][:2]
        self.assertClose(d["current_up"][0], (u*u+v*v)*d["charged_projector"])
        self.assertClose(d["current_up"][1:], 0)
        self.assertClose(d["scalar"], (u*u-v*v)*d["charged_projector"])
        density = np.diag(d["current_up"][0]).real.reshape(2, 3).sum(axis=0)
        self.assertTrue(np.all(density > 0))
        self.assertClose(density/density.sum(), d["eigenvector"]**2)

    def test_full_curved_dirac_and_all_sourced_gauge_components(self):
        residuals = model.lifted_residuals()
        for name, value in residuals.items():
            self.assertLess(np.linalg.norm(value), 2e-8, name)

    def test_curve_radius_and_null_load_changes_do_not_spoil_eigenmode_solution(self):
        for point, radius, eta in (([-0.3, 2.4, 1.2, -0.01], 1.6, -0.7),
                                   ([0.2, 0.5, -0.4, 0.01], 0.8, 0)):
            for name, residual in model.lifted_residuals(point, radius=radius, eta=eta).items():
                self.assertLess(np.linalg.norm(residual), 2e-8, name)

    def test_native_hard_and_independent_finite_penalty_domains_remain_distinct(self):
        audit = self.report["native_HC_domain_audit"]
        self.assertIn("thm:closed-master-system", audit["hard_reading"])
        self.assertIn("does not derive algebraic equality", audit["finite_penalty_reading"])
        self.assertTrue(audit["independent_soft_H_equation_is_not_silently_added_to_hard_lift"])
        self.assertTrue(self.report["eigenmode_lift"]["independent_HC_equation_not_solved_or_imposed"])

    def test_invalid_carriers_gauges_steps_and_intervals_are_rejected(self):
        for bad in (np.zeros((2, 2)), np.triu(np.ones((3, 3))), np.eye(3)*np.nan):
            with self.assertRaises(ValueError):
                model.real_mass(bad)
        with self.assertRaises(ValueError):
            model.stationary_jet([0, 0, 0], [0, 0, 0], np.eye(3), np.eye(3), gauge=0)
        with self.assertRaises(ValueError):
            model.eigenmode(-np.eye(3))
        with self.assertRaises(ValueError):
            model.centralizer_projection(np.eye(2))
        with self.assertRaises(ValueError):
            model.lifted_residuals(step=0)
        with self.assertRaises(ValueError):
            model.lifted_data([0.4, 0.9, 0.4, 0.031])

    def test_report_reproduces_results_without_native_or_physical_claim(self):
        saved = json.loads((ROOT / "analysis/HC_Triadic_Gauss_Compatibility.json").read_text(encoding="utf-8"))
        self.assertEqual(self.report, saved)
        self.assertFalse(self.report["main_TeX_changed"])
        self.assertIn("NOT native", self.report["status"])


if __name__ == "__main__":
    unittest.main()
