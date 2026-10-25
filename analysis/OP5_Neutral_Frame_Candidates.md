# OP5: neutral objects constructed from two frames or sectors

Date: 2026-10-25. Base Git revision:
`f2de387d66d6ab2da00ef28a14305729910d7ef1`.
This is a bounded construction check. No manuscript, release, issue or index
is changed. No identification with a physical cosmological constant is made.

## Sources and typing

`sources/research/parts/v490-post-release-layers.tex` supplies:

- r17, line 2442: the state disk, `|b|=sech(2 eta)`, and its eigenvalues;
- r18, line 2609: composable scale transport `X(sigma)=exp(k sigma)X(0)`;
- r24, line 3499: reference R, matter M, native tachyon T versus its projection
  `T|R`, and the distinction between pure R and maximally mixed photon P;
- r28, line 3980: correction of the native tachyon map from `J_B` to
  `z -> iz`, with `rho -> sigma_y rho sigma_y` and `b -> -b` on the real disk;
- H20/r35, line 4870; H23/r38, line 5239; H25/r40, line 5490.

`formal/QSFormal/Frames.lean` has exact statements `J_B_ρ`, `T_ρ`,
`J_B_port`, `J_B_swaps_iff`, `J_B_fixes_iff` and `reference_frame`.
These definitions were inspected; Lean was not rebuilt for this note.

The word "frame" has several meanings in these sources. A point on the real
scale line, a state-disk point, an internal complex structure, a triality
slot, and a Lorentz observer are not interchangeable without a supplied map.
The constructions below deliberately keep these meanings separate.

## A. A neutral reference from a pair of scale-line points

Let `sigma_1,sigma_2` be two finite real rapidities on the same oriented
one-dimensional scale line. Choose its ordinary distance and define

\[
\sigma_N=\frac{\sigma_1+\sigma_2}{2},\qquad
\delta=\frac{\sigma_1-\sigma_2}{2}.
\]

Relative to N the two rapidities are `+delta,-delta`. Thus for a weight-k
scale quantity the two relative factors are reciprocal:

\[
e^{k\delta}e^{-k\delta}=1.
\]

The construction is exchange-symmetric and equivariant under a common
shift: `N(sigma_1+chi,sigma_2+chi)=N(sigma_1,sigma_2)+chi`.
It does not assume either input is photon-like. In positive scale factors
`s_i=exp(sigma_i)`, its reference scale is the geometric mean
`s_N=sqrt(s_1 s_2)`.

The midpoint is unique **after** requiring equal rapidity distance to the
two points and locating it between them. Exchange symmetry and common-shift
equivariance alone do not make it unique: adding any even function of
`sigma_1-sigma_2` preserves both properties. For example an added squared
difference also vanishes when the inputs coincide. A weighted mean is another
possible choice when weights are supplied, but they do not come from the
word "neutral".

This establishes a viable relational reference. It does not make a state
with `b=0`. In the r17 one-field family, relative offsets `+delta,-delta`
both have positive radius `sech(2 delta)` for finite delta. Their equal
radius alone does not make their Bloch vectors opposite or make a mixture
maximally mixed.

### Non-collinear boundary

A single additive rapidity line cannot encode general non-collinear boosts.
For active boosts of speed `3/5` in x and y, acting on the rest vector,

\[
B_xB_y(1,0,0,0)=(25/16,15/16,3/4,0),
\]
\[
B_yB_x(1,0,0,0)=(25/16,3/4,15/16,0).
\]

They differ. A geometric extension for two future unit timelike velocities
is instead the hyperbolic midpoint

\[
u_N=\frac{u_1+u_2}{\sqrt{-(u_1+u_2)^2}},\qquad
g=\operatorname{diag}(-1,1,1,1).
\]

It is Lorentz-equivariant and exchange-symmetric, and it reduces to the
rapidity midpoint in the collinear equal-weight case. It still presupposes
an identification of the project's scale line with Lorentz observers.

## B. A neutral density matrix from two opposite state-disk points

On the **real two-dimensional disk** used by Frames.lean, write

\[
\rho(b_z,b_x)=\tfrac12(I+b_z\sigma_z+b_x\sigma_x),
\quad b_z^2+b_x^2\le1.
\]

For the corrected native tachyon/duality map
`D(rho)=sigma_y rho sigma_y=rho(-b_z,-b_x)` one has exactly

\[
\frac12[\rho+D(\rho)]=\frac I2.
\]

