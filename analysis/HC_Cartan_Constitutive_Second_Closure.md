# Second Constitutive Compatibility and a Conditional Final Curl Gate

Date: 2026-10-18. Added neutral commuting-spinor odd-cross Cartan comparison
only. The action, M, Q, spinor value and entire spinor first jet remain fixed.
No native frame, gravitational scale or main-TeX/PDF identification is made.

## Two Distinct Results

The [first closure stage](HC_Cartan_Constitutive_First_Closure.md) left three
mixed first-constitutive curl responses. Its witness did not satisfy the full
second constitutive derivative F2. This stage tests that missing compatibility
with freely variable symmetric psi3, rather than freezing it.

1. Imposing all F2 alongside the previous first equations still permits a
   three-dimensional mixed-defect image at the prepared point. A new witness
   realizes it with every imposed residual recomputed, without projection.
2. The first spatial derivative of the coordinate Ward identity supplies a
   further necessary gate involving second gravitational Euler derivatives.
   Together with the earlier coordinate gate it forces the remaining defect
   to zero IF the displayed multiplier matrix is invertible and the specified
   residual hypotheses hold exactly.

The second result is a conditional finite-jet theorem, not a constructed
regional evolution or an existence/constraint-propagation theorem. Numerical
invertibility at the stored approximate jet is not an interval certificate
for an exact nearby solution or a constant-rank neighborhood.

## Full F2 Test with Free Higher Jets

Start at the authoritative joint 1114-component completion. As before only
E_,00 and temporal derivatives of the spatial multiplier columns vary in the
22-dimensional original normal kernel; all lower spatial data remain fixed.
Now all 1200 higher coordinates psi2, lambda2, E3 and psi3 can vary. Neither the
twelve mixed first curls X nor their vanishing is imposed as an equation.

The 372-by-1222 affine system comprises the previous 212 equations (spatial F1,
all derivatives of F_0, R1, FE1) plus 160 unique-pair F2 components. Its numerical
rank is 335. The smallest retained singular value is 0.00823985, and the next
is about 9.20e-13. On its kernel the mixed first-curl map still has rank three,
with singular values about 0.671687, 0.485263, 0.147189; the next is 4.07e-11.
These are coordinate norms, not physical mode counts or scales.

At amplitude 0.01 of the sign-fixed unit maximum-response kernel direction:

| Residual | Full recomputed norm |
| --- | --- |
| Original 56 point equations | 9.55e-15 |
| First spatial constitutive derivatives | 4.10e-12 |
| All derivatives of temporal constitutive column | 1.92e-12 |
| Complete first probe derivatives R1 | 6.37e-12 |
| Independent first coframe Euler derivatives FE1 | 1.71e-11 |
| ALL second constitutive derivatives, expanded symmetric tensor | 5.95e-11 |
| Mixed first-constitutive defect X | 0.00671686667 |

The defect reverses under opposite amplitude and doubles under doubled
amplitude. A random finite superposition checks that the system is genuinely
affine for these fixed lower data. Direct product-rule curls reproduce X.
The expanded variable normalization differs from the first-stage witness;
the smaller displayed defect norm is not evidence of physical damping.
Actual polynomial-field second differences converge with quarter-sized errors
under step halving; Richardson error is about 1.05e-4. Those field differences
are independent truncation/roundoff controls, not verification to 1e-11.
The [report](HC_Cartan_Constitutive_Second_Closure.json) retains source hashes,
witness coordinates, all singular values and both types of numerical check.

The independent [psi3 symmetry calculation](HC_Cartan_Second_Constitutive_Symmetry.md)
explains why arbitrary second constitutive sources cannot be canceled by psi3
alone. Its 160-by-480 principal map has rank 80, leaving 80 compatibility
conditions. Its image is fully symmetric in the THREE spacetime indices,
without symmetrizing the internal frame index. A weighted projector retains
the multiplicity of off-diagonal derivative pairs. A deliberately incompatible
unit target leaves full-norm residual sqrt(2/3). In the enlarged calculation
the other permitted jets meet these compatibilities too; the principal
negative control is not promoted to a general obstruction.

