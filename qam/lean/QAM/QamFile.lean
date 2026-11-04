import QAM.Provenance

/-!
# Checking an exported QAM record

`qam.sty` (option `export`) writes every declaration of a LaTeX document to a file `\jobname.qam`,
one line per declaration:

```
map G : M -> T
gamma := <6,gamma>; frame M; status computed; inputs {gamma}
counting := claim; frame M; status proved; inputs {}
beta := derive(gamma,counting); frame M; status computed; inputs {gamma}
betaT := convert(G,beta); frame T; status conditional; inputs {gamma}
independent counting
compare betaT obs
```

This module reads such a file and checks it line by line against the record before it
(`step`, `run`).  The checker is a Lean function, and the theorems below say what a successful
check guarantees: no promotion, inputs exactly those of the premises, frames only changed by a
declared map with the right source, no duplicate keys, and correct independence and comparison
assertions.  The executable `qamcheck` (file `QamCheck.lean`) runs the checker on a file.

Generic: no reference to any physics.  Lean core only.
-/

namespace QAM.QamFile

open QAM.Provenance (Status)

def statusName : Status → String
  | .«open» => "open"
  | .reading => "reading"
  | .conditional => "conditional"
  | .computed => "computed"
  | .proved => "proved"

def parseStatus : String → Option Status
  | "open" => some .«open»
  | "reading" => some .reading
  | "conditional" => some .conditional
  | "computed" => some .computed
  | "proved" => some .proved
  | _ => none

/-- What the record knows about a claim. -/
structure Info where
  frame  : String
  status : Status
  inputs : List String
  /-- the premises the claim was derived from (empty for inputs, claims and theses) -/
  prem   : List String

/-- One line of a `.qam` file. -/
inductive Line where
  | map (g src tgt : String)
  | input (k f : String) (s : Status)
  | claim (k f : String) (s : Status)
  | derive (k f : String) (s : Status) (ps ins : List String)
  | convert (k f : String) (s : Status) (g p : String) (ins : List String)
  | indep (k : String)
  | compare (a b : String)

/-- The record so far: claims (newest first) and declared maps. -/
structure State where
  claims : List (String × Info) := []
  maps   : List (String × String × String) := []

def State.find (st : State) (k : String) : Option Info :=
  (st.claims.find? (fun e => decide (e.1 = k))).map (·.2)

def State.findMap (st : State) (g : String) : Option (String × String) :=
  (st.maps.find? (fun e => decide (e.1 = g))).map (·.2)

def State.add (st : State) (k : String) (i : Info) : State :=
  { st with claims := (k, i) :: st.claims }

/-- The convention-free frame: a claim in it fits every frame. -/
def anyFrame : String := "*"

/-- A premise is declared, lives in frame `f` (or is convention-free), and has at least status `s`. -/
def premOk (st : State) (f : String) (s : Status) (p : String) : Bool :=
  match st.find p with
  | some i => decide (s.rank ≤ i.status.rank) && decide (i.frame = f ∨ i.frame = anyFrame)
  | none => false

def premInputs (st : State) (p : String) : List String :=
  match st.find p with
  | some i => i.inputs
  | none => []

/-- The listed inputs are exactly the inputs of the premises. -/
def inputsOk (st : State) (ps ins : List String) : Bool :=
  ins.all (fun x => ps.any (fun p => decide (x ∈ premInputs st p))) &&
  ps.all (fun p => (premInputs st p).all (fun x => decide (x ∈ ins)))

/-- The map is declared, starts in the premise's frame, ends in `f`, and the status does not rise. -/
def convertOk (st : State) (f : String) (s : Status) (g p : String) : Bool :=
  match st.findMap g, st.find p with
  | some (a, b), some i => decide (a = i.frame) && decide (b = f) && decide (s.rank ≤ i.status.rank)
  | _, _ => false

def indepOk (st : State) (k : String) : Bool :=
  match st.find k with
  | some i => decide (i.inputs = [])
  | none => false

def compareOk (st : State) (a b : String) : Bool :=
  match st.find a, st.find b with
  | some i, some j => decide (i.frame = j.frame ∨ i.frame = anyFrame ∨ j.frame = anyFrame)
  | _, _ => false

