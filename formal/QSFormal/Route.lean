import QSFormal.QAM

/-!
# Routenabhängige Admissibilität

Lesart der zweiseitigen Tensorschreibweise `^A_B 𝒯^i_j` (`def:two-sided-structural-tensor-interface`)
als Routing: die Vorderseite `^A_B` nennt, von welchem Frame nach welchem ausgelesen wird,
die Rückseite die Struktur, die transportiert wird. Admissibilität ist dann keine einzelne
Relation, sondern eine pro Route: `model a b` ist ein eigenes QAM-Modell, und auf
verschiedenen Routen dürfen verschiedene Definitionen stehen, auch die beiden trivialen
aus `QSFormal.Models`.

Was die Routen zusammenhält, ist ein Kompositionsgesetz. Es steht nicht im Companion und
ist hier eine Annahme: Wer admissibel von `a` nach `b` und dann von `b` nach `c`
transportiert, transportiert admissibel von `a` nach `c`.
-/

namespace QSFormal.Route

open QSFormal.QAM

structure RoutedModel (F S O R V : Type) where
  /-- Das QAM-Modell der Route `a → b`. -/
  model : F → F → Model S O R V
  /-- Kompositionsgesetz. -/
  comp : ∀ {a b c : F} {o o' : O} {s t u : S},
    (model a b).admTransport o s t → (model b c).admTransport o' t u →
      ∃ o'', (model a c).admTransport o'' s u

variable {F S O R V : Type} (RM : RoutedModel F S O R V)

/-- Ein Weg durch die Frames mit mindestens einem Schritt, jeder Schritt admissibel auf
seiner eigenen Route. -/
inductive Path : F → S → F → S → Prop
  | hop {a b : F} {o : O} {s t : S} : (RM.model a b).admTransport o s t → Path a s b t
  | cons {a b c : F} {o : O} {s t u : S} :
      (RM.model a b).admTransport o s t → Path b t c u → Path a s c u

/-- Ein Weg über beliebig viele Frames ist admissibel auf der direkten Route. -/
theorem path_admissible {a c : F} {s u : S} (h : Path RM a s c u) :
    ∃ o, (RM.model a c).admTransport o s u := by
  induction h with
  | hop h => exact ⟨_, h⟩
  | cons h _ ih =>
    obtain ⟨_, h'⟩ := ih
    exact RM.comp h h'

theorem path_clEq {a c : F} {s u : S} (h : Path RM a s c u) : (RM.model a c).clEq s u := by
  obtain ⟨o, h'⟩ := path_admissible RM h
  exact (RM.model a c).adm_clEq o s u h'

/-- Folgerung für Schleifen: ein Umlauf `a → … → a` bleibt in einer Klasse der Route
`a → a`. Unter dem Kompositionsgesetz kann eine Holonomie also nur sichtbar werden, wenn
die Klassen von `model a a` selbst gröber als die Gleichheit sind; als Klassenwechsel
zeigt sie sich nie. -/
theorem loop_clEq {a : F} {s u : S} (h : Path RM a s a u) : (RM.model a a).clEq s u :=
  path_clEq RM h

end QSFormal.Route
