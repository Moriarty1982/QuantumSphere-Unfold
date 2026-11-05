# Referee report

**Manuscript:** "Three frames on one kernel: duality sectors of a complex quaternion and chirality from a compensator in C⊗H⊗O" (draft dated 4 November 2026, 17 pp.)
**Journal type considered:** J. Math. Phys. / Phys. Rev. D

---

## 1. Summary of the submission

The manuscript studies a complex-quaternion "kernel" q = it + z·e in C⊗H. The vector part z ∈ C³ is read as the Riemann–Silberstein vector E + iB, and the complex-bilinear norm qq̄ = −t² + z·z contains the electromagnetic invariant s = E² − B² + 2iE·B. The sign of s (for real s) labels "matter-type" (s > 0), "tachyon-type" (s < 0) and "light-like" (s = 0) kernels. Sections 2–4 prove elementary statements about these sectors:
- SO(3,C)-orbits;
- the orbits of SO(3,C) × U(1)_dual;
- a "triple lemma": centred and null ⇔ z ∝ (1, ω, ω²);
- the spinor parametrisation of the null cone;
- an antilinear involution J_B z = i z̄ with "compensator" projector C = (1 + J_B)/2;
- a Gram/Stokes "state disk" for the real doublet (E, B);
- the commutant of (J_B, C) on that doublet.

Section 5 works on C⊗H⊗O. It uses Furey's number operator, takes the weak SU(2) as right quaternionic multiplication, and introduces C_ch = (1 + iL_{e7})/2. With the hypercharge Y/2 = Q − 1/2 + (1 − C_ch)T₃, this gives the content of one Standard Model generation with ν_R. The paper also claims that, among four admissible projectors, anomaly cancellation selects ±iL_{e7}. Section 6 introduces a single number, β_sym = 0.5494. It is the ratio of two Barbero–Immirzi values from U(1) horizon counting, rewritten as a "frame rapidity". From it the paper obtains Ω_M = β², sin²θ₁₂ = β²/cos²θ₁₃ and cot θ_W = γ_L (so m_W = 80.3615 GeV), plus two θ₂₃ statements, all described as pre-registered. The appendices list withdrawn claims of a longer version (among them a claimed proof of the Riemann hypothesis), describe the method (pre-registration, Lean, LLM use) and give a translation into a private "QAM" notation.

## 2. Overall assessment and recommendation

**Recommendation: reject in the present form** for J. Math. Phys. or Phys. Rev. D. A substantially re-scoped mathematical note might be acceptable later in a pedagogical or mathematical-physics venue (e.g. J. Phys. A, Adv. Appl. Clifford Algebras, Eur. J. Phys. for the electromagnetic part).

The author is unusually candid about limitations. The appendices honestly list earlier errors, and the hedging is often careful. I could confirm most stated propositions (Section 5 below). These are real strengths. Even so, the recommendation follows from three findings:

1. **Sections 2–4 are correct but not new.** The material is textbook electromagnetism and linear algebra: the complex invariant of the Riemann–Silberstein vector, SO(3,C) ≅ SO⁺(1,3), the classification into null and non-null fields, the existence of a frame with E ∥ B, duality rotations, and the spinor map onto the null cone (Cartan, Penrose). Repackaging it in biquaternion language does not add new mathematics. The physical vocabulary ("matter", "tachyon", "compensator", "three frames") goes beyond what the mathematics supports. In particular, nothing tachyonic appears anywhere.

2. **Section 5 only loosely connects to Sections 2–4, and its claimed novelty is weak.** The link is that both projectors have "the same form" (1 + J)/2. But every projector P has this form, with J = 2P − 1, and J_B is antilinear while iL_{e7} is linear. The decomposition obtained is the standard Pati–Salam/SO(10) decomposition of one generation, 16 = (4,2,1) ⊕ (4̄,1,2), with Y/2 = (B − L)/2 + T₃R. The projector (1 + iL_{e7})/2 is the Günaydin–Gürsey split-octonion projector onto 1 ⊕ 3. That chirality is put in by restricting SU(2) with a projector is likewise known from Furey's ideal constructions. The "anomaly selection" among four discrete options is correct up to a numerical error I found (Major issue 5), but it is a small step beyond the known fact that anomaly cancellation fixes hypercharges once the multiplet structure is given. Moreover C_ch does not act on Lorentz chirality at all: all 32 states carry the same Weyl representation, which I checked explicitly.

