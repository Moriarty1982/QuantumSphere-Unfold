# Independent audit: physical contributions versus frame views, and two null streams

26 October 2026. Base checkpoint:
`3fa5ba9440d0985fbb2b3786eaebe56a887cfe6a`.
Exact local analysis with metric signature (-+++), c=1. No numerical
experiment, native M16/P_C7 reconstruction or cosmological prediction.

## 1. What counts as a second physical contribution?

The following source distinctions are essential before adding stresses:

| Source construction | What is actually given | What is not yet established |
|---|---|---|
| Corrected field duality z->iz in v490 r28 | A deterministic map of the given field; in the declared Maxwell model it preserves the entire stress tensor | A second independently present stress source, or an opposite momentum direction |
| r28.1 product rho tensor sigma_y rho sigma_y | Two labelled Hilbert factors, an explicitly factorized input and a partial-swap interaction | A physical ancilla/preparation derived solely from the frame map; full spacetime stress and energy cost of that preparation |
| `prop:triadic-two-probe` in v470/10 | Distinct coupled variables Psi_1,Psi_2,Psi_perp and operator-valued channels | Their computed joint stress tensor, the metric/adjoint realization, or an identification with positive counterpropagating null streams |
| Opposite-frame probe traces in v470/13 | A hypothesis-level joint tensor readout with mixed bilinears and mismatch data | A proved decomposition into independent positive additive energy components |
| HS(5) front/back in v470/32 | Duplication of carrier roles, readout versus structure/action, with declared comparison selectors required | Two physical energy sources or a matter/tachyon correspondence |

A frame description of one source is not an additional source. A second
prepared physical copy is additional, but its propagation and stress must
be specified separately. In particular, D rho alone is only reduced state
data: it does not determine the device's field F, energy or flux direction.
If its physical realization is explicitly z_dev=i z_sys, its Maxwell
stress is the same as the system's; a different realization requires
additional data. One must not infer equal or opposite stress from D rho
alone after the Gram information loss already demonstrated.

The product in r28 is thus stronger than merely assigning a second frame
label. Its factors are initially uncorrelated in that product state,
although the chosen second state's parameters depend on the first. The
expression does not construct a second physical system from a relabelling.

The additive stress model below is therefore a separate, explicit control
model. For coherent Maxwell amplitudes, stress of the summed field can
contain interference terms. For coupled fields, the interaction also
contributes to metric variation. Additivity requires those terms to be
absent, averaged away by a justified procedure, or included independently.

## 2. Assumptions for two genuinely present null streams

At a spacetime point let k,l be nonzero future-directed null vectors and
let a,b be strictly positive real coefficients. Suppose

    k.k=l.l=0,    k.l=-chi<0,
    T^{mu nu}=a k^mu k^nu+b l^mu l^nu.

The streams are distinct noncollinear null directions. Their weights and
directions are physical inputs in a common tangent space, not two
coordinate views of the same stream. The formula defines the complete
stress considered here; no interaction, interference or vacuum term is
silently added. This is an instantaneous local eigenvector problem,
not a proof of conservation, evolution or realizability in the native
coupled field system.

## 3. Unique future timelike zero-flux observer

Define

    epsilon=sqrt(a b) chi>0,
    N=sqrt(2 sqrt(a b) chi),
    U=(sqrt(a) k+sqrt(b) l)/N,
    V=(sqrt(a) k-sqrt(b) l)/N.

Direct contraction gives U.U=-1, V.V=+1 and U.V=0. U is future-directed
because its numerator is a positive sum of nonparallel future null
vectors. The mixed stress operator acts by

    T^mu_nu U^nu=-epsilon U^mu,
    T^mu_nu V^nu=+epsilon V^mu.

Proof: k.(sqrt(a)k+sqrt(b)l)=-sqrt(b)chi and the analogous l contraction
is -sqrt(a)chi. Substitution gives the first relation; changing the
relative sign gives the second.

The orthogonal complement of span(k,l) is a two-dimensional spacelike
space. Every vector in it is annihilated by T^mu_nu. Hence its complete
spectrum is

    {-epsilon,+epsilon,0,0}.

The -epsilon eigenspace is the unique timelike eigendirection. Its
normalization and future orientation determine U uniquely. The measured
energy is T^{mu nu}U_mu U_nu=epsilon, and the U-spatial energy flux
vanishes because T U is parallel to U.

In its orthonormal rest basis the contravariant stress is

    diag(epsilon,epsilon,0,0),

with the first spatial axis along V. Thus the two streams supply a
unique local rest observer under the given hypotheses, but retain
positive energy and anisotropic pressure. This is not vacuum form
T^{mu nu}=-rho_vac g^{mu nu}; its trace is zero, not that of nonzero
cosmological vacuum stress.

## 4. Null-ray normalization and exchange consistency

