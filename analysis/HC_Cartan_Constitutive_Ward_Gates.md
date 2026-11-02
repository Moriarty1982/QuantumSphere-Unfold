# Pointwise Constitutive Ward Gates

Date: 2026-10-18. Bounded sidecar for the added neutral commuting-spinor
odd-cross Cartan comparison, with the declared action, M, Q, c=1 and u=0
fixed. This derives necessary restrictions from the existing Ward identities
and compares them with the existing 56-variable normal block. No parent
720-variable continuation, coupling fit, native identification or existence
claim is made.

## Conventions and Point Assumptions

Use the identities and signs in
[the coordinate audit](HC_Cartan_Diffeomorphism_Residual_Identity.md),
[the Lorentz audit](HC_Cartan_Lorentz_Residual_Identity.md), and their `.py`
implementations. The algebraic Cartan connection must be eliminated as a
field expression with compatible differential consequences, not just have
zero connection Euler value at the point.

Write F^a_mu=C[Q]^a_mu-E^a_mu, and distinguish the constitutive curl J from a
Lorentz generator L:

```text
J^a_mu,nu = partial_mu F^a_nu - partial_nu F^a_mu,
X_ai = J^a_0i,                         a=0,...,3; i=1,2,3,
R1 = (partial_r R)_r,
FE1 = (partial_r FE_a^mu)_r,a,mu.
```

Here R1=0 means all first derivatives of the full complex probe residual,
and FE1=0 means all first derivatives of the independent coframe Euler
density. All assumptions below are at one point:

```text
F=R=FE=0, E=I, dE=0,
partial_i F^a_mu=0, partial_mu F^a_0=0,
lambda_a^0 = ell_a = (0.01,0.02,-0.03,0.04),
lambda_a^i = 0.
```

Consequently the only potentially nonzero first constitutive derivatives
are partial_0 F^a_i=X_ai. All spatial curls vanish. No multiplier derivative
is assumed zero. Internal indices on ell are already lower indices: the
contractions below contain no additional Minkowski metric.

## Coordinate Identity: Three Rows

The off-shell coordinate identity is

```text
E^a_nu partial_mu FE_a^mu
 + FE_a^mu (partial_mu E^a_nu-partial_nu E^a_mu)
 + lambda_a^mu (partial_mu F^a_nu-partial_nu F^a_mu)
 + F^a_nu partial_mu lambda_a^mu
 - 2 Re[(partial_nu psi)^dagger R] = 0.
```

At the point in question it becomes, before imposing FE1=0,

```text
sum_mu partial_mu FE_nu^mu + sum_a,mu lambda_a^mu J^a_mu,nu = 0.
```

For nu=0 the multiplier term is zero: J_00=0 and the spatial multiplier
columns vanish. For nu=i it is ell_a X_ai. Thus FE1=0 requires exactly the
following three rows from this identity:

```text
0.01 X_0i + 0.02 X_1i - 0.03 X_2i + 0.04 X_3i = 0,
i=1,2,3.
```

The fourth coordinate row is identically zero on these twelve variables.
R1=0 is not needed for this step: the coordinate identity already contains
FE1 and F1, while its probe source uses R itself. In particular, one must
not replace the off-shell identity by a source-free divergence identity
before performing this specialization.

## Differentiated Lorentz Identity: No Additional Rows

For each constant elementary generator L with L.T eta+eta L=0, the identity is

```text
FE:(L E) + 2 Re[(S_L psi)^dagger R] + F:(L.T lambda) = 0.
```

Differentiate the full identity once in direction r. The product rule gives

```text
(partial_r FE):(L E) + FE:(L partial_r E)
 + 2 Re[(S_L partial_r psi)^dagger R
        + (S_L psi)^dagger partial_r R]
 + (partial_r F):(L.T lambda) + F:(L.T partial_r lambda) = 0.
```

F=R=FE=0 and R1=FE1=0 leave

```text
(partial_r F):(L.T lambda) = 0.
```

For r=i this vanishes because partial_i F=0. For r=0, partial_0 F has
only spatial columns, whereas L.T lambda has only its temporal column.
Their componentwise contraction is therefore zero for every L, even for
nonzero X. Equivalently, before setting the spatial multiplier columns to
zero the remaining normal row would be

```text
sum_a,i,b X_ai L_ba lambda_b^i = 0.
```

Every coefficient vanishes here. Hence the 24 differentiated Lorentz rows
(six generators times four derivative directions) add rank zero on X.
The undifferentiated Lorentz identity is already zero under F=R=FE=0.
Differentiating an equality known only at this point would not be valid;
the step above differentiates the full off-shell identity first. A second
Lorentz differentiation or a coordinate differentiation would introduce
higher residual jets not set to zero by the stated assumptions, so neither
justifies extra homogeneous rows on X alone.

