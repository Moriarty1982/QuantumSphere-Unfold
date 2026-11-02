# Normal Spinor Hessian Gate: Analytic Polynomial Structure

Date: 2026-10-18. Independent source-reading derivation for the implemented
finite residual. No Python modules were imported, numerical matrices assembled,
saved reports validated, or numerical checks run. Numerical verification belongs
to the main agent.

## Verdict and Definition of the Problem

For fixed `prepared`, fixed lower `point` (including a chosen normal-source
shift), fixed prescribed coordinates, and fixed matching LC cubic, the actual
`full_residual(...)["vector"]` has the form

    F(p,w) = b + J p + Q(p) + A w,
    p in R^96, w in R^1168, F in R^1114.

Here A and J are constant real matrices and Q is homogeneous quadratic.
In particular, A is independent of p. There are no p*w, w*w, or higher-degree
terms. All quadratic terms are in the final 320 C3 rows. This is an exact
algebraic statement about the displayed analytic evaluator, interpreted in
exact arithmetic, rather than a numerical rank or existence claim.

Define coordinates about any one consistently chosen baseline `(c_*,h_*)`:

    c(p,w) = c_* + I_p p + I_old w_old,
    h(w)   = h_* + I_high w_high,
    F(p,w) = evaluate_fields(prepared, point, c(p,w), h(w), lc)["vector"].

`I_p` inserts into the normal-containing psi2 entries from
`source.allowed_cauchy_coordinates()["psi2"]`. `I_old` inserts into exactly
the `older` list of `_reprepare_matrix`; `I_high` uses `highest_mask()` in
the order E4, lambda3, psi4. Increments in frozen slots are zero; their
absolute baseline values need not be zero. The split is:

| Variable | Allowed derivative tuples | Real count |
| --- | --- | ---: |
| p: psi2 | pairs containing 0 | 96 |
| w_old: lambda2 | pairs containing 0 | 64 |
| w_old: E3 | triples with at least two zeros | 64 |
| w_old: psi3 | triples containing 0 | 240 |
| w_high: E4 | quartets with at least two zeros | 160 |
| w_high: lambda3 | triples containing 0 | 160 |
| w_high: psi4 | quartets containing 0 | 480 |
| Total w | | 1168 |

The 1200 earlier coordinates use whole-block realification for psi2 and
psi3. The 1720 highest coordinates use 560 E4, 320 lambda3, and 35 groups
of 24 psi4 entries; each psi4 group has 12 real then 12 imaginary entries.
Symmetric unpacking copies derivatives without factorial factors. These
are linear insertions, so these packing choices preserve polynomial degree.

## Analytic Dependencies

The relevant call chain is `HC_Cartan_Cauchy_Next_Completion.evaluate_fields`
to `HC_Cartan_Next_Joint_Completion.full_residual`. The latter concatenates
old394, packed R2 (240), packed FE2 (160), and full C3 (320). It does not
project C3 onto the smaller complement used by `joint_vector` in other
solvers. The dependencies inspected for this derivation are:

- `HC_Cartan_Normal_Source_Compatibility.allowed_cauchy_coordinates`.
- `HC_Cartan_Regular_Gravity.unpack`, `connection_second`, and `equations`.
- `HC_Cartan_Spatial_Propagation.connection_first` and `first_probe`.
- `HC_Cartan_Next_Scalar_Compatibility.covariant_jets` and `scalar_jet`.
- `HC_Cartan_Third_Constraint_Reprepare.bilinear_third`, `lc_cubic`,
  `connection_third`, `constraint_third`, and `old_equations`.
- `HC_Cartan_Second_Probe_Affine.weight_jets` and `probe_second`.
- `HC_Cartan_Second_Gravity_Affine.highest_delta_omega3`,
  `curvature_second`, `normal_frame_response`, and `coframe_euler_second`.
- `HC_Cartan_Third_Constraint_Diagnostic.connection_image` and
  `principal_image`.
- `HC_Cartan_Prolongation.prepare`, `HC_Cartan_Compatible_Jets` packing,
  and `HC_Gauge_Invariant_Geometry_Readouts.pairing`.

