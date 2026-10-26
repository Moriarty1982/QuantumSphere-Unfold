# OP5: which readout, in which order, at which time?

Checkpoint: `OP5-READOUT-ORDER-2026-10-26`.
Base Git revision: `3fa5ba9440d0985fbb2b3786eaebe56a887cfe6a`.
This is an exact finite instrument comparison. It does not derive a native
field Hamiltonian, a preferred observer, or an OP5 vacuum energy. Its order
and timing results are established before assigning any energy interpretation.
No source manuscript, index or Git state is changed.

## 1. The necessary distinction

There are three different operations:

1. **Passive change of representation:** the same state, dynamics and meter
   are all represented in a different basis. Complete record probabilities
   are invariant.
2. **Active measurement or coupling:** a particular apparatus interacts with
   the state. The resulting completely positive instrument can disturb it.
   Different apparatus axes and orders can give different physical protocols.
3. **Selective retention:** only an outcome or branch is kept. Its conditional
   state and survival probability are not the unconditional ensemble.

Thus "which frame reads what" matters if it specifies a different coupling,
instrument, clock synchronization or selection. It cannot change a prediction
solely through passive relabelling of the same complete experiment.

## 2. Exact instrument and meter realization

Use a qubit state

\[
\rho=\tfrac12(I+b\cdot\sigma),\quad b\in\mathbb R^3,
\quad |b|\le1,
\]

and a unit real axis n. The source's compensator uses `n=x`. Its rank-one
outcome projectors, instrument branches and unconditioned channel are

\[
P_s^n=\tfrac12(I+s\,n\cdot\sigma),\quad
\mathcal I_s^n(\rho)=P_s^n\rho P_s^n,\quad s=\pm1,
\]
\[
p_s^n=\operatorname{tr}\mathcal I_s^n(\rho)
=\tfrac12(1+s\,n\cdot b),\qquad
\mathcal D_n(\rho)=\sum_s\mathcal I_s^n(\rho).
\]

For `p_s^n>0` the normalized conditional state is exactly `P_s^n`.
At zero probability that conditional state is undefined, not a state that
may be silently normalized. The unnormalized instrument maps remain linear
and completely positive; the normalized conditional map is nonlinear in rho.

The Bloch map of the nonselective channel is the rank-one projection

\[
b\longmapsto\Pi_n b,
\qquad\Pi_n=nn^{\mathsf T}.
\]

A finite meter realizes it: initialize an ancilla in |0> and apply
`V=P_+^n tensor I+P_-^n tensor sigma_x`. Tracing out the ancilla gives D_n.
More generally, a controlled apparatus unitary `W` multiplies the off-diagonal
blocks by the pointer overlap `tr(sigma_env W^dagger)`. It is the actual
coupling and apparatus state, not an observer's description alone, that
controls disturbance. This is the same instrument distinction used in r28.

The source's real disk has `b_y=0`. Axes with `n_y=0` preserve it, but a
general free Hamiltonian need not. All calculations below either stay on
that disk explicitly or use the full positive Bloch ball.

## 3. Order dependence without fitted parameters

For two axes n,m,

\[
\Pi_m\Pi_n b=(m\cdot n)m(n\cdot b),\qquad
\Pi_n\Pi_m b=(n\cdot m)n(m\cdot b).
\]

Their nonselective channels commute for all states if and only if the axes
are parallel (including opposite signs) or orthogonal. If `m dot n` is
nonzero, equality of the two matrix products implies `mn^T=nm^T`, hence
parallel axes; if the dot product is zero both compositions vanish on the
Bloch vector. This criterion is about final nonselective states, not about
the entire labeled sequence of selective records.

Take the valid pure state and two real-disk axes

\[
\rho_z=\tfrac12(I+\sigma_z),\qquad
x=(1,0,0),\qquad n=(x+z)/\sqrt2.
\]

Protocol A measures x first and n second:

\[
\mathcal D_n\mathcal D_x(\rho_z)=I/2.
\]

Protocol B measures n first and x second:

