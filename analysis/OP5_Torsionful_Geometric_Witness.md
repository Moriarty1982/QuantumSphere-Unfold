# Explicit torsionful geometric witness for the cross-readout identity

2026-10-27. Geometry-only exact witness. No spinor realization, native action solution or physical torsion prediction.

## Necessary condition

For a Lorentz-compatible connection and E^a=(1/2)D j^a, integrability gives T^a=(1/2)R^a_b j^b. Antisymmetry of R_ab implies j_a T^a=0. Arbitrary torsion therefore cannot be inserted as a repair. In particular a curvature-free connection would also force T=0 for this exact dictionary; a generic teleparallel torsion ansatz is not automatically compatible.

## Construction on t>0

Choose the Minkowski coframe E0=dt, Ei=dxi, eta=diag(-1,1,1,1), and the timelike vector j^a=(2t,0,0,0). Let the independent Lorentz connection be

 omega^i_0=dxi/t, omega^0_i=dxi/t, omega^i_j=0 (spatial i,j).

The equal mixed components satisfy omega_ab=-omega_ba after lowering with eta. Direct evaluation gives

 D j^0=2dt, D j^i=2dxi,
 E^a=(1/2)D j^a.

The torsion and connection curvature are

 T0=0, Ti=-(1/t)dt wedge dxi,
 R^i_0=R^0_i=-(1/t^2)dt wedge dxi,
 R^i_j=(1/t^2)dxi wedge dxj.

Hence (1/2)R^i_b j^b=-(1/t)dt wedge dxi=Ti and j_a T^a=0. The integrability and metric compatibility hold on every patch with t>0. The t=0 boundary is excluded.

## Which geometry is curved?

The metric itself is exactly Minkowski, so its Levi-Civita curvature vanishes. The independent metric-compatible connection has nonzero torsion AND nonzero connection curvature. These are two distinct connections; calling the metric curved because the independent connection is curved would be incorrect. Ordinary metric geodesics and autoparallels of the independent connection need not coincide. A matter action is required to determine physical trajectories.

This shows that allowing torsion is not algebraically empty: there are explicit nonzero-torsion pairs satisfying the cross-gradient dictionary. It does NOT show that the Einstein-Cartan connection equation with the specified probe spin and multiplier sources produces this omega.

## Missing dynamical realization

The selected vector j must still be realized as the native two-probe cross bilinear; both probes must obey their varied equations and any C7 constraint. The full coframe equation must determine lambda. The connection equation must then supply exactly the torsion above, rather than a freely chosen torsion. The pure vector-type torsion in this example is not generally the torsion produced by minimally coupled Dirac spin alone; multiplier or other justified sources would matter.

Consequently the current result is a nonempty geometric candidate class, not a completed alternative to the torsion-free no-go. A next dynamical test must compute the irreducible source components and coframe reaction from one declared action. No absolute vacuum coefficient has been selected.
