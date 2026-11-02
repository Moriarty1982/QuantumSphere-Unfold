# Bounded Cauchy-Jet Source Mask Audit

Date: 2026-10-18. Independent source-reading audit of the finite mask only.
The parent owns the actual A (384 by 1200), B (384 by 6), saved-point
validation, ranks, and solves. No modules were imported or executed here;
no assembly, rank fit, tests, or saved-data recomputation was performed.

## Verdict and Scope

The proposed 464-coordinate mask is correct for preserving the represented
finite tangential germ of E, E_t, psi, and lambda on the coordinate slice
t=x^0=0, with E treated as second order and psi and auxiliary lambda as
first order. The intermediate mask preserving only spatial psi2 has 1056
allowed coordinates. These statements concern increments about the same
saved jet; they do not assert that the fixed surface data are arbitrary,
admissible, or extendible to an actual solution.

The functions read were `Compatible_Jets.realify`, `complexify`, and
`unpack_second`; `Prolongation.unpack_third`; `Regular_Gravity.unpack`,
`connection_second`, and `equations`; `Remaining_Multiplier.normal_point`
and `canonical_basis`; `Normal_Source_Reduction.build_reduction`; and
`Joint_Neighborhood.load_data` and `fields` (all filenames carry the
`HC_Cartan_` prefix). The current
`HC_Cartan_Normal_Source_Compatibility.allowed_cauchy_coordinates` and
its intermediate mask in `evaluate` agree with the indices below.

## Coordinates and Packing

Use the matching tuple from `HC_Cartan_Joint_Neighborhood.load_data()` and
U=`Normal_Source_Reduction.build_reduction(prepared, point)["sources"]`.
The loader reads the latest saved joint completion and checks matching
fingerprints and retention of psi2; this audit read those checks without
executing them. Older regular-gravity or remaining-multiplier loaders are
not interchangeable with this tuple.

Write `jets(z) = jets + Regular_Gravity.unpack(z)` blockwise. In the
1200-real-coordinate z, the half-open slices are:

| Block | Slice | Independent entries |
| --- | --- | ---: |
| psi2 | 0:240 | 10 symmetric pairs times 12 complex components |
| lambda2 | 240:400 | 10 symmetric pairs times 16 real components |
| E3 | 400:720 | 20 symmetric triples times 16 real components |
| psi3 | 720:1200 | 20 symmetric triples times 12 complex components |

`PAIR2` and `PAIR3` use `itertools.combinations_with_replacement(range(4), k)`
in lexicographic order. Their leading axes are coordinate derivative axes;
the trailing axes are field components. Thus a zero in a trailing coframe
or multiplier component index is irrelevant to this mask. For spinors the
trailing shape is (3,4), flattened as j=4*channel+spinor_component. Real
coframe/multiplier blocks use trailing (4,4), flattened as j=4*a+mu.

For psi2, `complexify(vector, (10,3,4))` reads all 120 real entries followed
by all 120 imaginary entries. For psi3 it reads all 240 real entries followed
by all 240 imaginary entries. Neither is interleaved by pair, triple, or
component. In particular, the 240-real psi2 input must be passed as
`prior.unpack_second(vector, True)`; the default is the 160-real tensor
unpacker. The third-order spinor call likewise requires `probe=True`.

The unpackers copy unique entries into symmetric derivative slots, without
factorial scaling. Taylor factors 1/2 and 1/6 occur in the field evaluator,
not in z. Coordinate norms therefore differ from full symmetric-tensor
norms with permutation multiplicities.

## Tangential Germ and Explicit Mask

Let i,j,k range over 1,2,3. Within the represented orders, freezing the
surface traces fixes E_ijk as tangential derivatives of E|, and E_0ij as
tangential derivatives of E_t|. It also fixes psi_ij, psi_ijk, and lambda_ij
as tangential derivatives of psi| and lambda|. The lower tangential
coefficients must already be held fixed in `point` and `prepared`.
This is a finite germ at the base point, not all derivatives of surface
functions. In particular, fixing the E_t trace is stronger than fixing
the E trace alone.

| Block | Allowed derivative tuples | Tuple count | Allowed real count |
| --- | --- | ---: | ---: |
| psi2 | 00, 01, 02, 03 | 4 | 96 |
| lambda2 | 00, 01, 02, 03 | 4 | 64 |
| E3 | 000, 001, 002, 003 | 4 | 64 |
| psi3 | 000, 001, 002, 003, 011, 012, 013, 022, 023, 033 | 10 | 240 |
| Total | | | 464 |

