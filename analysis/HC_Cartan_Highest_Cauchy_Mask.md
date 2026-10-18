# Next-Order Highest-Jet Tangential Cauchy Mask

Date: 2026-10-18. Independent bounded source-reading derivation. No modules
were imported or executed, matrices assembled, numerical ranks inferred,
saved reports validated, or test suites run. The parent owns the actual
1114-row completion, input matching, numerical gates, and residual checks.

## Fixed-Witness Problem

Start with the matching `(prepared, point, jets, extras, report)` described
by `HC_Cartan_Joint_Neighborhood.load_data()`. That loader checks the current
joint report's source and scalar-completion fingerprints and retained psi2;
reading those checks here does not execute them. The saved joint report
supplies the baseline highest coefficients as well as its earlier jets.
Do not combine its extras with jets from an older completion loader.

For the parent's chosen fixed source shift q, form the shifted lower point
`point_q` and a chosen 384-row lifted witness `jets_*`. Its packed coordinate
vector is `c_*`, of length 1200, with blocks psi2/lambda2/E3/psi3. If the
earlier lift was z relative to the matching report, then
`c_* = report["jet_coordinates"] + z`. Freeze all four blocks in the first
problem, including their mixed normal entries. Freeze q, prepared data,
couplings, and all other lower coefficients as well.

Recompute `lc_* = third.lc_cubic(prepared, point_q)` for the shifted point.
This cache excludes E4; using the unshifted LC cubic would change the
problem. Let `b_*` be the matching report's 880 connection coordinates and
`p_*` its `(35,24)` fourth-spinor array. Define a new 1720-real-coordinate
increment v by the packing below and evaluate

    F_*(v) = joint.full_residual(
        prepared, point_q, c_*,
        b_* + v[:880], p_* + v[880:].reshape(35,24), lc_*)["vector"].

The additions are increments about saved highest coefficients. Freezing a
coordinate means zero increment, not replacing its saved coefficient by
zero. An independently constructed, consistently matched highest baseline
can be used instead, provided the same baseline defines F_*(0).

The sources establishing the conventions and dependencies are
`HC_Cartan_Normal_Source_Compatibility.py`, its `_Derivation.md`,
`HC_Cartan_Source_Cauchy_Jet_Mask.md`,
`HC_Cartan_Next_Joint_Completion.py`,
`HC_Cartan_Third_Constraint_Diagnostic.py`, and
`HC_Cartan_Second_Gravity_Affine.py`. Supporting definitions were read in
`Third_Constraint_Reprepare`, `Second_Probe_Affine`, `Joint_Neighborhood`,
`Regular_Gravity`, `Compatible_Jets`, and `Prolongation`, all with the
`HC_Cartan_` prefix.

## Packing and Exact Coordinate Sets

Use t=x^0 and spatial derivative indices 1,2,3. Let T3 and T4 be
`combinations_with_replacement(range(4),3)` and the analogous quartets,
in lexicographic order: 20 triples and 35 quartets. All indices below are
zero-based; intervals are half-open. Only derivative indices determine
normal multiplicity, never a trailing field-component index.

| Block in v | Shape of unique entries | Slice | Real dimension |
| --- | --- | --- | ---: |
| delta E4 | (35,4,4), real | [0,560) | 560 |
| delta lambda3 | (20,4,4), real | [560,880) | 320 |
| delta psi4 | (35,24), realified per quartet | [880,1720) | 840 |

For real tensor components j=4*a+mu, the E4 coordinate is `16*k+j`
and the lambda3 coordinate is `560+16*l+j`, with k in T4 and l in T3.
For psi4 set j=4*channel+spinor_component, 0 <= j < 12:

    real part:       880 + 24*k + j
    imaginary part:  880 + 24*k + 12 + j.

This is the convention of `diagnostic.principal_image` and the report's
`fourth_spinor_real`: each quartet has its own 12 real then 12 imaginary
entries. It is NOT `prior.realify` applied to the whole `(35,3,4)` tensor,
which would place all 420 real entries before all 420 imaginary entries.
Earlier psi2 and psi3 DO use whole-block realification. The difference
must be respected when constructing a combined coordinate vector.

The unpackers copy unique derivatives into symmetric slots with no
factorial scaling. Taylor factors belong to field evaluation, not to the
increment vector. Permutations are not additional coordinates. Euclidean
coordinate norms are unweighted and need not equal full-tensor norms.

## Derivation of the Trace-Preserving Mask

Preserve the represented tangential germs of E|, E_t|, psi|, and lambda|
on t=0. Here E_t means the coordinate derivative partial_0 E, as in the
earlier mask. At this next represented order those germs fix

    E_ijkl, E_0ijk, psi_ijkl, lambda_ijk,  i,j,k,l in {1,2,3}.

