# Second constitutive principal compatibility

This bounded sidecar concerns the neutral odd-cross Cartan comparison at the
fixed action, state and couplings. It varies only the fully symmetric spinor
third derivative psi3, keeping the point and E3/p2/l2 fixed. It does not assemble
or solve the enlarged normal-plus-1200 system and proves no propagation or
regional existence statement.

## Derivation and coordinate convention

In `HC_Cartan_Regular_Gravity.equations`, the only psi3 contribution to
`constraint_second[r,s,a,mu]` is

    delta C2[r,s,a,mu] = Im pairing(psi, delta psi3[r,s,mu], Q)[a]
                       = L[a,:] realify(delta psi3[r,s,mu]).

All other terms are fixed in this variation. In particular,
`connection_second` depends on p2/l2/E3 and the lower jets, but not psi3.
The same L is `spatial.constraint_principal_map(psi)`, a real 4 x 24 matrix.
At the retained state it has rank 4. There are 20 unique symmetric triples,
each providing an independent 24-real spinor slot. Thus the 160 x 480 map has
rank 20*4 = 80 and kernel dimension 20*(24-4) = 400.

C2 is stored as `(PAIR2, a, mu)`, flattened to 160 coordinates, with PAIR2
the ten lexicographic pairs r <= s. The input uses exactly the existing
`regular.unpack` convention: all 240 real parts followed by all 240 imaginary
parts of `(PAIR3, channel, spinor)`. It is not twenty contiguous 24-real blocks.
`principal_matrix(L)` constructs this bounded map without evaluating a large
jet system. `pack_second` and `unpack_second` convert the C2 representations.

The image consists exactly of tensors symmetric in all THREE spacetime
indices `(r,s,mu)` for each fixed frame index a. It does not symmetrize a.
For each sorted triple t, group the stored rows `(p,mu)` whose pair and mu
sort to t. All their four-component frame values must agree. Differences from
one reference row per group give `(40-20)*4 = 80` independent compatibility
conditions, exposed by `compatibility(source)`.

## Metric and projector

Let w_p = 1 for a diagonal pair and 2 otherwise. The full tensor Frobenius norm
is

    ||C2||_F^2 = sum_(p,a,mu) w_p * C2[p,a,mu]^2.

For each triple group G_t, the orthogonal image projection copies the value

    mean_t[a] = sum_((p,mu) in G_t) w_p*C2[p,a,mu]
                / sum_((p,mu) in G_t) w_p

to every row of that group. The denominator is the number of distinct ordered
permutations of t: 1, 3 or 6. Equivalently, expand to the full tensor and fully
symmetrize the three spacetime indices. This projector P satisfies P^2=P and
W P=P^T W, with W repeating each pair weight sixteen times. It need not be
self-adjoint in the unweighted stored-vector metric.

`project(source)` returns `(image, defect, means)`, using the full tensor
metric by default. `project(source, "unique")` instead averages stored rows
equally. These have the same image and exact compatibility test, but different
least-squares defects. In particular a source with only C2[0,0,0,1]=1 projects
to 1/3 on the (0,0,1) group in the full metric and to 1/2 in the unique metric.
Its unavoidable full-norm residual is sqrt(2/3).

For a frozen source b=C2, a symmetric psi3 correction exists exactly when
`compatibility(b)=0`, or equivalently `(I-P)b=0`. A correction is obtained by
applying -L^+ to each projected frame readout. `minimum_norm_lift(L, -b)`
returns that correction in the existing 480-coordinate ordering; if b is
incompatible it cancels only P b, leaving `(I-P)b`. No additional jet equations
are enforced by this helper. A parent system may use `compatibility(b)` as
80 independent rows, or use a metric-adjusted defect for least squares.

## Bounded verification

The starting jets come from the latest
`HC_Cartan_Joint_Neighborhood.load_data()`, including its saved-input checks.
The JSON pins the sidecar and inherited sources, plus the directly used action,
readout and spinor helpers, with LF-normalized SHA-256 hashes. Fingerprints
are checked before and after evaluation.

The map has 80 nonzero singular values; the smallest is about 0.80145 and the
largest rejected value about 3.3e-15. Direct `regular.equations` evaluations
at random, signed and sparse real/imaginary increments agree with the map to
about 1e-11. The second connection and all other returned equations change by
exactly zero. The tests separately compare the weighted projector to explicit
full-tensor symmetrization, check its weighted adjoint and rank, verify the
80 independent compatibility rows, and lift compatible targets.

The latest starting C2 full norm is about 5.5e-11, already near numerical zero.
Projected cancellation agrees with the predicted defect to about 1e-11;
these small baseline values are not a new nonzero obstruction. The deliberately
incompatible unit target has compatibility norm 1 and unavoidable residual
0.8164965809. An independent direct regular-equation evaluation of its lifted
projection reproduces that residual to about 2e-12. This negative control tests
principal incompatibility at fixed other jets, not incompatibility after the
parent's additional normal/higher-jet variations.

Focused verification (NumPy only, no installs or full suite):

    python -m unittest discover -s scripts/qsc_audit/tests -p test_hc_cartan_second_constitutive_symmetry.py -v

The sidecar CLI also supports `--output` to regenerate the JSON after an
intentional source or starting-jet change.
