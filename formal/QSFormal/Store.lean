import QSFormal.QAM

/-!
# QAM-Store mit MML-Befehlen und MMA-Übergangssemantik

Formalisiert aus `Quantum_Sphaera_Companion_v4_8_0_source.tex`:
`def:qam-store-state`, `def:mml-store-instructions`, `def:mma-store-transition`,
`prop:qam-store-snapshot-stability` und die Regel, dass kein Befehl ein Zertifikat
„by syntax alone“ erzeugt.

Vereinfachungen gegenüber dem Companion: Adressen sind natürliche Zahlen, das Ledger
trägt keine Zeiger (also gibt es keine Zeigerbedingung), `CLONE` und `MERGE_CAND`
fehlen, weil sie Verzweigungen über mehrere Stores brauchen.
-/

namespace QSFormal.Store

open QSFormal.QAM

abbrev Addr := Nat

/-- Der mathematische Inhalt eines Stores: Objekte `𝒪` an Adressen `𝒜` und Relationen `ℛ`. -/
structure Content where
  objs : List (Addr × Obj Nat)
  links : List (Addr × Addr)

def Content.addrs (c : Content) : List Addr := c.objs.map Prod.fst

/-- Jede Relation benutzt gespeicherte Adressen. -/
def Content.linksOk (c : Content) : Bool :=
  c.links.all fun (a, b) => c.addrs.contains a && c.addrs.contains b

inductive Instr where
  | store (a : Addr) (x : Obj Nat)
  | link (a b : Addr)
  | snapshot
  | rollback (k : Nat)
  | scrub
  | export (a : Addr)

inductive Status where
  | cont | halt | reject | guard
  deriving DecidableEq, Repr

structure Entry where
  instr : Instr
  status : Status

/-- `def:qam-store-state`: Inhalt, Guard-Register `𝒢`, Ledger `ℒ`, dazu die Snapshots. -/
structure Store where
  content : Content
  guards : List (Content → Bool)
  snapshots : List Content
  ledger : List Entry

/-- Admissibel: Relationen auf gespeicherten Adressen und alle Guards erfüllt. -/
def admissible (s : Store) : Bool :=
  s.content.linksOk && s.guards.all (· s.content)

/-- Der rohe Effekt eines Befehls, bevor die Guards geprüft werden. `none` heißt: nicht
anwendbar (etwa Rollback auf einen Snapshot, den es nicht gibt). -/
def raw (s : Store) : Instr → Option Store
  | .store a x => some { s with content.objs := (a, x) :: s.content.objs.filter (·.1 ≠ a) }
  | .link a b => some { s with content.links := (a, b) :: s.content.links }
  | .snapshot => some { s with snapshots := s.content :: s.snapshots }
  | .rollback k => s.snapshots[k]?.map fun c => { s with content := c }
  | .scrub => some s
  | .export a => if s.content.addrs.contains a then some s else none

/-- `def:mma-store-transition`. Ein Ergebnis, das einen Guard verletzt, wird nicht
übernommen: der alte Inhalt bleibt, Status `guard`, und das Ledger hält den Defekt fest. -/
def exec (s : Store) (i : Instr) : Store × Status :=
  match raw s i with
  | none => ({ s with ledger := ⟨i, .reject⟩ :: s.ledger }, .reject)
  | some s' =>
    if admissible s' then ({ s' with ledger := ⟨i, .cont⟩ :: s'.ledger }, .cont)
    else ({ s with ledger := ⟨i, .guard⟩ :: s.ledger }, .guard)

/-- Admissibilität hängt nicht vom Ledger ab. -/
theorem admissible_ledger (s : Store) (l : List Entry) :
    admissible { s with ledger := l } = admissible s := rfl

/-- Guard-Treue: ein Schritt mit Status `cont` endet in einem admissiblen Store. -/
theorem exec_cont_admissible {s : Store} {i : Instr} (h : (exec s i).2 = .cont) :
    admissible (exec s i).1 = true := by
  cases hr : raw s i with
  | none => simp [exec, hr] at h
  | some s' =>
    by_cases ha : admissible s' = true
    · simp only [exec, hr, ha, ↓reduceIte]; exact ha
    · simp [exec, hr, ha] at h

/-- Invariante: aus einem admissiblen Store führt kein Befehl heraus. -/
theorem exec_preserves {s : Store} (hs : admissible s = true) (i : Instr) :
    admissible (exec s i).1 = true := by
  cases hr : raw s i with
  | none => simp only [exec, hr]; exact hs
  | some s' =>
    by_cases ha : admissible s' = true
    · simp only [exec, hr, ha, ↓reduceIte]; exact ha
    · simp only [exec, hr, ha, Bool.false_eq_true, ↓reduceIte]; exact hs

/-- Lineage-Treue: jeder Schritt legt vorn im Ledger einen Eintrag mit Befehl und Status an. -/
theorem exec_logs (s : Store) (i : Instr) :
    (exec s i).1.ledger.head? = some ⟨i, (exec s i).2⟩ := by
  cases hr : raw s i with
  | none => simp [exec, hr]
  | some s' =>
    by_cases ha : admissible s' = true
    · simp [exec, hr, ha]
    · simp [exec, hr, ha]

/-- Ein Programm ist eine Befehlsfolge. -/
def run (s : Store) : List Instr → Store
  | [] => s
  | i :: is => run (exec s i).1 is

theorem run_preserves {s : Store} (hs : admissible s = true) (p : List Instr) :
    admissible (run s p) = true := by
  induction p generalizing s with
  | nil => exact hs
  | cons i is ih => exact ih (exec_preserves hs i)

/-- Ein Rollback stellt einen gespeicherten Inhalt exakt wieder her. -/
theorem rollback_restores {s : Store} {k : Nat} {c : Content} (hk : s.snapshots[k]? = some c)
    (hc : admissible { s with content := c } = true) :
    (exec s (.rollback k)).1.content = c := by
  simp [exec, raw, hk, hc]

/-! ## Zertifikate

Im Companion wird ein `CertificateFinal` „an actual theorematic certificate only when the
previously stated mathematical trigger conditions are discharged outside the machine
interface“. In Lean ist das keine Absichtserklärung, sondern eine Typfrage: ein Zertifikat
für `P` enthält einen Beweis von `P`. -/

structure Certificate (P : Prop) : Prop where
  proof : P

/-- Was die Maschine liefern kann: ein Kandidat mit Bezeichnung, aber ohne Beweis. -/
structure CertificateFinal (P : Prop) where
  label : String

/-- Aus einem Kandidaten wird ein Zertifikat nur mit einem Beweis, der von außen kommt. -/
theorem CertificateFinal.promote {P : Prop} (_ : CertificateFinal P) (h : P) : Certificate P :=
  ⟨h⟩

/-- Ein Kandidat gibt es für jede Aussage, auch für falsche. -/
def anyCandidate (P : Prop) : CertificateFinal P := ⟨"candidate"⟩

/-- Kein falsches Zertifikat: für `False` gibt es keines, gleich welche Befehle liefen. -/
theorem no_false_certificate : ¬ Certificate False :=
  fun c => c.proof

end QSFormal.Store
