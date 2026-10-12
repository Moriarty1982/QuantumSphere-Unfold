# v4.2.0-r02 DEV-PATCH: HS Split/Refold XOR Register Memory

Mode: DEV-PATCH only. No PDFs, no release metadata, no DOI/Zenodo text.

## Scope

This working patch extends the v4.2.0-r01 OP1/OP4 Joint HC-Dixon Reduction by adding a higher-HS split/refold register-memory layer.

The intended section title is:

```text
HS split/refold XOR register memory
```

## Main additions

1. Even HS state `S_m=(K_m,R_m)`.
2. Focal split `K_m -> (K_m^-,K_m^+)`.
3. Split signature `sigma_m` carrying branch, lens, selector, residual, and orientation data.
4. XOR-like reversible register update:
   \[
   R_{m+1}=R_m\oplus\sigma_m.
   \]
5. No-erase refold guard:
   \[
   \operatorname{Refold}\neq\operatorname{Erase}.
   \]
6. Higher-HS alternation convention:
   \[
   \mathrm{HS}(2m)=(K_m,R_m),\quad
   \mathrm{HS}(2m+1)=(K_m^-,K_m^+,R_m,\sigma_m).
   \]
7. Lens signatures for split layers.
8. XOR reconstruction lemma.
9. No higher-HS residual explosion criterion.
10. OP1/OP4 register-closure strengthening candidate.
11. r02 proof-obligation register.

## Governing status language

This patch does **not** claim OP1 or OP4 closure. It records a strengthening candidate: higher HS layers need not create visible exponential geometry if their split histories are stored as reversible finite register signatures.

## Relation to r01

r01 introduced the OP1/OP4 joint HC-Dixon reduction and finite Fano/Dixon selector normal form. r02 adds a mechanism explaining how those selectors and higher-HS histories can be treated as reversible register data rather than uncontrolled new geometry.

## Build status

No PDF build was run by standing DEV-PATCH rule. PDF builds are deferred until freeze/release capability.
