"""Canonical normal quotient and response diagnostics, not new physical modes."""
import hashlib
import importlib.util
import json
from pathlib import Path
import unittest

import numpy as np


ROOT = Path(__file__).resolve().parents[3]
SPEC = importlib.util.spec_from_file_location("remaining_multiplier", ROOT / "analysis/HC_Cartan_Remaining_Multiplier.py")
model = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(model)


class HCCartanRemainingMultiplierTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.prepared, cls.point, cls.jets = model.load_data()
        cls.quotient = model.quotient_data(cls.prepared, cls.point)
        cls.basis = cls.quotient["basis"]
        cls.effects = model.effect_maps(cls.prepared, cls.point, cls.jets, cls.basis)
        cls.report = json.loads((ROOT / "analysis/HC_Cartan_Remaining_Multiplier.json").read_text(encoding="utf-8"))

    def assertClose(self, actual, expected, atol=2e-10):
        np.testing.assert_allclose(actual, expected, atol=atol, rtol=2e-9)

    def test_both_saved_input_fingerprints_are_retained(self):
        for name, expected in self.report["input_sha256"].items():
            self.assertEqual(hashlib.sha256((ROOT / "analysis" / name).read_bytes()).hexdigest(), expected)

    def test_saved_canonical_basis_is_reproducible(self):
        self.assertClose(self.basis, self.report["parametrization"]["normal_basis_56_by_6"])

    def test_original_mass_selector_and_multiplier_value_are_unchanged(self):
        saved = self.report["unchanged"]
        self.assertClose(model.prior.MASS, saved["mass"])
        self.assertClose(model.spatial.Q, np.array(saved["selector_real"])+1j*np.array(saved["selector_imaginary"]))
        self.assertClose(self.point["multiplier"], saved["multiplier_value"])
        self.assertEqual((saved["Einstein_coefficient"], saved["vacuum"]), (1., 0.))

    def test_normal_perturbation_does_not_mutate_any_input(self):
        saved = {key: value.copy() for key, value in self.point.items()}
        model.normal_point(self.point, self.basis @ np.arange(6))
        for key in self.point:
            self.assertClose(self.point[key], saved[key])

    def test_wrong_normal_coordinate_count_is_rejected(self):
        with self.assertRaises(ValueError):
            model.normal_point(self.point, np.zeros(55))

    def test_degenerate_axial_or_normalization_branch_is_not_silently_used(self):
        prepared = dict(self.prepared, data=dict(self.prepared["data"], psi=np.zeros((3, 4), complex)))
        with self.assertRaises(ValueError):
            model.canonical_basis(prepared)
        with self.assertRaises(ValueError):
            model.raw_compensating_velocity(np.ones(3), 0.)
        with self.assertRaises(ValueError):
            model.closed_contorsion(np.ones(4), np.ones(3), 0.)

    def test_principal_response_formula_rejects_unaccounted_spinor_change(self):
        direction = self.basis[:, 0].copy()
        direction[16] = 1
        with self.assertRaises(ValueError):
            model.analytic_effects(self.prepared, direction)

    def test_normal_rank_and_six_quotient_coordinates(self):
        self.assertEqual(self.quotient["normal"]["matrix"].shape, (68, 56))
        self.assertEqual(self.quotient["normal"]["rank"], 40)
        self.assertEqual(model.rank(self.basis), 6)
        self.assertEqual(model.rank(self.quotient["combined"]), 16)

    def test_basis_is_orthogonal_to_the_ten_exhibited_leading_gauge_directions(self):
        self.assertEqual(model.rank(self.quotient["gauge"]), 10)
        self.assertClose(self.quotient["gauge"].T @ self.basis, 0.)

    def test_combined_basis_spans_the_full_observed_normal_kernel(self):
        self.assertLess(np.linalg.norm(self.quotient["kernel_span_error"]), 1e-10)
        self.assertClose(self.quotient["normal"]["matrix"] @ self.basis, 0.)

    def test_spatial_multiplier_projection_is_injective_on_quotient(self):
        self.assertEqual(model.rank(self.basis[40:][model.SPATIAL_INDICES]), 6)

    def test_temporal_spinor_and_temporal_multiplier_column_do_not_change(self):
        self.assertClose(self.basis[16:40], 0.)
        self.assertClose(self.basis[40:][[0, 4, 8, 12]], 0.)

    def test_temporal_probe_weights_and_schur_block_stay_regular(self):
        psi = self.prepared["data"]["psi"]
        base = model.spatial.rank_model.probe_constraint_block(np.eye(4), psi, self.point["multiplier"])
        self.assertGreater(base["weight_eigenvalues"][0], .96)
        self.assertGreater(base["singular_values"][-1], .03)
        for column in self.basis.T:
            shifted = model.normal_point(self.point, column)
            self.assertClose(shifted["multiplier"], self.point["multiplier"])

    def test_clifford_axial_response_matches_all_gamma_matrix_entries(self):
        self.assertClose(model.axial_response(self.quotient["weighted_axial"]), self.prepared["response"], atol=1e-14)
        rng = np.random.default_rng(831)
        for _ in range(3):
            psi = rng.normal(size=(3, 4))+1j*rng.normal(size=(3, 4))
            response, _ = model.cartan.spin_maps(np.eye(4), psi)
            axial = model.cartan.axial_currents(psi)[1]
            self.assertClose(model.axial_response(axial), response, atol=1e-13)

    def test_axial_covector_gives_exact_cartan_source_nulls(self):
        source = self.prepared["response"].T @ self.basis[40:, :3]
        self.assertClose(source, 0.)
        self.assertClose(self.basis[:40, :3], 0.)

    def test_compensation_hessian_identity_checks_every_bilinear_coefficient(self):
        identity = model.coefficient_identity(self.prepared)
        self.assertEqual(identity["H_integer_error"], 0.)
        np.testing.assert_array_equal(identity["residuals"], np.zeros((12, 24)))

    def test_three_accelerations_have_declared_longitudinal_symmetric_form(self):
        unit = self.quotient["spatial_axial_unit"]
        for i, v in enumerate(np.eye(3)):
            h = self.basis[:16, 3+i].reshape(4, 4)
            self.assertClose(h[0], 0.)
            self.assertClose(h[:, 0], 0.)
            self.assertClose(h[1:, 1:], np.outer(unit, v)+np.outer(v, unit))

    def test_closed_multiplier_formula_agrees_with_unique_perpendicular_compensation(self):
        matrix = self.quotient["compensation_map"]
        self.assertEqual(model.rank(matrix), 12)
        self.assertLess(np.linalg.norm(self.quotient["compensation_residual"]), 1e-12)
        u = self.quotient["axial_covector_unit"]
        for i in range(3):
            self.assertClose(u @ self.basis[40:, 3+i].reshape(4, 4), 0.)

    def test_closed_contorsion_formula_matches_source_elimination(self):
        a = self.quotient["weighted_axial"]
        for i, v in enumerate(np.eye(3)):
            effects = model.analytic_effects(self.prepared, self.basis[:, 3+i])
            expected = model.closed_contorsion(a, v, np.linalg.norm(a[1:]))
            self.assertClose(effects["contorsion_first"][0], expected)

    def test_three_compensated_directions_are_not_cartan_source_nulls(self):
        self.assertEqual(model.rank(self.prepared["response"].T @ self.basis[40:]), 3)
        self.assertEqual(model.rank(self.effects["contorsion_first"][:, 3:]), 3)

    def test_schur_nulls_are_not_confused_with_source_nulls(self):
        l, hinv = self.prepared["response"], self.prepared["inverse_hessian"]
        schur = l @ hinv @ l.T
        self.assertEqual(model.rank(l), 12)
        self.assertEqual(model.rank(schur), 9)
        self.assertEqual(model.rank(schur @ self.basis[40:]), 2)
        longitudinal = self.basis[:, 3:] @ self.quotient["spatial_axial_unit"]
        self.assertClose(schur @ longitudinal[40:], 0.)
        self.assertGreater(np.linalg.norm(l.T @ longitudinal[40:]), .1)
        self.assertGreater(np.linalg.norm(longitudinal[:16]), 1.)

    def test_gravity_plus_mixed_curls_annihilates_all_spatial_connection_variations(self):
        blocks = model.spatial_connection_blocks(self.prepared)
        self.assertEqual(model.rank(blocks["gravity"]), 12)
        self.assertEqual(model.rank(blocks["mixed_curls"]), 9)
        self.assertEqual(model.rank(blocks["joint"]), 18)
        symmetric_rotations = []
        axial_time = self.quotient["weighted_axial"][0]
        for j, k in model.prior.PAIR2:
            if j == 0:
                continue
            rotation = np.zeros((3, 3))
            rotation[j-1, k-1] = rotation[k-1, j-1] = 1
            connection = np.zeros((4, 4, 4))
            connection[1:, 1:, 1:] = np.einsum("kjl,ik->ijl", model.EPSILON[0, 1:, 1:, 1:], rotation)
            coordinates = model.cartan.pack(connection)[6:]
            symmetric_rotations.append(coordinates)
            self.assertClose(blocks["gravity"] @ coordinates, 0.)
            self.assertClose((blocks["mixed_curls"] @ coordinates).reshape(4, 3)[1:], axial_time*rotation.T/2)
        self.assertEqual(model.rank(np.array(symmetric_rotations).T), 6)

    def test_fixing_coframe_acceleration_leaves_only_three_axial_nulls(self):
        normal = self.quotient["normal"]["matrix"]
        self.assertEqual(model.rank(normal[:, 40:][:, model.SPATIAL_INDICES]), 9)
        removed = self.basis[:, 3:].copy()
        removed[:16] = 0
        self.assertEqual(model.rank(normal @ removed), 3)

    def test_all_original_point_equations_are_unchanged_without_projection(self):
        self.assertClose(self.effects["point_equations"], 0.)
        x = self.basis @ np.array([.2, -.3, .4, -.5, .6, -.7])
        p = model.normal_point(self.point, x)
        result = model.spatial.rank_model.point_equations(
            self.prepared, p["psi_first"], p["coframe_second"], p["multiplier"], p["multiplier_first"])
        self.assertLess(np.linalg.norm(result["vector"]), 1e-11)
        self.assertLess(np.linalg.norm(model.spatial.curl_constraints(self.prepared, p)), 1e-10)

    def test_independent_connection_value_is_unchanged_for_all_six(self):
        old = model.spatial.connection_first(self.prepared, self.point)[0]
        for x in self.basis.T:
            self.assertClose(model.spatial.connection_first(self.prepared, model.normal_point(self.point, x))[0], old)

    def test_only_three_connection_derivative_directions_are_nonzero(self):
        self.assertEqual(model.rank(self.effects["connection_first"]), 3)
        self.assertClose(self.effects["connection_first"][:, :3], 0.)
        for column in self.basis.T:
            effect = model.analytic_effects(self.prepared, column)["connection_first"]
            self.assertClose(effect[1:], 0.)
            self.assertClose(effect[0, 1:], 0.)

    def test_cartan_curvature_is_unchanged_but_lc_metric_curvature_is_not(self):
        self.assertClose(self.effects["curvature"], 0.)
        self.assertEqual(model.rank(self.effects["LC_curvature"]), 3)
        self.assertClose(self.effects["LC_curvature"][:, :3], 0.)
        first = np.zeros((4, 4, 4))
        baseline = model.prolong.dirac.bundle(np.eye(4), first, self.point["coframe_second"])["curvature"]["riemann"]
        differences = []
        for x in self.basis.T:
            point = model.normal_point(self.point, x)
            metric = model.prolong.dirac.bundle(np.eye(4), first, point["coframe_second"])["curvature"]["riemann"]
            differences.append((metric-baseline).reshape(-1))
        self.assertEqual(model.rank(np.array(differences).T), 3)
        self.assertClose(np.array(differences)[:3], 0.)

    def test_torsion_first_derivative_sees_three_compensated_directions(self):
        self.assertEqual(model.rank(self.effects["torsion_first"]), 3)
        self.assertClose(self.effects["torsion_first"][:, :3], 0.)

    def test_cartan_linear_equation_and_direct_connection_reconstruction_agree(self):
        self.assertClose(self.effects["Cartan_linear_residual"], 0.)
        self.assertClose(self.effects["direct_connection_error"], 0.)
        self.assertClose(self.effects["direct_curvature_error"], 0.)

    def test_only_temporal_temporal_first_coframe_constraint_can_change(self):
        self.assertEqual(model.rank(self.effects["constraint_first"]), 2)
        self.assertClose(self.effects["constraint_first"][:, :3], 0.)
        tensor = self.effects["constraint_first"].T.reshape(6, 4, 4, 4)
        self.assertClose(tensor[:, 1:], 0.)
        self.assertClose(tensor[:, 0, :, 1:], 0.)

    def test_changed_first_constraint_is_repairable_by_a_symmetric_second_spinor_derivative(self):
        principal = model.spatial.constraint_principal_map(self.prepared["data"]["psi"])
        base = model.spatial.constraint_first(self.prepared, self.point, self.jets["p2"])
        for x in self.basis[:, 3:].T:
            point = model.normal_point(self.point, x)
            changed = model.spatial.constraint_first(self.prepared, point, self.jets["p2"])-base
            p2 = self.jets["p2"].copy()
            p2[0, 0] -= model.prior.complexify(np.linalg.pinv(principal) @ changed[0, :, 0], (3, 4))
            self.assertClose(model.spatial.constraint_first(self.prepared, point, p2), base)

    def test_first_probe_equations_detect_all_six_with_higher_jets_frozen(self):
        self.assertEqual(model.rank(self.effects["first_probe_equations"]), 6)
        self.assertGreater(np.linalg.svd(self.effects["first_probe_equations"], compute_uv=False)[-1], .5)

    def test_first_gravity_and_second_constraints_also_detect_all_six_when_frozen(self):
        self.assertEqual(model.rank(self.effects["first_gravity_equations"]), 6)
        self.assertEqual(model.rank(self.effects["second_constraint_equations"]), 6)

    def test_probe_density_derivative_detects_all_six(self):
        self.assertEqual(model.rank(self.effects["kinetic_density_first"]), 6)

    def test_frozen_higher_response_is_affine_not_a_projected_success(self):
        self.assertLess(np.linalg.norm(self.effects["higher_affinity_error"]), 1e-9)
        self.assertEqual(model.rank(self.effects["higher_equations"]), 6)
        self.assertGreater(np.linalg.norm(self.effects["higher_equations"]), 100.)

    def test_axial_value_shift_is_not_an_algebraic_parent_redundancy(self):
        result = model.algebraic_value_control(self.prepared, self.point, self.basis)
        self.assertEqual(model.rank(result), 3)
        self.assertClose(result, self.basis[40:, :3])

    def test_taylor_field_differences_independently_check_the_response_formulas(self):
        differences = model.field_difference_checks(self.prepared, self.point, self.jets, self.basis)
        for name in ("connection_first_errors", "constraint_first_errors", "probe_first_errors", "torsion_first_errors"):
            self.assertLess(max(differences[name]), 5e-7)

    def test_new_report_retains_scope_and_does_not_claim_a_cauchy_solution(self):
        self.assertFalse(self.report["main_TeX_or_PDF_changed"])
        self.assertIn("added neutral odd-cross Cartan comparison", self.report["status"])
        self.assertIn("constraint closure or a Cauchy solution", self.report["not_claimed"])


if __name__ == "__main__":
    unittest.main()
