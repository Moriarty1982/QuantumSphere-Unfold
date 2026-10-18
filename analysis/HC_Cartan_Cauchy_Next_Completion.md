# Next Cartan Completion with Fixed Tangential Jets

Date: 2026-10-18. Added neutral commuting-spinor odd-cross comparison only.
This continues the finite source law, not a native HC/C7 or regional PDE
construction. Current committed numerical baseline: 8215320. The v4.9.0
main-text integration and this follow-up are local, uncommitted work.
The [research issue](https://github.com/Moriarty1982/QuantumSphere-Unfold/issues/16)
and central register were read; no issue was changed or posted to.

## Fixed Question

The [source law](HC_Cartan_Normal_Source_Compatibility.md) determines six
normal source values from compatible tangential data at the 384-row order.
Does its example q=0.01(1,-0.5,0.3,0.2,0.4,-0.1) extend to the later
1114-row equations while the chosen tangential jets stay fixed?

Use the matching current joint loader, its saved highest coefficients and
the source report's actual 1200-coordinate increment. No lower coupling,
spinor first jet, multiplier value or spatial lower point is changed.
Recompute the Levi--Civita cubic at the shifted point. The old original
1114 completion remains valid at its own unshifted point; it is not
invalidated by a failure of this changed witness.

## Highest Mask and Exact Finite Gate

The [independent source-reading derivation](HC_Cartan_Highest_Cauchy_Mask.md)
gives the next tangential mask and the finite compatibility proof. Highest
increments v have 1720 real coordinates: E4 (560), lambda3 (320), psi4
(840). Psi4 is realified per quartet, unlike the earlier whole-block
realification of psi2 and psi3. Preserving the represented tangential
traces of E, E_t, psi and lambda allows exactly:

| Block | Allowed derivative tuples | Real count |
| --- | --- | ---: |
| E4 | At least two temporal indices | 160 |
| lambda3 | At least one temporal index | 160 |
| psi4 | At least one temporal index | 480 |
| Total | | 800 |

All unallowed coordinates retain their original nonzero values, not zero
absolute derivatives. For a frozen earlier witness the residual is affine:

    f(v) = f0 + (0 ; D) v,

where its first 394 rows have no highest dependence, and D has 720 rows.
For an allowed insertion M, a highest lift exists exactly when both
f0_old=0 and K_M.T f0_new=0, with K_M spanning ker((D M).T).
This is finite linear algebra. Numerical least squares only supplies a
solution if the actual unprojected residual vanishes to the declared
tolerance; otherwise its output is a failed minimum-residual control.

## Results for the Chosen Witness

The frozen source lift has all 384 earlier rows small, but its ten extra
scalar Hessian rows have norm 0.4756266. Highest derivatives cannot affect
these rows, even if their tangential restrictions are removed.

| Permitted correction | Numerical rank | All 1114 residual norm |
| --- | ---: | ---: |
| None, old highest frozen | Not applicable | 98.96015 |
| All 1720 highest coordinates | 363 in 720 rows | 25.41024 |
| Only 800 trace-preserving highest coordinates | 240 in 720 rows | 40.85894 |
| Also 368 earlier mixed coordinates, psi2 fixed | 568 in 1114 rows | 32.09525 |
| Same freedom, first enforce all old 394 rows | 454 in reduced 720-row tail | 33.15927 |

The 1114-row norm uses the declared packed unique-derivative coordinates.
Separate R2 and FE2 diagnostics use full symmetric derivative tensors;
C3 uses unique triples. They need not add in quadrature to the packed norm.
The old-first report's increment norm refers to its reduced kernel/highest
coordinates, not an independently selected physical norm of the full jet.

The 368 earlier coordinates are lambda2 (64), E3 (64) and psi3 (240),
using the preceding Cauchy mask. Together with 800 highest entries they
form the 1114-by-1168 affine re-preparation problem. Entire psi2 is fixed
at the shifted witness, including its 96 normal-containing coordinates.
Only p2-fixed affinity is used. General psi2 re-preparation can introduce
quadratic terms, particularly in C3, and is not included in this solve.

The unrestricted least-squares minimum 32.09525 trades errors among all
equations, including old rows; it is NOT an acceptable continuation.
The separate old-first calculation prevents that trade:

1. The 394-by-368 old response has rank 114. Its minimum residual is
   2.62e-11, so the old conditions can be restored within tolerance.
2. Its 254-dimensional kernel is the remaining earlier freedom. Combine
   it with the 800 allowed highest coordinates and minimize only the new
   720 rows without altering the old response.
3. This tail map has rank 454 and minimum residual 33.15927. Direct actual
   re-evaluation has old norm 3.00e-11, R2 norm 10.40042, FE2 norm 4.57813,
   and C3 norm 32.03219. All represented tangential entries remain fixed.

Thus the residual is not merely a frozen-highest artifact or an inability
to restore the old scalar gate. The chosen earlier data fail the later
finite gate under this fixed-psi2, fixed-tangential re-preparation.
The rank relation 114+454=568 agrees with the combined response.
These are floating-point ranks and distances, not interval certificates.
The combined retained/discarded singular gap is about 0.01496 versus
1.53e-13, with cutoff 7.64e-8. Affine prediction errors are below 3e-10;
the failed residuals are not roundoff-sized.

## Interpretation and Next Step

This does not refute the finite 384-row source law: it adds necessary
higher-order compatibility. Nor does it rule out all completions for the
same q, all compatible tangential data, or the parent comparison model.
The chosen prescribed tangential data were obtained from a compatible
384-row lift, not from a proved admissible surface solution.

The next finite problem should release the remaining 96 normal-containing
psi2 coordinates while keeping its spatial entries and all other prescribed
tangential data fixed. Its exact dependence needs a fresh derivation and
a controlled nonlinear/reduced compatibility solve. Failure with psi2 fixed
does not decide that larger problem. Spatial derivatives of moving source
and gauge bases, genuine surface data, further prolongation, propagation,
regional existence and native/physical identification are still separate.
No older neighborhood estimate transfers to these modified witnesses.

The [script](HC_Cartan_Cauchy_Next_Completion.py) and
[pinned report](HC_Cartan_Cauchy_Next_Completion.json) retain the actual
failed witnesses, fixed data, numerical cutoffs and input fingerprints.
The main v4.9.0 TeX/PDF are unchanged by this follow-up.

Verification: all 2175 audit tests passed in 292.349 seconds, including
14 new next-completion tests. All 34 separate OP5 checks also passed
(2209 total). Full-monolith preservation and whitespace checks passed.
The main expanded source hash remains
`f998e7b97373b87b9395192709059db1543a5edfeeee0e2bf968c53c85eb4ba8`.
No commit, push, issue update, publication or new PDF build was performed.

Performance follow-up: the script now uses the
[persistent matrix/SVD cache](Numerical_Matrix_Cache.md). Its own input
fingerprints include that implementation, and its scientific report has
been regenerated accordingly. The equations, mask, ranks and reported
residuals are unchanged. Actual field residuals are still recomputed on
cached runs. Use `--no-cache` to bypass all stored matrices/decompositions.
