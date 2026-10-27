# Boost tangent diagnosis

2026-10-27. Local diagnostic, not a solution of the native field theory. Reproduce with OP5_Boost_Tangent_Check.py and its JSON output.

Hold the fields, spatial jets and fitted Hamiltonian of OP5_Counterflow_Full_Residual_Result.md fixed. Fit the missing instantaneous velocity w=iR to real tangent vectors of psi=B(v)(xi,0), where xi is an arbitrary complex two-spinor and v a real subluminal velocity. Four real rest-spinor directions and three velocity directions give rank seven per species inside eight real Dirac components. Complex boost coefficients are not allowed. The normalization B/sqrt(gamma) used in the script does not change the manifold because rest amplitudes are free.

Remaining squared residual as percentage of the original full residual:

| Tangent family | P1=(1,0.6,0,0) | P2=(1,0.4,0.2,0.2) |
| --- | ---: | ---: |
| Rest spinors only, boosts fixed | 100.0000 | 94.6620 |
| Independent A, B, C boosts | 10.8637 | 12.7096 |
| Common A/B boost, separate C | 42.8028 | 39.5067 |
| Common A/B boost, opposite C variation | 97.8001 | 93.8593 |

All rows allow independent spin, phase and amplitude changes. These relaxed fits do NOT impose the cross coframe or spin-balance constraints. A fitted component is therefore not automatically a physically admissible correction. A residual surviving even this relaxed fit cannot be repaired by imposing more constraints. This tests active field changes, not passive coordinate transformations.

The remaining direction has an algebraic interpretation. Define gamma5=[[0,I],[I,0]], P5=i beta_D gamma5 and p5=psi^dagger P5 psi. P5 is Hermitian, P5^2=I and anticommutes with every alpha_i. Thus B^dagger P5 B=P5 for a Lorentz boost. Pure upper rest spinors have p5=0, so the entire chosen boosted-rest family does too. The desired velocity instead has dp5=2 Re(psi^dagger P5 w) nonzero for each species.

Rates (A,B,C) are (12.44016936,0.89316397,-13.33333333) at P1 and (16.69023860,1.19830522,-17.88854382) at P2, in comparison units. Their sum cancels, but individual zero-pseudoscalar constraints fail. The real normal P5 psi predicts the residual norm squared as dp5^2/(4||P5 psi||^2). This independently reproduces the least-squares residual for every species; totals are 11.11111111 and 20. Matrix ranks, singular values and residuals are recorded in JSON. Boost invariance was also checked by exact matrix algebra.

Consequently the fixed boosts explain much, but not all, of the mismatch. A passive frame change cannot remove the nonzero pseudoscalar-rate obstruction. No antiparticle production, tachyons, necessary spacetime curvature or physical numerical prediction follows. These are two numerical samples of analytic derivatives; no regional existence theorem or independent review is claimed. OP5 remains open.
