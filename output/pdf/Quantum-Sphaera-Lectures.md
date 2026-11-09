# Quantum Sphaera Companion
A lecture course on a common algebraic carrier and the limits of its physical interpretation

Eight lectures • English study notes and recording guide

Research snapshot: public release v4.10.0, research layers through v4.10.0-r11, and the committed area-operator follow-up a88cf08.

## How to use this course
The main path assumes complex numbers, vectors and elementary linear algebra. Familiarity with special relativity helps in Lecture 4. Lectures 6 and 7 introduce the purpose of their more advanced machinery before using it. Each lecture pairs an argument with a board exercise and an explanation of its scope.

The source Companion is a research record. These notes teach a selection of its mathematical arguments, trace the physical claims back to their prerequisites, and give the major corrections a place in the story. The thesis atlas at the end maps the broader scope.

For recording, start from the spoken opening, build the equations one line at a time, leave a pause for the exercise, and show the scope statement on its own slide.

# 01  What could “one object” mean?
## Opening narration
“Imagine someone gives you three descriptions and says they belong to one object. You can ask whether the descriptions use the same mathematics. You can also ask whether they represent the same physical state. Those questions sound similar. Today we will see why the difference determines what Quantum Sphaera can claim.”

The motivating proposal is that matter, light and a tachyon sector might be read from a common underlying structure. We begin with a modest question. What operations and measurements would make such a claim precise?

## Four statements to separate
A shared carrier means several data sets are elements of one mathematical space. Vectors (1,0) and (0,1) both live in R². They are distinct elements.

A passive change of description changes coordinates while keeping the represented object fixed. If the basis vectors are swapped, the coordinates of the first basis vector become (0,1) in the new basis. The physical interpretation of the basis must be carried along.

An active transformation sends a state to another state with the description held fixed. Rotating the arrow (1,0) into (0,1) in the original basis is an example. If the transformation is a symmetry, certain quantities agree between the two states. The agreement depends on which quantities are invariant.

A readout selects information. The map (x,y) ↦ x sends all points on a vertical line to the same output. A later attempt to reconstruct y must supply further data.

## Board exercise
Show the vectors (2,1) and (2,−3). Both give 2 under the first-coordinate readout. Their squared lengths are 5 and 13. They therefore cannot be related by a length-preserving rotation, even though one instrument cannot distinguish them. Which additional measurement separates them? The second coordinate, or even the squared length for this particular pair.

# 01  From a shared carrier to a prediction
## The claim in three steps
Write “carrier → operation → readout” across the board. Under carrier put a state x. Under operation put a map A with a specified domain. Under readout put R, a map with a specified output and meaning.

= x  ↦  Ax  ↦  R(Ax)

If A is supposed to be a passive frame conversion, its action on state data and on the measurement formula must be compatible. If A is a projection, specify the discarded data. If R claims to predict an observed quantity, specify the measurement and the units, then give a derivation or a calibration procedure.

## Demonstration with a simple instrument
Let R(x,y)=x and let J(x,y)=(x,−y). Show both arrows landing on the same number. Now introduce S(x,y)=y. S changes sign while R remains fixed. The equality R(Jv)=R(v) is a precise statement about one readout. It cannot by itself establish agreement for every measurement.

Apply that discipline to the M, T and P labels used in the Companion. The labels refer to different proposed descriptions or sectors. Every actual comparison needs a map and a target formula. In particular, a construction involving a null field cannot be interpreted as a finite boost to a photon rest frame.

## What changed in the research
The early Unity argument drew on the project's Riemann work. That support was withdrawn. The modern lecture starts with explicit algebra and keeps the physical identity as a research hypothesis. The back-to-basics reconstruction and r11 recover the exact question behind the later counting and cosmology work.

## Recording beats
Cold open with the two arrows. Reveal the four statements one at a time. End by circling the arrow between the carrier and the measured value. The next lecture supplies a concrete carrier.
Source trail: Overall Picture T1 and T4; Back to the Basic Idea §§5–10; r11.1–r11.2.

# 02  Building the biquaternion carrier
## Opening narration
“Today we build the object on the board. By the end we will have a scalar that can vanish for a nonzero vector. That small fact will matter when we talk about light.”

