# Bloch mapping and residual decomposition

2026-10-27. Two-point diagnostic for the explicit counterflow fields and connection from OP5_Counterflow_Full_Residual_Result.md. Script: OP5_Bloch_Residual_Decomposition.py; corresponding JSON holds all values. No native-model or global theorem.

## What is mapped

The normalized rest Pauli spinors have Bloch vectors s=(-y,x,0)/rho for A/B and -s for C. The separate normalized A/B amplitude vector m=(cos theta,sin theta) has Bloch vector (sin 2theta,0,cos 2theta). At N=16,t=1 this is (0.5,0,sqrt(3)/2). These are distinct degrees of freedom; neither sphere contains the full Dirac spinor.

## Definition of the diagnostic

Let R=i partial_t Psi-H Psi be the previous full residual. The missing instantaneous field velocity, holding the current spatial jets and H fixed, is delta(dot Psi)=iR. For each species at each point hold its specified boost B(+-v) fixed. The two vectors e_+=B(+-v)(chi_+,0)/sqrt(gamma) and e_-=B(+-v)(chi_-,0)/sqrt(gamma) form an orthonormal pair in the chosen lab-frame positive Euclidean norm. Orthogonality follows because the upper block of B^dagger B is gamma I.

Project iR onto the occupied vector, the opposite-spin vector in this pair, and the orthogonal complement in C^4. The three squared norms add to the full squared norm (checked numerically). Current conservation makes the coefficient along the occupied vector purely imaginary up to rounding, hence a phase direction, not an amplitude-growth direction. The opposite-spin coefficient describes Bloch-sphere tangent motion at fixed boost. The complement changes the relation between upper and lower Dirac components; it cannot be represented by changing just the rest spinor at that same boost.

The complement is NOT automatically a pure boost change, physical negative-energy production, antiparticles, tachyons, or spacetime curvature. Nor is the decomposition Lorentz-invariant or gauge-independent: it is a declared local diagnostic with fixed boost, spinor chart and norm.

## Results

At P1=(1,0.6,0,0), essentially 100% of the summed squared residual norm is in the complementary Dirac directions. Phase and spin-flip projections are at floating-point rounding scale.

At P2=(1,0.4,0.2,0.2), 94.6619815% is complementary; 5.3380185% lies in the occupied phase directions; the pure spin-flip contribution is at rounding scale. These are squared-norm fractions, NOT probabilities or percentages of a physical discrepancy. The computation evaluates analytic derivatives at 30 digits, then performs this projection in ordinary complex floating point, so tiny values around 1e-16 in velocities or 1e-32 in squared components are not exact-zero proofs.

After projecting A and B onto their common occupied spinor, their normalized amplitude velocity gives a mixing-Bloch velocity difference approximately (0,-0.774596669,0) at P2 and zero at P1. A global A/B common phase cancels from this Bloch derivative. This y-direction therefore detects a relative phase mismatch, not a missing change in the A/B population imbalance. Spin-Bloch velocity differences are zero within numerical precision at both tested points.

## Interpretation and next step

The Bloch diagnostic corrects the earlier suggestion that the residual might primarily be a wrong spin rotation. For these two samples it is predominantly outside the fixed-boost rest-spin subspace. One sample additionally has a relative A/B phase mismatch. Spatial spin texture derivatives were included; their presence does not imply that the resulting residual is itself a pure spin-rotation tangent.

Next separate the complementary directions into the tangent space of admissible boost changes and directions outside that tangent space, accounting for shared versus independent boosts and the coframe constraints. The present result does not justify changing a frame by fiat, nor does it establish necessity of curvature. Full gauge/action, stress and native coupling derivation remain open. OP5 remains open.

The visualization selects between the two actual computed points; it does not interpolate a solved field evolution. The arrow is the local projected missing mixing velocity scaled by 0.5 for legibility, not an integrated trajectory. Local uncommitted research artifacts.
