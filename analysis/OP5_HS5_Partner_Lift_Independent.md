# Independent audit: HS(5) paired sector and exchange lift

26 October 2026. Base checkpoint:
`3fa5ba9440d0985fbb2b3786eaebe56a887cfe6a`.
Exact finite-dimensional algebra; no native matrix recovery, new physical
identification, numerical experiment or change to the manuscript.

## 1. Source and verdict

The source `sources/research/parts/v470/32_atlas_and_op_promotion.tex`,
sections “HS(4) meta-septum leakage target” and “HS(5) two-sided duplication”,
defines the duplicated carrier, its block projector and its debt register:

    V_5=V_front direct_sum V_back,
    P_5=diag(P_front,P_back),
    Debt(T_5)=(I-P_5)T_5 P_5+P_5 T_5(I-P_5).

The source says front carries readout/frame/language information, while
back carries structure/action/field information. It requires declared
comparison tensors or selectors for front/back comparisons.

**Verdict:** The debt register has a complete exact block-intertwining
test. A paired sector is compatible with an exchange symmetry when a
unitary partner identification is supplied. It then contains both exchange
eigenports, rather than selecting one. The cited source does not supply
that unitary map, the projector rank or an identification of front/back
with matter/tachyon. Those remain additional physical inputs.

## 2. Domain and hypotheses

Use finite positive inner-product spaces V_front and V_back over C
(the same block arguments hold over R). The projectors P_f,P_b are
orthogonal in these specified metrics. The inherited source explicitly
gives idempotence; its promotion to orthogonality in a common positive
metric is an assumption of this calculation, not a derived native result.

Set Q_f=I-P_f, Q_b=I-P_b and

    T_5=[[A,B],[C,D]],

where A and D act on their own sides, B maps back to front and C maps
front to back. The B,C symbols are coupling blocks, not the structural
HC projector also called C elsewhere. No self-adjointness of T_5 is
assumed for the general intertwining calculation.

## 3. Exact zero-debt criterion

For any projector P with Q=I-P, multiplying QTP+PTQ on the left by Q
and right by P isolates QTP; multiplying on the left by P and right
by Q isolates PTQ. Thus

    Debt(T)=0 iff QTP=0 and PTQ=0 iff [T,P]=0.

The last equivalence follows by writing TP-PT=QTP-PTQ.
No cancellation between the selected-to-complementary block and its
opposite direction can make the debt vanish, since they have different
source and target sectors. Orthogonality is unnecessary for these
algebraic equivalences, although needed for the later positive-space
interpretations.

For P_5 the full commutator is

    [T_5,P_5]=[[A P_f-P_f A, B P_b-P_f B],
               [C P_f-P_b C, D P_b-P_b D]].

Consequently the exact necessary and sufficient four conditions are

    [A,P_f]=0,    [D,P_b]=0,
    B P_b=P_f B,    C P_f=P_b C.

The diagonal conditions impose sidewise closure. The two cross-side
intertwining conditions are each equivalent to two separate leakage tests:

    Q_f B P_b=0,    P_f B Q_b=0,
    Q_b C P_f=0,    P_b C Q_f=0.

The source's “cross-side debt” formula, taken literally, tests diagonal
sidewise leakage as well as cross-side leakage. If sidewise closure is
already separately established, the remaining obligations reduce exactly
to the two cross-side intertwining conditions above.

For self-adjoint T_5 one has A=A†, D=D† and C=B†; the C intertwining
condition then follows by taking the adjoint of the B condition. Without
self-adjointness, neither cross condition may be omitted. A one-way
invariance test Q_5 T_5 P_5=0 alone is weaker than the full debt-free test.

## 4. Unitary comparison map and the exchange operator

Now supply an additional unitary W:V_front -> V_back and assume

    P_b=W P_f W†.

The existence of W requires equal full dimensions, and this compatibility
requires equal selected ranks. The front/back duplication gives matching
carrier sizes, but the actual unitary comparison and projector compatibility
are additional data. Define

    X=[[0,W†],[W,0]].

Then X†=X, X²=I and therefore E_+=(I+X)/2 and E_-=(I-X)/2 are
orthogonal exchange eigenprojectors. Direct multiplication yields

    X P_5=[[0,W†P_b],[W P_f,0]],
    P_5 X=[[0,P_f W†],[P_b W,0]].