Start with quaternion basis 1,e₁,e₂,e₃. The eₐ square to −1. The cyclic products e₁e₂=e₃, e₂e₃=e₁ and e₃e₁=e₂ reverse sign when the factors are swapped. Complexification allows complex coefficients. The scalar imaginary unit i commutes with the basis.

= q = it + Z,    Z = z₁e₁ + z₂e₂ + z₃e₃

The quaternion conjugate sends the vector part to its negative and keeps the complex coefficients as written. Componentwise complex conjugation is a separate operation. Use the word “quaternion” before “conjugation” every time this first calculation appears.

## Derive the norm
Expand Z². Every mixed term comes in an anticommuting pair. For instance the coefficient of z₁z₂ is e₁e₂+e₂e₁=0. Only the three squares survive.

= Z² = −s(z),    s(z) = z₁² + z₂² + z₃²
= (it + Z)(it − Z) = −t² + s(z)

The two middle terms cancel because it is central. The expression is complex bilinear in its ingredients. An expression with absolute squares would be a different quadratic construction. In the field interpretation discussed later, t is an invariant parameter of this presentation. A spacetime coordinate transformation would require its own specification.

## Board exercise
Take t=0 and z=(1,i,0). The bilinear scalar s is 1+i²=0. The Hermitian squared length is |1|²+|i|²=2. Put the two answers beside each other and ask the audience to explain why neither calculation overrides the other. Each uses a different form.

# 02  A trio of components
## The root-of-unity picture
Set ω=exp(2πi/3). Draw 1,ω,ω² on the complex unit circle at equally spaced angles. Their sum vanishes because (ω³−1)/(ω−1)=0. For z=c(1,ω,ω²), the sum of squared components also vanishes.

= s(z) = c²(1+ω²+ω⁴) = c²(1+ω²+ω) = 0

The two zero conditions have separate meanings. One is a linear condition on the chosen coordinates. The other is a quadratic condition on the vector. The example lies in their intersection.

## Show why both conditions matter
Display z=(1,−1,0). Its components add to zero, yet s=2. Now display z=(1,i,0). It has s=0, yet the components sum to 1+i. Neither condition forces the other. The pictures explain how easy it is to turn an elegant special configuration into a claim that is too broad.

There is a neat converse for three components. If their sum and sum of squares both vanish, then their pairwise product sum vanishes, since the square of the sum is the sum of squares plus twice the pairwise sum. The monic cubic with these three roots is therefore X³−z₁z₂z₃. If the product is nonzero, its three roots are one common scalar times the three cube roots of unity, in some order. If the product is zero, all three roots vanish.

## Scope
The converse is an algebraic fact about three coordinates. The coordinate condition and the field invariant play different roles. A physical theory would still have to explain why those coordinates and those conditions describe the system in question.

## Recording beats
Animate the circle first. Use the two counterexamples as an audience prediction. If time is short, put the converse in the handout and state its result after the pause.
Source trail: Overall Picture T2–T3; Back to the Basic Idea §§8–9; short draft, kernel and frames.

# 03  The compensator is a projector
## Opening narration
“What happens if you average something with its mirror image? You keep the part that the mirror leaves fixed. The calculation is short. Interpreting what the average represents is where the real work begins.”

Let V be a real vector space and J a real-linear involution, so J²=I. Define the two linear maps

= C₊ = (I+J)/2,    C₋ = (I−J)/2.

Calculate C₊²=(I+2J+J²)/4=C₊. In the same way C₋²=C₋, and C₊C₋=(I−J²)/4=0. The two maps sum to I.

= f = C₊f + C₋f,    JC₊f=C₊f,    JC₋f=−C₋f.

If a vector is fixed by J, C₊ leaves it unchanged. If J reverses it, C₊ sends it to zero. This proves the decomposition into the +1 and −1 eigenspaces. No inner product is needed. Calling it orthogonal would require an inner product and a corresponding property of J.

## Board exercise
Take J(x,y)=(y,x). For f=(3,1), find C₊f=(2,2) and C₋f=(1,−1). Draw both and show they add to f. Now try f′=(4,0). Its symmetric part is also (2,2). The two distinct inputs demonstrate exactly which information was removed.

## A real-linear subtlety
When J contains complex conjugation it need not be complex-linear. For Jz=i conjugate(z), J(iz)=−iJ(z). The projector proof still works over the reals. Writing down the scalar field before the proof prevents a subtle mistake in later interpretations of the image.

