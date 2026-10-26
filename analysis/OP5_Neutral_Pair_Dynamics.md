# OP5: conditional dynamics of a neutral state pair

Checkpoint: `OP5-PAIR-DYNAMICS-2026-10-26`.
Base revision: `3fa5ba9440d0985fbb2b3786eaebe56a887cfe6a`.
Scope: exact finite-dimensional constructions on the existing real state disk,
with their hypotheses. This is not a native MM/HC derivation, a new physical
frame convention, an action, or a solution of OP5. No paper or index is edited.

## Inputs and construction target

The source's corrected r28 identifies the native counterpart, on the real
disk, with the duality map `rho -> sigma_y rho sigma_y`, not the earlier
`J_B=sigma_x` reflection. Set

\[
U=\sigma_y=U^\dagger,\quad U^2=I,\quad
\rho(b)=\tfrac12(I+b_x\sigma_x+b_y\sigma_y+b_z\sigma_z).
\]

The **real source disk** has `b_y=0` and `b_x^2+b_z^2<=1`. On that disk
`U rho(b) U=rho(-b)`, so an equal convex mixture of a state and its
counterpart is I/2. We ask for dynamics realizing that mixture, and then ask
whether its fixed point determines energy or a cosmological vacuum term.
The comparison with the full Bloch ball is retained as a negative control.

## 1. A Markov generator with an exact disk attractor

Choose a constant rate `k>0`, measured in an as-yet unspecified time unit:

\[
\dot\rho=\mathcal L\rho=k(U\rho U-\rho).
\]

This is a legitimate Lindblad form with `L=sqrt(k) U`, since
`L rho L^dagger - (1/2){L^dagger L,rho}=k(UrhoU-rho)`.
It also has an elementary random-unitary construction: apply U at the
events of a rate-k Poisson process. Even event counts give I and odd counts
give U. Their probabilities yield the exact solution

\[
\rho(t)=[1-p(t)]\rho_0+p(t)U\rho_0U,\qquad
p(t)=\frac{1-e^{-2kt}}2.
\]

Hence

\[
b_x(t)=e^{-2kt}b_{x0},\quad b_z(t)=e^{-2kt}b_{z0},
\quad b_y(t)=b_{y0}.
\]

The map is trace-preserving, positive and completely positive by its Kraus
operators `sqrt(1-p) I` and `sqrt(p) U`. It preserves the real disk, and the
semigroup law follows either from the generator or from multiplication of
the exponential factor. On the real disk I/2 is the **unique** stationary
state and every initial state approaches it.

For the full Bloch ball the stationary set is instead

\[
\rho_*=\tfrac12(I+b_y\sigma_y),\qquad |b_y|\le1.
\]

Thus the generator is dephasing in the U eigenbasis, not a universally
depolarizing qubit dynamics. Claiming uniqueness on the full ball would be
false, even for the two pure sigma-y eigenstates.

### Information and finite time

On the real disk, with `r(t)=sqrt(b_x^2+b_z^2)`,

\[
r(t)=e^{-2kt}r_0,\qquad
\operatorname{tr}\rho^2=\tfrac12(1+r^2),\qquad
\frac{d}{dt}\operatorname{tr}\rho^2=-2kr^2.
\]

The eigenvalues are `(1+r)/2,(1-r)/2`. For `0<r<1` their base-2 entropy obeys

\[
\dot S=kr\log_2\frac{1+r}{1-r}\ge0.
\]

The initial derivative is singular for a pure input, and S tends to one bit.
A nonzero r_0 never reaches exact zero at a finite Markov time. For a declared
tolerance `0<epsilon<r_0`, the exact bound is
`t >= log(r_0/epsilon)/(2k)`. A numerical detector zero is not exact I/2.
Neither this entropy nor its production is a physical energy density.

## 2. Unequal pair rates and the equilibrium assumption

The simplest two-label preparation model has probabilities `p_M,p_T`,
`p_M+p_T=1`, and rates `a>0` for M->T, `b>0` for T->M:

\[
\dot p_M=-a p_M+b p_T,\qquad
p_M(t)=\frac b{a+b}
+\left(p_M(0)-\frac b{a+b}\right)e^{-(a+b)t}.
\]

For fixed preparations `rho_M=rho(b_0)` and `rho_T=rho(-b_0)` on the disk,
their mixture has Bloch vector `(p_M-p_T)b_0`. Its stationary imbalance is

\[
p_M^*-p_T^*=\frac{b-a}{a+b}.
\]

