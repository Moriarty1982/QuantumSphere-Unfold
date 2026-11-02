# A Temporal Regularity Neighborhood of the Saved Jet

Date: 2026-10-18. Status: conservative analytic norm estimates, evaluated with floating-point input norms, on the saved finite Taylor fields of the neutral Cartan comparison. Not a full normal-symbol estimate, interval certificate, physical scale or Cauchy solution. Main TeX/PDF unchanged.

This is the parent integration task accompanying the [parallel follow-up](HC_Cartan_Parallel_Research.md). It is independent of classification of the remaining multiplier directions and of the next scalar gate. The [regular gravitational jet](HC_Cartan_Regular_Gravity.md) is the baseline, not an assumed evolved field.

## 1. Control the Temporal Weight

At the origin E=I and dE=0. Let r be the Euclidean norm of the four comparison coordinates, and use Frobenius norms of the full symmetric derivative arrays. The saved cubic E/Psi and quadratic lambda fields obey

\[
 \|E-I\|_2\le d(r)=\tfrac12\|E_2\|_F r^2+\tfrac16\|E_3\|_F r^3,
\]

\[
 \|\Psi-\Psi_0\|_2\le p(r)
 =\|\Psi_1\|_F r+\tfrac12\|\Psi_2\|_F r^2+\tfrac16\|\Psi_3\|_F r^3,
\]

\[
 \|\ell-\ell_0\|_2\le l(r)
 =\|\lambda_{1,\mathrm{temporal}}\|_F r
   +\tfrac12\|\lambda_{2,\mathrm{temporal}}\|_F r^2,
 \qquad \ell_a=\lambda_a{}^0.
\]

For d<1, E is invertible, ||E^-1-I||<=d/(1-d) and its volume v satisfies

\[
 (1-d)^4\le v\le(1+d)^4,\qquad |v-1|\le(1+d)^4-1.
\]

In the fixed Clifford representation, K0=I and K^i=alpha_i, so
`||a0 I+a.alpha||=|a0|+|a|<=sqrt(2)||a||` for real a. Also ||Q||=1/2. Thus the complete temporal probe weight

\[
 {\mathbb K}^0=v(E^{-1})^0{}_a I_3\otimes K^a+\ell_a A_a,
 \qquad A_a=Q\otimes K^a,
\]

obeys the uniform perturbation estimate

\[
 \|{\mathbb K}^0-{\mathbb K}^0_0\|_2\le k(r)
 =((1+d)^4-1)+(1+d)^4\frac{\sqrt2 d}{1-d}+\frac{l(r)}{\sqrt2}.
                                                               \tag{1}
\]

The polynomial volume difference is evaluated without subtracting nearly equal numbers. If mu is the origin's smallest probe eigenvalue, then mu_r=mu-k(r)>0 gives a positive temporal weight throughout the coordinate ball and inverse norm at most 1/mu_r.

## 2. Control the Derived Constraint Block

The temporal coframe/probe Schur block remains

\[
 T_{ab}=-\tfrac12\operatorname{Im}
       (\Psi^\dagger A_a({\mathbb K}^0)^{-1}A_b\Psi).
\]

This formula applies to the coefficient map even away from the constraint surface. Each A_a has operator norm 1/2. Let P=||Psi0|| and tau be the origin's smallest T singular value. The inverse perturbation identity gives

\[
 \|({\mathbb K}^0)^{-1}-({\mathbb K}^0_0)^{-1}\|_2
 \le\frac{k(r)}{\mu_r\mu}.
\]

Splitting the spinor and inverse-weight variations gives a per-entry bound with coefficient 1/8. The 4-by-4 operator norm is at most four times that entry bound, hence

\[
 \|T-T_0\|_2\le t(r)
 =\tfrac12\left[\frac{2Pp(r)+p(r)^2}{\mu_r}
                +\frac{P^2k(r)}{\mu_r\mu}\right].                \tag{2}
\]

If tau_r=tau-t(r)>0, T stays invertible, with inverse norm at most 1/tau_r. This estimate controls the actual derived T, not merely the positivity of the probe weight. It does not control the full constrained gravitational principal symbol.

## 3. Evaluated Baseline Ball

The baseline has mu approximately `.96807418` and tau approximately `.03392304`. Halving a trial radius until both lower margins retain at least half their origin values gives:

- Coordinate radius `1/8192 = .0001220703125`.
- Coframe-change bound approximately `8.88e-9`.
- Probe eigenvalue lower estimate approximately `.96795885`.
- T singular-value lower estimate approximately `.01750565`.
- T inverse-norm upper estimate approximately `57.1244`.

This is a deliberately conservative selected radius, not an optimal threshold. Its size is chart-dependent and has no assigned physical length. The bounds use floating-point coefficient norms/eigenvalues and therefore are not an interval-certified numerical enclosure. The underlying norm inequalities are analytic; sampled directions serve only as independent diagnostics of their implementation.

The sampled Taylor fields still have nonzero constraint residuals. Staying in a regular coefficient domain does not turn them into solutions. Nor does this prove constant rank of the entire normal system, classify the six remaining directions, or establish hyperbolic evolution.

The coefficient routine accepts other symmetric higher jets with the same lower data. A re-prepared next-gate jet therefore requires its own coefficient norms and radius estimate; the old radius must not simply be inherited.

## Recomputed Next-Gate Neighborhood

The independently prepared [next-scalar jet](HC_Cartan_Next_Scalar_Compatibility.md) retains the lower point and couplings but changes the 1,200 higher coordinates. Parent integration checks every retained lower array/coupling and the common input fingerprints before recomputing this estimate.

The selected coordinate radius is again 1/8192, but this equality is an outcome of the halving rule, not an inherited radius. The new higher coefficient norms differ. The recomputed lower margins are about `.96795881` for the probe and `.01750509` for T, with T inverse-norm bound about `57.12625`. These retain exactly the same finite-Taylor-field and floating-input limitations as the baseline estimate.

[The cross-result JSON](HC_Cartan_Parallel_Neighborhood.json) stores both estimates, the next-scalar input fingerprint and the complete checks on the changed Taylor fields. [Eight integration tests](../scripts/qsc_audit/tests/test_hc_cartan_parallel_integration.py) also reproduce all 394 equations without another fit, reject mismatched lower data/masses and check common input consistency with the independently constructed multiplier quotient. The old 22-test baseline suite remains unchanged.

## Reproduction

- [Calculation](HC_Cartan_Regular_Neighborhood.py), [saved baseline bounds](HC_Cartan_Regular_Neighborhood.json), [22 tests](../scripts/qsc_audit/tests/test_hc_cartan_regular_neighborhood.py).
- `python -B analysis/HC_Cartan_Regular_Neighborhood.py --output analysis/HC_Cartan_Regular_Neighborhood.json`
- `python -B -m unittest discover -s scripts/qsc_audit/tests -p test_hc_cartan_regular_neighborhood.py`
- `python -B analysis/HC_Cartan_Regular_Neighborhood.py --next-scalar analysis/HC_Cartan_Next_Scalar_Compatibility.json --output analysis/HC_Cartan_Parallel_Neighborhood.json`
- `python -B -m unittest discover -s scripts/qsc_audit/tests -p test_hc_cartan_parallel_integration.py`

The tests cover Clifford/readout norms, the zero-radius limit, the distinct inverse/coframe/probe/constraint failure cases, monotonicity and changed input norms, uniform sample bounds, inverse estimates and the explicit non-solution/full-PDE limitations. No package installation, release/main-TeX/PDF change or Git operation is introduced.
