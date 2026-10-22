/-!
# QAM-over-ZF

Formalisiert aus `Quantum_Sphaera_Companion_v4_8_0_source.tex`:

* „Primitive QAM predicates“ und „Primitive QAM coded relations“ (um Zeile 2854),
* „QAM closure-class schema“ und „QAM admissibility implies closure preservation“
  (beide im Companion als `axiom` geführt),
* „QAM closure-compatible readout“ (`def:qam-closure-compatible-readout`),
* „First QAM transport principle“ und „First QAM version of the OP transport principle“
  (`thm:qam-first-op-transport`),
* die Hilbert-Verschiebung der Tag-Namensräume (`def:v3370-pre-shift-shifted-tag-namespaces`,
  `lem:v3370-round-trip-inhabited-tags`).

Die Bedeutung von „admissibel“ und „Abschlussklasse“ bleibt im Companion schematisch.
Sie wird hier deshalb nicht erfunden, sondern als Parameter eines `Model` geführt: Jeder
Satz unten gilt für *jede* Wahl dieser Relationen, die die beiden Axiome erfüllt.
-/

namespace QSFormal.QAM

/-! ## Objektsorten -/

/-- Die acht QAM-Objektsorten. Im Companion sind sie ZF-Tupel `⟨k, …⟩` mit Tag `k = 0, …, 7`;
hier ein induktiver Typ über einem Nutzlasttyp `α`. -/
inductive Obj (α : Type) where
  | state (a : α)
  | layer (ℓ D : α)
  | op (ℓ₁ ℓ₂ G : α)
  | readout (ℓ W R : α)
  | branch (b B : α)
  | shell (r s T : α)
  | witness (u : α)
  | tensor (p q : α)
  deriving DecidableEq, Repr

variable {α : Type}

/-- Der Tag der ZF-Kodierung. -/
def Obj.tag : Obj α → Nat
  | .state .. => 0
  | .layer .. => 1
  | .op .. => 2
  | .readout .. => 3
  | .branch .. => 4
  | .shell .. => 5
  | .witness .. => 6
  | .tensor .. => 7

def QState (x : Obj α) : Prop := ∃ a, x = .state a
def QLayer (x : Obj α) : Prop := ∃ ℓ D, x = .layer ℓ D
def QOp (x : Obj α) : Prop := ∃ ℓ₁ ℓ₂ G, x = .op ℓ₁ ℓ₂ G
def QReadout (x : Obj α) : Prop := ∃ ℓ W R, x = .readout ℓ W R

/-- Die Prädikate sind genau die Tag-Tests: `QState x ↔ tag x = 0`. -/
theorem qState_iff_tag (x : Obj α) : QState x ↔ x.tag = 0 := by
  cases x <;> simp [QState, Obj.tag]

/-- Kein Objekt hat zwei Sorten. In ZF folgt das aus der Verschiedenheit der Tags,
hier aus der Verschiedenheit der Konstruktoren. -/
theorem not_state_and_op (x : Obj α) : ¬ (QState x ∧ QOp x) := by
  rintro ⟨⟨a, rfl⟩, ⟨_, _, _, h⟩⟩
  cases h

theorem tag_lt_eight (x : Obj α) : x.tag < 8 := by
  cases x <;> simp [Obj.tag]

/-! ## Hilbert-Verschiebung der Tag-Namensräume -/

/-- `Σ₄(k) = k + 1`. -/
def shift (k : Nat) : Nat := k + 1

/-- `B₄(a) = a − 1` auf bewohnten Tags `a ≥ 1`; auf dem reservierten Tag `0` undefiniert. -/
def back : Nat → Option Nat
  | 0 => none
  | a + 1 => some a

/-- `lem:v3370-round-trip-inhabited-tags`, erste Richtung. -/
theorem back_shift (k : Nat) : back (shift k) = some k := rfl

/-- `lem:v3370-round-trip-inhabited-tags`, zweite Richtung. -/
theorem shift_back (a : Nat) (h : 1 ≤ a) : (back a).map shift = some a := by
  cases a with
  | zero => contradiction
  | succ a => rfl

/-- Der verschobene Namensraum mit reserviertem `0` ist genau `Option Nat`:
`0` ist `none` („keine aktive Sorte“), `k + 1` ist `some k`. -/
def toShifted : Option Nat → Nat
  | none => 0
  | some k => shift k

theorem back_toShifted (o : Option Nat) : back (toShifted o) = o := by
  cases o <;> rfl

