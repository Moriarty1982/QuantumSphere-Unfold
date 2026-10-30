# The second completed projection and the next one-dimensional obstruction

30 October 2026. Bounded continuation of all_order_criteria_completion.md. Derived conditional finite-jet statements, not an analytic existence or OP5 proof. Here R1 denotes the completed first-order system F=0,G=0,C=dg=0; Rk is its symmetric prolongation to field-jet orderk.

## 1. Original-symbol assumptions retained

Use the complete original Clifford-projector symbol module from all_order_criteria.md, with A rank4, invertible coframe and the null-cone rank3 condition. Original highest-jet ranks are88 at field order2,215 at3,424 at4,735 at5 and1168 at6. The first completed projection proposition additionally assumes completed rank113 at order2 and a smooth analytic R1 chart; under those conditions R2->R1 is locally an analytic affine bundle.

The exact operator lift used throughout is

V^(mu a) partial_mu G_a - q^(mu nu)partial_mu C_nu
= M^nu partial_nu F - q^(mu nu)(partial_mu partial_nu ell)F.

Coefficient derivatives of this identity must be kept off shell. When the corresponding completed lower equations vanish, they disappear in the projection argument below.

## 2. Conditional theorem: R3 -> R2 is surjective

**Hypotheses.** Fix an exact second jet in R2. Assume the original order3 symbol has rank215 with the established complete left module. Assume the completed third-jet matrix has rank271. For an analytic-bundle conclusion assume these ranks are constant in a smooth analytic neighborhood of R2.

**Conclusion.** There is a symmetric third jet making all second derivatives of F,G,C vanish. The completed projection R3->R2 is locally an analytic affine bundle of fibre dimension480-271=209 under the neighborhood hypotheses.

**Proof.** The original order3 compatibility tests are the second derivatives of g and first derivatives of G, up to lower F residual terms. On R2, C=dg=0,dC=d²g=0,G=dG=0,F=dF=0, so those tests vanish. Hence some symmetric reference third jet z0 satisfies d²F(z0)=0.

Let Y2(z)=(d²G(z),d²C(z)). There are40 d²G and40 d²C entries: four components times ten symmetric derivative pairs. At fixed second jet, this is affine in the third jet z. Because C=dg, the d²C tensor must be fully symmetric in three coordinate indices. Its allowed dimension is20 rather than40, yielding20 independent curl constraints.

Differentiate the lifted identity once. At the fixed R2 lower jet all terms containing F,dF,dG,dC vanish. If d²F(z)=0 as well, the remaining four equations are

V^(mu a)(d²G_a)_(lambda mu) - q^(mu nu)(d²C)_(lambda mu nu)=0,

one for each lambda. These four are independent modulo the curl constraints: after an invertible frame change V=I, contraction of a vector-valued symmetric degree2 tensor onto a degree1 tensor is onto. Equivalently divergence maps homogeneous degree2 vector polynomials onto degree1 scalar polynomials. Their nonzero G block is also independent of the curl constraints, which involve C alone.

Thus Y2 belongs to a fixed56-dimensional linear space Z2:80-20-4=56. Let AF3 be the original215-rank third-jet map, and B2 the map from third jets to Y2. The restricted linear map B2|ker(AF3) has rank

rank([AF3;B2])-rank(AF3)=271-215=56.

It is contained in Z2 by the identities just proved, so it fills Z2. Since Y2(z0) belongs to Z2, choose a correction in ker(AF3) sending it to zero. This preserves d²F=0 and kills d²G,d²C. Constant-rank analytic linear algebra supplies local sections and the stated affine fibres. End proof.

This proof is a source-membership argument, not an inference from a numerical tangent gate alone. Approximate jets with small lower residuals give a numerical candidate; they do not replace the exact hypotheses.

## 3. At order4, the same known identities leave exactly one unresolved class

Fix an exact third jet in R3. Original-symbol completeness again supplies a symmetric reference fourth jet z0 with d³F(z0)=0: the needed d³g and d²G vanish on R3. Put Y3=(d³G,d³C), which has80+80=160 entries.

The C part must now be fully symmetric in four indices, dimension35 instead of80, so there are45 independent curl constraints. Differentiating the lifted identity twice leaves ten independent relations indexed by a symmetric coordinate pair. Their G contraction is onto the ten-dimensional space of symmetric degree2 tensors. Thus the known identities restrict Y3 to a105-dimensional space Z3:

