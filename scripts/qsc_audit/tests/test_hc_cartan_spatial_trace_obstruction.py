"""Spatial C3 dependence and exact rational obstruction for the frozen witness."""
import importlib.util
import json
from pathlib import Path
import unittest

import numpy as np
import sympy as sp


ROOT = Path(__file__).resolve().parents[3]
SPEC = importlib.util.spec_from_file_location(
    "spatial_trace_test", ROOT / "analysis/HC_Cartan_Spatial_Trace_Obstruction.py")
model = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(model)


class SpatialTraceObstructionTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.report = json.loads((ROOT / "analysis/HC_Cartan_Spatial_Trace_Obstruction.json").read_text(encoding="utf-8"))
        cls.before = json.loads((ROOT / "analysis/HC_Cartan_Cauchy_Next_Completion.json").read_text(encoding="utf-8"))
        cls.services = model.prior.create_container().services()
        cls.prepared, cls.assembled, residual = model.quadratic.load_problem(cls.services)
        cls.residual = staticmethod(residual)
        _, point, _, _, _ = model.prior.source.neighborhood.load_data()
        reduction = model.prior.source.normal.build_reduction(cls.prepared, point)
        cls.point = model.prior.source.normal.remaining.normal_point(
            point, reduction["sources"] @ np.array(cls.before["source_values"]))
        cls.coordinates = np.array(cls.before["starting_coordinates"])
        cls.highest = np.array(cls.before["starting_highest"])

    def test_fingerprints(self):
        self.assertEqual(self.report["input_sha256"], model.input_fingerprints())

    def test_all_120_rows_are_purely_spatial(self):
        rows = model.spatial_rows()
        self.assertEqual(rows, self.report["spatial_rows"])
        self.assertEqual(len(rows), 120)
        self.assertEqual(len(set(rows)), 120)
        for row in rows:
            triple, rest = divmod(row-794, 16)
            _, mu = divmod(rest, 4)
            self.assertNotIn(0, model.prior.joint.third.TRIPLES[triple])
            self.assertNotEqual(mu, 0)

    def test_all_allowed_linear_columns_are_exactly_zero_in_spatial_rows(self):
        np.testing.assert_array_equal(self.assembled.matrix[model.spatial_rows()], np.zeros((120, 1168)))

    def test_actual_normal_changes_leave_all_spatial_rows_unchanged(self):
        rng = np.random.default_rng(1910121)
        before = self.residual(np.zeros(96))[model.spatial_rows()]
        after = self.residual(rng.normal(size=96), rng.normal(size=1168))[model.spatial_rows()]
        np.testing.assert_array_equal(before, after)
        self.assertGreater(np.linalg.norm(before), 31.)

    def test_source_alone_is_not_the_spatial_defect(self):
        self.assertEqual(self.report["source_only_spatial_change"], 0.)
        self.assertLess(self.report["source_only_spatial_norm"], 1e-8)
        self.assertGreater(self.report["fixed_spatial_C3_norm"], 31.)

    def test_saved_rational_certificates_exceed_15(self):
        for numerator_key, denominator_key in (("chosen_exact_numerator", "chosen_exact_denominator"),
                ("rebuilt_spin_maps_numerator", "rebuilt_spin_maps_denominator")):
            numerator = int(self.report[numerator_key])
            denominator = int(self.report[denominator_key])
            self.assertGreater(denominator, 0)
            self.assertGreater(numerator, 15*denominator)

    def test_replay_rebuilt_exact_spin_maps(self):
        value = model.exact_repeated_spatial_component(
            self.prepared, self.point, self.coordinates, self.highest, rebuild_spin_maps=True)
        expected = sp.Rational(self.report["rebuilt_spin_maps_numerator"],
                               self.report["rebuilt_spin_maps_denominator"])
        self.assertEqual(value, expected)
        self.assertLess(abs(float(value)-self.report["chosen_float_value"]), 1e-8)

    def test_exact_frozen_value_is_invariant_under_all_allowed_coordinates(self):
        rng = np.random.default_rng(1910122)
        coordinates = self.coordinates.copy()
        coordinates[model.prior.source.allowed_cauchy_coordinates()["psi2"]] += rng.normal(size=96)
        coordinates, highest = self.assembled.apply(coordinates, self.highest, rng.normal(size=1168))
        value = model.exact_repeated_spatial_component(self.prepared, self.point, coordinates, highest)
        self.assertEqual(value, sp.Rational(self.report["chosen_exact_numerator"],
                                           self.report["chosen_exact_denominator"]))

    def test_releasing_a_tangential_psi4_coordinate_changes_the_component(self):
        highest = self.highest.copy()
        quartet = model.prior.joint.third.diagnostic.QUADS.index((2, 3, 3, 3))
        principal = model.prior.source.spatial.constraint_principal_map(self.prepared["data"]["psi"])
        column = int(np.argmax(abs(principal[0])))
        highest[880+24*quartet+column] += .125
        value = model.exact_repeated_spatial_component(self.prepared, self.point, self.coordinates, highest)
        before = sp.Rational(self.report["chosen_exact_numerator"], self.report["chosen_exact_denominator"])
        self.assertNotEqual(value, before)
        self.assertAlmostEqual(float(value-before), .125*principal[0, column], places=10)

    def test_scope_is_not_general_model_nonexistence(self):
        self.assertTrue(self.report["not_general_nonexistence_or_regional_evolution"])
        self.assertTrue(self.report["not_unrounded_action_or_interval_certificate"])


if __name__ == "__main__":
    unittest.main()
