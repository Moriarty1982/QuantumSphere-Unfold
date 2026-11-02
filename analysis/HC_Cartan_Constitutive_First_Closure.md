# First Prolongation Closes Three of Six Constitutive Curl Responses

Date: 2026-10-18. Added neutral commuting-spinor odd-cross Cartan comparison
only, with the declared M, Q, Einstein coefficient and vacuum term unchanged.
No native action, frame assignment, physical scale or main TeX/PDF change.

## Question and Answer at This Finite Order

The [previous transport audit](HC_Cartan_Constitutive_Transport.md) showed that
the original point equations do not force the twelve mixed constitutive curls
to vanish. Six independent curl responses occur on their normal kernel. That
audit's maximum-response witness did not retain the first probe derivatives.

Here ALL first probe derivatives R1 and independent coframe Euler derivatives
FE1 are included. First spatial derivatives of F=C-E and derivatives of its
temporal column remain zero. The numerical result is:

    mixed curl image before first prolongation: rank 6,
    mixed curl image after first prolongation:  rank 3.

Thus this first differential stage removes three responses, but does not force
the entire mixed defect to vanish. The new witness satisfies the first probe
and coframe Euler equations, not merely the original point equations. This is
still a finite-jet non-implication, NOT a regional solution, a propagation
counterexample for the fully reduced system, or a count of physical modes.
The ranks refer to this prepared normal point, with spatial multiplier
columns zero. Away from it those columns need not vanish and differentiated
Lorentz gates can change. No constant-rank neighborhood for this enlarged
system is established by the earlier partial 28-block coefficient bounds.

## Why Three Combinations Are Removed

The [independent Ward derivation](HC_Cartan_Constitutive_Ward_Gates.md) retains
all off-shell sources before specializing. At F=R=FE=0, E=I, dE=0 and FE1=0,
the coordinate identity requires

    sum_a ell_a X_ai = 0,   i=1,2,3,
    X_ai = partial_0 F^a_i - partial_i F^a_0,
    ell = lambda[:,0] = (0.01,0.02,-0.03,0.04).

There is no extra eta contraction: ell already carries the lower internal
index. The three-by-twelve row map W has WW.T=0.003 I. On the original rank-six
curl image it has rank three. These are necessary conditions; their presence
alone would not prove that actual higher field jets realize every surviving
response. The explicit continuation below supplies that realization at this
order. Differentiated Lorentz Ward identities add no independent rows here:
lambda has only a temporal column, while the remaining F1 has only spatial
columns. R1 is not needed in the undifferentiated coordinate identity, whose
probe source contains R itself.

The older 0.01-amplitude maximum-response witness violates these three gates,
so cannot be promoted to FE1=0 by simply adjusting higher derivatives. The new
witness uses a different normal direction lying in the allowed subspace.

## Affine Construction with Fixed Lower Data

The authoritative starting data are the latest joint 1114-component completion.
The spinor value AND its entire first derivative, lambda value, all dE,
non-temporal E2 entries and spatial derivatives of lambda remain fixed. The
temporal derivative of lambda's temporal column remains exactly fixed too.

Allow only 16 E_,00 and 12 temporal derivatives of spatial lambda columns to
vary initially. Their original normal matrix has rank six and a 22-dimensional
kernel Z, matching the full original normal kernel without numerical spinor
variations. Add 720 higher coordinates: symmetric psi2 (240 real), lambda2
(160) and E3 (320). psi3 is kept fixed, since it enters none of the imposed
first derivative equations. No coupling or spinor first data is refitted.

The 742 variables are subjected to 212 real conditions:

- 48 first spatial derivatives of the sixteen constitutive components.
- Four temporal derivatives of the temporal constitutive column.
- 96 real first derivatives of the complete complex probe law.
- 64 first derivatives of the independent coframe Euler law.

The map is affine in these variables, not just its infinitesimal approximation:
the fixed spinor first jet prevents quadratic normal-variation terms. Direct
random finite superposition and signed/double-amplitude controls check this.
Its numerical rank is 175. The smallest retained singular value is 0.01576169,
while the next is about 1.20e-12. Its 567-dimensional kernel includes many
higher-jet freedoms; this number is not a count of physical or gauge modes.

On that kernel the twelve mixed curls have rank three, with retained singular
values 4.84820588, 4.67933290 and 0.24004161; the next is about 5.42e-11. These
singular values use the declared coordinate norms and are not physical scales.
All normal-kernel-induced curls satisfying the three Ward rows are realized
at this finite order, as the contained image has the same dimension three.
This dimension statement is numerical, not an interval/exact rank certificate.

## Unprojected Witness and Its Limitation

At amplitude 0.01 of the sign-fixed unit kernel direction, full re-evaluation
without solver projection gives the following norms:

| Residual | Norm |
| --- | --- |
| Original 56 point equations | 1.00e-14 |
| First spatial constitutive derivatives | 4.10e-12 |
| All derivatives of the temporal constitutive column | 1.89e-12 |
| Complete first probe derivatives R1 | 6.26e-12 |
| Independent first coframe Euler derivatives FE1 | 1.66e-11 |
| Mixed constitutive defect X | 0.0484820588 |
| Coordinate Ward gate W X | 1.01e-14 |

Independent product-rule curls reproduce the defect. Its sign reverses under
opposite amplitude and its magnitude doubles under doubled amplitude. Actual
polynomial-field differences independently check the first probe/gravity
derivatives, with the expected finite-difference errors rather than the much
smaller analytic-jet residuals. Sources, fingerprints, complete witness
coordinates and singular values are retained in the [report](HC_Cartan_Constitutive_First_Closure.json).
At step 1e-5 those independent errors are 4.56e-5 for R1 and 1.93e-4 for
FE1; the probe error falls by about four under step halving. The displayed
defect norm and amplitude use comparison-model coordinates, not measured
physical units or a claimed physical instability rate.

The full second constitutive derivative F2 is NOT imposed: its norm is
0.5102587791 for this witness, versus about 5.5e-11 at zero amplitude. Nor are
R2, FE2 or a regional evolution system imposed. This deliberately retained
failure limits the conclusion: the first prolonged equations and the stated
spatial/temporal-column constitutive first jets do not imply X=0. It does not
show that the new witness extends to a fully consistent solution.

## Next Closure Problem

The remaining three-dimensional mixed-defect image needs a subsidiary equation
or a justified constrained reduction. The next useful test must include the
next differential compatibility conditions, permitting the higher jets that
those conditions actually control. Merely fixing all old higher coefficients
and observing a failure would not prove a structural obstruction. Conversely,
imposing X=0 by hand and reporting a successful fit would not derive it from
the parent equations. The conditional gravitational propagation theorem's
open-region R=F=0 assumptions therefore remain unremoved.

Fifteen focused tests cover fixed data, affine superposition, numerical rank
gaps, the Ward rows, direct curl evaluation, differentiated Lorentz gates,
the full unprojected first equations, actual-field derivative checks and the
nonzero unimposed second constitutive derivatives.

Verification: 2,083 audit tests plus 34 separate OP5 checks passed, for 2,117
total, including fifteen new first-closure tests. Full-monolith preservation
and whitespace checks passed. No commit, push or PDF build was performed.
