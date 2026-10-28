# Independent audit: antilinear comparison and forward dynamics

26 October 2026. Base checkpoint:
`3fa5ba9440d0985fbb2b3786eaebe56a887cfe6a`.
Exact finite positive-Hilbert-space analysis, not a native identification
of comparison data, a full field solution or a change to the manuscript.

## 1. Source and principal result

`sources/research/parts/v470/07_qam_infrastructure.tex`,
`def:two-sided-structural-tensor-interface` and
`def:two-sided-admissible-contractions`, introduces front/back interface
roles and explicitly declared comparison tensors. It is described as a
conservative notation layer, not a new tensor calculus or closure criterion.

`sources/research/parts/v490-post-release-layers.tex`,
`subsec:v490-r40-model` and `subsec:v490-r40-results`, supplies a concrete
model with the linear front map x->ix, antilinear complex conjugation and
their composite. It distinguishes the complex-bilinear q from Hermitian h.
The source itself finds that the notation is covariant, not generally
invariant, under the antilinear front maps.

**Result:** An antiunitary partner map can transport positive projectors
and closure norms, but its induced HS(5) exchange is antilinear, not a
complex-linear spectral involution. Its fixed subspaces are real subspaces.
Furthermore, a forward-time antilinear state comparison transforms a
Schroedinger Hamiltonian with a minus sign and a connection term. This is
different from antiunitary time reversal. Neither fact can be replaced
by a scalar comparison tensor without specifying its types and metric.

## 2. Antiunitary HS(5) exchange

Let V_f,V_b be n-dimensional complex Hilbert spaces with specified
positive metrics. Let K denote coordinate conjugation in an orthonormal
front basis and let W=UK:V_f->V_b be antiunitary, with U unitary.
Assume P_f is an orthogonal complex-linear projector and set

    P_b=W P_f W^(-1)=U P_f* U†,
    P_5=diag(P_f,P_b),
    X(v,w)=(W^(-1)w,Wv).

Here * denotes coordinatewise complex conjugation, not the adjoint.
X obeys X²=I and is an isometry of the underlying real inner product
Re<.,.>. It is nevertheless antilinear:

    X(cz)=conj(c)Xz,    X(iz)=-iXz.

Thus E_+=(I+X)/2 and E_-=(I-X)/2 are idempotent real-linear maps,
with E_+E_-=0 and E_++E_-=I. They are orthogonal projections on the
underlying real Hilbert space because an orthogonal real involution is
real-selfadjoint. They are not complex-linear projections:

    E_+(iz)=i E_-(z),    E_-(iz)=i E_+(z).

Their ranges are the graph subspaces

    L_+={(v,Wv)},    L_-={(v,-Wv)}.

Each has real dimension 2n. Multiplication by i exchanges L_+ and L_-;
neither is a nonzero complex subspace. Calling E_+/- complex spectral
projectors or assigning them complex rank n on V_f direct_sum V_b would
therefore be incorrect. There is no complex-linear spectral theorem for
X as an operator on this original complex carrier.

The complex-linear P_5 commutes with X as real-linear maps under the
stated partner relation. If rank_C P_f=k, the intersections
ran P_5 intersect L_+/- are graphs of vectors in ran P_f, each of real
dimension 2k. They are real, not complex, exchange sectors. The paired
selected carrier itself has complex dimension 2k and real dimension 4k.
For k=0 all intersections vanish; no normalized selected state exists.

One can instead use the conjugate complex space bar(V_f), on which the
same antiunitary W induces a complex-linear map bar(V_f)->V_b. A linear
exchange on bar(V_f) direct_sum V_b then has ordinary complex eigenports.
This changes the complex structure assigned to the front carrier. It is
a legitimate typed reformulation, not an unchanged conclusion on the
original V_f direct_sum V_b; the projector, scalars and dynamics must all
be transported accordingly.

## 3. Projector transport and closure norms remain meaningful

For any complex-linear M_f define its instantaneous partner by

    M_b=W M_f W^(-1)=U M_f* U†.

Then P_b is complex-linear, orthogonal and idempotent, and

    [M_b,P_b]=W[M_f,P_f]W^(-1).

Adjoints are also transported:

    (W M_f W^(-1))†=W M_f† W^(-1).

Consequently a minimal positive closure operator with real coefficients
rho,sigma transforms to W H_C,f W^(-1). Its eigenvalues, singular values
and positive operator norm are unchanged. A vanishing commutator remains
zero. These are instantaneous positive-Hilbert-space covariance statements.

Complex scalar contractions need not be invariant: for example
Tr(M_b P_b)=conj(Tr(M_f P_f)). It is unchanged if the original trace is
real, as it is for Hermitian M_f and orthogonal P_f. The statement does
not identify the partner M_b with the physical forward-time generator.

## 4. Forward-time antiunitary comparison: the Hamiltonian sign

Let f(t) obey i dot f(t)=H_f(t)f(t), in units hbar=1, with H_f Hermitian.
Let U(t) be differentiable and unitary, and compare the states at the
same time by

    b(t)=U(t)f(t)*.

Since dot f* = +i H_f* f*, direct differentiation gives

    i dot b = H_b,forward b,
    H_b,forward = -U H_f* U† + i dot U U†.

The second term is Hermitian, since dot U U† is antihermitian. The minus
sign comes from conjugating i; it is not optional. Transporting H merely
as U H_f* U† fails to reproduce the same-time compared trajectory, unless
special additional conditions happen to make the difference irrelevant.

