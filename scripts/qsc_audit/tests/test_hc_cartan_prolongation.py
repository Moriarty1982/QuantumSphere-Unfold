"""Higher normal-point jets, retained reactions and independently checked curvature matching."""
import hashlib
import importlib.util
import itertools
import json
from pathlib import Path
import unittest

import numpy as np


ROOT = Path(__file__).resolve().parents[3]
SPEC = importlib.util.spec_from_file_location("cartan_prolongation", ROOT / "analysis/HC_Cartan_Prolongation.py")
model = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(model)


class HCCartanProlongationTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.data, cls.previous = model.load_prior()
        cls.prepared = model.prepare(cls.data)
        cls.solved = model.solve(cls.prepared)
        cls.jets, cls.result = cls.solved["jets"], cls.solved["result"]
        cls.report = model.evaluate(cls.solved)

    def assertClose(self, actual, expected, atol=1e-9, rtol=3e-7):
        np.testing.assert_allclose(actual, expected, atol=atol, rtol=rtol)

    def test_preserves_parent_state_first_derivatives_and_resonance_data(self):
        data, _ = model.load_prior()
        self.assertClose(self.data["psi"], data["psi"])
        self.assertClose(self.data["first"], data["first"])
        self.assertClose(model.MASS, [[0.6, 0, 4], [0, 0.6, 0.7], [4, 0.7, 0.6]])
        self.assertClose(model.Q, model.odd.Q_PHASE)

    def test_third_jet_coordinates_obey_every_mixed_partial_symmetry(self):
        for key in ("e3", "p3"):
            tensor = self.jets[key]
            for permutation in itertools.permutations(range(3)):
                self.assertClose(tensor.transpose((*permutation, 3, 4)), tensor)

    def test_bad_coordinate_dimension_is_rejected(self):
        with self.assertRaises(ValueError):
            model.unpack(np.zeros(1423))

    def test_normal_lc_formula_matches_existing_bundle(self):
        rng = np.random.default_rng(8341)
        for _ in range(3):
            first = rng.normal(size=(4, 4, 4))
            self.assertClose(model.normal_lorentz(first), model.dirac.bundle(np.eye(4), first)["omega"])

    def test_normal_gravity_euler_retains_torsion_curvature_not_symmetrized_ricci(self):
        rng = np.random.default_rng(1451)
        omega = model.cartan.unpack(rng.normal(size=24))
        dw = np.array([model.cartan.unpack(rng.normal(size=24)) for _ in range(4)])
        curvature = model.cartan.curvature_upper(omega, dw)
        zero = np.zeros((3, 4), complex)
        expected = model.cartan.coframe_euler(np.eye(4), zero, np.zeros((4, 3, 4)), omega,
                                               curvature, model.MASS, np.zeros((4, 4)))
        self.assertClose(model.gravity_euler(curvature), expected)

    def test_source_forms_reproduce_actual_independent_spin_source(self):
        p = self.data["psi"]
        source = np.einsum("ri,pij,rj->p", p.conj(), self.prepared["source_forms"], p).real
        self.assertClose(source, self.prepared["source"])

    def test_fast_cartan_contractions_match_original_full_formulas_off_normal_point(self):
        rng = np.random.default_rng(9811)
        e = np.eye(4)+0.03*rng.normal(size=(4, 4))
        p = self.data["psi"]+0.01*(rng.normal(size=(3, 4))+1j*rng.normal(size=(3, 4)))
        h, response, source = model.fast_cartan_data(self.prepared, e, p)
        expected_response, expected_source = model.cartan.spin_maps(e, p)
        self.assertClose(h, model.cartan.contorsion_hessian(e))
        self.assertClose(response, expected_response)
        self.assertClose(source, expected_source)

    def test_coframe_hessian_derivative_is_independently_differentiated(self):
        rng = np.random.default_rng(471)
        d = rng.normal(size=(4, 4))
        step = 1e-5
        difference = (model.cartan.contorsion_hessian(np.eye(4)+step*d)
                      -model.cartan.contorsion_hessian(np.eye(4)-step*d))/(2*step)
        self.assertClose(np.einsum("am,ampq->pq", d, self.prepared["hessian_first"]), difference, atol=1e-8)

    def test_source_first_jet_is_the_actual_quadratic_polarization(self):
        _, base = model.cartan.spin_maps(np.eye(4), self.data["psi"])
        for r, u in enumerate(self.data["first"]):
            _, mixed = model.cartan.spin_maps(np.eye(4), self.data["psi"]+u)
            _, quadratic = model.cartan.spin_maps(np.eye(4), u)
            self.assertClose(self.prepared["source_first"][r], mixed-base-quadratic)

    def test_previous_connection_first_jet_is_preserved_before_new_solve(self):
        expected = model.prior.connection_first(self.data, self.previous["e2"], self.previous["l1"])
        self.assertClose(model.connection_jets(self.prepared, self.previous)[0], expected)

    def test_previous_point_equations_and_first_constraint_remain_as_previously_reported(self):
        old = model.evaluate_jets(self.prepared, self.previous)
        self.assertClose(old["constraint_first"], 0)
        self.assertClose(old["coframe_Euler"], 0)
        self.assertClose(old["probe"], 0)
        self.assertClose(old["constraint"], 0)

    def test_old_scalar_gate_exposes_failure_of_frozen_lower_jet(self):
        gate = model.scalar_gate(self.prepared, self.previous)
        self.assertClose(gate, [3.7044327695, 3.7398175967, 5.8631454124, -5.5006821138])
        self.assertGreater(np.linalg.norm(gate), 9.)

    def test_scalar_gate_is_an_offshell_weighted_equation_identity_not_a_conserved_Q_charge(self):
        rng = np.random.default_rng(214)
        jets = model.unpack(rng.normal(size=1424)*0.1)
        result = model.evaluate_jets(self.prepared, jets)
        p, dp = self.data["psi"], self.data["first"]
        remainder = np.array([np.vdot(model.Q @ p, r).real+np.vdot(model.Q @ u, result["probe"]).real
                              for r, u in zip(result["probe_first"], dp)])
        remainder += np.trace(result["constraint_first"], axis1=1, axis2=2)
        self.assertClose(model.scalar_gate(self.prepared, jets)+remainder, 0)

    def test_equation_map_is_affine_in_all_higher_jet_coordinates(self):
        rng = np.random.default_rng(398)
        x = rng.normal(size=1424)*0.03
        expected = self.solved["base"]+self.solved["matrix"] @ x
        self.assertClose(model.evaluate_jets(self.prepared, model.unpack(x))["vector"], expected)

    def test_full_joint_system_sizes_and_evaluated_rank(self):
        self.assertEqual(self.solved["matrix"].shape, (404, 1424))
        self.assertEqual(self.solved["rank"], 360)
        self.assertGreater(self.solved["singular_values"][359], 1e-6)

    def test_unprojected_joint_residual_is_small(self):
        self.assertLess(self.solved["norm"], 1e-8)
        self.assertLess(np.linalg.norm(self.solved["matrix"] @ self.solved["solution"]+self.solved["base"]), 1e-8)

    def test_multiplier_divergence_is_retained_as_chosen_lower_branch_condition(self):
        self.assertClose(np.einsum("mam->a", self.jets["l1"]), 0)

    def test_new_scalar_compatibility_gate_is_satisfied(self):
        self.assertClose(self.solved["scalar_gate"], 0)
        self.assertGreater(np.linalg.norm(self.jets["l1"]-self.previous["l1"]), 0.1)

    def test_lower_spinor_state_and_first_derivatives_are_not_refitted(self):
        saved, _ = model.load_prior()
        fields = model.taylor_fields(self.prepared, self.jets, np.zeros(4))
        self.assertClose(fields["psi"], saved["psi"])
        self.assertClose(fields["first_p"], saved["first"])

    def test_point_probe_and_constraint_are_still_satisfied(self):
        self.assertClose(self.result["probe"], 0)
        self.assertClose(self.result["constraint"], 0)

    def test_coframe_equation_and_every_first_derivative_are_satisfied(self):
        self.assertClose(self.result["coframe_Euler"], 0)
        self.assertClose(self.result["coframe_Euler_first"], 0)

    def test_constraint_matches_through_second_order(self):
        self.assertClose(self.result["constraint_first"], 0)
        self.assertClose(self.result["constraint_second"], 0)

    def test_complete_probe_equation_matches_through_first_order(self):
        self.assertClose(self.result["probe_first"], 0)

    def test_second_probe_coframe_and_multiplier_jets_are_symmetric(self):
        for key in ("e2", "p2", "l2"):
            self.assertClose(self.jets[key], self.jets[key].swapaxes(0, 1))

    def test_connection_second_jet_agrees_with_independent_field_differences(self):
        self.assertLess(self.report["independent_checks"]["connection_second_fd_error"], 3e-4)

    def test_cross_readout_second_jet_is_checked_independently(self):
        self.assertLess(self.report["independent_checks"]["cross_second_fd_error"], 0.001)

    def test_cross_and_independent_metric_curvatures_match_at_the_point(self):
        r = self.report["independent_checks"]
        self.assertLess(r["curvature_match_fd_error"], 0.002)
        self.assertClose(r["coframe_LC_scalar_unscaled"], r["cross_LC_scalar_fd_unscaled"], atol=0.001)

    def test_probe_first_derivative_is_checked_in_all_four_coordinate_directions(self):
        self.assertLess(self.report["independent_checks"]["probe_first_fd_error"], 0.0005)

    def test_coframe_first_derivative_is_checked_independently(self):
        self.assertLess(self.report["independent_checks"]["coframe_Euler_first_fd_error"], 0.001)

    def test_constraint_remainder_is_cubic_and_nonzero(self):
        samples = self.report["independent_checks"]["samples_not_exact_solutions"]
        for a, b in zip(samples, samples[1:]):
            self.assertGreater(a["constraint_norm"]/b["constraint_norm"], 7.8)
            self.assertLess(a["constraint_norm"]/b["constraint_norm"], 8.2)
        self.assertGreater(samples[-1]["constraint_norm"], 1e-9)

    def test_probe_remainder_is_quadratic_and_nonzero(self):
        samples = self.report["independent_checks"]["samples_not_exact_solutions"]
        for a, b in zip(samples, samples[1:]):
            self.assertGreater(a["probe_norm"]/b["probe_norm"], 3.8)
            self.assertLess(a["probe_norm"]/b["probe_norm"], 4.2)
        self.assertGreater(samples[-1]["probe_norm"], 1e-6)

    def test_coframe_euler_remainder_is_quadratic_and_nonzero(self):
        samples = self.report["independent_checks"]["samples_not_exact_solutions"]
        for a, b in zip(samples, samples[1:]):
            self.assertGreater(a["coframe_Euler_norm"]/b["coframe_Euler_norm"], 3.8)
            self.assertLess(a["coframe_Euler_norm"]/b["coframe_Euler_norm"], 4.2)
        self.assertGreater(samples[-1]["coframe_Euler_norm"], 1e-6)

    def test_full_auxiliary_connection_equation_remains_solved_nearby(self):
        for sample in self.report["independent_checks"]["samples_not_exact_solutions"]:
            self.assertLess(sample["Cartan_norm"], 1e-10)

    def test_cubic_temporal_bound_retains_quadratic_multiplier_contribution(self):
        bound = model.temporal_ball_bound(self.jets)
        self.assertGreater(bound["temporal_eigenvalue_lower_bound"], 0.25)
        self.assertLessEqual(bound["coframe_perturbation_bound"], 0.1)
        self.assertGreater(np.linalg.norm(self.jets["l2"]), 0.1)

    def test_positive_temporal_form_and_full_rank_on_multiple_ball_directions(self):
        bound = model.temporal_ball_bound(self.jets)
        radius = bound["radius_in_arbitrary_comparison_coordinates"]
        for direction in (*np.eye(4), np.ones(4)/2):
            fields = model.taylor_fields(self.prepared, self.jets, radius*direction)
            self.assertGreaterEqual(np.linalg.eigvalsh(fields["weights"][0])[0], bound["temporal_eigenvalue_lower_bound"])
            self.assertEqual(np.linalg.matrix_rank(fields["coframe"]), 4)

    def test_saved_coordinates_reproduce_all_joint_equations(self):
        saved = json.loads((ROOT / "analysis/HC_Cartan_Prolongation.json").read_text(encoding="utf-8"))
        result = model.evaluate_jets(self.prepared, model.unpack(saved["jet_coordinates"]))
        self.assertLess(np.linalg.norm(result["vector"]), 1e-8)

    def test_input_fingerprint_identifies_the_unchanged_previous_jet(self):
        expected = hashlib.sha256((ROOT / "analysis/HC_Cartan_Compatible_Jets.json").read_bytes()).hexdigest()
        self.assertEqual(self.report["previous_input_sha256"], expected)

    def test_higher_derivatives_alone_cannot_repair_a_frozen_scalar_gate(self):
        rng = np.random.default_rng(931)
        changed = dict(self.previous)
        changed["e3"] = model.unpack_third(rng.normal(size=320))
        changed["p3"] = model.unpack_third(rng.normal(size=480), True)
        changed["l2"] = model.prior.unpack_second(rng.normal(size=160))
        self.assertClose(model.scalar_gate(self.prepared, changed), model.scalar_gate(self.prepared, self.previous))

    def test_metric_curvature_is_not_a_flat_or_a_physically_calibrated_prediction(self):
        self.assertGreater(abs(self.report["independent_checks"]["coframe_LC_scalar_unscaled"]), 5.)
        self.assertGreater(np.linalg.norm(self.jets["e2"]), 1.)

    def test_report_keeps_evolution_native_and_higher_order_obligations_open(self):
        self.assertTrue(self.report["prolonged_equations_numerically_satisfied"])
        self.assertTrue(self.report["second_order_cross_curvature_matching_at_origin_only"])
        self.assertFalse(self.report["main_TeX_changed"])
        self.assertIn("no evolved/native solution", self.report["status"])
        self.assertIn("Cauchy", " ".join(self.report["remaining"]))


if __name__ == "__main__":
    unittest.main()