The stationary detailed-balance equation is `a p_M^*=b p_T^*`.
Exact I/2 requires equal rates `a=b` unless b_0 was zero already. The
symmetric generator above corresponds to equal label rates on this pair;
unequal rates do not establish neutral equilibration.

If the labels are physical energy levels coupled to a thermal bath, the
additional thermal detailed-balance hypothesis would impose
`a/b=exp[-beta(E_T-E_M)]`. Equal rates then require degeneracy or an
infinite-temperature limit (or a nonthermal external drive instead of that
thermal hypothesis). The rate balance must be derived, not chosen solely
to obtain neutrality. For nonorthogonal or mixed preparations, these labels
are preparation records; interpreting them as distinct energy eigenstates
requires further structure.

## 3. Finite-time system-plus-ancilla realization

Introduce an ancilla initially in `|0><0|` and the joint unitary

\[
W_\theta=e^{-i\theta(U\otimes\sigma_x)}
=\cos\theta\,I_4-i\sin\theta(U\otimes\sigma_x).
\]

Its reduced map after discarding the ancilla is exactly

\[
\mathcal E_\theta(\rho)
=\cos^2\theta\,\rho+\sin^2\theta\,U\rho U,
\]

with Kraus operators `K_0=cos(theta)I`, `K_1=-i sin(theta)U`.
At `theta=pi/4` the real disk is sent exactly to I/2 in one interaction.
On the full ball its sigma-y component remains. This is an explicit
system-environment realization of neutral mixing, not a new theorem about
the native field.

If `H_int=hbar*g U tensor sigma_x` with constant `g>0` and no unaccounted
free evolution, then `theta=gt` and the disk-neutral time is `pi/(4g)`.
With a noncommuting free Hamiltonian the displayed solution is no longer
automatic; a justified interaction-picture or controlled coupling is needed.

One closed ancilla does **not** give irreversible attraction: at theta=pi/2
the state is `U rho U`, and at theta=pi it revives to rho. The reduced entropy
can subsequently decrease. For a pure initial system the joint state remains
pure, and the intermediate reduced entropy records system-ancilla
correlations rather than information destruction in the joint system.
Resetting or replacing ancillas supplies a reservoir assumption.

The Markov semigroup is recovered at the channel level by choosing
`sin^2 theta(t)=(1-exp(-2kt))/2`, for which theta approaches pi/4 only
asymptotically. This family is not the constant-g closed-ancilla orbit.

## 4. Exact comparison with existing r27 and r28

The source r27 step is a different channel: rotate by
`V_alpha=exp(-i alpha sigma_y)` and then measure nonselectively in the
compensator x basis. With `C=(I+sigma_x)/2`, `A=(I-sigma_x)/2`, it is

\[
\mathcal M_\alpha(\rho)
=C V_\alpha\rho V_\alpha^\dagger C
+A V_\alpha\rho V_\alpha^\dagger A.
\]

On the disk,

\[
b'_x=b_x\cos(2\alpha)+b_z\sin(2\alpha),\qquad b'_z=0.
\]

Thus r27 projects onto one axis after a rotation; it is not generally the
radial contraction `b -> cos(2theta)b` of E_theta. After the first r27 step,
the successive x components are multiplied by cos(2alpha). At pi/6 this
factor is 1/2. For example a z-polarized state at alpha=0 becomes I/2 under
r27, while E_0 leaves it unchanged; the two maps are not identical.

The r28 partial-swap construction with a state's own opposite counterpart
does give the same reduced radial formula as E_theta on the real disk,
because rho and its counterpart commute. This note provides an explicit
alternative dilation and a continuous Markov comparison for that already
recorded reduced map. It does not claim to discover or natively derive it.
Maintaining a fresh state-dependent counterpart at each iteration has a
preparation/correlation cost that is absent from the formal reduced map.
The random-unitary dilation can instead implement the fixed U operation
without preparing a copy of an unknown system state.

### The C5 score is not automatically the Bloch radius

At theta=pi/6, E_theta multiplies r by 1/2 and r^2 by 1/4. The r27 selective
survival is cos^2(alpha)=3/4 at alpha=pi/6, a different readout. If a *toy*
score is declared to be r^2, a 3/4 step factor requires theta=pi/12, or a
Markov sampling interval `Delta t=log(4/3)/(4k)`. These choices do not prove
that the native C5 residual equals r^2 or supply a physical clock. This is a
necessary readout distinction, not a new C5 closure claim.

