# Independent review: four-direction fifth-extension gate

Read-only formula/code review of precision_fifth_gate.py and precision_fifth_source.py. No numerical run was performed for this review. The finite comparison model and its analytic completed first-order evaluator are taken as declared; this is not a physical validity review.

## Preservation and affine dependence

Let R=R(psi,partial psi,x) be analytic near the regular first jet. Varying only homogeneous degree4 field coefficients changes psi at degree4 and its first derivatives at degree3. Therefore coefficients of R below degree3 do not change, and its degree3 coefficient changes linearly through the prolonged first-order symbol A4. Full A4-kernel membership preserves the previously solved degree3 R equations; merely solving selected rows would not establish this. The script correctly recomputes all640 A4 residual entries after refining each candidate direction.

The degree4 R source is affine in these fourth field coefficients with field0..3 fixed and field5 zero: two varying first-derivative insertions first appear at degree6, and any insertion involving the varying field itself has still higher degree. Thus the source differences at a unit step give the exact formal affine gate in this degree, conditional on the analytic evaluator and coefficient conventions. This does not imply that the computed numerical source differences are exact.

The normalized degree4 source uses fourth directional derivatives divided by24 and the checked rational interpolation inverse. The top free fifth-field symbol is fixed by the unchanged first jet. The packing conventions of fourth directions agree with the preceding A4 assembly: symmetric Taylor coefficients, with multiplicity alpha_mu+1 in prolongation.

## What four directions can establish

The script constructs four deterministic random candidates in the float64 nullspace of A4, then refines them using a rank528 minor while checking every preceding equation. These directions define a restricted map from a four-dimensional parameter space into the full213-dimensional numerical left quotient of A5. Four nonzero gate singular values show numerical injectivity/rank4 on this tested subspace, not that the complete source gate on all312 A4-kernel directions has rank4 or that its image equals all admissible source conditions.

If the source quotient q lies in the tested four-column image, the proposed correction is a finite constructive candidate. It must still be recomputed through the original analytic source, followed by a fifth-jet solve and a check of all1120 new equations. One should also check lower residuals after multiplying each tangent leakage by the fitted parameter, because parameters can magnify very small direction errors. A failure to fit q in this restricted span would not be an obstruction to the full fourth-jet freedom; it would motivate more directions or a structurally guided gate calculation.

## Numerical boundaries

The final quotient projection, singular values and least-squares fit are float64, even though source differences and direction-leak checks use70-digit arithmetic. Near-null numerical left directions may contain roundoff, and subtracting two large source arrays before float conversion must be interpreted with the observed precision checks. The script subtracts source arrays while still at70 digits, which is appropriate. Full residual checks after the repair are the decisive numerical evidence; a small projected quotient alone is insufficient.

The float minor inverse is a refinement preconditioner, not a high precision factorization or certified rank proof. Rank assumptions528 and907 are inherited numerical diagnostics. No exact root, interval certificate, all-order formal integrability, regional existence, complete Omega covector, or physical theorem follows from this four-direction test. No substantive formula or indexing error was found by inspection.
