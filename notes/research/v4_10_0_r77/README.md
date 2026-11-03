# Layer v4.9.0-r77: high precision, formal integrability at the germ and covariance of the OP5 comparison system

| Record | Content |
|---|---|
| r77.1 | Exploration, high precision (160/70 digits). There are exactly four hidden conditions on 6-jets (Gram gap 1e58). g''_p = 477, 594, 723, 865; the symbol is involutive first at p = 8, with characters 723, 130, 12, 0. |
| r77.2 | **H59 confirmed.** No further hidden conditions on 7- and 8-jets: F_7 = 594, F_8 = 723, positive control F_6 = 477, gaps ≥ 4e56, residuals ≤ 1e-51 (parallel GitHub runners, up to 15.2 GB). The system is formally integrable at the germ. |
| r77.3 | **H60 confirmed.** 6 real polarizations per null direction (p = 6..9), none off the cone: six massless modes. |
| r77.4 | **H61 refuted.** In the naive assignment I₃ ⊗ Spin½ the modes are not invariant under i, γ₅ or helicity; a Majorana reading also fails (exploration). |
| r77.5 | **H62 refuted.** The symbol stabilizer has dimension 50; its spacetime part is only the scaling, and its intersection with so(Q) is 0. The internal algebra (dimension 49) is mostly nilpotent. Addendum: at a fixed background this is structurally expected. |
| r77.6 | **H63 refuted.** F alone has 7 spacetime symmetries, but none in so(Q); with G only the scaling remains. Ψ at the germ enters the principal symbol. |
| r77.7 | **H64 confirmed** (run 2, not blind; run 1 invalid). At symbol level R is GL(4) coordinate covariant and internally Lorentz covariant (residuals ≤ 4e-10; negative control 0.26). The breaking comes from the background. |

Folders:
- `rounds/v490_r77_round.tex`: the layer;
- `llm/`: the scripts k153b–k164, the logs and the exploration note;
- pre-registration and result notes: H59–H64 in `../predictions/`;
- the computation job for parallel runners: `ci/hp/` with `.github/workflows/hp-faser.yml`.

OP5 is not closed, and the guards are unchanged.