# 03  Does this operation produce light?
## Put the interpretation on trial
In the concrete field reading, write z=E+iB with real three-vectors. The involution J sends z to i times its complex conjugate. Its square is the identity because i times the conjugate of i equals 1.

= J(E+iB)=B+iE
= C₊(z)=(1+i)(E+B)/2

Set a=(E+B)/2. In the resulting field E′=B′=a. If a is nonzero, the two vectors are parallel. Now calculate the bilinear invariant introduced in Lecture 2.

= s(C₊z)=(1+i)² a·a=2i|a|².

The image is therefore non-null whenever it is nonzero. If E=−B, the output is the zero field. Equal field magnitudes and the vanishing of the real part of s are insufficient for nullity. The imaginary part must vanish too.

## A side-by-side scene
On the left show E′=(1,0,0), B′=(1,0,0). On the right show E″=(1,0,0), B″=(0,1,0). Both pairs have equal magnitudes. The first has s=2i. The second has s=0. Let the arrows and the imaginary part of s change together.

The demonstration separates an average, a product, and a physical measurement. The relation e₁e₂=e₃ describes quaternion multiplication. It supplies no reason for E′ and B′ in this averaging map to become perpendicular.

## Scope
The algebraic projector survives the test. This particular photon-production interpretation fails. A new interpretation would require a specific map from the projected algebraic data to a physical state, with its own checks.
Source trail: Overall Picture T2–T3; Back to the Basic Idea §7; r11.2.

# 04  Lorentz transformations, duality and sectors
## Opening narration
“Two operations can act on the same field and preserve different things. Today we will track exactly what each one preserves. That will tell us which sectors it can connect.”

Use units in which E and B have the same dimensions. The complex field z=E+iB packages the electric and magnetic field vectors. Its bilinear invariant reads

= s(z)=|E|²−|B|² + 2i E·B.

The real and imaginary parts encode the usual two electromagnetic field invariants up to conventions and factors. In this representation proper orthochronous Lorentz transformations preserve s. A duality rotation is a separate operation.

= z ↦ exp(iα)z    implies    s ↦ exp(2iα)s.

Set α=π/2. Then z ↦ iz, meaning (E,B) ↦ (−B,E). It sends s to −s. This quarter-turn is distinct from complex conjugation z ↦ conjugate(z), which sends (E,B) to (E,−B) and s to its conjugate. The Companion distinguishes the tachyon map and time reversal.

## Use the complex plane
Plot s on a complex plane. A Lorentz operation leaves the dot where it is. A duality rotation moves it on a circle of fixed |s|. The origin is a separate level. Any composition of these transformations preserves |s|. Hence a point at positive radius cannot reach the origin by such a composition. This argument establishes a separation by invariants and does not require a classification of all Lorentz orbits.

## Board exercise
Start from E=(2,0,0), B=0. Then s=4. After the quarter-turn E′=0, B′=(2,0,0), and s′=−4. Ask whether a second duality angle can make s zero. Its radius remains 4 for every angle.

# 04  A null field and a mass shell
## Work through a null example
Let E=(1,0,0) and B=(0,1,0). The magnitudes agree and E·B=0. Thus s=0 while z is nonzero. In particular the energy density in standard electromagnetic normalization is proportional to |E|²+|B|²=2. A vanishing invariant does not imply vanishing energy or vanishing field.

For a general complex s, the terms “positive” and “negative” apply only when the imaginary part vanishes. On that real slice, the sign distinguishes electric and magnetic dominance. This is a statement about the classical field data.

## Compare two kinds of quantities
Write s on the left and p² on the right. The left side takes an electromagnetic field as input. The right side takes a four-momentum as input. For signature (+,−,−,−), the standard relativistic mass shell has p²=m² in units c=1. This separate formula gives the conditions under which “massive,” “massless,” and “spacelike momentum” refer to particle kinematics.

An argument identifying the two classifications must give a field-to-momentum map and justify its transformation law, dimensions and regime. Reading the signs side by side is a motivation for seeking such a map.

## Frame convention on screen
M, T and P are the Companion's frame labels. Keep the frame labels attached to the quantities being compared. If using a reference R from the older scale discussion, introduce it separately. The back-to-basics notes distinguish it from the register P of a nonzero null field.

