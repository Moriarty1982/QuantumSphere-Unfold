# v4.2.0-r02 DEV-PATCH: HS Split/Refold XOR Register Memory

Mode: DEV-PATCH only. No PDFs, no release metadata, no DOI/Zenodo text.

## Scope

This working patch extends the v4.2.0-r01 OP1/OP4 Joint HC-Dixon Reduction with a split/refold register-memory layer.

## Main additions

1. Even HS state `S_m=(K_m,R_m)`.
2. Focal split signature `sigma_m`.
3. XOR-like reversible register update:
   \[
   R_{m+1}=R_m\oplus\sigma_m.
   \]
4. No-erase refold guard:
   \[
   \operatorname{Refold}\neq\operatorname{Erase}.
   \]
5. Higher-HS alternation convention.
6. Lens signatures as finite shift data.
7. No higher-HS residual explosion criterion.
8. OP1/OP4 register-closure strengthening candidate.
9. r02 proof-obligation register.

## Status

This patch does not prove OP1, OP4, the OP1 compression load, or the selector values. It records a structural strengthening candidate explaining how higher HS layers may preserve route history through reversible register traces without visible exponential geometry.