Rescale the representatives of the null rays by positive r,s:

    k'=r k,    l'=s l,    a'=a/r²,    b'=b/s².

T is unchanged, chi'=r s chi and epsilon'=epsilon. Moreover
sqrt(a')k'=sqrt(a)k and sqrt(b')l'=sqrt(b)l, so U is unchanged. The
formula is therefore independent of arbitrary positive null-ray
normalization when the weights are transported consistently.

Swapping the two physically labelled streams leaves U and epsilon
unchanged and reverses V. Keeping a,b fixed while rescaling k,l would
change the physical stress and is not the same operation.

## 5. Degenerate cases are different physical situations

- If k and l are collinear future null vectors, chi=0. Their sum stress
  is again a single nonzero null-stream stress for positive total weight.
  There is no timelike rest eigenvector. The displayed U formula has
  zero denominator and does not extend to a normalized timelike limit
  within that collinear configuration.
- If a=0 or b=0 and the remaining weight is positive, only a single
  nonzero null stream remains. Again there is no timelike zero-flux
  observer, and the formula is inapplicable.
- If both weights are zero, T=0. Every observer has zero flux, so there
  is no unique selected observer.
- Negative weights or spacelike flow directions are outside the proof.
  The result cannot be applied unchanged to hypothetical superluminal
  tachyon energy components or to an indefinite native comparison form.

These cases explain why merely adding a second label does not guarantee
the existence of a rest frame. Noncollinearity and two positive physical
weights are load-bearing assumptions.

## 6. Opposed local streams: quarter-log rapidity

Choose normalized opposed rays

    k=(1,0,0,1),    l=(1,0,0,-1),    chi=2.

Then a,b are their local energy densities in the chosen observer frame.
The unique rest observer has

    v=U^z/U^0=(sqrt(a)-sqrt(b))/(sqrt(a)+sqrt(b)),
    eta=atanh(v)=(1/4)log(a/b),
    epsilon=2sqrt(a b).

For a passive boost along +z with this eta, the local stream densities
transform as a'=a exp(-2eta), b'=b exp(+2eta), and become equal at
sqrt(a b). This independently verifies the quarter-log factor.

## 7. Packet centre of momentum: half-log instead

Two opposed isolated packets with total energies E_+,E_->0 have total
four-momentum

    P=(E_++E_-,0,0,E_+-E_-).

Its rest velocity and rapidity are

    v_COM=(E_+-E_-)/(E_++E_-),
    eta_COM=(1/2)log(E_+/E_-).

Packet energies have one Doppler factor under a boost, whereas local
null-dust energy densities have two. Consequently the half-log packet
formula and quarter-log local-stress formula answer different questions.
For ratio 4:1 they give respectively v_COM=3/5 and v_local=1/3. A
packet model needs its spatial support and simultaneity/integration
prescription before its total momentum is related to a local stress.

These two distinctions were already noted in prior neutral-frame work;
the present calculation checks the general noncollinear local formula
and makes the physical-input distinction explicit, rather than claiming
the opposed-stream observation as new.

## 8. Source mapping and remaining native obligations

The sources authorize considering paired/coupled components, but they
do not compute the a,b,k,l of this model from M16,P_C7 or a triad state.
An actual native application must supply a joint real action or another
justified stress law, specify whether contributions are independent or
coherent, retain interaction terms and establish the positivity and
null character of the relevant components. The comparison between two
frames of a single tensor does not meet this burden by itself.

The model shows how two independent physical flows can select a unique
reference without an arbitrary equal-weight convention. The weights
are measured physical data, and the observer is selected by the total
stress eigenstructure. It does not select a closure projector, remove
positive energy or determine an absolute cosmological constant.

## 9. Verification and source fingerprints

Analytically checked: normalization and orientation of U, all four
eigenvalues, uniqueness, positive ray-rescaling invariance, exchange of
labels, all zero/collinear degeneracies, rest pressure, local Doppler
weights and the separate total-packet momentum formula. No numerical
experiment or native parameter fitting was performed.

| Repository-relative source | SHA-256 |
|---|---|
| `sources/research/parts/v470/10_sphaera_and_physics.tex` | `7d72c58b1159f5462c6be395961fcd8882028fc3e8c8495e7f2a3b10055c1a32` |
| `sources/research/parts/v470/13_hc_hypotheses.tex` | `fa97bc7dc07be0263a95d2cd4083b3ee0e4572073fb386464b24ceaa75ee2b47` |
| `sources/research/parts/v490-post-release-layers.tex` | `232bdd631bac34259be48b6d326fbf6eaf38f084ee4bec1a621658b3c964424e` |
| `sources/research/parts/v470/32_atlas_and_op_promotion.tex` | `6e9fb2e657886c4edcf3298f7b697686cbc573557465281e2ab8842359aa2d02` |

Only this audit note was written. Classical positive null streams are
not identified with the native tachyon frame, FTL matter or vacuum energy.