## Recording beats
Show the invariant-plane animation, then freeze on the two input types. End with the question “What map would make this comparison meaningful?” That question returns in Lectures 7 and 8.
Source trail: Overall Picture T1, T3, T10; Back to the Basic Idea §§4–6; r51, r81 and r11.2.

# 05  Hopf geometry and the algebra beyond quaternions
## Opening narration
“A quotient can tell us exactly what information a picture has thrown away. The first Hopf map is a clean example. We can write it down and see the lost information directly.”

Take complex u,v with |u|²+|v|²=1. The pair lies on S³. Define the first Hopf map by

= h(u,v)=(2 Re(u conj(v)), 2 Im(u conj(v)), |u|²−|v|²).

The squared length of the image is 4|u|²|v|²+(|u|²−|v|²)²=(|u|²+|v|²)²=1. So the output lies on S². Simultaneously multiplying u and v by exp(iθ) preserves u conj(v) and the two magnitudes, leaving h fixed.

## Recover the fiber
For a point away from the two poles, the third component gives the two magnitudes, and the first two components determine the relative phase. The common phase remains free. At a pole one component vanishes and the surviving component can carry any phase. Thus the fibers are circles, including at the poles.

## Board exercise
Compute h(1,0)=(0,0,1), h(0,1)=(0,0,−1) and h(1/√2,1/√2)=(1,0,0). Recompute the last value after multiplying both entries by i. For contrast, multiply only u by i and get (0,1,0). Common phase and relative phase have different effects.

# 05  Where the proposed cascade adds structure
## Three classical fibrations
= S¹ → S³ → S²
= S³ → S⁷ → S⁴
= S⁷ → S¹⁵ → S⁸

These fit the complex, quaternionic and octonionic constructions. The sequence uses increasingly large real normed division algebras. Octonion multiplication is nonassociative. In particular, the appearance of an S⁷ fiber does not give S⁷ an associative group multiplication analogous to the unit complex numbers or unit quaternions.

## A construction requires maps
A fibration specifies a total space, a base, and fibers. To make the three stages into a physical cascade, supply the maps that transfer data between stages, their domains, and a rule for transporting a state. To turn transport into dynamics, supply a law for its evolution and a physical interpretation of the time parameter.

Draw the three fibrations on separate rows. Draw any inter-row arrows in a different color and label them “additional map.” A claim linking levels to light, matter or generations belongs on those inter-row arrows. The existence of the individual fibrations establishes their geometry. The extra claims require additional work.

## A preparation for particle algebra
The Companion also uses the tensor product of the complex, quaternion and octonion algebras, often called the Dixon algebra in this discussion. Octonions can act by linear multiplication operators on a vector space. Composition of those linear operators is associative, even when the octonion products used to define the operators are not. Distinguish an octonion product ab from the composed action LₐLᵦ on a third element.

## Recording beats
For video, reveal one row at a time. Keep the first Hopf calculation on screen while introducing the higher analogues. Show the proposed links as a separate overlay.
Source trail: Overall Picture T5 and T7; Back to the Basic Idea §8; research correction r70.

# 06  What a one-generation construction establishes
## Opening narration
“Suppose a small algebraic system contains states whose charges match a familiar particle table. What exactly has been achieved? First we will build a small example and then ask which extra choices turn the labels into physics.”

The Companion's one-generation work organizes states using a complex/quaternion/octonion construction with chosen operators and identifications. This lecture uses an exterior-algebra toy model to illustrate the number-operator mechanism. The toy model isolates the counting. The full construction supplies the embedding, chirality conventions and representation data.

## A worked exterior-algebra model
Let W=C³ with basis b₁,b₂,b₃. The exterior algebra has degrees 0,1,2,3. Its degree dimensions are 1,3,3,1. For example, degree two has basis b₁∧b₂, b₁∧b₃ and b₂∧b₃. Define N to multiply a degree-k vector by k. A charge operator Q=N/3 then has the eigenvalues

= degree      0       1       2       3
= charge      0      1/3     2/3      1
= dimension   1       3       3       1

If SU(3) acts on W in its defining representation, it acts on each exterior degree. The invariant determinant form identifies the degree-two space with the dual of W. Degrees zero and three are singlets. Thus the two three-dimensional entries have a precise representation distinction.