3. **Section 6 is numerology without a mechanism.** The one input combines two determinations of the same Barbero–Immirzi parameter. One of them (ln 2/(π√3), the 1998 ABCK value) is a counting the community regards as superseded, and the other is the U(1) value disfavoured relative to the SU(2) treatment, as the author concedes. The identifications Ω_M = β², sin²θ₁₂ cos²θ₁₃ = β² and cot θ_W = γ_L have no derivation. The on-shell scheme for θ_W is chosen ad hoc; in MS-bar the relation fails at the 2% level. And the "predictions" were registered when the relevant data were already known to agree: m_W(PDG 2026) = 80.3625 ± 0.0077 GeV vs 80.3615 predicted, and JUNO 2025 gives 0.3092 ± 0.0087 vs 0.3087. The proposed tests therefore cannot tell the proposal apart from the Standard Model or from ordinary global fits.

The Lean formalisation and the pre-registration practice are commendable but do not make up for missing physical content. Appendix C (QAM notation) and much of Appendix A (Riemann hypothesis history) are not suitable for a research journal.

## 3. Major issues

**M1. Physical interpretation of the sectors (Sections 1, 3.1, Prop. 3.2; Abstract).**
- Fields with s < 0 are ordinary magnetic-dominated fields. Examples are a static magnetic field and the near field of any magnetic dipole, including the electron's own moment. Nothing about them is tachyonic: no space-like momentum and no superluminal propagation.
- Definition 3.1 only classifies real s, while generic fields have E·B ≠ 0.
- Prop. 3.2 shows the matter/tachyon label is not invariant under the group the paper itself uses. Any z with s ≠ 0 can be written as e^{iα}z_m with s(z_m) > 0, but equally as e^{i(α+π/2)}z_t with s(z_t) < 0. So the "three sectors" are really two orbits (s ≠ 0 and s = 0), and the matter–tachyon split needs a preferred duality frame. Free Maxwell theory has no such frame, and with charged matter only one duality frame is physical (the one with no magnetic charges).
- *Suggestion:* replace "matter/tachyon" by "electric-/magnetic-dominated" (or "s > 0 / s < 0"), state the two-orbit structure plainly, and remove claims that the kernel describes matter and tachyons.

**M2. The compensator does not do what the abstract says (Sections 3.2–3.3; Abstract, item 2 of the main results; Conclusions).**
- From Definition 3.3, Cf = ½(E + B)(1 + i) for every f, so the image of C is the real 3-plane {E = B}. Every compensated field sits at the single boundary point b = (0, +1) of the state disk, and every Af at b = (0, −1). Both are on the axis orthogonal to the matter–tachyon axis, i.e. Re s = 0.
- The state disk itself (ρ = G/tr G) is defined independently of C and is the standard Stokes-type parametrisation of (Re s, Im s)/(E² + B²). The abstract's "a projector built from the duality involution places matter and tachyon on opposite sides of a state disk" is therefore inaccurate: the projector places nothing, and its ports are neither matter nor tachyon.
- J_B is E ↔ B without a sign, i.e. a duality quarter-turn composed with time reversal. It maps Maxwell solutions to solutions of the time-reversed equations, so Cf is in general not a solution at all. The "two-arm interferometer" and "dyon" readings need this caveat.
- *Suggestion:* state these facts explicitly and rewrite the abstract and conclusions accordingly.

**M3. Section 4 is trivial and does not support the "compensator matrix" programme.**
- Prop. 4.2 is a two-line linear-algebra fact. The hypothesis ker(M − λ₀) ∩ ker C = {0} is essentially the conclusion, and self-adjointness is not used.
- Prop. 4.3 is the commutant of σ_x in M₂(R). Its statement is also incomplete: the determinant-one solutions are ±e^{θσ_x}, not only e^{θσ_x}.
- The "16 × 16 compensator matrix" of the longer version is mentioned "without interpretation". A journal paper should not carry this.
- *Suggestion:* compress Section 4 to a remark or delete it.

**M4. The bridge between Sections 2–4 and Section 5 is notational (Section 5.4, §5.7 item (ii)).**
- "A projector of the same form (1 + J)/2" says nothing, since every projector has that form.
- J_B is antilinear on C³ (vector representation); J = iL_{e7} is complex-linear on C⊗O.
- The Lorentz group acts on the kernel by conjugation (vector), but on the fermion carrier by left multiplication (spinor).
- Nothing in Sections 2–4 enters the proofs of Section 5.
- *Suggestion:* either derive C_ch from the kernel structure (for instance by exhibiting a map from the kernel or J_B to iL_{e7}), or present Section 5 as a separate algebraic observation and drop "three frames on one kernel" as its motivation.