Indeed restriction of a Taylor monomial to t=0 retains exactly terms with
no t factor. Applying partial_0 first and restricting retains exactly
terms with one t factor. Thus preserving both E| and E_t| requires at
least two normal indices in every allowed E4 increment. For psi and
lambda only their value traces are frozen, so at least one normal index
suffices. Neither psi_t| nor lambda_t| is an additional frozen trace.

| Block | Allowed derivative tuples | Tuple count | Allowed real count | Fixed real count |
| --- | --- | ---: | ---: | ---: |
| E4 | quartets with at least two zeros | 10 | 160 | 400 |
| lambda3 | triples with at least one zero | 10 | 160 | 160 |
| psi4 | quartets with at least one zero | 20 | 480 | 360 |
| Total | | | 800 | 920 |

For E4 the allowed quartets are

    0000, 0001, 0002, 0003, 0011, 0012, 0013, 0022, 0023, 0033.

They are T4 indices 0 through 9. The forbidden quartets are ten with
exactly one zero (tangential third derivatives of E_t|) and fifteen
all-spatial quartets (tangential fourth derivatives of E|).

The allowed lambda3 triples, T3 indices 0 through 9, are

    000, 001, 002, 003, 011, 012, 013, 022, 023, 033.

The allowed psi4 quartets are T4 indices 0 through 19: the ten E4 tuples
above, followed by

    0111, 0112, 0113, 0122, 0123, 0133, 0222, 0223, 0233, 0333.

Equivalently, the exact highest-coordinate masks in v are

    full:       [0,1720)
    tangential: [0,160) union [560,720) union [880,1360)
    fixed complement:
                [160,560) union [720,880) union [1360,1720).

The counts follow directly from symmetric tuples in three spatial
variables: 35-15-10=10 allowed E4 tuples, 20-10=10 allowed lambda3 tuples,
and 35-15=20 allowed psi4 tuples. These are coordinate counts, not ranks.

The highest mask preserves traces relative to the frozen witness and
highest baseline. To preserve the original matching report's entire
represented tangential germ, the earlier lift z must itself have obeyed
the earlier 464-coordinate Cauchy mask, and the lower source shift must
preserve the lower trace coefficients. The displayed six-source chart
changes E_00 and selected lambda_0 components and has that lower support.
If an unrestricted earlier lift already changed tangential coefficients,
this highest mask cannot undo those changes at lower degree.

## Highest Linearity and the Full Residual

At this fixed lower point and frozen earlier witness, source reading gives

    F_*(v) = f_* + T v,     f_* = F_*(0),
    T : R^1720 -> R^1114.

This is affinity in the new highest increments only. The implemented rows
and highest dependencies are

| Residual block | Real rows | Dependence on new highest increments |
| --- | ---: | --- |
| old | 394 | none |
| packed R2 | 240 | lambda3 only |
| packed FE2 | 160 | E4 and lambda3 |
| flattened C3 | 320 | E4, lambda3, psi4 |
| Total | 1114 | |

`old_equations` contains the earlier 384 rows PLUS the ten unique scalar
Hessian rows. `packed_probe` selects the ten derivative pairs and uses
whole-block realification; `packed_gravity` selects the same pairs and
flattens the real tensor. C3 uses `(triple,a,mu)` row order. Consequently
the matrix's first 394 rows are identically zero.

For E4/lambda3, `highest_delta_omega3` is linear, with coefficients fixed
by prepared data. FE2 inserts it into the linear omega3 term of the
curvature Hessian; the omega1*omega1 terms are frozen lower contributions.
The new lambda3 contribution to R2 is linear through w3 in `weight_jets`.
C3 adds the linear `diagnostic.connection_image` and
`diagnostic.principal_image`; psi4 enters neither R2 nor FE2 nor old.
Thus T depends on prepared data in these formulas, not on the chosen
earlier witness. Shifting lower jets changes f_*, and requires recomputing
the lower connections and LC cubic, but introduces no product with v.

A 384-row lift need not satisfy the additional ten scalar rows. Because
highest increments cannot change any old row, that possible obstruction
must remain in the full gate. Passing C1/R1/FE1/C2 alone is insufficient.

## Necessary and Sufficient Finite Gate

For either allowed set let M insert its coordinates into v and put

    T_M = T M,   columns(L_M) span ker(T_M.T).

The full problem has M=I_1720; the tangential problem has 800 columns.
For this frozen witness, existence of a highest lift is exactly

    exists u: f_* + T_M u = 0
        if and only if L_M.T f_* = 0.

Necessity is left multiplication; sufficiency follows from
`range(T_M) = ker(T_M.T)^perp`. If compatible, all solutions are

    u = -T_M^+ f_* + N_M a,   columns(N_M) span ker(T_M).

The solution dimension is `dim(u)-rank(T_M)` if nonempty. No numerical
value for that rank or the gate dimension is asserted here. Retain the
actual f_*, including any saved residual, rather than setting it to zero.
If incompatible, the pseudoinverse leaves residual
`(I-T_M T_M^+) f_*`; a nullspace correction cannot remove it.