theorem toShifted_back (a : Nat) : toShifted (back a) = a := by
  cases a <;> rfl

/-! ## Transport, Abschlussklasse, Auslese -/

/-- Ein Modell der QAM-Transportschicht. `S` sind Zustandscodes, `O` Operatorcodes,
`R` Auslesecodes, `V` beobachtete Werte. Die beiden Felder `clEq_equiv` und `adm_clEq`
sind die zwei Axiome des Companion. -/
structure Model (S O R V : Type) where
  /-- `QAdmTransport(o, s, t)` -/
  admTransport : O → S → S → Prop
  /-- `QClEq(s, t)` -/
  clEq : S → S → Prop
  /-- `QRead(r, s, w)` -/
  read : R → S → V → Prop
  /-- „QAM closure-class schema“: Reflexivität, Symmetrie, Transitivität. -/
  clEq_equiv : Equivalence clEq
  /-- „QAM admissibility implies closure preservation“. -/
  adm_clEq : ∀ o s t, admTransport o s t → clEq s t

variable {S O R V T : Type} (M : Model S O R V)

/-- `def:qam-closure-compatible-readout` für einen gegebenen Faktor `J`. -/
def ClosureCompatible (r : R) (J : V → T) : Prop :=
  ∀ s t, M.clEq s t → ∀ w₁ w₂, M.read r s w₁ → M.read r t w₂ → J w₁ = J w₂

/-- „First QAM transport principle“. -/
theorem first_transport_principle {o : O} {s t : S} {r : R} {J : V → T}
    (hJ : ClosureCompatible M r J) (h : M.admTransport o s t) :
    M.clEq s t ∧ ∀ w₁ w₂, M.read r s w₁ → M.read r t w₂ → J w₁ = J w₂ :=
  ⟨M.adm_clEq o s t h, hJ s t (M.adm_clEq o s t h)⟩

/-- `thm:qam-first-op-transport`: die fünf Transporte
`s_in → s₂ → s₃ → s₄`, `s_in → t_fwd`, `s_in → t_bwd` legen alle sechs Zustände in die
Abschlussklasse von `s_in`. -/
theorem first_op_transport {s_in s₂ s₃ s₄ t_fwd t_bwd : S} {o₂ o₃ o₄ o_fwd o_bwd : O}
    (h₂ : M.admTransport o₂ s_in s₂) (h₃ : M.admTransport o₃ s₂ s₃)
    (h₄ : M.admTransport o₄ s₃ s₄) (hf : M.admTransport o_fwd s_in t_fwd)
    (hb : M.admTransport o_bwd s_in t_bwd) :
    ∀ x ∈ [s_in, s₂, s₃, s₄, t_fwd, t_bwd], M.clEq s_in x := by
  have e := M.clEq_equiv
  have c₂ := M.adm_clEq _ _ _ h₂
  have c₃ := e.trans c₂ (M.adm_clEq _ _ _ h₃)
  have c₄ := e.trans c₃ (M.adm_clEq _ _ _ h₄)
  intro x hx
  simp only [List.mem_cons, List.not_mem_nil, or_false] at hx
  rcases hx with rfl | rfl | rfl | rfl | rfl | rfl
  · exact e.refl _
  · exact c₂
  · exact c₃
  · exact c₄
  · exact M.adm_clEq _ _ _ hf
  · exact M.adm_clEq _ _ _ hb

/-- Die Verallgemeinerung, auf der `thm:qam-first-op-transport` eigentlich beruht:
jede endliche Kette admissibler Transporte bleibt in einer Abschlussklasse. -/
inductive Chain : S → S → Prop
  | refl (s : S) : Chain s s
  | step {s t u : S} (o : O) : M.admTransport o s t → Chain t u → Chain s u

theorem chain_clEq {s u : S} (h : Chain M s u) : M.clEq s u := by
  induction h with
  | refl s => exact M.clEq_equiv.refl s
  | step o h _ ih => exact M.clEq_equiv.trans (M.adm_clEq _ _ _ h) ih

/-- Folgerung zweiter Teil: Ausleser am Anfang und Ende einer Kette stimmen nach `J` überein. -/
theorem chain_readout {s u : S} {r : R} {J : V → T} (hJ : ClosureCompatible M r J)
    (h : Chain M s u) {w₁ w₂ : V} (h₁ : M.read r s w₁) (h₂ : M.read r u w₂) : J w₁ = J w₂ :=
  hJ s u (chain_clEq M h) w₁ w₂ h₁ h₂

end QSFormal.QAM