## Board exercise
Find the charge of b₁∧b₃ and the charge of b₂. Answers are 2/3 and 1/3. Ask why the two spaces can transform differently even though both have dimension three. One is W and the other is identified with W* under the chosen SU(3) action.

# 06  Choices, successes and remaining obligations
## From a charge table to a model
The overall picture reports a construction of one generation under specified choices. A viewer should be able to name the operator producing the charges, which algebra or representation it acts on, and how the chiral sectors are selected. A charge spectrum by itself leaves open the action of the gauge group on the full space, the dynamical couplings and the generation count.

In the Companion a chiral projector acts on its Dixon carrier. In the corrected comparison the tachyon map preserves that projector. A horizon spin mask acts on a different space. To transfer a selection from one to the other one needs an explicit map between carriers and a proof that it intertwines the relevant operations.

## Why masses are a separate lesson
Write a charge operator Q and a mass operator M side by side. On a two-dimensional space, choose Q=I. Both diagonal matrices diag(1,2) and diag(5,9) commute with it. The same charge data admit different masses. A physically predictive calculation must identify what fixes the mass operator and its scale. This is the gap illustrated by the Companion's attempts at direct mass readings.

The empirical Koide relation and mixing-angle fits are discussed in the research record. A relation that can be matched by choosing a mask or adjustable parameters needs an independent rule for those choices before it becomes a prediction. OP4 remains open.

## Recording beats
Show the four exterior degrees as a rising staircase, then replace it with two mass matrices that share Q. Keep “toy model” visible on the charge slide and “under stated choices” visible on the Companion result.
Source trail: Overall Picture T7–T8; r32–r60; r51 and r11.2 for the projector comparison.

# 07  Dynamics, gravity and the OP5 reset
## Opening narration
“An algebra tells us what we can write down. An action tells us which variations a particular model permits and which equations follow. The distance between those two statements is the subject of this lecture.”

A schematic action is S[fields]=∫ L. One varies the declared fields with the declared boundary conditions and looks for δS=0. For example, on an interval with fixed endpoints, take

= S[u]=∫ [(u′)²/2 − m²u²/2] dt.

The first variation is ∫[u′δu′−m²u δu]dt. Integration by parts gives −∫(u″+m²u)δu dt because the endpoint term vanishes. Arbitrary interior variations give u″+m²u=0. The equation depends on the chosen Lagrangian and on which variables can vary.

## What the Companion has explored
The Master equation, compensator matrix and probe equations organize candidate couplings and Dirac, Yang–Mills and Einstein limits. W1/W2 gave conditional action candidates with explicit field readings. Subsequent work corrected the gravitational sign in the W1 equations and corrected the earlier vacuum-cancellation interpretation of the tachyon branch. The current programme freezes those candidates pending the earlier physical identifications.

The OP5 comparison model exhibits structural results under its own assumptions, including a gauge symmetry and local compatibility work. The source–return result is a conditional schema. A native route would need the Companion's actual data to supply and verify its premises. These are separate claims even if the same equation appears in both.

## Board question
If you hold a geometric variable fixed during variation, which equation will you obtain by varying it? None. Its equation needs a variational problem in which the variable is actually free, or a different derivation.

# 07  Four ratios and one missing measurement
## Reconstruct the break
The historical OP5 chain moved from a spectral term through a proposed metric action to a bare cosmological term and then to a proposed cancellation. The step from spectral data to the physical action was missing. The author suspended that chain as a foundation in November 2026. The current question starts earlier. Which independently defined physical quantity can actually be read out of the core?

## A small model for the denominator problem
Take two positive register entries x and y. Put q=x/y. The fraction of the first entry in their sum is x/(x+y)=q/(1+q). If the entries have different positive physical weights a and b, the first weighted fraction is

= f = ax/(ax+by) = aq/(aq+b).

With q=1/2, the unweighted fraction is 1/3. For a=2 and b=1, f=1/2. More generally, for any desired 0<f<1 and fixed q>0 one can choose a/b=f/[q(1−f)]. A numerical match can therefore be produced without an independent prediction. The same lesson applies when comparing a register ratio, a cascade outflow fraction, a γ contrast and the cosmological matter fraction ΩM. These have separate definitions and denominators.

