import QSFormal.Dixon

/-!
# Ladungen, Chiralität und Brechungsstufen (v4.9.0-r34 bis r47)

Formalisiert die exakten algebraischen Kerne der Runden v4.9.0-r34 bis r47 aus
`Quantum_Sphaera_Companion_v4_8_0_source.tex`; die zugehörigen Rechnungen stehen in `notes/research/v4_10_0_r34_r47/llm/`.

* r36 (H21a): Die zyklische Vertauschung `σ : e₄ → e₅ → e₆ → e₄`, `e₁ ↦ −e₃`, `e₂ ↦ −e₁`, `e₃ ↦ e₂`, `e₀, e₇` fest, respektiert alle 64
  Basisprodukte (also, durch Bilinearität, die Oktonionen-Multiplikation) und hat Ordnung 3. Unter den 48 Vorzeichen-Fortsetzungen des
  Zyklus auf `e₁, e₂, e₃` ist sie die einzige mit dieser Eigenschaft. Dass sie damit in `Stab(e₇) = SU(3)` liegt, ist die Definition
  des Stabilisators und wird hier nicht weiter formalisiert.
* r45 (H30a): `c (e₇ · c x) = −(x · e₇)` für alle `x`: Die Konjugation tauscht Links- und Rechtsmultiplikation mit `e₇`.
* r34/r35, r42, r43, r47: Die vier Ladungs-Sektoren werden durch die Vorzeichen `(ℓ, r)` der Operatoren `iL_{e₇}`, `iR_{e₇}` auf ihnen
  beschrieben (numerisch bestimmt in k75/k84; hier als Daten gesetzt). Daraus folgen, als reine Ganzzahl-Arithmetik:
  `6Q = 3 − ℓ − 2r`; die Quantenzahlen einer Generation mit `ν_R` unter dem Chiralitätsprojektor `J = iL_{e₇}` (r42.1(b));
  die Anomalie-Spuren für die vier Wahlen `J = ±iL_{e₇}, ±iR_{e₇}` und der Versatz `s = −½` (r43.1); die Platz-Gewichte der
  Abweichung `Δ` und ihre Antisymmetrie (r47.1(a), (b)); die Eisenstein-Normen, deren Neuntel die Quadrate der Fourier-Nebendiagonalen
  sind (r47.1(d); die Identität `|a + bω + cω²|² = a² + b² + c² − ab − bc − ca` ist Standard und hier nicht formalisiert).
* r39 (H24a, c): `2^j ≡ (−1)^j (mod 3)` und die Zählung der Masken.

Alle Ladungen und Hyperladungen sind mit 6 multipliziert, damit sie ganzzahlig sind. Ohne Mathlib: nur Lean-Kern (`decide`, `omega`).
-/

namespace QSFormal.Ladungen

open QSFormal.Dixon

/-! ## r36: die Farbdrehung σ -/

/-- Bild des Basisvektors `eᵢ` unter σ als (Vorzeichen, Index). -/
def sigmaImg (i : Nat) : Int × Nat :=
  match i with
  | 0 => (1, 0) | 1 => (-1, 3) | 2 => (-1, 1) | 3 => (1, 2)
  | 4 => (1, 5) | 5 => (1, 6) | 6 => (1, 4) | _ => (1, 7)

/-- Komponente `k` (0..7) eines Oktonions. -/
def comp (x : O) (k : Nat) : Int :=
  match k with
  | 0 => x.p.a | 1 => x.p.b | 2 => x.p.c | 3 => x.p.d
  | 4 => x.q.a | 5 => x.q.b | 6 => x.q.c | _ => x.q.d

/-- Oktonion aus einer Komponentenfunktion. -/
def ofComp (f : Nat → Int) : O := ⟨⟨f 0, f 1, f 2, f 3⟩, ⟨f 4, f 5, f 6, f 7⟩⟩

/-- Lineare Fortsetzung einer Vorzeichen-Permutation der Basis. -/
def applySP (img : Nat → Int × Nat) (x : O) : O :=
  ofComp fun k => (List.range 8).foldl (fun acc i => acc + (if (img i).2 = k then (img i).1 * comp x i else 0)) 0

/-- Respektiert die Abbildung alle 64 Basisprodukte? -/
def respectsBasis (img : Nat → Int × Nat) : Bool :=
  (List.range 8).all fun i => (List.range 8).all fun j =>
    applySP img (O.mul (O.e i) (O.e j)) = O.mul (applySP img (O.e i)) (applySP img (O.e j))

