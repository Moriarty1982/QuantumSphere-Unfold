/-!
# Dixon-Ablage, Triality-Form und Generationen-Tripel

Formalisiert aus `Quantum_Sphaera_Companion_v4_8_0_source.tex` (Stand v4.9.0-r32) und `llm/Pruefung_Dixon_Ablage.md`
(Kernkarte K77), dazu die algebraischen Kerne von Theoremlet v4.9.0-r26.1 und v4.9.0-r32.1.

* Oktonionen über `Int` nach derselben Cayley–Dickson-Formel wie `llm/k22_oktonion_triplett.py`:
  `(p,q)(r,s) = (pr − s̄q, sp + q r̄)`. Triality-Form `t x y z = Re((xy)z)`.
* Triality-S₃ (v4.8.0-r14): `t` ist zyklisch invariant und invariant unter `(x,y,z) ↦ (x̄,z̄,ȳ)`.
* K77.4: Von den 24 Vorzeichen-Permutationen der drei Plätze in SO(3) lassen genau die 12 die Form invariant, die eine
  gerade Permutation mit einer geraden Zahl von Vorzeichenwechseln sind (die Standarddarstellung der Tetraedergruppe A₄;
  der abstrakte Isomorphismus zu A₄ wird hier nicht formalisiert).
* K77.1/K77.3: Dixon-Kanäle `(a,b,c) ∈ 2 × 4 × 8` (64), Bit `32a + 8b + c`; das Tripel `(Im ℍ) ⊗ 𝕆` belegt 24 Bits,
  die farbigen Zustände (c ∈ e₄,e₅,e₆) eine 9-Bit-Teilmaske.
* r26.1/r32.1: Die Norm-Invarianten bis Grad 6 sind linear in `e₂`; auf der reellen Achse ist `V_R` linear in `e₃`.
  Formalisiert sind die Polynom-Identitäten und das Vorzeichen des 2×2-Hauptminors; der Schritt „Hauptminor < 0 ⇒
  Sattelpunkt“ (Koordinatenwechsel, Kongruenz der Hessematrix) ist Analysis und hier nicht formalisiert.
* K77.6, nur unter Annahme: Wirkt `J_B` auf der Ablage als Konjugation des ℂ-Faktors, bleibt die Menge der aktiven
  Kanäle (die Maske) erhalten. Ob `J_B` so wirkt, ist eine Lesart, keine Folgerung.

Ohne Mathlib: nur Lean-Kern (`grind`, `decide`).
-/

namespace QSFormal.Dixon

/-! ## Quaternionen und Oktonionen über `Int` -/

structure Q where
  (a b c d : Int)
  deriving DecidableEq, Repr

namespace Q
def mul (p r : Q) : Q :=
  ⟨p.a*r.a - p.b*r.b - p.c*r.c - p.d*r.d, p.a*r.b + p.b*r.a + p.c*r.d - p.d*r.c,
   p.a*r.c - p.b*r.d + p.c*r.a + p.d*r.b, p.a*r.d + p.b*r.c - p.c*r.b + p.d*r.a⟩
def conj (p : Q) : Q := ⟨p.a, -p.b, -p.c, -p.d⟩
def sub (p r : Q) : Q := ⟨p.a - r.a, p.b - r.b, p.c - r.c, p.d - r.d⟩
def add (p r : Q) : Q := ⟨p.a + r.a, p.b + r.b, p.c + r.c, p.d + r.d⟩
def neg (p : Q) : Q := ⟨-p.a, -p.b, -p.c, -p.d⟩
end Q

/-- Oktonion als Paar `(p, q)` von Quaternionen; Basis `e₀..e₃` in `p`, `e₄..e₇` in `q` (wie k22). -/
structure O where
  (p q : Q)
  deriving DecidableEq, Repr

namespace O
def mul (x y : O) : O :=
  ⟨Q.sub (Q.mul x.p y.p) (Q.mul (Q.conj y.q) x.q), Q.add (Q.mul y.q x.p) (Q.mul x.q (Q.conj y.p))⟩