\[
\mathcal D_x\mathcal D_n(\rho_z)
=\tfrac12(I+\tfrac12\sigma_x).
\]

A subsequent **same compensator readout** has

\[
p_+^x(A)=1/2,\qquad p_+^x(B)=3/4.
\]

Both outputs are positive and normalized (determinants 1/4 and 3/16).
No energy observable, fitted parameter or frame singularity is used in this
counterexample. Same-axis repetitions and orthogonal x/z axes are exact
commuting negative controls; the maximally mixed input is fixed by every D_n.
Orthogonal selective measurements can still have order-dependent recorded
joint probabilities for a nonuniform initial state, despite this equality
of final nonselective states.

For consecutive selected outcomes s on n, then t on m, the joint probability is

\[
p(s,t)=\tfrac14(1+s\,n\cdot b)(1+st\,m\cdot n).
\]

This formula follows by retaining the unnormalized first branch and tracing
the second. Reporting only the normalized surviving branch would discard
the first probability factor and can falsely suggest that a selected result
occurred in the complete ensemble.

## 4. Timing and free evolution

Introduce a **comparison** Hamiltonian, not a native derivation,

\[
H=\frac{\hbar\omega}{2}\sigma_y,\quad
U_\tau=e^{-i\omega\tau\sigma_y/2}.
\]

It preserves the real disk. Starting at rho_z, waiting tau before the first
compensator readout gives

\[
p_+^x(\tau)=\tfrac12[1+\sin(\omega\tau)].
\]

It is 1/2 at zero delay and 1 at `tau=pi/(2 omega)` for positive omega.
If the x measurement is performed nonselectively at time zero first, the
state becomes I/2 and stays there under this free evolution: the later
probability remains 1/2. These are genuinely different interventions.

For a selected first outcome n,s, then a delay tau and a measurement m,t,

\[
p(s,t;\tau)=\tfrac14(1+s\,n\cdot b)
[1+st\,m\cdot R_\tau n],
\]

where R_tau is the Bloch rotation generated by the specified H. A fully
specified protocol needs the order, delay, Hamiltonian, outcome labels and
whether earlier outcomes were discarded or selected.

If `[H,P_s^n]=0`, inserting any free delay does not change that outcome
probability for any initial state. Conversely, invariance of all such
probabilities for all states and all delays implies `U_tau^dagger P_s U_tau=P_s`
and hence this commutation. An unchanged probability for one state or one
delay does not establish the general criterion.

There are also exceptional times. In the displayed y-rotation, a pi rotation
swaps the x outcome projectors. The *nonselective* dephasing channel commutes
with that rotation, but fixed + and - labels exchange. At a 2pi rotation
the labels are preserved too. This prevents confusing equality of a summed
channel with equality of every selective outcome record.

A different choice `H=(hbar omega/2)sigma_z` sends a real x-polarized state
to a y-polarized state after a quarter period. That leaves the source's real
disk. One must then extend the model to the full Bloch ball or justify a
restriction on the Hamiltonian; discarding the y component is another active
channel, not a harmless notation convention.

## 5. Fixed passive covariance of the complete experiment

Let C be a fixed unitary representation change. Transform **everything**:

\[
\rho'=C\rho C^\dagger,\quad H'=CHC^\dagger,\quad
P_s'=CP_sC^\dagger,\quad K_j'=CK_jC^\dagger.
\]

Then `U_tau'=C U_tau C^dagger`. Every instrument sequence, including free
delays, telescopes to `C (original unnormalized branch) C^dagger`.
Cyclicity of trace proves invariance of all joint probabilities and energy
expectations. Conditional states transform in the same way whenever their
probability is positive. The order effect in section 3 is therefore itself
representation-covariant; it does not disappear or arise by changing basis.

Rotating only rho while holding the meter fixed is an active relative
preparation change, not this passive comparison. Transforming only the
readout is an apparatus change. If C depends on time, the generator also
needs a connection term, derived below. Antiunitary time reversal and spacetime Lorentz
observer transformations require their own time/observable transformation
rules and are not identified with this qubit unitary basis calculation.