## Differentiating the Coordinate Identity

The [independent derivation](HC_Cartan_Second_Coordinate_Ward_Gates.md)
differentiates the full off-shell identity BEFORE setting residuals to zero.
At the normal point define

    X_ai = partial_0 F^a_i,
    ell_a = lambda_a^0,
    L_ja = partial_j lambda_a^0,
    D_ji = sum_mu FE2[j,mu,i,mu],   i,j=1,2,3.

The sum in D includes temporal AND spatial mu. Assume F=R=FE=0, E=I, dE=0,
the stated spatial/temporal-column F1 conditions, full F2=0, and R1=FE1=0.
The coordinate identity and its spatial derivative imply

    ell_a X_ai = 0,
    D_ji + L_ja X_ai = 0.

No R2 is needed. Only spatial R1 is used in the differentiated probe source.
No extra Minkowski metric belongs in these contractions of lower multiplier
indices with upper constitutive indices. Full FE2=0 is stronger than needed:
only the nine D=0 conditions enter this gate.

Stack ell and the three spatial multiplier-gradient rows into a matrix M_gate.
For the retained point it is

    [ 0.01000000  0.02000000 -0.03000000  0.04000000 ]
    [-0.20452417 -0.10195844 -0.51670177  0.00234671 ]
    [ 0.49884981  0.73747571  0.13030799  0.00701527 ]
    [-0.01115521 -0.09723682  0.24438112 -0.02428063 ].

Its singular values are approximately

    0.95443573, 0.53748909, 0.04400971, 0.00866071.

This matrix is independent of the varied temporal normal entries. If its
exact counterpart is invertible and all nine D vanish, each column X_i obeys
M_gate X_i=0, hence X=0. The spatial gradient gate has rank three on the
remaining three-dimensional curl image. It therefore excludes the entire
remaining image at this next necessary compatibility step, conditional on
the exact hypotheses. This is not merely a failed fit with frozen E4/lambda3.

## Unprojected Gravity and Source Controls

For the new nonzero-X witness the recomputed spatial gradient source L X
has norm 0.00496144052. Analytic differentiation of the independent coframe
Euler equation gives D=-L X, with error about 4.20e-11. The FULL differentiated
coordinate identity has error about 3.92e-11. Its implementation retains
coframe-second, F1, F2, multiplier-divergence, multiplier-second and complete
probe source terms. Generic off-shell jets test all seven groups, and dropping
each group breaks the identity. Thus nonzero F2 or R1 cannot silently be
discarded when applying the homogeneous gate.

Independent random E4 and lambda3 variations change FE2 itself but leave the
nine divergences D unchanged to numerical precision. They cannot cancel this
nonzero source while preserving the other hypotheses. This follows from the
Ward identity, not from keeping those highest coefficients fixed. The witness
cannot continue to FE2=0 under those hypotheses and fixed spatial lower data;
allowing F2, R1 or the relevant lower data to change alters that conclusion.

## Remaining Problem

This supplies an order-specific compatibility reason for excluding nonzero
mixed F1 under the stronger equations. It does not derive full F2=0 from
initial data, propagate the gate or prove that its invertibility persists
along an actual solution. Nor does it establish all R2/FE2/C3 compatibility
for an arbitrary new state. The original saved joint jet is still the
unchanged zero-defect baseline; modified witnesses do not inherit its
coefficient-domain bounds. The next task is a closed, sourced subsidiary
system or an equivalent constrained evolution, with its regularity and
initial hypotheses justified on a region.

Seventeen parent tests and eight independent symmetry tests cover the affine
continuation, unprojected equations, source-retaining Ward identity, highest
coefficient negative control, multiplier gate and full tensor norm conventions.

Verification: all 2,108 audit tests plus 34 separate OP5 checks passed (2,142
total), including the 25 new second-stage/symmetry tests. Full-monolith
preservation and whitespace checks passed. No commit, push or PDF build
was performed.