160-45-10=105.

However the reported completed order4 rank is528 whereas the original rank is424. Hence, under those exact rank hypotheses, the variation of Y3 along ker(AF4) has dimension only104. The known relations leave one more dimension than can be moved by free fourth jets.

Define the exact obstruction as a quotient class

Omega4(lower third jet) = [Y3(z0)] in Z3 / image(B3|ker(AF4)).

The quotient is one-dimensional. This class is independent of the choice of original reference fourth jet: changing z0 by an element of ker(AF4) adds an image vector. In a regular local chart a nonzero covector lambda annihilating the104-dimensional image represents it as the scalar lambda Y3(z0), up to nonzero scale. The next projection R4->R3 is feasible exactly when this class vanishes.

This identifies the precise missing condition without asserting whether it is an identity or a new constraint. Two possibilities remain:

- Omega4 vanishes identically on a regular R3 chart because of another nonlinear identity;
- Omega4 is a genuine third-jet condition, so R3 must be further restricted before projection is onto.

An existing compatible sixth jet shows Omega4 is numerically small at that germ only. It does not establish either alternative on a neighborhood. A projected derivative of Omega4 along the R3 tangent is a useful discriminating test: a verified nonzero tangent derivative disproves identity there; a zero numerical derivative alone does not prove identity.

## 4. General known-identity allowance and the observed extra family

At field orderp>=2, the extra residuals are Y_(p-1)=(d^(p-1)G,d^(p-1)C). Curl symmetry reduces C to a fully symmetric p-tensor, and derivatives of the lift impose one symmetric(p-2)-tensor of relations. Therefore the space allowed by these known identities has dimension

Z_p =4 C(p+2,3)+C(p+3,3)-C(p+1,3).

Contraction onto the last term is onto: in polynomial notation, divergence of x f divided by(4+degree f) equals f for each homogeneous scalar polynomial f. This proves the independence used in the counts, after the invertible frame transformation.

Parent numerical symbol dimensions give the following comparison:

| field orderp | allowed Z_p | completed rank - original rank | remaining dimension |
|---|---:|---:|---:|
| 2 | 25 | 113-88=25 | 0 |
| 3 | 56 | 271-215=56 | 0 |
| 4 | 105 | 528-424=104 | 1 |
| 5 | 176 | 907-735=172 | 4 |
| 6 | 273 | 1431-1168=263 | 10 |

The sequence1,4,10 matches derivatives of one scalar condition of third-jet order. This is a plausible completion mechanism, not by itself proof that the extra higher conditions are only derivatives of Omega4.

If the prolonged tableau g3 is *exactly* involutive with the reported generic characters(127,62,19,1), the standard tableau prolongation formula gives, forp>=3,

dim g_p =127+62(p-2)+19 C(p-1,2)+C(p,3).

Combining this with the original proved symbol ranks yields an extra dimension C(p-1,3) at everyp>=3. Thus the dimension pattern itself has a conditional all-order explanation once involutivity is exact. It still does not prove generation by one scalar source: different graded modules can have the same Hilbert series. For example S and S/(x) direct-sum S(-1) have the same graded dimensions but different generator behavior.

To upgrade the extra family to derivatives of Omega4, identify the new degree3 left-syzygy class, check its multiplication by coordinate covectors spans the four new degree4 classes and then their prolongations, and establish the corresponding module-generation/saturation statement. At the nonlinear level retain all derivatives of coefficients and lower residuals when lifting these classes.

## 5. Source checking and proof boundary

The linear algebra and tensor-count proofs above are internal derivations. The involutive-tableau prolongation formula is the one verified in Bryant, Notes on Exterior Differential Systems, arXiv1405.3116v1, section2.2, as recorded in all_order_criteria.md. Here it is used conditionally, not as a claim that numerical ranks certify exact involutivity.

The first two completed projection lemmas are stronger than sampled tangent-surjectivity checks under their explicit rank hypotheses. They do not settle the newly isolated one-dimensional fourth-order source condition, exact root existence, analytic neighborhood rank certification, all later projection maps, Taylor convergence, a common regional field or physical OP5 closure.