### 5.1 Time-dependent passive representation: which frame when

Let `C(t)` be a differentiable unitary and compare the **same physical events
and clock parameter** in the two descriptions. Set `|psi'(t)>=C(t)|psi(t)>`.
Differentiating the transformed state in the Schrodinger equation gives

\[
H'_{\rm gen}(t)=C(t)H_{\rm gen}(t)C^\dagger(t)
+i\hbar\dot C(t)C^\dagger(t).
\]

The last term is Hermitian because differentiation of `C C^dagger=I`
makes `dot(C) C^dagger` anti-Hermitian. If `U(t_2,t_1)` is the original
propagator, the exact transformed propagator is

\[
U'(t_2,t_1)=C(t_2)U(t_2,t_1)C^\dagger(t_1).
\]

It has the correct identity at coincident times, preserves composition, and
differentiation verifies its generator H'_gen. Omitting the connection term
while rotating states and meters describes different dynamics in general.

If a measurement at an event `t_j` has original Kraus operators `K_{j,r}`,
allowing different pre- and post-event coordinate choices gives

\[
K'_{j,r}=C(t_j^+)K_{j,r}C^\dagger(t_j^-).
\]

For a continuous representation these two C values are the same. A jump
in coordinate convention is represented by this endpoint rule, rather than
by pretending that its derivative is an ordinary smooth Hamiltonian term.
Completeness is preserved:
`sum_r K'^dagger K'=C(t_j^-)(sum_r K^dagger K)C^dagger(t_j^-)=I`.

In a complete branch containing any number of delays and outcomes, adjacent
endpoint C factors cancel. The branch operator therefore transforms as
`B'=C(t_final) B C^dagger(t_initial)`, and

\[
\rho'_{\rm branch}=C(t_{\rm final})\rho_{\rm branch}
C^\dagger(t_{\rm final}),\qquad
\operatorname{tr}\rho'_{\rm branch}
=\operatorname{tr}\rho_{\rm branch}.
\]

Thus all joint outcome probabilities remain the same even for a changing
passive frame. Positive-probability conditional states transform by the same
endpoint conjugation. Changing the measurement order, delay, chosen output
labels or physical clock is not part of this passive invariance statement.

### 5.2 Generator connection is not automatically physical energy

If the original experiment measures an energy observable H_phys, its passive
representation is

\[
H'_{\rm phys}(t)=C(t)H_{\rm phys}(t)C^\dagger(t),\qquad
\operatorname{tr}(\rho'H'_{\rm phys})
=\operatorname{tr}(\rho H_{\rm phys}).
\]

Even when H_gen and H_phys coincide in the original description, their two
transformed formulas differ by the connection term. The coordinate generator
H'_gen should not automatically be relabelled as the apparatus's physical
energy observable. A physical detector in a rotating or accelerating frame
can measure a different observable, but that requires an actual observer,
clock and apparatus model rather than this passive identity.

A decisive control is the global phase `C(t)=exp(i alpha t) I`, for a real
constant alpha with units of inverse time. Then

\[
\rho'=\rho,\qquad
H'_{\rm gen}=H_{\rm gen}-\hbar\alpha I,\qquad
H'_{\rm phys}=H_{\rm phys}.
\]

Every recorded probability and physical-energy expectation is unchanged.
The apparent generator offset therefore does not supply a new physical
vacuum energy or cancel an independently specified gravitational vacuum
term. A real local metric-volume counterterm changes the action and its
stress response; a passive phase convention does not derive such a change.

Active driving, apparatus rotation relative to the system, a changed bath or
clock state, and genuinely different readout couplings are separate physical
protocols. They may alter the dynamics or readouts and require a complete
instrument/time model. A generic C(t) can also leave the real state disk,
so the representation calculation then uses the full Hilbert space; one
must not insert an unannounced projection back into the disk.

## 6. Energy transfer is a separate later question

For a fixed system Hamiltonian `H=h_0 I+h dot sigma`, an active nonselective
measurement changes its mean by

