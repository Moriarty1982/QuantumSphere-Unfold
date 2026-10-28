# Independent audit: symmetry selection on the native doublet

Date: 26 October 2026. Base checkpoint:
`3fa5ba9440d0985fbb2b3786eaebe56a887cfe6a`.
Scope: exact finite doublet algebra; no native 16-mode realization,
Lorentz identification, numerical experiment, manuscript change or OP5 closure.

## Question and primary verdict

Can the structural involution and corrected matter/tachyon exchange select
a unique nontrivial orthogonal closure projector without choosing one frame?

**Verdict: refuted in the stated doublet reading if the selected projector
must individually respect both conjugations.** Only zero and identity do.
If the two sector projectors may instead be exchanged, their unordered pair
is admissible but no single member is chosen by exchange symmetry alone.
This is not a no-go for a larger native carrier or a different symmetry action.

## 1. Sources and exact assumptions

The native r05.1 statement in
`sources/research/parts/v490-post-release-layers.tex`,
`subsec:v490-r05-millennium`, supplies

    J_B = sigma_x,    C_+ = (I+sigma_x)/2,    C_- = I-C_+,
    M = lambda_+ C_+ + lambda_- C_-.

The source treats M as port weighting and explicitly does not identify the
doublet matrix with full M_16 or with Lorentz transport. Its real doublet
coefficients lambda_+,lambda_- are real. Orthogonality below uses the
ordinary positive doublet inner product.

The r28 correction, `subsec:v490-r28-correction`, distinguishes J_B from
the corrected opposite map D on states:

    D(rho) = sigma_y rho sigma_y.

J_B conjugation fixes the x port coordinate and reverses z on the real
state disk. D reverses x and z and exchanges the ports. On the full
complex Bloch ball D leaves the y coordinate unchanged. The full reversal
claim therefore has the real-disk restriction.

T4 in `sources/research/parts/v470/12_structural_core.tex`,
`def:tensor-structural-kernel`, requires M to commute with the structural
J and C. It does not identify the physical P_C7 with either C_+ or C_-.
`sources/research/parts/native-operator-link.tex`,
`v480:native-frame-covariance`, already distinguishes joint unitary
transport from an unspecified physical relative frame relation.

## 2. Classification of projectors compatible with port weighting

Every rank-one orthogonal projector on C^2 is

    P(n) = (I+n_x sigma_x+n_y sigma_y+n_z sigma_z)/2,
    n in R^3,    |n|=1.

It is a real matrix exactly when n_y=0. The remaining orthogonal
projectors on C^2 are 0 and I.

Write M=aI+b sigma_x with b=(lambda_+-lambda_-)/2. The Pauli identity
[u.sigma,v.sigma]=2i(u cross v).sigma gives

    [M,P(n)]=i b (e_x cross n).sigma.

If b!=0, [M,P]=0 forces n=+/-e_x, so the complete list is

    0, I, C_+, C_-.

If b=0, M is scalar and every orthogonal projector commutes with M. The
dynamics/port weighting then supplies no axis or nontrivial uniqueness.
If [P,J_B]=0 is independently required, its nondegenerate spectrum still
restricts the list to 0,I,C_+,C_- even when M is scalar.

This classification is about compatibility, not physical preference:
choosing the '+' eigenspace needs a physically justified label or criterion.

## 3. Individual exchange invariance versus exchange of a pair

Conjugation by sigma_y sends

    P(n_x,n_y,n_z) -> P(-n_x,n_y,-n_z),
    C_+ -> C_-,    C_- -> C_+.

An individually D-invariant rank-one projector on the complex doublet
must therefore be P_y^+=(I+sigma_y)/2 or P_y^-=(I-sigma_y)/2.
Neither commutes with a nonscalar M=aI+b sigma_x or with J_B. On the
real doublet, neither is an allowed real matrix, and no real rank-one
projector is individually D-invariant at all. The same real-plane
conjugation may be implemented with the real orthogonal matrix i sigma_y;
it has no real invariant line, so this does not change the result.

Consequently, requiring an orthogonal P to commute with J_B and to obey
sigma_y P sigma_y=P leaves only 0 and I. In particular a neutral rank-one
projector selected by these two symmetries does not exist in the doublet.

In contrast, the unordered set {C_+,C_-} is preserved by D. It is a
perfectly consistent decomposition into two exchanged sectors. Symmetry
therefore justifies a paired decomposition but not choosing one member
as *the* physical P_C7. Choosing their sum gives I, the whole doublet;
that is a larger allowed sector, not a preferred ray within it.

## 4. Covariant selection is not individual invariance