## Connection Derivatives Are Jointly Affine

Write P=psi2, L=lambda2, T=E3, U=psi3. Lower psi, psi1, E2, lambda0,
lambda1 and all prepared forms are fixed. The Cartan Hessian H and its
inverse in `prepared` are fixed; no inverse depending on P is evaluated.
`connection_first` depends only on the lower point, so omega0 and omega1
are constant in both p and w.

In `connection_second`, `source_second` and `response_second` are affine
in P. Their other terms contain only fixed psi1 and E2. `hessian_second`
depends only on E2. The RHS is

    -source_second + response_second * lambda0
    + response_first * lambda1 (two placements)
    + L * prepared.response - hessian_second * k0.

Every factor paired with a variable term is fixed. Applying H inverse and
adding the LC linear image of T gives

    omega2 = constant + linear(P,L,T).

In `connection_third`, `bilinear_third` contains psi*U and the three
psi1*P placements. Its geometric additions contain T times fixed source
data and E2 times fixed source1 data. Thus source3 and response3 are
jointly affine in P,T,U. Also h3 is linear in T, whereas h2 and k1 are
fixed. The remaining products are

    response3 * lambda0, h3 * k0,
    response_second(P) * lambda1,
    response_first * L, h2 * k1.

None pairs two variable factors. Consequently omega3 is jointly affine in
P,L,T,U. `highest_delta_omega3` adds a constant linear map of E4/lambda3.
The LC cubic used here is a function of fixed E2, independent of E3 and P.

## Residual Blocks and the Only Quadratic Term

Let B_j denote the spin lift of omega_j. With derivative and connection
indices made explicit, the covariant jets used in these routines satisfy

    d0_mu       = fixed,
    d1_r,mu     = P_r,mu + fixed,
    d2_rs,mu    = U_rs,mu + B2_rs,mu psi
                  + B1_r,mu psi1_s + B1_s,mu psi1_r + B0_mu P_rs.

Thus d2 is jointly affine in P,L,T,U. The d3 expression in
`constraint_third` contains B3*psi, B0*U, and the three placements of
B1*P and B2*psi1. It is jointly affine as well. In particular d1 has no
w dependence, even though d2 and d3 do.

**Old394.** C1, R1, FE1, and C2 are jointly affine: their variable
covariant jets are paired only with fixed psi or psi1, and P in C2 is
paired with fixed d0. The extra ten scalar-Hessian rows are affine too:
`lambda_second` is L times fixed t0, `lambda_first_cross` is fixed
lambda1 times affine t1(P), and `lambda_value_cross_second` is fixed
lambda0 times affine t2(P,L,T,U). There is no L*t1 product.

**R2.** In `weight_jets`, W0 and W1 are fixed, W2 is affine in L, and
W3 is linear in T/lambda3. In `probe_second`, the possibly variable
factors occur as W2*d0, W1*d1, W0*d2, Z2*psi, Z1*psi1, and Z0*P.
Here d0, W1, W0, psi, psi1, and Z0 are fixed. Z2 is affine through
B2, W2, and W3; Z1 is affine through W2. The apparently dangerous
W2*d1 product is absent. R2 is jointly affine.

**FE2.** `curvature_second` contains omega3 linearly, omega2 times
fixed omega0, and omega1 times omega1, with both omega1 factors fixed.
Its matter terms are pair(P,d0), pair(psi1,d1), pair(psi,d2), and an
affine mass Hessian. The frame-response inputs E2, x0, mass0, and R0
are fixed. FE2 is jointly affine.

**C3.** `constraint_third` evaluates

    Im { pair(U_rst,d0,Q) + pair(psi,d3_rst,Q)
         + sum_(i,j,k) [pair(psi1_i,d2_jk,Q)
                        + pair(P_jk,d1_i,Q)] } - T_rst,

where the three placements are `(r,s,t)`, `(s,r,t)`, `(t,r,s)`.
All but the last pairing are jointly affine. For a tensor X define
`X_i` to mean the four-entry derivative array `mu -> X_i,mu`. The
homogeneous quadratic part in the full P tensor is exactly

    Q_full(P)_rst = Im sum_(i,j,k) pair(P_jk, P_i, Q).

