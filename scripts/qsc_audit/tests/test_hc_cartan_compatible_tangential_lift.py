"""Expanded higher-data construction with explicit changed-boundary scope."""
import importlib.util
import json
from pathlib import Path
import unittest

import numpy as np


ROOT = Path(__file__).resolve().parents[3]
SPEC = importlib.util.spec_from_file_location(
    "compatible_tangential_test", ROOT / "analysis/HC_Cartan_Compatible_Tangential_Lift.py")
model = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(model)


class FullSpinorPolynomialTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.basis = model.spinor_basis()
        cls.scalar = model.prior.joint.third.scalar
        cls.weights = np.array(cls.scalar.odd.readouts.dirac.WEIGHTS)

    def test_all_240_real_directions_are_symmetric(self):
        np.testing.assert_array_equal(self.basis, self.basis.swapaxes(1, 2))
        flat = self.basis.reshape(240, -1)
        self.assertEqual(np.linalg.matrix_rank(np.column_stack((flat.real, flat.imag))), 240)

    def test_full_quadratic_against_direct_pairing_loop(self):
        p = np.random.default_rng(1910240).normal(size=240)*.03
        tensor = model.prior.regular.unpack(np.r_[p, np.zeros(960)])["p2"]
        expected = []
        for r, s, t in model.prior.joint.third.TRIPLES:
            value = np.zeros((4, 4), complex)
            for i, j, k in ((r, s, t), (s, r, t), (t, r, s)):
                value += self.scalar.odd.readouts.pairing(tensor[j, k], tensor[i], self.scalar.Q)
            expected.append(value.imag)
        actual = model.spinor_quadratic(p, self.basis, self.scalar.Q, self.weights)
        np.testing.assert_allclose(actual, np.asarray(expected).reshape(320), atol=1e-12)

    def test_analytic_quadratic_derivative(self):
        rng = np.random.default_rng(1910241)
        p, direction = rng.normal(size=(2, 240))*.1
        derivative = model.spinor_quadratic_jacobian(p, self.basis, self.scalar.Q, self.weights)
        step = .125
        expected = (model.spinor_quadratic(p+step*direction, self.basis, self.scalar.Q, self.weights)
                    -model.spinor_quadratic(p-step*direction, self.basis, self.scalar.Q, self.weights))/(2*step)
        np.testing.assert_allclose(derivative @ direction, expected, atol=1e-11)

    def test_apply_increment_does_not_modify_inputs(self):
        c, h = np.arange(1200, dtype=float), np.arange(1720, dtype=float)
        before_c, before_h = c.copy(), h.copy()
        changed_c, changed_h = model.apply_increment(c, h, np.ones(240), np.ones(2680)*2)
        np.testing.assert_array_equal(c, before_c)
        np.testing.assert_array_equal(h, before_h)
        np.testing.assert_array_equal(changed_c[:240], c[:240]+1)
        np.testing.assert_array_equal(changed_c[240:], c[240:]+2)
        np.testing.assert_array_equal(changed_h, h+2)


class CompatibleTangentialLiftTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.report = json.loads((ROOT / "analysis/HC_Cartan_Compatible_Tangential_Lift.json").read_text(encoding="utf-8"))
        cls.prepared, point, _, _, cls.saved = model.prior.source.neighborhood.load_data()
        cls.original_point = point
        sources = model.prior.source.normal.build_reduction(cls.prepared, point)["sources"]
        cls.point = model.prior.source.normal.remaining.normal_point(
            point, sources @ np.array(cls.report["source_values"]))
        cls.c = np.array(cls.report["fitted_coordinates"])
        cls.h = np.array(cls.report["fitted_highest"])
        cls.lc = model.prior.joint.third.lc_cubic(cls.prepared, cls.point)
        cls.actual = model.prior.evaluate_fields(cls.prepared, cls.point, cls.c, cls.h, cls.lc)

    def test_fingerprints(self):
        self.assertEqual(self.report["input_sha256"], model.input_fingerprints())

    def test_fixed_source_values_and_lower_equations(self):
        before = json.loads((ROOT / "analysis/HC_Cartan_Cauchy_Next_Completion.json").read_text(encoding="utf-8"))
        self.assertEqual(self.report["source_values"], before["source_values"])
        self.assertFalse(self.report["lower_point_changed_during_fit"])
        value = np.linalg.norm(model.prior.source.normal.normal_equations(self.prepared, self.point))
        self.assertLess(value, 1e-8)
        self.assertAlmostEqual(value, self.report["all_68_lower_norm"], places=12)

    def test_actual_all_1114_and_full_symmetric_blocks(self):
        for key, value in model.prior.norm_report(self.actual).items():
            self.assertAlmostEqual(value, self.report["final"][key], places=7)
        self.assertEqual(self.report["numerically_completed"], bool(
            np.linalg.norm(self.actual["vector"]) < 1e-7 and self.report["all_68_lower_norm"] < 1e-7))

    def test_actual_spatial_and_earlier_rows(self):
        rows = [794+16*t+4*a+mu for t, triple in enumerate(model.prior.joint.third.TRIPLES)
                if 0 not in triple for a in range(4) for mu in (1, 2, 3)]
        self.assertAlmostEqual(np.linalg.norm(self.actual["vector"][rows]), self.report["spatial_C3_norm"], places=8)
        self.assertAlmostEqual(np.linalg.norm(self.actual["old"][:384]), self.report["all_384_norm"], places=8)

    def test_expanded_problem_is_not_old_prescribed_germ(self):
        self.assertEqual(self.report["matrix_shape"], [1114, 2680])
        self.assertEqual(self.report["free_psi2_count"], 240)
        self.assertTrue(self.report["tangential_data_changed"])
        self.assertTrue(self.report["not_preservation_of_previous_prescribed_germ"])
        self.assertTrue(self.report["not_regional_existence_native_action_or_scale_identification"])
        self.assertLess(self.report["polynomial_control_error"], 1e-7)

    def test_selected_worker_columns_replay(self):
        c = np.array(self.saved["jet_coordinates"])
        h = np.concatenate((self.saved["connection_coordinates"], np.array(self.saved["fourth_spinor_real"]).reshape(-1)))
        base = model.prior.evaluate_fields(self.prepared, self.point, c, h, self.lc)["vector"]
        model._initialize_worker(self.prepared, self.point, c, h, self.lc, base)
        for task in (("older", 345), ("psi2", 117)):
            kind, index, actual = model._column(task)
            self.assertEqual((kind, index), task)
            delta = c.copy()
            step = 64. if kind == "older" else .25
            delta[index] += step
            plus = model.prior.evaluate_fields(self.prepared, self.point, delta, h, self.lc)["vector"]
            if kind == "older":
                expected = (plus-base)/step
            else:
                delta[index] -= 2*step
                minus = model.prior.evaluate_fields(self.prepared, self.point, delta, h, self.lc)["vector"]
                expected = (plus-minus)/(2*step)
            np.testing.assert_allclose(actual, expected, atol=1e-12)

    def test_earlier_source_law_recovers_the_same_q_from_new_data(self):
        services = model.prior.create_container().services()
        _, masked, _ = model.quadratic.load_problem(services)
        high = model.prior.highest_matrix(self.prepared, services=services)
        c0 = np.array(self.saved["jet_coordinates"])
        h0 = np.concatenate((self.saved["connection_coordinates"], np.array(self.saved["fourth_spinor_real"]).reshape(-1)))
        response = model.higher_response(self.prepared, self.point, c0, h0, self.lc,
                                         masked, high, services=services, workers=1)
        matrix = np.column_stack((response["jacobian"][:384], response["matrix"][:384, :960]))
        reduction = model.prior.source.normal.build_reduction(self.prepared, self.original_point)
        jets = model.prior.regular.unpack(c0)
        source, _ = model.prior.source.normal.higher_source_response(
            self.prepared, self.original_point, jets, reduction)
        base = model.prior.regular.equations(self.prepared, self.original_point, jets)["vector"]
        system = {"matrix": matrix, "base": base, "source": source}
        allowed = sum(model.prior.source.allowed_cauchy_coordinates().values(), [])
        fixed = np.setdiff1d(np.arange(1200), allowed)
        free = model.prior.source.elimination(matrix[:, allowed], source, base)
        self.assertEqual(free["gate_rank"], 6)
        recovered = model.prior.source.prescribed_source_law(system, free, allowed, (self.c-c0)[fixed])
        np.testing.assert_allclose(recovered["source"], self.report["source_values"], atol=1e-8)
        self.assertLess(recovered["compatibility_norm"], 1e-7)


if __name__ == "__main__":
    unittest.main()
