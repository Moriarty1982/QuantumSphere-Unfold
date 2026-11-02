# Next Scalar Compatibility Gate on the Regular Cartan Jet

Date: 2026-10-18. Scope: **the explicitly added neutral odd-cross Cartan comparison model only**. This is a bounded necessary compatibility test and a numerical joint finite-jet completion. It is not a native-physics derivation, an open-surface Cauchy solution, a propagation/existence theorem or a physical normalization. No main TeX, PDF, release, authoritative input or shared helper is changed.

Inputs: [regular gravity calculation](HC_Cartan_Regular_Gravity.py), [saved 1200-coordinate jet](HC_Cartan_Regular_Gravity.json), [its derivation](HC_Cartan_Regular_Gravity.md) and the existing [spatial-propagation helper](HC_Cartan_Spatial_Propagation.py). All six regular-gravity/spatial-propagation source, data and note fingerprints are retained in the new JSON. Nothing below overwrites those data.

For source `.py` and `.md` fingerprints, CRLF is normalized to LF so Git's Windows checkout conversion does not invalidate an unchanged source. The saved fingerprints were captured from LF sources and therefore remain unchanged. JSON fingerprints retain the existing raw-byte artifact convention; this narrow source fix is not a claim of cross-platform normalization of every inherited artifact. The fingerprint regression also checks CRLF source bytes explicitly.

## 1. The Exact Off-Shell Identity at Nonzero Multiplier

Write the real probe Euler density, with all variable-density terms included, as

\[
 R=i\mathbb K^\mu D_\mu\Psi-v\mathcal W\Psi
          +\frac{i}{2}Z\Psi,\qquad
 \mathbb K^\mu=v e_a{}^\mu(I\otimes K^a)
                    +\lambda_a{}^\mu(Q\otimes K^a),                 \tag{1}
\]

\[
 Z=\partial_\mu\mathbb K^\mu
       -B_\mu^\dagger\mathbb K^\mu-\mathbb K^\mu B_\mu,
 \quad v=|\det E|,\quad \mathcal W=M\otimes\beta.
\]

Here Q is the specified constant Hermitian internal selector, B is the common neutral Lorentz spin connection, E and lambda are real, and M is Hermitian. There is **no** assumption that Q and M commute. Internal Q acts on the full probe as Q tensor I; the tensor identity is suppressed below. Define

\[
 C[P]^a{}_{\mu}=\operatorname{Im}
       (\Psi^\dagger(P\otimes K^a)D_\mu\Psi),\quad
 F=C[Q]-E,\quad
 b_Q=\operatorname{Re}(\Psi^\dagger Q\mathcal W\Psi).
\]

Since Q commutes with B, each kinetic weight and each weight derivative, Z and QZ are Hermitian. Therefore

\[
 \operatorname{Re}\left(\frac i2\Psi^\dagger QZ\Psi\right)=0.
\]

This is a vanishing **real contraction of a retained term**, not permission to delete Z from the probe equation. In general its imaginary contraction and the operator Z itself are nonzero. Taking the real Q contraction of (1) gives

\[
 \operatorname{Re}(\Psi^\dagger QR)
   =-v e_a{}^\mu C[Q]^a{}_{\mu}
      -\lambda:C[Q^2]-v b_Q.
\]

Using e_a^mu E^a_mu=4 proves the exact off-shell identity

\[
 \boxed{\quad A:=v(4+b_Q)+\lambda:C[Q^2]
     =-\operatorname{Re}(\Psi^\dagger QR)-v e_a{}^\mu F^a{}_{\mu}.
       \quad}                                                       \tag{2}
\]

No Cartan or gravitational equation, coordinate-normality assumption or zero-multiplier specialization is needed for (2). The comparison-model assumptions above are needed; a nonneutral connection failing to commute with Q need not obey it. Twelve deterministic off-shell controls use nonnormal E, nonzero dE, a fully nonzero multiplier and its derivatives, arbitrary spinor jets and an independent Lorentz connection. The largest identity error is about `3.11e-15`. They retain the complete Z term and confirm its real Q contraction vanishes.

Equation A=0 is consequently **not a new independent physical axiom**. It is necessary whenever F=R=0 on a neighborhood.

## 2. The General Normal-Point Hessian

Now specialize only the coordinate/coframe data to the stored normal point E=I and dE=0, keeping **general lambda_0 != 0**. Put T=C[Q^2], and write subscripts r,s for coordinate derivatives. Since v=1, v_r=0 and v_rs=tr(E_rs), ordinary product differentiation gives

\[
 \boxed{\begin{split}
 A_{,rs}={}&\operatorname{tr}(E_{,rs})(4+b_Q)
                   +(b_Q)_{,rs}
       +\lambda_{,rs}:T\\
       &+\lambda_{,r}:T_{,s}+\lambda_{,s}:T_{,r}
       +\lambda:T_{,rs}.
 \end{split}}                                                       \tag{3}
\]

In particular the last term cannot be imported from a calculation setting lambda's value to zero. Nor should the volume term be removed from the general formula merely because the prepared spinor happens to have b_Q=-4 to roundoff.

