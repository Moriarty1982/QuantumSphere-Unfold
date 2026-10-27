# Independent audit: observer selected by a general 0–1 stress block

26 October 2026. Base revision:
`a97e32d25b4b66ec2d534bdbc142df7b51883057`.
Exact pointwise algebra with metric diag(-1,1,1,1), c=1. No energy
condition, native stress realization, numerical experiment or field
equation solution is assumed.

## 1. Contract and observer equation

Let the symmetric contravariant tensor have only the entries

    T^{00}=rho,    T^{01}=T^{10}=q,
    T^{11}=p,    T^{22}=p_2,    T^{33}=p_3,

where all five parameters are real. Its mixed-index matrix is

    T^mu_nu=[[-rho,q,0,0],[-q,p,0,0],
             [0,0,p_2,0],[0,0,0,p_3]].

A future unit timelike observer in the 0–1 plane has

    U=(cosh eta,sinh eta,0,0),
    V=(sinh eta,cosh eta,0,0),
    U.U=-1,    V.V=1,    U.V=0.

The observer measures zero spatial energy flux exactly when
T^mu_nu U^nu=-epsilon U^mu for a real epsilon. This epsilon is the
measured energy T^{mu nu}U_mu U_nu; it is not required to be positive
under the present algebraic contract.

## 2. Boost equation and measured energy

Use the passive boost convention in which the moving observer is U
with velocity v=tanh eta along +x. The measured energy and directed
flux are obtained by contraction with the observer tetrad:

    epsilon(eta)=rho cosh² eta-2q sinh eta cosh eta+p sinh² eta,
    q'(eta)=q cosh(2eta)-(rho+p)sinh(2eta)/2.

Let A=rho+p and Delta=A²-4q². The zero-flux equation is

    A tanh(2eta)=2q.

There is no division by A in this equation; that division is allowed
only when A!=0. If A!=0 and Delta>0, the solution is

    eta=(1/2)atanh(2q/A),
    v=2q/[A+sign(A)sqrt(Delta)].

The velocity expression is also regular at q=0 in this regime, where
its numerator vanishes and its denominator is 2A. Equivalently, for
q!=0 it is (A-sign(A)sqrt(Delta))/(2q). The other root of the quadratic
q v²-A v+q=0 is outside the timelike interval; the roots are reciprocal
when both are defined.

The finite solution has

    cosh(2eta)=|A|/sqrt(Delta),
    sinh(2eta)=2q sign(A)/sqrt(Delta).

Consequently its energy and longitudinal pressure are

    epsilon=(rho-p+sign(A)sqrt(Delta))/2,
    p_rest=(p-rho+sign(A)sqrt(Delta))/2.

The corresponding mixed eigenvalues are lambda_t=-epsilon and
lambda_s=p_rest. In particular one must not always choose the positive
square-root branch for epsilon: if A<0 the timelike eigenvector lies
on the other algebraic branch. No assumed energy condition removes
that case here.

## 3. Complete 0–1-plane existence classification

1. **Delta>0:** A is nonzero and |2q/A|<1. There is exactly one future
   unit timelike zero-flux observer in the plane. This includes q=0,
   A!=0, for which eta=0, epsilon=rho and p_rest=p.
2. **A=q=0:** Then p=-rho and the mixed 0–1 block is -rho times
   identity. Every eta is a solution with epsilon=rho. There is no
   distinguished plane observer, including when rho=p=0.
3. **Delta=0 with (A,q)!=(0,0):** Here q and A are both nonzero and
   2q/A=+1 or -1. The required rapidity has infinite magnitude. The
   repeated mixed eigenvalue (p-rho)/2 has only a null eigendirection
   (1,2q/A), not a normalized timelike eigenvector. The nonzero
   off-diagonal block is a nontrivial Jordan case.
4. **Delta<0:** No finite real rapidity solves the equation. The mixed
   0–1 block has no real eigendirection and no timelike observer. This
   includes A=0,q!=0.

These cases exhaust the real parameters. An infinite-rapidity limit
in case 3 is not a future unit timelike observer and must not be counted
as a rest frame.

## 4. Full 3+1 uniqueness and transverse degeneracies

In case Delta>0 the 0–1 block has the distinct eigenvalues
lambda_t=-epsilon and lambda_s=p_rest. Its two eigenvectors U,V are
respectively timelike and spacelike. The transverse eigenvectors e_2,e_3
are spacelike with eigenvalues p_2,p_3.

The future unit timelike eigenvector is unique in the entire four-space
exactly when

    p_2!=lambda_t and p_3!=lambda_t.

If p_2=lambda_t, for example, every

    U_theta=cosh(theta)U+sinh(theta)e_2

is also a future unit timelike eigenvector. A second equality with p_3
enlarges this family further. Degeneracy of p_2 and p_3 with each other,
or with lambda_s only, is spatial degeneracy and does not destroy
timelike uniqueness.

In the scalar 0–1 case A=q=0, uniqueness is already lost within that
plane. Equality of a transverse eigenvalue with -rho merely enlarges
the family. If both equal -rho, T^{mu nu}=-rho g^{mu nu} and every
future unit timelike observer is an eigenvector.