def conj (x : O) : O := ⟨Q.conj x.p, Q.neg x.q⟩
def neg (x : O) : O := ⟨Q.neg x.p, Q.neg x.q⟩
def re (x : O) : Int := x.p.a
/-- Basisvektor `eᵢ`, `i = 0..7`. -/
def e (i : Nat) : O :=
  ⟨⟨if i = 0 then 1 else 0, if i = 1 then 1 else 0, if i = 2 then 1 else 0, if i = 3 then 1 else 0⟩,
   ⟨if i = 4 then 1 else 0, if i = 5 then 1 else 0, if i = 6 then 1 else 0, if i = 7 then 1 else 0⟩⟩
end O

/-- Triality-Form `t(x,y,z) = Re((xy)z)`. -/
def t (x y z : O) : Int := (O.mul (O.mul x y) z).re

/-- Konjugation ist ein Anti-Automorphismus: `(xy)* = y* x*`. -/
theorem conj_mul (x y : O) : O.conj (O.mul x y) = O.mul (O.conj y) (O.conj x) := by
  obtain ⟨⟨a0,a1,a2,a3⟩,⟨a4,a5,a6,a7⟩⟩ := x
  obtain ⟨⟨b0,b1,b2,b3⟩,⟨b4,b5,b6,b7⟩⟩ := y
  simp only [O.conj, O.mul, Q.mul, Q.sub, Q.add, Q.conj, Q.neg, O.mk.injEq, Q.mk.injEq]
  refine ⟨⟨?_, ?_, ?_, ?_⟩, ⟨?_, ?_, ?_, ?_⟩⟩ <;> grind

/-- … und kein Automorphismus: `(e₁e₂)* ≠ e₁* e₂*`. -/
theorem conj_not_hom : O.conj (O.mul (O.e 1) (O.e 2)) ≠ O.mul (O.conj (O.e 1)) (O.conj (O.e 2)) := by decide

/-! ## Triality-S₃ (v4.8.0-r14) -/

theorem t_cyc (x y z : O) : t y z x = t x y z := by
  obtain ⟨⟨a0,a1,a2,a3⟩,⟨a4,a5,a6,a7⟩⟩ := x
  obtain ⟨⟨b0,b1,b2,b3⟩,⟨b4,b5,b6,b7⟩⟩ := y
  obtain ⟨⟨c0,c1,c2,c3⟩,⟨c4,c5,c6,c7⟩⟩ := z
  simp only [t, O.mul, O.re, Q.mul, Q.sub, Q.add, Q.conj]
  grind

theorem t_conjSwap (x y z : O) : t (O.conj x) (O.conj z) (O.conj y) = t x y z := by
  obtain ⟨⟨a0,a1,a2,a3⟩,⟨a4,a5,a6,a7⟩⟩ := x
  obtain ⟨⟨b0,b1,b2,b3⟩,⟨b4,b5,b6,b7⟩⟩ := y
  obtain ⟨⟨c0,c1,c2,c3⟩,⟨c4,c5,c6,c7⟩⟩ := z
  simp only [t, O.mul, O.re, O.conj, Q.mul, Q.sub, Q.add, Q.conj, Q.neg]
  grind

/-! ## Vorzeichen-Permutationen der Plätze (K77.4) -/

/-- Signierte Platz-Permutation: neuer Platz `k` = `s k · (alter Platz π k)`. -/
structure SP where
  (p0 p1 p2 : Nat)
  (s0 s1 s2 : Int)
  deriving DecidableEq, Repr

namespace SP
def pick (k : Nat) (x y z : O) : O := if k = 0 then x else if k = 1 then y else z
def smul (s : Int) (x : O) : O := if s = 1 then x else O.neg x
def act (g : SP) (x y z : O) : O × O × O :=
  (smul g.s0 (pick g.p0 x y z), smul g.s1 (pick g.p1 x y z), smul g.s2 (pick g.p2 x y z))
/-- Die Form ist invariant unter `g`. -/
def Inv (g : SP) : Prop := ∀ x y z : O, t (g.act x y z).1 (g.act x y z).2.1 (g.act x y z).2.2 = t x y z
/-- Invarianz auf allen Basis-Tripeln (entscheidbar). -/
def invOnBasis (g : SP) : Bool :=
  (List.range 8).all fun i => (List.range 8).all fun j => (List.range 8).all fun k =>
    t (g.act (O.e i) (O.e j) (O.e k)).1 (g.act (O.e i) (O.e j) (O.e k)).2.1 (g.act (O.e i) (O.e j) (O.e k)).2.2
      == t (O.e i) (O.e j) (O.e k)
