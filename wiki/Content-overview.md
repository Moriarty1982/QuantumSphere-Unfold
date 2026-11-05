# What the Companion contains

**State: 5 November 2026, research draft 4.10.0-draft with layers through v4.9.0-r82.** English companion of the German [Inhaltsübersicht](https://github.com/Moriarty1982/QuantumSphere-Unfold/wiki/Inhalt), which is the master. This page states what the *Quantum Sphaera Companion* assumes, defines and shows, and how far each part currently holds. Source labels at the end of each part are for checking; the page itself should be enough to understand the content. [Home](https://github.com/Moriarty1982/QuantumSphere-Unfold/wiki/English)

## How to read each statement

The Companion separates **conjecture** (the starting hypothesis), **mathematics** (a definition, theorem or construction built in the text) and **status** (proved, local or conditional, numerically checked, refuted, or open). Building mathematics from a conjecture does not prove the conjecture. Whether a unified theory follows is open.

## The starting conjecture

Spacetime and particles are projections of an underlying information layer. Matter, light (the photon) and a tachyon sector are meant to be *one* object seen from three frames. Spacetime points were to come from a "clock", originally the zeros of the Riemann zeta function. **Status:** conjecture. Since v4.8.0-r04 the Riemann paper is no longer a proof source; its proof chain for the Riemann Hypothesis does not hold.

## 1. The language: QAM over ZF

States, layers, operators, readouts and branches are written in a coded language, the **QAM**, defined on top of Zermelo–Fraenkel set theory by eight tagged tuple predicates. A finite instruction language (MML) and its execution semantics (MMA) sit above it. **Status:** clean definitions, recognition clauses rather than a new axiom system; translation back to set theory is shown for the admissible fragment.

## 2. The building block: three complex kernels

Each level has a biquaternion kernel $q = it + z_1e_1 + z_2e_2 + z_3e_3$, $e_3 = e_1e_2$. An involution $J$ splits every state into a symmetric part $C(f) = \tfrac12(f+Jf)$ (the **Heisenberg compensator**, $C^2 = C$) and an antisymmetric part. Since v4.8.0-r07 the sector is given by the sign of $s = \sum z_k^2$: matter $s > 0$, tachyon $s < 0$, light $s = 0$; the original norm had the wrong signature (1,6) and was replaced ("reading B"). **Status:** decomposition and sector rule are sound; that the sectors *are* matter, tachyon and light is conjecture.

## 3. Hopf structure and the frame constants

The three levels are linked to the classical Hopf fibrations over $S^2$, $S^4$, $S^8$. The central number is the **frame offset** $\beta_{\mathrm{sym}} = \sqrt{(\gamma_L-1)/(\gamma_L+1)} \approx 0.5494$ with $\gamma_L = \gamma_{\mathrm{BI}}/\gamma_{\mathrm{string}} \approx 1.8644$, the ratio of two published Barbero–Immirzi values (0.2375 and $\ln2/(\pi\sqrt3) \approx 0.1274$). **Status:** the fibrations are classical; their particle assignment is conjecture. $\beta_{\mathrm{sym}}$ is inserted, not derived. Since r63 it is read as a ratio of two horizon state countings, which works only with the U(1) counting; the literature prefers SU(2), which gives 0.604 (r68). The old label of the fibre $S^7$ as a group containing $G_2 \supset SU(3)$ was wrong and has been corrected.

## 4. Trioles and 5. Fractal light axis

The basic structure is threefold: three equal complex numbers 120° apart sum to zero. The triolic orbit scan is a well-defined local readout model, proved within its frame. "Triole" names three different structures (the frames M/P/T, the 120° kernels, and the three places of the octonionic triality form). The null axis ($s = 0$) is claimed to be transported from level to level and to be the light axis; that transport is explicitly open, and the diagnostic dimension $D_{\mathrm{res}} \approx 2.435$ is not a proof.

## 6. The master equation

$\mathfrak G + \mathfrak T_{\mathrm{tri}} + \mathfrak H_{\mathrm{HC}} + \mathfrak Q_{\mathrm{cl}} + \mathfrak B_\beta = 0$ organizes geometry, triole dynamics, compensator, closure and frame phase, with the 16-dimensional compensator matrix (called the Millennium matrix until r75) in the chain. **Status:** an outline of what should work together; couplings undetermined, no defined action. Research sections test what follows: commuting operators do not give a single eigenspace; direct compensator-to-mass routes are refuted one by one; a cyclic coupling gives the Brannen form but leaves masses underdetermined; scales stay free inputs; a geometry rebuilt from spinors is conditional and not a field solution.

## 7. Open problems OP1–OP5

OP1: derive $\beta_{\mathrm{sym}}$ (open; now "justify the two counting rules"). OP2: Dirac operator on the antisymmetric sector (old proofs rest on the Riemann paper). OP3: admissible shell passages (local QAM certificate). OP4: origin of the mixing angles (open; mis-posed in its old form, r61). OP5: cosmological constant (closed only locally by a detector threshold; exact form open). Details: [Offene Probleme](https://github.com/Moriarty1982/QuantumSphere-Unfold/wiki/Offene-Probleme) (German).

## 8. Physical readouts

The old chain sets $\Lambda$ to zero in the photon frame and explains the observed value as a matter-frame effect. Several links fail: the trace formula is not a defined action (v4.8.0-r05), $\beta^2/\ell_P^2$ is $10^{121}$ too large, and one corollary gives zero and a finite ratio $\gamma_L^5$ for the same quantity. What survives is the share reading $\Omega_M = \beta_{\mathrm{sym}}^2 \approx 0.302$ (Planck 2018: 0.315 ± 0.007; DESI DR2: 0.2975 ± 0.0086), valid for today only (r67). The printed regularization was wrong; the corrected finite part at $T = 0.393$, $\mu = 1$ is 1.686953 (r69, corrected in r70). None of the old predictions P1–P6 is confirmed.

## 9. Standard-model structure from the octonions

Layers r32–r60 build, from the Dixon algebra $\mathbb C\otimes\mathbb H\otimes\mathbb O$, the charges of one generation, a full left-handed generation with right-handed neutrino and anomaly-free quantum numbers (with the compensator read as chirality projector), and generations as orbits of triality. Masses and mixing remain the hard part: masks and couplings fit the data but do not explain them. Open predictions: $\sin^2\theta_{23} \le 0.54$ (H42) and $\in [0.49, 0.50]$ (H46), awaiting the next global fit or DUNE/Hyper-K; the W mass (H15). Full list: [Vorhersagen und Tests](https://github.com/Moriarty1982/QuantumSphere-Unfold/wiki/Vorhersagen-und-Tests) (German).

## 10. The 4.10 consolidation and the latest tests (r69–r74)

A second language model worked on OP5 with the author (25–30 October). Results: a frame change cannot remove a balance defect; "neutral" has three distinct meanings; no route fixes the absolute vacuum term; the probe light cone comes from the Clifford structure; a new section separates quantum and relativistic readouts through a mediator with explicit proof obligations, recovers the field doublet from its Gram matrix plus orientation, and pushes a numerical compatibility check to fourth derivative order at three points (not a regional solution). Test H48 — $\beta_{\mathrm{sym}}$ as the frozen length of the matter/tachyon state — is refuted: the frozen value carries the expansion history.

Layer r71 independently confirms the second model's 70-digit fifth-order germ of the OP5 comparison system, including the compatibility part $G$. The puzzling count −1 at degree 5 was a numerical artifact. The system leaves one function of four variables free: shifts along the polar angle $\vartheta$. This is an exact gauge symmetry, because the background depends only on $t$, $r$ and $\varphi$, with mass $h(t, r)$ and connection $A = M(t)\,d\varphi$. The extra condition $\Omega$ is gauge invariant; it adds information only on the light cone of the reconstructed geometry and on two planes. Pre-registered tests H49 and H50 are refuted. Next step: fix the $\vartheta$ gauge, then test involutivity.

Layer r72 fixes the $\vartheta$ gauge by prescribing one current component, $\Psi^\dagger K_2\Psi$; this removes exactly the free function. The pre-registered Cartan test H51 is confirmed: the gauged symbol is involutive from order 6 on and not before, leaving formally 14 functions of three variables. Three pre-registered tests of formal integrability (H52 to H54) are invalid by their own criteria, each because of a test-design error. They still show that the stored fifth-order coefficients cannot be extended, that everything is clean through the degree-6 equations, and that the degree-7 equations add four conditions on the sixth derivatives. The Spencer cohomology of the gauged symbol leaves room for exactly four, and an error bound rules out a numerical artifact. So the gauged system is, by all evidence, not formally integrable at order 6, but this is not formally confirmed. Next: a second base point (H55), then the explicit conditions and a new Cartan test.

Layer r73 confirms the four conditions at a second base point (H55): the gauged system is not formally integrable at order 6. An exploration determines them: they are sixth-order equations that act only on light-like waves, fix one of seven polarizations per null direction, and depend on the direction through the four quadrics of the two special planes of r71; they are the remainders of the four relations $q\,d_k\,\Omega$. The Cartan test of the extended symbol (H56, H57) is invalid: not involutive at order 6, and from order 8 the available precision cannot decide. Next: consistent high-precision data at the repaired germ.

Layer r74 rebuilds Ω consistently at the repaired germ. With consistent data the extended symbol is, by all evidence, involutive first at order 8 (H58, invalid only by its gap threshold); the value 724 of H57 was an artifact. The Spencer cohomology of the extended symbol leaves room for up to four further hidden conditions on 7-jets and three on 8-jets. A method check shows a structural precision limit: Ω and the four conditions are nearly consequences of the basic equations (weight about 1e-8); staged elimination and a plane-wave reformulation do not lift it.

Layer r77 repeats the chain in high precision (70 digits) and runs the decisive eliminations on parallel GitHub runners. The results:
- There are exactly four hidden conditions, and the extended symbol is involutive first at order 8 (characters 723, 130, 12, 0).
- There are no further hidden conditions on 7- and 8-jets (H59 confirmed), so the system is formally integrable at the germ.
- It carries six real massless modes per null direction (H60 confirmed). These are not Weyl or Majorana modes in the naive spin assignment (H61 refuted).
- At a fixed background the symbol is invariant only under scaling (H62 and H63 refuted).
- The construction R itself is coordinate covariant and internally Lorentz covariant (H64 confirmed, run 2 not blind), so the Lorentz breaking comes from the background.

Layer r78 confirms that R is covariant at value level, with all lower-order terms (H66, not blind); hence Ω is covariant too. The gauge Ψ†K₂Ψ = S is preserved only by so(1,2), the stabilizer of e_y (H65(b); H65 as a whole is invalid by its control bound). The four hidden conditions are therefore covariant at most under so(1,2).

Layer r79 shows that the four hidden conditions are gauge independent (H67 confirmed). Five gauges, including the Lorentz scalar Ψ̄Ψ, each give a fibre of 477 and 6 polarizations on the cone. The conditions therefore belong to the covariant content of the system, and the Lorentz breaking comes only from the background.

Layer r80 asks whether that background is generated by the three spinor blocks. An exploration of their polar (Fierz) variables shows three regular Dirac fluids in a Hubble-like counterflow v = ±x/t, with all spins along the azimuthal axis. The pre-registered test H68 is refuted: in the model's own coframe metric the connection A = M(t) dφ satisfies no Yang–Mills equation on span(λ₂, λ₄, λ₆) with the colour current as source (residual 0.955), and h satisfies no Klein–Gordon equation with the Yukawa source (0.995 massless, 0.826 massive). The sources are about a thousand times too small and point in other colour directions. By author decision the comparison-model branch r71–r80 is closed here: its results remain valid as local statements about a construction whose background is prescribed. The next step is one level up, a survey of the action ansätze and of what a joint dynamics for spinors, connection, scalar and coframe must achieve.

Layer r81 records the first joint action W1 (Einstein–Cartan gravity with an independent coframe, the sixteen Weyl states of one generation on the Dixon carrier, a U(1) from the inner unit) and the work on it. The complex reading of the action forces a current balance between matter and its tachyon image; an offset matter–tachyon pair satisfies it exactly and carries no net energy (H69), provided the offset is comoving with the expansion (H70). Coupling matter by a mass to its tachyon image gives the tachyonic Dirac equation (H71). A Λ-like term can arise from tachyonic modes of both norm signs, but its size is not fixed by the structure (H72; H73 refuted). A Higgs-like negative mass squared follows kinematically for the transition between matter and a counter-moving tachyon image. Three earlier statements are corrected, among them the frame reading of r44.

Layer r82 adds the Higgs sector (action W2). Alone it has the familiar vacuum energy of about (100 GeV)⁴, some 10⁵⁵ times too large. Together with the tachyon image of every field, whose energy–momentum tensor changes sign, the vacuum energy becomes (a − b)·V_min for frame weights a and b: exactly zero at photon weights, V_min/γ at matter weights (the structure of Kaplan–Sundrum energy parity). Two pre-registered, not blind stability tests follow. A direct coupling between the sectors makes the exactly cancelling case unstable for every coupling strength (H74); with gravity as the only coupling there is no exponential instability, but the common mode grows like t² and a ± mass pair runs away together (Bondi; H75). An exploration shows that the torsion four-fermion interaction of W1 is attractive in a Lorentz-scalar pairing channel, but condenses only at the Planck scale; the only gauge-invariant channel is the Majorana channel of ν^c. The structure supplies mechanisms, not a scale.

## Never claimed

Exact finite C5 zero closure, exact all-readout terminality, T2 closure, a global photon-clock/RH theorem and global all-readout closure. All five guards have stood unchanged since layer r60: *guarded effective/local and frame-typed closures, not exact global closure.*