For clarity let

\[
 \mathcal H_Q=\tfrac12(QM+MQ)\otimes\beta.
\]

The complete real mass Hessian is

\[
 (b_Q)_{,rs}=2\operatorname{Re}
       (\Psi^\dagger\mathcal H_Q\Psi_{,rs}
           +\Psi_{,r}^\dagger\mathcal H_Q\Psi_{,s}).                \tag{4}
\]

With U_mu=D_mu Psi and Q2K^a=Q^2 tensor K^a,

\[
 \begin{split}
 T^a{}_{\mu,rs}=\operatorname{Im}\big(&
   \Psi_{,rs}^\dagger Q2K^a U_\mu
  +\Psi_{,r}^\dagger Q2K^a U_{\mu,s}
  +\Psi_{,s}^\dagger Q2K^a U_{\mu,r}
  +\Psi^\dagger Q2K^a U_{\mu,rs}\big),\\
 U_{\mu,rs}={}&\Psi_{,rs\mu}+B_{\mu,rs}\Psi
        +B_{\mu,r}\Psi_{,s}+B_{\mu,s}\Psi_{,r}+B_\mu\Psi_{,rs}.
 \end{split}                                                       \tag{5}
\]

The second connection derivative in (5) is the full sourced Cartan derivative from the input calculation, including the nonzero-value reaction:

\[
 H k_{,rs}=-s_{,rs}+L_{,rs}^T\lambda
      +L_{,r}^T\lambda_{,s}+L_{,s}^T\lambda_{,r}
      +L^T\lambda_{,rs}-H_{,rs}k.                                \tag{6}
\]

Add the LC connection derivative linear in E3. No torsion/source term is dropped. Equations (3)-(6) apply to arbitrary real multiplier components, not only the temporal-column value of the saved point. Separate off-shell field-difference tests use a fully nonzero multiplier matrix, and an altered spinor value with independently recomputed Cartan coefficients checks the normally cancelling volume term. Those synthetic controls are not new solutions and do not change the completion's inputs. The zero-multiplier specialization is regression-tested against the previous scalar-gate helper.

## 3. Which Jet Order Does This Test Use?

The Hessian uses only Psi up to order 3, E up to order 3 and lambda up to order 2. **It depends on the existing 1200 coordinates** of the regular-gravity calculation:

- Psi2: 240 real coordinates.
- lambda2: 160 real coordinates.
- E3: 320 real coordinates.
- Psi3: 480 real coordinates.

No Psi4, E4 or lambda3 can alter the Hessian of a jet once these coordinates and the lower data are fixed. Algebraic elimination of the Cartan connection does not increase this order: (6) contains only E2, Psi2 and lambda2 in its non-LC part. The new lambda:T_rs term does introduce third jets that were absent from the old lambda=0 formula.

With the lower point fixed, each term in (3)-(6) is **affine** in these 1200 coordinates. Products of free higher coordinates do not occur: the factors paired with them are fixed lower data. This is not an assertion of affinity in the full fields or in the freely variable lower point.

One can also interpret the gate directly by differentiating (2). At F=R=dF=dR=0,

\[
 A_{,rs}=-\operatorname{Re}(\Psi^\dagger Q R_{,rs})
                          -v e_a{}^\mu F^a{}_{\mu,rs}.             \tag{7}
\]

The stored regular-gravity jet already has F2=0, so (3) tests a necessary real Q contraction of the **next** probe equation. It is not the complete R2 system. Potential highest lambda3 contributions in the differentiated Z term have zero real Q contraction; they do not repair a nonzero A2 on fixed existing data.

## 4. The Previously Saved Regular Jet Fails This Gate

Reevaluation of the saved coordinates preserves all 384 prior equations to their reported numerical accuracy. A is about `-3.29e-15`, and dA is below `6e-12` in component magnitude. Nevertheless (3) gives approximately

```text
[[  180.015009,  -429.765852,   116.432314, -1283.011172],
 [ -429.765852,  -129.317040,  -198.341805,  -337.352385],
 [  116.432314,  -198.341805,  -436.975614,  -292.997203],
 [-1283.011172,  -337.352385,  -292.997203,   157.385337]]
```

Its full symmetric tensor norm is **2105.131525**. The previously omitted-on-lambda=0 value term lambda:T_rs has norm about **128.022463** here; it is not negligible. The mass, lambda2 and mixed lambda1/T1 pieces have norms about `1876.20`, `508.37` and `877.60`, respectively. The volume piece is retained but nearly zero for this particular b_Q=-4 preparation.

Independent differences evaluate A on the actual cubic E/Psi and quadratic lambda fields, recomputing the full algebraically eliminated Cartan connection at each displaced point. They do not reuse (3) or its connection-jet formula. Centered Hessian stencils at step .001 give error .45321 and at half that step .11331, showing the expected second-order truncation. Richardson extrapolation at step .0003 agrees with the analytic Hessian to about **3.61e-7** in norm. Smaller steps eventually amplify roundoff; none of these are interval certificates.

This failure says that **this frozen particular higher jet cannot be extended by merely adding still higher derivatives**. It does not invalidate the previously verified finite-order claims, exclude a different allowed higher jet, or establish a model-wide obstruction.