def isEvenPerm (g : SP) : Bool :=
  (g.p0, g.p1, g.p2) == (0, 1, 2) || (g.p0, g.p1, g.p2) == (1, 2, 0) || (g.p0, g.p1, g.p2) == (2, 0, 1)
def det (g : SP) : Int := (if isEvenPerm g then 1 else -1) * g.s0 * g.s1 * g.s2
end SP

def perms : List (Nat × Nat × Nat) := [(0,1,2), (1,2,0), (2,0,1), (0,2,1), (2,1,0), (1,0,2)]
def signs : List (Int × Int × Int) :=
  [(1,1,1), (1,1,-1), (1,-1,1), (1,-1,-1), (-1,1,1), (-1,1,-1), (-1,-1,1), (-1,-1,-1)]
/-- Alle Vorzeichen-Permutationen mit Determinante `+1`, also die in SO(3) = Aut(ℍ) auf `i, j, k`. -/
def so3 : List SP :=
  (perms.flatMap fun p => signs.map fun s => SP.mk p.1 p.2.1 p.2.2 s.1 s.2.1 s.2.2).filter (fun g => g.det == 1)
/-- Gerade Permutation und gerade Zahl von Vorzeichenwechseln. -/
def a4 : List SP := so3.filter SP.isEvenPerm

theorem so3_length : so3.length = 24 := by decide
theorem a4_length : a4.length = 12 := by decide

theorem inv_invOnBasis {g : SP} (h : g.Inv) : g.invOnBasis = true := by
  simp only [SP.invOnBasis, List.all_eq_true, beq_iff_eq]
  intro i _ j _ k _
  exact h _ _ _

/-- Auf den Basis-Tripeln entscheidbar: außerhalb von `a4` ist die Form nicht invariant. -/
theorem outside_fails : ∀ g ∈ so3, SP.isEvenPerm g = false → SP.invOnBasis g = false := by decide

/-- Die 12 Elemente außerhalb von `a4` lassen die Form nicht invariant. -/
theorem not_inv_outside : ∀ g ∈ so3, SP.isEvenPerm g = false → ¬ g.Inv := by
  intro g hg hodd hinv
  have h1 := inv_invOnBasis hinv
  rw [outside_fails g hg hodd] at h1
  exact Bool.false_ne_true h1

theorem a4_eq : a4 =
    [⟨0,1,2, 1,1,1⟩, ⟨0,1,2, 1,-1,-1⟩, ⟨0,1,2, -1,1,-1⟩, ⟨0,1,2, -1,-1,1⟩,
     ⟨1,2,0, 1,1,1⟩, ⟨1,2,0, 1,-1,-1⟩, ⟨1,2,0, -1,1,-1⟩, ⟨1,2,0, -1,-1,1⟩,
     ⟨2,0,1, 1,1,1⟩, ⟨2,0,1, 1,-1,-1⟩, ⟨2,0,1, -1,1,-1⟩, ⟨2,0,1, -1,-1,1⟩] := by decide

/-- Die 12 Elemente von `a4` lassen die Form invariant. -/
theorem inv_a4 : ∀ g ∈ a4, g.Inv := by
  intro g hg
  rw [a4_eq] at hg
  simp only [List.mem_cons, List.not_mem_nil, or_false] at hg
  rcases hg with rfl | rfl | rfl | rfl | rfl | rfl | rfl | rfl | rfl | rfl | rfl | rfl <;>
  · intro x y z
    obtain ⟨⟨a0,a1,a2,a3⟩,⟨a4,a5,a6,a7⟩⟩ := x
    obtain ⟨⟨b0,b1,b2,b3⟩,⟨b4,b5,b6,b7⟩⟩ := y
    obtain ⟨⟨c0,c1,c2,c3⟩,⟨c4,c5,c6,c7⟩⟩ := z
    simp (config := { decide := true }) only [SP.act, SP.pick, SP.smul, t, O.mul, O.re, O.neg, Q.mul, Q.sub, Q.add,
      Q.conj, Q.neg, ite_true, ite_false]
    all_goals grind