**M5. Prop. 5.4(c) contains a numerical error and understates the failure of the alternatives.**
- I recomputed everything with explicit matrices on C³² (convention in Section 5 below).
- For J = ±iR_{e7} at σ = −1/2, I obtain, per Weyl field (dividing the 32-dimensional trace by the two Lorentz components):
  - Tr Y³ = ±12, equivalently Tr(Y/2)³ = ±3/2;
  - Tr(T₃′² Y) = ∓1, so the SU(2)²U(1) anomaly also fails;
  - Tr Y = 0 and Tr(T_c² Y) = 0.
- I cannot reproduce "Tr Y³ = ±2/3" in any normalisation I tried (Y or Y/2; per Weyl field or over all 32 components).
- *Suggestion:* correct the value, state the normalisation, give all four anomaly coefficients for all four projectors in a table, and include the SU(3)³ check (which vanishes for ±iL_{e7}).

**M6. The novelty of the "anomaly selection" (§5.5, §5.7) is overstated.**
- (a) Prop. 5.4(b) is trivially independent of the projector: Tr T₃ = 0 on every sector and Tr Q = 16, so Tr Y/2 = 16 + 32σ for all four choices.
- (b) The four options are: image = {Q=0, Q=2/3} (= 1⊕3, the Pati–Salam 4 in the Günaydin–Gürsey split basis), its conjugate {1, 1/3} (= 4̄), and the two "mixed" choices {0, 1/3} and {2/3, 1}, which break the lepton-as-fourth-colour structure. That the mixed choices are anomalous is the familiar fact that, once the SU(2) and SU(3) multiplets are fixed, anomaly cancellation fixes the relative hypercharges and relative chirality of quarks and leptons (Geng–Marshak; Minahan–Ramond–Warner).
- (c) Y/2 = Q − 1/2 + (1 − C)T₃ is exactly the Pati–Salam formula Y/2 = (B − L)/2 + T₃R, with Q − 1/2 = (B − L)/2 here. The generation content therefore follows from the definitions, i.e. from the (assumed) Pati–Salam/SO(10) structure.
- *Suggestion:* compare explicitly with Baez–Huerta (Pati–Salam), Krasnov (SM group as the subgroup of Spin(9)/Spin(10) commuting with a complex structure from one imaginary octonion), Furey (ideals and projectors separating SU(2)_L), Furey–Hughes 2022 (one generation of Weyl representations in a single copy of R⊗C⊗H⊗O), Todorov / Dubois-Violette (B − L projector, superselection of hypercharge) and Gresnigt. Then state precisely what, if anything, is new.

**M7. "Chirality" is a misnomer (Prop. 5.3).** C_ch commutes with the Lorentz group, and all 32 states transform as the same Weyl type: I verified J_n + iK_n = 0 on the whole space. C_ch therefore separates SU(2)_L doublets from the conjugates of right-handed fields, i.e. it selects where SU(2)′ acts. Spacetime chirality enters only through the standard convention of writing all fields as left-handed. The claim that "the frame change T exchanges image and kernel, so matter frame and tachyon frame are particle and antiparticle with mirrored chirality" relies on T, which is antilinear complex conjugation. It is not the duality quarter-turn of Section 3. *Suggestion:* rename, and justify or drop the identification of T with the matter→tachyon frame change.

**M8. The input β_sym and the "counting reading" (Sections 6.1–6.2).**
- (a) γ_T = ln 2/(π√3) is the 1998 ABCK estimate, which Domagała–Lewandowski showed to undercount. γ_M = 0.2375 is the DL/Meissner U(1) value. Both are determinations of the same parameter of the theory, so their ratio as a physical "Lorentz factor between frames" is not motivated.
- (b) Prop. 6.1 is correct, but "count only states that saturate the uncertainty bound" yields m = ±j at every j, which reproduces only the g = 2 (Meissner) rule. The "minimal" rule (only j = 1/2) needs a different criterion ("all states of the multiplet saturate"). So the statement "a single principle produces both rules" is not established.
- (c) Even as an effective description, the DL equation counts m-sequences with a projection constraint. Ghosh–Mitra show that the equation coincides with counting |m| = j only effectively.
- *Suggestion:* either give a derivation in which two frames use two countings, or present β_sym as a free parameter.