A selection rule can be equivariant while selecting one projector from
labelled data. For a supplied nondegenerate M and a specified eigenvalue
lambda_+, its spectral projector transforms as

    P_{lambda_+}(U M U†)=U P_{lambda_+}(M) U†.

Taking U=sigma_y swaps the coordinate ports. This is covariant transport
of the whole data set, not the assertion that P remains fixed while its
reference data are exchanged. It does not prove a native physical reason
to prefer lambda_+ over lambda_-, nor does it identify this projector with
P_C7. A nondegenerate eigenvalue label is extra information in this rule.

If exchange is instead demanded to be an unbroken symmetry of the fixed
port-weighting operator, sigma_y M sigma_y=M, then b=0. Thus unequal
port weights and this exact fixed-operator exchange symmetry cannot both
hold. A transformation that changes the physical data, or reverses the
time parameter, is a different assertion and is not excluded by this test.

## 5. Which dynamics can share a nontrivial doublet projector?

For an explicitly supplied Hermitian generator H=h_0 I+h.sigma,
[H,P(n)]=0 iff h cross n=0 (or h=0). A family of nonscalar Hermitian
generators therefore shares a rank-one orthogonal projector only when
all its Bloch vectors are parallel. Two nonparallel generator axes have
only 0 and I as common orthogonal projectors.

If a nondegenerate port-weighting matrix with x axis must be preserved
as well as the continuous rotation generator H proportional to sigma_y,
there is no common rank-one orthogonal projector. The pair of axes
generates the full 2x2 matrix algebra; no preferred smaller sector remains.
This does not imply physical inconsistency of a two-mode system: its full
doublet remains a valid sector. It prevents treating one fixed ray as a
closed subsystem for all those operations.

No step here assumes M itself is a Hamiltonian. Its algebraic commutant
can be tested alongside actual generators once those have been identified.
The source currently does not supply their full common native matrix data.

## 6. A neutral density is available, but it is not a closure projector

For rho=(I+b.sigma)/2, |b|<=1, simultaneous invariance under J_B and D
forces b=0. Thus rho_*=I/2 is the unique normalized density matrix fixed
by both conjugations. Its eigenvalues are 1/2,1/2, so

    rho_*^2=I/4 != rho_*.

It is not an idempotent rank-one closure projector. Likewise,
(C_++C_-)/2=I/2 cannot replace P_C7 in an equation requiring P_C7^2=P_C7.

On the real disk, equal mixing of rho with its D image produces I/2.
On the full Bloch ball the same operation leaves b_y sigma_y/2; it is
not generally completely neutral. The source's opposite-state averaging
must keep that domain restriction explicit.

Symmetry fixes rho_* as a possible neutral state, not as an attractor.
For example unitary evolution preserves the eigenvalues and purity of a
density matrix, so it cannot drive every initial pure state to I/2.
No relaxation rate, bath, absolute energy or cosmological stress follows
from this fixed-point calculation.

## 7. Meaning for the native sector question

The available symmetry supports either an exchanged pair of ports or
the complete doublet. It does not select a nontrivial individually
exchange-invariant real closure ray. A larger native physical sector can
contain both ports and their mutual dynamics; selecting that larger
sector requires its actual embedding and the other native operators.

If the intended P_C7 is smaller than the whole doublet, additional
physical data must break or qualify the exchange, supply a labelled
spectral branch, or define a genuinely different covariant relational
operator. If P_C7 contains the entire doublet, this obstruction is absent,
but the symmetry does not determine its rank or complement in M_16.

The corrected opposite map D is not the same as J_B. Using J_B as if it
exchanged its own eigenspaces would silently assume a false symmetry
action and could indeed carry a mistaken sector selection forward.
The source's r28 correction explicitly prevents that conflation.

## 8. Verification and source fingerprints

Analytically checked: complete rank classification on C^2, real-matrix
restriction, Pauli commutator, both conjugation actions, the degenerate
M case, exchanged set versus individually fixed projector, density-matrix
idempotence and unitary non-attraction. No finite sample is used as proof.

SHA-256 of inputs read for this audit:

| Path relative to repository | SHA-256 |
|---|---|
| `sources/research/parts/v490-post-release-layers.tex` | `232bdd631bac34259be48b6d326fbf6eaf38f084ee4bec1a621658b3c964424e` |
| `sources/research/parts/v470/12_structural_core.tex` | `4d663bedef288c803b1538b417e8a846006d77fe2c540adc066a86851e952b15` |
| `sources/research/parts/native-operator-link.tex` | `3843a019e6ba8b1c6e642ba2c53ad11f33134e1745d8b68e15c69ac2b5617b0f` |

Only this audit note was written. No native coefficients were re-solved,
no public status was changed, and no identification P_C7=C_+ was assumed.
