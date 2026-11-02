# General-coframe first source gate: stable samples, remaining compatibility

## Scope and question

The previous first-prolongation calculation determines six normal source values
at the prepared point, conditional on compatible prescribed higher data. This
sidecar tests its tangent analogue at two displaced points of the same finite
Taylor field, without reimposing the origin restrictions E=I and dE=0.

Only the added neutral commuting-spinor odd-cross Einstein--Cartan comparison is
used. No native HC/C7 identification, physical source classification, uniform
source-gate certificate or regional solution is claimed. Main TeX/PDF are unchanged.

## Coordinate kernel section

Let N(x) be the general 68-by-56 normal matrix, and let W be the previously chosen
16 fixed coordinate rows. At each sample, form T=(N;W) and

\[
 V(x)=T(x)^+\begin{pmatrix}0_{68\times6}\\0_{10\times6}\\I_6\end{pmatrix}.
\]

Numerically, NV=0 and WV=(0;I_6) to about 2e-14 and 3e-15, respectively.
Thus V selects six smooth-coordinate candidates for kernel directions wherever
the assumed rank branch and chart persist. This is not a covariant physical
gauge/source classification, nor does augmented invertibility alone prove that
all these targets lie in the image throughout a neighborhood.

## General first prolongation

The local Taylor data are translated consistently: E3 includes E4 contracted
with the displacement; psi2 includes psi3 and psi4 terms; lambda2 includes
lambda3. For the seven field blocks entering F0, form their four holonomic
derivatives and evaluate DF0 on each direction. Five-point differences compute
these derivatives without using the origin-specific 384-row formula.

The 224 normal higher columns are evaluated separately using the polynomial
highest-jet dependence, with symmetric differences of size 16. No small spatial
difference is used to determine their rank. At the origin their matrix agrees
with the previous extracted matrix to 1.13e-10 in Frobenius norm. The general
first derivative agrees with the prior formula to 7.54e-10.

Write H for the resulting 272-vector, A for its normal-higher derivative, and B
for its derivative along V while keeping the prescribed higher data fixed.
For a first-order correction, eliminating normal higher changes gives

\[
 G\,\delta q=-L^\top H,\qquad G=L^\top B,\qquad L^\top A=0.
\]

This is a tangent system. The earlier exact joint affinity at the special point
has not been established for general coordinates. In particular, the following
linear corrections are not advertised as solutions of the nonlinear equations.

## Results

Coordinates use the previous Taylor convention, with r=1/16384. This diagnostic
radius is not the much smaller uniform normal-majorant radius, and is not a
certified source-gate radius.

| Sample | rank A | rank G | smallest singular value G | projected H | after best linear source correction |
| --- | ---: | ---: | ---: | ---: | ---: |
| origin | 160 | 6 | 0.134596 | 1.81e-10 | 1.79e-10 |
| (r,0,0,0) | 160 | 6 | 0.134904 | 0.005230 | 0.004060 |
| (0,r,0,0) | 160 | 6 | 0.134552 | 0.004190 | 0.004060 |

Normal rank stays 40 at all three samples. Halving the directional step from
1e-4 to 5e-5 changes the full source-response matrix by at most 4.70e-7; the
six gate singular values change by less than 1.1e-8. First-prolongation values
change by at most 2.74e-9. These are numerical consistency checks, not rigorous
error bounds. The smallest gate singular value is well separated from this
observed numerical variation.

The source correction changes the primary 68 residuals by at most 1.3e-14,
consistent with the coordinate kernel section. It does not repair their already
nonzero off-origin residuals (up to 6.03e-7).

## Interpretation and next step

The tested obstruction is not disappearance of the six-source tangent gate:
that gate remains injective in these samples. Instead, the first prolongation
has compatibility components outside the source image. There are 112 projected
directions and a six-dimensional source image, leaving 106 tangent compatibility
directions. Equal dimensions of the six source coordinates and six earlier mixed
left gates do not identify those spaces.

The nonzero remainders belong to this particular finite Taylor continuation.
They neither prove a regional solution impossible nor prove that a nonlinear
source change cannot help. They show that simply transporting the pointwise
source rule is not yet a closed propagation argument.

Next, identify the remaining projected components against differentiated known
constraints and determine which require changing prescribed tangential higher
data. Such changes must retain all lower equations and be checked against the
full higher residual, rather than only the six source-sensitive combinations.

## Reproduce

Run `python -B analysis/HC_Cartan_General_First_Source_Gate.py` and
`python -B -m unittest scripts.qsc_audit.tests.test_hc_cartan_general_first_source_gate`.
The highest-response matrices use the existing fingerprinted dependency/cache
services. Three independent point diagnostics run with two local workers.
