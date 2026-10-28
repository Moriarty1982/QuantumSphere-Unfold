# One triadic chiral tangent completes the relaxed sampled velocity fit

2026-10-27. Follow-up to OP5_Boost_Tangent_Result.md. Reproduce with OP5_Chiral_Tangent_Check.py and its JSON. This script extends the same real tangent-space test; it is not an independent review.

## Missing internal variable

Enlarge each field locally by psi(chi)=exp(i chi gamma5/2)psi. This is an active internal chiral change, not an ordinary phase and not a Lorentz boost. At chi=0 its tangent is i gamma5 psi/2. If scalar sigma=psi^dagger beta_D psi and pseudoscalar p5=psi^dagger i beta_D gamma5 psi, then dp5/dchi=-sigma. Thus it can leave the p5=0 submanifold that trapped the boosted-rest ansatz.

For the prescribed fields sigma is nonzero at both points. Required rates -dp5/sigma are:

| Point | chi_dot_A | chi_dot_B | chi_dot_C |
| --- | ---: | ---: | ---: |
| P1 | -2.0833333333 | -2.0833333333 | +2.0833333333 |
| P2 | -2.5649458802 | -2.5649458802 | +2.5649458802 |

Hence one triadic tangent with signs (+,+,-) spans the three missing normal components of this particular residual. This relation is sampled evidence, not a universal native law.

## Combined fit

Adding this one tangent to the independent-boost and arbitrary-rest-spinor fit gives rank 22 in 24 real field components. At both points the squared residual is below 4e-28 (floating-point evaluation). Thus the desired instantaneous velocity lies in this enlarged tangent space at the samples, despite the space not filling all 24 directions.

Keeping the common A/B and opposite-C boost restriction instead leaves 86.9364% and 81.1497% of the original squared residual. The chiral variable alone therefore does not save the rigid counterflow ansatz. The successful fit releases independent boost and rest-spinor variations and does not preserve the original geometric constraints by construction.

## Geometric meaning and limits

For an individual field, chiral rotation preserves the vector and axial-vector bilinears because gamma5 commutes with I, alpha_i and their axial counterparts. A common chiral rotation of A and B preserves their cross vector. These observations explain why an internal variable can be invisible in some Bloch/current diagnostics. They do not establish that the full connection-dependent coframe, stress, or field equation is preserved. Off-diagonal connections, derivatives, and mass terms must be treated consistently.

We have represented the previously mismatched instantaneous derivative; we have NOT changed the old fields into a solved PDE trajectory. In particular spatial derivatives, connection and source fields must be evolved together, with constraint propagation and the native operator representation checked. Fitting unrestricted matrix potentials would not supply that derivation. No spacetime curvature, empirical parameter or physical vacuum-energy result has been deduced. OP5 remains open.