If V(p) is the symmetric normal-only psi2 tensor inserted by I_p, then
the quadratic term about the chosen baseline is

    Q(p) = (zeros(794), Q_full(V(p)).reshape(-1)).

All baseline cross terms from P_*+V(p) are linear in p and belong to J.
Using the actual pairing implementation, each output component is

    Q_full(V)_rst,a,mu
      = Im sum_(i,j,k) vdot(V_jk, (Q @ V_i,mu) @ weight_a.T).

This formula includes multiplicities for repeated indices, just as the
three-term loop does. For example, the `(r,s,t)=(0,0,0)` row contains

    3 Im vdot(V_00, (Q @ V_0,mu) @ weight_a.T).

For spatial mu this displays possible bilinear coupling between the
normal-containing Hessian slots 00 and 0mu. These are p*p terms, not
p*w terms. Individual components can vanish or cancel; the expression
does not assert a nonzero coefficient or a rank for every component.

**Highest additions.** `connection_image` and `principal_image` depend
on the fixed prepared psi and fixed response/H inverse, not on P.
The R2 lambda3 contribution also multiplies fixed psi. Thus all highest
columns are constant, including after restriction to the Cauchy mask.

There are consequently no actual p*w mixed terms to list for this scope.
In particular `response_second(P)*lambda1` cannot produce one because
lambda1 is fixed, and `pair(P_jk,d1_i,Q)` cannot produce one because
d1_i contains no w. The fixed-psi2 affinity comments in existing solvers
are sufficient for their use, but weaker than this joint conclusion.

## Hessian Gate and Numerical Verification Contract

Let L have columns spanning ker(A.T), with A the full 1114 by 1168 map.
In exact finite-dimensional linear algebra, existence of w for a given p
is equivalent to

    g(p) = L.T (b + J p + Q(p)) = 0.

The same L works for every p in this fixed problem. If desired, write
`Q(p) = (1/2) H[p,p]`. For directions u,v, the only potentially nonzero
rows of H are C3, where

    H[u,v]_rst
      = Im sum_(i,j,k) {pair(V(u)_jk, V(v)_i, Q)
                       + pair(V(v)_jk, V(u)_i, Q)}.

The gate Hessian is L.T H. Its nonzero entries, rank, null directions,
and solvability are separate numerical or symbolic questions. Projection
can annihilate some or all of the displayed quadratic tensor.

Useful independent numerical identities are constancy of w-column
differences across different p, zero rectangular differences in a p and
a w direction, zero second differences in w, and zero third differences
in p. The second difference in p should agree with the explicit C3
polarization above and vanish on the first 794 rows. Testing only p=0
would not establish constant A; source inspection supplies that argument.
No such numerical verification is claimed in this sidecar.

## Scope and Caveats

- This derivation freezes the six lower source values, lower point,
  prepared data, couplings, tangential coordinates, and LC cubic while
  varying p and w. Repreparing the lower point as a function of p changes
  the problem and requires the corresponding chain-rule terms.
- Varying lower psi1, E2, lambda0, or lambda1 can make previously fixed
  factors variable. For example the displayed response_second*lambda1
  and curvature omega1*omega1 products then require renewed analysis.
  No constant-matrix statement over that larger family is made here.
- The normal-point convention E=I, E1=0 and the fixed regular Cartan
  inverse are those of these analytic routines. This is not a derivation
  of a general-coordinate residual formula.
- A must use all 1114 rows and the actual 1168-column mask. Restricting
  columns can change its cokernel; the complement or ranks from other
  completions cannot be substituted without proof. The source-based
  degree argument itself also holds before this coordinate restriction.
- Saved input matching, floating-point cancellation, rank cutoffs,
  conditioning, numerical tolerances, and agreement of the assembled
  highest map with direct residual changes remain to be checked by the
  main agent. A finite-difference response matrix is only a numerical
  representation of the constant analytic A proved here.
- Polynomial structure and gate equivalence provide no solution of g=0,
  no rank certificate, no nonexistence conclusion, no regional Cauchy
  evolution or formal integrability theorem, and no native-action or
  physical identification.
