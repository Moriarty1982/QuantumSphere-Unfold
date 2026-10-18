"""Focused analytic R2 controls; no extension or rank solve."""
import importlib.util
import json
from pathlib import Path
import unittest

import numpy as np


ROOT = Path(__file__).resolve().parents[3]
SPEC = importlib.util.spec_from_file_location(
    "cartan_second_probe_affine", ROOT / "analysis/HC_Cartan_Second_Probe_Affine.py")
model = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(model)
SPEC = importlib.util.spec_from_file_location(
    "second_probe_difference_control", ROOT / "analysis/HC_Cartan_Second_Probe_Diagnostic.py")
diagnostic = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(diagnostic)


def actual_probe(prepared, point, jets, l3, x):
    """Evaluate displaced polynomial fields and solve Cartan anew, including lambda3."""
    fields = model.regular.taylor_fields(prepared, point, jets, x)
    e, de, psi, dp = (fields[k] for k in ("coframe", "coframe_first", "psi", "psi_first"))
    lam = fields["multiplier"]+np.einsum("r,s,t,rstam->am", x, x, x, l3)/6
    dl = (point["multiplier_first"]+np.einsum("s,rsam->ram", x, jets["l2"])
          +np.einsum("s,t,rstam->ram", x, x, l3)/2)
    h, response, source = model.prolong.fast_cartan_data(prepared, e, psi)
    omega = fields["bundle"]["omega"]+model.cartan.unpack(
        np.linalg.solve(h, -source+response.T @ lam.reshape(16)))
    inverse, volume = np.linalg.inv(e), abs(np.linalg.det(e))
    di = np.array([-inverse @ d @ inverse for d in de])
    dv = volume*np.einsum("ma,ram->r", inverse, de)
    dw = (np.einsum("r,ma,aij->rmij", dv, inverse, model.prolong.FLAT_WEIGHTS)
          +volume*np.einsum("rma,aij->rmij", di, model.prolong.FLAT_WEIGHTS)
          +np.einsum("ram,aij->rmij", dl, model.prolong.Q_WEIGHTS))
    b = np.array([np.kron(np.eye(3), s) for s in model.prolong.spin_lift(omega)])
    return model.scalar.odd.real_law.real_operator(
        psi.reshape(12), dp.reshape(4, 12), model.cartan.kinetic_weights(e, lam), b,
        volume*model.prior.MASS_WEIGHT, np.einsum("mmij->ij", dw))["symmetric"]


class HCCartanSecondProbeAffineTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.prepared, cls.point, cls.jets, _ = diagnostic.load_data()

    def test_frozen_diagnostic_full_complex_tensor(self):
        saved = json.loads((ROOT / "analysis/HC_Cartan_Second_Probe_Diagnostic.json").read_text())
        tensor = saved["result"]["R2"]
        expected = np.array(tensor["real"])+1j*np.array(tensor["imag"])
        actual = model.probe_second(self.prepared, self.point, self.jets)
        self.assertEqual(actual.shape, (4, 4, 12))
        np.testing.assert_allclose(actual, actual.swapaxes(0, 1), atol=2e-10, rtol=1e-12)
        np.testing.assert_allclose(actual, expected, atol=2e-6, rtol=2e-8)

    def test_actual_fields_with_nonzero_lambda3(self):
        rng = np.random.default_rng(1823)
        l3 = model.prolong.unpack_third(rng.normal(size=320)*.4)
        jets = dict(self.jets)
        jets["l2"] = model.prior.unpack_second(rng.normal(size=160)*.2)
        jets["e3"] = model.prolong.unpack_third(rng.normal(size=320)*.2)
        jets["p3"] = model.prolong.unpack_third(rng.normal(size=480)*.2, True)
        analytic = model.probe_second(self.prepared, self.point, jets, l3)
        function = lambda x: actual_probe(self.prepared, self.point, jets, l3, x)
        coarse = diagnostic.second_difference(function, 2e-4)
        fine = diagnostic.second_difference(function, 1e-4)
        extrapolated = diagnostic.richardson(coarse, fine)
        self.assertLess(np.linalg.norm(fine-analytic), .4*np.linalg.norm(coarse-analytic))
        np.testing.assert_allclose(extrapolated, analytic, atol=3e-5, rtol=1e-7)

    def test_affine_in_all_allowed_variable_blocks_with_p2_fixed(self):
        rng = np.random.default_rng(203)

        def evaluate(x):
            jets = dict(self.jets, l2=model.prior.unpack_second(x[:160]),
                        e3=model.prolong.unpack_third(x[160:480]),
                        p3=model.prolong.unpack_third(x[480:960], True))
            return model.probe_second(self.prepared, self.point, jets, x[960:])

        x, y = rng.normal(size=(2, 1280))*.3
        base = evaluate(np.zeros(1280))
        np.testing.assert_allclose(evaluate(1.7*x-.4*y),
                                   base+1.7*(evaluate(x)-base)-.4*(evaluate(y)-base),
                                   atol=2e-10, rtol=2e-12)

    def test_lambda3_packing_and_exact_principal_term(self):
        packed = np.random.default_rng(83).normal(size=320)
        full = model.prolong.unpack_third(packed)
        base = model.probe_second(self.prepared, self.point, self.jets)
        actual = model.probe_second(self.prepared, self.point, self.jets, packed)
        np.testing.assert_allclose(actual, model.probe_second(
            self.prepared, self.point, self.jets, full), atol=0, rtol=0)
        expected = .5j*np.einsum("rsmam,aij,j->rsi", full,
                                 model.prolong.Q_WEIGHTS,
                                 self.prepared["data"]["psi"].reshape(12))
        np.testing.assert_allclose(actual-base, expected, atol=2e-10, rtol=1e-11)
        for invalid in (np.zeros(319), np.full(320, np.nan), np.ones(320, complex)):
            with self.assertRaises(ValueError):
                model.probe_second(self.prepared, self.point, self.jets, invalid)

    def test_twice_differentiated_next_scalar_identity(self):
        prepared, point, jets = self.prepared, self.point, self.jets
        origin = model.regular.taylor_fields(prepared, point, jets, np.zeros(4))
        first = model.spatial.first_probe(prepared, point, jets["p2"], jets["l2"])
        second = model.probe_second(prepared, point, jets)
        c2 = model.regular.equations(prepared, point, jets)["constraint_second"]
        a2 = model.scalar.scalar_jet(prepared, point, jets)["hessian"]
        p, p1, p2 = (prepared["data"]["psi"].reshape(12),
                     point["psi_first"].reshape(4, 12), jets["p2"].reshape(4, 4, 12))
        q = model.scalar.Q_FULL
        errors = np.empty((4, 4))
        for r, s in np.ndindex(4, 4):
            probe = (np.vdot(p2[r, s], q @ origin["probe"])
                     +np.vdot(p1[r], q @ first[s])+np.vdot(p1[s], q @ first[r])
                     +np.vdot(p, q @ second[r, s])).real
            g2 = np.trace(point["coframe_second"][r, s])*np.eye(4)-point["coframe_second"][r, s].T
            errors[r, s] = a2[r, s]+probe+np.trace(c2[r, s])+np.sum(g2*origin["constraint"])
        np.testing.assert_allclose(errors, 0, atol=2e-9, rtol=0)


if __name__ == "__main__":
    unittest.main()