theorem sigma_respects : respectsBasis sigmaImg = true := by decide

theorem sigma_order3 : ∀ i < 8, applySP sigmaImg (applySP sigmaImg (applySP sigmaImg (O.e i))) = O.e i := by decide

theorem sigma_fixes_e7 : applySP sigmaImg (O.e 7) = O.e 7 := by decide

/-- Fortsetzung des Zyklus `e₄ → e₅ → e₆` auf `e₁, e₂, e₃` durch eine Permutation und Vorzeichen. -/
def ext (perm : Nat × Nat × Nat) (sg : Int × Int × Int) (i : Nat) : Int × Nat :=
  match i with
  | 0 => (1, 0) | 1 => (sg.1, perm.1) | 2 => (sg.2.1, perm.2.1) | 3 => (sg.2.2, perm.2.2)
  | 4 => (1, 5) | 5 => (1, 6) | 6 => (1, 4) | _ => (1, 7)

def perms3 : List (Nat × Nat × Nat) := [(1,2,3), (1,3,2), (2,1,3), (2,3,1), (3,1,2), (3,2,1)]
def signs3 : List (Int × Int × Int) :=
  [(1,1,1), (1,1,-1), (1,-1,1), (1,-1,-1), (-1,1,1), (-1,1,-1), (-1,-1,1), (-1,-1,-1)]

/-- Die 48 Vorzeichen-Fortsetzungen, die alle Basisprodukte respektieren. -/
def goodExt : List ((Nat × Nat × Nat) × (Int × Int × Int)) :=
  (perms3.flatMap fun p => signs3.map fun s => (p, s)).filter fun ps => respectsBasis (ext ps.1 ps.2)

set_option maxHeartbeats 4000000 in
/-- r36.1(a): Genau eine der 48 Fortsetzungen ist ein Automorphismus, und zwar σ (`e₁ ↦ −e₃`, `e₂ ↦ −e₁`, `e₃ ↦ e₂`). -/
theorem unique_extension : goodExt = [((3, 1, 2), (-1, -1, 1))] := by decide

/-! ## r45: Konjugation tauscht Links- und Rechtsmultiplikation -/

/-- r45.1(a) auf der Basis: `c (e₇ · c eᵢ) = −(eᵢ · e₇)`. -/
theorem conj_left_right_basis : ∀ i < 8, O.conj (O.mul (O.e 7) (O.conj (O.e i))) = O.neg (O.mul (O.e i) (O.e 7)) := by
  decide

/-- r45.1(a) für alle `x`: `c (e₇ · c x) = −(x · e₇)`, also `c L_{e₇} c = −R_{e₇}`. -/
theorem conj_left_right (x : O) : O.conj (O.mul (O.e 7) (O.conj x)) = O.neg (O.mul x (O.e 7)) := by
  obtain ⟨⟨a, b, c, d⟩, ⟨e, f, g, h⟩⟩ := x
  simp only [O.conj, O.mul, O.neg, O.e, Q.mul, Q.conj, Q.neg, Q.sub, Q.add, O.mk.injEq, Q.mk.injEq]
  simp

/-! ## Ladungs-Sektoren (r34, r35) -/

/-- Ein Ladungs-Sektor, beschrieben durch die Vorzeichen von `iL_{e₇}` (ℓ) und `iR_{e₇}` (r) auf ihm. -/
structure Sector where
  (l r : Int)
  deriving DecidableEq, Repr

/-- Die vier Sektoren: Q = 0 (ℓ, r) = (1, 1); Q = 1/3: (−1, 1); Q = 2/3: (1, −1); Q = 1: (−1, −1). -/
def sectors : List Sector := [⟨1, 1⟩, ⟨-1, 1⟩, ⟨1, -1⟩, ⟨-1, -1⟩]

/-- `6Q = 3 − ℓ − 2r` aus `Q = ½ − (iL)/6 − (iR)/3` (r35.1(d)). -/
def q6 (s : Sector) : Int := 3 - s.l - 2 * s.r

theorem q6_values : sectors.map q6 = [0, 2, 4, 6] := by decide

/-- Farbdimension: Singulett, wenn ℓ = r (Q = 0, 1), sonst Triplett. -/
def colourDim (s : Sector) : Int := if s.l = s.r then 1 else 3

