# Second Coordinate Ward Gates at a Fixed Finite Jet

Date: 2026-10-18. Independent bounded proof check for the added neutral
commuting-spinor Cartan comparison. The conclusion below is conditional on
exact finite-jet hypotheses. It is a necessary compatibility obstruction,
not an existence or propagation theorem.

## Conventions and Source Identity

Use the signs and Euler-density conventions of
[the coordinate identity](HC_Cartan_Diffeomorphism_Residual_Identity.md) and
`HC_Cartan_Diffeomorphism_Residual_Identity.py:ward_terms`. Internal indices
`a,b=0,...,3`, coordinate indices `mu,nu,r=0,...,3`, and spatial indices
`i,j=1,2,3` have distinct roles. Define

```text
F^a_nu = C[Q]^a_nu - E^a_nu,
J^a_mu,nu = partial_mu F^a_nu - partial_nu F^a_mu,
F2[r,s,a,nu] = partial_r partial_s F^a_nu,
FE2[r,s,a,mu] = partial_r partial_s FE_a^mu,
R1[r] = partial_r R.
```

`FE_a^mu` and `lambda_a^mu` are weight-one coordinate vector densities;
`F^a_nu` has a lower coordinate index. The multiplier Euler expression is
`-F`. `R` is the full complex probe Euler density. Every spinor pairing
below sums all flavor and spinor components, using complex conjugation in
the first factor. No extra Minkowski metric occurs in `lambda_a^mu F^a_nu`
or its derivatives: the internal indices are already paired as lower/upper.

The connection must be eliminated identically as a field expression,
including its differentiated consequences. For compatible field jets the
off-shell identity is

```text
0 = sum_a,mu E^a_nu partial_mu FE_a^mu
  + sum_a,mu FE_a^mu (partial_mu E^a_nu - partial_nu E^a_mu)
  + sum_a,mu lambda_a^mu J^a_mu,nu
  + sum_a F^a_nu sum_mu partial_mu lambda_a^mu
  - 2 Re sum_A conjugate(partial_nu psi_A) R_A.             (1)
```

This is an off-shell differential identity, not an equation valid only at
the selected point. It may therefore be differentiated before specializing.
Arbitrary independent residual arrays, or an unrelated curvature with only
the connection Euler value set to zero, do not meet this premise.

## Full Product Rule

For any direction `r`, differentiating (1) gives exactly

```text
0 = sum_a,mu (partial_r E^a_nu) partial_mu FE_a^mu
  + sum_a,mu E^a_nu partial_r partial_mu FE_a^mu
  + sum_a,mu (partial_r FE_a^mu)
                  (partial_mu E^a_nu - partial_nu E^a_mu)
  + sum_a,mu FE_a^mu
                  (partial_r partial_mu E^a_nu
                   - partial_r partial_nu E^a_mu)
  + sum_a,mu (partial_r lambda_a^mu) J^a_mu,nu
  + sum_a,mu lambda_a^mu
                  (F2[r,mu,a,nu] - F2[r,nu,a,mu])
  + sum_a (partial_r F^a_nu) sum_mu partial_mu lambda_a^mu
  + sum_a F^a_nu sum_mu partial_r partial_mu lambda_a^mu
  - 2 Re sum_A [conjugate(partial_r partial_nu psi_A) R_A
              + conjugate(partial_nu psi_A) R1[r]_A].      (2)
```

In particular the multiplier-curl derivative has a plus sign, while both
probe-source terms have minus signs. Only `R` and `R1` occur; `R2` does not.
Vanishing residual values at a point must not be differentiated as though
they vanished on an open set.

## Conditional Finite-Jet Theorem

Let a compatible jet of sufficient order for (1)-(2) be given at a point p,
with commuting coordinate derivatives. Suppose, exactly at p,

```text
E^a_nu = delta^a_nu,  partial_r E^a_nu = 0,
F=R=FE=0,  R1=0,  FE1=0,
partial_i F^a_mu = 0 for every spatial i and every a,mu,
partial_mu F^a_0 = 0 for every a,mu,
F2=0 in all derivative directions and all constitutive components,
lambda_a^k = 0 for spatial k.
```

No derivative of lambda is assumed zero. Write

```text
X_ai = partial_0 F^a_i = J^a_0,i,
ell_a = lambda_a^0,
L_ja = partial_j lambda_a^0,
D_ji = sum_mu FE2[j,mu,i,mu],
M = [ ell.T ; L_1 ; L_2 ; L_3 ].                         (3)
```

The internal row `a=i` in D comes from `E^a_i=delta^a_i`, not from a metric
contraction. The repeated coordinate `mu` runs over **all four** directions:
`D_ji = FE2[j,0,i,0] + sum_k FE2[j,k,i,k]`. Thus these are nine spatial
derivatives of full Euler divergences, not divergences restricted to spatial
mu. In code, `FE1[r,a,mu]=partial_r FE_a^mu`, so the contraction is the
second-order counterpart of `einsum("mam->a", FE1)`.

Then (1), with `nu=i`, implies

```text
sum_a ell_a X_ai = 0,                                    (4)
```

and (2), with `r=j, nu=i`, implies

```text
D_ji + sum_a L_ja X_ai = 0.                              (5)
```

