"""Native closed-sector jets and the declared gauge-fixed Euclidean comparison."""
import importlib.util
import json
from pathlib import Path
import unittest

import numpy as np


ROOT = Path(__file__).resolve().parents[3]
SPEC = importlib.util.spec_from_file_location(
    "closure_hessian", ROOT / "analysis/HC_Closure_Fluctuation_Hessian.py")
model = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(model)


class HCClosureFluctuationHessianTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.p = np.diag([1.0, 0.0])
        cls.m = np.diag([0.4, 1.3])
        cls.k = np.array([0.3, 0.8, -0.4, 0.5])
        cls.data = model.symbol(cls.k, cls.p)
        cls.report = model.evaluate()

    def setUp(self):
        self.rng = np.random.default_rng(511)

    def assertClose(self, actual, expected, rtol=2e-8, atol=1e-11):
        np.testing.assert_allclose(actual, expected, rtol=rtol, atol=atol)

    def test_hermitian_color_basis_is_trace_orthonormal(self):
        for n in (1, 2, 3):
            b = model.hermitian_basis(n)
            self.assertClose(b, b.conj().swapaxes(-1, -2))
            self.assertClose(np.einsum("aij,bji->ab", b, b), np.eye(n*n))

    def test_projector_tangent_is_off_diagonal_and_has_correct_real_dimension(self):
        p = np.diag([1, 1, 0])
        tangent = model.tangent_basis(p)
        self.assertEqual(len(tangent), 4)
        self.assertClose(p @ tangent+tangent @ p, tangent)
        self.assertClose(p @ tangent @ p, 0)
        self.assertClose(np.einsum("aij,bji->ab", tangent, tangent), np.eye(4))

    def test_zero_and_full_projectors_have_no_tangent(self):
        for p in (np.zeros((2, 2)), np.eye(2)):
            self.assertEqual(model.tangent_basis(p).shape, (0, 2, 2))

    def test_projector_path_preserves_rank_and_idempotence(self):
        x = np.array([[0.1, 1-0.3j], [1+0.3j, -0.2]])
        for e in (-0.7, 0, 0.3):
            p = model.projector_path(self.p, x, e)
            self.assertClose(p @ p, p)
            self.assertClose(np.trace(p), 1)
        e = 1e-5
        derivative = (model.projector_path(self.p, x, e)-model.projector_path(self.p, x, -e))/(2*e)
        self.assertClose(derivative, 1j*(x @ self.p-self.p @ x))

    def test_minimal_closure_has_zero_first_variation_at_closed_background(self):
        dp = model.tangent_basis(self.p)[0]
        dm = np.array([[0.2, 0.1j], [-0.1j, -0.1]])
        jets = model.closed_jets(self.m, self.p, dm, dp)
        self.assertClose(jets["Lambda_first"], 0)
        self.assertGreater(np.linalg.norm(jets["Lambda_quadratic_coefficient"]), 0)

    def test_closure_quadratic_coefficient_matches_exact_nonlinear_function(self):
        dp = model.tangent_basis(self.p)[0]+0.3*model.tangent_basis(self.p)[1]
        x = -1j*(dp @ self.p-self.p @ dp)
        dm = np.array([[0.2, 0.1j], [-0.1j, -0.1]])
        expected = model.closed_jets(self.m, self.p, dm, dp)["Lambda_quadratic_coefficient"]
        errors = []
        for e in (0.01, 0.005):
            p = model.projector_path(self.p, x, e)
            result = model.phase.minimal_native_closure(self.m+e*dm, p)/e**2
            errors.append(np.linalg.norm(result-expected))
        self.assertGreater(errors[0]/errors[1], 1.9)
        self.assertLess(errors[1], 0.01)

    def test_fixed_gapped_M_excludes_all_projector_tangents_under_hard_closure(self):
        tangents = model.tangent_basis(self.p)
        gram = np.array([[np.vdot(self.m @ a-a @ self.m, self.m @ b-b @ self.m).real
                          for b in tangents] for a in tangents])
        self.assertEqual(np.linalg.matrix_rank(gram), 2)
        self.assertClose(np.linalg.eigvalsh(gram), [0.9**2, 0.9**2])

    def test_cross_block_degeneracies_retain_some_hard_closure_tangents(self):
        p, m = np.diag([1, 0, 0]), np.diag([0.4, 1.3, 0.4])
        tangents = model.tangent_basis(p)
        gram = np.array([[np.vdot(m @ a-a @ m, m @ b-b @ m).real
                          for b in tangents] for a in tangents])
        self.assertEqual(len(tangents)-np.linalg.matrix_rank(gram), 2)

    def test_joint_unitary_variation_preserves_linearized_closure(self):
        x = np.array([[0.1, 1-0.3j], [1+0.3j, -0.2]])
        dp, dm = 1j*(x @ self.p-self.p @ x), 1j*(x @ self.m-self.m @ x)
        jets = model.closed_jets(self.m, self.p, dm, dp)
        self.assertClose(jets["commutator_first"], 0)
        self.assertClose(jets["residue_first"], 0)
        self.assertClose(jets["Lambda_quadratic_coefficient"], 0)

    def test_independent_H_penalty_has_no_quadratic_H_projector_mixing(self):
        dp = model.tangent_basis(self.p)[0]
        h = np.diag([0.2, 0.3])
        x = -1j*(dp @ self.p-self.p @ dp)
        errors = []
        for e in (0.02, 0.01):
            p = model.projector_path(self.p, x, e)
            target = model.phase.minimal_native_closure(self.m, p)
            quotient = np.vdot(e*h-target, e*h-target).real/e**2
            errors.append(abs(quotient-np.vdot(h, h).real))
        self.assertGreater(errors[0]/errors[1], 1.9)

    def test_hard_H_is_second_order_and_cannot_be_counted_as_a_first_order_field(self):
        dp = model.tangent_basis(self.p)[0]
        x = -1j*(dp @ self.p-self.p @ dp)
        h = [model.phase.minimal_native_closure(self.m, model.projector_path(self.p, x, e))
             for e in (0.02, 0.01)]
        self.assertGreater(np.linalg.norm(h[0])/np.linalg.norm(h[1]), 3.99)
        self.assertLess(np.linalg.norm(h[0])/np.linalg.norm(h[1]), 4.01)

    def test_positive_H_at_zero_does_not_have_a_two_sided_Hermitian_tangent_space(self):
        h = np.diag([0.2, 0.4])
        self.assertGreater(np.linalg.eigvalsh(h)[0], 0)
        self.assertLess(np.linalg.eigvalsh(-h)[0], 0)
        self.assertTrue(self.report["native_gaussian_jets"]["positive_H_at_zero_is_a_cone_boundary_not_an_unconstrained_Hermitian_Gaussian"])

    def test_hessian_is_hermitian_and_nonnegative_in_the_declared_comparison(self):
        self.assertClose(self.data["H"], self.data["H"].conj().T)
        self.assertGreater(np.linalg.eigvalsh(self.data["H"])[0], 0)

    def test_full_constant_background_gauge_directions_are_null_before_gauge_fixing(self):
        d = model.symbol(self.k, self.p, gauge_fix=None)
        self.assertClose(d["F_map"] @ d["gauge_directions"], 0)
        self.assertClose(d["X_map"] @ d["gauge_directions"], 0)
        self.assertClose(d["H"] @ d["gauge_directions"], 0)

    def test_dropping_the_lower_derivative_background_loses_the_gauge_identity(self):
        d = model.symbol(self.k, self.p, gauge_fix=None, principal_only=True)
        self.assertGreater(np.linalg.norm(d["X_map"] @ d["gauge_directions"]), 0.1)

    def test_faddeev_popov_operator_is_the_actual_gauge_condition_variation(self):
        self.assertClose(self.data["gauge_map"] @ self.data["gauge_directions"], self.data["ghost"])
        self.assertClose(self.data["ghost"], (self.k @ self.k)*np.eye(4))

    def test_generic_full_and_principal_ranks_differ(self):
        principal = model.symbol(self.k, self.p, principal_only=True)
        self.assertEqual(np.linalg.matrix_rank(self.data["H"], tol=1e-10), 22)
        self.assertEqual(np.linalg.matrix_rank(principal["H"], tol=1e-10), 20)

    def test_parallel_momentum_has_projector_null_directions_even_after_gauge_fixing(self):
        for zeta in (0.2, 1, 4):
            d = model.symbol([3, 0, 0, 0], self.p, gauge_fix=zeta)
            self.assertEqual(np.linalg.matrix_rank(d["H"], tol=1e-10), 20)
            self.assertClose(d["H"][:, 20:], 0)

    def test_no_matching_penalty_leaves_the_H_projector_redundancy(self):
        d = model.symbol(self.k, self.p, penalty=0)
        self.assertEqual(np.linalg.matrix_rank(d["H"], tol=1e-10), 20)

    def test_zero_eta_leaves_projector_tangents_absent_from_this_quadratic_curvature(self):
        d = model.symbol(self.k, self.p, eta=0)
        self.assertClose(d["H"][:, 20:], 0)

    def test_tangent_H_and_projector_principal_combination_is_exactly_kappa_H_minus_eta_pi(self):
        d = model.symbol(self.k, self.p, principal_only=True)
        vector = np.zeros(22, complex)
        pi = np.array([0.3, -0.4])
        vector[16:20] = d["eta"]*(d["tangent_embedding"] @ pi)
        vector[20:] = d["kappa"]*pi
        self.assertClose(d["H"] @ vector, 0)

    def test_central_H_eigenvalue_has_no_parallel_momentum_growth(self):
        for momentum in (1, 10, 1000):
            d = model.symbol([momentum, 0, 0, 0], self.p)
            vector = np.zeros(22, complex)
            vector[16:18] = 1/np.sqrt(2)
            self.assertClose(d["H"] @ vector, 2*d["penalty"]*vector)

    def test_central_H_generic_eigenvalue_has_the_axis_wedge_factor(self):
        vector = np.zeros(22, complex)
        vector[16:18] = 1/np.sqrt(2)
        value = self.data["kappa"]**2*self.data["axis_wedge_square"]+2*self.data["penalty"]
        self.assertClose(self.data["H"] @ vector, value*vector)

    def test_missing_parallel_derivative_produces_a_growing_regulated_heat_sum(self):
        s = 0.2
        counts = [sum(np.exp(-s*2*1.2) for _ in range(-cutoff, cutoff+1)) for cutoff in (10, 20, 40)]
        self.assertGreater(counts[2]/counts[1], 1.9)
        self.assertGreater(counts[1]/counts[0], 1.9)

    def test_hessian_spectrum_is_covariant_under_internal_unitary_coordinates(self):
        z = self.rng.normal(size=(2, 2))+1j*self.rng.normal(size=(2, 2))
        u, _ = np.linalg.qr(z)
        changed = model.symbol(self.k, u @ self.p @ u.conj().T)
        self.assertClose(np.linalg.eigvalsh(changed["H"]), np.linalg.eigvalsh(self.data["H"]))

    def test_larger_finite_carrier_has_expected_tangent_and_hessian_dimensions(self):
        p = np.diag([1, 0, 0])
        d = model.symbol(self.k, p)
        principal = model.symbol(self.k, p, principal_only=True)
        self.assertEqual(d["H"].shape, (49, 49))
        self.assertEqual(np.linalg.matrix_rank(d["H"], tol=1e-10), 49)
        self.assertEqual(np.linalg.matrix_rank(principal["H"], tol=1e-10), 45)

    def test_frechet_projector_jet_handles_noncommuting_generator_derivatives(self):
        x, dx = model.hermitian_basis(2)[2:]
        e, step = 0.2, 1e-5
        p, dp = model._projector_jet(self.p, x, np.repeat(dx[None], 4, axis=0), e)
        difference = (model.projector_path(self.p, x+step*dx, e)
                      -model.projector_path(self.p, x-step*dx, e))/(2*step)
        self.assertClose(dp[0], difference)
        self.assertClose(p @ dp+dp @ p, dp)

    def test_independent_nonlinear_action_converges_to_the_quadratic_symbol(self):
        d = self.report["example"]["independent_finite_action"]
        errors = d["absolute_errors"]
        self.assertGreater(errors[0]/errors[1], 3.99)
        self.assertGreater(errors[1]/errors[2], 3.99)
        self.assertLess(errors[-1], 2.2e-5)

    def test_projector_H_subblock_schur_reduction_is_not_two_scalar_propagators(self):
        kappa, eta, mass = 0.4, 0.7, 2.4
        for q in (1, 10, 1000):
            block = np.array([[kappa*kappa*q+mass, -kappa*eta*q],
                              [-kappa*eta*q, eta*eta*q]])
            self.assertClose(np.linalg.det(block), mass*eta*eta*q)
            reduced = block[1, 1]-block[1, 0]*block[0, 1]/block[0, 0]
            self.assertClose(reduced, eta*eta*q*mass/(kappa*kappa*q+mass))

    def test_free_Feynman_maxwell_block_is_laplacian_not_four_physical_bosons(self):
        d = model.symbol(self.k, self.p, eta=0, kappa=0)
        self.assertClose(d["H"][:16, :16], (self.k @ self.k)*np.eye(16))
        self.assertEqual(4-2, 2)

    def test_massless_Maxwell_ghost_control_cancels_vacuum_but_has_negative_Einstein_sign(self):
        d = model.maxwell_dirac_control()
        i = model.heat.proper_time_integral(0, 20, 2, 2)
        self.assertEqual(d["vacuum_weight"], 0)
        self.assertEqual(d["rho"], 0)
        self.assertClose(d["A"], -i/(32*np.pi**2))

    def test_single_Maxwell_curvature_coefficient_includes_ghosts(self):
        d = model.maxwell_dirac_control(0, 1)
        self.assertEqual(d["vacuum_weight"], -2)
        self.assertClose(d["curvature_weight"], -2/3)

    def test_Maxwell_and_Dirac_control_has_correct_mass_dimensions(self):
        a = model.maxwell_dirac_control(1, 1, 20, 2)
        b = model.maxwell_dirac_control(1, 1, 60, 6)
        self.assertClose(b["A"], 9*a["A"])
        self.assertClose(b["rho"], 81*a["rho"])

    def test_invalid_projector_or_closed_jets_are_rejected(self):
        for p in ([[0.5, 0], [0, 0]], [[1, 1], [0, 0]]):
            with self.assertRaises(ValueError):
                model.tangent_basis(p)
        with self.assertRaises(ValueError):
            model.closed_jets([[0, 1], [1, 0]], self.p, np.zeros((2, 2)), np.zeros((2, 2)))
        with self.assertRaises(ValueError):
            model.closed_jets(self.m, self.p, np.zeros((2, 2)), np.eye(2))

    def test_invalid_symbol_parameters_are_rejected(self):
        for kwargs in ({"axis": [0]*4}, {"gauge_fix": 0}, {"gauge_fix": -1}, {"penalty": -1}):
            with self.subTest(kwargs=kwargs), self.assertRaises(ValueError):
                model.symbol(self.k, self.p, **kwargs)
        with self.assertRaises(ValueError):
            model.symbol([0]*4, self.p)

    def test_no_native_quantization_or_main_TeX_change_is_claimed(self):
        self.assertIn("NOT native quantization", self.report["status"])
        self.assertFalse(self.report["main_TeX_changed"])
        self.assertTrue(self.report["quadratic_dictionary"]["no_valid_native_heat_trace_or_physical_mode_count_follows"])
        self.assertIn("NOT a justified continuation", self.report["comparison_assumptions"][1])

    def test_native_closed_system_anchors_remain_inspectable(self):
        text = (ROOT / "sources/research/parts/v470/10_sphaera_and_physics.tex").read_text(encoding="utf-8")
        for label in ("thm:variational-form", "prop:equivalent-closure-criteria", "thm:closed-master-system"):
            self.assertIn("\\label{"+label+"}", text)

    def test_report_reproduces_saved_results(self):
        saved = json.loads((ROOT / "analysis/HC_Closure_Fluctuation_Hessian.json").read_text(encoding="utf-8"))
        self.assertEqual(self.report, saved)


if __name__ == "__main__":
    unittest.main()