In cases 3 and 4 a transverse component cannot rescue a timelike
eigenvector. In case 3 its possible 0–1 part is null and the added
transverse part is spacelike; their sum is never timelike. In case 4
a real eigenvector has no nonzero 0–1 part, so is purely spacelike.

## 5. Adding an arbitrary constant vacuum term

For a real constant C, set

    T_new^{mu nu}=T^{mu nu}-C g^{mu nu}.

Then

    rho_new=rho+C,    p_new=p-C,
    q_new=q,    (p_2)_new=p_2-C,    (p_3)_new=p_3-C,
    (T_new)^mu_nu=T^mu_nu-C delta^mu_nu.

Every mixed eigenvector and every eigenspace is unchanged. All
eigenvalues shift by -C, so every degeneracy condition is unchanged.
In particular A,Delta,eta and v are unchanged, while

    epsilon_new=epsilon+C,    (p_rest)_new=p_rest-C.

This remains true if epsilon+C passes through zero or becomes negative:
the algebraic rest direction is independent of that offset. A rest-frame
selection rule based only on the stress eigenvectors cannot determine C.
The statement is not that C fails to gravitate; its metric field equation
and energy/pressure contribution are different obligations.

For a point-dependent C(x), the same eigenvector statement holds
pointwise, but conservation changes by -partial^nu C. A variable vacuum
term cannot be assumed to solve the same dynamical conservation equation.

## 6. Independent control: a homogeneous positive triadic Dirac probe

Use exactly the declared comparison conventions of
`analysis/HC_Dirac_State_Gravity.md`, section 1, equation (3):

    beta=diag(1,1,-1,-1),    Gamma^0=beta,
    Gamma^i=beta alpha_i,    {Gamma^mu,Gamma^nu}=-2g^{mu nu}I,
    barPsi=Psi† beta,
    T_mu_nu=-i/4[barPsi Gamma_mu <->partial_nu Psi
                 +barPsi Gamma_nu <->partial_mu Psi].

Here alpha_i is Hermitian and anticommutes with beta. Fix a constant
positive Hermitian internal matrix M commuting with all spin matrices,
and choose a normalized spinor s_+ with beta s_+=s_+. Let

    f(t)=exp(-i M t)f_0,
    Psi(t)=f(t) tensor s_+,
    partial_i Psi=0.

Then (i Gamma^mu partial_mu-M)Psi=0 because i Gamma^0 dotPsi=M Psi
on the positive-beta spinor. With lowered Gamma_0=-beta,

    barPsi Gamma_0 <->partial_0 Psi=2i f†Mf.

Therefore T_00=f†Mf=:rho_D. The only possible off-diagonal term is
proportional to f†Mf times s_+†alpha_i s_+, which vanishes because
alpha_i maps the positive-beta eigenspace to its orthogonal negative-beta
eigenspace. Every spatial-spatial term vanishes through partial_i Psi=0.
Thus the full stress, with either both indices raised or both lowered, is

    T=diag(rho_D,0,0,0),    rho_D=f_0†M f_0>0

for f_0!=0. Its trace is -rho_D=-barPsi M Psi as required by the source.
The modal expectation is constant because M commutes with exp(-iMt).

This control permits genuine three-channel couplings, for example

    M=(m-g)I_3+g 1_3 1_3^T,    m>g>0.

All three pair couplings are nonzero. Initial channel phases can alter
rho_D at fixed channel populations: the equal-phase vector and the
cube-root-phase vector in `OP5_Triadic_Energy_Independent.md` give
m+2g and m-g at unit norm. Nevertheless both stresses select the same
observer U=(1,0,0,0); there is no spatial flux in either preparation.

After adding -C g, the stress is diag(rho_D+C,-C,-C,-C). Its mixed
timelike eigenvalue is -(rho_D+C) and its spatial eigenvalues are -C,
separated by rho_D!=0 for every C. The rest observer stays unique and
unchanged even when rho_D+C=0. Phases change energy density but not the
rest direction in this explicitly homogeneous special case.

This is a local homogeneous probe on a fixed flat metric, not a globally
finite-energy packet or a native state identification. With nonzero
stress the flat metric does not satisfy a coupled Einstein equation by
itself. No backreaction, native closure, gauge source or full field
solution is claimed. Spatially varying or momentum-superposed states
can have different flux and stress and are not covered by this control.

## 7. Verification and scope

Analytically checked: the observer tetrad contractions, finite boost
solution and its sign(A) branch, scalar/Jordan/complex-eigenvalue cases,
full transverse degeneracies, identity shift by C, and the homogeneous
Dirac equation and all stress components with the negative Clifford
convention. No numerical experiment is needed for these identities.

The general stress block is supplied as input, not derived from a native
action. The Dirac control uses only the explicitly declared comparison
action and stress of `analysis/HC_Dirac_State_Gravity.md`, whose SHA-256 is

`2f73c9e3278b39a2c70ae4a710d1b04b1b03414462fb7bcf5160102a127ad16d`.

Only this note was written. The calculation establishes conditional
observer selection and its energy-offset blindness, not a mechanism
for selecting a closure projector or a cosmological constant.
