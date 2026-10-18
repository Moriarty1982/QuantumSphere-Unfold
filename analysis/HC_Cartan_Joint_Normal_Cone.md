# A Tilted Normal Cone for the Partial Probe/Constraint Block

This extends the recomputed [joint coefficient-domain estimate](HC_Cartan_Joint_Neighborhood.md).
It is a uniform estimate for a selected 28-real-dimensional block with geometry
derivative amplitudes frozen, NOT the full gravitational principal symbol.
No main TeX/PDF, coupling, native HC/C7 or frame identification is changed.

## Correct Normalization of the Tilted Block

The full real probe law has principal derivative terms

    i W^mu partial_mu psi + (i/2) partial_mu(W^mu) psi.

For real normal covector n, write delta(partial_mu psi)=n_mu u and
delta(partial_nu lambda_a^mu)=n_nu b_a^mu. Define the four real divergence
amplitudes a_a=n_mu b_a^mu. With frozen geometry derivatives the probe response is

    i K(n) u + (i/2) A_a psi a_a, K(n)=n_mu W^mu.

The factor 1/2 is essential; it comes from the variable-weight real law,
including its defect term. The constitutive normal response is

    delta F_a,mu = n_mu L_a(u), L_a(u)=Im(psi^dagger A_a u).

Eliminating u from the probe gives the full response n_mu T(n)_ab a_b, where

    T(n)_ab = -1/2 Im(psi^dagger A_a K(n)^-1 A_b psi).

Selecting X^mu F_a,mu with n_mu X^mu=1 gives precisely T(n). For n=(1,q),
q purely spatial, the original temporal-column rows use X=partial_t. Raw
metric-normal rows or unnormalized temporal rows have extra n(X) factors;
dropping those factors is not legitimate. There is no extra universal A(n)
insertion in this chosen reduction.

The tested real matrix has unknowns u (24 real components) and a (four), and
outputs the probe residual plus normalized constitutive rows. Its inverse is
controlled by K(n) and T(n). The other twelve multiplier derivative amplitudes
and the geometric derivative amplitudes are not solved by this block.

## Uniform Spatial Weight Bound

Use the parent coordinate ball r=1/16384. Let d bound ||E-I|| and let lS
bound ||lambda[:,1:4]||_F using the spatial columns of EVERY multiplier
coefficient through lambda3, including any nonzero constant value. Then

    sup_(|q|=1) ||q_i W^i|| <= S
       = sqrt(2)(1+d)^4/(1-d) + lS/sqrt(2).

Using only the parent's temporal-column multiplier estimate would not justify
this assertion. The saved data give lS about 0.0001942166 and S about 1.414350915.

## Cone and Inverse Estimate

The parent provides K(dt)>=m I, sigma_min(T(dt))>=s and ||psi||<=B uniformly.
For |q|<=rho and h=rho S<m,

    K(dt+q)>=(m-h) I,
    ||T(dt+q)-T(dt)|| <= B^2 h/[2m(m-h)].

The sufficient condition h<=min(m/2, s m^2/(B^2+s m)) retains at least half
of both temporal margins. The implementation takes half this allowed tilt
and also caps it by half the metric timelike bound
sqrt((1-z)/(1+z)), z=||g^-1-ETA|| bound from the parent.

For positive rescaling n=alpha(1,q), K scales by alpha and T by 1/alpha.
The recorded numbers use alpha=1; unnormalized numeric margins must not be
carried over unchanged to a different normal normalization.

With mN=m-h and sN=s-B^2h/[2m(m-h)], let rP and f denote the two output norms.
Since ||L||<=B and the probe divergence block norm is at most B/2,

    ||a|| <= B/(mN sN) rP + 1/sN f,
    ||u|| <= [1/mN+B^2/(2 mN^2 sN)] rP + B/(2mN sN) f.

The operator norm of this 2-by-2 positive majorant bounds the actual real
28-by-28 inverse, without identifying it with a full coupled inverse.

| Uniform quantity | Numerical estimate |
| --- | ---: |
| Normal tilt radius rho | 0.0002377642642 |
| K(n) eigenvalue lower bound | 0.9676721906 |
| T(n) singular lower bound | 0.01918487091 |
| g^-1(n,n) upper bound | -0.9999999375 |
| Partial 28-block inverse norm upper bound | 1056.518539 |

These are sufficient, deliberately loose bounds in uncalibrated coordinates,
not physical angles, signal speeds or measured stability margins. Analytic
inequalities are evaluated with floating input norms, not interval arithmetic.

## Verification and Limit

Tests compare the tilted principal amplitudes directly to the complete real
operator, form and eliminate the real matrix independently, check normal
rescaling and its required constitutive factors, and sample both coordinate
and normal balls. They check actual inverse norms, not just matrix rank.
The independent read-only derivation confirmed the normalization and the
resolvent bounds; agreement is not substituted for their written derivation.

This establishes robustness of this subblock against small tilts of the
coordinate time slices on the finite Taylor fields. It does not establish
constant rank or hyperbolicity of the entire constrained gravity system,
propagation, Cauchy existence or a field-equation solution on the ball.

```text
python -B analysis/HC_Cartan_Joint_Normal_Cone.py --output analysis/HC_Cartan_Joint_Normal_Cone.json
python -B -m unittest discover -s scripts/qsc_audit/tests -p test_hc_cartan_joint_normal_cone.py
```

Ten focused checks are preserved with the saved report and normalized source
fingerprints. The normal estimate is recomputed from the current full joint
data rather than inherited from an earlier jet or radius.
