# Independent audit: norm and energy in a real three-mode action

26 October 2026. Base checkpoint:
`a97e32d25b4b66ec2d534bdbc142df7b51883057`.
Exact conditional modal calculation, hbar=1, no numerical experiment,
manuscript change or native stress-tensor identification.

## 1. Contract and relation to the native sources

Assume three complex commuting mode amplitudes f=(f_1,f_2,f_3), or three
vectors f_i in fixed finite positive Hilbert blocks. Normalize the fixed
kinetic inner product to identity and supply a Hermitian H(t)=H(t)†.
Consider the real first-order action

    L=i/2(f† dot f-dot f† f)-f† H(t) f.

The positive kinetic metric and a positive Hamiltonian are different
conditions. The derivations below require the former and Hermiticity,
not H>=0. Section 5 supplies an explicitly positive H as a stronger
counterexample. A fixed nonidentity positive kinetic metric may first
be normalized by a fixed change of coordinates; a varying metric would
introduce further terms and is outside this contract.

`sources/research/parts/v470/10_sphaera_and_physics.tex`,
`prop:triadic-two-probe`, supplies three coupled channels and symbolic
operators. Its `thm:variational-form` supplies a field action with
connection, projector and compensator terms. These do not by themselves
derive the positive finite modal action above. The differences are already
explicit in `analysis/HC_Real_Probe_Current_Closure.md` and
`analysis/HC_Collective_Action_Reduction.md`: physical adjoint, reality,
mode profiles, omitted field variations and normal equations matter.

## 2. Equations of motion and exact norm currents

Varying f and f† independently, subject to the usual compatible real
field variation and fixed endpoints, gives

    i dot f=H(t) f,    dot f†=i f†H(t).

Hence N=f†f has dot N=0 even for explicitly time-dependent Hermitian H.
For the mode population n_i=f_i†f_i,

    dot n_i=sum_(j!=i) J_(j->i),
    J_(j->i)=2 Im(f_i† H_ij f_j).

Hermiticity H_ji=H_ij† gives J_(i->j)=-J_(j->i). Thus all internal
transfers cancel in sum_i dot n_i=0. The diagonal expectation
f_i†H_ii f_i is real and makes no direct norm-current contribution.
For scalar modes f_i=sqrt(n_i) exp(i phi_i) and
H_ij=|H_ij| exp(i theta_ij), this becomes

    J_(j->i)=2 |H_ij| sqrt(n_i n_j)
                  sin(theta_ij+phi_j-phi_i).

The edge-current formula is well defined directly in f even if a
population vanishes; phase coordinates then cease to be defined.
These are modal norm currents, not identified spatial Poynting fluxes,
particle-number currents or energy currents of the native field theory.

## 3. Total energy includes all coupling coherences

The canonical time-translation energy of the declared action is

    E=dot f.(partial L/partial dot f)
        +dot f†.(partial L/partial dot f†)-L
     =f†H(t)f.

The first-order momenta are constrained, but this algebraic energy
identity and its on-shell balance follow directly from the action.
For scalar modes,

    E=sum_i H_ii n_i
        +2 Re sum_(i<j) f_i* H_ij f_j,

and the same expression with block inner products holds for Hermitian
blocks. The interaction energy is not generally zero and cannot be
omitted by adding only diagonal mode energies.

For fixed nonzero scalar couplings, the cross contributions depend on
cos(theta_ij+phi_j-phi_i), whereas the norm currents depend on the sine
of those phases. Populations alone therefore do not determine either
the full energy or the instantaneous transfer pattern.

## 4. Explicit-time dependence gives a work term

Differentiate E and use the equations of motion:

    dot E=dot f†Hf+f†dot H f+f†H dot f
         =f†dot H f.

The two H² terms cancel exactly. Thus for prescribed H(t),

    E(t_2)-E(t_1)=integral_(t_1)^(t_2) f(t)† dot H(t) f(t) dt.

This is the work supplied to the modal subsystem by the prescribed
parameter variation. Constant H gives exact energy conservation. If
the couplings come from dynamical apparatus/background fields, their
equations and energy must be included to establish conservation of the
larger closed system. The prescribed-time calculation alone does not
provide that missing background energy or treat it as free.

Redistribution of populations may occur at fixed total E. Conversely,
unchanged populations do not guarantee a fixed E when coherences or
externally driven couplings change.

