# Exact evolution of the two-probe exchange witness

2026-10-27. Full reference-system solution and failed self-induced continuation. Conventions and g=8 from OP5_Two_Probe_Exchange_First_Jet.md. No native OP5 closure or nonlinear existence result.

Let u=e1, X=(x alpha_x+y alpha_y+z alpha_z)u, s=sin(gt), c=cos(gt), h=1-6/g. The chosen initial data A(0,x)=u, B(0,x)=2X have the exact reference evolution

 A=c u+2s X,
 B=h s u+2c X.

For the Hermitian coupling M=g sigma_y the equations in Hamiltonian form are

 partial_t A=-alpha_i partial_i A-g beta B,
 partial_t B=-alpha_i partial_i B+g beta A.

Since beta u=u, beta X=-X, and sum_i alpha_i alpha_i u=3u, substitution verifies both equations at every (t,x), not only at the initial point. Explicitly their right sides are -g s u+2g c X and gh c u-2g s X. Their total phase current is conserved. The polynomial spatial profile is for local analysis, not a finite-energy global state.

## Reconstructed coordinates

Using the symmetric cross-readout Y^a=Re(A^dagger K^a B)/2 gives, with r^2=x^2+y^2+z^2,

 Y0=(h/4)sin(2gt)+r^2 sin(2gt),
 Yi=f(t) x_i,  f=c^2+h s^2=1-(6/g)s^2.

All terms follow directly from the standard alpha algebra and real parts. In particular the third spatial component of X and the complex fourth component supply all three spatial directions.

At g=8, t=0 the coframe is diag(1+16r^2,1,1,1). Thus the initial-data construction already matches the reference metric only at the spatial origin, not on the whole initial slice.

On the time axis x=0 the coframe is

 E=diag(d,f,f,f), d=cos(16t), f=1-(3/4)sin^2(8t).

At t=0 it equals I. Nearby its determinant d f^3 remains nonzero, so the readout is genuinely a local flat metric. But its cone differs from the reference cone once d and f differ. A coordinate change to Y cannot remove the difference between two metrics on the same patch. At t=pi/32 the axis determinant vanishes. This is a failure of this readout chart/coframe, not proof of a physical singularity.

## Explicit induced-equation residual

Use the induced inverse coframe on the time axis, keeping the same coupling, and compute R_B=i Gamma_ind^mu partial_mu B-i g A. In the tetrad E=dY with constant internal matrices the pulled-back flat spin connection can be chosen zero. Direct substitution gives

 R_B=i c [gh/d+6/f-g]u
    =i cos(8t)[2/cos(16t)+6/(1-(3/4)sin^2(8t))-8]u.

Its expansion is R_B=544 i t^2 u+O(t^4). It vanishes at the initial point but not at nearby generic times. Similarly R_A=i s[-g/d+6/f+gh]u. This is a calculated failure of this reference evolution as a solution of the self-induced equations. The obstruction appears beyond the first-jet check.

For small t the induced null speed along the axis in the original x chart is |d/f|=1-80t^2+O(t^4), whereas the reference system has unit front speed. These are different model cones, not an observed change of physical c.

## Interpretation and next obligation

Two structured complex probes give rank four and a genuine exact Hermitian coupled evolution. The earlier one-point compatibility does NOT propagate under the reference dynamics. Adjusting g while retaining these initial gradients is not a free repair: E00(0)=1 requires g=8. Different source data, couplings or a nonlinear induced evolution may work and are not ruled out.

The next mathematical problem is to solve the implicit self-induced equations and the dictionary together, with compatible Cauchy data, instead of evolving a separate reference equation. Moreover, an actual common action with composite coframe or multiplier generally adds source reactions; these must be derived before claiming physical self-consistency. The derivative-dependent coframe makes ordinary linear-Dirac existence insufficient. This note establishes neither a no-go for that nonlinear system nor its well-posedness.