Indeed `J^a_k,i=0`, while `J^a_0,i=X_ai`; the derivative of the curl
vanishes by full `F2=0`. The term `(partial_j F^a_i) div(lambda_a)` vanishes
by the spatial F1 hypothesis. The coframe product terms vanish by `dE=0`
and `FE=0`, and the probe product terms vanish by `R=R1=0`.

Consequently, if all nine `D_ji` vanish and `M` is invertible, then for each
spatial i,

```text
M (X_0i,X_1i,X_2i,X_3i).T = 0,
```

so `X=0`. This proves the claimed conditional theorem. No second probe
derivative is needed. In fact only the three spatial `R1[j]` are needed in
this proof; temporal `R1[0]` is unused. Full `FE2=0` is sufficient but
stronger than the nine conditions `D_ji=0`.

The listed hypotheses are sufficient, not minimal. With `F2=0`, the spatial
equations (4)-(5) do not themselves require zero spatial multiplier values:
their other curls already vanish. Those values are retained here to match
the proposed fixed point and simplify the source formula below. They must
not be interpreted as vanishing multiplier derivatives or as vanishing
spatial multiplier columns throughout a neighborhood.

## If F2, R1, or FE1 Is Retained

Keep `E=I,dE=0,F=R=FE=0`, the stated F1 restrictions, and zero spatial
multiplier values, but now allow `F2,R1,FE1` to be nonzero. Define

```text
b_i = sum_mu FE1[mu,i,mu],
T_ji = sum_a ell_a (F2[j,0,a,i] - F2[j,i,a,0]),
P_ji = 2 Re sum_A conjugate(partial_i psi_A) R1[j]_A.
```

The exact equations are then

```text
sum_a ell_a X_ai = -b_i,
D_ji + sum_a L_ja X_ai + T_ji - P_ji = 0,

M X_i = (-b_i,
         -D_1i - T_1i + P_1i,
         -D_2i - T_2i + P_2i,
         -D_3i - T_3i + P_3i).T.                         (6)
```

These formulas give the source contractions and signs without suppressing
any nonzero source. In particular:

- Nonzero F2 can balance `L X` through T, even if all D vanish. Full F2=0
  is stronger than necessary; only the nine contractions T need vanish.
- Nonzero spatial R1 can balance `L X` through P. The source uses the
  first spinor derivative paired with R1, not a spinor Hessian paired with
  R2. If R itself were nonzero, the additional Hessian-times-R term in (2)
  would also remain.
- Nonzero FE1 changes the undifferentiated row through b. At this normal
  point it contributes no separate product term to (5), because every such
  term has a factor dE. Only `b=0`, rather than all FE1=0, is needed for
  the first row of the homogeneous gate.

Thus invertibility alone determines X from the source vector in (6); it
forces X=0 only when that vector vanishes. If the spatial F1 restrictions
are also relaxed, the full extra terms in (1)-(2), including
`(partial_j F^a_i) div(lambda_a)` and spatial curls, must be restored.

## Bounded Numerical Check

A read-only import with bytecode writing disabled loaded
`HC_Cartan_Constitutive_First_Closure.neighborhood.load_data()`. No affine
continuation or large linear solve was run. With the loader's names,

```text
ell = point["multiplier"][:,0]
L   = point["multiplier_first"][1:,:,0]
M   = vstack((ell,L))
```

Here the derivative direction is the first index of `multiplier_first`;
the last index is its coordinate vector index. The loaded floating matrix,
rounded for display, is

```text
M = [ 0.0100000000000000  0.0200000000000000 -0.0300000000000000  0.0400000000000000
     -0.2045241655696958 -0.1019584398471559 -0.5167017728758491  0.0023467144244680
      0.4988498067135351  0.7374757134687321  0.1303079875601946  0.0070152656388749
     -0.0111552056646192 -0.0972368158289423  0.2443811230494329 -0.0242806315896344 ].

singular values = (0.9544357315957098, 0.5374890896196485,
                   0.0440097075602066, 0.0086607090318710)
determinant     = 0.0001955321941569791.
```

These reproduce the reported scales and support numerical invertibility in
the stored coordinates. They are not an exact or interval certificate for
the underlying jet, its residual equalities, or a neighborhood rank bound.
The theorem assumes exact hypotheses independently of this calculation.

## Continuation Obstruction and Limits

The [first-closure witnesses](HC_Cartan_Constitutive_First_Closure.md) retain
the multiplier value and all spatial multiplier first derivatives, so the
matrix M is fixed. Conditional on exact counterparts of those lower
equations and an invertible M, a nonzero-X witness cannot extend to a
compatible higher jet satisfying both full F2=0 and the nine D=0 equations
while retaining R1=FE1=0 and the other stated hypotheses. Adjusting other
higher coefficients cannot cancel (4)-(5) once those sources are zero.
R2 is unnecessary for this exclusion, even if a parent continuation also
chooses to impose it. The floating witnesses satisfy lower equations only
to numerical tolerance; this exact statement is not an exact certification
of those stored witnesses.

This does not exclude FE2 continuations when F2 is allowed to supply T,
nor establish that F2=0 follows from earlier equations. It does not show
that any X=0 continuation exists or that all remaining prolongation
conditions are compatible. If spatial lower multiplier data change, M
must be reassessed; if it is singular, the gate alone permits columns of
X in its kernel. No evolution equation, initial-data uniqueness argument,
regional persistence of the hypotheses, or closed subsidiary system is
proved. The result is a conditional obstruction at one finite jet, not
full constitutive or gravitational constraint propagation.