/-- K77.4 zusammengefasst: Unter den 24 Vorzeichen-Permutationen in SO(3) sind genau die aus `a4` Symmetrien der
Triality-Form. -/
theorem inv_iff (g : SP) (hg : g ∈ so3) : g.Inv ↔ g ∈ a4 := by
  constructor
  · intro h
    cases he : SP.isEvenPerm g
    · exact absurd h (not_inv_outside g hg he)
    · simp only [a4, List.mem_filter]; exact ⟨hg, he⟩
  · exact inv_a4 g

/-! ## Dixon-Ablage HS(6) (K77.1, K77.3) -/

/-- Kanal `(a, b, c)`: `a ∈ {0,1}` (ℂ), `b ∈ {0..3}` (ℍ), `c ∈ {0..7}` (𝕆); Bit `32a + 8b + c` (wie k71). -/
def bit (a b c : Nat) : Nat := 32 * a + 8 * b + c
def channels : List Nat :=
  (List.range 2).flatMap fun a => (List.range 4).flatMap fun b => (List.range 8).map fun c => bit a b c

theorem channels_length : channels.length = 64 := by decide
theorem channels_eq_range : channels = List.range 64 := by decide

def maskOf (l : List Nat) : Nat := l.foldl (fun m i => m ||| (1 <<< i)) 0
def popcount (m : Nat) : Nat := ((List.range 64).filter fun i => m.testBit i).length

/-- Generationen-Tripel `(Im ℍ) ⊗ 𝕆`: `a = 0`, `b ∈ {i, j, k}`, `c` beliebig. -/
def tripleMask : Nat := maskOf ([1, 2, 3].flatMap fun b => (List.range 8).map fun c => bit 0 b c)
/-- Farbige Zustände: `c ∈ {e₄, e₅, e₆}` (Rahmen `u = e₇`). -/
def colourMask : Nat := maskOf ([1, 2, 3].flatMap fun b => [4, 5, 6].map fun c => bit 0 b c)

theorem tripleMask_popcount : popcount tripleMask = 24 := by decide
theorem colourMask_popcount : popcount colourMask = 9 := by decide
theorem colour_sub_triple : colourMask &&& tripleMask = colourMask := by decide
theorem tripleMask_lt : tripleMask < 2 ^ 64 := by decide

/-! ### Nur unter Annahme (K77.6): `J_B` als Konjugation des ℂ-Faktors -/

/-- Konjugation des ℂ-Faktors auf einem Trägervektor: Kanäle mit `a = 1` wechseln das Vorzeichen. -/
def conjC (v : Nat → Int) : Nat → Int := fun i => if i / 32 = 1 then -v i else v i

theorem conjC_support (v : Nat → Int) (i : Nat) : conjC v i ≠ 0 ↔ v i ≠ 0 := by
  unfold conjC; split <;> omega

theorem conjC_invol (v : Nat → Int) : conjC (conjC v) = v := by
  funext i; unfold conjC; split <;> simp

/-! ## Algebraischer Kern von Theoremlet v4.9.0-r26.1 und v4.9.0-r32.1 -/

section r26
variable (n1 n2 n3 : Int)
/-- `x_k = n_k²`, `S = Σx`, `e₂ = Σ_{i<j} x_i x_j`, `P = n₁n₂n₃`. -/
def S := n1^2 + n2^2 + n3^2
def e2x := n1^2*n2^2 + n1^2*n3^2 + n2^2*n3^2
def P := n1*n2*n3
def Qn := n1^4 + n2^4 + n3^4
def Hn := n1^6 + n2^6 + n3^6

theorem Q_eq : Qn n1 n2 n3 = (S n1 n2 n3)^2 - 2 * e2x n1 n2 n3 := by simp only [Qn, S, e2x]; grind
theorem H_eq : Hn n1 n2 n3 = (S n1 n2 n3)^3 - 3 * S n1 n2 n3 * e2x n1 n2 n3 + 3 * (P n1 n2 n3)^2 := by
  simp only [Hn, S, e2x, P]; grind