theorem colour_dims : sectors.map colourDim = [1, 3, 3, 1] := by decide

/-- Ladungskonjugation / Frame T: `Q ↦ 1 − Q`, d. h. `(ℓ, r) ↦ (−ℓ, −r)` (r34.1(d)). -/
def frameT (s : Sector) : Sector := ⟨-s.l, -s.r⟩

theorem q6_frameT : ∀ s ∈ sectors, q6 (frameT s) = 6 - q6 s := by decide

/-! ## Chiralitätsprojektor und Hyperladung (r42, r43) -/

/-- Wahl des Chiralitätsoperators `J ∈ {iL, −iL, iR, −iR}`: Vorzeichen und Seite (links = true). -/
structure Choice where
  (sign : Int) (left : Bool)
  deriving DecidableEq, Repr

def choices : List Choice := [⟨1, true⟩, ⟨-1, true⟩, ⟨1, false⟩, ⟨-1, false⟩]

/-- Liegt der Sektor im Bild von `C = ½(1 + J)`? -/
def inImage (J : Choice) (s : Sector) : Bool := J.sign * (if J.left then s.l else s.r) = 1

/-- Zustände pro Lorentz-Komponente: Sektor × `6T₃ ∈ {3, −3}`, mit Farbdimension als Vielfachheit. -/
def states : List (Sector × Int) := sectors.flatMap fun s => [(s, 3), (s, -3)]

/-- `6·Y/2 = 6Q + 6s + 6(1 − C)T₃`; der Versatz `s6 = 6s`. -/
def y6 (J : Choice) (s6 : Int) (st : Sector × Int) : Int :=
  q6 st.1 + s6 + (if inImage J st.1 then 0 else st.2)

def mult (st : Sector × Int) : Int := colourDim st.1

def trY (J : Choice) (s6 : Int) : Int := (states.map fun st => mult st * y6 J s6 st).foldl (· + ·) 0
def trY3 (J : Choice) (s6 : Int) : Int := (states.map fun st => mult st * (y6 J s6 st) ^ 3).foldl (· + ·) 0
def su2Y (J : Choice) (s6 : Int) : Int :=
  (states.map fun st => if inImage J st.1 then mult st * y6 J s6 st else 0).foldl (· + ·) 0
def su3Y (J : Choice) (s6 : Int) : Int :=
  (states.map fun st => if colourDim st.1 = 3 then mult st * y6 J s6 st else 0).foldl (· + ·) 0

/-- r43.1(b): Für jede der vier Wahlen ist `Tr Y = 16·s6 + 48`, also `Tr Y = 0` genau bei `s = −½` (`s6 = −3`). -/
theorem trY_affine : ∀ J ∈ choices, ∀ s6 : Int, trY J s6 = 16 * s6 + 48 := by
  intro J hJ s6
  simp only [choices, List.mem_cons, List.mem_nil_iff, or_false] at hJ
  rcases hJ with rfl | rfl | rfl | rfl <;>
    simp [trY, states, sectors, y6, mult, colourDim, inImage, q6] <;> omega

theorem trY_zero_iff : ∀ J ∈ choices, ∀ s6 : Int, trY J s6 = 0 ↔ s6 = -3 := by
  intro J hJ s6
  rw [trY_affine J hJ s6]
  omega

/-- r43.1(c): Bei `s = −½` sind alle vier Anomalie-Spuren genau für `J = ±iL_{e₇}` null. -/
theorem anomalies_left : ∀ J ∈ [⟨1, true⟩, ⟨-1, true⟩],
    trY J (-3) = 0 ∧ trY3 J (-3) = 0 ∧ su2Y J (-3) = 0 ∧ su3Y J (-3) = 0 := by decide

/-- r43.1(c): Für `J = ±iR_{e₇}` (in Einheiten von 6³ bzw. 6): `Tr Y³ = ±3/2` und `SU(2)²U(1) = ∓2`. -/
theorem anomalies_right :
    trY3 ⟨1, false⟩ (-3) = 324 ∧ su2Y ⟨1, false⟩ (-3) = -12 ∧
    trY3 ⟨-1, false⟩ (-3) = -324 ∧ su2Y ⟨-1, false⟩ (-3) = 12 := by decide

