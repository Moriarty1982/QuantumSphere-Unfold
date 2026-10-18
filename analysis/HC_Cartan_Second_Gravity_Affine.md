# Analytic independent-coframe Euler Hessian

`coframe_euler_second(prepared, point, jets, *, e4=None, l3=None,
omega3=None, lc_third=None)` returns real `FE2[r,s,a,mu]`, shape `(4,4,4,4)`.
`gravity_second` is an alias. These are unnormalized coordinate derivatives.
The formula assumes the existing normal point `E=I,E1=0`, Einstein coefficient
one and vacuum zero, and differentiates `HC_Cross_Cartan_Parent.coframe_euler`.
It is the independent coframe variation evaluated on the Cartan branch.
It is not a variation of a substituted metric Levi-Civita Einstein tensor.

The lower point, `E2` and `psi2` remain fixed. The old `l2,e3,p3` stay variable;
new `e4` has shape `(35,4,4)` and new `l3` shape `(20,4,4)`. Unique derivative
indices use the existing lexicographic QUADS/TRIPLES order, followed by `(a,mu)`.
Both new tensors default to zero. The optional `omega3` is an absolute full
third connection derivative of shape `(4,4,4,4,4,4)`, not a delta, and excludes
simultaneous `e4`/`l3` arguments. The caller may cache
`third.lc_cubic(prepared,point)` in `lc_third`, excluding the E4 contribution.

## Derivation

Let `J=E^-1`, `v=abs(det E)`, `X=Im pairing(psi,D psi)`, and
`m=Re <psi,M psi beta.T>`. The matter part of the independent Euler density is

```
Ld = v (-sum(J.T * X) - m)
Fm = Ld J.T + v (J X J).T.
```

At the normal point `J1=v1=0`. The second Euler derivative therefore separates
into the normal-point linear expression in `X2,m2,R2,lambda2` and the derivative
of the Euler expression with respect to the frame in direction `H=E2[r,s]`:

```
FE2[r,s] = (-trace(X2[r,s])-m2[r,s]) I + X2[r,s].T
           + gravity_euler(R2[r,s]) + lambda2[r,s]
           + frame_response(H; X0,m0,R0).
```

The response is evaluated at fixed `X,m,R`; writing `j=-H`, `v'=trace(H)`,

```
Ld0 = -trace(X)-m
Ld' = v' Ld0 - sum(j.T * X)
Fm' = Ld' I + Ld0 j.T + v' X.T + (j X + X j).T.
```

For gravity define `C(A,B)=sum A[mu,a] B[nu,b] R[mu,nu,a,b]` and
`Lg0=C(I,I)/2`. For each output component `(a,nu)`, let
`dJ=-outer(I[:,a],I[nu,:])` and
`dJ'=-outer(j[:,a],I[nu,:])-outer(I[:,a],j[nu,:])`. Then

```
Lg' = v' Lg0 + (C(j,I)+C(I,j))/2
dr = C(dJ,I)+C(I,dJ)
dr' = C(dJ',I)+C(dJ,j)+C(j,dJ)+C(I,dJ')
Fg' = Lg' I + Lg0 j.T + (v' dr + dr')/2  [componentwise last term].
```

This retains both the volume and inverse-frame second responses multiplying
the undifferentiated curvature. They cannot be omitted even if `R2=0`.

`X2` uses the complete bilinear product rule:
`Im(pair(psi2,D0)+pair(psi1_r,D1_s)+pair(psi1_s,D1_r)+pair(psi,D2))`.
The mass Hessian is
`2 Re <psi,M psi2 beta.T> + 2 Re <psi1_r,M psi1_s beta.T>`.

For `A_mu=eta omega_mu`, upper curvature is
`R_mu,nu=([A_mu,A_nu]+eta(partial_mu omega_nu-partial_nu omega_mu)) eta`.
`curvature_second` differentiates this expression directly: each ordered
connection product contributes its four second-product-rule terms, and the
curl term uses `omega3[r,s,mu,nu]-omega3[r,s,nu,mu]`.

