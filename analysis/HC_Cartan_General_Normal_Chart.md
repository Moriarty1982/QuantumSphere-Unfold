# General-Coframe Normal System and a Local Coordinate Chart

Date: 2026-10-19. Local, uncommitted continuation after baseline 5eb266f.
The OP register and issue 16 were read; neither was updated. Added
neutral commuting-spinor odd-cross comparison only. Main TeX/PDF unchanged.

## Why the Origin Formula Was Insufficient

The original 68-by-56 normal system assumed E=I and dE=0. The compatible
Taylor field has E(x)!=I and dE(x)!=0 away from its origin. Updating only
the spinor or multiplier in the old normal-point formula would omit
coframe, volume, inverse-frame, LC and algebraic Cartan derivative terms.

This module evaluates the same independent constraint, real probe and
coframe Euler equations at general invertible coframe. It adds the same
twelve mixed temporal/spatial constitutive curls. It does not assume
that the sampled Taylor field is an exact solution.

## General Connection Derivative

Let H(E), R(psi), s(E,psi) be the existing Cartan Hessian, response and
source, with lambda flattened in the established coframe order:

    k = H^-1 (-s + R.T lambda),
    partial_r k = H^-1(-partial_r s + (partial_r R).T lambda
                      + R.T partial_r lambda - (partial_r H) k).

All terms are differentiated analytically. In particular, with V=E^-1
and v=|det E|,

    partial_r V = -V (partial_r E) V,
    partial_r v = v tr(V partial_r E).

Source components are recomputed from the fixed Clifford forms and the
current psi. Their derivative is twice the real mixed bilinear. The
response derivative and the two inverse-coframe factors of H are also
included. No inverse or prepared spin map at another field value is
substituted for the current one.

The Levi--Civita derivative follows by differentiating

    omega_LC,mu = eta (E Gamma_mu - partial_mu E) V.

The existing analytic metric-jet routine supplies partial_r Gamma_mu.
Adding partial_r k in the declared Lorentz basis gives the complete
partial_r omega_mu. The general real probe uses the full density-weight
divergence, including derivatives of v, V and lambda.

## General Mixed Curls

Write B_mu for the spin lift of omega_mu and D_mu psi=psi_mu+B_mu psi.
The mixed curl of the constraint C_a,mu is

    partial_0 C_a,i - partial_i C_a,0
      = Im pair_a(psi_0,D_i psi) - Im pair_a(psi_i,D_0 psi)
        + Im pair_a(psi, (partial_0 B_i-partial_i B_0)psi
                          + B_i psi_0-B_0 psi_i)
        - partial_0 E_a,i + partial_i E_a,0.

The symmetric second spinor derivative cancels. The final coframe terms
vanished at the old special origin but must be present at general x.

Hold E, dE, psi, lambda and the tangential lower derivatives fixed. Use
normal coordinates

    u = (E_,00 [16], real/imag psi_,0 [24], lambda_,0 [16]).

The 68-vector is affine, F_x(u)=b(x)+N(x)u. E_,00 occurs linearly in LC
curvature; psi_,0 and lambda_,0 enter the first Cartan derivative
linearly. The mixed curls have exactly one temporal derivative, so no
psi_,0 squared term occurs. This is a mixed-differential-order normal
block, not by itself a homogeneous principal symbol or a hyperbolicity
classification. Other spatial compatibility equations are not erased
by selecting these 68 rows.

## Coordinate Completion and Compatibility

Let G0 and U0 be the ten gauge and six source columns of the original
origin chart. Fix W=[G0 U0].T only as sixteen coordinate rows and form

    T(x) = (N(x); W), shape 84 by 56.

At the origin W completes the normal kernel. Away from it these fixed
rows are not asserted to be a transported geometric gauge or a new
physical source classification. If T has full column rank, the least
squares inverse supplies a unique candidate for a compatible augmented
right-hand side. It does not make arbitrary 84-component data solvable;
there are 28 left compatibility conditions.

The usual continuity argument is conditional and qualitative: if T(0)
has positive smallest singular value and the regular-coefficient
formulas are smooth, T stays full column rank in some smaller open
neighborhood. To certify a specified ball one still needs a uniform
bound such as ||T(x)-T(0)||<sigma_min(T(0)). Sampling does not supply
that bound. This argument also does not prove that N has rank exactly
40 everywhere: persistence of at least 40 directions and an exact
upper-rank/kernel classification are separate matters.

## Numerical Results

The [compatible-lift coefficient-domain](HC_Cartan_Compatible_Lift_Regularity.md)
ball supplies test coordinates, not a uniform normal-rank certificate.
Thirteen points cover the origin, positive/negative coordinate axes and
seeded directions, at radius 1/16384. Two local threads share scoped
cache services; each normal system is computed from its actual fields.

| Control | Result |
| --- | ---: |
| General versus original normal matrix at origin | 3.45e-14 norm |
| General versus original 68 equations at origin | 2.21e-14 norm |
| Numerical rank N at every sample | 40 |
| Largest sampled 41st singular value | 3.67e-15 |
| Smallest sampled augmented singular value | 0.10544038 |
| Largest sampled N(x)-N(0) operator norm | 0.03771356 |
| Largest affine reconstruction error | 3.93e-14 |
| Largest full 68 residual on the unchanged Taylor field | 7.82e-7 |
| Largest residual after augmented least squares correction | 1.14e-7 |

The last row matters: even re-solving normal values with the fixed W
coordinates cannot remove incompatible right-hand sides. The normal
operator's favorable sample ranks do not turn the Taylor field into a
regional solution. All source values at the original lower point remain
those of the compatible finite lift; they are not reinterpreted as free
functions on the sampled ball.

Independent centered differences of the original Taylor-field evaluator
check the complete omega derivative and mixed curls at a non-origin
point. Errors are about 4.23e-8 and 8.44e-8 at step 1e-7. The general
probe and connection value agree with that existing evaluator within
test tolerance. These numerical checks support the analytic formulas;
they do not certify differential identities by themselves.

## Next Work

A quantitative coefficient bound for N(x)-N(0) is still needed before
claiming a uniform full-normal chart on an explicit radius. The sampled
maximum above cannot be substituted for it. In parallel, the left
compatibility conditions must be propagated or imposed on evolving
tangential data. Neither an origin inverse nor a sampled augmented
inverse proves that propagation. Native HC/C7, global closure, physical
frames, scale identification, formal integrability and regional Cauchy
existence remain outside this result.

## Reproduction and Verification

Run `python -B analysis/HC_Cartan_General_Normal_Chart.py --output
analysis/HC_Cartan_General_Normal_Chart.json` from the repository root.
`--workers 1` selects sequential sampling. Per-field response matrices
and augmented SVDs use the existing DI/cache service, with the actual
field values and dependency fingerprints as inputs.

31 focused tests passed: 10 new general-normal-chart tests, 10 compatible
regularity tests and 11 compatible-tangential-lift tests. The new tests
cover the origin reduction, off-origin affinity, independent connection
and curl differences, general probe agreement, chart rejection of singular
input, and the nonzero compatibility residuals. The full repository suite
was not rerun for this isolated analysis module.