/-- r43.1(d): Der Frame T vertauscht die beiden zulässigen Wahlen: `inImage (−iL) s = inImage iL (T s)`. -/
theorem frameT_swaps_left : ∀ s ∈ sectors, inImage ⟨-1, true⟩ s = inImage ⟨1, true⟩ (frameT s) := by decide

/-! ## Inhalt einer Generation (r42.1(b)) -/

/-- (Farbe 1/3/−3 für 3̄, schwache Dimension, 6·Y/2, Vielfachheit) unter `J = iL_{e₇}`, `s = −½`. -/
def content : List (Int × Int × Int × Int) :=
  (states.map fun st =>
    let col : Int := if colourDim st.1 = 1 then 1 else if q6 st.1 = 4 then 3 else -3
    (col, (if inImage ⟨1, true⟩ st.1 then 2 else 1), y6 ⟨1, true⟩ (-3) st, mult st))

/-- Q_L = (3, 2, 1/6), L = (1, 2, −1/2), u^c = (3̄, 1, −2/3), d^c = (3̄, 1, 1/3), e^c = (1, 1, 1), ν^c = (1, 1, 0); jedes Dublett
erscheint mit beiden T₃-Zuständen. -/
theorem generation_content : content =
    [(1, 2, -3, 1), (1, 2, -3, 1), (-3, 1, 2, 3), (-3, 1, -4, 3), (3, 2, 1, 3), (3, 2, 1, 3), (1, 1, 6, 1), (1, 1, 0, 1)] := by
  decide

/-- Elektrische Ladung `6Q_em = 6T₃ + 6Q − 3` der Zustände: (ν, e), (d^c, u^c), (u, d), (e^c, ν^c). -/
def qem6 (st : Sector × Int) : Int := st.2 + q6 st.1 - 3

theorem charges : states.map qem6 = [0, -6, 2, -4, 4, -2, 6, 0] := by decide

/-! ## Generationen-Maske (r47) -/

/-- Platz-Gewichte der Abweichung `Δ = J_II − J_I` auf einem Sektor: `(0, r − ℓ, −2ℓ − r)`. -/
def weights (s : Sector) : Int × Int × Int := (0, s.r - s.l, -2 * s.l - s.r)

theorem weights_values :
    sectors.map weights = [(0, 0, -3), (0, 2, 1), (0, -2, -1), (0, 0, 3)] := by decide

/-- r47.1(b): Die Gewichte sind antisymmetrisch unter dem Frame T (`q ↔ 1 − q`). -/
theorem weights_antisym : ∀ s ∈ sectors,
    weights (frameT s) = (-(weights s).1, -(weights s).2.1, -(weights s).2.2) := by decide

/-- Eisenstein-Norm `a² + b² + c² − ab − bc − ca = |a + bω + cω²|²`. -/
def eisNorm (w : Int × Int × Int) : Int :=
  w.1 ^ 2 + w.2.1 ^ 2 + w.2.2 ^ 2 - w.1 * w.2.1 - w.2.1 * w.2.2 - w.2.2 * w.1

/-- r47.1(d): Quark-Maske (Sektor 2/3) Norm 3, Lepton-Maske (Sektor 0) Norm 9; die Fourier-Nebendiagonalen haben die Quadrate 3/9 = 1/3
bzw. 9/9 = 1, ihr Verhältnis ist √3. -/
theorem mask_norms : eisNorm (weights ⟨1, -1⟩) = 3 ∧ eisNorm (weights ⟨1, 1⟩) = 9 := by decide

/-! ## Zoom und Masken (r39) -/

/-- r39.1(a): `2^j ≡ 1 (mod 3)` für gerades `j`, `≡ 2` für ungerades `j`: Der Generationenkreis wechselt die Orientierung. -/
theorem pow_two_mod_three (j : Nat) : 2 ^ j % 3 = if j % 2 = 0 then 1 else 2 := by
  induction j with
  | zero => decide
  | succ n ih =>
    rw [Nat.pow_succ, Nat.mul_mod, ih]
    split <;> split <;> omega

/-- r39.1(c): Von den 63 nichtleeren Masken über 6 Bits sind 21 durch 3 teilbar (Lesart Σ: eine Generation sichtbar). -/
theorem masks_div_three : ((List.range 64).filter fun k => k ≠ 0 ∧ k % 3 = 0).length = 21 := by decide

end QSFormal.Ladungen