For a general equation dot f=G_f f the corresponding exact formula is

    G_b=dot U U†+U G_f* U†.

Thus even if an instantaneous M or P has a simple antiunitary transform,
the complete dynamical comparison includes its time connection and the
complex structure. A passive description can also be expressed with
the opposite complex structure; then one must explicitly transform the
meaning of i rather than infer negative physical energy.

In particular the displayed minus sign is not a derivation of a negative
gravitating energy density, a tachyon mass or vacuum cancellation. It
belongs to the relationship between antilinear coordinates and the
chosen forward-time Schroedinger convention.

## 5. Time reversal is a different comparison

Now compare to the reversed trajectory

    b_rev(t)=U(t)f(-t)*.

The additional derivative sign from -t yields instead

    H_b,reverse(t)=+U(t)H_f(-t)*U(t)†+i dot U(t)U(t)†.

For constant U and time-independent H_f this is the familiar positive
antiunitary transform U H_f* U†. A time-reversal symmetry of a fixed
Hamiltonian requires that transformed Hamiltonian to equal the original
one, with any external time-odd data also appropriately transformed.
Antilinear coordinate conjugation alone does not assert this symmetry
and does not reverse the time parameter by itself.

The forward-time paired carrier and a time-reversed partner therefore
have different dynamical compatibility conditions. A comparison-selector
construction must state which relationship it intends.

## 6. Bilinear and Hermitian comparisons separate different content

In the r40 declared model, G is real symmetric and

    q(x)=x^T G x,    h(x)=x†Gx.

Direct substitution gives

    q(ix)=-q(x),    h(ix)=h(x),
    q(x*)=conj(q(x)),    h(x*)=h(x).

The last equality uses that h(x) is real for real symmetric G. Positive
definiteness of h would additionally require positive G; real symmetry
alone does not establish it. The opposite q sign under ix cannot be
imported into a positive closure norm defined using h. Conversely,
replacing q by h removes that particular sign distinction and therefore
changes the comparison content.

For a general U, neither form is automatically preserved: bilinear
preservation requires U^T G U=G, and Hermitian preservation requires
U†G U=G. The phase U=iI satisfies the latter and negates the former.
These formulae are exact algebra, not an independent proof that q is a
physical squared mass. The source presents that mass interpretation as
a reading of the bilinear sign; a physical action and operator bridge
would still have to establish it.

## 7. A comparison tensor is not automatically a front-to-back map

The grammar's expression G_{alpha beta} X^alpha Y^beta specifies a
pairing of active channels. It has two covariant slots. If nondegenerate
and bilinear, it can be curried into a linear map from one vector space
to the dual of the other. This is not yet a map V_f->V_b. Converting a
dual into a carrier requires another specified identification or metric.

A Hermitian pairing is conjugate-linear in its first slot (with the
convention h(x,y)=x†Gy). Its Riesz identification has a different
linearity type from the bilinear identification. An antiunitary W may
be obtained only after specifying all such domains, metric identifications
and normalization; the symbol G alone does not provide one.

Moreover, in r40 the front maps act on the complex factor while the
back maps act on the real structural index. Commutation of these two
actions is not itself an isomorphism between a duplicated front Hilbert
space and a duplicated back Hilbert space. The structural tensor indices,
HS(5) duplicated carrier and physical matter/tachyon state spaces need
an explicit source-to-target dictionary before their maps are identified.

In particular r40 writes J_B=iK on its complex factor, which is
antilinear there. The doublet notation used elsewhere writes J_B=sigma_x
as a linear matrix on the doublet coordinates. These may encode related
real transformations in different carriers, but cannot be equated by an
unexplained complex-linear change of basis: linear conjugation preserves
whether a map is linear or antilinear. A realification/intertwining
dictionary is needed rather than the shared letter J_B.

## 8. Consequence for the paired-sector route

A unitary-linear HS(5) comparison, an antiunitary same-time partner,
an antiunitary reversed-time partner and a bilinear structural pairing
are distinct contracts. Each can be studied, but selecting one changes
the projector and dynamical obligations. The r40 distinction between
bilinear and Hermitian comparison makes it impossible to silently infer
the required W from the existing notation.

The paired closure route remains meaningful after declaring the proper
contract. What is ruled out is using antiunitary W together with the
unchanged complex spectral-projector and same-time Hamiltonian formulae
from the linear-unitary case.

## 9. Verification and fingerprints

Analytically checked: real versus complex linearity of X and E_+/-, graph
dimensions including selected rank, conjugation of idempotents and
adjoints, both trajectory derivatives, scalar pairing transformations
and the domain/codomain of a two-covariant-slot comparison. No numerical
experiment or native coefficient choice was used.

SHA-256 input fingerprints:

| Repository-relative path | SHA-256 |
|---|---|
| `sources/research/parts/v470/07_qam_infrastructure.tex` | `380455cda15546021d2caea8e8676e64af7d1327f9a78a0af0e118b7a37371f2` |
| `sources/research/parts/v490-post-release-layers.tex` | `232bdd631bac34259be48b6d326fbf6eaf38f084ee4bec1a621658b3c964424e` |

Only this audit note was written. No physical interpretation of P_C7,
comparison tensor G or the absolute energy scale has been promoted.
