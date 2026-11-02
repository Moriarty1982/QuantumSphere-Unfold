# Normal Spinor Hessian Completion

Date: 2026-10-19. Local, uncommitted continuation of baseline 8215320.
The central OP register and issue 16 were read; neither was changed.
Added neutral commuting-spinor odd-cross comparison action only.

## Question and Fixed Data

The [previous completion](HC_Cartan_Cauchy_Next_Completion.md) held all
psi2 entries fixed. This calculation releases its 96 normal-containing
real entries, while retaining the same six source values, lower point,
couplings, spatial psi2 values, and all other prescribed tangential jets.
There are also 368 allowed earlier and 800 allowed highest corrections.
Unallowed coordinates retain their original absolute values, not zero.
The LC cubic is recomputed at the shifted point.

## Reduction

The [source-reading derivation](HC_Cartan_Normal_Hessian_Gate_Derivation.md)
gives the finite polynomial structure

    F(p,w) = b + J p + Q(p) + A w,

with p in R^96, w in R^1168 and F in R^1114. A is independent of p;
the only quadratic terms Q are in the last 320 C3 rows. The saved
1168-column matrix is reused through the dependency-injection services
and persistent cache. Its numerical rank is 568, leaving a 546-dimensional
left gate L. For a fixed p, the exact finite compatibility condition is

    L.T (b + J p + Q(p)) = 0.

The numerical implementation uses central derivatives, bounded
Gauss--Newton updates and a decreasing-residual line search. It recovers
w using the pseudoinverse and then evaluates the original full residual,
not just the projected gate. A small optimization step does not mean a
solution exists.

## Numerical Result

The initial gate norm is 32.09525329. Its 96-column derivative has rank
96, with smallest retained singular value about 0.15862. The attempted
correction lowers the full residual only to about 31.94761833. The old
394-row norm remains about 0.34373004; this fit is therefore rejected as
a field-equation completion. The C3 norm is about 31.89493.

The mixed-response control is about 3.35e-10 and the reconstructed full
residual agrees with the eliminated expression within about 3.6e-10.
All frozen earlier and highest coordinates are preserved exactly.

Directional second-difference controls at three amplitudes test whether
quadratic C3 contributions survive projection. The raw third difference
is about 7.9e-10, consistent with the derived degree bound. Directional
controls and an apparently constant reduced Jacobian are numerical
evidence, not a certificate that the entire projected Hessian vanishes.
The raw quadratic norms in the three directions are 0.02401, 1.44993,
and 31.93503, whereas their projected norms are 1.6e-11 to 2.6e-11.
Thus the small projection is not merely due to negligible raw terms.
The machine-readable report retains their actual norms.

## Interpretation and Next Step

Releasing normal psi2 alone did not resolve this chosen witness. The
six-source law at its earlier 384-row order remains unchanged. Nor is
the original unshifted 1114-row solution invalidated.

The next useful check is the complete projected quadratic coefficient
tensor, not more iterations at the same stationary point. If it vanishes
exactly, the remaining gate is affine and one can seek a certified
incompatibility row for these prescribed data. If it does not, a local
failed iteration does not exclude distant roots. Separately, compatible
tangential data may have to satisfy an additional next-order condition;
changing those data would be a different problem and must be recorded.

No native HC/C7 identification, physical frame or scale assignment,
regional Cauchy existence, global nonexistence, or release claim follows.
Main TeX and PDF were not edited for this calculation.

## Reproduction

Run `python -B analysis/HC_Cartan_Normal_Hessian_Completion.py --output
analysis/HC_Cartan_Normal_Hessian_Completion.json` from the repository root.
The report fingerprints all inherited numerical inputs and the prior
completion report. Focused tests independently replay all 1114 equations
and verify the preserved coordinate masks. No whole-suite rerun is
implied by this targeted verification.

Verification: 34 focused tests passed (7 normal-Hessian tests, 18
dependency-injection tests, and 9 solver-container tests).
An additional 14 previous next-completion tests passed (48 total), and
`git diff --check` found no whitespace errors. The attempted
parallel reviewer reached a usage limit after saving its derivation note;
the parent reviewed that note and performed the numerical checks locally.
