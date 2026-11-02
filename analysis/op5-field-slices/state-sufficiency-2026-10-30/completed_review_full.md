# Full completed-R1 tangent projection and nearby controls

30 October 2026. This extends the earlier vertical-only projection test at point0. The authoritative equations remain R=(F24,G4,dg4). No model assumptions, old source/results or repository files were modified.

## Full tangent test

completed_review_full_gate.py uses the exact original background Taylor coefficients through degree3, constructed by TaylorModel(4). The background monomials are formed by repeated multiplication, including the constant term without differentiating an ambiguous zero-to-zero power. This supplies the third position derivatives needed when differentiating the completed system's total derivative in arbitrary q directions.

Here q=(psi24,firstjets96,position4), and the full tangent is N_full=ker D_q R rather than only ker D_jets R. At point0 the 32x124 Jacobian has numerical rank32 and a92-dimensional kernel. Its first-jet-only block still has rank31 and65 vertical directions. Thus the added directions include allowed field-value and position variations rather than only first-jet changes at a fixed base state.

The actual saved symmetric H is restored from normalized coefficients and repaired by a closest correction. Its total completed derivative residual falls from about3e-13 to2.97e-14. For the fixed repaired H, AD differentiates the entire expression

P(q,H)=[D_q R(q) tangent(q,H)]

including the changing first-jet entries in the tangent's psi rows. The full gate is L^T D_q P N_full, where L is the complete15-dimensional left kernel of the symmetric A2 matrix (128x240, rank113). Background variation and both field/jet chain-rule terms are retained.

## Observed full gate

| quantity | result |
|---|---:|
| R norm | 7.81e-14 |
| repaired total derivative norm | 2.98e-14 |
| full projected gate shape | 15x92 |
| full projected gate norm | 6.57e-14 |
| largest gate singular value | 3.46e-14 |
| gate norm / full unprojected derivative norm | 1.74e-16 |
| vertical projected gate norm with the same background | 5.17e-14 |

No stable nonzero singular value is detected at this scale. This removes the vertical-only limitation of the previous calculation at this point: the full tangent projection has no observed infinitesimal obstruction in float64. It is not an analytic proof of exact rank or surjectivity on a neighborhood.

## Two nearby nonlinear controls

completed_review_full_nearby.py chooses two reproducible random unit directions in the full92-dimensional tangent (seed20261030) and perturbs q by epsilon1e-3. Each perturbed state is reprojected onto R=0 by at most five least-norm Newton corrections; both actually need one correction. The background Taylor expansion is recentered from the ORIGINAL exact symbolic background at every evaluation. The test therefore does not evaluate an old cubic background truncation as though it were exact at the displaced point.

At each reprojected q, the symmetric-H completion matrix is rebuilt and a closest H correction is solved. The source and the complete unprojected derivative residual are evaluated, not only a left-projected score.

| quantity | trial0 | trial1 |
|---|---:|---:|
| R1 reproject correction norm | 5.67e-8 | 6.48e-8 |
| final R norm | 7.32e-15 | 1.22e-14 |
| derivative residual with old H | 0.01029 | 0.01121 |
| H correction norm | 0.00432 | 0.00456 |
| final completed derivative residual | 1.56e-14 | 2.48e-14 |
| A2 numerical rank | 113 | 113 |
| coframe determinant | 13.6378 | 13.6326 |
| inverse metric g00 | -0.468065 | -0.467973 |

The coordinate positions, field values and first jets vary together in these controls. Their regular coframes remain in the tested comparison chart. The two successful completions support the local numerical projection picture beyond the central germ, but do not sample all nearby states or establish uniform bounds.

## Interpretation and boundary

The completed system has no detected source-projection obstruction at the central full R1 tangent, and two nearby reprojected germs also admit numerical symmetric second-jet completions. Therefore the previously observed sampled Cartan character gap of one cannot, by itself, be identified with a new lower compatibility equation obstructing this projection. Character equality/involutivity and source compatibility are different tests.

No conclusion of exact formal integrability follows. The calculation does not prove constant analytic ranks, surjectivity of every later projection, eventual involutivity, convergence of a formal series, a regional common field, native physical action, or OP5 closure. The declared G equations are reused as the authoritative completion; they are not independently derived from physical principles here.

## Artifacts and reproduction

- `python completed_review_full_gate.py`: full AD tangent projection, writes completed_review_full_gate_result.json.
- `python completed_review_full_nearby.py`: two exact-background reproject/complete controls, writes completed_review_full_nearby_result.json.

JSON artifacts record source/input hashes and numerical spectra. Runs use only the existing declared comparison and write new completed_review_full* artifacts in the task workspace. They perform no scalar fitting, commit, merge, push or publication.