## 5. Energy and the vacuum coefficient

For a fixed system Hamiltonian

\[
H=E_0 I+h_x\sigma_x+h_y\sigma_y+h_z\sigma_z,
\]

the Markov model gives

\[
\frac{d}{dt}\langle H\rangle
=k\operatorname{tr}\rho(UHU-H)
=-2k(h_xb_x+h_zb_z).
\]

The sign is not universally negative. If H commutes with U, system energy is
conserved while the real-disk entropy can increase. Otherwise a bath or
external coupling must account for energy exchange. The unitary dilation
conserves the energy of its own specified total Hamiltonian, but does not
automatically conserve an independently chosen `H_system+H_ancilla`.

Most importantly, replacing H by `H+C I` changes none of the commutator or
mixing dynamics and changes every normalized state's mean energy by C.
At the neutral disk state the mean energy is E_0, an undetermined offset,
not necessarily zero. Neutralization determines neither the absolute energy
reference nor a spacetime volume density. A constant term in a gravitational
action is physically relevant even though an identity Hamiltonian shift is
invisible to these reduced state equations. Consequently the dynamics cannot
fix that gravitational constant without a metric-dependent completion.

In a thermal interpretation, I/2 is the Gibbs state for finite inverse
temperature only if H is degenerate (or beta=0). A unital equal-rate channel
with nondegenerate H may describe noise or driving, but calling its neutral
fixed point a unique zero-temperature physical vacuum would be false.

The normalized state rho and its unit trace do not specify a conserved
stress tensor, a physical mode density, a physical clock, or the variation
of a regulated spectral action with respect to the spacetime metric. The
previous OP5 action/subtraction/target obligations therefore remain.

## 6. QAM status and exact missing physical data

The state family, channel graph, time parameter, counterpart map and readouts
are now explicit mathematical objects. The supplied maps can be represented
as QAM state/operator/readout data. Complete positivity and the stated disk
invariance are proved, but are not a proof of preservation of a separately
defined native QClEq closure class. Such `QAdmTransport` requires its own
native bridge and guards.

To promote the model into a physical candidate requires:

1. A native state/field identification and the correct counterpart map, with
   the real-disk restriction or an explicit y-component treatment.
2. The interaction mechanism and why the rates are equal, including reservoir
   state, preparation, refresh and correlations, or a different equilibrium.
3. A physical time and a derived k or g, not a fit obtained by choosing a
   sampling interval to reproduce 3/4.
4. System, environment and interaction Hamiltonians plus a total energy/stress
   balance, including the physical density of modes.
5. A metric-dependent action and a fixed renormalization prescription that
   can determine a vacuum coefficient rather than leave the H+C I freedom.

**Bounded constructive result:** there is an exact symmetric Markov attractor
and an exact finite-time ancilla realization of neutral mixing on the real
disk. They provide genuine specified dynamics, not just a proposed word
"neutral". Their microscopic physical origin, energy accounting and Lambda
coefficient remain unproved and underdetermined.

## Verification and provenance

Command: `python -B analysis/OP5_Neutral_Pair_Dynamics_Check.py`.
All exact symbolic controls passed: generator and solution, semigroup law,
full-ball exception, dilation unitarity and partial trace, finite neutral
angle and revival, unequal-rate balance, energy-shift freedom, exact r27 map,
and the squared-radius/selective-survival distinction.

Sources are the r27 model (`subsec:v490-r27-model`, line 3842) and corrected
r28 map (`subsec:v490-r28-correction`, line 3980) in
`sources/research/parts/v490-post-release-layers.tex`, and the existing
`formal/QSFormal/Frames.lean` definitions. No Lean rebuild or historical
test-suite rerun is claimed. The elementary quantum channel construction is
proved above rather than attributed to a new external physical theorem.

SHA256 at this checkpoint:

- `v490-post-release-layers.tex`:
  `232BDD631BAC34259BE48B6D326FBF6EAF38F084EE4BEC1A621658B3C964424E`.
- `formal/QSFormal/Frames.lean`:
  `D05C812136899BC82FE1ACFE0D5FA39967477A9E5EB0BECD66F314A42B7BC03D`.
- `analysis/OP5_Neutral_Pair_Dynamics_Check.py`:
  `049FC00E8A00BEC562DA042829721392BC41330B4131AF9A7C98C773B22AA30A`.

Review provenance: separate bounded child-agent derivation and symbolic
controls within the same overall session; not independent physical evidence.
