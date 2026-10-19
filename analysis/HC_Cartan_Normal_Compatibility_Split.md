# Splitting the Normal Compatibility Conditions

Date: 2026-10-19. Local, uncommitted follow-up after baseline 176427e.
The OP register and issue 16 were read, not updated. Added neutral
commuting-spinor odd-cross comparison only. Main TeX/PDF unchanged.

## The 28 Left Rows Are Not 28 Independent Physical Constraints

The [general normal block](HC_Cartan_General_Normal_Chart.md) has 68 rows,
56 normal unknowns, and numerical rank 40 on the checked branch. Its
28-dimensional left nullspace can be identified more concretely:

| Group | Dimension | Meaning |
| --- | ---: | --- |
| Spatial constitutive values C_ai, i=1,2,3 | 12 | Initial/tangential constraints |
| Temporal coframe Euler density FE_a^0 | 4 | Gravitational constraint rows |
| Lorentz Ward rows | 6 | Algebraic identities, not new initial constraints |
| Additional mixed-curl gates | 6 | Remaining compatibility introduced by the mixed curls |

Here a=0,...,3 is a frame index, not a normal derivative. This is a
row-space statement for the mixed-order normal system, not a count of
propagating physical modes or a classification of the full PDE.

## Explicit Known Rows

The unknowns are E_,00, psi_,0 and lambda_,0. The spatial constitutive
values depend on spatial psi derivatives and the order-zero connection,
which depends on E,dE,psi,lambda, not these normal unknowns. Their twelve
matrix rows therefore vanish identically.

The four FE_a^0 rows also have no normal coefficients. The first-order
matter density's time-derivative terms cancel in this coframe variation;
antisymmetry in the Palatini curvature expression leaves only spatial
curvature components in the temporal Euler density. The general matrix
evaluation verifies these cancellations without setting E=I or dE=0.

For each elementary Lorentz generator J and its spin lift S_J, the
existing exact Cartan-eliminated identity is

    FE:(J E) + 2 Re[(S_J psi)^dagger R] + C:(J.T lambda) = 0.

In residual order (C[16], real/imag R[24], FE[16], mixed curls[12]),
the corresponding row is

    ((J.T lambda).flat, 2 realify(S_J psi), (J E).flat, 0[12]).

The [Lorentz audit](HC_Cartan_Lorentz_Residual_Identity.md) supplies the
signs and normalization. Compatible elimination includes the derivative
of the Cartan equation; merely solving its value would not suffice.
The six rows annihilate both N and the affine constant b, even for
unfitted normal derivatives. They are therefore not six additional
restrictions to impose on genuine field data.

## Projector Construction and the Remaining Six Gates

The original 56-row block has rank 34 and left dimension 22. The sixteen
explicit constraint selectors plus six independent Lorentz rows span
that entire left space in the numerical checks. Adding the twelve mixed
curls increases rank by six, leaving six additional left gates.

The implementation removes the explicit selectors from the Lorentz
rows, orthonormalizes the remainder, and uses projectors to avoid
assigning meaning to arbitrary SVD basis rotations. It then projects
the full 68-row left space orthogonally to those known 22 directions.
The remaining projector has rank six. Its rows generally mix old
equations with curls; they are not six arbitrarily selected bare curls.

An orthogonal Lorentz representative can carry a contribution determined
by nonzero known constraint values. It must not be mistaken for a failure
of the raw Lorentz identity. The report tests the raw identity separately.

On the rank-34/rank-40 branch, with the six Lorentz identities satisfied,
finite normal solvability is equivalent to vanishing spatial C, temporal
FE, and these six remaining gates. This is a conditional finite row-space
criterion, not yet propagation of those conditions. The sampled branch
does not prove an exact upper rank throughout a region.

At the origin the six remaining gate residuals have norm 3.8e-15. At the
six tested points they can reach about 1.02e-7. Varying every normal
unknown leaves their values unchanged to rounding tolerance. Thus they
cannot be removed by another normal-only least-squares fit of the same
prescribed data.

## Conditional Constitutive Propagation

Define J_0i,a=partial_0 C_ai-partial_i C_a0. Then identically,

    partial_0 C_ai = J_0i,a + partial_i C_a0.

