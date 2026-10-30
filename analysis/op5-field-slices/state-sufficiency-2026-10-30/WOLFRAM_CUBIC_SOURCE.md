# Wolfram-assisted cubic source reconstruction

Wolfram Language independently computed the exact interpolation matrix for homogeneous cubic polynomials in four variables. Directions: four coordinate units, both sum/difference for each of six pairs, and four three-coordinate sums. In the stored ordered monomial basis it returned determinant -64, rank20, exact inverse weights in {-1,-1/2,0,1/2,1}, and symbolic reconstruction True. A clean second evaluation with localized variables confirmed these results without warnings; its inverse has maximum absolute row sum7. The first exploratory query emitted undefined-symbol warnings; the clean confirmation is separately retained.

The normalization is essential: P(d)=D^3 R[d,d,d]/6. Inverse interpolation acts on P, not raw third derivatives. The inverse weights returned as JSON decimals are exact halves and integers, and are converted to rationals locally. SymPy independently checked the determinant and W M=I over the rationals.

The verified map was then applied to70-digit third directional derivatives of the analytic completed R evaluator along the repaired cubic field germ, with the fourth field jet zero. All640 source coefficients (20 monomials times32 equations) are stored in precision-fourth-source-result.json. Two directions not used for interpolation agree to7.42e-68 and3.71e-68. The largest source coefficient is266.19; this is not a compatibility residual or Omega value, since the free fourth jet has not yet been eliminated.

Wolfram has therefore supplied a verified and directly used reconstruction step. It has not solved the entire PDE or certified an exact nonlinear root. Next step remains eliminating the fourth jet from the rebuilt source and identifying the remaining compatibility quotient.

Artifacts: wolfram_cubic_interpolation.wl, wolfram-cubic-interpolation.json, wolfram-cubic-confirmation.json, precision_fourth_source.py, precision-fourth-source-result.json. No repository mutation or publication was performed.