## Distinguish fitting from stability
Suppose a recurrence has the fixed point q* because q* was entered as a parameter. Showing convergence to it is a stability result. Predicting q* would require a model that supplies the value independently. The r11 review makes this distinction for the r31 cascade.

## Recording beats
Show the historical chain with the missing arrow highlighted. Use the numerical example as the board centerpiece. Finish by writing the new question on an otherwise empty slide.
Source trail: Research Status r71–r80 and r81–r86; v4.10.0-r01, r05 and r11.1–r11.3; OP5 Rebuild.

# 08  What is established, conditional or open?
## Opening narration
“Let us finish by rebuilding the chain in the order in which the claims depend on one another. Wherever we need a new hypothesis, we will put it on the board as a separate step.”

Start with the carrier, its operations, and the invariants. The involution gives a real-linear projector. The field calculation separates the non-null levels from the null level under Lorentz and duality operations. The named physical identifications require further maps. The one-generation construction works under stated choices. Candidate dynamics and local comparison results come with their own assumptions. An observable needs a derived measurement prescription.

## The horizon counting example
In the investigated counting model, saturation restricts the magnetic label to m=±j. This leaves j free among the permitted spin values. The minimal spin can dominate or be selected only with an additional rule. In r10, the investigated Unruh-statistics route gives the same counting rule for the two descriptions under its stated assumptions. The alternate interpretation uses a different area quantum and leaves its origin open.

A follow-up tests a proposed explanation by a passive operator change. Suppose A has a smallest positive spectral value a and U is unitary. The operator UAU⁻¹ has the same spectrum as A. If the same operator were also A/G with G>0, its smallest positive spectral value would be a/G. Equality forces G=1. The argument applies under the assumption of one fixed area operator related by unitary conjugation. It leaves a different operator or independently motivated accessible state space as a separate research problem.

## Board exercise
For A=diag(0,2,5), swap the last two basis vectors. The matrix entries change places but the smallest positive eigenvalue stays 2. Compare with A/2, where it becomes 1. Show which assumption is broken if one tries to identify the two operations.

# 08  The remaining research programme
## A map of open obligations
OP1 asks for the origin of the symmetric frame factor βsym. The horizon-counting interpretation has model-dependent inputs. The area-operator argument on the preceding page blocks one explanation under its explicit assumptions.

OP2 asks for the Dirac operator in the intended native construction. Writing down a probe equation and recovering the relevant operator from the underlying data are separate obligations.

OP3 asks for transitions between the proposed shells. An actual transition rule requires source and target data, a map or dynamics, and compatibility with the quantities the model intends to preserve.

OP4 covers masses and mixing, where independent selection rules and scales remain missing. OP5 has separate core, observable and dynamics tasks. The core schema is conditional, the native route is open, and the historical Λ basis is suspended. H96 and H97 retain their recorded status. H98 is unaffected by the r10/r11 comparison.

The closure guards continue to limit what can be exported. C4 is withheld, the remaining C5 form (iii) is open, and C6/T2 is unclaimed. QAM can record a declared frame profile, map and target formula; type checking this record gives a bookkeeping result.

## Closing narration
“We began with one object and three names. We can now say exactly what the mathematics has given us. It gives a common carrier, several explicit maps and some sharp restrictions on what those maps can accomplish. The question for the next stage is how to get from those restrictions to a measured quantity. We need to define the quantity independently and then derive the link.”

Source trail: Research Status and Overall Picture T13–T15; v4.10.0-r08–r11; committed follow-up a88cf08.

# Thesis atlas  T1–T8
## Structure and interpretation
T1 • Unity. Common carrier and structured transformations are available. Identity of full physical states remains a hypothesis. The early Riemann-based justification was withdrawn.

T2 • Compensator. The involution yields complementary projectors, with the domain and scalar field specified.

T3 • Sectors. The complex-bilinear field invariant gives the sign distinction on a real slice and the null condition. Physical particle identifications require a separate bridge.

T4 • Riemann origin and clock. The earlier proof source is withdrawn. The GUE derivation was archived and the early P1 prediction was refuted.

T5 • Hopf architecture. The fibrations are classical. The physical assignments and assembly into a dynamical cascade remain proposals.

T6 • Symmetric frame factor. Counting interpretations can produce a ratio under specified counting choices. An independent derivation of the factor remains open. The r10/r11 comparison exposes a missing area or access rule.