Hence a maximally mixed state can indeed be constructed from two finite,
nonzero, opposite Bloch vectors; no infinite boost is needed to perform this
mixing operation. For weights `w,1-w`, the mixture has vector `(2w-1)b`:
exact neutrality requires `w=1/2`, unless b was already zero. The equal weight
is therefore a physical/preparation assumption to be justified, not an
automatic cancellation law.

This is an incoherent density-matrix mixture (or a reduced state after an
appropriate coupling), not a passive observer transformation. A unitary
change of basis preserves eigenvalues and cannot turn a non-maximally mixed
single state into I/2. The r17 claim that the single-state observer family
reaches b=0 only in a limiting boost is compatible with this finite mixing
construction: they are different operations. Nor may I/2 simply be declared
to be a spacetime rest frame or a physical photon.

### J_B is not the required opposite-state map in general

Frames.lean gives

\[
J_B(\rho)=\sigma_x\rho\sigma_x=\rho(-b_z,b_x),
\qquad \tfrac12[\rho+J_B(\rho)]=\rho(0,b_x).
\]

Thus equal J_B mixing kills the z asymmetry only. At
`b=(3/10,2/5)` the result retains `b_x=2/5` and is not I/2.
The compensator probabilities are `(1+b_x)/2,(1-b_x)/2`; they remain
`7/10,3/10` in this counterexample. J_B fixes these ports. This is precisely
why r28 corrected the earlier identification of the port-swapping tachyon
map. A special state with `b_x=0` does become I/2 under equal J_B mixing;
that special axis is not a general theorem.

Likewise M at `+beta` and its purely sign-reversed `T|R` coordinate do not
by themselves imply opposite density matrices. The even scalar `x=beta^2`
is unchanged under that sign reversal. The native-T eigenchannel exchange
uses `x -> 1/x` and the explicitly corrected duality map, not just the real
projection's sign. One must declare which map and which port axis is used.

The disk qualification matters: conjugation by sigma_y reverses x and z
components of a full three-dimensional Bloch vector but leaves y fixed.
The argument applies to the source's real disk, not an unqualified universal
Bloch-vector inversion by a unitary.

## C. A zero-flux Lorentz observer from two positive streams

Use signature `(-,+,+,+)`, units c=1, and future-directed energies. Two finite
particle/packet momenta have total `P=p_1+p_2`. Whenever `P^2<0`,

\[
u_{\rm COM}=P/\sqrt{-P^2}
\]

is a covariant center-of-momentum observer. For opposed null packets,

\[
p_+=(E_+,E_+,0,0),\quad p_-=(E_-,-E_-,0,0),\quad
-P^2=4E_+E_->0,
\]
\[
v_{\rm COM}=\frac{E_+-E_-}{E_++E_-},\qquad
\eta_{\rm COM}=\tfrac12\log(E_+/E_-).
\]

For equal packets it is the original observer; for unequal positive packets
it is a finite boosted observer. For non-collinear null directions,
`-P^2=2E_1E_2(1-n_1 dot n_2)>0` unless the directions coincide. For a single
null beam, or parallel null packets, P remains null and there is no such
rest observer. Negative weights or spacelike native "tachyon" vectors are
outside these positive-causal assumptions.

### Local Landau frame is a different weighted construction

For two opposed local null-dust streams set

\[
T^{\mu\nu}=\epsilon_+k_+^\mu k_+^\nu
+\epsilon_-k_-^\mu k_-^\nu,
\qquad k_\pm=(1,\pm1,0,0),\quad\epsilon_\pm>0.
\]

A passive boost of rapidity eta sends the two densities to
`epsilon_+'=epsilon_+ exp(-2 eta)` and
`epsilon_-'=epsilon_- exp(2 eta)`. The energy-flux-free observer is therefore

\[
\eta_L=\tfrac14\log(\epsilon_+/\epsilon_-),\qquad
v_L=\frac{\sqrt{\epsilon_+}-\sqrt{\epsilon_-}}
{\sqrt{\epsilon_+}+\sqrt{\epsilon_-}}.
\]

This differs from the finite-packet COM formula: local energy density has
two boost factors, whereas each packet energy has one. At numerical ratio
4:1 the packet formula gives v=3/5, while the local Landau formula gives
v=1/3. They must not be mixed merely because both are called neutrality.
If one local density vanishes, the Landau rapidity diverges and no timelike
Landau observer remains.

In the Landau frame the tensor is

\[
T^{\mu\nu}=\operatorname{diag}(\rho,\rho,0,0),\qquad
\rho=2\sqrt{\epsilon_+\epsilon_-}>0.
\]

