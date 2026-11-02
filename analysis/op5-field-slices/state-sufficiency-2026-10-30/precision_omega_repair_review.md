# Independent review: affine third-jet compatibility repair

Read-only formula and implementation review of `precision_omega_repair.py`, `precision_completed_rebuild.py`, and `precision_fourth_source.py`. No numerical experiment was rerun. This review is bounded to the finite comparison model and does not establish physical validity or regional existence.

## Affine dependence

Let R=R(x,u,j) be analytic near the fixed regular first jet, with j=du. Fix the field Taylor coefficients of degrees0,1,2. A change T in the degree3 field coefficients changes u first at degree3 and j first at degree2. In the degree3 Taylor coefficient of R, two insertions of T cannot occur: their minimum combined degree is2+2=4. Therefore the degree3 source with fourth field jet zero is affine in T, despite R being nonlinear in its first-jet arguments. Coefficient dependence on the background and the fixed lower jets does not alter this degree counting. This argument applies componentwise to the completed R=(F,G,dg), because the implemented G has already eliminated all symmetric second-field derivatives and is a first-order analytic function on the invertible-coframe chart.

Consequently b(T+s d)=b(T)+s D b[d] exactly in the finite formal Taylor algebra. Computing the slope from the unit displacement is valid; this is not an uncontrolled large-step finite-difference approximation. The independently evaluated corrected source and its affine-prediction error are an appropriate implementation control.

## Lower constraints

The degree2 coefficient of R is affine in the degree3 field coefficients, with linear operator A3 formed by prolonging the first-order principal symbol. Thus A3 d=0 preserves the degree2 R equations exactly in formal arithmetic, while degrees0 and1 are unchanged by degree counting. A direction in the full320-row kernel is required. The code first projects the old numerical direction onto the new numerical kernel, then iteratively refines it and reports `max(abs(apply3(d)))` over all320 rows. The retained old direction is only a search seed, not a transfer of the old compatibility condition to the new germ.

The hard-coded rank271 and extracted numerical kernel are conditional on the earlier rank diagnostics, not exact rank certificates. Reporting full kernel leakage is essential. The coefficient correction times that leakage bounds the added lower residual, in addition to the existing finite lower residual.

## Scalar correction versus complete compatibility

The frozen lower first jet fixes the fourth-order principal operator A4 and its left witness lambda. If the rebuilt directional slope lambda Db[d] is nonzero, s=-lambda b/lambda Db[d] cancels that one witness pairing. It does not by itself prove that all112 left-quotient coordinates vanish. The subsequent fourth-jet re-elimination and evaluation of every one of the640 equations are therefore the decisive finite check. A small selected528-row residual alone would be insufficient. The implementation retains the complete640-row residual and actual recomputed source, which is the correct distinction.

A nonzero slope should be checked explicitly before division; the recorded value and successful completion can support this run, but a future reusable solver should have a guarded near-zero/failure outcome. Neither a successful scalar correction nor successful full fourth completion constructs the full nonlinear Omega covector on all209 third-jet tangent directions. It establishes a successful one-direction finite repair if the reported lower leakage, affine-prediction error and full640 residual are all acceptably small.

No substantive formula error was found in this route. The main residual limitations are numerical rank selection, lack of exact/interval certification, dependence on the shared analytic R evaluator, and absence of higher-order propagation/convergence. A direct field-path recheck using the corrected third and fourth coefficients would strengthen the final finite result without turning it into an all-order theorem.

## Reported run reconciliation

Parent reported the following successful finite controls: full A3 direction leakage3.95e-70, witness slope1.5525, step-1.7977e-7, and maximum normalized third-coefficient correction4.203e-8. The actual source agrees with the affine prediction to4.87e-68; the corrected witness pairing is-3.57e-69. More importantly, all640 completed residuals after fourth completion are bounded by2.18e-63, and direct quartic-path checks in an axis and mixed direction give degree3 residuals1.58e-64 and5.03e-62. These values were reported by the parent, not independently rerun in this review. They support finite degree4 completion at one common germ and do not establish general closure or the unresolved fifth-degree symbol claim.
