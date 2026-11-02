# Design review: joint second/third-jet repair at fixed first jets

30 October 2026. Bounded independent implementation-design review, not a regional-existence proof.

## Reduction is valid under the declared fixed data

The base variables q=(psi,first jets,position) are fixed. Therefore D=DF(q), DD=HessF(q), and the third-jet coefficient matrix A are fixed while the symmetric second jets H vary. The coordinate tangents v_mu(H) depend linearly on H. Consequently the second-prolongation source b(H)=DD[v_mu(H),v_nu(H)]+D_psi H_munu is quadratic in H, whereas the first prolongation D v_mu(H) is linear in H.

For A of shape 240x480, use its complete left-nullspace at an explicit singular cutoff. An economy SVD already gives all 240 columns of U in this wide-matrix case; a full SVD is also valid. If the rank is 215, the gate has 25 rows. Solving the 96 first-prolongation components jointly with U_left^T b(H)=0 is equivalent, up to the stated numerical cutoff, to existence of a third jet satisfying A T+b(H)=0. Recover T using the same SVD and verify the full unprojected second-prolongation residual.

Unlike an optimization that changes first jets, freezing A and U_left here is correct because H is not an argument of the first-order field equation. If first jets were released, that simplification would cease to be valid.

## Required checks

- The original successful F=0 and time-coframe fixing must remain unchanged because psi and first jets are fixed.
- Preserve first prolongation while changing H. Solving only the 25 higher gates would be insufficient.
- Recompute full dF and ddF after recovering T, without accepting projected loss alone.
- Report the rank gap and repeat A elimination at cutoffs 1e-8,1e-9,1e-11. A small source projection near a singular cutoff is not a symbolic rank certificate.
- Record H change, H norm, T norm and changes to any movement penalty. An enormous minimum-norm T can indicate ill-conditioning even if finite residuals are small.
- Independently evaluate d²g from original symbolic background h and derivatives plus saved H, and independently finite-difference the original F on a common cubic Taylor spinor.

The same coframe and its sampled regularity remain fixed because they depend on psi and first jets. This does not establish regularity over a neighborhood. Separate pointwise cubic Taylor witnesses need not be one shared regional solution. Fourth jets and propagation remain untested.

## Initial verdict

The elimination and joint-variable design are mathematically appropriate for finite third-jet feasibility under the fixed model. Await actual saved H/T and independent checks before claiming numerical success.

## Actual implementation review and independent computations

Reviewed third_joint_fit.py and its completed three-point result. The complete left-space reduction is correct for the wide 240x480 matrix. D and DD remain fixed while H varies; tangents and the nonlinear source are rebuilt. All 96 lower first-prolongation components are retained jointly with the 25 projected higher-source conditions. The recovered third jets are checked against the full 240-row system at three singular cutoffs. No indexing or mathematical-design bug was found.

Two reviewer scripts were executed without rerunning optimization:

- third_joint_gate_review.py evaluates g,dg,ddg using the original symbolic h and direct bilinear contractions of saved psi,J,H. Results are saved in third-joint-gate-review-result.json.
- third_joint_direct_review.py independently implements derivative product rules for covariant jets, coframe, inverse coframe and F, using original symbolic background derivatives. It does not import Torch or the optimizer's field evaluator. Results are in third-joint-direct-review-result.json.

| point | norm dF, independent | norm ddF, independent | norm ddg | norm H | norm T |
|---|---:|---:|---:|---:|---:|
| 0 | 1.2322e-11 | 8.4581e-12 | 2.6480e-11 | 20.8800 | 80.0665 |
| 1 | 1.4086e-11 | 8.6179e-12 | 3.0740e-11 | 21.4593 | 79.6893 |
| 2 | 1.1523e-11 | 8.4441e-12 | 2.4572e-11 | 20.5714 | 79.7116 |

g remains about 1e-15 and dg norms are 3.29e-14,2.62e-15,3.47e-15 because psi and first jets are unchanged. The former scalar-Hessian obstruction of norm about 40 is now removed to roughly 3e-11.

At this numerical floor one must not use raw ||ddg||/||ell|| as a strict ddF lower bound: the differentiated identity is

ddg_munu = ell ddF_munu + (d_mu ell)d_nu F + (d_nu ell)d_mu F + (dd_munu ell)F.

The nonzero lower residual dF~1e-11 contributes at this scale. The independent product-rule computation verifies the complete identity with errors 7.67e-14,6.62e-14,5.49e-14. Raw lower-bound ratios and attributed fractions were consequently removed from the joint-repair artifact; the earlier frozen-data attribution remains valid at its much larger residual scale.

H changed materially from norm about 7 to about 21, and recovered T has norm about 80. These are finite, stable-across-points values in the declared packed Euclidean coordinates, not evidence for a physical scale or a uniform derivative bound. The fit did not keep the old Hessians; releasing them is exactly the authorized change.

## Updated verdict

The observed three-point numerical finite third-jet feasibility is corroborated by an independent explicit product-rule implementation. This removes the previous frozen-H obstruction at the tested order. It remains a finite floating-point result under the fixed comparison model: no fourth-jet check, no single regional solution through all points, no constraint-propagation theorem, no native common action and no OP5 closure have been established.
