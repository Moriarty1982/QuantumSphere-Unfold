# An Explicit Source-Parameterized Normal Reduction

Date: 2026-10-18. Added neutral odd-cross Cartan comparison only. This follows
the regional Ward scope audit by returning to the actual parent normal
equations, rather than treating constitutive residuals as independent fields.
The action, M, Q and retained lower/spatial data are unchanged. Main TeX/PDF
are unchanged. No full regional evolution or native identification is claimed.

## What Is Now Explicit

The actual 68-by-56 normal system is reduced to an explicit compatible inverse
with every remaining coordinate displayed. It contains the original sixteen
constitutive, twenty-four real probe and sixteen independent coframe Euler
equations, plus the twelve mixed constitutive curls. The latter are necessary
differential consequences of regional F=C-E=0, not a new action law.

The 56 normal variables are E_,00 (16), real psi_,0 (24), and lambda_,0 (16).
Their matrix N has numerical rank 40. Its kernel splits into ten exhibited
leading gauge directions G and six complementary directions U. These SIX
directions are NOT the previously discussed three mixed-curl responses:
the present system already enforces every mixed curl. The counts refer to
different maps and different compatibility stages.

The independent [derivation](HC_Cartan_Normal_Source_Reduction_Derivation.md)
proves the finite-dimensional statement, conditional on the exact rank and
kernel hypotheses:

    N delta = r has a solution iff L.T r = 0,
    delta = N^+ r + G g + U q,
    G.T delta = g,   U.T delta = q.

Here L has 28 orthonormal columns spanning ker(N.T), g has ten entries and
q has six. N^+ is the Moore-Penrose inverse in the declared real coordinate
norm. The 28 conditions are range compatibility on arbitrary algebraic right
hand sides, not automatically 28 independent new physical constraints.

For the implemented increment convention, r is an increment of the normal
equation vector. To repair an actual origin residual r0 to zero one needs
r=-r0, including its compatibility check. The direct saved-origin residual
is about 2.34e-14, not declared exactly zero. The q controls below use r=0
and therefore retain that tiny origin residual, instead of silently refitting
other fixed data.

The six source values are exposed and preserved when supplied to the solver.
Zero defaults select a particular solution only; they are NOT a derived
closure q=0, a gauge proof or new physical couplings. The solver rejects
incompatible right hand sides above an explicit numerical tolerance. Within
that tolerance its output must still be interpreted with its recomputed
residual, not as an exact certificate.

## Construction from the Existing Parent

G is the orthonormal span of the four coordinate and six Lorentz leading
normal directions already exhibited in the parent analysis. The six canonical
remaining multiplier directions are projected perpendicular to G and then
orthonormalized to U. No old higher-jet loader is used: the latest joint
neighborhood loader supplies the point and higher data together.

The decomposition is checked against the FULL normal SVD kernel, not just
against its six multiplier columns. It satisfies, to numerical precision,

    N G = N U = 0,
    G.T U = 0,
    I - N^+ N = G G.T + U U.T,
    N N^+ = I - L L.T.

Adding the ten gauge-coordinate and six source-coordinate rows yields an
84-by-56 system of full column rank 56. This gives a unique normal increment
when all coordinates and a compatible r are supplied. It does not establish
a full field gauge fixing or a spatial/time PDE principal-symbol reduction.
The inverse amplification in these coordinates is about 9.43893; the smallest
retained normal singular value is 0.1059442, the next about 8.33e-15. No
uniform rank or inverse estimate on a neighborhood is inferred from this.

## Actual-Equation and Higher-Equation Controls

At a nonzero q=0.01*(1,-0.5,0.3,0.2,0.4,-0.1) with g=r=0:

- All 68 actual normal equations recompute with norm 2.07e-14.
- The incremental normal error is 4.83e-17.
- The requested six source coordinates are recovered within 2.18e-18.
- The gauge-coordinate error is below 2e-19.
- The full Cartan curvature at the point changes by about 3.3e-15.
- The current frozen-higher 384-equation residual becomes 0.661523885.

The final item is deliberately retained. Re-evaluating the latest higher
equations along the six U columns gives rank SIX, with smallest singular
value about 16.2213. Thus ignoring these directions solely because the
normal equations or point curvature do not see them is unjustified. This
does not prove that they are non-gauge under every transformation of the
full higher jets; a full gauge transformation can change those jets too.
Nor does the failed frozen-higher check prove that re-solving appropriate
higher derivatives is impossible.

These response calculations use the current joint psi2/lambda2/E3/psi3,
not the older Remaining_Multiplier loader. Their 384 rows are only C1/R1/FE1/C2,
not the complete later 1114-component completion. In this restricted six-source
variation psi1 and lambda's temporal-column normal derivative are exactly
unchanged. Inspection of the parent formulas then gives an affine higher
response: connection_second, C1/R1/FE1/C2 depend linearly on the changed E2
and lambda1 while psi1 and all higher entries are fixed. Random finite
superpositions and signed/double-amplitude controls confirm this property.
It is not asserted for arbitrary changes of all 56 normal entries.

## What Remains for a Regional Evolution

This step supplies the finite normal inverse and a precise place for the
unresolved q coordinates. They cannot yet be prescribed as arbitrary smooth
functions on a region: mixed-derivative equality, higher equations and spatial
compatibility can restrict them and their derivatives. A raw QR/SVD frame
also needs a smooth local choice before its coefficients become fields.
The ten leading gauge directions likewise do not by themselves supply a
complete regional gauge reduction.

The next calculation must derive the conditions on q from actual spatial and
prolonged Euler equations, allowing the higher derivatives those equations
control to vary. After equivalence and regularity are justified, the full
characteristic and subsidiary estimates become meaningful. No closed q
evolution, symmetrizer, uniqueness or regional existence is supplied here.

The [pinned report](HC_Cartan_Normal_Source_Reduction.json) stores the kernel
bases and diagnostics. Thirteen focused tests cover the pseudoinverse
identities, rejection of incompatible targets, arbitrary prescribed source
coordinates, unprojected normal equations, current higher responses and the
distinction between a selected particular solution and a proved closure.

Verification: all 2,137 audit tests plus 34 separate OP5 checks passed (2,171
total), including thirteen new normal-source tests. Full-monolith preservation
and whitespace checks passed. Commit afcbfed was pushed BEFORE this new stage;
the normal-source additions remain uncommitted. No later push or PDF build
was performed.