/-- Check one line against the record before it. -/
def step (st : State) : Line → Option State
  | .map g a b =>
      if (st.findMap g).isNone = true then some { st with maps := (g, a, b) :: st.maps } else none
  | .input k f s =>
      if (st.find k).isNone = true then some (st.add k ⟨f, s, [k], []⟩) else none
  | .claim k f s =>
      if (st.find k).isNone = true then some (st.add k ⟨f, s, [], []⟩) else none
  | .derive k f s ps ins =>
      if (st.find k).isNone = true then
        if ps ≠ [] then
          if ps.all (premOk st f s) = true then
            if inputsOk st ps ins = true then some (st.add k ⟨f, s, ins, ps⟩) else none
          else none
        else none
      else none
  | .convert k f s g p ins =>
      if (st.find k).isNone = true then
        if convertOk st f s g p = true then
          if inputsOk st [p] ins = true then some (st.add k ⟨f, s, ins, [p]⟩) else none
        else none
      else none
  | .indep k => if indepOk st k = true then some st else none
  | .compare a b => if compareOk st a b = true then some st else none

/-- Check a whole record. -/
def run : State → List Line → Option State
  | st, [] => some st
  | st, l :: ls =>
      match step st l with
      | some st' => run st' ls
      | none => none

/-! ## What a successful check guarantees -/

theorem premOk_sound {st : State} {f : String} {s : Status} {p : String}
    (h : premOk st f s p = true) :
    ∃ i, st.find p = some i ∧ s.rank ≤ i.status.rank ∧ (i.frame = f ∨ i.frame = anyFrame) := by
  unfold premOk at h
  cases hp : st.find p with
  | none => simp [hp] at h
  | some i =>
    simp only [hp, Bool.and_eq_true, decide_eq_true_eq] at h
    exact ⟨i, rfl, h.1, h.2⟩

theorem inputsOk_sound {st : State} {ps ins : List String} (h : inputsOk st ps ins = true) :
    (∀ x ∈ ins, ∃ p ∈ ps, x ∈ premInputs st p) ∧ (∀ p ∈ ps, ∀ x ∈ premInputs st p, x ∈ ins) := by
  simpa [inputsOk, List.all_eq_true, List.any_eq_true] using h

theorem convertOk_sound {st : State} {f : String} {s : Status} {g p : String}
    (h : convertOk st f s g p = true) :
    ∃ a b i, st.findMap g = some (a, b) ∧ st.find p = some i ∧ a = i.frame ∧ b = f ∧
      s.rank ≤ i.status.rank := by
  unfold convertOk at h
  cases hm : st.findMap g with
  | none => simp [hm] at h
  | some ab =>
    obtain ⟨a, b⟩ := ab
    cases hp : st.find p with
    | none => simp [hm, hp] at h
    | some i =>
      simp only [hm, hp, Bool.and_eq_true, decide_eq_true_eq] at h
      first
        | exact ⟨a, b, i, rfl, rfl, h.1.1, h.1.2, h.2⟩
        | exact ⟨a, b, i, rfl, rfl, h.1, h.2.1, h.2.2⟩