T7 • Gauge group and one generation. The Companion reports a construction under declared choices. It gives no exclusion of an additional generation.

T8 • Masses and mixing. Direct routes were refuted or only fitted the data. Empirical relationships and open proposals belong in the research discussion with that status visible.

## How to read the numbering
The T labels here follow the wiki thesis atlas. The label C6/T2 in the closure register belongs to that register's own naming scheme. Read each label in its source context.

# Thesis atlas  T9–T15
## Physical readings and proof discipline
T9 • Cosmological term. The earlier Λ derivation is suspended. The matter-fraction numerical identification needs a measurement bridge. The conditional OP5 core work has a separate status.

T10 • Frame-shifted constants. Earlier claims of shifts in ℏ, G and related quantities lacked support in the investigated reading. Frame conversions require a declared map and target formula.

T11 • Hawking, strings and loop quantum gravity. The record contains interpretive proposals, including a string/LQG pairing of sectors. The equivalence and the physical assignments remain unproved.

T12 • Entanglement and Bell. A shared proper-time interpretation is discussed. The required equivalence step is open. A compatible reading and a physical derivation are different achievements.

T13 • Master architecture. The equations and matrix organize candidate models. A common native dynamics and the relevant coupling choices remain unresolved.

T14 • QAM, MML and MMA. The formal language supplies recognition and bookkeeping rules, with a supported reverse translation for its admissible fragment. This organizes data and assumptions for checks.

T15 • Guards. Local and frame-typed results retain their scope. A comparison-model theorem needs verified hypotheses before transfer to the Companion's native system.

## Source trail
@ Overall Picture and thesis map | https://github.com/Moriarty1982/QuantumSphere-Unfold/wiki/Gesamtbild
@ Research Status | https://github.com/Moriarty1982/QuantumSphere-Unfold/wiki/Forschungsstand
@ Public Companion v4.10.0 | https://doi.org/10.5281/zenodo.23991357
@ Back to the Basic Idea | https://github.com/Moriarty1982/QuantumSphere-Unfold/blob/a88cf08/notes/research/qsc_back_to_basic_idea_2026_11_06.md
@ OP5 Rebuild | https://github.com/Moriarty1982/QuantumSphere-Unfold/blob/a88cf08/notes/research/op5_neuaufbau_2026_11_06.md
@ Research layer r11 | https://github.com/Moriarty1982/QuantumSphere-Unfold/tree/a88cf08/notes/research/v4_10_0_r11

# Production sheet  A first video
## Pilot  What Does “One Object” Mean?
0:00–0:20 • Presenter opens with the opening narration from Lecture 1. Show the series title after the question.

0:20–1:05 • On a fixed coordinate grid show (1,0) and (0,1). Narration: “They live in the same space. To decide whether these describe one state, we need to know whether the basis changed or the arrow changed.”

1:05–1:50 • Show two pairs, (2,1) and (2,−3). Highlight their common first coordinate. Narration: “Our instrument reports two in both cases. Now measure the squared length. We get five in the first case and thirteen in the second. A readout can hide a difference without removing it.”

1:50–2:20 • Reveal “carrier → operation → readout.” Narration: “In this series we will build the carrier, work through its operations, and ask which observations they actually explain. Next time we start with the biquaternion.”

## Preparing the scenes
Make one 16:9 slide per beat. Typeset equations and labels in the slides. For exact rendering export the finished scenes as images or use a slide import mode that preserves their layout. Provide the English narration separately and preview every occurrence of a technical term. Split longer calculations into one formula step per scene.

For a full lecture, expand the board calculation, let viewers try the exercise, and pause after revealing the solution. The lecture notes supply a teachable argument and examples. A 25–30 minute recording still needs a timed rehearsal or an expanded line-by-line narration.

## A production choice
HeyGen AI Studio can import slide material and assemble narrated avatar scenes. A source-generated Video Overview can be used to try out the opening at a lower level of editorial control. For the full lectures, keep the exact equations, script and status statements under editorial control.
@ HeyGen PPT/PDF import | https://help.heygen.com/en/articles/13007313-ppt-pdf-to-video
@ Google Video Overviews | https://support.google.com/gemininotebook/answer/16454555?hl=en
