# Coordinate Ward Identity with All Residual Sources

This derives the coordinate identity of the added neutral Cartan comparison,
using the declared real probe law and independent-coframe Euler density. It
does not modify the action, main TeX/PDF, couplings or saved finite jets.

## Residuals and Weights

Let FE_a^mu be the independent coframe Euler density, R the full complex probe
Euler density, and F^a_mu=C[Q]^a_mu-E^a_mu. The multiplier Euler expression is
F_lambda=-F. Lambda_a^mu is a coordinate vector density of weight one, not an
ordinary vector. Its Lie variation is

    delta lambda_a^mu = xi^nu partial_nu lambda_a^mu
                       -lambda_a^nu partial_nu xi^mu
                       +lambda_a^mu partial_nu xi^nu.

The coframe is a covector, and the spinor is a coordinate scalar with its
separate Lorentz transformation. The connection Euler expression is assumed
eliminated identically as a field expression, together with its differential
consequences. Merely zeroing its value while drawing arbitrary curvature is
not sufficient; the independent Lorentz audit preserves that failed control.

## Derivation without Imposing Matter Equations

Insert the Lie variations into

    delta S = integral [FE:delta E + 2 Re(delta psi^dagger R)
                        -F:delta lambda].

For compactly supported xi the connection term vanishes after exact Cartan
elimination. The coefficient of partial_mu xi^nu is

    I^mu_nu = FE_a^mu E^a_nu + F^a_nu lambda_a^mu
              -delta^mu_nu (F:lambda).

Integration by parts gives

    partial_mu I^mu_nu = FE_a^mu partial_nu E^a_mu
                         +2 Re((partial_nu psi)^dagger R)
                         -F^a_mu partial_nu lambda_a^mu.

Expanding and cancelling the last multiplier derivatives yields the tested form:

    E^a_nu partial_mu FE_a^mu
      + FE_a^mu (partial_mu E^a_nu-partial_nu E^a_mu)
      + lambda_a^mu (partial_mu F^a_nu-partial_nu F^a_mu)
      + F^a_nu partial_mu lambda_a^mu
      - 2 Re((partial_nu psi)^dagger R) = 0.                 (1)

No coframe, constitutive or probe equation has been set to zero in (1). In
particular the multiplier-curl term, multiplier-divergence term and full complex
R cannot be dropped on arbitrary data. At the prior on-shell normal point,
E=I,dE=0 and F=R=0, this reduces to the four conditional coordinate rows
already used in the earlier prolongation. That specialization is not the full
off-shell identity.

## Bridge to the Gravitational Residual Tensor

The independently checked [Lorentz identity](HC_Cartan_Lorentz_Residual_Identity.md)
is

    FE:(J E) + 2 Re((S_J psi)^dagger R) + F:(J.T lambda) = 0.

If R=F=0 on an open set, it implies symmetry of

    S^{mu nu} = FE_a^mu eta^{ab} inverse(E)[nu,b].

Indeed, for every eta-antisymmetric J, FE:(J E)=0 makes E FE.T eta symmetric;
congruence by inverse(E) gives S=S.T. S is a contravariant density of weight
one, not an ordinary tensor. The coordinate identity then gives

    partial_mu(g_nu,rho S^{mu rho})
                    = (1/2) partial_nu g_mu,rho S^{mu rho},
    partial_mu S^{mu nu} + GammaLC^nu_mu,rho S^{mu rho} = 0.   (2)

There is no additional GammaLC^mu_mu,rho S^{rho nu} term in the last expression
for a weight-one density. Dividing by v=|det E| gives the ordinary tensor
T=S/v with nablaLC_mu T^{mu nu}=0. The Levi-Civita derivative here expresses
the geometric residual identity; it does NOT identify the independent sourced
Cartan curvature with metric LC curvature.

This proves the parent-identity link assumed in the independent
[conditional propagation derivation](HC_Cartan_Constraint_Propagation_Derivation.md).
Equation (2) remains conditional on the open-set R/F equations. It does not
establish their propagation from initial data.

## Off-Shell Controls

Six unfitted random normal jets retain fixed Q,M,c=1,u=0, generic psi/p1,
nonzero multipliers with every column present, and arbitrary compatible higher
derivatives. The exact eliminated connection and its actual derivatives give
F,R,FE and their first derivatives. No continuation fit is used.

Local coordinate second jets, local Lorentz first jets and a nonidentity
constant coordinate Jacobian transform these Euler data into nonzero coframe
first jets. The 40 coordinate and 24 Lorentz directions span all 64 first
coframe slots. Density weights, derivative companion terms and curvature
compatibility are preserved; an arbitrary unrelated curvature replacement
would not be a valid fixture.

The six Ward residual norms are between about 1.84e-14 and 9.56e-14 although
F,R,FE and dE are nonzero. Every omitted source term has a failed control.
Tests also check covariance of deliberately nonzero Ward defects, the required
multiplier density weight, invalid coordinate/Lorentz jets and the density-to-
tensor bridge, including a negative control for an extra volume-connection term.

The identities follow from the displayed action variation; numerical tests
check implementation and signs, not a universal symbolic or interval certificate.
The source inputs are pinned with normalized SHA256 values.

```text
python -B analysis/HC_Cartan_Diffeomorphism_Residual_Identity.py --output analysis/HC_Cartan_Diffeomorphism_Residual_Identity.json
python -B -m unittest discover -s scripts/qsc_audit/tests -p test_hc_cartan_diffeomorphism_residual_identity.py
```

Nine focused checks are preserved. There is no autonomous full R/F/gravity
subsidiary system, complete gauge reduction or native identification claim.
