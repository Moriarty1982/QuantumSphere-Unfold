"""Whole-ball residual formulas, independent point matching and failure controls."""
import importlib.util
import json
from pathlib import Path
import unittest

import numpy as np


ROOT = Path(__file__).resolve().parents[3]
SPEC = importlib.util.spec_from_file_location(
    "uniform_residual_bound_test", ROOT / "analysis/HC_Cartan_Uniform_Residual_Bound.py")
model = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(model)


class BallJetTests(unittest.TestCase):
    def test_complex_product_rule_matches_independent_directional_difference(self):
        rng = np.random.default_rng(801114)
        a = rng.normal(size=(2, 3))+1j*rng.normal(size=(2, 3))
        b = rng.normal(size=(3, 4))+1j*rng.normal(size=(3, 4))
        da, db = rng.normal(size=(4, 2, 3)), rng.normal(size=(4, 3, 4))
        ja = model.FirstJet(model.B(a), [model.B(d) for d in da])
        jb = model.FirstJet(model.B(b), [model.B(d) for d in db])
        result = model.jc("ij,jk->ik", ja.conjugate(), jb).real().transpose(1, 0)
        np.testing.assert_allclose(result.value.center, (a.conj() @ b).real.T)
        for r in range(4):
            h = 1e-4
            expected = (((a+h*da[r]).conj() @ (b+h*db[r]))
                        -((a-h*da[r]).conj() @ (b-h*db[r]))).real.T/(2*h)
            np.testing.assert_allclose(result.derivatives[r].center, expected, atol=2e-11)
            self.assertEqual(result.derivatives[r].radius, 0.)

    def test_product_rule_ball_contains_perturbed_first_jet(self):
        a = model.FirstJet(model.B(np.array([1., 2.]), .1),
                           [model.B(np.array([.3, -.2]), .02) for _ in range(4)])
        output = model.jc("i,i->", a, a)
        value = np.array([1.03, 1.98])
        derivative = np.array([.31, -.205])
        self.assertLess(abs(value @ value-output.value.center), output.value.radius)
        self.assertLess(abs(2*value @ derivative-output.derivatives[0].center), output.derivatives[0].radius)

    def test_bad_first_jet_derivative_shape_rejected(self):
        with self.assertRaises(ValueError):
            model.FirstJet(model.B(np.ones(2)), [model.B(np.ones(3)) for _ in range(4)])

    def test_stacked_radii_use_full_tensor_multiplicity(self):
        output = model.stack([model.B(np.ones(2), 3.), model.B(np.ones(2), 4.)])
        self.assertEqual(output.center.shape, (2, 2))
        self.assertEqual(output.radius, 5.)

    def test_natural_ball_arithmetic_does_not_preserve_dependency_cancellation(self):
        value = model.B(np.array([2., -1.]), .1)
        difference = value-value
        np.testing.assert_array_equal(difference.center, [0, 0])
        self.assertEqual(difference.radius, .2)


class UniformResidualReportTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.case = model.previous.load_case()
        cls.report = json.loads((ROOT / "analysis/HC_Cartan_Uniform_Residual_Bound.json").read_text(encoding="utf-8"))

    def test_fingerprints_and_all_80_row_contract(self):
        self.assertEqual(self.report["input_sha256"], model.input_fingerprints())
        fields, _ = model.previous.fields_and_higher(self.case, np.zeros(4))
        ball, blocks = model.residual_ball(self.case[0], model.point_balls(self.case[0], fields))
        self.assertEqual(ball.center.shape, (80,))
        self.assertEqual([v.center.size for v in blocks.values()], [16, 24, 16, 24])

    def test_saved_zero_radius_points_match_actual_parent_equations(self):
        for point in self.report["point_controls"]:
            self.assertEqual(point["zero_radius"], 0.)
            self.assertLess(point["match_error"], 2e-12)
        fields, _ = model.previous.fields_and_higher(self.case, model.common.RADIUS*np.array([.1, -.2, .3, .4]))
        actual = model.common.lower.lower_residual(self.case[0], fields)
        bound, _ = model.residual_ball(self.case[0], model.point_balls(self.case[0], fields))
        np.testing.assert_allclose(bound.center, actual, atol=2e-12, rtol=0)

    def test_off_shell_zero_radius_control_checks_more_than_fitted_field(self):
        fields, _ = model.previous.fields_and_higher(self.case, np.zeros(4))
        rng = np.random.default_rng(801115)
        for key in fields:
            perturbation = rng.normal(size=fields[key].shape)*1e-4
            if np.iscomplexobj(fields[key]):
                perturbation = perturbation+1j*rng.normal(size=fields[key].shape)*1e-4
            if key == "coframe_second":
                perturbation = (perturbation+perturbation.swapaxes(0, 1))/2
            fields[key] = fields[key]+perturbation
        actual = model.common.lower.lower_residual(self.case[0], fields)
        bound, _ = model.residual_ball(self.case[0], model.point_balls(self.case[0], fields))
        self.assertGreater(np.linalg.norm(actual), 1e-3)
        np.testing.assert_allclose(bound.center, actual, atol=3e-12, rtol=0)

    def test_extended_field_balls_enclose_dde_dp_and_dl(self):
        rng = np.random.default_rng(801116)
        for radius in (model.common.RADIUS, self.report["bounds"][2]["radius"]):
            balls = model.field_balls(self.case, radius)
            for _ in range(3):
                direction = rng.normal(size=4)
                direction /= np.linalg.norm(direction)
                fields, _ = model.previous.fields_and_higher(self.case, radius*direction)
                for key, name in (("dde", "coframe_second"), ("dp", "psi_first"), ("dl", "multiplier_first")):
                    self.assertLess(np.linalg.norm(fields[name]-balls[key].center), balls[key].radius*(1+1e-9)+1e-13)

    def test_full_bound_encloses_saved_samples_but_is_not_sharp(self):
        for bound in self.report["bounds"]:
            self.assertGreater(bound["full_residual_upper_estimate"], 1.)
            self.assertLess(bound["origin_center_match_error"], 2e-12)
            self.assertGreater(bound["blocks"]["curls"]["variation_majorant"], bound["blocks"]["coframe"]["variation_majorant"])
            for point in bound["sample_checks_not_the_proof"]:
                self.assertLess(point["distance_from_ball_center"], bound["variation_majorant"])
                self.assertGreater(bound["full_residual_upper_estimate"], 1e10*point["residual_norm"])

    def test_small_radius_bound_scales_linearly_not_quintically(self):
        a, b = self.report["bounds"][2:]
        self.assertAlmostEqual(a["variation_majorant"]/b["variation_majorant"], 2., delta=1e-5)
        self.assertGreater(a["center_norm"], 0.)

    def test_scope_does_not_turn_a_bound_into_an_existence_claim(self):
        for key in ("no_new_coefficients_fitted", "retains_nonzero_origin_residual",
                    "not_a_fifth_order_Taylor_remainder_bound", "not_outward_rounded_or_interval_certified",
                    "not_distance_to_exact_solution_or_convergence_proof"):
            self.assertTrue(self.report[key])
        self.assertFalse(self.report["main_TeX_PDF_changed"])


if __name__ == "__main__":
    unittest.main()
