# Recursive OP5 calibration: construction and fourth-order test

30 October 2026. Numerical finite-jet research on the declared comparison, not a native physical identification or a regional existence theorem.

## Construction rule

Store coefficients c_alpha=(partial^alpha Psi)/alpha!, with multiindex factorial (not total-degree factorial). Use ordinary truncated convolution for products, the derivative weight alpha_mu+1, and a finite Neumann series for the inverse coframe. All connection/coupling derivatives required at the tested order are symbolically evaluated from the original background. At field-jet order p, evaluate the full nonlinear residual F through derivative order p-1.

The highest field jets enter linearly: A_p z_p+b_p(J_lower)=0. Their complete left kernel L_p produces the compatibility conditions L_p b_p=0. The calibrator varies all lower field jets of degrees2..p-1, while protecting the residual coefficients of all previous orders in the same objective. Field values, first jets, backgrounds and couplings stay fixed. Highest jets are eliminated before optimization and recovered afterward; the full unprojected residual is re-evaluated and reported by order. No constant time-coframe derivative is imposed.

This is a bounded damped minimum-norm search, with maximum steps, acceptance checks and a large-coefficient guard. It prefers small increments but does not prove the smallest possible correction or force roots to exist. Previous levels may be warm-started from recursive-order-(p-1)-result.json when present; all actually used files are fingerprinted. The code uses arbitrary-order multiindex indexing, but the new generic implementation has been executed and independently checked only through field-jet order4. No guarantee for every later level is claimed. The present implementation releases the entire allowed lower window, not an automatically proven minimal subset.

## Fourth-order experiment

Three previous successful third-order germs serve as initial data. Their frozen fourth-order completion fails: minimum residuals of normalized degree3 coefficients are53.5428,52.7698,53.0532. An independent scalar d³g gate also fails for those frozen data. The calibrator then releases degrees2 and3 and recovers degree4. Values and first jets remain identical to the preceding solution.

The degree4 operator is480x840, numerical rank424, leaving56 left compatibility rows. Each point converges in five accepted steps. Rank and recovered residual are stable for relative SVD cutoffs1e-8,1e-9,1e-11; the last retained singular value is about0.68 and the next about8e-14 in this packing.

| point | full F | full dF | full d²F | full d³F |
|---|---:|---:|---:|---:|
| centre | 3.06e-14 | 3.93e-14 | 2.35e-13 | 6.37e-12 |
| edge | 2.03e-15 | 2.85e-14 | 2.46e-13 | 5.44e-12 |
| inner | 2.64e-15 | 3.75e-14 | 2.34e-13 | 6.51e-12 |

These are norms of independent symmetric raw derivative entries, recovered by multiplying normalized coefficients by their multiindex factorial. The optimization and frozen-source comparisons use normalized coefficient norms; these two conventions are separately stored and must not be mixed.

The corresponding raw field-jet norms for degrees2/3/4 are approximately26/89/900. More precisely degree4 norms are903.44,887.77,913.33. This is not a physical length or energy scale. No convergence conclusion follows from three unscaled jet norms or from the success of this fit. Coordinate/radius normalization and a uniform growth bound remain separate obligations.

## Verification

An independently implemented NumPy univariate formal series restricts the multivariate result to six directions at each point. It uses a recurrence inverse instead of the optimizer's Neumann expansion and the original exact background derivatives. Residual coefficients through degree3 agree within4e-13. Sampled highest-operator columns agree within9e-14. Both multiplication orders for the inverse, the scalar constraint coefficients and the factorial convention are checked separately. Directional checks are finite implementation checks; they do not certify all roots or a theorem.

Earlier tests and independent product-rule verification of second/third-order results are preserved alongside the new result. All successful and failed lower-data controls remain in the archive. Scripts, coefficients, source/input hashes, software versions and stopping histories are retained. No fifth-order computation is included in this checkpoint.

## Meaning and boundary

The fitting rule can repair finite compatibility obstructions by revisiting lower derivatives rather than treating each fitted level as permanently fixed. It has now produced numerical full fourth-order field jets at all three points, with F,dF,d²F,d³F near numerical zero. It does not show that all levels can be made compatible simultaneously, that lower coefficients stabilize when higher orders are added, that the Taylor series converges, or that one regional solution passes through all three germs. It also does not derive a native common action, physical predictions or OP5 closure.

Next discriminating work: test the next order with the same algorithm while monitoring movement of every earlier coefficient; normalize the expansion radius and seek a uniform majorant/stability argument. A finite fit alone cannot decide the core theorem.

## Reproduction

Python with NumPy, SymPy and PyTorch. Run from the repository root:

`python analysis/op5-field-slices/state-sufficiency-2026-10-30/recursive_calibrator.py --order 4 --points 0 1 2`

The script writes result sidecars in its own directory. To preserve an archived result, copy this artifact directory to a separate location and run from the repository root. The original background model is read from analysis/OP5_Counterflow_Full_Residual_Check.py. Prior local experimental scripts and input snapshots are historical provenance; the new recursive calibrator discovers the repository rather than requiring the author's machine path.
