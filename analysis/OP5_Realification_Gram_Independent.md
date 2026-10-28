# Independent audit: existing realification and the information lost by Gram readout

26 October 2026. Base checkpoint:
`3fa5ba9440d0985fbb2b3786eaebe56a887cfe6a`.
Bounded analytic audit of r04.1–r04.3 and the r28 correction. No numerical
experiment, manuscript change or native M16/P_C7 identification.

## 1. Correction to the previous comparison audit

The source already gives the required bridge from the antilinear complex
field map to the real doublet. It is explicit in
`sources/research/parts/v490-post-release-layers.tex`,
`subsec:v490-r04-doublet`, Theoremlet r04.1. The preceding note
`OP5_Antilinear_Comparison_Independent.md` correctly demanded a typed
realification dictionary, but did not incorporate this already available
one. At this level the bridge is therefore **present**, not missing.

What remains missing is its full identification with the native M16,
P_C7, joint time generator and physical comparison data. The doublet
realification by itself does not provide that larger embedding.

## 2. Exact realification dictionary

Write z=E+iB in C^d with real E,B and let F=[E|B] in R^(d x 2).
Use R_alpha=[[cos alpha,-sin alpha],[sin alpha,cos alpha]]. Then

    e^(i alpha) z <-> F R_alpha^T,
    Kz=conj(z) <-> F sigma_z,
    J_B z=i conj(z) <-> F sigma_x,
    iz <-> F R_(pi/2)^T=[-B|E].

These are direct expansions of the real and imaginary parts. There is
no contradiction between J_B being antilinear on C^d and represented
by a real linear reflection on the realified carrier. The realification
retains the complex structure as the right action R_(pi/2)^T. The
reflection anticommutes with that complex structure; it has not become
a complex-linear operator on the original C^d.

This is precisely the distinction stated in r04's purpose and consequence.
It does not require a new physical law or a redefinition of J_B.

## 3. What the Gram matrix retains and forgets

For d=3 let G=F^T F. In units with light speed one,

    G=[[|E|²,E.B],[E.B,|B|²]],
    u=(|E|²+|B|²)/2,
    s=z.z=|E|²-|B|²+2i E.B,
    det G=|E cross B|².

Thus G retains the separate magnitudes, their mutual scalar product,
the invariants s, the energy density u in the chosen observer frame,
and the magnitude of the energy flux. It forgets the absolute spatial
orientation of both vectors and the direction of E cross B. The source
explicitly records this last loss after r04.3.

More precisely, two real 3x2 matrices with the same Gram matrix are
related by an orthogonal spatial map: their columns define an isometry
on their spans, which extends to R³. Because their spans have dimension
at most two, the extension can be chosen in SO(3) by adjusting the
unused perpendicular direction if needed. This does not mean their
response to a fixed external boost direction is identical: that direction
has not also been rotated in such a comparison.

For nonzero F, rho=G/Tr G additionally discards the overall intensity.
It retains only s/(2u). At F=0, rho is undefined; zero energy must not
be encoded as the null-field density I/2 by this normalization.

## 4. Same G and rho, different response to the same boost

Take the two nonzero null fields

    E_+=E_-=e_x,    B_+=+e_y,    B_-=-e_y.

Both have G=I, rho=I/2, u=1 and s=0. Their energy fluxes are
S_+=+e_z and S_-=-e_z. Consider the same passive boost along +z,
with speed v=tanh eta and gamma=(1-v²)^(-1/2). Define the sign convention
by

    E'=gamma(E+v_vec cross B) - longitudinal correction,
    B'=gamma(B-v_vec cross E) - longitudinal correction.

The longitudinal corrections vanish for these transverse fields. Hence

    E_+'=gamma(1-v)e_x,    B_+'=gamma(1-v)e_y,
    E_-'=gamma(1+v)e_x,    B_-'=-gamma(1+v)e_y,
    u_+'=exp(-2 eta),    u_-'=exp(+2 eta).

Both normalized matrices remain rho'=I/2, but G'_+=exp(-2eta)I and
G'_-=exp(+2eta)I. The original G, even supplemented with u, cannot
determine the boosted G without the missing flux direction. Reversing
the convention for the passive boost swaps the two exponent signs and
does not alter the nonuniqueness.

Equivalently, for the stated convention

    T00'=gamma²(u-2v S_z+v² Tzz).

For these null transverse fields Tzz=u. The two signs of S_z produce
exactly the same energy factors. The formula is also obtained by the
explicit field substitutions above, so the example does not rely on
an unstated stress-tensor sign convention.

## 5. The normalized rho itself can also have different boost responses

The null example leaves rho at the centre and therefore does not alone
prove that boosted normalized states differ. A non-null extension does.
Choose a,b>0 with a!=b and

    E_+=E_-=a e_x,    B_+=+b e_y,    B_-=-b e_y.

