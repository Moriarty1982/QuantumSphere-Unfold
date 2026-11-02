# Centered spinor readouts with fixed-map certificates

## What is centered, and what is not frozen

This audit sharpens the spinor expectations in the unchanged Hermitian curl
and trace-reversed coframe equations. It separates their constant spinor
centers from variable deviations, but does not approximate the field by its
center. All deviation and cross terms remain in the Taylor model and tail.
No source, coupling or field coefficient is fitted or changed.

The reference values are the spinor and first spinor derivatives at the
existing germ's origin. They do not introduce a new physical background,
medium or frame assumption. Scope remains the added neutral commuting-spinor
odd-cross Einstein--Cartan comparison; no native HC/C7 identification is added.
Main TeX/PDF are unchanged.

## Joint fixed readout before norms

Let A(omega)_a denote the fixed anti-Hermitian spin response from the preceding
audit, acting on a real lower connection tensor. For spinor models

    u = u0 + du,    v = v0 + dv,

the readout is decomposed exactly as

    Im[u^dagger Q A(omega) v]
      = M(u0,v0,Q) omega
        + Im[du^dagger Q A(omega) v0]
        + Im[u0^dagger Q A(omega) dv]
        + Im[du^dagger Q A(omega) dv].

Here M is the real 4-by-16 matrix obtained by contracting the fixed u0,v0,Q
and the frozen spin-response entries together. Its operator norm can be much
smaller than separately multiplying the norms of those factors. For leading
connection indices, the same matrix acts on each block without a new batch
count factor. A complex connection is rejected for this real-connection
expectation formula; the complex-linear extension from the prior operator
audit is not silently substituted for this real expectation map.

The three remaining terms are evaluated with the previous Taylor contraction
and response machinery. None are discarded. In particular, when u0=v0=0 the
fixed matrix vanishes, but the du/dv term can still be nonzero. A regression
test exercises precisely that case.

## Exact bound for each fixed matrix

The fixed binary64 spinor/selector entries are interpreted as exact Gaussian
rationals. Their products with the frozen response produce an exact rational
real matrix M. For its four-by-four Gram matrix G=M M^T, define

    b = max_i sum_j |G_ij|.

Since ||M||_2^2=lambda_max(G)<=b, any nonnegative q with q^2>=b bounds the
fixed readout norm. The implementation constructs such a dyadic q using
integer square roots after rational power-of-two scaling. It checks
Fraction.from_float(q)^2>=b exactly, rejecting negative inputs or values
outside its finite binary64 representation range. No floating-point eigenvalue
or rounded square root is trusted as this particular upper-bound certificate.

This is an upper norm bound, not generally the sharp singular value. The
matrix entries, rational Gram row bound and certified binary64 upper constant
are saved for each of six maps: Q-weighted and unweighted spinor expectations,
plus four first-derivative/spinor Q-weighted maps. They are built before the two
radius calculations. Full binary input keys distinguish cache entries; hash
equality alone is not used as mathematical equivalence.

The exact fixed matrix is converted to floating coefficients for production
Taylor operations. Those conversion and later arithmetic errors are not
outward-rounded here. Consequently the six constant norm certificates are
only local exact components of the calculation, not a certificate of the
complete nonlinear enclosure.

## Results on the unchanged domains

Let r=1/16384; the bounds cover |x_i|<=L and hence the ball ||x||<=L.

| Quantity | L=r | L=r/2 |
| --- | ---: | ---: |
| Previous curl tail | 0.354565 | 0.0110520 |
| Centered curl tail | 0.233298 | 0.00726948 |
| Previous coframe tail | 0.296727 | 0.00924819 |
| Centered coframe tail | 0.283795 | 0.00884678 |
| Previous combined 80-row estimate | 0.465620 | 0.0145121 |
| Centered combined 80-row estimate | 0.371492 | 0.0115774 |

At r the frame-level matter tail decreases from about 0.01627 to 0.00334.
The Ricci/gravity tail remains about 0.28046: no gravitational improvement is
attributed to this spinor-readout step. The combined estimate includes the
unchanged constraint/probe bounds and all retained low-order coefficients.

The first 40 coefficient rows are bitwise unchanged. The complete coefficient
arrays differ in norm by about 1.07e-14 after regrouping and rational-to-float
conversion. The nonzero degree-three/four defects are retained, not replaced
by their fitted targets. Original equation values, including cube corners,
remain unchanged and well below the conservative tails. This is still not
a distance-to-solution estimate or a regional existence result.

## Controls and remaining work

Tests verify exact rational square inequalities, negative/overflow/underflow
rejection, full-input cache matching, arbitrary variable readouts and the
zero-center/nonzero-deviation control. All six saved Gram bounds are rebuilt
exactly. Perturbed off-shell curl and coframe expressions agree with the
original evaluator while retaining clearly nonzero residuals.

The surrounding polynomial coefficients, inverse models, nonlinear tails
and floating arithmetic are not outward-rounded. Exact low-order closure,
regional PDE compatibility, all-order convergence, physical scales and native
identification remain open. The separate rational retained-origin kernel
certificate is not replaced by these neighborhood models.

Run `python -B analysis/HC_Cartan_Background_Readout_Bound.py` and
`python -B -m unittest scripts.qsc_audit.tests.test_hc_cartan_background_readout_bound`.
Two bounded local workers evaluate the radii using the prepared fixed maps.
The JSON stores fingerprints, exact map data, coefficient arrays, previous/new
bounds and actual-equation controls. This continuation remains a local working
extension after the preceding pushed research snapshot.