**M9. Phenomenology (Sections 6.3–6.6).**
- (a) **Scheme dependence.** cot θ_W = γ_L is not RG- or scheme-invariant. In the on-shell scheme it matches at 0.1%, while MS-bar(m_Z) gives cot θ_W = 1.823 vs γ_L = 1.865, a 2% mismatch. Since the on-shell scheme was chosen once the agreement was known, the quoted precision (±0.0018 GeV) is meaningless. A tree-level relation between a horizon-counting ratio and a renormalised electroweak parameter needs a reason for the scale and scheme.
- (b) **Severity of the tests.** At registration (20–21 Oct 2026) the JUNO first result (0.3092 ± 0.0087) and the PDG 2026 world average for m_W (80.3625 ± 0.0077 GeV) were already public, and both agree with the "predictions" well within 1σ. The refutation criteria (|pull| ≥ 3) will also be met by the SM electroweak fit (80.357 ± 0.006 GeV) and by generic θ₁₂ fits. So the tests are not discriminating, and "registered before the relevant data" overstates their value.
- (c) **Look-elsewhere.** The author reports 58 registered tests and several candidate structural numbers (β, β², γ_L, η, 1/√3, …). A look-elsewhere estimate is needed before 0.1–1% coincidences can carry weight.
- (d) **The θ₂₃ model (Section 6.5) cannot be reproduced.** W, the A₄ assignments, the fit procedure and the data windows are not given, and the two θ₂₃ "predictions" are nested (the second implies the first).
- (e) **Ω_M = β² is put in after the fact.** It is explicitly post hoc and epoch-dependent. It should not appear in the abstract-level summary of results.
- (f) **Koide (Section 6.4).** The circulant parametrisation √m_k = a + 2|b|cos(θ + 2πk/3) with |b| = a/√2 is due to Foot and Brannen and should be cited. The framework adds nothing to it.
- *Suggestion:* either remove Section 6 or reduce it to a clearly labelled speculative remark.

**M10. Scope and presentation.**
- Sections 7.2–7.3 announce unpublished results (an involutive symbol at order six, 14 functions of three variables, hidden conditions) that cannot be checked from the paper.
- Appendix C introduces a private notation (QAM) that the main text does not use.
- Appendix A discusses withdrawn claims of a separate manuscript, including a claimed proof of the Riemann hypothesis.
- None of these belongs in a journal article. A footnote referring to an erratum or changelog in the repository is enough. The disclosure of LLM use (Appendix B) is appropriate and should stay, in the form the journal requires.

## 4. Minor issues

1. **Abstract and §2.3:** "symmetric triple of *kernels* at 120°". The lemma concerns the three components of one vector z, not three kernels. Also, the centring condition z₁ + z₂ + z₃ = 0 is not SO(3,C)-invariant (it singles out the direction (1,1,1)). So "the symmetric triple … has an invariant meaning" holds only for the null condition, not for the centring.
2. **§2.2:** "on the null set N(q) = 0 … t² = s". The light-like sector is defined by s = 0, not N(q) = 0 (with t real these coincide only if t = 0). Please distinguish the two null conditions. The parameter t plays no role anywhere in Sections 2–4 and could be dropped.
3. **Prop. 2.2:** the remark that the Hermitian form has "signature (1,6)" should state the sign convention. A sentence noting that qq̄ = det under C⊗H ≅ M₂(C) would shorten the proof.
4. **Prop. 2.3:** "every element of SO(3,C) arises" is fine. Note that SO(3,C) ≅ PSL(2,C) is a group isomorphism, but the identification of z with E + iB as a Lorentz representation (the (1,0) representation) should be said explicitly.
5. **§2.4:** "single spinors are light-like and pairs massive". Pairs of proportional spinors give null vectors. The identifications HP¹ ↔ Dirac spinors and OP¹ ↔ three generations are unsupported and should be marked as speculation.
6. **Prop. 3.2 / abstract:** {0} is also a duality-invariant orbit. Say "the unique non-trivial…".
7. **Prop. 3.6:** "boosting any field moves it towards light" is false in general. |b| = |s|/(E² + B²) first increases towards 1 when one boosts towards the frame with E ∥ B, and only then decreases. My numerical example is non-monotone. Only the asymptotic statement holds.
8. **Prop. 3.4:** "With respect to the real inner product Re⟨Cf, Af⟩ = 0" reads badly. Suggest "C and A are orthogonal with respect to the real inner product Re⟨·,·⟩."
9. **§3.2:** state that J_B = (duality quarter-turn) ∘ (time reversal), which bears on whether the plane-wave and Coulomb examples are solutions.
10. **Prop. 4.3:** missing −e^{θσ_x} (see M3). "A boost … is not of the form F ↦ LFM" needs one line of proof: a boost acts as F ↦ AF + BFε with ε = iσ_y.
11. **§5.1:** give the full multiplication table (or the Cayley–Dickson formula). Three products do not fix the convention. I used (a,b)(c,d) = (ac − d̄b, da + bc̄), e_{4+m} = (0, e_m), which reproduces the stated products.
12. **§5.2:** write α_a = ½(L_{e_a} + i L_{(e₇e_a)}) with explicit parentheses. The alternative reading ½(L_{e_a} + i L_{e₇}L_{e_a}) gives different operators, and I checked that it does not reproduce the stated algebra.
13. **§5.2 remark:** "P_± translate between O with the inner unit … and C⊗O with the outer unit" is unclear. Please make it a precise statement or delete it.
14. **Prop. 5.2:** the table row "1/3 (conj. triplet) … (d̄, ū)" uses a different particle reading from the sentence "in her reading the sectors are ν, d̄, u, e⁺" just above. Please harmonise.
15. **Prop. 5.3:** "sixteen Weyl states with two Lorentz components each" while C_ch has rank 16. Clarify that the image holds 8 Weyl fields (16 complex components) and the total space holds 16 Weyl fields (32 components).
16. **Prop. 5.5:** the statement that triality "excludes a fourth inequivalent eight-dimensional representation" is true but irrelevant to generations. The slot shift commutes with colour, Q, Lorentz and weak SU(2) trivially, because these act diagonally, so any S₃ on three identical copies would do the same. Cite Furey 2018 (three generations from C⊗O), Gillard–Gresnigt 2019, Dubois-Violette–Todorov and Boyle.
17. **§6.1:** the populations "(2/3, 1/3)" vs "(3/4, 1/4)" for the matter frame are never defined. The equivalence "γ_L = 1/β_sym, i.e. cosh 2η = e^η" is true but not obvious. Both reduce to the tribonacci cubic x³ = x² + x + 1 with x = e^η (I checked: if x³ = x² + x + 1 then y = x² satisfies y³ − 3y² − y − 1 = 0, the coth equation). Please add a line.
18. **Eq. (9):** state that g(j) = 2 at all spins is the DL/Meissner equation and that only j = 1/2 reproduces ABCK. Cite Agullo et al. (exact counting) for the status of both values.
19. **Ref. [12] (Boyle):** I could find only the arXiv version (2006.16265). Please check the journal reference "J. Math. Phys. 67 (2026) 071701".
20. **Ref. [21]:** the JUNO first result is quoted as Nature 654 (2026). Please check this; I found only the arXiv preprint. Give the measured value (0.3092 ± 0.0087) in the text when computing the "3.6σ".
21. **Table in §6.6:** quote the current experimental values next to each prediction (m_W, PDG 2026: 80.3625 ± 0.0077 GeV; sin²θ₁₂, JUNO: 0.3092 ± 0.0087) so the reader can see that the agreement predates registration.
22. **Style:** the text contains many self-referential process remarks ("was seen analytically before the computation", "noticed during other computations", "cross-checked between language models"). These are better placed in a data/methods statement.

