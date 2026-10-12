# v4.2.0-r01 DEV-PATCH: OP1/OP4 Joint HC-Dixon Reduction

Mode: DEV-PATCH only. No PDFs, no release metadata, no DOI/Zenodo text.

## Scope

This working patch adds a local OP1/OP4 transfer section after the v4.1.0 OP5 closure hardening layer.

The intended section title is:

```text
v4.2.0-r01 OP1/OP4 Joint HC--Dixon Reduction Candidate
```

## Main additions

1. HS(0)-anchored Hilbert-shift ladder.
2. OP1 continuum-compression determinant.
3. OP1 compression load
   \[
   \Omega_{CL}=\gamma_1/(4\pi\gamma_L^5).
   \]
4. Exponential HC/Dixon determinant lemma.
5. CL-to-OP5 load factorization and CL residual inheritance.
6. Finite Fano/Dixon mediator table for CKM.
7. CKM selector normal form:
   \[
   s_{12}=2(15/16)\gamma_s\delta_{CL},\quad
   s_{23}=2(4/3)\gamma_s^2\delta_{CL},\quad
   s_{13}=2\gamma_s^3\delta_{CL}^2.
   \]
8. CKM phase candidate:
   \[
   \phi_q=\pi/3+2\Omega_{CL}.
   \]
9. PMNS triolic/Fano-leakage candidate:
   \[
   \theta_{12}=\arcsin(1/\sqrt3)\delta_{CL},\quad
   \theta_{23}=\arctan(\sqrt2)\delta_{CL}^2,\quad
   \theta_{13}=\arcsin((7/6)\gamma_s).
   \]
10. Frame-extraction residual and joint OP1/OP4 residual ledger.

## Governing status language

This patch does **not** claim global OP1 or OP4 closure. It records a conditional local closure architecture inside the OP5-inherited HC/Dixon/Fano/triolic readout grammar.

## Local artifact packet

The full local DEV-PATCH packet generated in the ChatGPT workspace contains:

- `Quantum_Sphaera_Companion_v4_2_0_r01_active_core_op1_op4_joint_hcdixon_reduction.tex`
- `OP1_OP4_Joint_HC_Dixon_Reduction_v4_2_0_r01_section.tex`
- `v4_2_0_r01_op1_op4_joint_hcdixon_reduction.patch`
- `SOURCE_AUDIT_v4_2_0_r01.txt`
- `MANIFEST_v4_2_0_r01.txt`
- `CHECKSUMS_v4_2_0_r01.sha256`

The full active-core TeX was intentionally not committed here as routine repo content; the recommended repo form for development is patch/section first, PDF only at FREEZE/RELEASE.