Thus [X,P_5]=0 is exactly the condition P_b=W P_f W†. This exchange
is itself debt-free for the compatible pair. It does not make a general
T_5 debt-free: A,B,C,D must still pass section 3.

## 5. Which exchange eigenports are contained in the paired sector?

Let dim V_front=dim V_back=n and rank P_f=rank P_b=k. The exchange
eigenspaces consist of graph vectors

    ran E_+={(v,Wv): v in V_front},
    ran E_-={(v,-Wv): v in V_front}.

Both have dimension n. Their intersections with the paired selected
sector are

    ran P_5 intersect ran E_+={(v,Wv):v in ran P_f},
    ran P_5 intersect ran E_-={(v,-Wv):v in ran P_f}.

Both intersections have dimension k. Since P_5 and E_+/- commute,

    P_5^+=P_5 E_+,    P_5^-=P_5 E_-

are orthogonal projectors of rank k, with P_5^+ P_5^-=0 and
P_5^++P_5^-=P_5. The paired sector has rank 2k and contains both
exchange eigenports with equal multiplicity. Its complement contains
n-k dimensions of each exchange parity.

This differs from averaging two rays to obtain I/2. P_5 is an idempotent
projector on a larger duplicated space, whereas P_5/(2k), for k>0, is a
normalized density matrix. For integer k>=1 this density is not a projector.
It is exchange invariant but not selected uniquely by exchange alone:
P_5^+/k and P_5^-/k are also exchange-invariant density matrices.

For k=0 the selected paired sector is zero and these normalized densities
are undefined. For k=n the paired projector is the identity on the
duplicated carrier; both parity ports remain, each of rank n. If n=0,
all the spaces are trivial. No physical rank is inferred from these cases.

## 6. Incompatible projectors and intersection rank

If W is unitary but P_b=W P_f W† is not assumed, set

    K=ran P_f intersect W† ran P_b,    t=dim K.

Each exchange eigenport intersects the selected paired space in a
dimension-t graph: (v,+/-Wv) with v in K. If the two ranks are r_f,r_b,

    max(0,r_f+r_b-n) <= t <= min(r_f,r_b).

These bounds follow from the dimension formula for two subspaces of
the n-dimensional front space. Let R_K be the orthogonal projector onto K.
Then

    P_inv=diag(R_K,W R_K W†)

has rank 2t, is contained in P_5 and commutes with X. It is the largest
X-invariant subspace contained in ran P_5: if (v,w) lies in such a
subspace, both (v,w) and X(v,w) must lie in ran P_5; hence v in K and
w in WK. Conversely K direct_sum WK is X-invariant.

Thus exchange-compatible restriction can discard all selected content
when t=0. It does not automatically produce a nonzero common physical
sector, nor does it make the restricted sector invariant under T_5.
In the fully compatible case K=ran P_f and t=k, recovering section 5.

## 7. What the source does and does not identify

The cited HS(5) passage supplies a concrete two-sided carrier grammar,
not merely an informal instruction to average frame states. It gives a
valid place to seek a paired closure sector. It explicitly requires
declared comparison selectors/tensors, so the W obligation is consistent
with its own discipline.

However, in this passage front/back means readout versus structure/action
roles. It is not identified with matter/tachyon, with the two eigenports
of J_B=sigma_x, or with the corrected sigma_y opposite-state map. A
unitary W, its metric, its action on M16 and the clock, and ranks of the
two P_C7 realizations are not supplied here. Calling the two sides a
physical exchange pair therefore needs an additional source-to-target
dictionary and transformation law.

If a nonunitary comparison tensor is intended, X above is not automatically
self-adjoint/unitary; the spectral and orthogonality conclusions cannot
be imported unchanged. If the comparison is antiunitary, a different
real-linear or antiunitary formulation is required. Neither possibility
is excluded by the inherited grammar, but neither is proved by this audit.

## 8. Verification and source fingerprint

All conclusions were checked analytically by block multiplication,
isolation of the independent leakage directions, explicit exchange
graph eigenspaces, rank-nullity and the subspace dimension formula.
No numerical experiment, native coupling re-fit or physical vacuum-energy
claim is involved.

Source SHA-256:

`sources/research/parts/v470/32_atlas_and_op_promotion.tex`

`6e9fb2e657886c4edcf3298f7b697686cbc573557465281e2ab8842359aa2d02`

Only this note was written. The distinction between the algebraic paired
lift, the actual P_C7 selection and a physical matter/tachyon identification
is retained throughout.