## 5. Verification log

All scripts are in /tmp/claude-0/referee/ (octo.py, gen.py, misc.py, gg.py).

**Octonion convention used.** Cayley–Dickson on quaternion pairs: (a,b)(c,d) = (ac − d̄b, da + bc̄), with e₁, e₂, e₃ = i, j, k and e_{4+m} = (0, e_m). This reproduces e₇e₄ = −e₃, e₇e₅ = −e₂ and e₇e₆ = e₁, and I checked the composition property and alternativity numerically. C⊗H⊗O is realised as C⁴ ⊗ C⁸ = C³², with the outer i as the complex scalar.

| # | Statement | Method | Result |
|---|---|---|---|
| 1 | Prop. 2.2: qq̄ = −t² + s, multiplicative | sympy, C⊗H ≅ M₂(C); qq̄ = det q·1 | Confirmed |
| 2 | Signature (1,6) of the Hermitian form | by inspection | Confirmed (convention-dependent) |
| 3 | Prop. 2.3: conjugation by SL(2,C) gives SO(3,C), t fixed | standard; checked | Confirmed |
| 4 | Prop. 2.4: SO(3,C) orbits | Witt's theorem | Confirmed |
| 5 | Lemma 2.5 (triple lemma) | elementary symmetric functions; sympy | Confirmed. Centring is not Lorentz-invariant (Minor 1) |
| 6 | Prop. 2.6: s(z(ψ)) = 0, preimages ±ψ, inverse formulas, equivariance | sympy; solved for R(g) with z(gψ) = R z(ψ) for generic g ∈ SL(2,C): RᵀR = 1, det R = 1 | Confirmed |
| 7 | §2.4: k(ψ) null; future time-like = sum of two nulls | standard | Confirmed (pairs can be null if parallel) |
| 8 | Prop. 3.2: duality angle, orbits of SO(3,C) × U(1) | by hand | Confirmed. Interpretation issue (M1) |
| 9 | Prop. 3.4: J_B² = 1; C, A projections; Re⟨Cf,Af⟩ = 0; A(f) = −iC(if) | by hand + 200 random numerical tests | Confirmed. Additionally im C = {E = B}, im A = {E = −B} (M2) |
| 10 | Coulomb/dyon and plane-wave examples | by hand | Algebra confirmed. J_B f is not a Maxwell solution (time-reversed) |
| 11 | Prop. 3.5: σ_x, σ_z, R_αᵀ; Gram decomposition (5); det G = abs(E×B)² | numerical | Confirmed |
| 12 | Prop. 3.6: abs(b) ≤ 1 via u² − det G = abs(s)²/4; rotation by 2α; J_B reflects b₁ | by hand + numerical | Confirmed. "Boosting moves any field towards light" is false in general (non-monotone \|b\| along a boost family) |
| 13 | Prop. 4.2 | by hand | Confirmed (trivial; self-adjointness unused) |
| 14 | Prop. 4.3 | by hand | Confirmed except "det-one members are e^{θσ_x}": −e^{θσ_x} is missing. Preservation of Re s confirmed |
| 15 | Prop. 5.1: α_a² = 0, {α_a, α_b†} = δ_ab, {α_a, α_b} = 0 | explicit 8×8 matrices | Confirmed with α_a = ½(L_{e_a} + i L_{(e₇e_a)}); fails with the composition reading |
| 16 | Spectrum of N | same | 0, 1, 2, 3 with multiplicities 1, 3, 3, 1. Confirmed |
| 17 | Q = ½ − (i/6)L_{e₇} − (i/3)R_{e₇}; TQT⁻¹ = 1 − Q | same | Confirmed |
| 18 | Colour SU(3) = Stab_{G₂}(e₇); commutes with Q | computed Der(O): dim 14; stabiliser of e₇: dim 8 | Confirmed |
| 19 | Q = 1/3 and Q = 2/3 sectors are mutually conjugate triplets | weights opposite | Confirmed |
| 20 | Q = 0 sector spanned by 1 + ie₇, Q = 1 by 1 − ie₇ | same | Confirmed |
| 21 | Prop. 5.2: [T_a, T_b] = iε_abc T_c, Casimir 3/4; weak SU(2) commutes with Lorentz, colour, Q; table of Y/2, Q_em; TQ_emT⁻¹ = −Q_em | C³² matrices | Confirmed |
| 22 | Prop. 5.3: J² = 1, Hermitian, rank 16, commutes with colour, Lorentz, right H, Q; image = Q ∈ {0, 2/3} | same | Confirmed |
| 23 | Decomposition (3,2)₁/₆ ⊕ (1,2)₋₁/₂ ⊕ (3̄,1)₋₂/₃ ⊕ (3̄,1)₁/₃ ⊕ (1,1)₁ ⊕ (1,1)₀; Q_em = T₃′ + Y/2 | joint eigenvalues of (Q, C, T₃, Y/2, Q_em) | Confirmed |
| 24 | Anomalies for C_ch: Tr Y, Tr Y³, SU(2)²U(1), SU(3)²U(1) = 0 | exact rationals | Confirmed. SU(3)³ also vanishes |
| 25 | T C_ch T⁻¹ = 1 − C_ch | same | Confirmed |
| 26 | All 32 states carry one Weyl type | J_n + iK_n = 0 identically | Confirmed (M7) |
| 27 | Image of C_ch contains the Günaydin–Gürsey idempotent ½(1 + ie₇) | same | Confirmed (projector onto 1⊕3) |
| 28 | Prop. 5.4(a): commutant of colour + Q on C⊗O, hence four projectors | dim_C = 4 | Confirmed |
| 29 | Prop. 5.4(b): Tr Y = 0 iff σ = −1/2 | Tr Y/2 = 16 + 32σ for every projector | Confirmed (trivially projector-independent) |
| 30 | Prop. 5.4(c), J = ±iL_{e₇} | per Weyl field | All anomalies vanish. Confirmed |
| 31 | Prop. 5.4(c), J = ±iR_{e₇} | per Weyl field | Tr Y³ = ±12 (Tr(Y/2)³ = ±3/2) and SU(2)²U(1) = ∓1. **Error: the stated ±2/3 is not reproduced** |
| 32 | Prop. 5.4(d) | trivial | Confirmed |
| 33 | Prop. 5.5: t cyclic; dim g = 28; diagonal (A,A,A) solutions of dim 14 (= g₂) | numerical null spaces | Confirmed. Inequivalence of the slot representations not checked numerically (classical) |
| 34 | Eq. (8): γ_T, γ_M | γ_T = ln 2/(π√3) = 0.127384; eq. (9) with g = 2 gives γ_M = 0.23753296 | Confirmed |
| 35 | γ for g = 2j + 1 | eq. (9) | 0.274067 (β = 0.6045). Confirmed |
| 36 | γ_L, β_sym, η | from (7)–(8) | 1.86470, 0.549406, 0.6175 = artanh β, cosh 2η = γ_L. Confirmed |
| 37 | Eq. (10): Ω_M | β² = (γ_M − γ_T)/(γ_M + γ_T) | 0.3018. Confirmed |
| 38 | sin²θ₁₂ = β²/cos²θ₁₃ with sin²θ₁₃ = 0.02215 | direct | 0.30868 (0.3087); with rounded γ_M = 0.2375: 0.30862 (0.3086). Confirmed |
| 39 | TM2 value 1/(3cos²θ₁₃) | direct | 0.3409. Confirmed. (0.3409 − 0.3092)/0.0087 = 3.6σ vs JUNO. Confirmed |
| 40 | m_W = m_Z γ_L/√(1 + γ_L²), m_Z = 91.1880 GeV | direct | 80.3615 GeV; δm_Z = 0.0021 gives ±0.0019 GeV. Confirmed. Implied on-shell sin²θ_W = 0.22336 |
| 41 | Comparison values for cot θ_W | direct | 1.8655 (PDG 2024 m_W = 80.3692), 1.8234 (MS-bar 0.23122), 1.8218 (sin²θ_eff) vs γ_L = 1.8647 (M9a) |
| 42 | Lepton window: tanh(0.611) and tanh(0.647) | direct | 0.5448, 0.5696. Consistent with the stated [0.545, 0.570] |
| 43 | Excluded alternative values | direct | artanh(1/√3) = 0.658 outside; γ_L = 1/β gives η = 0.6094, β = 0.5437, just outside. Confirmed |
| 44 | Equivalence "γ_L = 1/β, i.e. cosh 2η = e^η" | algebra | Both reduce to the tribonacci cubic. Confirmed |
| 45 | Prop. 6.1 | sympy: excess = (j − m)(j + m + 1)/2 | Confirmed |
| 46 | Koide ratio | PDG masses | K = 0.6666645 (K − 2/3 = −2.2 × 10⁻⁶). Confirmed ("about 10⁻⁵") |
| 47 | Circulant parametrisation and \|b\| = a/√2 | sympy: ratio = (a² + 2b²)/(3a²) | Confirmed |
| 48 | Literature values: DESI DR2 Ω_M = 0.2975 ± 0.0086; Planck Ω_M = 0.3153 ± 0.0073; NuFIT 6.0 sin²θ₂₃ = 0.561 / 0.470 | memory, not re-fetched | Consistent with my knowledge |
| 49 | JUNO 0.3092 ± 0.0087 | arXiv:2511.14593 | Confirmed |
| 50 | PDG 2026 m_W average 80.3625 ± 0.0077 GeV; SM fit 80.357 ± 0.006 GeV | PDG 2026 W-mass review | Confirmed |
| 51 | DL/Meissner eq. (9) coincides with counting \|m\| = j | Ghosh–Mitra (gr-qc/0411035) | Confirmed (effective statement only) |
| 52 | Section 6.5 (A₄ model, W, θ₂₃ ∈ [0.491, 0.498]); pre-registration dates; Lean formalisation; Section 7.3 PDE results | — | **Could not check**: insufficient information in the manuscript, and the instructions excluded the repository |

