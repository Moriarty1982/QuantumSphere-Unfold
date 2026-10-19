"""Joint probe identity, variable weight factorization and retained uncertainty."""
import importlib.util
import json
from pathlib import Path
import unittest

import numpy as np


ROOT = Path(__file__).resolve().parents[3]
SPEC = importlib.util.spec_from_file_location("joint_probe_test", ROOT / "analysis/HC_Cartan_Joint_Probe_Response_Bound.py")
model = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(model)


def direct_action(psi, omega, volume, inverse, multiplier):
    spin = -.25*np.einsum("mab,aij,bjk->mik", omega, model.general.cartan.GAMMA, model.general.cartan.GAMMA)
    spin_full = np.array([np.kron(np.eye(3), s) for s in spin])
    weights = (volume*np.einsum("ma,aij->mij", inverse, model.general.prolong.FLAT_WEIGHTS)
        +np.einsum("am,aij->mij", multiplier, model.general.prolong.Q_WEIGHTS))
    response = np.einsum("mij,mjk->ik", weights, spin_full)-np.einsum("mji,mjk->ik", spin_full.conj(), weights)
    return response @ psi.ravel()


class JointProbeTests(unittest.TestCase):
    def test_off_shell_regrouping_identity_for_arbitrary_complex_matrices(self):
        rng = np.random.default_rng(191501)
        w = rng.normal(size=(4, 12, 12))+1j*rng.normal(size=(4, 12, 12))
        s = rng.normal(size=(4, 12, 12))+1j*rng.normal(size=(4, 12, 12))
        psi = rng.normal(size=12)+1j*rng.normal(size=12)
        ws = np.einsum("mij,mjk->ik", w, s)
        sw = np.einsum("mji,mjk->ik", s.conj(), w)
        left = 1j*ws @ psi+.5j*(-sw-ws) @ psi
        np.testing.assert_allclose(left, .5j*(ws-sw) @ psi, atol=3e-13, rtol=1e-14)

    def test_variable_factorization_matches_direct_expression(self):
        model.check_weight_structure()
        rng = np.random.default_rng(191502)
        arrays = [rng.normal(size=(3, 4))+1j*rng.normal(size=(3, 4)), rng.normal(size=(4, 4, 4)),
            np.asarray(1.1), np.eye(4), rng.normal(size=(4, 4))*.1]
        values = [model.core.tensor(v) for v in arrays]
        for value in values:
            value.coefficients[model.core.INDEX[(1, 0, 0, 0)]] = rng.normal(size=value.center.shape)*.03
        result = model.response_action(*values)
        for y in (np.ones(4), np.array([-.3, .1, .2, .4])):
            expected = direct_action(*(v.evaluate(y) for v in values))
            np.testing.assert_allclose(result.evaluate(y), expected, atol=2e-13, rtol=1e-13)
        self.assertEqual(result.tail, 0.)

    def test_uncertain_variable_weights_and_connection_enclosed(self):
        rng = np.random.default_rng(191503)
        arrays = [rng.normal(size=(3, 4))+1j*rng.normal(size=(3, 4)), rng.normal(size=(4, 4, 4)),
            np.asarray(1.2), np.eye(4), rng.normal(size=(4, 4))*.1]
        values = [model.T(model.core.tensor(v).coefficients, .001) for v in arrays]
        result = model.response_action(*values)
        for _ in range(5):
            actual = []
            for index, v in enumerate(values):
                error = rng.normal(size=v.center.shape)
                if index == 0:
                    error = error+1j*rng.normal(size=v.center.shape)
                actual.append(v.center+error*v.tail/np.linalg.norm(error))
            self.assertLess(np.linalg.norm(direct_action(*actual)-result.center), result.tail)
        self.assertGreater(result.tail, 0.)

    def test_zero_multiplier_center_does_not_drop_variable_channel_action(self):
        rng = np.random.default_rng(191504)
        psi = model.core.tensor(rng.normal(size=(3, 4))+1j*rng.normal(size=(3, 4)))
        omega = model.core.tensor(rng.normal(size=(4, 4, 4)))
        multiplier = model.core.tensor(np.zeros((4, 4)))
        multiplier.coefficients[model.core.INDEX[(1, 0, 0, 0)]] = rng.normal(size=(4, 4))
        result = model.response_action(psi, omega, model.core.tensor(np.asarray(0.)), model.core.tensor(np.eye(4)), multiplier)
        self.assertEqual(np.linalg.norm(result.center), 0.)
        self.assertGreater(np.linalg.norm(result.evaluate(np.ones(4))), .1)

    def test_complex_geometric_input_rejected(self):
        arrays = [np.ones((3, 4), complex), np.zeros((4, 4, 4)), np.asarray(1.), np.eye(4), np.eye(4)]
        for index in range(1, 5):
            values = [model.core.tensor(v) for v in arrays]
            values[index] = model.core.tensor(arrays[index]+.01j)
            with self.assertRaises(ValueError):
                model.response_action(*values)

    def test_original_probe_off_shell_with_nonzero_weight_derivatives(self):
        case = model.control.load_case()
        fields, _ = model.control.fields_and_higher(case, model.common.RADIUS*np.array([.2, -.3, .1, .4]))
        fields["psi"] = fields["psi"]+(.01+.003j)
        fields["multiplier"] = fields["multiplier"]+.02*np.eye(4)
        fields["multiplier_first"] = fields["multiplier_first"]+np.random.default_rng(191505).normal(size=(4, 4, 4))*.01
        inputs = model.full.point_models(fields)
        omega, volume, inverse, _, _ = model.prior.prior.connection_models(case[0], inputs)
        result, pieces = model.probe_model(inputs, omega, volume, inverse)
        expected = model.common.lower.lower_residual(case[0], fields)[16:40]
        self.assertGreater(np.linalg.norm(expected), 1e-3)
        np.testing.assert_allclose(result.center, expected, atol=2e-12, rtol=0)
        self.assertEqual(result.tail, 0.)
        self.assertLess(pieces["factorized_vs_generic_coefficients_error"], 1e-12)


class JointProbeReportTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.report = json.loads((ROOT / "analysis/HC_Cartan_Joint_Probe_Response_Bound.json").read_text(encoding="utf-8"))
        cls.parent = model.load_parent()

    def test_fingerprints_and_scope(self):
        self.assertEqual(self.report["input_sha256"], model.input_fingerprints())
        for flag in ("identity_is_off_shell", "variable_volume_inverse_and_multiplier_retained", "weight_derivatives_not_dropped",
                     "other_56_equations_and_enclosures_unchanged", "no_coefficients_fitted_or_low_order_defects_zeroed",
                     "only_previously_certified_fixed_response_constant_used", "not_a_full_outward_rounded_certificate",
                     "not_exact_closure_regional_solution_or_native_identification"):
            self.assertTrue(self.report[flag])
        self.assertFalse(self.report["main_TeX_PDF_changed"])

    def test_other_56_components_and_low_order_defects_retained(self):
        indices = list(range(16))+list(range(40, 80))
        for report, parent in zip(self.report["reports"], self.parent["reports"]):
            np.testing.assert_array_equal(np.asarray(report["coefficients"])[:, indices], np.asarray(parent["coefficients"])[:, indices])
            for key in ("constraint", "coframe", "curl"):
                self.assertEqual(report[key], parent[key])
            self.assertLess(report["coefficient_identity_error"], 1e-12)
            self.assertLess(report["tail_diagnostics"]["factorized_vs_generic_coefficients_error"], 1e-12)
            for level in (3, 4):
                self.assertGreater(report["combined"]["coefficient_level_bounds"][level], 1e-12)

    def test_both_control_steps_improve_without_dropping_terms(self):
        for report in self.report["reports"]:
            pieces = report["tail_diagnostics"]
            self.assertLess(pieces["generic_regrouped_probe_tail"], report["previous_probe_tail"])
            self.assertLess(report["probe"]["tail_bound"], pieces["generic_regrouped_probe_tail"])
            self.assertAlmostEqual(report["probe"]["tail_bound"], sum(pieces[k] for k in
                ("transport_tail", "mass_tail", "weight_derivative_tail", "joint_connection_action_tail")))
            self.assertGreater(pieces["weight_derivative_tail"], 0.)
            self.assertLess(report["combined"]["whole_cube_upper_estimate"], report["previous_combined_upper_estimate"])
            for check in report["sample_checks_not_the_proof"]:
                self.assertLess(check["probe_tail_discrepancy"], report["probe"]["tail_bound"])
                self.assertLess(check["combined_tail_discrepancy"], report["combined"]["tail_bound"])
                self.assertGreater(report["combined"]["tail_bound"], 1e3*check["actual_norm"])


if __name__ == "__main__":
    unittest.main()
