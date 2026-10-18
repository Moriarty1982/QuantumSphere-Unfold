# Regular Coefficient Domain for the Joint Jet

Date: 2026-10-18. This recomputes neighborhood estimates for the saved joint
1114-component finite jet. It concerns the explicitly added neutral Cartan
comparison, not the native paper's full action, HC/C7, frames or physical units.
Main TeX/PDF and the saved joint completion remain unchanged.

## Why a New Estimate Is Needed

The joint fit changes lambda2, E3 and psi3 and introduces E4, psi4 and lambda3.
The older cubic/quadratic field estimate therefore cannot be inherited. The
loader checks the saved completion's source fingerprints, its lower-point
provenance and exact retention of psi2. No new fit or coupling change is made.

Full symmetric derivative arrays are reconstructed from the unique coordinates,
including permutation multiplicities. For example, a single nonzero E4 component
with four distinct derivative indices occurs 24 times in the full tensor.
Using the unweighted unique-coordinate norm instead would understate the bound.

## Uniform Polynomial Changes

Let r be the Euclidean norm of the four comparison coordinates and use full
Frobenius derivative norms. Cauchy-Schwarz bounds the actual Taylor fields by

    d(r) = ||E2|| r^2/2 + ||E3|| r^3/6 + ||E4|| r^4/24,
    p(r) = ||psi1|| r + ||psi2|| r^2/2 + ||psi3|| r^3/6 + ||psi4|| r^4/24,
    l(r) = ||lambda1[:,0]|| r + ||lambda2[:,0]|| r^2/2
           + ||lambda3[:,0]|| r^3/6.

The column notation refers to the last coordinate column; all derivative and
internal indices are included in the norms. Hence ||E-I||_2<=d,
||psi-psi0||<=p and ||lambda[:,0]-lambda0[:,0]||<=l throughout the ball.

For d<1, E is invertible, ||E^-1||<=1/(1-d) and
(1-d)^4<=|det E|<=(1+d)^4. With v=|det E|, temporal weights are

    K0 = v inverse(E)[0,a] FLAT_WEIGHT[a] + lambda[a,0] Q_WEIGHT[a].

The fixed Clifford representation gives ||a0 I+a.alpha||<=sqrt(2)||a|| and
||Q||=1/2. Thus

    ||K0-K0_origin|| <= k(r)
       = 4d+6d^2+4d^3+d^4 + (1+d)^4 sqrt(2)d/(1-d) + l/sqrt(2).

If the origin's least eigenvalue is mu, set m=mu-k>0. The complete temporal
probe density stays positive with inverse norm at most 1/m.

The derived constitutive/probe Schur block is

    T_ab = -1/2 Im(psi^dagger A_a K0^-1 A_b psi), A_a=Q_WEIGHT[a].

Since ||A_a||=1/2, each entry perturbation is bounded with coefficient 1/8.
The 4-by-4 operator norm is at most four times that bound. With P=||psi0||,

    ||T-T_origin|| <= t(r)
      = 1/2 [(2Pp+p^2)/m + P^2 k/(m mu)].

For origin least singular value tau, s=tau-t>0 bounds sigma_min(T) throughout
the ball, and ||T^-1||<=1/s. T is real antisymmetric; a positive singular
margin is not a positive-definiteness claim about T.

These are analytic inequalities valid off shell. Their recorded inputs and
matrix margins are ordinary floating-point evaluations, NOT interval-certified
enclosures. The tests do not turn rounding-dependent numbers into a proof.

## Geometric Domain

Congruence g=E^T ETA E keeps Lorentzian signature whenever E is invertible.
The same d bounds

    ||g^-1-ETA|| <= d(2-d)/(1-d)^2 = z,
    lambda_min(g_spatial) >= 1-d(2+d).

Therefore g^-1(dt,dt)<=-1+z<0 when z<1, and the coordinate t=constant
slices are spacelike when the displayed spatial lower bound is positive.
These are statements about the Taylor metric, not a physical choice of clock.

## Recomputed Ball

The dyadic selection rule retains at least half of both origin temporal
margins, bounds d by .1, and checks both geometric slice conditions. It gives
r=1/16384=0.00006103515625, rather than the earlier r=1/8192.
The parent dyadic radius fails the chosen half-T-margin test. This failure
does not locate a singularity or prove that the larger ball is irregular.

| Uniform quantity on the new ball | Numerical estimate |
| --- | ---: |
| d: coframe change | 2.989405570e-9 |
| p: spinor change | 0.001151570051 |
| l: temporal multiplier change | 9.289561569e-5 |
| Temporal probe eigenvalue lower bound m | 0.9680084727 |
| T singular lower bound s | 0.02557686508 |
| T inverse norm upper bound | 39.09783301 |
| Inverse-metric change z | 5.978811166e-9 |
| Spatial metric eigenvalue lower bound | 0.9999999940 |

The coordinate radius is conservative and chart-dependent, with no physical
length calibration. It is not an optimized threshold or an existence radius.

## Independent Companion Checks

[Cartan regularity](HC_Cartan_Joint_Cartan_Regularity.md) derives an exact
H(E)=|det E| A^T H(I) A congruence and a uniform inverse estimate. At this same
ball it gives sigma_min(H)>=0.9999999821 and ||H^-1||<=1.00000001794.
This closes a separate algebraic connection-elimination check, not a missing
proof of full gravitational hyperbolicity.

[The tilted normal cone](HC_Cartan_Joint_Normal_Cone.md) additionally controls
the normalized 28-real-dimensional probe/constitutive subblock for small
changes of time-slice normal. It explicitly keeps the n_mu constitutive factors
and all spatial multiplier columns; it does not replace the full normal symbol.

The parent uses full symmetric arrays and tensor contractions for its fields.
The independent Cartan worker instead uses the unique-coordinate homogeneous
Taylor evaluator. The resulting actual fields agree in cross-checks. Both
recompute the algebraically eliminated connection at displaced points.

## Remaining Gap

All 1114 origin components still have norm about 5.38e-10. The actual Taylor
fields nevertheless have nonzero probe and constitutive residuals away from
the origin. A regular coefficient domain is not a solution domain.

Still required are the full gauge-reduced gravitational normal symbol and
constraint-propagation system, compatible surface data, and an existence or
formal-integrability argument. No uniform full-normal rank, hyperbolicity,
energy stability, physical scale or native model identification follows here.

## Reproduction

```text
python -B analysis/HC_Cartan_Joint_Neighborhood.py --output analysis/HC_Cartan_Joint_Neighborhood.json
python -B -m unittest discover -s scripts/qsc_audit/tests -p test_hc_cartan_joint_neighborhood.py
```

Sixteen focused checks cover the full fourth-order terms, factorials, independent
fields, changed-radius rule, geometric and temporal estimates, actual sample
controls, provenance and explicit non-solution limitations. Boundary samples
check the implementation; the norm inequalities provide the uniform argument.

Final verification: 2,026 audit tests and 34 separate OP5 checks passed (2,060
total), including 16 neighborhood, ten normal-cone and eight Cartan-regularity
checks added in this stage. The full-monolith preservation and whitespace
checks also passed. No new commit, push or PDF build was performed.
