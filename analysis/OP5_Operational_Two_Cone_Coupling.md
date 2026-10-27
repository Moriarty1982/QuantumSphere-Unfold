# Operational two-cone coupling test

2026-10-27. New explicitly auxiliary local model, not native field identification or a global solution. Builds on OP5_Relative_Connection_And_Free_Paths.md.

## Declared two-sector experiment

At a central-axis point before degeneracy, freeze the local coefficients of the two metrics. In the reference orthonormal chart the reference cone speed is 1 and the readout cone speed is v=d/f, 0<v<=1. Canonically normalize two real scalar test fields with Lagrangian

 L=1/2[(partial_t phi)^2-|grad phi|^2-m1^2 phi^2]
  +1/2[(partial_t chi)^2-v^2|grad chi|^2-m2^2 chi^2]
  -epsilon phi chi.

This is a local constant-coefficient comparison with an explicitly chosen common chart and interaction, not a derived native covariant action. The canonical field rescaling absorbs local volume/lapse factors; mass parameters refer to these coordinates. Take m1^2,m2^2>0 and epsilon^2<m1^2 m2^2 to avoid a negative homogeneous mass eigenvalue. Do not interpret mixed propagation as an instability by default.

For a Fourier mode define a=k^2+m1^2 and b=v^2 k^2+m2^2. The squared-frequency eigenvalues are

 omega_+/-^2=(a+b +/- sqrt((a-b)^2+4epsilon^2))/2.

Both are nonnegative under the stated mass condition. At large |k|, for v<1 the two front-speed branches tend to 1 and v. The algebraic coupling does not make the two principal cones equal. At v=1 there is one common cone with different mass eigenmodes. No finite-frequency group velocity is substituted for a causal front.

## Can the faster sector be observed by the slower detector?

For epsilon!=0 a source in phi contributes to chi through the coupled Green function. Perturbatively the cross response starts at -epsilon G_chi,ret * G_phi,ret (sign depends on source convention); support can extend beyond the chi-only cone by traveling mainly in the faster phi sector and converting locally near reception. The fastest cone remains an upper support bound for this constant-coefficient local hyperbolic system. Conversion response may be small; cone speed alone says nothing about experimental detectability or signal-to-noise. If epsilon=0 and the detector couples only to chi, there is no such cross-channel reception.

An observer using readout rods and clocks measures local intervals d ell_g=f dx and d tau_g=d dt on the central axis. The reference channel therefore has speed f/d=1/v in those units, whereas the readout null channel has speed 1. This is a dimensionless ratio of two channels, not a coordinate artifact once those operational couplings have been stipulated. It is not a prediction that actual light is superluminal, because neither the sector assignment nor this interaction has been derived from the paper.

Numerical example at t=(1/2)t*, t*=pi/32: v=0.794354694998..., so the reference channel is faster by factor 1.25888347648 relative to the readout null cone. Near the initial point the factor tends to 1. The frozen-coefficient model applies only locally; it does not compute long trajectories across the evolving background.

## Consequence for the relational-gravity hypothesis

A relative connection is operational only after defining physical sector couplings. With the explicit two-sector coupling above it leads to distinct signal cones, not automatically to universal ordinary gravitational behavior. Algebraic mass/mixing terms cannot repair their principal mismatch. To obtain a common observed cone one must derive common kinetic coupling, show the extra channel inaccessible, or establish a controlled effective regime; none is supplied merely by calling the relation ART.

The next native target is therefore the kinetic/derivative coupling of the ART/QFT readouts and physical detector, not a freely chosen mass/mixing coefficient. If the native action has derivative mixing, its full principal matrix must be computed. This is separate from choosing the absolute vacuum coefficient in OP5.

## Checks

OP5_Two_Cone_Coupling_Check.py verifies the characteristic polynomial and stable representative mass matrix and evaluates a finite large-k convergence sample. The analytic large-k limit supplies the limiting claim. No independent reviewer or experimental validation is claimed.
