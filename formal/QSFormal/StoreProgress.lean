import QSFormal.Store

/-!
# Fortschritt, Atomarität und Lineage der MMA

Ergänzt `QSFormal.Store` um die Aussagen, die man von einer operationalen Semantik neben der
Erhaltung (`exec_preserves`) erwartet:

* **kein Hängenbleiben:** kein Schritt endet mit Status `halt`;
* **genaue Statuskennzeichnung:** `cont` genau dann, wenn der rohe Effekt definiert und
  admissibel ist;
* **Atomarität:** ein abgelehnter oder vom Guard gestoppter Schritt ändert weder Inhalt noch
  Snapshots noch Guards;
* **Fortschritt** für die Befehle, die einen admissiblen Inhalt nicht verändern;
* **Lineage-Vollständigkeit:** jedes Programm verlängert das Ledger um genau seine Länge.
-/

namespace QSFormal.Store

/-- Der rohe Effekt lässt das Ledger unberührt. -/
theorem raw_ledger {s s' : Store} {i : Instr} (h : raw s i = some s') : s'.ledger = s.ledger := by
  cases i with
  | store a x => simp only [raw, Option.some.injEq] at h; subst h; rfl
  | link a b => simp only [raw, Option.some.injEq] at h; subst h; rfl
  | snapshot => simp only [raw, Option.some.injEq] at h; subst h; rfl
  | rollback k =>
    simp only [raw] at h
    cases hk : s.snapshots[k]? with
    | none => simp [hk] at h
    | some c => simp only [hk, Option.map_some, Option.some.injEq] at h; subst h; rfl
  | scrub => simp only [raw, Option.some.injEq] at h; subst h; rfl
  | «export» a =>
    simp only [raw] at h
    split at h
    · simp only [Option.some.injEq] at h; subst h; rfl
    · simp at h

/-- Kein Schritt bleibt hängen: der Status ist nie `halt`. -/
theorem exec_ne_halt (s : Store) (i : Instr) : (exec s i).2 ≠ .halt := by
  cases hr : raw s i with
  | none => simp [exec, hr]
  | some s' =>
    by_cases ha : admissible s' = true
    · simp [exec, hr, ha]
    · simp [exec, hr, ha]

/-- Genaue Kennzeichnung von `cont`. -/
theorem exec_cont_iff (s : Store) (i : Instr) :
    (exec s i).2 = .cont ↔ ∃ s', raw s i = some s' ∧ admissible s' = true := by
  cases hr : raw s i with
  | none => simp [exec, hr]
  | some s' =>
    by_cases ha : admissible s' = true
    · simp [exec, hr, ha]
    · simp [exec, hr, ha]

/-- `reject` genau dann, wenn der rohe Effekt nicht definiert ist. -/
theorem exec_reject_iff (s : Store) (i : Instr) :
    (exec s i).2 = .reject ↔ raw s i = none := by
  cases hr : raw s i with
  | none => simp [exec, hr]
  | some s' =>
    by_cases ha : admissible s' = true
    · simp [exec, hr, ha]
    · simp [exec, hr, ha]

/-- Atomarität: ohne `cont` bleiben Inhalt, Snapshots und Guards unverändert. -/
theorem exec_atomic {s : Store} {i : Instr} (h : (exec s i).2 ≠ .cont) :
    (exec s i).1.content = s.content ∧ (exec s i).1.snapshots = s.snapshots ∧
      (exec s i).1.guards = s.guards := by
  cases hr : raw s i with
  | none => simp [exec, hr]
  | some s' =>
    by_cases ha : admissible s' = true
    · simp [exec, hr, ha] at h
    · simp [exec, hr, ha]

/-- Fortschritt: ein Snapshot gelingt in jedem admissiblen Store. -/
theorem snapshot_progress {s : Store} (hs : admissible s = true) :
    (exec s .snapshot).2 = .cont :=
  (exec_cont_iff s .snapshot).2 ⟨_, rfl, hs⟩

/-- Fortschritt: `scrub` gelingt in jedem admissiblen Store. -/
theorem scrub_progress {s : Store} (hs : admissible s = true) :
    (exec s .scrub).2 = .cont :=
  (exec_cont_iff s .scrub).2 ⟨s, rfl, hs⟩

/-- Fortschritt: der Export einer gespeicherten Adresse gelingt in jedem admissiblen Store. -/
theorem export_progress {s : Store} (hs : admissible s = true) {a : Addr}
    (ha : s.content.addrs.contains a = true) : (exec s (.export a)).2 = .cont :=
  (exec_cont_iff s (.export a)).2
    ⟨s, by rw [show raw s (.export a) = if s.content.addrs.contains a then some s else none from rfl, if_pos ha], hs⟩

/-- Jeder Schritt verlängert das Ledger um genau einen Eintrag. -/
theorem exec_ledger_length (s : Store) (i : Instr) :
    (exec s i).1.ledger.length = s.ledger.length + 1 := by
  cases hr : raw s i with
  | none => simp [exec, hr]
  | some s' =>
    have hl := raw_ledger hr
    by_cases ha : admissible s' = true
    · simp [exec, hr, ha, hl]
    · simp [exec, hr, ha]

/-- Lineage-Vollständigkeit: ein Programm hinterlässt genau so viele Einträge, wie es Befehle hat. -/
theorem run_ledger_length (s : Store) (p : List Instr) :
    (run s p).ledger.length = s.ledger.length + p.length := by
  induction p generalizing s with
  | nil => simp [run]
  | cons i is ih =>
    simp only [run, ih, exec_ledger_length, List.length_cons]
    omega

end QSFormal.Store
