# State sufficiency: exact comparison and OP5 boundary

30 October 2026. Self-review against repository revision f98b29ba8eeb87c053a39285ca348c4d2ef76081. New exact comparison computation, not a new native QSC solution. Reproduce: `python check.py` in this directory. `manifest.json` passes the computation-audit evidence validator. Source and output SHA-256 hashes are recorded. Wolfram separately verified both curl equations, both divergences, point fields and point Gram derivatives; local SymPy additionally checked equality of the entire initial Gram fields and the full-field spatial-jet derivative formula.

## Precise target

For a readout pi and an evolution X, a necessary condition for a deterministic projected vector field Y is Dpi(c) X(c) = Y(pi(c)). Thus states with the same readout must have the same readout velocity. This test must use admissible solutions, fixed backgrounds, clock and observer. Comparing arbitrary off-shell jets does not establish nonuniqueness of evolution.

## Exact counterexample in a declared comparison

Use vacuum Maxwell evolution in units c=1: dt E=curl B, dt B=-curl E, with both divergences zero. For real nonzero k and a=+1 or -1 choose

E=(2,-a cos(kx) sin(kt),0), B=(0,1,a sin(kx) cos(kt)).

Both satisfy all four equations identically. This is a local smooth/periodic comparison, with constant background; finite total energy on all of R^3 is not claimed.

At t=0 the entire Gram field is G=diag(4,1+sin(kx)^2), independent of the sign a. Its normalized version is likewise identical. Consequently all spatial derivatives of G and rho at initial time agree between the two solutions. Nevertheless, at x=t=0:

- E=(2,0,0), B=(0,1,0), G=diag(4,1), rho=diag(4/5,1/5), all identical.
- dt G has off-diagonal entries -a k and zero diagonal entries.
- dt rho has off-diagonal entries -a k/5 and zero diagonal entries.
- dx B=(0,0,a k), which distinguishes the solutions.

The chart is regular at this point: det G=4. This is not caused by a singular Gram chart. The counterexample excludes autonomous evolution of the whole Gram field, even with arbitrary spatial derivatives of Gram data, on this comparison family. The missing orientation field cannot be recovered by differentiating Gram data alone.

In contrast, full oriented E,B and their spatial first derivatives determine their next time derivatives through the declared equations. Product differentiation gives dt G11=2 E dot curl B, dt G12=(curl B) dot B-E dot curl E, dt G22=-2 B dot curl E. The script verifies this formula identically. This is no counterexample to full-field Cauchy determinism and no demonstration of fundamental memory, an extra clock or an added physical field.

## Transfer to actual OP5: important negative finding

The existing OP5 comparison already retains the full spinor and covariant first jets; it does not evolve only a Bloch point. Its coframe itself depends on first derivatives. The current symmetric-second-jet obstruction therefore cannot be attributed to discarded Bloch orientation merely by this counterexample.

The existing temporal analysis gives A0 B0=E, P=I-B0 E^-1 A0 and J0=H0 P. At fixed spinor, spatial jets and time-coframe, the map on ker A0 is H0, invertible under the stated time-operator assumption. If the four left compatibility conditions hold, the temporal correction in this fixing is unique. Arbitrarily appending free time derivatives to a state does not explain or solve the four conditions.

The previously recorded joint compatibility/erhaltung experiment solves point equations and scalar derivative conditions, but reports stable nonzero symmetric-second-jet completion residuals at three points. These are existing numerical records, not rerun or promoted by this experiment. Equality of mixed derivatives is an additional field-integrability requirement; adding a state label cannot remove it. No general nonexistence follows from those three samples.

## Result and next discriminating obligation

Verified: a Gram/Bloch field can fail to be a dynamically sufficient state even when its entire spatial initial profile is known. Orientation-complete field data and their spatial variation repair this particular comparison.

Not established: that omitted state variables cause the current full OP5 obstruction, or that the common-carrier hypothesis is true. The stronger initial suspicion has narrowed, not become a solution.

Next native check: eliminate symmetric second jets to obtain compatibility functions C(Psi,J)=0 on full first jets, enforce them jointly with point equations and existing constraints while allowing the remaining admissible spatial jets to change. Fix the background and time convention, preserve coframe regularity, and distinguish a genuine gauge quotient from a pointwise algebraic fixing. A corrected initial-data manifold and propagation identity are required before interpreting a regional evolution. This is a proposed calculation, not an executed result in this record.