The flux vanishes, but energy and anisotropic pressure do not. The trace
is zero. In contrast, a cosmological vacuum stress has

\[
T^{\mu\nu}_\Lambda=-\rho_\Lambda g^{\mu\nu}
=\operatorname{diag}(\rho_\Lambda,-\rho_\Lambda,-\rho_\Lambda,-\rho_\Lambda),
\quad g_{\mu\nu}T^{\mu\nu}_\Lambda=-4\rho_\Lambda.
\]

Two positive null streams therefore do not become cosmological vacuum by
going to their neutral observer. An actual metric-proportional term retains
its scalar coefficient under every finite Lorentz observer change. The
trace part of a general tensor is invariant too, although identifying it
with a constant Lambda requires a physical field equation, conservation
and an equation of state, not just a trace calculation.

## Relation to H20, H23 and H25

H20 distinguishes an inner complex structure `L_e7` from the outer complex
scalar and supplies projector bridges. That is a useful precedent for
requiring an explicit bridge; it is not a spacetime observer average.
H23 identifies the exchange/fixed-slot pattern of the frame triole with an
S3/triality pattern. That algebraic pattern does not select mixture weights,
a Lorentz stress tensor, or a unique neutral observer. H25 distinguishes
bilinear and Hermitian comparisons and their sign/conjugation behavior.
Thus one cannot silently average a sign-changing bilinear squared-mass
readout as if it were positive energy density or a Hermitian state norm.

## Outcome and remaining physical inputs

Three constructions survive, with different outputs:

1. Pairwise rapidity midpoint: a relational scale reference.
2. Equal mixture of opposite disk states: an information-neutral density
   matrix I/2, conditional on the correct map and equal weights.
3. Positive-stream COM/Landau construction: a flux-free timelike observer,
   conditional on the causal and positivity hypotheses.

The user's suggestion is mathematically viable in each of these precise
senses: neutrality need not be assumed to coincide with one initial frame.
But none proves that the three outputs coincide, that the result is photon
P rather than reference R, or that a nonzero physical Lambda disappears.
In QAM terms, declaring a state and an operator graph for a mixing operation
does not yet supply `QAdmTransport` or preservation of a native `QClEq`
class. In particular, the mixture changes the eigenvalues in general; its
information loss should remain explicit rather than being labelled a passive
frame conversion.

To connect this to OP5 requires: the native objects being combined; the
physical operation (coordinate choice, mixture, coherent coupling or stress
addition); invariant and justified weights; the exact map to the spectral
variable/cutoff and regulated action; and a metric-dependent stress tensor
whose vacuum coefficient can be evaluated. The existing OP5 subtraction and
target issues are not removed by naming an object neutral.

## Finite verification and source fingerprints

Command: `python -B analysis/OP5_Neutral_Frame_Candidates_Check.py`.
All controls passed: exact rational density-matrix mixture identities,
non-collinear boost noncommutation and metric preservation, packet COM,
local Landau flux cancellation, and the trace-zero versus nonzero-energy
counterexample. The general formulas are derived above; these controls are
not a proof of a native physical identification.

SHA256 at the pinned revision:

| Source | SHA256 |
|---|---|
| `sources/research/parts/v490-post-release-layers.tex` | `232BDD631BAC34259BE48B6D326FBF6EAF38F084EE4BEC1A621658B3C964424E` |
| `formal/QSFormal/Frames.lean` | `D05C812136899BC82FE1ACFE0D5FA39967477A9E5EB0BECD66F314A42B7BC03D` |
| `notes/research/v4_10_0_r34_r47/llm/Vorab_Notiz_H20_Frame_Zuordnung.md` | `4AD70C9196F67A7FF03195A490A9D79FDD7ABA566C02678B3C49E5977E97F041` |
| `notes/research/v4_10_0_r34_r47/llm/Vorab_Notiz_H23_Frame_Triole_Triality.md` | `114AC045D4FDDB3E2F07AFDEC38CE7F24D7EAA70615A408CF3156ACB64C6BCC9` |
| `notes/research/v4_10_0_r34_r47/llm/Vorab_Notiz_H25_Zweiseitige_Kontraktion_Frames.md` | `37331328FD5CBEF721661501B4FDEE3B17D284DDD981B0D85CAE191F603B8A52` |

Review provenance: separate child-agent derivation within the same overall
session, with a fresh finite control script; not an independent external
review and not a rerun of the historical H20/H23/H25 computations.
