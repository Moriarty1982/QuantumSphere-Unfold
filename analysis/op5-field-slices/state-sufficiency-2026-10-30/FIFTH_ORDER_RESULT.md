# Fifth-order OP5 calibration and lower-data stability

30 October 2026, repository baseline f0f2b9e539ea3fb6823e93fdae1df43bbaf082f4. Original comparison model and generic calibrator unchanged. Research data are saved locally; this turn does not commit or publish them.

## Full fifth-order calibration

Run: `python recursive_calibrator.py --order 5 --points 0 1 2 --maxsteps 15` from the repository root, with the artifact directory as script location. The preceding fourth-order result is used as warm seed and fingerprinted. Field values and all first derivatives stay fixed. Degrees2,3,4 vary; fully symmetric degree5 jets are eliminated/recovered. Original backgrounds through derivative order4 are evaluated symbolically. Products and inverses use multiindex-factorial normalized Taylor coefficients.

The highest operator is840x1344, numerical rank735, leaving105 complete left compatibility rows. The three fits accept6,5,6 steps respectively. Full symmetric raw derivative residual blocks are:

| point | F | dF | d²F | d³F | d⁴F |
|---|---:|---:|---:|---:|---:|
| centre | 3.06e-14 | 2.80e-14 | 1.77e-13 | 2.31e-12 | 8.41e-11 |
| edge | 2.03e-15 | 3.12e-12 | 2.44e-11 | 3.44e-10 | 5.05e-10 |
| inner | 2.64e-15 | 2.17e-14 | 2.18e-13 | 2.44e-12 | 9.61e-11 |

The edge fit stops at the declared normalized objective tolerance1e-9; its resulting1e-10-scale raw blocks are reported rather than presented as machine-zero roots. No certified exact root is claimed.

## Independent verification

The separate NumPy univariate formal-series evaluator in six directions per point, with a recurrence inverse and exact original background derivatives, agrees with residual coefficients through degree4 within9.9e-13. Selected highest-operator columns agree within2.8e-13. The full scalar constraint coefficients through fourth derivatives are checked separately; fourth-derivative norms are9.66e-12,1.25e-10,1.18e-11. Input hashes remain unchanged. These are finite implementation checks, not exhaustive proof certificates.

## Important stability finding

Field values and first derivatives are exactly unchanged, but lower coefficients move substantially compared with the fourth-order construction:

| degree | relative change of normalized coefficient vector |
|---|---:|
| 2 | about44–53% |
| 3 | about63–69% |
| 4 | about35–38% |

Raw fifth-derivative norms are13629–15776; normalized degree5 coefficient norms are about715–733. Neither raw nor normalized growth from this small number of orders proves divergence or convergence. The data are new finite feasible germs, not a strict extension of the frozen previous fourth-order jets.

## Targeted frozen-lower control

Run: `python fifth_frozen_lower.py`. Keep every coefficient of degree0..3 from the successful fourth-order seed fixed, allow only degree4 to change, and eliminate/recover degree5. With lower degrees fixed, the remaining source is affine in degree4: a degree4 residual coefficient can contain the degree3 derivative of first jets only paired with degree1, not two such degree3 factors. The coefficient Jacobian therefore defines a finite linear feasibility check.

The585x840 repair matrix has numerical rank528, stable at relative cutoffs1e-8,1e-9,1e-11 (last retained singular values2.4e-4 to6.4e-4; next about1.2e-13). Remaining normalized objective norms are1.3870,1.3707,1.3615. Midpoint affine errors are below4.5e-12. The unrestricted least-squares compromise violates some retained lower equations as well; it is a failed control, not an alternative solution. This numerically excludes simultaneous closure within that frozen0..3 coefficient window at the tested germs and thresholds. It does not show that every possible lower germ must change or that an all-order compatible germ cannot exist. At least some degree2 or3 data from the particular previous seed need revision for this fifth-order test.

## Direct finite-neighbourhood probe

Run: `python fifth_local_probe.py`. Evaluate the actual original nonlinear field equation on each degree5 Taylor polynomial at twelve signed directional offsets for each radius, using the exact original background at each offset (no fitted residual operator). In coordinate units, sampled maximum full residuals are:

| radius | range across three germs |
|---|---:|
| 0.02 | 5.65e-6 to7.16e-6 |
| 0.01 | 1.76e-7 to2.23e-7 |
| 0.005 | 5.47e-9 to6.96e-9 |
| 0.0025 | 1.71e-10 to2.17e-10 |

Halving the coordinate radius reduces the sampled error by about32, consistent with the expected degree5 leading residual after F through derivative4 has been fitted. The sampled coframe remains regular and inverse g00 remains negative. These are sampled small-region approximations, not a uniform PDE bound or an exact solution.

The coefficient triangle inequality gives a bound on the difference between the fourth and fifth Taylor polynomials throughout the coordinate cube. At radius0.01 this is0.00279–0.00313 in field-vector norm. This bound concerns those two finite polynomials, not their difference from an unknown exact field. It shows why large changes of derivatives can still produce a modest change of field values on a small coordinate region.

## Consequence

Finite compatibility now reaches field-jet degree5 at all three points. The newly observed issue is selection/stabilization of lower coefficients when the order increases. Before interpreting further successful fits as evidence for one infinite formal jet, test narrower admissible update windows, monitor every retained coefficient across orders, and seek a compatible limiting/growth argument. The three local germs have not been joined into one field. Native action, physical interpretation, regional existence and OP5 closure remain open.

Artifacts: recursive-order-5-result.json; fifth_review_coefficients.py, fifth-review-coefficients-result.json, fifth_review.md; fifth_frozen_lower.py/result; fifth_local_probe.py/result; fifth-order-manifest.json and input snapshots. All prior successful and failed checkpoints are preserved.
