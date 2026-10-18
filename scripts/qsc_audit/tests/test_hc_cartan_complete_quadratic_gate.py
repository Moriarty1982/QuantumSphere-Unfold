"""Complete Hessian coefficients checked against the direct pairings and residual."""
import importlib.util
import json
from pathlib import Path
import unittest

import numpy as np


ROOT = Path(__file__).resolve().parents[3]
SPEC = importlib.util.spec_from_file_location(
    "complete_quadratic_gate_test", ROOT / "analysis/HC_Cartan_Complete_Quadratic_Gate.py")
model = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(model)


class CompleteQuadraticGateTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.report = json.loads((ROOT / "analysis/HC_Cartan_Complete_Quadratic_Gate.json").read_text(encoding="utf-8"))
        cls.services = model.prior.create_container().services()
        cls.prepared, cls.assembled, residual = model.load_problem(cls.services)
        cls.residual = staticmethod(residual)
        cls.basis = model.normal_basis()
        scalar = model.prior.joint.third.scalar
        cls.coefficients = model.quadratic_coefficients(cls.basis, scalar.Q,
            np.asarray(scalar.odd.readouts.dirac.WEIGHTS), model.prior.joint.third.TRIPLES)

    def test_fingerprints(self):
        self.assertEqual(self.report["input_sha256"], model.input_fingerprints())

    def test_complete_coefficient_count(self):
        self.assertEqual(self.coefficients.shape, (320, 96*97//2))
        self.assertEqual(self.report["quadratic_coefficient_shape"], [320, 4656])
        self.assertGreater(np.linalg.norm(self.coefficients), 1.)

    def test_normal_basis_is_symmetric_and_has_no_spatial_trace(self):
        np.testing.assert_array_equal(self.basis, self.basis.swapaxes(1, 2))
        np.testing.assert_array_equal(self.basis[:, 1:, 1:], np.zeros_like(self.basis[:, 1:, 1:]))
        flat = self.basis.reshape(96, -1)
        self.assertEqual(np.linalg.matrix_rank(np.column_stack((flat.real, flat.imag))), 96)

    def test_coefficients_against_independent_pairing_loop(self):
        scalar = model.prior.joint.third.scalar
        p = np.random.default_rng(194656).normal(size=96)*.1
        tensor = np.einsum("p,prsuq->rsuq", p, self.basis)
        expected = []
        for r, s, t in model.prior.joint.third.TRIPLES:
            value = np.zeros((4, 4), dtype=complex)
            for i, j, k in ((r, s, t), (s, r, t), (t, r, s)):
                value += scalar.odd.readouts.pairing(tensor[j, k], tensor[i], scalar.Q)
            expected.append(value.imag)
        np.testing.assert_allclose(self.coefficients @ model.monomials(p),
                                   np.array(expected).reshape(-1), atol=1e-12)

    def test_coefficients_against_actual_second_difference(self):
        p = np.random.default_rng(194657).normal(size=96)*.3
        second = (self.residual(p)+self.residual(-p)-2*self.residual(np.zeros(96)))/2
        np.testing.assert_allclose(second[:794], np.zeros(794), atol=1e-8)
        np.testing.assert_allclose(second[794:], self.coefficients @ model.monomials(p), atol=1e-8)

    def test_all_projected_coefficients_small(self):
        left, singular, _ = self.services.svd(self.assembled.matrix, full_matrices=False)
        rank = int(np.sum(singular > max(1e-9, singular[0]*1e-10)))
        projected = left[794:, rank:].T @ self.coefficients
        self.assertLess(np.linalg.norm(projected), 1e-7)
        self.assertAlmostEqual(np.linalg.norm(projected), self.report["projected_coefficient_norm"], places=9)

    def test_witness_replayed_on_actual_equations(self):
        y = np.array(self.report["witness"])
        self.assertAlmostEqual(np.linalg.norm(y), 1., places=12)
        self.assertLess(np.linalg.norm(y @ self.assembled.matrix), 1e-7)
        self.assertLess(np.linalg.norm(y[794:] @ self.coefficients), 1e-7)
        base_value = y @ self.residual(np.zeros(96))
        self.assertGreater(base_value, 30.)
        p = np.random.default_rng(194658).normal(size=96)*.2
        w = np.random.default_rng(194659).normal(size=1168)*.02
        self.assertAlmostEqual(y @ self.residual(p, w), base_value, places=7)

    def test_no_exact_proof_claim_from_float_controls(self):
        self.assertTrue(self.report["floating_point_evidence_not_exact_or_interval_certificate"])
        self.assertTrue(self.report["not_regional_existence_or_general_nonexistence"])
        for control in self.report["controls"]:
            self.assertLess(control["full_polynomial_error"], 1e-7)


if __name__ == "__main__":
    unittest.main()