## Explicit Row Map and Rank

Use the pair-major ordering of `curl_constraints(... )[:3].reshape(-1)`:

```text
x = (X_01,X_11,X_21,X_31,
     X_02,X_12,X_22,X_32,
     X_03,X_13,X_23,X_33).T,

W = [ .01 .02 -.03 .04   0   0    0   0    0   0    0   0
       0   0    0   0   .01 .02 -.03 .04   0   0    0   0
       0   0    0   0    0   0    0   0   .01 .02 -.03 .04 ].
```

Thus W=I_3 tensor ell.T. Including the temporal coordinate row and all
first differentiated Lorentz rows gives the 28-by-12 map
`G = vertical_stack(zeros(1,12), W, zeros(24,12))`, in coordinate order
nu=0,1,2,3 followed by the Lorentz rows.

WW.T=0.003 I_3. Its three nonzero singular values are all
sqrt(0.003)=0.0547722557505; rank(W)=rank(G)=3 and dim ker(W)=9.
These ranks also follow exactly for the displayed decimal coefficients.
For example, each column may be chosen independently subject to

```text
X_0i = -2 X_1i + 3 X_2i - 4 X_3i.
```

This is the complete restriction on X supplied by these Ward identities at
the stated derivative order. It is a necessary compatibility condition,
not a sufficient condition for realizing R1=FE1=0 by actual field jets.

## Comparison with the Existing Normal Kernel

For a bounded numerical check, load the saved joint point using
`HC_Cartan_Constitutive_Transport.py`'s existing neighborhood loader and call
`HC_Cartan_Spatial_Propagation.py:normal_curl_system`. This only rebuilds the
existing 56-variable affine normal map; it performs no higher continuation
and writes no data. The loaded multiplier equals the one specified above.

Let A be its original 56-by-56 normal matrix, K its orthonormal kernel basis,
C its twelve mixed-curl rows, and B=CK the induced curl map. The original
normal rank is 34, so K has 22 columns. The measured results are:

| Map or quantity | Numerical result |
| --- | --- |
| rank B | 6 |
| nonzero singular values of B | 38.2050601, 29.5216687, 29.5216687, 14.4551958, 4.62789358, 4.62789358 |
| singular values of WB | 1.25099319, 1.02893444, 0.75868378 |
| rank WB | 3 |
| rank vertical_stack(A, WC) | 37 |
| rank vertical_stack(A, C) | 40 |

Ranks in this comparison use absolute tolerance 1e-10. The largest omitted
singular value of B is about 5.85e-13. If H is an orthonormal basis for
ker(WB), it has 19 columns and BH has three nonzero singular values,
approximately 17.9284277, 7.00920036 and 5.92545482. Its largest remaining
singular value is about 8.29e-13, and ||WBH|| is about 2.56e-16.

Accordingly, at numerical rank six,

```text
dim(image(B) intersect ker(W)) = rank(B) - rank(WB) = 3.
```

The Ward gates are compatible with nonzero normal-kernel-induced curls,
but exclude three of the six independent curl responses. Their admissible
normal directions have dimension 19, comprising the 16-dimensional kernel
of B and three directions with nonzero curl image. These are linear
normal-block statements, not counts of physical modes or a completed
prolongation. The saved point has mixed-curl norm about 1.80e-14, so it
provides a numerically zero affine offset; no exact affine consistency is
certified by these floating calculations.

The sign-fixed maximum-response direction used in
[the transport witness](HC_Cartan_Constitutive_Transport.md), at amplitude
0.01, has mixed-curl norm 0.3820506011 and

```text
W x = (0.00617979, 0.00826877, 0.00541482).T.
```

It therefore fails these necessary Ward gates. For compatible eliminated
jets retaining the assumed point residuals and constitutive first-jet
conditions, the coordinate identity forces the corresponding coframe
Euler divergences to be the negatives of these entries; all of FE1 cannot
vanish. This is consistent with the transport note's explicit warning that
the witness was not asserted to retain the prolonged completion. Its
reported nonzero frozen-higher-data R1 is a separate failure; it cannot
cancel the coordinate source, which contains R rather than R1.

## Limits

The three surviving curl responses show that these Ward gates alone do not
force J_0i=0. They do not show that any such response extends to a point jet
with all of R1=FE1=0, much less to a neighborhood solution. Conversely, the
excluded maximum-response witness is not a counterexample to propagation
by a fully prolonged parent system. Actual higher-jet compatibility,
including the remaining constitutive curl conditions and their affine
compatibilities, remains for the parent calculation. No regional closure,
gauge reduction, native-action result or existence theorem follows here.