## 5. Exact three-coupling phase counterexample with positive energy

Choose real g>0 and m>g, and fix

    H=m I_3+g [[0,1,1],[1,0,1],[1,1,0]]
      =(m-g) I_3+g 1_3 1_3^T.

All three pair couplings are nonzero. The eigenvalues are m+2g and
m-g with the latter of multiplicity two, so H is positive definite.
Let zeta=exp(2 pi i/3), for which 1+zeta+zeta²=0, and take

    f_A=(1,1,1)^T/sqrt(3),
    f_B=(1,zeta,zeta²)^T/sqrt(3).

Both have N=1 and populations (1/3,1/3,1/3). Nevertheless

    H f_A=(m+2g)f_A,    E_A=m+2g,
    H f_B=(m-g)f_B,     E_B=m-g.

Their energies differ by 3g despite identical populations and positive
energies. Since both states are eigenstates, their populations remain
identical for every time under this same fixed H. This is not merely
an instantaneous comparison.

For f_A every edge norm current is zero. For f_B there is a circulation:

    J_(2->1)=J_(3->2)=J_(1->3)=sqrt(3)g/3,

with the reversed currents negative. Each mode has zero net incoming
current, so every population is stationary despite nonzero edge currents.
This extra distinction illustrates information lost by diagonal population
readouts. It is an internal three-mode circulation, not a claimed
spatial circulating energy flow.

The two states are different physical preparations in this fixed model.
A passive rephasing of both f and H does not change their energy gap;
rephasing f alone while holding the specified H fixed is not a common
basis transformation of the same preparation.

## 6. A moving unitary basis separates generator and energy observable

Let b=U(t)f with differentiable unitary U(t). Direct differentiation gives

    i dot b=H_gen' b,
    H_gen'=U H U†+i dot U U†.

The physical energy observable of the original subsystem transforms as

    H_phys'=U H U†,
    b† H_phys' b=f†Hf.

The connection i dot U U† belongs to the moving-coordinate generator.
It is not automatically additional physical energy. Their difference
also follows by substituting f=U†b into the action: the kinetic term
contributes the basis-connection term, producing H_gen' in the canonical
moving-coordinate form.

The original work law is recovered exactly in the new description:

    d/dt <H_phys'>
       =b†[partial_t H_phys'+i[H_gen',H_phys']]b
       =f†dot H f.

For example U(t)=exp(i alpha(t))I gives
H_gen'=H-dot alpha I, while H_phys'=H. A scalar energy-looking shift
in the moving generator can therefore be only a coordinate phase term.
It must not be identified with a physical change in vacuum energy or
external work without specifying which Hamiltonian is the observable.

This concerns time-dependent unitary basis changes in the declared
positive modal metric. It does not identify physical Lorentz boosts,
the source's antilinear maps or a changed metric with such a U.

## 7. What the calculation establishes and leaves open

The conditional three-mode action supplies a complete local modal
norm and energy ledger: pairwise norm transfer, coupling coherence
energy and work from explicit driving. It proves that diagonal readout
populations alone cannot determine total energy even for three positive
energies and three active Hermitian couplings.

It supplies no pressure, stress tensor, field-energy density, physical
clock scale, dissipative attractor or absolute gravitating energy offset.
Those require the native spatial realization and the full real action
including its metric/background/connection/projector variations. Neither
a neutral population pattern nor conservation of modal E establishes
vacuum form or Lambda=0.

## 8. Verification and input fingerprints

Checked analytically: Euler--Lagrange signs, antisymmetry of edge currents,
canonical energy, cancellation of H² terms, all eigenvalues and phases
in the positive three-coupling witness, and moving-basis generator versus
observable work balance. No numerical sample was used as proof.

| Repository-relative input | SHA-256 |
|---|---|
| `sources/research/parts/v470/10_sphaera_and_physics.tex` | `7d72c58b1159f5462c6be395961fcd8882028fc3e8c8495e7f2a3b10055c1a32` |
| `analysis/HC_Real_Probe_Current_Closure.md` | `cd787b6664b9ad8d03bad97831b707e17033e3ab6e8463ae035080745c07edc6` |
| `analysis/HC_Collective_Action_Reduction.md` | `0055f72e6587e3e2be0b0fbd0ba6291fcf3e3a0b49a2fd032021d5624ddd8a72` |

Only this note was written. No source definitions, native coefficients,
Git state or public OP status were changed.
