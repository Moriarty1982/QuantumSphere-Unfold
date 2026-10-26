# Independent audit: corrected opposite map, stress and observer neutrality

26 October 2026. Base checkpoint:
`3fa5ba9440d0985fbb2b3786eaebe56a887cfe6a`.
Bounded exact audit in the electromagnetic field model, with signature
(-+++), c=1 and real local E,B. No identification with the full native
M16, P_C7 or an independently derived cosmological stress tensor.

## 1. Source and result

The native source `sources/research/parts/v490-post-release-layers.tex`,
r04.2–r04.3, defines F=[E|B], G=F^T F, rho=G/Tr G and records that G
forgets flux direction. Its r28 correction identifies the opposite
real-disk state map with z->iz, not J_B:i conj(z).

**Result:** The corrected opposite map reverses the real Bloch vector
but leaves the full Maxwell stress-energy tensor, including Poynting
flux, unchanged. Equal opposite-state mixing is therefore not generally
momentum-neutral. Conversely, J_B reverses the flux but not the entire
Bloch vector. A single non-null field need not select a unique zero-flux
observer; a nonzero null field has no such timelike observer at all.

The already established realification dictionary and Gram information
loss are retained; see `OP5_Realification_And_Gram_Boundary.md` for the
current parent checkpoint. Nothing here restores missing native matrices.

## 2. Definitions and complete stress components

In the chosen observer coordinates define

    u=(|E|²+|B|²)/2,    S=E cross B,
    T^{00}=u,    T^{0i}=T^{i0}=S_i,
    T^{ij}=u delta_ij-E_i E_j-B_i B_j,
    s=z.z=|E|²-|B|²+2i E.B,    z=E+iB.

This fixes all signs and normalization for the following algebra. T is
the classical Maxwell stress tensor in this declared model. The index
positions matter: the mixed operator is T^mu_nu=T^{mu alpha}g_{alpha nu}.

For nonzero field G has trace 2u and

    rho=(I+b_z sigma_z+b_x sigma_x)/2,
    b_z=Re(s)/(2u),    b_x=Im(s)/(2u).

At zero field rho is undefined rather than a normalized neutral state.

## 3. Corrected opposite map preserves every stress component

The map D:z->iz acts as

    E_D=-B,    B_D=E.

Direct substitution gives

    u_D=u,
    S_D=(-B) cross E=E cross B=S,
    (E_D)_i(E_D)_j+(B_D)_i(B_D)_j=B_iB_j+E_iE_j.

Therefore T_D^{mu nu}=T^{mu nu} in all components. Meanwhile s_D=-s,
so the normalized real-disk Bloch vector changes sign. Equivalently
rho_D=sigma_y rho sigma_y as r28 states.

For a statistical equal mixture of the two field configurations,

    rho_bar=(rho+rho_D)/2=I/2,
    T_bar=(T+T_D)/2=T,
    S_bar=S,    u_bar=u.

Here equal mixing of normalized Gram states agrees with normalization
of the equally averaged Gram matrices because u_D=u. This special
agreement does not identify Gram-state mixing with any general physical
quantum measurement or coherent amplitude superposition.

In particular, when S!=0 the neutral Bloch mixture still transports
nonzero energy and momentum in the same direction. It does not select
a momentum-rest frame, cancel gravitating stress or enforce vacuum form.

## 4. Explicit non-null control and the single-field/ensemble boundary

Choose E=2 e_x and B=e_y. Then

    u=5/2,    S=2 e_z,    s=3,
    G=diag(4,1),    G_D=diag(1,4),
    rho=diag(4/5,1/5),    rho_D=diag(1/5,4/5).

The equal mixture has rho_bar=I/2, but u_bar=5/2 and S_bar=2 e_z.
Its averaged stress is the same original non-null stress. The initial
spatial stress is diag(-3/2,3/2,5/2), also unchanged by D.

For a single real field value the exact identities are

    det G=|S|²,    u²-|S|²=|s|²/4.

For the mixture, G_bar=(5/2)I has determinant 25/4, whereas
|S_bar|²=4. Also s_bar=0 while u_bar²-|S_bar|²=9/4. These do not
contradict the identities: those identities relate quadratic invariants
of one field configuration, not determinants or squares of already
averaged second moments. The mixture cannot be reinterpreted as a single
null field with the same full stress merely because its Gram rho is central.