## 5. Joint Bounded Repair, Without Changing the Lower Point

Retain the exact lower data from the input: E=I, dE=0, E2, Psi and Psi1, lambda and lambda1, M, Q, c=1 and u=0. In particular the temporal multiplier column stays `(.01,.02,-.03,.04)`. No original mass, coupling or lower datum is fitted or rescaled in this completion.

Append the ten independent symmetric entries A_rs to **all** 384 existing equations:

\[
 (F_1,\ R_1,\ FE_1,\ F_2,\ A_2)=0,\qquad
 \text{394 real components in 1200 real coordinates}.             \tag{8}
\]

The calculation solves the full affine system by ordinary least squares and then evaluates every unprojected original expression directly. It does not fit only a projected subset or discard a failed residual. An independent random-coordinate control of the affine representation has error about `3.12e-13`.

Observed numerical ranks (relative cutoff 1e-10 for the full operators; absolute cutoff 1e-9 for the ten-row Hessian blocks):

| Quantity | Rank |
| --- | ---: |
| Previous 384-by-1200 operator | 332 |
| Ten Hessian rows alone | 10 |
| Joint 394-by-1200 operator | 342 |
| New independent conditions | 10 |
| Joint coordinate kernel dimension | 858 |

Each individual Psi2, lambda2, E3 and Psi3 column block has rank 10 in the ten Hessian rows. This does not make those four sets of columns jointly independent of one another, nor does it classify physical/gauge modes. The previous 52 derived row identities extend by ten zero columns in equation space and remain valid. These are evaluated ranks, not symbolic constant-rank or neighborhood proofs.

The new joint completion gives:

| Full directly evaluated quantity | Norm |
| --- | ---: |
| All 394 packed components | 7.04e-11 |
| Previous 384 packed components | 6.97e-11 |
| First coframe constraints | 4.50e-12 |
| First probe equations | 5.84e-12 |
| First gravitational equations | 1.82e-11 |
| Second coframe constraints, both mixed entries counted | 7.72e-11 |
| Scalar Hessian, both mixed entries counted | 1.22e-11 |

The maximum absolute packed residual is about `2.50e-11`. A packed norm counts each symmetric pair once; the displayed full symmetric tensor norms count both mixed entries. This explains why the latter can exceed the packed full-system norm.

All 1200 new coordinates, all 394 residuals, the full unchanged lower point and couplings, the coordinate layout, singular values and input fingerprints are saved in [the new JSON](HC_Cartan_Next_Scalar_Compatibility.json). The change from the previous particular higher-coordinate vector has norm about `268.82`: this is a new higher-jet preparation, not a smallness claim. New and old data must not be conflated.

Independent field differences on the completed jet reproduce its near-zero Hessian to about **4.04e-7** with the same Richardson control. The finite-difference error is larger than the analytic residual, as expected. Regression tests also recheck the complete old equations and the nonzero off-origin remainders.

## 6. Limits and Handoff

The lower temporal K0 and T blocks remain unchanged **at the point**, because their data were fixed. Any neighborhood bound using higher Taylor coefficients must be recomputed on the new coordinates; an old radius cannot simply be inherited. The parent task can load `joint_394_system.jet_coordinates` with the existing `HC_Cartan_Regular_Gravity.unpack` helper. `fixed_lower_point_and_couplings` records every lower datum needed for independent inspection.

This result passes ten more necessary scalar compatibility conditions in the additional comparison model. It does **not** solve the complete third coframe constraints, second probe equation or second gravitational equation. The smooth Taylor fields remain off shell away from the point; the full algebraic Cartan equation alone is satisfied along them. Constraint propagation, remaining multiplier/gauge structure, constant-rank control, Cauchy data on an open surface, convergence/existence, native identification and physical units remain open.

## Reproduction

- [Calculation](HC_Cartan_Next_Scalar_Compatibility.py), [full saved data](HC_Cartan_Next_Scalar_Compatibility.json), [34 tests](../scripts/qsc_audit/tests/test_hc_cartan_next_scalar_compatibility.py).
- `python -B analysis/HC_Cartan_Next_Scalar_Compatibility.py --output analysis/HC_Cartan_Next_Scalar_Compatibility.json`
- `python -B -m unittest discover -s scripts/qsc_audit/tests -p test_hc_cartan_next_scalar_compatibility.py`

Executed verification: all **34 new tests** pass. The existing `test_hc_cartan_regular_gravity.py` (42 tests) and `test_hc_cartan_spatial_propagation.py` (38 tests) also pass in a combined **80-test regression run**, for **114 distinct tests** checked in this subtask. The JSON generation command completed successfully. A final fingerprint check confirms all six authoritative input files still match the saved audit. This is not a claim to have rerun the entire repository suite.

Only these four new calculation/data/note/test paths are authored by this subtask. No Git write/commit/push, package installation, main-document/PDF build, release edit, shared-index edit or other-chat message is performed. Read-only Git status/diff inspection does not change the checkout; the script's `git_operations=false` flag records that the calculation itself invokes no Git operation.
