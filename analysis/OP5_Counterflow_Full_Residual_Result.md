# Full spinor residual: current-compatible counterflow is not on shell

2026-10-27. Follow-up to OP5_Resonance_Exchange_Current_Gate_Closure.md. Reproducible script OP5_Counterflow_Full_Residual_Check.py and output JSON with the same stem.

## Explicit differentiable fields

Use N=16, rho=sqrt(x^2+y^2), v=(x,y,z)/t, gamma=(1-|v|^2)^(-1/2), n=N/(2gamma). On rho>0 choose

chi_+=(1,i(x+iy)/rho)/sqrt(2),
chi_-=(1,-i(x+iy)/rho)/sqrt(2).

These have opposite spin along (-y,x,0)/rho. With a=sqrt((gamma+1)/2), define

U=sqrt(n) (a chi_+, a gamma/(gamma+1) sigma.v chi_+),
W=sqrt(n) (a chi_-, -a gamma/(gamma+1) sigma.v chi_-).

A=cos(theta)U, B=sin(theta)U, C=W, theta=asin(8t/N)/2. All four spacetime derivatives are computed analytically before evaluation. This includes the spin texture derivatives, not merely local constant spinors.

## Necessary chart correction to the previous pointwise formula

The earlier p,q formulas were in an adapted local frame with a chosen relative spinor phase. They cannot be copied unchanged as real coefficients into every fixed-coordinate spinor chart. In the explicit chart above, the source-producing imaginary overlap is proportional to rho/t, not |x|/t. Therefore use

p=3 cos(theta)/(2 rho Delta), q=-3 sin(theta)/(2 rho Delta),
Delta=cos(2theta), A_i=spin_i G, A_0=0,
G=[[0,0,p],[0,0,q],[p,q,0]], Omega=h_m Y,
h_m=16 gamma/(N Delta).

This agrees with the earlier adapted formula on the positive x axis. Away from that axis it is an explicitly chosen chart-specific connection that restores the current gates, not a proof of a globally transformed gauge field. A spatially varying basis transformation would also require its derivative connection. The initial uncorrected |x| denominator failed individual current projections at the second test point; that failed control is why this adjustment was made. The earlier pointwise algebra remains valid, but no unqualified global extension should be inferred from it.

## Full equation tested

R=i partial_t Psi+i alpha^i partial_i Psi - (alpha^i A_i+beta_D Omega)Psi.

Analytic derivatives evaluated with 30-digit arithmetic give:

Point (t,x,y,z)=(1,3/5,0,0):
||R_A||=7.9589700052, ||R_B||=3.9213541894, ||R_C||=4.8534065929.

Point (1,2/5,1/5,1/5):
||R_A||=9.4870761878, ||R_B||=4.4957702561, ||R_C||=6.8662361299.

At both points Im(psi_a^dagger R_a) and Im(Psi^dagger S R) vanish to about 1e-29 or better. These are precisely the phase-current and selected-current projections checked earlier. The substantial full residual therefore lies beyond those necessary tests. Norms are in the arbitrary comparison normalization, not measured physical errors. They are numerical evaluations of analytic expressions, not interval-certified bounds; their scale is far above rounding.

## Conclusion and next route

This particular prescribed field plus fitted connection/resonance is not a solution of the full probe equations, despite matching the current gates. The result is not a no-go for the native model or for all non-scalar couplings. It is also not evidence that a different frame automatically fixes the issue.

Next isolate the spinor components of R and test whether the operator algebra actually allowed by the native projected model can supply them, while retaining the coframe conditions. Merely fitting an arbitrary 12-by-12 Hermitian potential would not establish a physical derivation. Gauge/action, gravitational and multiplier equations remain unchecked. OP5 remains open. Local uncommitted note.
