"""Full nonzero-multiplier scalar Hessian and unprojected bounded completion."""
import importlib.util
import json
from pathlib import Path
import unittest
from unittest.mock import patch

import numpy as np


ROOT = Path(__file__).resolve().parents[3]
SPEC = importlib.util.spec_from_file_location(
    "cartan_next_scalar", ROOT / "analysis/HC_Cartan_Next_Scalar_Compatibility.py")
model = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(model)


class HCCartanNextScalarCompatibilityTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.prepared, cls.point, cls.saved = model.load_data()
        cls.report = json.loads((ROOT / "analysis/HC_Cartan_Next_Scalar_Compatibility.json").read_text(encoding="utf-8"))
        cls.solved = model.joint_system(cls.prepared, cls.point)
        cls.new = cls.solved["solution"]
        cls.old_scalar = model.scalar_jet(cls.prepared, cls.point, model.regular.unpack(cls.saved))
        cls.new_scalar = model.scalar_jet(cls.prepared, cls.point, model.regular.unpack(cls.new))

    def assertClose(self, actual, expected, atol=2e-8, rtol=3e-8):
        np.testing.assert_allclose(actual, expected, atol=atol, rtol=rtol)

    def test_authoritative_input_fingerprints_are_retained(self):
        self.assertEqual(self.report["input_sha256"], model.input_fingerprints())
        original = Path.read_bytes

        def windows_source_bytes(path):
            data = original(path)
            return data.replace(b"\r\n", b"\n").replace(b"\n", b"\r\n") if path.suffix in (".py", ".md") else data

        with patch.object(Path, "read_bytes", windows_source_bytes):
            self.assertEqual(self.report["input_sha256"], model.input_fingerprints())

    def test_lower_point_and_all_couplings_are_saved_without_change(self):
        kept = self.report["fixed_lower_point_and_couplings"]
        self.assertClose(kept["psi_real"], self.prepared["data"]["psi"].real)
        self.assertClose(kept["psi_imag"], self.prepared["data"]["psi"].imag)
        self.assertClose(kept["psi_first_real"], self.point["psi_first"].real)
        self.assertClose(kept["psi_first_imag"], self.point["psi_first"].imag)
        self.assertClose(kept["coframe_second"], self.point["coframe_second"])
        self.assertClose(kept["multiplier"], self.point["multiplier"])
        self.assertClose(kept["multiplier_first"], self.point["multiplier_first"])
        self.assertClose(np.array(kept["M_real"])+1j*np.array(kept["M_imag"]), model.MASS)
        self.assertClose(np.array(kept["Q_real"])+1j*np.array(kept["Q_imag"]), model.Q)
        self.assertEqual((kept["Einstein_coefficient"], kept["vacuum"]), (1., 0.))

    def test_offshell_identity_holds_without_normal_frame_or_cartan_solution(self):
        controls = model.random_identity_checks()
        self.assertEqual(len(controls), 12)
        self.assertLess(max(abs(c["identity_error"]) for c in controls), 1e-11)
        self.assertGreater(max(abs(c["probe_contraction"]) for c in controls), 1.)
        self.assertGreater(max(abs(c["constraint_contraction"]) for c in controls), 1.)

    def test_complete_nonzero_Z_term_is_retained_but_real_Q_contraction_vanishes(self):
        controls = model.random_identity_checks()
        self.assertGreater(min(c["Z_norm"] for c in controls), 1.)
        self.assertGreater(max(c["Z_contraction_magnitude"] for c in controls), 1.)
        self.assertLess(max(abs(c["Z_real_contraction"]) for c in controls), 1e-12)
        self.assertLess(max(c["Q_Z_commutator_norm"] for c in controls), 1e-12)

    def test_noncommuting_mass_is_not_silently_diagonalized_in_Q_basis(self):
        self.assertGreater(np.linalg.norm(model.Q @ model.MASS-model.MASS @ model.Q), .1)
        rng = np.random.default_rng(734)
        psi = rng.normal(size=(3, 4))+1j*rng.normal(size=(3, 4))
        self.assertAlmostEqual(model.prior.weighted_mass(psi), np.vdot(psi, model.H_MASS @ psi @ model.BETA.T).real)

    def test_original_56_point_equations_remain_satisfied(self):
        p = self.point
        value = model.spatial.rank_model.point_equations(self.prepared, p["psi_first"], p["coframe_second"],
                                                         p["multiplier"], p["multiplier_first"])["vector"]
        self.assertLess(np.linalg.norm(value), 1e-8)

    def test_saved_regular_jet_still_satisfies_its_384_equations(self):
        value = model.regular.equations(self.prepared, self.point, model.regular.unpack(self.saved))["vector"]
        self.assertLess(np.linalg.norm(value), 1e-8)

    def test_scalar_value_and_gradient_already_vanish_on_saved_jet(self):
        self.assertLess(abs(self.old_scalar["value"]), 1e-9)
        self.assertLess(np.linalg.norm(self.old_scalar["first"]), 1e-8)

    def test_scalar_hessian_is_symmetric_for_nonzero_multiplier(self):
        self.assertClose(self.old_scalar["hessian"], self.old_scalar["hessian"].T)
        self.assertClose(self.old_scalar["cross_q2_second"], self.old_scalar["cross_q2_second"].swapaxes(0, 1))

    def test_general_product_rule_keeps_all_five_terms(self):
        self.assertEqual(set(self.old_scalar["pieces"]),
                         {"volume", "mass", "lambda_second", "lambda_first_cross", "lambda_value_cross_second"})
        self.assertClose(self.old_scalar["hessian"], sum(self.old_scalar["pieces"].values()))

    def test_nonzero_multiplier_value_cross_term_cannot_be_dropped(self):
        self.assertGreater(np.linalg.norm(self.old_scalar["pieces"]["lambda_value_cross_second"]), .01)

    def test_frozen_jet_fails_the_next_necessary_scalar_gate(self):
        self.assertGreater(np.linalg.norm(self.old_scalar["hessian"]), 1.)
        self.assertClose(self.old_scalar["hessian"], self.report["frozen_saved_1200_jet"]["scalar_hessian"])

    def test_saved_jet_hessian_has_independent_stable_field_differences(self):
        checks = model.independent_differences(self.prepared, self.point, model.regular.unpack(self.saved))
        self.assertLess(min(c["Richardson_error"] for c in checks), 2e-4)
        self.assertLess(checks[1]["coarse_error"], checks[0]["coarse_error"]*.2)

    def test_repaired_jet_hessian_has_independent_stable_field_differences(self):
        checks = model.independent_differences(self.prepared, self.point, model.regular.unpack(self.new))
        self.assertLess(min(c["Richardson_error"] for c in checks), 2e-4)

    def test_zero_multiplier_limit_matches_old_special_case_formula(self):
        prepared, jets = model.spatial.rank_model.load_data()
        point = {"multiplier": np.zeros((4, 4)), "psi_first": prepared["data"]["first"],
                 "coframe_second": jets["e2"], "multiplier_first": jets["l1"]}
        actual = model.scalar_jet(prepared, point, jets)["hessian"]
        expected = model.spatial.rank_model.scalar_second_gate(prepared, jets)
        self.assertClose(actual, expected)

    def test_volume_hessian_term_is_present_even_when_prepared_value_cancels_it(self):
        altered = dict(self.prepared, data=dict(self.prepared["data"], psi=self.prepared["data"]["psi"]*1.01))
        value = model.scalar_jet(altered, self.point, model.regular.unpack(self.saved))
        expected = np.einsum("rsaa->rs", self.point["coframe_second"])*(4+model.prior.weighted_mass(altered["data"]["psi"]))
        self.assertClose(value["pieces"]["volume"], expected)
        self.assertGreater(np.linalg.norm(expected), .01)

    def test_hessian_formula_also_handles_a_fully_nonzero_multiplier_value(self):
        point = dict(self.point, multiplier=np.random.default_rng(737).normal(size=(4, 4))*.03)
        jets = model.regular.unpack(self.saved)
        analytic = model.scalar_jet(self.prepared, point, jets)["hessian"]
        coarse = model.hessian_difference(self.prepared, point, jets, .0003)
        fine = model.hessian_difference(self.prepared, point, jets, .00015)
        self.assertLess(np.linalg.norm((4*fine-coarse)/3-analytic), 2e-4)

    def test_general_volume_term_is_checked_on_independently_recomputed_cartan_fields(self):
        data = dict(self.prepared["data"], psi=1.03*self.prepared["data"]["psi"])
        prepared = model.prolong.prepare(data)
        point = dict(self.point, multiplier=np.random.default_rng(738).normal(size=(4, 4))*.03)
        jets = model.regular.unpack(self.saved)
        scalar = model.scalar_jet(prepared, point, jets)
        self.assertGreater(np.linalg.norm(scalar["pieces"]["volume"]), .01)
        coarse = model.hessian_difference(prepared, point, jets, .0003)
        fine = model.hessian_difference(prepared, point, jets, .00015)
        self.assertLess(np.linalg.norm((4*fine-coarse)/3-scalar["hessian"]), 2e-4)

    def test_general_affine_map_keeps_all_394_rows_and_1200_columns(self):
        self.assertEqual(self.solved["matrix"].shape, (394, 1200))
        self.assertEqual(self.solved["residual"].shape, (394,))

    def test_joint_equations_are_affine_with_lower_point_fixed(self):
        x = np.random.default_rng(735).normal(size=1200)*.2
        direct = self.solved["evaluate"](x)
        self.assertClose(direct, self.solved["base"]+self.solved["matrix"] @ x)

    def test_affinity_includes_mixed_second_and_third_jet_blocks(self):
        rng = np.random.default_rng(736)
        x, y = rng.normal(size=(2, 1200))*.1
        f = self.solved["evaluate"]
        self.assertClose(f(2*x-.3*y), 2*f(x)-.3*f(y)-.7*f(np.zeros(1200)))

    def test_scalar_hessian_has_no_fourth_spinor_coframe_or_third_multiplier_jet_input(self):
        jets = model.regular.unpack(self.saved)
        actual = model.scalar_jet(self.prepared, self.point, jets)["hessian"]
        jets = dict(jets, p4=np.ones((4,)*4+(3, 4))*1e6,
                    e4=np.ones((4,)*6)*1e6, l3=np.ones((4,)*5)*1e6)
        self.assertClose(model.scalar_jet(self.prepared, self.point, jets)["hessian"], actual)

    def test_nonzero_multiplier_hessian_really_depends_on_existing_third_jets(self):
        matrix = self.solved["matrix"][384:]
        self.assertGreater(np.linalg.norm(matrix[:, 720:]), .01)

    def test_previous_384_rank_remains_332(self):
        singular = np.linalg.svd(self.solved["matrix"][:384], compute_uv=False)
        self.assertEqual(np.sum(singular > singular[0]*1e-10), 332)

    def test_rank_increase_is_recorded_against_unprojected_matrix(self):
        self.assertEqual(self.solved["rank"], self.report["joint_394_system"]["rank"])
        self.assertEqual(self.solved["rank"]-332, self.report["joint_394_system"]["additional_rank"])
        self.assertGreater(self.solved["rank"], 332)
        self.assertLessEqual(self.solved["rank"], 342)

    def test_noether_row_identities_of_previous_system_remain_valid(self):
        relations = model.regular.noether_dependencies(self.prepared, self.point)
        self.assertLess(np.linalg.norm(relations @ self.solved["matrix"][:384]), 1e-7)
        self.assertLess(np.linalg.norm(relations @ self.solved["base"][:384]), 1e-8)

    def test_joint_completion_keeps_every_previous_equation(self):
        value = model.regular.equations(self.prepared, self.point, model.regular.unpack(self.new))
        self.assertLess(np.linalg.norm(value["vector"]), 1e-8)
        for key in ("constraint_first", "probe_first", "coframe_Euler_first", "constraint_second"):
            self.assertLess(np.linalg.norm(value[key]), 1e-8)

    def test_joint_completion_satisfies_all_ten_scalar_hessian_conditions(self):
        self.assertLess(np.linalg.norm(self.new_scalar["hessian"]), 1e-8)
        self.assertLess(np.linalg.norm(model.packed_hessian(self.prepared, self.point, self.new)), 1e-8)

    def test_all_394_direct_residuals_are_small_without_projection(self):
        self.assertLess(np.linalg.norm(self.solved["evaluate"](self.new)), 1e-8)

    def test_saved_new_coordinates_reproduce_full_residual(self):
        saved = np.array(self.report["joint_394_system"]["jet_coordinates"])
        self.assertEqual(saved.shape, (1200,))
        self.assertLess(np.linalg.norm(self.solved["evaluate"](saved)), 1e-8)
        self.assertClose(self.solved["evaluate"](saved), self.report["joint_394_system"]["residuals"]["full_394_residual"])

    def test_repair_changes_only_allowed_higher_coordinates(self):
        self.assertGreater(np.linalg.norm(self.new-self.saved), 1.)
        self.assertTrue(self.report["joint_394_system"]["lower_point_unchanged"])
        self.assertEqual(self.report["highest_derivatives_used"], {"Psi": 3, "E": 3, "lambda": 2})

    def test_repaired_jet_is_still_not_an_off_origin_solution(self):
        fields = model.regular.taylor_fields(self.prepared, self.point, model.regular.unpack(self.new),
                                            np.array([.001, .0003, -.0002, .0001]))
        self.assertGreater(np.linalg.norm(fields["constraint"]), 1e-8)
        self.assertGreater(np.linalg.norm(fields["probe"]), 1e-8)
        self.assertLess(np.linalg.norm(fields["Cartan"]), 1e-10)

    def test_regular_temporal_block_is_unchanged_at_the_lower_point(self):
        block = model.spatial.rank_model.probe_constraint_block(np.eye(4), self.prepared["data"]["psi"], self.point["multiplier"])
        self.assertGreater(block["weight_eigenvalues"][0], .96)
        self.assertGreater(block["singular_values"][-1], .03)

    def test_no_native_cauchy_main_document_release_or_git_claim(self):
        self.assertIn("no Cauchy solution or native physics", self.report["status"])
        self.assertFalse(self.report["main_TeX_PDF_release_changed"])
        self.assertFalse(self.report["git_operations"])
        self.assertTrue(self.report["new_higher_derivatives_cannot_change_the_frozen_hessian"])


if __name__ == "__main__":
    unittest.main()