Equivalently write `f_*=(o_*,s_*)` with 394 old and 720 new rows, and
`T_M=(0;D_M)`. Then the necessary and sufficient conditions are

    o_* = 0,   K_M.T s_* = 0,
    columns(K_M) span ker(D_M.T),
    D_full: R^1720 -> R^720,   D_tangential: R^800 -> R^720.

This explicitly separates the immovable old equations. Dimension counts
alone do not establish surjectivity. Masked compatibility implies full
compatibility; failure under the mask may disappear when tangential
highest increments are allowed. The converse implication is unavailable.

Do not substitute `highest_maps()["joint"]` for T_M: that implementation
has only the 880 connection columns and projects C3 onto a complement of
the unrestricted spinor image. It omits explicit psi4 columns. Its
unrestricted spinor elimination does not enforce the psi4 mask. A masked
elimination must use the actual allowed principal image, or retain all
320 C3 rows and the explicit masked columns as above. C3-only connection
completion likewise does not impose R2 and FE2.

## Freezing Earlier w Versus Re-Preparing It

Write the parent's earlier affine 384-row problem, at fixed q, as

    h_q + A_C y = 0,

where C inserts the earlier trace-preserving coordinates into the
1200-vector and `A_C=A C`. There are 464 such coordinates, packed as

    psi2:    [0,48) union [120,168)           (96)
    lambda2: [240,304)                       (64)
    E3:      [400,464)                       (64)
    psi3:    [720,840) union [960,1080)       (240).

If this earlier gate is compatible, choose one solution y0. Every earlier
trace-preserving 384-row lift is

    y = y0 + Z_C w,   columns(Z_C) span ker(A_C),
    dim(w) = 464 - rank(A_C).

Freezing the chosen earlier w fixes psi2/lambda2/E3/psi3, exactly the first
problem above. Its highest gate is a gate for that one witness. Failure
does not rule out a different earlier lift of the same fixed q.

Allowing all earlier mixed normal entries to re-prepare instead gives
the exact finite question

    exists w: L_M.T f(q,w) = 0,

where f(q,w) is the actual 1114-row residual at those earlier jets and
the same highest baseline. This includes the ten scalar rows as well as
the 384 rows already enforced by parameterization. The same T_M works
for each w. After such a w is found, the compatible highest solution is
`u=-T_M^+ f(q,w)+N_M a`. This existential gate is necessary and sufficient,
but in general is NOT a single jointly linear gate in (w,u).

In particular, all 464 earlier mask coordinates include 96 psi2 entries.
`constraint_third` contains `pair(p2[j,k], d1[i])`, with d1 containing p2.
These permit quadratic dependence on the earlier re-preparation. A fresh
cancellation proof would be needed to call a particular restricted family
affine. The joint fit's source-reading affinity fixes psi2 and does not
supply that proof. Nor does the earlier 384-row affinity in (q,z) extend
automatically to the later residual as q varies.

One can equivalently use raw 464 earlier increments delta y about the
chosen witness and solve

    F(prepared,point_q,c_*+C delta y,highest_*+M u) = 0.

Its first 384 rows enforce the earlier lift condition themselves; its
additional ten old rows must still vanish. This has 464+800=1264 raw
unknowns under the two trace masks, or 464+1720=2184 with unrestricted
highest increments. These counts are not solution dimensions. Enforcing
the 384 rows first by Z_C avoids treating all 464 coordinates as free w.

There is a smaller genuinely affine re-preparation problem: retain psi2
and vary only masked lambda2/E3/psi3 (64+64+240=368 coordinates). At fixed
q and psi2, the read formulas are affine in these earlier variables and
the highest increments. If P is their full 1114-row response, its exact
gate is the left-nullspace condition for `[P T_M]` applied to f_*.
It has 368+800=1168 raw unknowns under the highest mask. The repository's
`joint.fit` instead allows 960 unmasked earlier lambda2/E3/psi3 entries
and handles psi4 separately; neither choice is the all-earlier-mixed
464-coordinate problem.

## Interpretation of the Parent's Controls

The parent can compare the full and tangential highest gates at the same
fixed q, same earlier witness, and same matching highest baseline. Each
reported pass or failure belongs to that declared choice of earlier w.
Allowing w to change is an enlarged finite problem and needs its own
compatibility check; it cannot be inferred from a single frozen-w result.
Any numerical gate requires declared cutoffs and tolerances and direct
re-evaluation of all 1114 rows, including old, with the changed data.

The mask and gates concern only represented coefficients and this finite
residual. They supply no numerical rank claim, freedom of regional source
functions, formal prolongation, propagation, Cauchy existence or uniqueness,
PDE classification, native-model identification, or physical mode count.
