# Cubic residual gate with the old highest spinor data frozen

## Contract

This control follows the failed lower-only polynomial collocation. Instead of
fitting isolated zeros of the original equations, it estimates the homogeneous
cubic part of the 80 primary/spatial-curl residuals and solves its coupled
coefficient conditions. All existing origin derivative values are retained.

Only the added neutral commuting-spinor odd-cross Einstein--Cartan comparison
is involved. There is no native HC/C7 identification, exact rank certificate or
regional nonexistence conclusion. Main TeX/PDF are unchanged.

## Coefficient extraction

Use y=x/r, r=1/16384. Along each direction, the stencil

\[
 D_h f=\frac{f(2h)-2f(h)+2f(-h)-f(-2h)}{12h^3}
\]

returns the cubic coefficient for a polynomial of degree at most three. It
cancels constant, linear and quadratic terms. Richardson combination
(4 D_(h/2)-D_h)/3 also removes the degree-five contamination. This extracts a
coefficient, not the unnormalized third derivative.

All 20 cubic multi-indices alpha define directions alpha/3. Their cubic
Vandermonde matrix is invertible, with condition number about 37.18. Thus these
are samples determining an entire homogeneous cubic polynomial, not a fit of
the original nonlinear residual at 20 nodes. Its estimated values remain subject
to finite-difference and floating-point errors.

The two extrapolation scales change the baseline sample vector by 8.13e-11,
versus baseline norm 1.40e-6. Reconstructed monomial coefficient vectors differ
by 1.20e-9. These are observed consistency measures, not rigorous error bounds.

## Allowed correction and result

Retain the previous degree-five coframe and degree-four multiplier correction,
but no spinor correction. The degree-five spinor term in the earlier ansatz
does not affect this leading cubic order. Only E2 and lambda1 correction blocks
contribute to the cubic symbol, evaluated with the origin lower Jacobian.

There are 1456 active real coefficients. Two nested controls give:

| Case | Shape | Numerical rank | Cubic remainder norm |
| --- | --- | ---: | ---: |
| all 16 normal coordinate corrections fixed to zero | 1920 x 1456 | 742 | 2.97e-7 |
| coordinate corrections free | 1600 x 1456 | 422 | 2.97e-7 |

The fixed-coordinate solution has coordinate cubic drift below 5e-21. The free
control allows drift about 8.44e-8 without lowering the residual. Hence those
coordinate restrictions are not the observed obstruction in this comparison.

The retained singular values are separated from omitted values below 1e-12.
The remainder is more than 3000 times the observed sample step variation.
Fresh actual cubic extractions, including a mixed direction, agree with the
linear response prediction to below 1e-12. The remainder still scales cubically
in radial lower-equation checks.

## Consequence

The frozen choice of highest derivative data must be examined before interpreting
the remainder as a new physical source or a failure of the full model. The next
[spinor reprepare](HC_Cartan_Cubic_Spinor_Reprepare.md) changes fourth spinor
derivatives within the kernel preserving the already imposed origin equations.
It does not discard this negative frozen-data control.

## Reproduce

Run `python -B analysis/HC_Cartan_Cubic_Residual_Gate.py` and
`python -B -m unittest scripts.qsc_audit.tests.test_hc_cartan_cubic_residual_gate`.
The adjacent JSON stores both coefficient vectors, singular gaps, residual block
norms and independent full-equation controls. Two workers handle independent
coefficient extractions; SVD and Jacobians use injected cache services.