Both initially have G=diag(a²,b²), the same normalized rho,
u=(a²+b²)/2 and real nonzero s=a²-b². The same boost gives

    E_+'=gamma(a-vb)e_x,    B_+'=gamma(b-va)e_y,
    E_-'=gamma(a+vb)e_x,    B_-'=-gamma(b+va)e_y,
    u_+'=gamma²[(1+v²)u-2vab],
    u_-'=gamma²[(1+v²)u+2vab].

In both cases s'=s, by cancellation of the mixed terms and
gamma²(1-v²)=1. For v!=0 the energies differ and therefore

    rho_+'=(I+s sigma_z/(2u_+'))/2,
    rho_-'=(I+s sigma_z/(2u_-'))/2

are different. Thus there is no universally defined boost-update function
rho -> rho' using rho alone; even the pair (rho,u), or G alone, is
insufficient for a fixed spatial boost. A signed spatial flux/stress
description or the original F is needed.

These are different initial fields with the same reduced readout, not
an inconsistency of Lorentz transformation or an observer-dependent
change of the field's invariant s.

The r04 description that boosts move b radially is consistent with
s remaining fixed and u changing, but does not specify a closed boost
law on b. It also requires directional and degeneracy qualifications:
for E=e_x,B=0, a boost along x leaves the field and rho unchanged.
A null nonzero field stays b=0 and cannot be transformed into a nonzero
parallel E,B configuration. An unrestricted monotonic statement that
every boost sends every field toward the disk centre would be too strong.

## 6. The corrected opposite map is also already represented

Under iz the real field transforms by R_(pi/2)^T, and

    G' = R_(pi/2) G R_(pi/2)^T,
    rho'=sigma_y rho sigma_y

for the real symmetric rho of this dictionary. The equality follows
because R_(pi/2)=-i sigma_y and its transpose is i sigma_y. It flips
both real Bloch coordinates. In contrast, J_B uses sigma_x and flips
only the sigma_z coordinate.

This reproduces the source's r28 distinction and port exchange. On the
full complex Bloch ball sigma_y conjugation leaves the sigma_y component
unchanged, so whole-vector reversal remains restricted to the real disk.

## 7. Projector lifting changes the scalar field

The real doublet matrices C_+=(I+sigma_x)/2 and C_-=(I-sigma_x)/2
are ordinary rank-one orthogonal projectors on R². Acting on F by right
multiplication, they lift to real-linear operators on C^d viewed as R^(2d):

    C_R^+(z)=(z+i conj z)/2,
    C_R^-(z)=(z-i conj z)/2.

Their real ranks are d. Their ranges satisfy respectively E=B and
E=-B. Multiplication by i exchanges these ranges; neither range is a
nonzero complex subspace of the original C^d. Therefore these lifted
projectors are not complex-linear projectors on that original field space.

For example C_R^+(iz)=i C_R^-(z), not i C_R^+(z). Treating the 2x2
matrix C_+ as a complex rank-one projector on an abstract C² is possible
after complexification, but is a different carrier statement. Its
complexification on C^(2d) has complex rank d; it is not a recovered
complex projector P_C7 on the original C^d or on a native 16-mode space.

This matters for commutants. Real-linear maps commuting with J_B may
act independently on its two real eigenspaces. Requiring them also to
be complex-linear forces them to commute with multiplication by i and
ties these two actions together. In original complex coordinates, a
complex-linear L commuting with J_B=iK must satisfy L=conj L. The
real-linear commutant is therefore larger than the complex-linear one.

In particular, the source's real port weighting

    lambda_+ C_R^+ + lambda_- C_R^-
      = a I+b iK,
    a=(lambda_++lambda_-)/2, b=(lambda_+-lambda_-)/2

is complex-linear on the original C^d only if b=0. A nondegenerate real
port weighting is not automatically a complex-linear Hamiltonian or a
complex-linear M16. This is not an error in r05, which explicitly works
with real doublet matrices and leaves the full M16 unidentified. It is
a restriction on transferring that result into later positive complex
operator models without specifying their carrier and complex structure.

## 8. Consequence and verification

The existing r04 dictionary resolves the apparent mismatch between the
antilinear field map and its real reflection matrix. The unresolved
transition lies further on: Gram readout loses spatial information,
normalized rho loses intensity, and real spectral ports need not lift
to complex-linear physical closure projectors. A frame reconstruction
using only rho, or a rank-one complex-projector argument borrowed from
an abstract qubit, cannot silently recover those missing data.

Analytically checked: real/imaginary expansion, Gram identities,
SO(3) extension argument, both explicit boost pairs including non-null
normalized states, the r28 conjugation action, idempotence and scalar-field
type of the lifted projectors, and commutant restrictions. No numerical
experiment or physical parameter fitting was used.

Source SHA-256:

`sources/research/parts/v490-post-release-layers.tex`

`232bdd631bac34259be48b6d326fbf6eaf38f084ee4bec1a621658b3c964424e`

Only this audit note was written. The native full M16/P_C7 map remains
unidentified; the already present lower-level realification is retained.