E3 requires at least two time indices: allowing E_0ij would change the
fixed E_t surface germ. Psi3 requires at least one time index: psi_t is
not an independently frozen surface trace for this first-order field.
The same first-order convention leaves normal-containing lambda2 free;
lambda_t is not an independently prescribed trace here. Calling lambda
auxiliary does not make its coefficients unconstrained by the equations.

With zero-based, half-open indices in the full z, the exact allowed set is

    psi2:     [0,48) union [120,168)
    lambda2:  [240,304)
    E3:       [400,464)
    psi3:     [720,840) union [960,1080).

All other z entries are zero increments, not zero absolute derivatives.
The 736 fixed entries are 144 spatial psi2, 96 spatial lambda2, 256 E3
with zero or one time index, and 240 spatial psi3. No extra independent
slots arise from permutations of a derivative tuple.

For the intermediate condition, freeze ONLY psi_ij. Allow the same 96
normal-containing psi2 entries and every entry in [240,1200):

    [0,48) union [120,168) union [240,1200),
    count = 96 + 960 = 1056.

This intermediate condition does not freeze spatial psi3 or the E_t germ
and must not be described as preserving the full tangential Cauchy germ.

## Lower Source Values and the Restricted Gate

`normal_point(point, U q)` changes E2[0,0] and the normal multiplier
derivative lambda1[0,a,i], i spatial, for these particular source columns.
It does not change psi1 or lambda1[0,a,0]. `canonical_basis` has this
support; subtracting the coframe gauge projection and orthonormalizing
preserves it because the gauge columns have only E2 support. Consequently
q itself changes no lower tangential coefficient of E, E_t, psi, or lambda.
This support assertion is about the displayed U, not arbitrary directions
of the full 56-coordinate normal chart.

Let M insert the allowed coordinates into z and A_M=A M. For the parent's
actual affine 384-row evaluator at the matching point, the masked problem is

    h0 + B q + A_M w = 0,
    L_M.T (h0 + B q) = 0,    columns(L_M) span ker(A_M.T).

The second equation is necessary and sufficient only for this finite
problem. Keep the actual h0 and use the left nullspace of the restricted
matrix, not that of A or the earlier 68-row normal matrix. Restriction can
create source obstructions previously absorbed by higher increments.
Neither mask cardinality nor a frozen-higher rank of B determines the gate
rank. Numerical rank cutoffs, consistency tolerances, and residual checks
remain the parent's responsibility; this audit assigns no ranks.

## Spatial Source Derivatives and Higher Residuals

An allowed coefficient is available to the finite solve, not an arbitrary
free derivative of a regional source. In particular, E_00i and lambda_0i
are among the allowed higher slots, but any proposed spatially varying q
must be compatible with their interpretation as derivatives of the lower
normal solution. The full normal coordinate vector also includes psi_t.
Even though U has zero psi_t support, spatial derivatives of the particular
normal solution need not vanish.

For a hypothetical smooth extension with normal coordinates

    n(x) = n_part(x) + G(x) g(x) + U(x) q(x),

one must impose

    partial_i n = partial_i n_part + (partial_i G) g + G partial_i g
                  + (partial_i U) q + U partial_i q.

Here partial_i n consists of the corresponding E_00i, psi_0i, and
lambda_0i entries. Derivatives of the particular solution, basis, and gauge
prescription cannot be omitted. A pointwise choice g=0 does not by itself
specify its spatial derivatives. Nor does a basis constructed only at this
point define a differentiable regional source chart.

The current rows C1, R1, FE1, C2 impose the implemented derivative
constraints, but no explicit independent q_x variable or regional chart
identity is installed by a column mask. To identify q_x or test its
freedom, differentiate the actual lower normal equations and the chosen
source/gauge chart and compare them with these mixed slots. At subsequent
orders enforce the further prolonged residuals and mixed-derivative
relations. Higher residuals can impose additional compatibility and can
couple the source derivatives to other coefficients; whether particular
relations are already redundant at this order requires a separate check.
One cannot simply equate the allowed mixed slots with freely chosen q_x.

Changing z can also spoil the saved later R2/FE2/C3 completion. Its highest
coefficients and residuals require renewed compatibility analysis. Any
extension of this mask to extras must likewise freeze all-spatial E4,
one-time E4, all-spatial lambda3, and all-spatial psi4 at those represented
trace orders. A finite masked lift proves neither preservation of all
1114 later residuals nor indefinite formal prolongation.

There is no conclusion here about arbitrary valid surface data, a
noncharacteristic Cauchy surface, constraint propagation, hyperbolicity,
existence or uniqueness of a surface solution, freely prescribable source
functions, gauge classification, or physical degrees of freedom.