\[
\Delta E_n=\operatorname{tr}H[\mathcal D_n(\rho)-\rho]
=h\cdot(\Pi_n-I)b.
\]

Its sign can be positive, negative or zero. In the order example of section
3, the separately declared choice `H=sigma_x` gives final system energies
0 in A and 1/2 in B, from zero initial energy. With `H` proportional to
sigma_y both real-disk protocols have zero mean-energy change while their
readout probabilities still differ. The order effect therefore does not
require an energy-loss explanation.

These quantities are **system energy changes**. Calling them work rather
than heat or measurement back-action requires a meter/control Hamiltonian
and a total energy balance. A selective branch can have a different energy,
but its probability-weighted average must be used for the unconditional
account. An identity shift in H cancels from every Delta E above and
therefore leaves the absolute vacuum coefficient undetermined.

## 7. What this establishes for the OP5 question

The user's question has a positive, precise answer: before discussing energy,
it matters whether different "frames" actually specify different instruments,
couplings, input states, orderings, delays, masks or postselection rules.
These differences can change readouts. A passive consistent re-expression
of one experiment cannot.

### Native counterpart negative control

On the source's real disk, the corrected native counterpart `U=sigma_y`
sends a real readout axis n to -n. But

\[
\mathcal D_n=\mathcal D_{-n},\qquad
P_+^{-n}=P_-^n,\quad P_-^{-n}=P_+^n.
\]

Thus naming two readers M and T does not alone supply two noncommuting
nonselective measurements. The complete unordered measurement is the same;
only the outcome labels exchange. Keeping "+ in the reader's own frame"
instead selects opposite physical branches and changes the retained
subensemble. That is postselection and must include the rejected branches
and their probabilities. The order example requires genuinely different
relative axes or different couplings, not merely this sign reversal.

Nor does a difference of finite output states force different steady-state
energy. The Hamiltonian, readout axes, repeated schedule and reservoir can
possess symmetries that remove that difference; an actual repeated protocol
must be solved rather than inferred from one noncommuting pair.

Source r27 already separates selective survival from nonselective evolution;
r28 supplies controlled-meter examples whose coherence depends on the device
state and coupling. They support asking for an actual readout protocol.
r47 instead discusses generation-selective masks in **couplings**, under an
explicit model assumption; it is not a proof that observer choice changes
intrinsic mixing. Its later r51 terminology correction distinguishes time
reversal from the native tachyon frame. These notions must not be merged
because all are called a frame/readout somewhere in the history.

To apply the finite construction natively, OP5 still needs: explicit system
and apparatus states; an admissible map between their object types; which
readout each one implements; a native generator and time; meter back-action;
the complete trace-preserving instrument or declared selected branches;
and comparison of common final observables. Native closure-class preservation
and any physical energy/stress interpretation are separate proof obligations.

## Verification and source provenance

Command: `python -B analysis/OP5_Readout_Order_Timing_Check.py`.
The exact SymPy controls cover the order counterexample, positivity, same and
orthogonal axes, delay formula, special pi rotation, full-instrument passive
covariance, controlled-meter partial trace, system-energy changes and a
Hamiltonian leaving the real disk. No probabilistic simulation or fitted
parameter is used.

Sources at the pinned revision:

- `sources/research/parts/v490-post-release-layers.tex`, r27 model line 3842,
  r28 meter line 3996, r47 model assumption line 6315 and results line 6323,
  r51 corrections/results line 6781. SHA256:
  `232BDD631BAC34259BE48B6D326FBF6EAF38F084EE4BEC1A621658B3C964424E`.
- `formal/QSFormal/Frames.lean`, compensator `C`, port probabilities and
  distinction of J_B from port swapping. SHA256:
  `D05C812136899BC82FE1ACFE0D5FA39967477A9E5EB0BECD66F314A42B7BC03D`.
- Control script SHA256:
  `54FF687936A86579CC37B0C5D279E73F4C820AF9D691838A554A837B24D47726`.

Review provenance: bounded separate child-agent derivation within the same
overall session, exact finite controls, no new native physical claim and no
historical H32/H35 or Lean rebuild.