Thus an augmented ensemble readout (T_bar,s_bar) can reconstruct the
averaged G using its linear entries, but cannot automatically reconstruct
a single underlying field or apply all single-field invariant identities.

## 5. J_B has different flux and state actions

The structural involution J_B:z->i conj(z) acts as

    E_J=B,    B_J=E.

It preserves u and the spatial stress, but S_J=B cross E=-S. Its
effect on the invariant is s_J=-conj(s), so b_z changes sign while
b_x is retained. Consequently an equally weighted incoherent J_B pair
has zero average flux but

    rho_bar,J=(I+b_x sigma_x)/2.

It is central only when E.B=0. This is exactly why J_B and the corrected
opposite map cannot be used interchangeably: one may cancel the directed
flux while the other reverses both disk coordinates. Neither operation
alone proves zero total energy. Both pairs retain positive u for any
nonzero input field.

The labels describe the declared local field transformations. Calling
J_B a physical exchange process requires its own dynamics and conservation
law; these algebraic substitutions do not provide that interaction.

## 6. A single non-null field need not choose a unique zero-flux observer

Let E=E_0 e_z with E_0!=0 and B=0. Then u=E_0²/2>0, and

    T^{mu nu}=diag(u,u,u,-u),
    T^mu_nu=diag(-u,u,u,-u).

For every real rapidity eta define the future unit timelike observer

    U^mu(eta)=(cosh eta,0,0,sinh eta),    g(U,U)=-1.

Direct multiplication gives

    T^mu_nu U^nu=-u U^mu.

The spatial projector in that observer's rest frame is
h^mu_nu=delta^mu_nu+U^mu U_nu. Its measured energy flux is

    q^mu=-h^mu_alpha T^{alpha beta}U_beta=0,
    rho_U=T^{alpha beta}U_alpha U_beta=u.

Thus an entire one-parameter family of distinct observers has zero
flux and the same energy density. This exact non-null example refutes
any universal claim that the stress tensor of one non-null Maxwell field
always selects a unique Landau/rest observer. It does not refute the
possibility that additional independent physical components select one.

## 7. A nonzero null field has no timelike zero-flux observer

For a nonzero null field let k=(1,n), |n|=1. Its stress has the form

    T^{mu nu}=u k^mu k^nu,    u>0,    k.k=0.

A zero-flux timelike observer would satisfy an eigenvector equation
T^mu_nu U^nu=-rho_U U^mu, with rho_U>0. The left side is
u k^mu(k.U), parallel to a null vector, whereas the right side is
parallel to a timelike vector. They cannot be equal. The alternative
rho_U=0 is also impossible because k.U is nonzero for a future timelike
U and nonzero future null k, and rho_U=u(k.U)²>0.

Hence the rho=I/2 assigned to a single nonzero null field does not define
its rest observer. It is a reduced port-coordinate statement, not a
momentum-rest condition. This conclusion is independent of the earlier
mixture example, whose central Gram rho can have non-null averaged stress.

## 8. Consequence for a neutral multi-reference construction

If neutrality means zero momentum flux, it must be checked using the
total physically defined T, not merely b_bar=0. Two corrected duality
partners have identical stress and do not constitute counterpropagating
streams. A second genuinely independent component can change the stress
eigenstructure; earlier work on positive counterstreams already illustrates
this possibility, so no novelty is claimed for that route here.

Even a unique zero-flux observer would define a rest frame for the supplied
matter content, not a vanishing vacuum energy or cosmological constant.
The components, their weights and their dynamics must first be specified.
The native M16/P_C7 correspondence remains a separate missing bridge.

## 9. Verification and source fingerprint

Analytically checked: all ten independent Maxwell stress components
under D and J_B, the non-null field/mixture invariants, mixed-index
eigenvector signs for signature (-+++), observer normalization and
the null no-timelike-eigenvector argument. No numerical experiment or
physical parameter fit was performed.

Source SHA-256:

`sources/research/parts/v490-post-release-layers.tex`

`232bdd631bac34259be48b6d326fbf6eaf38f084ee4bec1a621658b3c964424e`

Only this note was written. The result is an exact audit of the declared
Maxwell/doublet reading, not a stress-tensor derivation for the complete
native theory.
