# Frozen Second Probe Diagnostic

This bounded sidecar evaluates the full complex probe Hessian
`R2[r,s,k] = partial_r partial_s R[k]` on a frozen Taylor truncation.
It is not an actual extension calculation, and finite differences are not proof.

## Inputs and Truncation

The module imports `HC_Cartan_Next_Scalar_Compatibility.py` through `importlib`,
loads the fixed lower point with its `regular.load_data()`, and unpacks the
strongest saved `joint_394_system.jet_coordinates` from
`HC_Cartan_Next_Scalar_Compatibility.json`. It does not run the joint solver.
The saved `p2`, `l2`, `e3`, and `p3` are all retained. No couplings are fitted.
The JSON report includes the original fixed lower point and couplings, jet
norms, and SHA-256 hashes of the loaded local Python dependency graph and
consumed JSON inputs. Python line endings are normalized to LF before hashing.

The existing `spatial.taylor_fields` evaluates cubic psi, quadratic multiplier,
and cubic coframe fields. All NEW higher derivatives are zero, including
`lambda3`; the previously fixed `p3` and `e3` are not zeroed. At every displaced
point the evaluator recomputes the full algebraically eliminated Cartan
connection, including the source and multiplier reaction, and evaluates the
complete variable-weight real probe, including its defect term. The resulting
connection and probe are not themselves polynomial truncations.

## Numerical Result

All four diagonal and six mixed derivative pairs are evaluated using central
second differences. The diagonal stencil is
`(R(h*a)-2*R(0)+R(-h*a))/h^2`; the mixed stencil is
`(R(h*(a+b))-R(h*(a-b))-R(h*(-a+b))+R(-h*(a+b)))/(4*h^2)`.
Richardson extrapolation is `(4*D(h/2)-D(h))/3`.

| Finest step h | Central R2 norm | Successive central change | Richardson R2 norm | Successive Richardson change |
| --- | --- | --- | --- | --- |
| 1e-3 | 10453.39080514 | - | - | - |
| 5e-4 | 10453.21996595 | 0.61504701 | 10453.16302697 | - |
| 2.5e-4 | 10453.17726165 | 0.15375879 | 10453.16302735 | 1.42780e-5 |
| 1.25e-4 | 10453.16658641 | 0.03843947 | 10453.16302803 | 3.58008e-6 |

Central change ratios are 4.000077 and 4.000023, consistent with the expected
second-order truncation error. The last Richardson relative change is
3.42488e-10. The bounded refinement stops when that tensor change is at most
`1e-6 + 1e-9 * ||R2_Richardson||`, with at most nine levels. It always includes
the three requested initial steps. The largest absolute complex component is
1977.16597905, at zero-based index `[0,0,3]`.
The norm counts the full symmetric tensor, so mixed pairs occur twice.

Richardson changes do not demonstrate fourth-order asymptotics here: their last
ratio is about 3.99, not 16. A stricter exploratory refinement encountered a
numerical cancellation floor as steps shrank. Smaller steps need not improve
the answer. The stored `change/15` indicator is conditional on fourth-order
asymptotics and is not an error bound; the observed tensor changes are the
direct stability evidence.

At the origin, the full probe norm is 8.22e-15, the Cartan residual norm is
1.52e-16, the scalar Hessian norm is 1.22e-11, and the saved full 394-equation
residual norm is 7.04e-11. Thus the already solved scalar Hessian condition
does not force full `R2=0`; this frozen truncation has a numerically nonzero
full second probe derivative.

## Scope

`R` is first order in psi and multiplier, and depends on omega, whose coframe
dependence is first order. Consequently `R2` uses `psi3`, `lambda3`, and
`coframe3`, not only second derivatives. Variations of `p3`, `l3`, and `e3`
can affect `R2`. However, the old `p3` and `e3` are already fixed by the saved
jet used here; varying them requires rechecking the prior 394 conditions.
`l3` is a new freedom, set to zero in this diagnostic. No freedom is searched
and no compatibility or rank system for these variations is constructed.

The nonzero result therefore makes no impossibility claim about extension.
No full second-probe/gravity or third-constraint extension is solved, and
no propagation, convergence of a formal solution, or local-existence theorem
follows from this finite-difference calculation.

## Reproduction

From the repository root:

```text
python -B analysis/HC_Cartan_Second_Probe_Diagnostic.py --output analysis/HC_Cartan_Second_Probe_Diagnostic.json
python -B -m unittest scripts.qsc_audit.tests.test_hc_cartan_second_probe_diagnostic -v
```

The focused tests cover complex vector polynomial diagonal/mixed stencils,
quartic Richardson cancellation, input validation, normalized source hashes,
the fixed inputs, tensor symmetry, saved-level reproduction, and the distinction
between the scalar gate and frozen full probe Hessian. Numerical reproduction
uses componentwise `rtol=2e-7, atol=2e-4` to allow cancellation and linear-algebra
variation across platforms. No full audit suite is required.
