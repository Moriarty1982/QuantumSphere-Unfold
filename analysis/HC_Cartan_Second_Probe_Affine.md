# Analytic second probe at the normal point

The new `probe_second(prepared, point, jets, lambda_third=None)` returns the
full complex `(4,4,12)` tensor of unnormalized second coordinate derivatives.
It uses `regular.connection_second` directly, with the existing lower point,
couplings and `jets` keys `p2,l2,e3,p3`. No finite differences enter this function.
The implicit point convention is `E=I,E1=0`; this is not a general-point formula.

`lambda_third` accepts either 320 real coordinates, packed in the existing
lexicographic `prolong.PAIR3` order followed by `(a,mu)`, or a full real tensor
`(4,4,4,4,4)` symmetric in its first three axes. The default is zero.
The existing `e3` and `p3` coordinates remain variable, rather than being frozen
or counted as new freedoms. `lambda3` supplies 320 new coordinates.

## Product differentiation

Write `B_mu` for the lifted spin connection, `D_mu=psi_mu+B_mu psi`,
`v=abs(det E)`, `K_a=FLAT_WEIGHTS[a]`, `A_a=Q_WEIGHTS[a]`, and
`W^mu=v inverse(E)[mu,a] K_a+lambda[a,mu] A_a`. The complete real law is

```
R = i sum_mu W^mu D_mu - v M psi + (i/2) Z psi
Z = sum_mu (partial_mu W^mu - B_mu^dagger W^mu - W^mu B_mu).
```

At the normal point, `v1=inverse(E)1=0`. For derivative multi-indices
`J=(r,s)` or `(r,s,t)`,

```
v_J = trace(E_J)
W_J^mu = trace(E_J) K_mu - sum_a E_J[mu,a] K_a
         + sum_a lambda_J[a,mu] A_a.
```

Thus `W2` uses `E2,lambda2`, and `W3` uses `E3,lambda3`. There are no
`E2*E2` terms at derivative order three when `E1=0`. In particular,
`div(W)2[r,s]=sum_mu W3[r,s,mu,mu]`.

The implementation differentiates both matrix products in `Z` twice,
retaining all eight connection/weight terms. With subscripts denoting
ordinary derivatives, the final formula is

```
D_rs,mu = psi_rs,mu + B_rs,mu psi + B_r,mu psi_s
          + B_s,mu psi_r + B_mu psi_rs
R_rs = i sum_mu (W_rs^mu D_mu + W_r^mu D_s,mu
                 + W_s^mu D_r,mu + W^mu D_rs,mu)
       - M (psi_rs + trace(E_rs) psi)
       + (i/2) (Z_rs psi + Z_r psi_s + Z_s psi_r + Z psi_rs).
```

With the lower point and `p2` fixed, this is affine in `l2,e3,p3,lambda3`:
`B0,B1,D0,D1,W0,W1,Z0` are fixed; `B2,W2,W3,Z1,Z2,D2` are affine,
and no two variable factors multiply. The exact new principal term is
`delta R_rs = (i/2) sum_(mu,a) lambda3[r,s,mu,a,mu] A_a psi`.

## Focused validation

On 2026-10-18 the following command passed all five tests in 1.624 seconds:

```
python -m unittest scripts.qsc_audit.tests.test_hc_cartan_second_probe_affine -v
```

- Full complex tensor comparison with the existing frozen `lambda3=0`
  Second_Probe_Diagnostic JSON (`atol=2e-6,rtol=2e-8`).
- Independent central differences of displaced polynomial fields with random
  `l2,e3,p3` and nonzero `lambda3`. Cartan is solved anew at each sample;
  Richardson comparison uses `atol=3e-5,rtol=1e-7`, with a separate second-order
  convergence check on steps `2e-4` and `1e-4`.
- Affinity under simultaneous random variations of all 1280 allowed real
  coordinates, holding `p2` fixed.
- Packed/full `lambda3` equality, its exact principal term, and invalid-input
  rejection.
- Twice-differentiated existing NextScalar off-shell identity, including
  spinor contraction product rules and the second derivative of `v inverse(E).T`.
  The absolute identity residual tolerance is `2e-9`.

This supplies an analytic residual evaluator, not a solved R2 extension
system, rank calculation, Cauchy construction or local-existence claim.
Only the three new sidecar files were edited; no full suite or git operations
were run.

## Source fingerprints

SHA256 of raw file bytes at validation time (paths relative to repository root):

```
analysis/HC_Cartan_Second_Probe_Affine.py
2D2F8ABD51F13F2F0B56CA04ADD9ECFB4AA3FF749FE6F4372203A31CEC5787F9
scripts/qsc_audit/tests/test_hc_cartan_second_probe_affine.py
D37BAC2475358FB482A55B3BD9C4E773CF38ACBE51C70FAF4F8EC0B9C1E64AD5
analysis/HC_Cartan_Regular_Gravity.py
89CF5597FC935D463EED604F9C9EB247CDA17B576AE294DBFAD6E45DACBC063F
analysis/HC_Cartan_Spatial_Propagation.py
1EAA40763D84F28DFB0846032A96DA28DD18AB8080CDC2A400C82827EB21FEAF
analysis/HC_Cartan_Next_Scalar_Compatibility.py
916E412E18312E7AC72583029A3A2435B6CB4197B19BD5F49E4713B4CC5DCFBC
analysis/HC_Probe_Law_Revision_Audit.py
DAC01938BA5A92DBC55C7547E49BEAAA9C70734C81A9986E04EED7BD66C65123
analysis/HC_Cartan_Second_Probe_Diagnostic.json
5634E664DD8569289029B7FDBA5735EFF5B106B58B935C37AF4C0F348877DBA9
analysis/HC_Cartan_Next_Scalar_Compatibility.json
9D3A8191EABF668FBBCE0BD81D3BA01BDFD6BF926C293C15BB62B2D574867C0F
```
