"""Keep real action, field-space variations, matrix currents and charge balance together."""
from pathlib import Path
import importlib.util
import json
import unittest

import numpy as np


ROOT = Path(__file__).resolve().parents[3]
SPEC = importlib.util.spec_from_file_location("hc_real_probe", ROOT / "analysis/HC_Real_Probe_Current_Closure.py")
action = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(action)


class HCRealProbeCurrentClosureTests(unittest.TestCase):
    def setUp(self):
        self.e = action.example_fields()
        self.rng = np.random.default_rng(167)
        self.zero = np.zeros((4, *self.e["psi"].shape), dtype=complex)

    def assertClose(self, actual, expected, atol=3e-12):
        np.testing.assert_allclose(actual, expected, atol=atol, rtol=2e-9)

    def hermitian(self, size=2):
        value = self.rng.normal(size=(size, size))+1j*self.rng.normal(size=(size, size))
        return (value+value.conj().T)/2

    def generic_probe(self):
        return self.rng.normal(size=(2, 2))+1j*self.rng.normal(size=(2, 2))

    def currents(self, psi=None):
        return action.probe_currents(self.e["psi"] if psi is None else psi, self.e["weights"], self.e["spin_metric"])

    def real_L(self, psi=None, derivatives=None, gauge=None, hc=None):
        e = self.e
        return action.real_probe_density(e["psi"] if psi is None else psi,
                                          self.zero if derivatives is None else derivatives,
                                          e["gauge"] if gauge is None else gauge, e["hc"] if hc is None else hc,
                                          e["weights"], e["spin_metric"], e["mass"], e["yukawa"])

    def rates(self, psi=None, n=None, coupling=None):
        e = self.e
        return action.homogeneous_probe_rates(e["psi"] if psi is None else psi, e["gauge"], e["hc"],
                                              e["weights"], e["spin_metric"], e["n"] if n is None else n,
                                              e["coupling"] if coupling is None else coupling, e["mass"], e["yukawa"])

    def residual(self, psi, derivatives):
        e = self.e
        return action.probe_residual(psi, derivatives, e["gauge"], e["hc"], e["weights"],
                                      e["spin_metric"], e["mass"], e["yukawa"])

    def system(self, psi=None, gauge=None, hc=None, target=None):
        e = self.e
        return action.constant_field_system(e["psi"] if psi is None else psi, e["gauge"] if gauge is None else gauge,
                                             e["hc"] if hc is None else hc, e["target"] if target is None else target,
                                             e["weights"], e["spin_metric"], e["n"], e["coupling"], e["penalty"],
                                             e["mass"], e["yukawa"])

    def test_matrix_currents_equal_direct_component_contractions(self):
        psi, e = self.generic_probe(), self.e
        currents = self.currents(psi)
        for matrix, weight in zip([*currents["gauge"], currents["scalar"]], [*e["weights"], e["spin_metric"]]):
            expected = np.einsum("gs,st,ht->gh", psi, weight.T, psi.conj())
            self.assertClose(matrix, expected)
            self.assertClose(matrix, matrix.conj().T)

    def test_gauge_and_yukawa_sources_are_variations_of_the_same_real_probe_density(self):
        psi, step = self.generic_probe(), 1e-5
        direction, e = self.hermitian(), self.e
        currents = self.currents(psi)
        for mu in range(4):
            change = np.zeros_like(e["gauge"])
            change[mu] = direction
            derivative = (self.real_L(psi, gauge=e["gauge"]+step*change)-self.real_L(psi, gauge=e["gauge"]-step*change))/(2*step)
            self.assertClose(derivative, -np.trace(direction @ currents["gauge"][mu]).real, atol=2e-10)
        derivative = (self.real_L(psi, hc=e["hc"]+step*direction)-self.real_L(psi, hc=e["hc"]-step*direction))/(2*step)
        self.assertClose(derivative, -e["yukawa"]*np.trace(direction @ currents["scalar"]).real, atol=2e-10)

    def test_real_part_of_literal_probe_density_equals_the_symmetric_density_for_any_real_kappa(self):
        psi, e = self.generic_probe(), self.e
        derivatives = self.rng.normal(size=self.zero.shape)+1j*self.rng.normal(size=self.zero.shape)
        for coupling in [-1, 0, 0.4, 2]:
            literal = action.literal_probe_density(psi, derivatives, e["gauge"], e["hc"], e["weights"],
                                                    e["spin_metric"], e["n"], coupling, e["mass"], e["yukawa"])
            self.assertClose(literal.real, self.real_L(psi, derivatives))

    def test_hc_transport_changes_only_the_imaginary_part_of_the_literal_density(self):
        e = self.e
        inputs = [e["psi"], self.zero, e["gauge"], e["hc"], e["weights"], e["spin_metric"], e["n"]]
        changed = action.literal_probe_density(*inputs, e["coupling"], e["mass"], e["yukawa"])
        unchanged = action.literal_probe_density(*inputs, 0, e["mass"], e["yukawa"])
        self.assertClose(changed-unchanged, 0.56j)

    def test_general_noncommuting_hermitian_projection_keeps_only_the_commutator(self):
        k, h = self.hermitian(), self.hermitian()
        ordered = 1j*k @ h
        self.assertClose((ordered+ordered.conj().T)/2, 0.5j*(k @ h-h @ k))
        self.assertGreater(np.linalg.norm(ordered-(ordered+ordered.conj().T)/2), 0.1)

    def test_real_probe_euler_derivative_matches_complex_constant_probe_variations(self):
        psi, direction, step = self.generic_probe(), self.generic_probe(), 1e-5
        residual = self.residual(psi, self.zero)
        for delta in [direction, 1j*direction]:
            derivative = (self.real_L(psi+step*delta)-self.real_L(psi-step*delta))/(2*step)
            self.assertClose(derivative, 2*np.vdot(delta, residual).real, atol=5e-10)

    def test_probe_density_is_covariant_under_local_unitary_gauge_change(self):
        e, psi = self.e, self.generic_probe()
        derivatives = self.rng.normal(size=self.zero.shape)+1j*self.rng.normal(size=self.zero.shape)
        raw = self.generic_probe()
        u, _ = np.linalg.qr(raw)
        velocity = np.array([self.hermitian() for _ in range(4)])
        du = 1j*velocity @ u
        new_psi = u @ psi
        new_derivatives = u @ derivatives+du @ psi
        new_gauge = u @ e["gauge"] @ u.conj().T+1j*du @ u.conj().T
        new_h = u @ e["hc"] @ u.conj().T
        self.assertClose(self.real_L(new_psi, new_derivatives, new_gauge, new_h), self.real_L(psi, derivatives))
        before = action.literal_probe_density(psi, derivatives, e["gauge"], e["hc"], e["weights"], e["spin_metric"],
                                               e["n"], e["coupling"], e["mass"], e["yukawa"])
        after = action.literal_probe_density(new_psi, new_derivatives, new_gauge, new_h, e["weights"], e["spin_metric"],
                                              e["n"], e["coupling"], e["mass"], e["yukawa"])
        self.assertClose(after, before)

    def test_generation_currents_transform_by_the_same_unitary_conjugation(self):
        psi = self.generic_probe()
        u, _ = np.linalg.qr(self.generic_probe())
        before, after = self.currents(psi), self.currents(u @ psi)
        self.assertClose(after["gauge"], u @ before["gauge"] @ u.conj().T)
        self.assertClose(after["scalar"], u @ before["scalar"] @ u.conj().T)

    def test_common_spin_basis_change_leaves_internal_currents_unchanged(self):
        psi, e = self.generic_probe(), self.e
        u, _ = np.linalg.qr(self.generic_probe())
        before = self.currents(psi)
        after = action.probe_currents(psi @ u.T, u @ e["weights"] @ u.conj().T, u @ e["spin_metric"] @ u.conj().T)
        self.assertClose(after["gauge"], before["gauge"])
        self.assertClose(after["scalar"], before["scalar"])

    def test_matter_ward_identity_holds_off_shell_for_arbitrary_probe_jets(self):
        e, psi = self.e, self.generic_probe()
        derivatives = self.rng.normal(size=self.zero.shape)+1j*self.rng.normal(size=self.zero.shape)
        residual = self.residual(psi, derivatives)
        current = self.currents(psi)
        divergence = action.covariant_current_divergence(psi, derivatives, e["gauge"], e["weights"], e["spin_metric"])
        left = divergence+1j*e["yukawa"]*(e["hc"] @ current["scalar"]-current["scalar"] @ e["hc"])
        right = 1j*(psi @ residual.conj().T-residual @ psi.conj().T)
        self.assertClose(left, right)

    def test_on_shell_real_probe_current_exchanges_nonabelian_charge_but_conserves_its_trace(self):
        psi, e = self.generic_probe(), self.e
        rates = self.rates(psi)
        derivatives = self.zero.copy()
        derivatives[0] = rates["real_action_rate"]
        self.assertClose(self.residual(psi, derivatives), np.zeros_like(psi))
        divergence = action.covariant_current_divergence(psi, derivatives, e["gauge"], e["weights"], e["spin_metric"])
        scalar = self.currents(psi)["scalar"]
        exchange = -1j*e["yukawa"]*(e["hc"] @ scalar-scalar @ e["hc"])
        self.assertClose(divergence, exchange)
        self.assertGreater(np.linalg.norm(exchange), 0.01)
        self.assertAlmostEqual(np.trace(divergence).real, 0)

    def test_homogeneous_real_action_preserves_the_positive_temporal_norm(self):
        rates = self.rates(self.generic_probe())
        self.assertGreater(rates["norm"], 0)
        self.assertAlmostEqual(rates["real_norm_rate"], 0)

    def test_raw_hc_transport_solves_a_different_ordered_probe_equation(self):
        e, psi = self.e, self.generic_probe()
        derivatives = self.zero.copy()
        derivatives[0] = self.rates(psi)["raw_equation_rate"]
        residual = self.residual(psi, derivatives)
        slash = np.einsum("m,mij->ij", e["n"], e["weights"])
        source = 1j*e["coupling"]*e["hc"] @ psi @ slash.T
        self.assertClose(residual+source, np.zeros_like(psi))
        self.assertGreater(np.linalg.norm(residual), 0.1)

    def test_raw_norm_balance_matches_the_derived_local_source(self):
        rates = self.rates()
        self.assertClose(rates["raw_norm_rate"], -1.12)
        self.assertClose(rates["raw_norm_rate"], rates["raw_balance"])

    def test_reversing_null_axis_reverses_raw_norm_source_not_the_real_probe_action(self):
        forward, backward = self.rates(), self.rates(n=-self.e["n"])
        self.assertClose(forward["raw_norm_rate"], -backward["raw_norm_rate"])
        self.assertClose(forward["real_action_rate"], backward["real_action_rate"])

    def test_instantaneously_dark_null_spinor_is_not_a_general_autonomy_claim(self):
        psi = self.e["psi"].copy()
        psi[:, 1] *= -1
        rates = self.rates(psi)
        self.assertClose(rates["raw_equation_rate"], rates["real_action_rate"])
        self.assertAlmostEqual(rates["raw_norm_rate"], 0)

    def test_zero_kappa_removes_the_difference_between_the_probe_laws(self):
        rates = self.rates(coupling=0)
        self.assertClose(rates["raw_equation_rate"], rates["real_action_rate"])

    def test_nontrivial_positive_time_comparison_is_kept_in_the_norm_balance(self):
        e = self.e
        weights = e["weights"].copy()
        weights[0] = np.array([[2, 0.2j], [-0.2j, 1]])
        rates = action.homogeneous_probe_rates(self.generic_probe(), e["gauge"], e["hc"], weights,
                                               e["spin_metric"], e["n"], e["coupling"], e["mass"], e["yukawa"])
        self.assertAlmostEqual(rates["real_norm_rate"], 0)
        self.assertClose(rates["raw_norm_rate"], rates["raw_balance"])

    def test_full_candidate_gauge_hc_and_target_variations_match_their_joint_action(self):
        e, psi, direction, step = self.e, self.generic_probe(), self.hermitian(), 1e-5
        system = self.system(psi)
        for mu in range(4):
            change = np.zeros_like(e["gauge"])
            change[mu] = direction
            p, m = self.system(psi, gauge=e["gauge"]+step*change), self.system(psi, gauge=e["gauge"]-step*change)
            self.assertClose((p["L"]-m["L"])/(2*step), np.trace(system["gauge_EL"][mu] @ direction).real, atol=2e-9)
        for name, field in [("hc", "hc_EL"), ("target", "target_EL")]:
            p, m = self.system(psi, **{name: e[name]+step*direction}), self.system(psi, **{name: e[name]-step*direction})
            self.assertClose((p["L"]-m["L"])/(2*step), np.trace(system[field] @ direction).real, atol=2e-9)

    def test_full_candidate_probe_variation_matches_both_complex_directions(self):
        psi, direction, step = self.generic_probe(), self.generic_probe(), 1e-5
        residual = self.system(psi)["probe_EL"]
        for delta in [direction, 1j*direction]:
            p, m = self.system(psi+step*delta), self.system(psi-step*delta)
            self.assertClose((p["L"]-m["L"])/(2*step), 2*np.vdot(delta, residual).real, atol=2e-9)

    def test_full_constant_noncommuting_ward_identity_holds_off_shell(self):
        for _ in range(10):
            result = self.system(self.generic_probe(), np.array([self.hermitian() for _ in range(4)]),
                                 self.hermitian(), self.hermitian())
            self.assertClose(result["ward_identity"], np.zeros((2, 2)), atol=8e-12)

    def test_omitting_the_external_target_reaction_breaks_the_ward_identity(self):
        result = self.system()
        self.assertGreater(np.linalg.norm(result["external_target_torque"]), 0.04)
        self.assertClose(result["ward_identity"]-result["external_target_torque"], -result["external_target_torque"])

    def test_commuting_target_and_compensator_remove_the_external_torque(self):
        result = self.system(target=np.diag([0.3, 0.8]))
        self.assertClose(result["external_target_torque"], np.zeros((2, 2)))

    def test_penalty_changes_only_hc_target_variations_at_fixed_independent_fields(self):
        before = self.system()
        after = self.system(target=self.e["target"]+0.2*self.hermitian())
        self.assertClose(before["gauge_EL"], after["gauge_EL"])
        self.assertClose(before["probe_EL"], after["probe_EL"])
        self.assertGreater(np.linalg.norm(before["hc_EL"]-after["hc_EL"]), 0.01)

    def test_constant_curvature_gauge_terms_are_traceless_not_arbitrary_central_currents(self):
        e = self.e
        field = action.curvature.constant_paired_field_equations(e["gauge"], e["hc"], e["n"], e["coupling"])
        self.assertClose(np.trace(field["gauge_EL"], axis1=-2, axis2=-1), np.zeros(4))
        self.assertLess(np.trace(self.system()["gauge_EL"][0]).real, -0.9)

    def completion_inputs(self):
        e = self.e
        damping = e["coupling"]*np.kron(e["hc"], np.einsum("m,mij->ij", e["n"], e["weights"]))
        hamiltonian = sum(np.kron(a, k) for a, k in zip(e["gauge"], e["weights"]))
        hamiltonian += np.kron(e["mass"]*np.eye(2)+e["yukawa"]*e["hc"], e["spin_metric"])
        psi = e["psi"].reshape(-1)
        return np.outer(psi, psi.conj()), hamiltonian, damping

    def test_positive_recycling_factor_matches_twice_the_damping(self):
        density, h, d = self.completion_inputs()
        result = action.recycling_completion(density, h, d)
        self.assertClose(result["jump"].conj().T @ result["jump"], 2*d)
        self.assertGreaterEqual(np.linalg.eigvalsh(result["recycling"])[0], -1e-12)

    def test_conditional_density_rate_equals_the_raw_probe_outer_product_rate(self):
        density, h, d = self.completion_inputs()
        psi, rate = self.e["psi"].reshape(-1), self.rates()["raw_equation_rate"].reshape(-1)
        result = action.recycling_completion(density, h, d)
        self.assertClose(result["conditional_rate"], np.outer(rate, psi.conj())+np.outer(psi, rate.conj()))

    def test_recycling_balances_trace_loss_without_proving_a_microscopic_bath(self):
        density, h, d = self.completion_inputs()
        result = action.recycling_completion(density, h, d)
        self.assertClose(np.trace(result["conditional_rate"]).real, -2*np.trace(d @ density).real)
        self.assertClose(np.trace(result["conditional_rate"]).real, -1.12)
        self.assertClose(np.trace(result["trace_preserving_rate"]), 0)

    def test_the_same_no_jump_damping_does_not_fix_the_recycling_channel(self):
        density, h, d = self.completion_inputs()
        result = action.recycling_completion(density, h, d)
        u = np.roll(np.eye(4), 1, axis=0)
        changed_jump = u @ result["jump"]
        self.assertClose(changed_jump.conj().T @ changed_jump, 2*d)
        changed_recycling = changed_jump @ density @ changed_jump.conj().T
        self.assertGreater(np.linalg.norm(changed_recycling-result["recycling"]), 0.5)
        self.assertClose(np.trace(changed_recycling-result["recycling"]), 0)

    def test_finite_recycling_step_is_positive_and_exactly_trace_preserving(self):
        density, h, d = self.completion_inputs()
        for step in [0, 0.01, 0.1]:
            result = action.recycling_step(density, h, d, step)
            self.assertClose(result["completeness"], np.eye(4))
            self.assertClose(np.trace(result["density"]), np.trace(density))
            self.assertGreaterEqual(np.linalg.eigvalsh(result["density"])[0], -1e-12)

    def test_finite_step_has_the_derived_trace_preserving_infinitesimal_generator(self):
        density, h, d = self.completion_inputs()
        generator = action.recycling_completion(density, h, d)["trace_preserving_rate"]
        errors = []
        for step in [1e-3, 5e-4]:
            result = action.recycling_step(density, h, d, step)["density"]
            errors.append(np.linalg.norm((result-density)/step-generator))
        self.assertLess(errors[1], 0.51*errors[0])

    def test_invalid_spin_weights_and_nonhermitian_adjoint_are_rejected(self):
        for weights in [np.zeros((3, 2, 2)), np.ones((4, 2, 3)), np.full((4, 2, 2), np.nan)]:
            with self.assertRaises(ValueError):
                action.probe_currents(self.e["psi"], weights, self.e["spin_metric"])
        with self.assertRaises(ValueError):
            action.probe_currents(self.e["psi"], self.e["weights"], [[0, 1], [0, 0]])

    def test_fixed_positive_metric_does_not_erase_a_nonzero_pure_damping_source(self):
        damping = np.diag([0.3, 0.7])
        self.assertClose(action.comparison_balance(-damping, np.eye(2)), -2*damping)

    def test_moving_metric_can_restore_norm_for_a_declared_time_only_evolution(self):
        damping, time = np.array([0.3, 0.7]), 0.6
        comparison = np.diag(np.exp(2*damping*time))
        rate = 2*np.diag(damping) @ comparison
        self.assertClose(action.comparison_balance(-np.diag(damping), comparison, rate), np.zeros((2, 2)))
        initial = np.array([1, 1j])/np.sqrt(2)
        evolved = np.exp(-damping*time)*initial
        self.assertClose(np.vdot(evolved, comparison @ evolved), np.vdot(initial, initial))

    def test_nonzero_hermitian_curvature_has_the_positive_metric_integrability_obstruction(self):
        f = np.diag([1.0, -2.0])
        raw = self.generic_probe()
        q = raw.conj().T @ raw+np.eye(2)
        defect = action.comparison_balance(f, q)
        for eigenvalue, vector in zip(np.diag(f), np.eye(2)):
            self.assertClose(np.vdot(vector, defect @ vector), 2*eigenvalue*np.vdot(vector, q @ vector))
        self.assertGreater(np.linalg.norm(defect), 1)

    def test_nonhermitian_curvature_can_be_skew_in_a_different_positive_comparison(self):
        transform = np.array([[1.0, 0.4j], [0.0, 2.0]])
        f = np.linalg.solve(transform, 1j*np.diag([1.0, 2.0]) @ transform)
        comparison = transform.conj().T @ transform
        self.assertGreater(np.linalg.norm(f+f.conj().T), 0.1)
        self.assertClose(action.comparison_balance(f, comparison), np.zeros((2, 2)))

    def test_constant_hc_connection_has_a_flat_positive_compatible_bundle_metric(self):
        e, coordinate = self.e, np.array([0.2, 0.0, 0.0, 0.3])
        values = np.diag(e["hc"])
        comparison = np.diag(np.exp(2*e["coupling"]*values*(e["n"] @ coordinate)))
        connection = e["coupling"]*e["n"][:, None, None]*e["hc"]
        derivatives = np.zeros((4, 4, 2, 2))
        self.assertClose(action.curvature.connection_curvature(connection, derivatives), derivatives)
        for mu in range(4):
            comparison_derivative = 2*e["coupling"]*e["n"][mu]*e["hc"] @ comparison
            self.assertClose(action.comparison_balance(connection[mu], comparison), comparison_derivative)

    def test_mismatched_field_derivative_and_probe_carriers_are_rejected(self):
        with self.assertRaises(ValueError):
            self.real_L(derivatives=np.zeros((3, 2, 2)))
        with self.assertRaises(ValueError):
            self.real_L(psi=np.zeros((3, 2)))
        with self.assertRaises(ValueError):
            self.system(target=np.eye(3))

    def test_nonpositive_temporal_comparison_is_not_used_for_probability_claims(self):
        e, weights = self.e, self.e["weights"].copy()
        weights[0] = e["spin_metric"]
        with self.assertRaises(ValueError):
            action.homogeneous_probe_rates(e["psi"], e["gauge"], e["hc"], weights, e["spin_metric"], e["n"], e["coupling"])

    def test_negative_penalty_and_nonpositive_damping_are_rejected(self):
        e = self.e
        with self.assertRaises(ValueError):
            action.constant_field_system(e["psi"], e["gauge"], e["hc"], e["target"], e["weights"], e["spin_metric"],
                                          e["n"], e["coupling"], -1)
        density, h, d = self.completion_inputs()
        with self.assertRaises(ValueError):
            action.recycling_completion(density, h, -np.eye(4))
        with self.assertRaises(ValueError):
            action.recycling_step(density, h, d, 1)

    def test_report_preserves_native_and_open_model_boundaries(self):
        report = action.evaluate()
        json.dumps(report, allow_nan=False)
        self.assertFalse(report["main_TeX_changed"])
        self.assertFalse(report["native_masses_phase_viscosity_or_microscopic_environment_derived"])
        self.assertLess(report["ward_identity"]["constant_noncommuting_example_identity_norm"], 1e-12)
        self.assertTrue(report["real_probe_action"]["raw_equation_and_real_action_not_generally_equivalent"])

    def test_saved_report_reproduces_the_calculation(self):
        saved = json.loads((ROOT / "analysis/HC_Real_Probe_Current_Closure.json").read_text(encoding="utf-8"))
        self.assertEqual(saved, action.evaluate())


if __name__ == "__main__":
    unittest.main()