theorem SQ_eq : S n1 n2 n3 * Qn n1 n2 n3 = (S n1 n2 n3)^3 - 2 * S n1 n2 n3 * e2x n1 n2 n3 := by
  simp only [Qn, S, e2x]; grind

/-- r26.1: Jedes Norm-Potential bis Grad 6 ist `A(S,P) + e₂·(b₀ + b₁S)`. -/
theorem r26_linear_in_e2 (α β γ δ₁ δ₂ δ₃ κ l μ : Int) :
    α * S n1 n2 n3 + β * (S n1 n2 n3)^2 + γ * Qn n1 n2 n3 + δ₁ * (S n1 n2 n3)^3 + δ₂ * (S n1 n2 n3 * Qn n1 n2 n3)
      + δ₃ * Hn n1 n2 n3 + κ * P n1 n2 n3 + l * (S n1 n2 n3 * P n1 n2 n3) + μ * (P n1 n2 n3)^2
    = (α * S n1 n2 n3 + (β + γ) * (S n1 n2 n3)^2 + (δ₁ + δ₂ + δ₃) * (S n1 n2 n3)^3 + κ * P n1 n2 n3
        + l * (S n1 n2 n3 * P n1 n2 n3) + (μ + 3 * δ₃) * (P n1 n2 n3)^2)
      + e2x n1 n2 n3 * (-2 * γ + (-2 * δ₂ - 3 * δ₃) * S n1 n2 n3) := by
  simp only [Qn, S, e2x, P, Hn]; grind
end r26

section r32
variable (n1 n2 n3 : Int)
/-- Elementarsymmetrische Polynome der Normen. -/
def E1 := n1 + n2 + n3
def E2 := n1*n2 + n1*n3 + n2*n3
def E3 := n1*n2*n3

theorem S_axis : n1^2 + n2^2 + n3^2 = (E1 n1 n2 n3)^2 - 2 * E2 n1 n2 n3 := by simp only [E1, E2]; grind
theorem Q_axis : n1^4 + n2^4 + n3^4
    = (E1 n1 n2 n3)^4 - 4 * (E1 n1 n2 n3)^2 * E2 n1 n2 n3 + 2 * (E2 n1 n2 n3)^2 + 4 * E1 n1 n2 n3 * E3 n1 n2 n3 := by
  simp only [E1, E2, E3]; grind

/-- r32.1: Auf der reellen Achse ist `V_R = A(e₁,e₂) + e₃·(4γe₁ − κ)`. -/
theorem r32_linear_in_e3 (β γ κ μ ν l : Int) :
    -(n1^2 + n2^2 + n3^2) + β * (n1^2 + n2^2 + n3^2)^2 + γ * (n1^4 + n2^4 + n3^4) - κ * (n1*n2*n3)
      - μ * (n1 + n2 + n3) - ν * (n1^2 + n2^2 + n3^2) - l * (n1 + n2 + n3)^2
    = (-(1 + ν) * ((E1 n1 n2 n3)^2 - 2 * E2 n1 n2 n3) + β * ((E1 n1 n2 n3)^2 - 2 * E2 n1 n2 n3)^2
        + γ * ((E1 n1 n2 n3)^4 - 4 * (E1 n1 n2 n3)^2 * E2 n1 n2 n3 + 2 * (E2 n1 n2 n3)^2)
        - μ * E1 n1 n2 n3 - l * (E1 n1 n2 n3)^2)
      + E3 n1 n2 n3 * (4 * γ * E1 n1 n2 n3 - κ) := by
  simp only [E1, E2, E3]; grind
end r32

/-- Hauptminor `[[h, b], [b, 0]]`: Determinante `−b² < 0` für `b ≠ 0` (Kern des Sattel-Arguments). -/
theorem minor_neg (h b : Int) (hb : b ≠ 0) : h * 0 - b * b < 0 := by
  have : 0 < b * b := by
    rcases Int.lt_or_gt_of_ne hb with hlt | hgt
    · have := Int.mul_pos (Int.neg_pos.mpr hlt) (Int.neg_pos.mpr hlt); simpa [Int.neg_mul_neg] using this
    · exact Int.mul_pos hgt hgt
  omega

end QSFormal.Dixon