## 6. Novelty check

**Electromagnetic and kernel part (Sections 2–4).** Known material:
- Biquaternionic and Riemann–Silberstein formulations of electromagnetism: Conway (1911), Silberstein (1912), Lanczos; reviewed by Bialynicki-Birula [3] and Bialynicki-Birula & Bialynicka-Birula, J. Phys. A 46 (2013) 053001.
- The complex invariant F² + iFF̃, the classification into null and non-null fields, the frame with E ∥ B, and SO(3,C) ≅ SO⁺(1,3): Landau–Lifshitz Vol. 2 §25; Synge, *Relativity: the special theory*; Penrose–Rindler, *Spinors and Space-time* Vol. 1.
- Duality rotations: Deser–Teitelboim (1976).
- The spinor parametrisation of isotropic vectors: É. Cartan, *Leçons sur la théorie des spineurs* (1938).
- The Stokes-like Gram picture is a direct restatement of (Re s, Im s)/(E² + B²).

I found no new result here.

**C⊗H⊗O part (Section 5).**
- Günaydin & Gürsey, J. Math. Phys. 14 (1973) 1651: split basis u₀ = ½(1 + ie₇), giving 8 = 1 ⊕ 3 ⊕ 1 ⊕ 3̄ under SU(3) ⊂ G₂. The projector (1 + iL_{e₇})/2 is the projector onto 1 ⊕ 3.
- Dixon (1994) and later papers.
- C. Furey, Phys. Rev. D 86 (2012) 025024 (ideals; projectors separating Weyl spinors and SU(2)_L in C⊗H); Phys. Lett. B 742 (2015) 195; Phys. Lett. B 785 (2018) 84 (three generations); Eur. Phys. J. C 78 (2018) 375.
- C. Furey & M. J. Hughes, "One generation of standard model Weyl representations as a single copy of R⊗C⊗H⊗O", Phys. Lett. B 827 (2022) 136959, arXiv:2209.13016. This is the closest prior work: one generation including ν_R, Weyl representations, and complex conjugation as the distinguishing involution. The present paper must compare with it.
- C. Furey & M. J. Hughes, "Division algebraic symmetry breaking", Phys. Lett. B 831 (2022) 137186.
- K. Krasnov, "SO(9) characterisation of the Standard Model gauge group", J. Math. Phys. 62 (2021) 021703, arXiv:1912.11282: G_SM as the subgroup commuting with a complex structure fixed by one unit imaginary octonion. This is closely related to the role of iL_{e₇} here.
- J. Baez & J. Huerta, "The algebra of grand unified theories", Bull. AMS 47 (2010) 483: Pati–Salam 16 = (4,2,1) ⊕ (4̄,1,2) and Y/2 = (B − L)/2 + T₃R, which is precisely the structure of Prop. 5.3.
- M. Dubois-Violette & I. Todorov, Nucl. Phys. B 938 (2019) 751; I. Todorov, "Superselection of the weak hypercharge and the algebra of the Standard Model", JHEP 04 (2021) 164 (uses a B − L-type projector in Cl₁₀).
- N. Gresnigt, Phys. Lett. B 783 (2018) 212; A. Gillard & N. Gresnigt, Eur. Phys. J. C 79 (2019) 446.
- L. Boyle, arXiv:2006.16265.
- Hypercharge fixed by anomaly cancellation: C. Q. Geng & R. E. Marshak, Phys. Rev. D 39 (1989) 693; J. A. Minahan, P. Ramond & R. C. Warner, Phys. Rev. D 41 (1990) 715.