/-- A derived claim: fresh key, at least one premise, no promotion, one frame,
and inputs exactly those of the premises. -/
theorem derive_sound {st st' : State} {k f : String} {s : Status} {ps ins : List String}
    (h : step st (.derive k f s ps ins) = some st') :
    st.find k = none ∧ ps ≠ [] ∧
    (∀ p ∈ ps, ∃ i, st.find p = some i ∧ s.rank ≤ i.status.rank ∧ (i.frame = f ∨ i.frame = anyFrame)) ∧
    (∀ x ∈ ins, ∃ p ∈ ps, x ∈ premInputs st p) ∧
    (∀ p ∈ ps, ∀ x ∈ premInputs st p, x ∈ ins) ∧
    st' = st.add k ⟨f, s, ins, ps⟩ := by
  simp only [step] at h
  split at h
  next h1 =>
    split at h
    next h2 =>
      split at h
      next h3 =>
        split at h
        next h4 =>
          cases h
          refine ⟨Option.isNone_iff_eq_none.mp h1, h2, ?_, (inputsOk_sound h4).1,
            (inputsOk_sound h4).2, rfl⟩
          intro p hp
          exact premOk_sound (List.all_eq_true.mp h3 p hp)
        next => cases h
      next => cases h
    next => cases h
  next => cases h

/-- A conversion: fresh key, a declared map from the premise's frame to the new frame,
no promotion, and the premise's inputs. -/
theorem convert_sound {st st' : State} {k f : String} {s : Status} {g p : String}
    {ins : List String} (h : step st (.convert k f s g p ins) = some st') :
    st.find k = none ∧
    (∃ a b i, st.findMap g = some (a, b) ∧ st.find p = some i ∧ a = i.frame ∧ b = f ∧
      s.rank ≤ i.status.rank) ∧
    (∀ x ∈ ins, x ∈ premInputs st p) ∧ (∀ x ∈ premInputs st p, x ∈ ins) ∧
    st' = st.add k ⟨f, s, ins, [p]⟩ := by
  simp only [step] at h
  split at h
  next h1 =>
    split at h
    next h2 =>
      split at h
      next h3 =>
        cases h
        obtain ⟨hs, hc⟩ := inputsOk_sound h3
        refine ⟨Option.isNone_iff_eq_none.mp h1, convertOk_sound h2, ?_, ?_, rfl⟩
        · intro x hx
          obtain ⟨q, hq, hxq⟩ := hs x hx
          simp only [List.mem_singleton] at hq
          subst hq
          exact hxq
        · exact hc p (List.mem_singleton.mpr rfl)
      next => cases h
    next => cases h
  next => cases h

/-- An independence assertion holds only for a declared claim without inputs. -/
theorem indep_sound {st st' : State} {k : String} (h : step st (.indep k) = some st') :
    ∃ i, st.find k = some i ∧ i.inputs = [] := by
  simp only [step] at h
  split at h
  next hc =>
    unfold indepOk at hc
    cases hk : st.find k with
    | none => simp [hk] at hc
    | some i =>
      simp only [hk, decide_eq_true_eq] at hc
      exact ⟨i, rfl, hc⟩
  next => cases h

/-- A comparison is accepted only between declared claims of one frame. -/
theorem compare_sound {st st' : State} {a b : String} (h : step st (.compare a b) = some st') :
    ∃ i j, st.find a = some i ∧ st.find b = some j ∧
      (i.frame = j.frame ∨ i.frame = anyFrame ∨ j.frame = anyFrame) := by
  simp only [step] at h
  split at h
  next hc =>
    unfold compareOk at hc
    cases ha : st.find a with
    | none => simp [ha] at hc
    | some i =>
      cases hb : st.find b with
      | none => simp [ha, hb] at hc
      | some j =>
        simp only [ha, hb, decide_eq_true_eq] at hc
        exact ⟨i, j, rfl, rfl, hc⟩
  next => cases h

theorem run_cons {st st'' : State} {l : Line} {ls : List Line} (h : run st (l :: ls) = some st'') :
    ∃ st', step st l = some st' ∧ run st' ls = some st'' := by
  simp only [run] at h
  cases hs : step st l with
  | none => simp [hs] at h
  | some st' =>
    simp only [hs] at h
    exact ⟨st', rfl, h⟩

/-- In a checked record every line was accepted against the record before it. -/
theorem run_line : ∀ {st st'' : State} {ls : List Line}, run st ls = some st'' →
    ∀ l ∈ ls, ∃ st0 st1, step st0 l = some st1
  | _, _, [], _, l, hl => by simp at hl
  | st, _, l' :: ls, h, l, hl => by
      obtain ⟨st', hs, hr⟩ := run_cons h
      simp only [List.mem_cons] at hl
      rcases hl with rfl | hl
      · exact ⟨st, st', hs⟩
      · exact run_line hr l hl

/-- No promotion in a checked record: every derived claim has at most the status of each premise,
and all premises live in its frame. -/
theorem checked_no_promotion {st st'' : State} {ls : List Line} (h : run st ls = some st'')
    {k f : String} {s : Status} {ps ins : List String} (hl : Line.derive k f s ps ins ∈ ls) :
    ∃ st0 : State, ∀ p ∈ ps, ∃ i, st0.find p = some i ∧ s.rank ≤ i.status.rank ∧ (i.frame = f ∨ i.frame = anyFrame) := by
  obtain ⟨st0, _, h0⟩ := run_line h _ hl
  exact ⟨st0, (derive_sound h0).2.2.1⟩

/-- In a checked record every independence assertion is true of the record at that point. -/
theorem checked_indep {st st'' : State} {ls : List Line} (h : run st ls = some st'')
    {k : String} (hl : Line.indep k ∈ ls) :
    ∃ st0 : State, ∃ i, st0.find k = some i ∧ i.inputs = [] := by
  obtain ⟨st0, _, h0⟩ := run_line h _ hl
  exact ⟨st0, indep_sound h0⟩

/-! ## Guarantees about the whole checked record

The theorems above speak about one line at a time.  The following ones speak about the final
record that `run` returns: an invariant `Good` holds for every record reachable from the empty one,
and from it follow statements about all ancestors of a claim, at any distance. -/

theorem find_add (st : State) (k : String) (i : Info) (p : String) :
    (st.add k i).find p = if k = p then some i else st.find p := by
  unfold State.find State.add
  by_cases h : k = p <;> simp [h]

theorem premInputs_of {st : State} {p : String} {j : Info} (h : st.find p = some j) :
    premInputs st p = j.inputs := by
  simp [premInputs, h]

/-- Every premise of a stored claim is stored, has at least its status, and passes on its inputs;
every input of a stored claim is its own key (for a leaf) or comes from a premise. -/
def Good (st : State) : Prop :=
  ∀ k i, st.find k = some i →
    (∀ p ∈ i.prem, ∃ j, st.find p = some j ∧ i.status.rank ≤ j.status.rank ∧
      ∀ x ∈ j.inputs, x ∈ i.inputs) ∧
    (∀ x ∈ i.inputs, (i.prem = [] ∧ x = k) ∨ ∃ p ∈ i.prem, ∃ j, st.find p = some j ∧ x ∈ j.inputs)

theorem good_empty : Good {} := by
  intro k i h
  simp [State.find] at h

theorem good_add {st : State} {k : String} {i : Info} (hg : Good st)
    (hfresh : (st.find k).isNone = true)
    (h1 : ∀ p ∈ i.prem, ∃ j, st.find p = some j ∧ i.status.rank ≤ j.status.rank ∧
      ∀ x ∈ j.inputs, x ∈ i.inputs)
    (h2 : ∀ x ∈ i.inputs, (i.prem = [] ∧ x = k) ∨
      ∃ p ∈ i.prem, ∃ j, st.find p = some j ∧ x ∈ j.inputs) :
    Good (st.add k i) := by
  have lift : ∀ p j, st.find p = some j → (st.add k i).find p = some j := by
    intro p j hp
    have hkp : k ≠ p := by
      intro e
      subst e
      rw [hp] at hfresh
      cases hfresh
    rw [find_add]
    simp [hkp, hp]
  intro q iq hq
  rw [find_add] at hq
  by_cases hkq : k = q
  · simp only [hkq, ite_true, Option.some.injEq] at hq
    subst hq
    subst hkq
    constructor
    · intro p hp
      obtain ⟨j, hj, hr, hin⟩ := h1 p hp
      exact ⟨j, lift p j hj, hr, hin⟩
    · intro x hx
      rcases h2 x hx with hl | ⟨p, hp, j, hj, hxj⟩
      · exact Or.inl hl
      · exact Or.inr ⟨p, hp, j, lift p j hj, hxj⟩
  · simp only [hkq, ite_false] at hq
    obtain ⟨g1, g2⟩ := hg q iq hq
    constructor
    · intro p hp
      obtain ⟨j, hj, hr, hin⟩ := g1 p hp
      exact ⟨j, lift p j hj, hr, hin⟩
    · intro x hx
      rcases g2 x hx with hl | ⟨p, hp, j, hj, hxj⟩
      · exact Or.inl hl
      · exact Or.inr ⟨p, hp, j, lift p j hj, hxj⟩

/-- Every accepted line keeps the record good. -/
theorem good_step {st st' : State} {l : Line} (hg : Good st) (h : step st l = some st') :
    Good st' := by
  cases l with
  | map g a b =>
    simp only [step] at h
    split at h
    · cases h; exact hg
    · cases h
  | input k f s =>
    simp only [step] at h
    split at h
    next hf =>
      cases h
      refine good_add hg hf ?_ ?_
      · intro p hp; simp at hp
      · intro x hx
        simp only [List.mem_singleton] at hx
        exact Or.inl ⟨rfl, hx⟩
    · cases h
  | claim k f s =>
    simp only [step] at h
    split at h
    next hf =>
      cases h
      refine good_add hg hf ?_ ?_
      · intro p hp; simp at hp
      · intro x hx; simp at hx
    · cases h
  | derive k f s ps ins =>
    have hd := derive_sound h
    obtain ⟨hk, _, hprem, hsrc, htr, rfl⟩ := hd
    refine good_add hg (by simp [hk]) ?_ ?_
    · intro p hp
      obtain ⟨j, hj, hr, _⟩ := hprem p hp
      refine ⟨j, hj, hr, ?_⟩
      intro x hx
      exact htr p hp x (by rw [premInputs_of hj]; exact hx)
    · intro x hx
      obtain ⟨p, hp, hxp⟩ := hsrc x hx
      obtain ⟨j, hj, _, _⟩ := hprem p hp
      exact Or.inr ⟨p, hp, j, hj, by rw [← premInputs_of hj]; exact hxp⟩
  | convert k f s g p ins =>
    have hc := convert_sound h
    obtain ⟨hk, ⟨a, b, j, _, hp, _, _, hr⟩, hin, hout, rfl⟩ := hc
    refine good_add hg (by simp [hk]) ?_ ?_
    · intro q hq
      simp only [List.mem_singleton] at hq
      subst hq
      refine ⟨j, hp, hr, ?_⟩
      intro x hx
      exact hout x (by rw [premInputs_of hp]; exact hx)
    · intro x hx
      exact Or.inr ⟨p, List.mem_singleton.mpr rfl, j, hp, by rw [← premInputs_of hp]; exact hin x hx⟩
  | indep k =>
    simp only [step] at h
    split at h
    · cases h; exact hg
    · cases h
  | compare a b =>
    simp only [step] at h
    split at h
    · cases h; exact hg
    · cases h

theorem good_run : ∀ {st st' : State} {ls : List Line}, Good st → run st ls = some st' → Good st'
  | _, _, [], hg, h => by simp only [run, Option.some.injEq] at h; subst h; exact hg
  | _, _, _ :: _, hg, h => by
      obtain ⟨st1, hs, hr⟩ := run_cons h
      exact good_run (good_step hg hs) hr

/-- Every record accepted by the checker is good. -/
theorem checked_good {ls : List Line} {st : State} (h : run {} ls = some st) : Good st :=
  good_run good_empty h

/-- `a` is an ancestor of `k`: reachable through premises. -/
inductive Ancestor (st : State) : String → String → Prop where
  | prem {k p : String} {i : Info} : st.find k = some i → p ∈ i.prem → Ancestor st k p
  | trans {k p q : String} : Ancestor st k p → Ancestor st p q → Ancestor st k q

theorem ancestor_found {st : State} (hg : Good st) {k a : String} (h : Ancestor st k a) :
    ∃ j, st.find a = some j := by
  induction h with
  | prem hk hp =>
    obtain ⟨j, hj, _⟩ := (hg _ _ hk).1 _ hp
    exact ⟨j, hj⟩
  | trans _ _ _ ih2 => exact ih2

theorem ancestor_bound {st : State} (hg : Good st) {k a : String} (h : Ancestor st k a) :
    ∀ i j, st.find k = some i → st.find a = some j →
      i.status.rank ≤ j.status.rank ∧ ∀ x ∈ j.inputs, x ∈ i.inputs := by
  induction h with
  | prem hk hp =>
    intro i' j hi hj
    rw [hk] at hi
    cases hi
    obtain ⟨j', hj', hr, hin⟩ := (hg _ _ hk).1 _ hp
    rw [hj'] at hj
    cases hj
    exact ⟨hr, hin⟩
  | trans h1 _ ih1 ih2 =>
    intro i j hi hj
    obtain ⟨m, hm⟩ := ancestor_found hg h1
    obtain ⟨r1, in1⟩ := ih1 i m hi hm
    obtain ⟨r2, in2⟩ := ih2 m j hm hj
    exact ⟨Nat.le_trans r1 r2, fun x hx => in1 x (in2 x hx)⟩

/-- No promotion, for the whole record: in a checked record no claim has a higher status than
anything it rests on, at any distance. -/
theorem checked_no_promotion_record {ls : List Line} {st : State} (h : run {} ls = some st)
    {k a : String} {i j : Info} (ha : Ancestor st k a) (hi : st.find k = some i)
    (hj : st.find a = some j) : i.status.rank ≤ j.status.rank :=
  (ancestor_bound (checked_good h) ha i j hi hj).1

/-- In particular a claim marked proved rests, at any distance, only on proved claims. -/
theorem checked_proved_record {ls : List Line} {st : State} (h : run {} ls = some st)
    {k a : String} {i j : Info} (ha : Ancestor st k a) (hi : st.find k = some i)
    (hj : st.find a = some j) (hp : i.status = .proved) : j.status = .proved := by
  have := checked_no_promotion_record h ha hi hj
  rw [hp] at this
  exact QAM.Provenance.Status.eq_proved_of_rank this

/-- Inputs are never lost along the record: every input of an ancestor is an input of the claim.
So a claim without inputs rests on no claim with inputs, and in particular on no input line,
whose inputs consist of its own key (`input_stored`). -/
theorem checked_inputs_record {ls : List Line} {st : State} (h : run {} ls = some st)
    {k a : String} {i j : Info} (ha : Ancestor st k a) (hi : st.find k = some i)
    (hj : st.find a = some j) : ∀ x ∈ j.inputs, x ∈ i.inputs :=
  (ancestor_bound (checked_good h) ha i j hi hj).2

theorem checked_independent_record {ls : List Line} {st : State} (h : run {} ls = some st)
    {k a : String} {i j : Info} (ha : Ancestor st k a) (hi : st.find k = some i)
    (hj : st.find a = some j) (hind : i.inputs = []) : j.inputs = [] := by
  have hin := checked_inputs_record h ha hi hj
  cases hji : j.inputs with
  | nil => rfl
  | cons x xs =>
    have := hin x (by rw [hji]; exact List.mem_cons_self ..)
    rw [hind] at this
    cases this

/-- An input line stores the input as its own (only) input. -/
theorem input_stored {st st' : State} {k f : String} {s : Status}
    (h : step st (.input k f s) = some st') : st'.find k = some ⟨f, s, [k], []⟩ := by
  simp only [step] at h
  split at h
  · cases h
    rw [find_add]
    simp
  · cases h

/-- Every input listed for a claim is either its own key (if it is an input line) or the input of
one of its premises: inputs are never invented, anywhere in the record. -/
theorem checked_inputs_sourced {ls : List Line} {st : State} (h : run {} ls = some st)
    {k : String} {i : Info} (hi : st.find k = some i) :
    ∀ x ∈ i.inputs, (i.prem = [] ∧ x = k) ∨ ∃ p ∈ i.prem, ∃ j, st.find p = some j ∧ x ∈ j.inputs :=
  ((checked_good h) k i hi).2

/-! ## The hash chain

Every claim line carries a hash and the list of its sources, the hashes of its premises.  `qam.sty`
computes the hash as MD5 of the claim's canonical form together with its sources, so a change
anywhere upstream changes every hash below it.  Lean does not recompute MD5 (the script
`qam/tools/qamhash.py` does that independently); it checks the links: a derived claim names exactly
the hashes of its premises, in order, and no hash occurs twice. -/

structure Meta where
  hash    : String := ""
  sources : List String := []

def lookupH (hs : List (String × String)) (k : String) : Option String :=
  (hs.find? (fun e => decide (e.1 = k))).map (·.2)

def freshH (hs : List (String × String)) (h : String) : Bool :=
  hs.all (fun e => decide (e.2 ≠ h))

def linkLeaf (hs : List (String × String)) (k : String) (m : Meta) : Option (List (String × String)) :=
  if m.sources = [] ∧ freshH hs m.hash = true then some ((k, m.hash) :: hs) else none

/-- Check the hash links of one line against the hashes recorded so far. -/
def linkStep (hs : List (String × String)) : Line → Meta → Option (List (String × String))
  | .input k _ _, m => linkLeaf hs k m
  | .claim k _ _, m => linkLeaf hs k m
  | .derive k _ _ ps _, m =>
      if ps.map (lookupH hs) = m.sources.map some ∧ freshH hs m.hash = true then
        some ((k, m.hash) :: hs) else none
  | .convert k _ _ _ p _, m =>
      if [lookupH hs p] = m.sources.map some ∧ freshH hs m.hash = true then
        some ((k, m.hash) :: hs) else none
  | .map .., _ => some hs
  | .indep _, _ => some hs
  | .compare .., _ => some hs

/-- A derived claim names exactly the hashes of its premises, in order, and has a new hash. -/
theorem link_derive_sound {hs hs' : List (String × String)} {k f : String} {s : Status}
    {ps ins : List String} {m : Meta} (h : linkStep hs (.derive k f s ps ins) m = some hs') :
    ps.map (lookupH hs) = m.sources.map some ∧ (∀ e ∈ hs, e.2 ≠ m.hash) ∧
    hs' = (k, m.hash) :: hs := by
  simp only [linkStep] at h
  split at h
  next hc =>
    cases h
    refine ⟨hc.1, ?_, rfl⟩
    have h2 := hc.2
    simp only [freshH, List.all_eq_true, decide_eq_true_eq] at h2
    exact h2
  next => cases h

/-- A conversion names exactly the hash of its premise and has a new hash. -/
theorem link_convert_sound {hs hs' : List (String × String)} {k f : String} {s : Status}
    {g p : String} {ins : List String} {m : Meta}
    (h : linkStep hs (.convert k f s g p ins) m = some hs') :
    m.sources.map some = [lookupH hs p] ∧ (∀ e ∈ hs, e.2 ≠ m.hash) ∧
    hs' = (k, m.hash) :: hs := by
  simp only [linkStep] at h
  split at h
  next hc =>
    cases h
    refine ⟨hc.1.symm, ?_, rfl⟩
    have h2 := hc.2
    simp only [freshH, List.all_eq_true, decide_eq_true_eq] at h2
    exact h2
  next => cases h

/-- A thesis, claim or input has no sources and a new hash. -/
theorem link_leaf_sound {hs hs' : List (String × String)} {k : String} {m : Meta}
    (h : linkLeaf hs k m = some hs') :
    m.sources = [] ∧ (∀ e ∈ hs, e.2 ≠ m.hash) ∧ hs' = (k, m.hash) :: hs := by
  unfold linkLeaf at h
  split at h
  next hc =>
    cases h
    refine ⟨hc.1, ?_, rfl⟩
    have h2 := hc.2
    simp only [freshH, List.all_eq_true, decide_eq_true_eq] at h2
    exact h2
  next => cases h

/-! ## Reading a `.qam` file (not verified; only the checker above is) -/

def toS (l : List Char) : String := l.foldl String.push ""

def trimC (l : List Char) : List Char :=
  ((l.dropWhile Char.isWhitespace).reverse.dropWhile Char.isWhitespace).reverse

def stripPrefix (p l : List Char) : Option (List Char) :=
  if p.isPrefixOf l then some (l.drop p.length) else none

def stripSuffix (p l : List Char) : Option (List Char) :=
  (stripPrefix p.reverse l.reverse).map List.reverse

def splitOnce (sep : List Char) : List Char → Option (List Char × List Char)
  | [] => none
  | c :: cs =>
      if sep.isPrefixOf (c :: cs) then some ([], (c :: cs).drop sep.length)
      else (splitOnce sep cs).map (fun ab => (c :: ab.1, ab.2))

def splitChar (d : Char) (l : List Char) : List (List Char) :=
  l.foldr (fun c acc => if c = d then [] :: acc else
    match acc with
    | [] => [[c]]
    | a :: r => (c :: a) :: r) [[]]

def items (l : List Char) : List String :=
  ((splitChar ',' l).map trimC).filter (fun x => !x.isEmpty) |>.map toS

def parseLine (raw : List Char) : Except String (Option (Line × Meta)) := do
  let l := trimC raw
  if l.isEmpty || l.head? == some '%' then return none
  if let some r := stripPrefix "map ".toList l then
    let some (g, rest) := splitOnce " : ".toList r | throw "map line without ' : '"
    let some (a, b) := splitOnce " -> ".toList rest | throw "map line without ' -> '"
    return some (.map (toS (trimC g)) (toS (trimC a)) (toS (trimC b)), {})
  if let some r := stripPrefix "independent ".toList l then
    return some (.indep (toS (trimC r)), {})
  if let some r := stripPrefix "compare ".toList l then
    let some (a, b) := splitOnce " ".toList (trimC r) | throw "compare needs two keys"
    return some (.compare (toS (trimC a)) (toS (trimC b)), {})
  let some (k, rhs) := splitOnce " := ".toList l | throw "expected 'key := ...'"
  let k := toS (trimC k)
  match (splitChar ';' rhs).map trimC with
  | body :: fr :: sta :: inp :: rest =>
    let hsh := ((rest.findSome? (stripPrefix "hash ".toList)).map (fun x => toS (trimC x))).getD ""
    let srcs := match rest.findSome? (stripPrefix "sources {".toList) with
      | some r => items ((stripSuffix "}".toList r).getD r)
      | none => []
    let m : Meta := { hash := hsh, sources := srcs }
    let some f := stripPrefix "frame ".toList fr | throw "expected 'frame ...'"
    let some sn := stripPrefix "status ".toList sta | throw "expected 'status ...'"
    let some s := parseStatus (toS (trimC sn)) | throw s!"unknown status '{toS sn}'"
    let some inp' := stripPrefix "inputs {".toList inp | throw "expected 'inputs {...}'"
    let some inp'' := stripSuffix "}".toList inp' | throw "expected '}'"
    let f := toS (trimC f)
    let ins := items inp''
    if body = "claim".toList ∨ body = "thesis".toList then return some (.claim k f s, m)
    if (stripPrefix "<6,".toList body).isSome then return some (.input k f s, m)
    if let some r := stripPrefix "derive(".toList body then
      let some r' := stripSuffix ")".toList r | throw "expected ')'"
      return some (.derive k f s (items r') ins, m)
    if let some r := stripPrefix "convert(".toList body then
      let some r' := stripSuffix ")".toList r | throw "expected ')'"
      match items r' with
      | [g, p] => return some (.convert k f s g p ins, m)
      | _ => throw "convert needs a map and one premise"
    throw s!"unknown declaration '{toS body}'"
  | _ => throw "expected at least four fields separated by ';'"

/-- A human-readable reason for a rejected line (diagnostics only). -/
def reason (st : State) : Line → String
  | .map g _ _ => s!"map {g} is declared twice"
  | .input k _ _ => s!"{k} is declared twice"
  | .claim k _ _ => s!"{k} is declared twice"
  | .derive k f s ps _ =>
      if (st.find k).isSome then s!"{k} is declared twice"
      else if ps.isEmpty then s!"{k} has no premises"
      else match ps.find? (fun p => !premOk st f s p) with
        | some p =>
          match st.find p with
          | none => s!"premise {p} is not declared"
          | some i =>
            if i.frame ≠ f ∧ i.frame ≠ anyFrame then s!"frame mixing: premise {p} is in frame {i.frame}, {k} in frame {f}"
            else s!"promotion: {k} is declared {statusName s}, but premise {p} is only {statusName i.status}"
        | none => s!"the inputs listed for {k} are not those of its premises"
  | .convert k f s g p _ =>
      if (st.find k).isSome then s!"{k} is declared twice"
      else match st.findMap g, st.find p with
        | none, _ => s!"map {g} is not declared"
        | _, none => s!"premise {p} is not declared"
        | some (a, b), some i =>
          if a ≠ i.frame then s!"map {g} starts in frame {a}, but {p} is in frame {i.frame}"
          else if b ≠ f then s!"map {g} ends in frame {b}, but {k} is declared in frame {f}"
          else if s.rank > i.status.rank then
            s!"promotion: {k} is declared {statusName s}, but {p} is only {statusName i.status}"
          else s!"the inputs listed for {k} are not those of {p}"
  | .indep k =>
      match st.find k with
      | none => s!"{k} is not declared"
      | some i => s!"{k} is asserted independent, but rests on {i.inputs}"
  | .compare a b => s!"frame mixing: {a} and {b} are compared across frames (or not declared)"

end QAM.QamFile
