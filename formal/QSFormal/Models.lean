import QSFormal.QAM

/-!
# Zwei triviale Modelle der QAM-Axiome

Die beiden Companion-Axiome („closure-class schema“, „admissibility implies closure
preservation“) legen „admissibel“ nicht fest. Beide Extreme erfüllen sie:

* `totalModel`: jeder Transport ist admissibel, alle Zustände in einer Klasse;
* `emptyModel`: kein Transport ist admissibel, die Klassen sind die Gleichheit.

Alle Sätze aus `QSFormal.QAM` gelten in beiden. Was sie unterscheidet, ist allein, welche
Auslesen abschlussverträglich sind: im totalen Modell nur solche, die nach `J` nichts
unterscheiden, im leeren Modell jede, die pro Zustand eindeutig ist.
-/

namespace QSFormal.QAM

variable (S O R V : Type) (read : R → S → V → Prop)

def totalModel : Model S O R V where
  admTransport _ _ _ := True
  clEq _ _ := True
  read := read
  clEq_equiv := ⟨fun _ => trivial, fun _ => trivial, fun _ _ => trivial⟩
  adm_clEq _ _ _ _ := trivial

def emptyModel : Model S O R V where
  admTransport _ _ _ := False
  clEq := Eq
  read := read
  clEq_equiv := ⟨fun _ => rfl, fun h => h.symm, fun h₁ h₂ => h₁.trans h₂⟩
  adm_clEq _ _ _ h := h.elim

variable {S O R V read} {T : Type}

theorem total_admissible (o : O) (s t : S) : (totalModel S O R V read).admTransport o s t :=
  trivial

/-- Im totalen Modell ist eine Auslese genau dann abschlussverträglich, wenn sie nach `J`
überhaupt nichts unterscheidet. -/
theorem total_closureCompatible_iff (r : R) (J : V → T) :
    ClosureCompatible (totalModel S O R V read) r J ↔
      ∀ s t w₁ w₂, read r s w₁ → read r t w₂ → J w₁ = J w₂ :=
  ⟨fun h s t => h s t trivial, fun h s t _ => h s t⟩

/-- Im leeren Modell verbindet eine Kette nur einen Zustand mit sich selbst. -/
theorem empty_chain {s u : S} (h : Chain (emptyModel S O R V read) s u) : s = u := by
  cases h with
  | refl => rfl
  | step _ h _ => exact h.elim

/-- Im leeren Modell ist eine Auslese genau dann abschlussverträglich, wenn sie jedem
Zustand nach `J` einen eindeutigen Wert gibt. -/
theorem empty_closureCompatible_iff (r : R) (J : V → T) :
    ClosureCompatible (emptyModel S O R V read) r J ↔
      ∀ s w₁ w₂, read r s w₁ → read r s w₂ → J w₁ = J w₂ := by
  constructor
  · intro h s
    exact h s s rfl
  · intro h s t hst w₁ w₂ h₁ h₂
    subst hst
    exact h s w₁ w₂ h₁ h₂

end QSFormal.QAM