For sufficiently smooth fields, if C_a0=0 and all J_0i,a=0 are enforced
as equations on a region, C_ai(t,x)=C_ai(0,x). Zero initial spatial
constitutive constraints therefore remain zero. More generally the
coordinate-volume L2 norm on a fixed spatial domain obeys the elementary
Duhamel bound

    ||C_spatial(t)|| <= ||C_spatial(0)||
        + integral_0^t ||J_0i + partial_i C_a0|| ds.

This is conditional: the twelve mixed curls include six independent
normal directions and six remaining compatibility gates. Assuming all
mixed curls zero does not prove that a reduced evolution enforces their
remaining compatibility. No unconditional full constitutive propagation
theorem is being inferred from this kinematic identity.

The four gravitational rows have the already established
[conditional subsidiary result](HC_Cartan_Gravitational_Subsidiary.md):
exact Cartan elimination, C=R=0 on a region, spatial trace-reversed Euler
evolution, suitable Lorentzian slices and boundary conditions give
gravitational constraint propagation. The hypotheses C=R=0 are regional
field equations, not consequences of their values at a single point.

## Exact Projector Transport and the Missing Source Control

For the full-column-rank augmented chart T=(N;W), let g be its prescribed
84-component right-hand side, u=T^+g, P=I-TT^+, and r=Pg. Differentiating
the orthogonal range projector gives

    partial_0 P = -P (partial_0 T) T^+
                  -(T^+)^T (partial_0 T)^T P,

and hence

    partial_0 r
       = P(partial_0 g-(partial_0 T)u)
         -(T^+)^T (partial_0 T)^T r.

This is an exact matrix identity, not a closed subsidiary equation.
Writing s=P(g_0-T_0 u), the source s must be controlled by r and other
already controlled constraints to obtain homogeneous propagation. If
s=0, a bound on ||T^+|| ||T_0|| yields the usual conditional Gronwall
estimate. Invertibility alone says nothing about s.

A formal constant-T example makes the logical gap explicit: choose a
unit vector v in ker(T.T), g(t)=T u0+t v. Then r(0)=0 but r(t)=t v and
s=v. This is an algebraic example of compatibility data, not a lift to
the parent field equations or a physical counterexample.

For the actual finite Taylor field, the diagnostic uses
g(x)=(-b(x),W u_field(x)) and the original sample radius 1/16384 in the
positive time direction. This is explicitly not the much smaller
uniform-majorant radius 2^-32. At the tested point T is nonsingular,
the compatibility norm is about 1.13e-7, and the estimated source norm
is about 0.005577. The homogeneous term has norm about 7.6e-6.
Centered-difference transport checks at steps 1e-7 and 5e-8 have errors
about 2.1e-6 and 3.7e-6; decreasing the step does not improve this
roundoff-sensitive check. No convergence order or exact numerical
derivative certificate is claimed.

The source is therefore retained, not dropped in order to claim
propagation. A truncated Taylor field need not satisfy regional evolution,
so this diagnostic neither disproves a genuine solution nor identifies
a new physical source or interaction.

## Result and Next Task

The formerly undifferentiated 28-row obstruction is now separated into
known identities, recognizable initial constraints and six remaining
mixed-curl compatibility gates. The next task is to derive their source
control from the actual reduced field equations and the source-coordinate
law, including the variable chart derivatives. The projector identity
pinpoints the required forcing term but does not supply that closure.
Gauge/source transport, full hyperbolicity, exact rank upper bounds and
regional Cauchy existence remain open; this is not a claim that all of
those questions reduce to only six scalar equations.

## Reproduction and Verification

Run `python -B analysis/HC_Cartan_Normal_Compatibility_Split.py --output
analysis/HC_Cartan_Normal_Compatibility_Split.json` from the repository
root. Two local threads reuse scoped cache services for six diagnostic
field points. `--workers 1` selects sequential evaluation.

31 focused tests passed: 10 compatibility-split/transport tests, 11
uniform-bound tests and 10 general-normal-chart tests. They verify
projector dimensions and orthogonality, Lorentz identities on unfitted
normal data, the remaining gates' normal invariance, the constitutive
identity, and both a smooth-matrix transport check and a formal forced
example. The full repository suite was not rerun for this isolated
analysis addition. No main TeX/PDF, issue, release or Git remote was changed.
