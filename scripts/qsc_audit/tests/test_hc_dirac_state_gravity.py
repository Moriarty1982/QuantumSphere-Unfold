"""Common-metric triadic Dirac stress, non-null source and first-order backreaction."""
import importlib.util
import json
from pathlib import Path
import unittest

import numpy as np


ROOT = Path(__file__).resolve().parents[3]
SPEC = importlib.util.spec_from_file_location("dirac_state_gravity", ROOT / "analysis/HC_Dirac_State_Gravity.py")
model = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(model)


class HCDiracStateGravityTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.point = np.array([0.08, 0.2, -0.3, 0.1])
        cls.sample = model.common_sample(cls.point)

    def setUp(self):
        self.rng = np.random.default_rng(641)

    def assertClose(self, actual, expected, atol=3e-10):
        np.testing.assert_allclose(actual, expected, atol=atol, rtol=3e-8)

    def test_flat_clifford_and_adjoint_conventions(self):
        for a, b in np.ndindex((4, 4)):
            self.assertClose(model.GAMMA[a] @ model.GAMMA[b]+model.GAMMA[b] @ model.GAMMA[a],
                             -2*model.ETA[a, b]*np.eye(4))
        for gamma in model.GAMMA:
            self.assertClose(model.BETA @ gamma, (model.BETA @ gamma).conj().T)

    def test_previous_mass_matrix_and_intrinsic_mediator_are_retained(self):
        modes = model.mode_family()
        self.assertClose(modes["mass_operator"], model.parent.background.triadic_mass())
        self.assertEqual(modes["mass_operator"][0, 1], 0)
        self.assertGreater(abs(modes["internal"][2]), 0.5)
        self.assertClose(modes["mass_operator"] @ modes["internal"], modes["mass"]*modes["internal"])

    def test_each_spin_mode_has_positive_energy_and_unit_norm(self):
        modes = model.mode_family()
        for k, psi in zip(modes["momenta"], modes["spinors"]):
            h = np.einsum("i,ijk->jk", k, model.WEIGHTS[1:])+modes["mass"]*model.BETA
            self.assertClose(h @ psi, modes["energy"]*psi)
            self.assertClose(np.vdot(psi, psi), 1)
        self.assertGreater(modes["mass"], 0)

    def test_triadic_flat_probe_solves_every_dirac_component(self):
        for phase in (0, 0.4, np.pi):
            modes, psi, derivative, _ = model.probe_jets(self.point, phase)
            full = np.outer(modes["internal"], psi)
            dfull = np.einsum("r,mi->mri", modes["internal"], derivative)
            data = model.dirac_data(full, dfull, modes["mass_operator"])
            self.assertClose(data["residual"], np.zeros((3, 4)))
            self.assertClose(data["lagrangian"], 0)

    def test_flat_probe_analytic_jets_match_independent_differences(self):
        _, psi, first, second = model.probe_jets(self.point)
        step = 1e-6
        for mu, delta in enumerate(step*np.eye(4)):
            plus = model.probe_jets(self.point+delta)
            minus = model.probe_jets(self.point-delta)
            self.assertClose((plus[1]-minus[1])/(2*step), first[mu])
            self.assertClose((plus[2]-minus[2])/(2*step), second[mu])

    def test_mass_trace_identity_and_rest_energy_sign(self):
        data = self.sample["zeroth_matter"]
        self.assertClose(data["trace"], -data["mass_bilinear"].real)
        self.assertGreater(data["stress"][0, 0], 0)
        psi = np.array([[1, 0, 0, 0]], complex)
        derivative = np.zeros((4, 1, 4), complex)
        derivative[0] = -0.6j*psi
        rest = model.dirac_data(psi, derivative, np.array([[0.6]]))
        self.assertClose(rest["stress"], np.diag([0.6, 0, 0, 0]))

    def test_full_stress_matches_the_independent_on_shell_mode_kernel(self):
        modes = model.mode_family()
        q = modes["covectors"][1]-modes["covectors"][0]
        expected = modes["diagonal_stress"]+2*(modes["cross_stress"]*np.exp(1j*q @ self.point)).real
        self.assertClose(self.sample["zeroth_matter"]["stress"], expected)

    def test_interference_conservation_follows_from_the_on_shell_spinor_matrix_elements(self):
        modes = model.mode_family()
        q = modes["covectors"][1]-modes["covectors"][0]
        self.assertClose((model.ETA @ q) @ modes["cross_stress"], np.zeros(4))
        self.assertClose(modes["kernels"].swapaxes(0, 1).conj(), modes["kernels"])

    def test_all_relative_phases_have_strictly_nonzero_mass_trace_in_this_family(self):
        bound = model.mode_family()["mass_bilinear_lower_bound_all_phases"]
        self.assertGreater(bound, 0)
        for phase in 2*np.pi*np.arange(12)/12:
            modes, psi, derivative, _ = model.probe_jets(self.point, phase)
            data = model.dirac_data(psi[None, :], derivative[:, None, :], np.array([[modes["mass"]]]))
            self.assertGreaterEqual(data["mass_bilinear"].real+1e-12, bound)

    def test_dirac_stress_is_invariant_under_a_common_phase(self):
        modes, psi, dpsi, _ = model.probe_jets(self.point)
        phase = np.exp(1.4j)
        a = model.dirac_data(psi[None, :], dpsi[:, None, :], np.array([[modes["mass"]]]))
        b = model.dirac_data(phase*psi[None, :], phase*dpsi[:, None, :], np.array([[modes["mass"]]]))
        self.assertClose(a["stress"], b["stress"])
        self.assertClose(a["current"], b["current"])

    def test_fermionic_fock_operators_have_car_and_the_one_particle_covariance(self):
        lowering = np.array([[0, 1], [0, 0]])
        operators = [np.kron(lowering, np.eye(2)), np.kron(np.diag([1, -1]), lowering)]
        for r, s in np.ndindex((2, 2)):
            self.assertClose(operators[r] @ operators[s].conj().T+operators[s].conj().T @ operators[r],
                             np.eye(4)*int(r == s))
        modes = model.mode_family()
        vector = np.zeros(4, complex)
        vector[2], vector[1] = modes["coefficients"]
        occupation = np.array([[np.vdot(vector, a.conj().T @ b @ vector) for b in operators] for a in operators])
        self.assertClose(occupation, modes["occupation"])
        self.assertClose([np.vdot(vector, a @ vector) for a in operators], [0, 0])
        expected = np.zeros((4, 4), complex)
        for r, s in np.ndindex((2, 2)):
            factor = np.exp(1j*(modes["covectors"][s]-modes["covectors"][r]) @ self.point)/modes["volume"]
            expected += np.vdot(vector, operators[r].conj().T @ operators[s] @ vector)*factor*modes["kernels"][r, s]
        self.assertClose(expected.real, self.sample["zeroth_matter"]["stress"])

    def test_phase_changes_local_stress_but_not_total_energy_or_mass(self):
        sources = []
        for phase in (0, np.pi):
            modes, psi, derivative, _ = model.probe_jets(np.zeros(4), phase)
            data = model.dirac_data(psi[None], derivative[:, None], np.array([[modes["mass"]]]))
            sources.append(data["stress"][0, 0])
            self.assertClose(modes["volume"]*modes["diagonal_stress"][0, 0], modes["energy"])
        self.assertGreater(sources[0], 2*sources[1])

    def test_constant_metric_action_variation_has_the_full_symmetric_stress_including_volume(self):
        psi = self.rng.normal(size=(3, 4))+1j*self.rng.normal(size=(3, 4))
        derivative = self.rng.normal(size=(4, 3, 4))+1j*self.rng.normal(size=(4, 3, 4))
        mass = model.mode_family()["mass_operator"]
        delta = self.rng.normal(size=(4, 4))
        delta = (delta+delta.T)/2
        data = model.dirac_data(psi, derivative, mass)
        step, values = 1e-6, []
        for sign in (1, -1):
            inverse_frame = np.eye(4)+sign*step*delta @ model.ETA/2
            e = np.linalg.inv(inverse_frame)
            metric = e.T @ model.ETA @ e
            gamma = np.einsum("ma,aij->mij", inverse_frame, model.GAMMA)
            varied = model.dirac_data(psi, derivative, mass, gamma, metric)
            values.append(abs(np.linalg.det(e))*varied["lagrangian"])
        self.assertClose((values[0]-values[1])/(2*step), -np.sum(data["stress"]*delta)/2, atol=5e-8)

    def test_random_tetrad_spin_lift_is_compatible_and_has_the_right_adjoint(self):
        e = np.eye(4)+0.02*self.rng.normal(size=(4, 4))
        first = 0.02*self.rng.normal(size=(4, 4, 4))
        data = model.bundle(e, first)
        self.assertClose(data["omega"]+data["omega"].swapaxes(1, 2), np.zeros((4, 4, 4)))
        self.assertClose(data["gamma_compatibility"], np.zeros((4, 4, 4, 4)))
        for spin in data["spin"]:
            self.assertClose(spin.conj().T @ model.BETA+model.BETA @ spin, np.zeros((4, 4)))

    def test_curved_clifford_uses_the_same_metric_as_the_connection(self):
        data = self.sample["metric"]
        inverse = np.linalg.inv(data["metric"])
        for mu, nu in np.ndindex((4, 4)):
            self.assertClose(data["gamma"][mu] @ data["gamma"][nu]+data["gamma"][nu] @ data["gamma"][mu],
                             -2*inverse[mu, nu]*np.eye(4))

    def test_linear_operator_variation_matches_the_full_spin_lift(self):
        modes, psi, derivative, _ = model.probe_jets(self.point)
        h, dh, _ = model.metric_jets(self.point)["h"]
        step, residuals = 1e-5, []
        for sign in (1, -1):
            e = np.eye(4)+sign*step*model.ETA @ h/2
            first = sign*step*np.einsum("ab,lbc->lac", model.ETA, dh)/2
            data = model.bundle(e, first)
            residuals.append(model.dirac_data(psi[None], derivative[:, None], np.array([[modes["mass"]]]),
                                               data["gamma"], data["metric"], data["spin"])["residual"][0])
        self.assertClose((residuals[0]-residuals[1])/(2*step), model.operator_change(psi, derivative, h, dh))

    def test_the_old_reference_solution_is_not_on_shell_after_switching_to_its_effective_metric(self):
        old = model.old_background_test()
        self.assertLess(np.linalg.norm(old["reference"]["residual"]), 1e-12)
        self.assertGreater(np.linalg.norm(old["curved"]["residual"]), 1)
        self.assertGreater(abs(old["reference"]["mass_bilinear"]), 1)
        self.assertClose(old["reference"]["trace"], -old["reference"]["mass_bilinear"].real)
        self.assertLess(np.linalg.norm(old["bundle"]["gamma_compatibility"]), 1e-8)
        self.assertClose(old["metric_first_error"], np.zeros((4, 4, 4)))
        self.assertClose(old["metric_second_error"], np.zeros((4, 4, 4, 4)))

    def test_homogeneous_polynomial_is_lorenz_gauge_and_solves_every_component(self):
        stress = self.rng.normal(size=(4, 4))
        stress = (stress+stress.T)/2
        _, first, second = model.homogeneous_bar_jets(self.point, stress)
        self.assertClose(np.einsum("mr,rmn->n", model.ETA, first), np.zeros(4))
        self.assertClose(np.einsum("rs,rsmn->mn", model.ETA, second), -2*stress)
        self.assertClose(model.state.linearized_einstein(model.trace_reverse((second,))[0]), stress)

    def test_homogeneous_metric_jets_match_independent_differences(self):
        stress = model.mode_family()["diagonal_stress"]
        value, first, second = model.homogeneous_bar_jets(self.point, stress)
        step = 1e-5
        for mu, delta in enumerate(step*np.eye(4)):
            plus = model.homogeneous_bar_jets(self.point+delta, stress)
            minus = model.homogeneous_bar_jets(self.point-delta, stress)
            self.assertClose((plus[0]-minus[0])/(2*step), first[mu])
            self.assertClose((plus[1]-minus[1])/(2*step), second[mu])

    def test_full_metric_jets_match_independent_differences(self):
        value, first, second = model.metric_jets(self.point)["h"]
        step = 1e-5
        for mu, delta in enumerate(step*np.eye(4)):
            plus = model.metric_jets(self.point+delta)["h"]
            minus = model.metric_jets(self.point-delta)["h"]
            self.assertClose((plus[0]-minus[0])/(2*step), first[mu])
            self.assertClose((plus[1]-minus[1])/(2*step), second[mu])

    def test_full_source_including_positive_diagonal_part_passes_linear_einstein(self):
        self.assertClose(self.sample["linear_Einstein_residual"], np.zeros((4, 4)))
        h = model.metric_jets(self.point)
        self.assertClose(np.einsum("mr,rmn->n", model.ETA, h["bar_h"][1]), np.zeros(4))

    def test_missing_homogeneous_metric_has_exactly_the_previous_unsolved_source(self):
        jets = model.metric_jets(self.point)
        einstein = model.state.linearized_einstein(model.trace_reverse(jets["oscillatory_bar_h"])[2])
        difference = einstein-self.sample["zeroth_matter"]["stress"]
        self.assertClose(difference, -jets["modes"]["diagonal_stress"])
        self.assertGreater(np.linalg.norm(difference), 0.01)

    def test_nonzero_scalar_curvature_is_required_by_the_massive_source(self):
        h = model.metric_jets(self.point)["h"]
        einstein = model.state.linearized_einstein(h[2])
        scalar = -np.sum(model.ETA*einstein)
        self.assertClose(scalar, self.sample["zeroth_matter"]["mass_bilinear"].real)
        self.assertGreater(scalar, 0)

    def test_homogeneous_solution_is_local_not_a_periodic_metric(self):
        stress = model.mode_family()["diagonal_stress"]
        a = model.homogeneous_bar_jets(self.point, stress)[0]
        b = model.homogeneous_bar_jets(self.point+np.array([0, 2*np.pi, 0, 0]), stress)[0]
        self.assertGreater(np.linalg.norm(a-b), 0.01)

    def test_finite_forcing_matches_the_direct_perturbed_dirac_operator(self):
        systems = model.forcing_system()
        for point in (self.point, np.array([0, -0.1, 0.2, 0.4]), np.array([0.03, 0.4, 0.1, -0.2])):
            _, psi, derivative, _ = model.probe_jets(point)
            h, first, _ = model.metric_jets(point)["h"]
            direct = -model.BETA @ model.operator_change(psi, derivative, h, first)
            reconstructed = np.zeros(4, complex)
            for k, system in systems["systems"].items():
                for powers, row in zip(system["basis"], system["forcing"].reshape(-1, 4, 3)):
                    reconstructed += (np.exp(-1j*systems["modes"]["energy"]*point[0]+1j*np.array(k) @ point[1:])
                                      *np.prod(point[1:]**powers)*(row @ np.array([1, point[0], point[0]**2])))
            self.assertClose(reconstructed, direct)

    def test_matrix_exponential_clock_and_initial_data(self):
        for time in (0, float(self.point[0])):
            for data in model.correction_flow(time).values():
                self.assertClose(data["clock"], [1, time, time**2])
                if time == 0:
                    self.assertClose(data["value"], np.zeros_like(data["value"]))

    def test_correction_analytic_jets_match_spatial_differences(self):
        value, first = model.correction_jets(self.point)
        step = 1e-5
        for mu in range(1, 4):
            delta = step*np.eye(4)[mu]
            plus, minus = model.correction_jets(self.point+delta)[0], model.correction_jets(self.point-delta)[0]
            self.assertClose((plus-minus)/(2*step), first[mu])

    def test_correction_time_derivative_matches_independent_matrix_exponentials(self):
        value, first = model.correction_jets(self.point)
        step = 1e-5
        plus = model.correction_jets(self.point+np.array([step, 0, 0, 0]))[0]
        minus = model.correction_jets(self.point-np.array([step, 0, 0, 0]))[0]
        self.assertClose((plus-minus)/(2*step), first[0])

    def test_first_order_probe_reaction_is_nonzero_and_solves_all_dirac_components(self):
        self.assertGreater(np.linalg.norm(self.sample["correction"]), 1e-5)
        self.assertClose(self.sample["linear_Dirac_residual"], np.zeros(4))
        modes, psi, derivative, _ = model.probe_jets(self.point)
        h, first, _ = model.metric_jets(self.point)["h"]
        self.assertGreater(np.linalg.norm(model.operator_change(psi, derivative, h, first)), 1e-4)

    def test_first_order_probe_equation_holds_away_from_the_report_point(self):
        for point in (np.array([0.08, -0.2, 0.1, 0.3]), np.array([0, 0.4, 0.2, -0.1])):
            modes, psi, derivative, _ = model.probe_jets(point)
            first_value, first_derivative = model.correction_jets(point)
            h, dh, _ = model.metric_jets(point)["h"]
            residual = (1j*np.einsum("mij,mj->i", model.GAMMA, first_derivative)-modes["mass"]*first_value
                        +model.operator_change(psi, derivative, h, dh))
            self.assertClose(residual, np.zeros(4))

    def test_full_nonlinear_einstein_and_dirac_residuals_are_second_order(self):
        values = [model.common_sample(self.point, strength=s) for s in (0.04, 0.02, 0.01)]
        for key in ("Einstein_residual", "Dirac"):
            norms = [np.linalg.norm(v["matter"]["residual"] if key == "Dirac" else v[key]) for v in values]
            self.assertClose(norms[0]/norms[1], 4, atol=0.003)
            self.assertClose(norms[1]/norms[2], 4, atol=0.003)

    def test_current_ward_identity_keeps_the_residual_in_the_curved_common_frame(self):
        point, strength = self.point, 0.02
        modes, value, derivative, _ = model.probe_jets(point)
        first_value, first_derivative = model.correction_jets(point)
        psi, dpsi = value+strength*first_value, derivative+strength*first_derivative
        sample = model.common_sample(point, strength=strength)
        bundle = sample["metric"]
        first_current = np.array([[2*np.vdot(psi, model.BETA @ gamma @ d).real
                                   +np.vdot(psi, model.BETA @ bundle["gamma_first"][mu, nu] @ psi).real
                                   for nu, gamma in enumerate(bundle["gamma"])] for mu, d in enumerate(dpsi)])
        divergence = np.trace(first_current)+np.einsum("mmn,n->", bundle["curvature"]["connection"], sample["matter"]["current"])
        residual = sample["matter"]["residual"]
        full_psi = np.outer(modes["internal"], psi)
        rhs = 2*np.vdot(full_psi, residual @ model.BETA.T).imag
        self.assertClose(divergence, rhs)

    def test_native_real_bilinear_coframe_is_still_degenerate_not_the_independent_metric(self):
        modes, psi, derivative, _ = model.probe_jets(self.point)
        coframe = model.parent.background.coframe(np.outer(modes["internal"], psi),
                                                  np.einsum("r,mi->mri", modes["internal"], derivative), model.WEIGHTS)
        self.assertEqual(np.linalg.matrix_rank(coframe, tol=1e-12), 1)
        self.assertClose(coframe[:, 0], np.zeros(4))
        self.assertGreater(np.linalg.norm(coframe-np.eye(4)), 1)

    def test_invalid_internal_mass_is_not_treated_as_a_real_dirac_action(self):
        with self.assertRaises(ValueError):
            model.dirac_data(np.ones((1, 4)), np.zeros((4, 1, 4)), np.array([[1j]]))

    def test_saved_report_preserves_order_native_and_quantum_scope(self):
        saved = json.loads((ROOT / "analysis/HC_Dirac_State_Gravity.json").read_text(encoding="utf-8"))
        self.assertEqual(saved, model.evaluate())
        self.assertFalse(saved["main_TeX_changed"])
        self.assertTrue(saved["common_action"]["independent_metric_not_native_bilinear_constraint"])
        self.assertTrue(saved["local_weak_gravity_construction"]["only_first_order_not_an_exact_nonlinear_solution"])


if __name__ == "__main__":
    unittest.main()
