# Compatible Higher Tangential Data at the Shifted Source Point

Date: 2026-10-19. Local, uncommitted continuation of baseline 5eb266f.
The OP register and issue 16 were read. Neither was changed. This remains
the added neutral commuting-spinor odd-cross comparison, not native HC/C7.
Main TeX, PDF, published payloads and metadata were not changed.

## The Problem Is Deliberately Changed

The [spatial-trace obstruction](HC_Cartan_Spatial_Trace_Obstruction.md)
excludes normal-only completion of the previously selected tangential
germ. This calculation does not contradict that result: it chooses new
higher tangential data, subject to the full finite equations, instead of
freezing the rejected germ obtained at only the earlier 384-row stage.

The lower point is fixed throughout the solve. In particular, retain
the same six source values

    q = (0.01, -0.005, 0.003, 0.002, 0.004, -0.001),

the corresponding E2 and lambda1 shift, psi and psi1, lambda0, all lower
field values, Q, mass matrix, Einstein coefficient and vacuum value. The
LC cubic is recomputed at this shifted point. No fit parameter is hidden
in those quantities.

All higher coordinates are now free:

| Block | Real coordinates |
| --- | ---: |
| psi2, normal and spatial | 240 |
| lambda2, E3, psi3 | 960 |
| E4, lambda3, psi4 | 1720 |
| Total | 2920 |

Allowing spatial psi2 is necessary for this search: the earlier source
compatibility report gives an injective rank-six source gate even when
only spatial psi2 is held fixed and the other higher data are free.
One cannot quietly keep the original spatial psi2 and independently
prescribe the same nonzero q. Higher tangential jets, not just their
normal counterparts, must therefore be reconsidered.

## Construction

Start with the original unshifted completion's higher coefficients,
but evaluate them at the prescribed shifted lower point. For all 240
psi2 increments p, the same source inspection used in the earlier
normal-Hessian derivation yields

    F(p,w) = b + J p + (0_794 ; Q2(p)) + A w,

where w has 2680 coordinates and Q2 is quadratic. A is independent of p.
The old 368 earlier response columns are reused, 592 missing earlier
columns are computed, and the full analytic 1720-column highest map is
restored. Two bounded local processes compute the independent missing
columns and the 240 central derivative columns of J. Only the parent
owns the persistent cache and final output.

The cached A has shape 1114 by 2680 and numerical rank 821. Its left
gate has dimension 293. Eliminate w, then solve the remaining gate in
p using the explicit quadratic formula and analytic derivative. At
p=0 the reduced derivative has rank 155, with smallest retained
singular value about 0.009908. A full step reduces the gate norm from
0.03361381 to about 1.08e-11. Recover w by the pseudoinverse and check
the actual full unprojected residual, including the full symmetric
probe and gravity arrays.

## Result

| Actual residual | Norm |
| --- | ---: |
| All 1114 higher equations | 4.87e-10 |
| All lower 68 equations | 2.07e-14 |
| Old 394 equations | 3.41e-11 |
| Earlier 384 equations | 3.41e-11 |
| Full R2 array | 2.80e-11 |
| Full FE2 array | 1.18e-10 |
| All C3 components | 4.76e-10 |
| Previously obstructing 120 spatial C3 rows | 3.05e-10 |

The full polynomial reconstruction agrees with a direct simultaneous
p,w evaluation within 4.92e-10. The candidate is a numerical finite-jet
completion at the declared 1e-7 acceptance tolerance, not an exact
symbolic solution. All actual coefficients are stored in the JSON.

The 240-coordinate psi2 increment has norm 0.17684. The other higher
increment has norm 24.04154. Relative to the original completion, the
earlier prescribed-tangential entries change by norm 10.54334 and the
highest prescribed-tangential entries by norm 9.23191. These are
coordinate-dependent jet norms, not physical length or mass scales;
they do not establish a small perturbation or a controlled spatial
neighborhood.

## The Earlier Source Law Still Checks

An independent regression test reconstructs the 384-row response matrix
from the expanded derivatives, re-evaluates the six source columns at
the original lower point, and eliminates the original 464 normal
coordinates. Its source gate still has rank six. Feeding the candidate's
newly prescribed tangential data through `prescribed_source_law` recovers
the same q within 1e-8 and passes its compatibility tolerance. This
tests that the older conditional source law and the new candidate are
consistent; it does not promote q to an arbitrary regional function.

## Meaning and Limits

The earlier large residual was not proof that the source shift itself
was impossible. A higher tangential lift chosen only for 384 equations
did not meet later constraints; selecting higher data against all 1114
equations removes that particular obstruction numerically.

What is obtained is one alternative compatible finite jet at one fixed
lower source point. It is not preservation of the old tangential germ,
an exact or interval-certified existence proof, propagation on a surface,
a convergent Taylor series, a regional PDE solution, a gauge/physical-mode
classification, a native action derivation, or an identification of
frames, masses or Planck scales. The old original completion and the
rejected fixed-germ obstruction remain separate valid controls.

The [regularity follow-up](HC_Cartan_Compatible_Lift_Regularity.md) now
recomputes geometric, temporal-subblock and algebraic Cartan bounds from
these changed coefficients, and rechecks the normal inverse at the
origin. Uniform full-normal-operator control, formal propagation and
compatible surface evolution remain separate open questions.

## Reproduction and Verification

Run `python -B analysis/HC_Cartan_Compatible_Tangential_Lift.py --output
analysis/HC_Cartan_Compatible_Tangential_Lift.json` from the repository
root. The first build uses two local processes; `--workers 1` provides
a sequential path. All matrices and SVDs use the existing scoped DI and
collision-safe cache. Process count is not a mathematical input and
does not change column order or the cache identity.

50 focused tests passed: 11 expanded-lift, 10 spatial-trace, 8 complete
quadratic, 7 normal-Hessian and 14 previous Cauchy-completion tests.
They verify the analytic quadratic derivative, worker columns, direct
full residuals, unchanged lower source point, changed boundary scope,
and recovery of q by the earlier source law. The full repository suite
was not rerun for these isolated new analysis modules. No additional
agent was spawned after the earlier usage-limit failure; bounded local
process parallelism handled independent column evaluations.
