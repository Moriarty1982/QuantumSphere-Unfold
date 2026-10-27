# Relative connection, free trajectories and tidal test

2026-10-27. Exact comparison of the two metrics of OP5_Two_Probe_Exchange_Evolution.md. These metrics have not been shown to solve a common self-induced physical action.

## Two metrics on the same event patch

The reference metric is eta in x=(t,x1,x2,x3). The reconstructed flat metric is g=J^T eta J with J^a_mu=partial_mu Y^a, where

 Y0=sin(16t)(1/16+r^2), Yi=f(t)xi,
 f=(5+3cos(16t))/8.

Restrict to a patch with det J nonzero. Since reference Christoffels vanish in x, the relative tensor C=Gamma[g]-Gamma[eta] equals

 C^rho_mu_nu=(J^-1)^rho_a partial_mu partial_nu Y^a.

It is nonzero and transforms tensorially under a simultaneous change of chart for both metrics. Its coordinate entries alone are not invariant numbers, and it is not a Riemann curvature tensor.

## Exact initial-time connection

At t=0 set A=1+16r^2. Then J=diag(A,1,1,1). The only nonzero connection components are

 C^0_0i=C^0_i0=32xi/A,
 C^i_00=-96xi.

Thus a reference-rest trajectory x_i=constant is generally not g-geodesic. At this instant its g-unit tangent is u=(1/A,0,0,0), and its g-covariant acceleration has spatial components -96xi/A^2 and zero temporal component. Its magnitude is 96r/A^2 in these dimensionless model units. At the origin it vanishes. These statements concern the chosen model, not a measured gravitational field.

Conversely a g-geodesic initially at reference rest has coordinate acceleration d2xi/dt2=+96xi at t=0. Here reference proper time agrees with t to the required order because initial velocity is zero. The two acceleration formulas use different proper times and must not be compared as if their normalization were identical.

## Full family of freely falling trajectories

Straight, resting g-inertial trajectories have Yi=ai and Y0=T. Their x-chart expression is

 xi(t)=ai/f(t),
 T(t)=sin(16t)[1/16+|a|^2/f(t)^2].

For small enough t, T(t) is invertible and equals their g-proper time up to an additive origin. Since f=1-48t^2+O(t^4), xi=ai[1+48t^2+O(t^4)], giving the acceleration above. Two symmetric trajectories a and -a have coordinate separation 2|a|/f(t), which increases initially. Their equal-g-time physical separation in the Y chart is nevertheless constant 2|a|. Thus widening coordinate separation is not intrinsic geodesic deviation here. Reference-simultaneous and g-simultaneous distance comparisons must not be mixed; the symmetric pair has the same T(t).

## Curvature cancellation

Write the connection matrices C_mu=J^-1 partial_mu J. Direct differentiation, using partial_mu J^-1=-J^-1(partial_mu J)J^-1 and commuting mixed derivatives, gives

 partial_mu C_nu-partial_nu C_mu+[C_mu,C_nu]=0.

Therefore R[g]=0 identically on the nondegenerate patch, just as R[eta]=0. This proof includes off-axis derivative terms; merely differentiating axis-restricted connection coefficients would be invalid. The covariant geodesic-deviation equation for either metric has zero curvature term. A spatial gradient of relative coordinate acceleration does not by itself imply a nonzero Riemann tensor.

OP5_Relative_Connection_Check.py independently computes J, the connection and its derivative/commutator cancellation symbolically on the reflection-symmetric t,x slice at t=0 for arbitrary x. It confirms C^x_00=-96x and R_tx=0. The analytic matrix identity above establishes the full patch result; the slice check is not substituted for that proof.

## Physical interpretation

There is a genuine nonzero relationship between two separately flat connections under the stipulated identification of events. This supports investigating a relational gravity interpretation. If every physical clock, light signal and matter trajectory couples to g alone, local experiments here see flat special relativity; the reference connection is then only additional description. If distinct physical sectors couple to different metrics, the discrepancy can be operational, but requires an explicit common action and matter/clock coupling prescription. It is a two-metric hypothesis, not automatically ordinary general relativity. No such prescription or field equations have been solved in this example.

A nontrivial common dynamical completion might use relative-connection terms or change the geometric readout, but doing so is new model input. The observed nonzero C alone selects neither that action nor a vacuum coefficient and does not close OP5.
