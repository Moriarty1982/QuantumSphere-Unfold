"""Focused independent-coframe FE2 checks, including actual Cartan fields."""
import importlib.util
from pathlib import Path
import unittest

import numpy as np


ROOT = Path(__file__).resolve().parents[3]
SPEC = importlib.util.spec_from_file_location(
    "second_gravity_affine", ROOT / "analysis/HC_Cartan_Second_Gravity_Affine.py")
model = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(model)


def hessian(function, step):
    origin, axes = function(np.zeros(4)), np.eye(4)
    result = np.empty((4, 4)+origin.shape)
    for r, s in model.prior.PAIR2:
        a, b = axes[r], axes[s]
        if r == s:
            value = (function(step*a)-2*origin+function(-step*a))/step**2
        else:
            value = (function(step*(a+b))-function(step*(a-b))
                     -function(step*(-a+b))+function(-step*(a+b)))/(4*step**2)
        result[r, s] = result[s, r] = value
    return result


def polynomial_euler(prepared, point, jets, connection, x, e4=None, l3=None):
    """Independent coframe_euler on polynomial E,psi,lambda and omega jets.

    omega and its first jet are evaluated exactly as polynomials, avoiding
    differences inside curvature and avoiding the analytic FE2 expression.
    """
    w0, w1, w2, w3 = (connection[k] for k in ("omega", "first", "second", "third"))
    omega = (w0+np.einsum("r,rmab->mab", x, w1)
             +np.einsum("r,s,rsmab->mab", x, x, w2)/2
             +np.einsum("r,s,t,rstmab->mab", x, x, x, w3)/6)
    dw = (w1+np.einsum("s,rsmab->rmab", x, w2)
          +np.einsum("s,t,rstmab->rmab", x, x, w3)/2)
    e = (np.eye(4)+np.einsum("r,s,rsam->am", x, x, point["coframe_second"])/2
         +np.einsum("r,s,t,rstam->am", x, x, x, jets["e3"])/6)
    psi = (prepared["data"]["psi"]+np.einsum("r,ruj->uj", x, point["psi_first"])
           +np.einsum("r,s,rsuj->uj", x, x, jets["p2"])/2
           +np.einsum("r,s,t,rstuj->uj", x, x, x, jets["p3"])/6)
    dp = (point["psi_first"]+np.einsum("s,rsuj->ruj", x, jets["p2"])
          +np.einsum("s,t,rstuj->ruj", x, x, jets["p3"])/2)
    lam = (point["multiplier"]+np.einsum("r,ram->am", x, point["multiplier_first"])
           +np.einsum("r,s,rsam->am", x, x, jets["l2"])/2)
    if e4 is not None:
        e += model.third.diagnostic.homogeneous_jet(e4, 4, x)
    if l3 is not None:
        lam += model.third.diagnostic.homogeneous_jet(l3, 3, x)
    return model.cartan.coframe_euler(e, psi, dp, omega,
        model.cartan.curvature_upper(omega, dw), model.scalar.MASS, lam)


class HCCartanSecondGravityAffineTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.prepared, cls.point, cls.jets, _ = model.third.diagnostic.load_data()
        cls.lc = model.third.lc_cubic(cls.prepared, cls.point)
        cls.connection = model.third.connection_third(cls.prepared, cls.point, cls.jets, cls.lc)

    def test_full_polynomial_coframe_euler_with_new_highest_jets(self):
        rng = np.random.default_rng(652)
        e4, l3 = rng.normal(size=(35, 4, 4))*.3, rng.normal(size=(20, 4, 4))*.3
        connection = dict(self.connection, third=self.connection["third"]
                          +model.highest_delta_omega3(self.prepared, e4, l3))
        analytic = model.coframe_euler_second(self.prepared, self.point, self.jets,
                                             e4=e4, l3=l3, lc_third=self.lc)
        self.assertEqual(analytic.shape, (4, 4, 4, 4))
        self.assertTrue(np.isrealobj(analytic))
        np.testing.assert_allclose(analytic, analytic.swapaxes(0, 1), atol=2e-9, rtol=1e-12)
        function = lambda x: polynomial_euler(self.prepared, self.point, self.jets, connection, x, e4, l3)
        coarse, fine = hessian(function, 2e-4), hessian(function, 1e-4)
        error = np.linalg.norm((4*fine-coarse)/3-analytic)
        print("\npolynomial FE2 Richardson error:", error)
        self.assertLess(np.linalg.norm(fine-analytic), .4*np.linalg.norm(coarse-analytic))
        np.testing.assert_allclose((4*fine-coarse)/3, analytic, atol=5e-5, rtol=1e-7)
        np.testing.assert_allclose(analytic, model.coframe_euler_second(
            self.prepared, self.point, self.jets, omega3=connection["third"]), atol=0, rtol=0)

    def test_independent_frame_response_includes_E2_curvature(self):
        rng = np.random.default_rng(923)
        delta = rng.normal(size=(4, 4))*.4
        w = model.cartan.unpack(rng.normal(size=24))
        dw = np.array([model.cartan.unpack(rng.normal(size=24)) for _ in range(4)])
        curvature = model.cartan.curvature_upper(w, dw)
        psi = rng.normal(size=(3, 4))+1j*rng.normal(size=(3, 4))
        dp = rng.normal(size=(4, 3, 4))+1j*rng.normal(size=(4, 3, 4))
        for spinor, first in ((psi, dp), (np.zeros_like(psi), np.zeros_like(dp))):
            cross = model.scalar.odd.readouts.pairing(
                spinor, model.cartan.covariant_jet(spinor, first, w)).imag
            mass = np.vdot(spinor, model.scalar.MASS @ spinor @ model.scalar.BETA.T).real
            expected = model.normal_frame_response(delta, cross, mass, curvature)
            def field(t):
                return model.cartan.coframe_euler(np.eye(4)+t*delta, spinor, first,
                    w, curvature, model.scalar.MASS, np.zeros((4, 4)))
            numeric = (field(1e-5)-field(-1e-5))/(2e-5)
            np.testing.assert_allclose(expected, numeric, atol=2e-7, rtol=1e-8)
            self.assertGreater(np.linalg.norm(expected), 1.)
        # Pure gravity response is nonzero even when curvature2 is zero.
        self.assertGreater(np.linalg.norm(model.normal_frame_response(
            self.point["coframe_second"][0, 0], np.zeros((4, 4)), 0., curvature)), 1.)

    def test_affine_in_old_and_new_coordinates_with_p2_fixed(self):
        rng = np.random.default_rng(762)
        def evaluate(x):
            jets = dict(self.jets, l2=model.prior.unpack_second(x[:160]),
                        e3=model.prolong.unpack_third(x[160:480]),
                        p3=model.prolong.unpack_third(x[480:960], True))
            return model.coframe_euler_second(self.prepared, self.point, jets,
                e4=x[960:1520].reshape(35, 4, 4), l3=x[1520:].reshape(20, 4, 4), lc_third=self.lc)
        x, y = rng.normal(size=(2, 1840))*.2
        base = evaluate(np.zeros(1840))
        np.testing.assert_allclose(evaluate(.7*x-1.2*y),
            base+.7*(evaluate(x)-base)-1.2*(evaluate(y)-base), atol=3e-9, rtol=2e-11)

    def test_curvature_hessian_against_polynomial_connection(self):
        c = self.connection
        def field(x):
            w = (c["omega"]+np.einsum("r,rmab->mab", x, c["first"])
                 +np.einsum("r,s,rsmab->mab", x, x, c["second"])/2
                 +np.einsum("r,s,t,rstmab->mab", x, x, x, c["third"])/6)
            dw = (c["first"]+np.einsum("s,rsmab->rmab", x, c["second"])
                  +np.einsum("s,t,rstmab->rmab", x, x, c["third"])/2)
            return model.cartan.curvature_upper(w, dw)
        analytic = model.curvature_second(c["omega"], c["first"], c["second"], c["third"])
        coarse, fine = hessian(field, 2e-4), hessian(field, 1e-4)
        np.testing.assert_allclose((4*fine-coarse)/3, analytic, atol=3e-5, rtol=1e-7)

    def test_actual_cartan_fields_nested_difference_convergence(self):
        analytic = model.coframe_euler_second(self.prepared, self.point, self.jets, lc_third=self.lc)
        function = lambda x: model.regular.field_euler(self.prepared, self.point, self.jets, x)
        errors, tensors = [], []
        for step in (1e-3, 5e-4):
            tensors.append(hessian(function, step))
            error = np.linalg.norm(tensors[-1]-analytic)
            errors.append(error)
            print("\nactual Cartan FE2 nested-FD step/error:", step, error)
        self.assertLess(errors[1], .6*errors[0])
        extrapolated_error = np.linalg.norm((4*tensors[1]-tensors[0])/3-analytic)
        print("\nactual Cartan FE2 nested-FD Richardson error:", extrapolated_error)
        self.assertLess(extrapolated_error, .1)

    def test_override_rejects_ambiguous_highest_jets(self):
        with self.assertRaises(ValueError):
            model.coframe_euler_second(self.prepared, self.point, self.jets,
                omega3=self.connection["third"], e4=np.zeros((35, 4, 4)))
        with self.assertRaises(ValueError):
            model.highest_delta_omega3(self.prepared, e4=np.zeros(560))


if __name__ == "__main__":
    unittest.main()