The specific claim (iii), "among the four projectors commuting with colour and Q, anomaly cancellation selects ±iL_{e₇}", may not appear verbatim in the literature. However, it is a direct corollary of the known Pati–Salam structure combined with the standard anomaly-fixing of hypercharge. As noted in M5, the numerical statement about the rejected options is wrong as printed.

**LQG input (Section 6).**
- Ashtekar–Baez–Corichi–Krasnov (1998); Domagała–Lewandowski and Meissner (2004); Ghosh–Mitra (2005), gr-qc/0411035, who state that the DL equation corresponds to counting |m| = j.
- Agullo, Barbero, Borja, Díaz-Polo & Villaseñor, exact counting (2008–2010).
- Engle–Noui–Perez (2010).

I know of no prior use of the ratio γ_DL/γ_ABCK as a physical parameter. It has no theoretical motivation.

**Koide.** The circulant form √m_k = a + 2|b|cos(θ + 2πk/3) with |b| = a/√2 is due to R. Foot (1994) and C. Brannen (2006). Koide himself discussed S₃/circulant structures. It is not new.

**TM2 and A₄.** Standard: Harrison–Perkins–Scott (2002), Albright–Rodejohann (2009), Altarelli–Feruglio (2005/2010). The "modified TBM confronted by JUNO" literature (e.g. arXiv:2511.15978) already explores corrections that lower θ₁₂.

### Sources consulted (web)
- [JUNO first measurement, arXiv:2511.14593](https://www.arxiv.org/abs/2511.14593)
- [Modified tri-bimaximal mixing confronted by JUNO, arXiv:2511.15978](https://arxiv.org/pdf/2511.15978)
- [Furey & Hughes, arXiv:2209.13016](https://www.arxiv.org/abs/2209.13016)
- [Krasnov, SO(9) characterisation of the SM gauge group, arXiv:1912.11282](https://arxiv.org/pdf/1912.11282)
- [Boyle, arXiv:2006.16265](https://arxiv.org/abs/2006.16265)
- [Ghosh & Mitra, gr-qc/0411035](https://ar5iv.labs.arxiv.org/html/gr-qc/0411035)
- [PDG 2026 review: W-boson mass](https://pdgweb.lbl.gov/2026/reviews/rpp2026-rev-w-mass.pdf)
