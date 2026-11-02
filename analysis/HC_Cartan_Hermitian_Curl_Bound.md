# Off-shell Hermitian curl regrouping

## Fixed problem and useful identity

The full Taylor enclosure was dominated by the 24 curl rows. This audit
regroups those rows before taking tail norms, without changing the field,
couplings or equations. The other 56 rows and their saved bounds are retained
from the fingerprint-checked full Taylor report.

Let H_a = Q tensor W_a act on the flattened three-channel spinor, and let S_mu
be the spin connection, extended trivially to the channel index. In the present
comparison, Q and W_a are constant Hermitian matrices. Define

    C_a,mu = Im(psi^dagger H_a (partial_mu + S_mu) psi) - E_a,mu,
    M_a(S) = H_a S - S^dagger H_a.

For r<s, the ordinary constitutive curl is exactly

    partial_r C_a,s - partial_s C_a,r
      = 2 Im[(partial_r psi)^dagger H_a partial_s psi]
        + Im[(partial_r psi)^dagger M_a(S_s) psi
             - (partial_s psi)^dagger M_a(S_r) psi]
        + (1/2) Im[psi^dagger M_a(partial_r S_s-partial_s S_r) psi]
        - partial_r E_a,s + partial_s E_a,r.

This follows by expanding the derivatives, canceling the commuting mixed
partials of psi, and using Hermiticity:

    Im(u^dagger H v - v^dagger H u) = 2 Im(u^dagger H v),
    Im[u^dagger H S v + v^dagger H S u]
      = Im[u^dagger (H S - S^dagger H) v],
    Im(v^dagger H S v) = (1/2) Im[v^dagger M(S) v].

No field equation, vanishing constraint, source restriction or gauge choice is
used. In particular the curl is not set to zero. This is a regrouping of the
ordinary partial curl, not a substitution of a curvature field equation.
Variable Q or W_a would introduce extra derivative terms; they are not covered
by this frozen-weight identity.

## Frozen spin response before norms

For the real lower connection omega_mu,bc,

    S_mu = sum_bc omega_mu,bc L_bc,    L_bc = -gamma_b gamma_c / 4.

The code constructs the constant response

    R_a,bc = W_a L_bc - L_bc^dagger W_a

before applying the Taylor model. These matrices are anti-Hermitian; for the
frozen Clifford matrices they are also antisymmetric in b,c. Symbolic rational
matrix tests verify the response formula and anti-Hermiticity exactly for the
stored matrix entries. The production evaluation still uses binary64.

Connection-response terms now contract the real omega directly with R. Its
physical derivatives are contracted with the same response before taking
norms. The direct derivative terms use the factor-two Hermitian identity.
This avoids separately bounding expressions whose cancellations are known
algebraically. All low-order Taylor defects and every remaining tail term are
still included. No derivative is taken from an unknown tail bound.

## Numerical results

Here r=1/16384; both estimates cover the whole cube |x_i|<=L and hence the
Euclidean ball of radius L.

| Quantity | L=r | L=r/2 |
| --- | ---: | ---: |
| Previous curl tail | 10.2408 | 0.319199 |
| Regrouped curl tail | 0.867598 | 0.0270437 |
| Previous combined 80-row estimate | 10.4678 | 0.326262 |
| Regrouped combined 80-row estimate | 2.33530 | 0.0727342 |

The curl-tail improvement is about 11.8-fold and the combined improvement about
4.5-fold. The unchanged coframe Euler tail, about 2.16745 at r, now exceeds the
curl tail. This changes which block limits the present enclosure; it does not
identify a new physical obstruction or establish relative physical errors.

The new and old curl coefficient arrays differ in norm by about 1.43e-14,
consistent with reordered floating-point arithmetic. Independent actual-point
evaluations agree to about 1.4e-14--3.1e-14, including cube corners. Actual
curl values are unchanged, not reduced by a new field fit. All remain below
the conservative tail estimate, which is still far larger than sampled errors.

The retained degree-three and degree-four curl bounds at r remain about
3.41e-10 and 5.20e-10. They are not replaced by exact zeros. The recomputed
tail decreases by approximately 32 under radius halving, but this two-radius
observation is not a certified scaling law at every radius.

## Controls and boundary

Tests compare the compact formula with the original expanded expression using
arbitrary complex spinor jets, arbitrary real connection jets and nonzero
off-shell residuals. A separate case has zero spinor value but nonzero first
spinor derivatives and clearly nonzero curls; the identity preserves those
nonzero values. Non-Hermitian weights/selectors are rejected. The first 56
stored coefficients and the non-curl tail bounds remain unchanged.

The scope remains the added neutral commuting-spinor odd-cross Einstein--Cartan
comparison. No native HC/C7 identification, exact low-order closure, regional
PDE solution, convergence or distance-to-solution theorem follows. These are
real-arithmetic majorant formulas evaluated in binary64 without outward-rounded
error enclosure. The earlier exact origin-kernel certificate retains its own
authority and is not replaced by these rounded neighborhood models.
Main TeX/PDF are unchanged.

## Reproduce

Run `python -B analysis/HC_Cartan_Hermitian_Curl_Bound.py` and
`python -B -m unittest scripts.qsc_audit.tests.test_hc_cartan_hermitian_curl_bound`.
Two bounded local workers evaluate independent radii. The JSON records source
fingerprints, old/new estimates, combined coefficients and point controls.
The next numerical target is the unchanged coframe tail; no improvement there
is assumed from this curl identity alone.