The default connection comes from `third.connection_third` with its analytic
`lc_cubic`, including the fixed nonlinear E2 contributions. The added highest
connection derivative is

```
delta omega3[r,s,t] = normal_lorentz(E4[r,s,t,:,:,:])
                     + unpack(H0^-1 L0.T lambda3[r,s,t]).
```

It uses the same prepared Hessian, response and LC linear map as the parent.
No new couplings, lower-point changes or finite-difference matrices enter.
With E2 and psi2 fixed, omega0,omega1 are fixed, omega2 and omega3 are affine
in the allowed variables, and every product above has at most one variable
factor. FE2 is consequently affine in all 1840 coordinates
`l2(160),e3(320),p3(480),E4(560),lambda3(320)`.

## Focused validation

On 2026-10-18 all six relocated focused tests passed in 4.921 seconds:

```
python -m unittest scripts.qsc_audit.tests.test_hc_cartan_second_gravity_affine -v
```

- Independent direct `coframe_euler` on polynomial E,psi,lambda and cubic
  omega fields, with exact polynomial first connection derivatives and random
  nonzero E4/lambda3: full FE2 Richardson error `7.857617717576296e-06`.
  Steps are `2e-4,1e-4`; the test also checks second-order convergence,
  derivative-axis symmetry, real output and full-omega3 override equality.
- Actual eliminated-Cartan Taylor fields through existing `regular.field_euler`,
  with its inner connection-difference step `2e-6`, give full symmetric tensor
  errors `1.9176193650508422` at outer step `1e-3` and `0.47888705329367914`
  at `5e-4`. The reduction ratio is approximately four. Richardson error is
  `0.03365933975234388`, within the loose absolute norm threshold `0.1`.
  That threshold applies to the extrapolated tensor; the raw fine difference
  has error approximately `0.479`. This control retains its nested-FD noise.
- Curvature Hessian compared independently against polynomial connection
  curvature, including every connection-product term.
- Random independent frame variations of the actual parent coframe Euler
  expression, with both matter plus gravity and pure gravity. The nonzero
  E2-curvature response is explicitly checked.
- Simultaneous random affine combinations across all 1840 allowed coordinates,
  holding psi2 fixed.
- Ambiguous highest-jet override and invalid E4 shape rejection.

Only the new module, this note and `scripts/qsc_audit/tests/test_hc_cartan_second_gravity_affine.py`
were edited. No full suite, git operations, joint solve or rank calculation
was performed. The polynomial control tests the Euler differentiation tightly;
the actual-field comparison independently checks its use of the inherited
analytic third connection to the stated looser numerical tolerance.

## Source fingerprints

SHA256 of raw bytes at validation time, paths relative to repository root:

```
analysis/HC_Cartan_Second_Gravity_Affine.py
663AD2FF16C8BC687F8CD366F649BD83A9CD31BAAFFF532E6FA481B34394B46C
scripts/qsc_audit/tests/test_hc_cartan_second_gravity_affine.py
8781902119B4EC37E3897BA37005414F1587077A07FD0E9FBBD9373C1D9597AB
analysis/HC_Cartan_Third_Constraint_Reprepare.py
8E91386218BF8372C4F7329F7825B1443EAB018FE9DC65A1513C10C56A87D9C0
analysis/HC_Cross_Cartan_Parent.py
0FFA49D95232DAF76EA8A49B6E5F4D87B6E496CE6EBFD1C05DC0A7128708866F
analysis/HC_Cartan_Regular_Gravity.py
89CF5597FC935D463EED604F9C9EB247CDA17B576AE294DBFAD6E45DACBC063F
analysis/HC_Cartan_Next_Scalar_Compatibility.json
9D3A8191EABF668FBBCE0BD81D3BA01BDFD6BF926C293C15BB62B2D574867C0F
```
