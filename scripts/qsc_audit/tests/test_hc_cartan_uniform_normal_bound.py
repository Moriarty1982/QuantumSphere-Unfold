"""Tensor-ball majorants and direct general normal coefficients."""
import importlib.util
import json
from pathlib import Path
import unittest

import numpy as np


ROOT = Path(__file__).resolve().parents[3]
SPEC = importlib.util.spec_from_file_location(
    "uniform_normal_bound_test", ROOT / "analysis/HC_Cartan_Uniform_Normal_Bound.py")
model = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(model)


class TensorBallTests(unittest.TestCase):
    def test_multilinear_complex_contraction_encloses_perturbations(self):
        rng = np.random.default_rng(191084)
        centers = [rng.normal(size=shape)+1j*rng.normal(size=shape)
                   for shape in ((3, 4), (4, 5), (5, 2))]
        radii = (.02, .03, .01)
        result = model.contract("ij,jk,kl->il", *(model.TensorBall(c, r) for c, r in zip(centers, radii)))
        for _ in range(20):
            changed = []
            for center, radius in zip(centers, radii):
                delta = rng.normal(size=center.shape)+1j*rng.normal(size=center.shape)
                delta *= radius/np.linalg.norm(delta)
                changed.append(center+delta)
            actual = np.einsum("ij,jk,kl->il", *changed)
            self.assertLessEqual(np.linalg.norm(actual-result.center), result.radius+1e-12)

    def test_single_operand_sum_has_dimension_factor(self):
        result = model.contract("i->", model.TensorBall(np.zeros(9), .2))
        self.assertAlmostEqual(result.radius, .6)
        self.assertGreaterEqual(result.radius, np.sum(np.ones(9)*(.2/3)))

    def test_unhandled_traces_and_noncontractive_slices_rejected(self):
        with self.assertRaises(ValueError):
            model.contract("ii->", model.TensorBall(np.eye(4), .1))
        with self.assertRaises(ValueError):
            model.TensorBall(np.ones(3), .1)[[0, 0, 0]]
        with self.assertRaises(ValueError):
            model.TensorBall(np.ones(3), -.1)
        with self.assertRaises(ValueError):
            model.TensorBall(np.ones(3))+np.ones((1, 3))

    def test_block_stacking_uses_sum_of_squared_error_bounds(self):
        result = model.stack_blocks([model.TensorBall(np.zeros((2, 3)), .3),
                                    model.TensorBall(np.zeros((2, 4)), .4)])
        self.assertEqual(result.center.shape, (2, 7))
        self.assertAlmostEqual(result.radius, .5)


class UniformNormalBoundTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.report = json.loads((ROOT / "analysis/HC_Cartan_Uniform_Normal_Bound.json").read_text(encoding="utf-8"))
        cls.prepared, cls.point, cls.jets, _, cls.full, _ = model.general.domain.load_data()
        cls.norms = model.coefficient_norms(cls.prepared, cls.point, cls.jets, cls.full)

    def test_fingerprints_and_actual_norms(self):
        self.assertEqual(self.report["input_sha256"], model.input_fingerprints())
        self.assertEqual(self.report["coefficient_norms"], self.norms)

    def test_direct_formula_matches_general_matrix_at_nonorigin_point(self):
        x = np.eye(4)[1]/16384
        fields = model.general.domain.temporal.fields(self.prepared, self.point, self.jets, self.full, x)
        e = fields["coframe"]
        spatial = fields["psi_first"].copy()
        spatial[0] = 0
        hessian = model.general.prolong.fast_cartan_data(self.prepared, e, fields["psi"])[0]
        kwargs = {"e": e, "inverse": np.linalg.inv(e), "volume": np.asarray(abs(np.linalg.det(e))),
                  "de": fields["coframe_first"], "psi": fields["psi"], "spatial_dp": spatial,
                  "lam": fields["multiplier"], "hessian_inverse": np.linalg.inv(hessian)}
        direct, _ = model.coefficient_matrix(self.prepared, **{k: model.ball(v) for k, v in kwargs.items()})
        system = model.general.normal_system(self.prepared, fields,
            services=model.prior.create_container().services())
        np.testing.assert_allclose(direct.center, system["matrix"], atol=1e-10)
        self.assertEqual(direct.radius, 0.)

    def test_selected_majorant_replays_and_retains_positive_margins(self):
        estimate, blocks = model.coefficient_matrix(self.prepared,
            **model.field_balls(self.prepared, self.point, self.norms, self.report["radius"]))
        self.assertAlmostEqual(estimate.radius, self.report["matrix_change_majorant"], places=12)
        self.assertEqual(blocks, self.report["block_majorants"])
        self.assertGreater(self.report["augmented_singular_lower_bound"], 0.)
        self.assertGreater(self.report["normal_singular_40_lower_bound"], 0.)
        self.assertLess(self.report["augmented_inverse_norm_upper_bound"], 20.)

    def test_enclosures_apply_to_whole_taylor_field_inputs(self):
        for radius in (self.report["radius"], 1/16384):
            balls = model.field_balls(self.prepared, self.point, self.norms, radius)
            for direction in (np.eye(4)[2], np.array([.5, -.5, .5, -.5])):
                fields = model.general.domain.temporal.fields(self.prepared, self.point, self.jets, self.full, radius*direction)
                spatial = fields["psi_first"].copy()
                spatial[0] = 0
                actual = {"e": fields["coframe"], "de": fields["coframe_first"], "psi": fields["psi"],
                          "spatial_dp": spatial, "lam": fields["multiplier"],
                          "inverse": np.linalg.inv(fields["coframe"]),
                          "volume": np.asarray(abs(np.linalg.det(fields["coframe"]))),
                          "hessian_inverse": np.linalg.inv(fields["Cartan_hessian"])}
                for key, value in actual.items():
                    self.assertLessEqual(np.linalg.norm(value-balls[key].center), balls[key].radius+1e-13)

    def test_direct_sample_changes_obey_uniform_majorant(self):
        for sample in self.report["sample_checks_not_the_proof"]:
            self.assertLessEqual(sample["actual_matrix_change"], self.report["matrix_change_majorant"])
            self.assertGreaterEqual(sample["augmented_minimum_singular"], self.report["augmented_singular_lower_bound"])
            self.assertEqual(sample["rank"], 40)

    def test_monotonic_majorants_and_zero_radius(self):
        values = []
        for factor in (0., .25, .5, 1.):
            estimate, _ = model.coefficient_matrix(self.prepared,
                **model.field_balls(self.prepared, self.point, self.norms, factor*self.report["radius"]))
            values.append(estimate.radius)
        self.assertEqual(values[0], 0.)
        self.assertEqual(values, sorted(values))
        with self.assertRaises(ValueError):
            model.field_balls(self.prepared, self.point, self.norms, -1.)

    def test_scope_guards(self):
        for key in ("not_outward_rounded_or_interval_certified", "not_uniform_exact_rank_40_upper_bound",
                    "not_gauge_source_transport_or_compatibility_propagation", "not_regional_PDE_solution_or_physical_length"):
            self.assertTrue(self.report[key])
        self.assertFalse(self.report["main_TeX_PDF_changed"])
        self.assertLess(self.report["center_matrix_match_error"], 1e-10)


if __name__ == "__main__":
    unittest.main()
