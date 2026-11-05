/-!
# Provenance: status order, witness tracking and frame typing

This module is generic: it does not refer to any physics and can be used for any record.
A record consists of *claims*; each claim has a status, a frame and the list of inputs
(witnesses) it rests on.  Claims are combined by derivation trees:

* `step s t`   — derive a statement of status `s` from `t`;
* `join s l r` — combine two statements of the same frame;
* `conv s g b t` — move `t` into frame `b` through a declared comparison map `g`.

A tree is well formed (`WF`) when no step raises the status, joins only combine statements
of one frame, and every change of frame uses a declared map.  The theorems say:

* `no_promotion`: the conclusion never has a higher status than any premise;
* `proved_only_from_proved`: a conclusion with status `proved` rests only on proved claims;
* `inputs_tracked`, `inputs_sourced`: the inputs of a conclusion are exactly the inputs of
  its premises — none is lost, none is invented;
* `frames_declared`: every premise reaches the frame of the conclusion through a chain of
  declared comparison maps.

Lean core only.
-/

namespace QAM.Provenance

/-- Status of a claim, from weakest to strongest. -/
inductive Status where
  | «open»
  | reading
  | conditional
  | computed
  | proved
  deriving DecidableEq, Repr

/-- The order on statuses is given by a rank. -/
def Status.rank : Status → Nat
  | .«open» => 0
  | .reading => 1
  | .conditional => 2
  | .computed => 3
  | .proved => 4

theorem Status.eq_proved_of_rank {s : Status} : s.rank ≥ 4 → s = .proved := by
  cases s <;> decide

/-- A claim: status, frame, and the inputs (witness identifiers) it rests on. -/
structure Claim where
  status : Status
  frame  : Nat
  inputs : List Nat

/-- Derivation trees over claims. -/
inductive Tree where
  | leaf (c : Claim)
  | step (s : Status) (t : Tree)
  | join (s : Status) (l r : Tree)
  | conv (s : Status) (g : Nat) (b : Nat) (t : Tree)

namespace Tree

def status : Tree → Status
  | leaf c => c.status
  | step s _ => s
  | join s _ _ => s
  | conv s _ _ _ => s

def frame : Tree → Nat
  | leaf c => c.frame
  | step _ t => frame t
  | join _ l _ => frame l
  | conv _ _ b _ => b

def inputs : Tree → List Nat
  | leaf c => c.inputs
  | step _ t => inputs t
  | join _ l r => inputs l ++ inputs r
  | conv _ _ _ t => inputs t

def leaves : Tree → List Claim
  | leaf c => [c]
  | step _ t => leaves t
  | join _ l r => leaves l ++ leaves r
  | conv _ _ _ t => leaves t

/-- Well-formedness relative to the declared comparison maps `D g a b`
("`g` is a declared map from frame `a` to frame `b`"). -/
def WF (D : Nat → Nat → Nat → Prop) : Tree → Prop
  | leaf _ => True
  | step s t => s.rank ≤ (status t).rank ∧ WF D t
  | join s l r =>
      s.rank ≤ (status l).rank ∧ s.rank ≤ (status r).rank ∧ frame l = frame r ∧ WF D l ∧ WF D r
  | conv s g b t => s.rank ≤ (status t).rank ∧ D g (frame t) b ∧ WF D t

end Tree

open Tree

/-- Frames reachable through a chain of declared maps. -/
inductive Reach (D : Nat → Nat → Nat → Prop) : Nat → Nat → Prop where
  | refl (a : Nat) : Reach D a a
  | snoc {a b c : Nat} (g : Nat) : Reach D a b → D g b c → Reach D a c

/-- No promotion: in a well-formed tree the conclusion's status is at most that of every premise. -/
theorem no_promotion {D : Nat → Nat → Nat → Prop} :
    ∀ (t : Tree), WF D t → ∀ c ∈ leaves t, (status t).rank ≤ c.status.rank
  | .leaf c', _, c, h => by
      simp only [leaves, List.mem_singleton] at h
      subst h
      exact Nat.le_refl _
  | .step s t, hw, c, h => by
      simp only [WF] at hw
      simp only [leaves] at h
      exact Nat.le_trans hw.1 (no_promotion t hw.2 c h)
  | .join s l r, hw, c, h => by
      simp only [WF] at hw
      obtain ⟨hl, hr, _, wl, wr⟩ := hw
      simp only [leaves, List.mem_append] at h
      rcases h with h | h
      · exact Nat.le_trans hl (no_promotion l wl c h)
      · exact Nat.le_trans hr (no_promotion r wr c h)
  | .conv s g b t, hw, c, h => by
      simp only [WF] at hw
      simp only [leaves] at h
      exact Nat.le_trans hw.1 (no_promotion t hw.2.2 c h)

/-- A proved conclusion rests only on proved claims. -/
theorem proved_only_from_proved {D : Nat → Nat → Nat → Prop} (t : Tree) (hw : WF D t)
    (hs : status t = .proved) : ∀ c ∈ leaves t, c.status = .proved := by
  intro c hc
  have h := no_promotion t hw c hc
  rw [hs] at h
  exact Status.eq_proved_of_rank h

/-- Inputs are never lost: every input of a premise is an input of the conclusion. -/
theorem inputs_tracked : ∀ (t : Tree), ∀ c ∈ leaves t, ∀ x ∈ c.inputs, x ∈ inputs t
  | .leaf c', c, h, x, hx => by
      simp only [leaves, List.mem_singleton] at h
      subst h
      exact hx
  | .step _ t, c, h, x, hx => by
      simp only [leaves] at h
      exact inputs_tracked t c h x hx
  | .join _ l r, c, h, x, hx => by
      simp only [leaves, List.mem_append] at h
      simp only [inputs, List.mem_append]
      rcases h with h | h
      · exact Or.inl (inputs_tracked l c h x hx)
      · exact Or.inr (inputs_tracked r c h x hx)
  | .conv _ _ _ t, c, h, x, hx => by
      simp only [leaves] at h
      exact inputs_tracked t c h x hx

/-- Inputs are never invented: every input of the conclusion comes from a premise. -/
theorem inputs_sourced : ∀ (t : Tree), ∀ x ∈ inputs t, ∃ c ∈ leaves t, x ∈ c.inputs
  | .leaf c, x, hx => ⟨c, by simp [leaves], hx⟩
  | .step _ t, x, hx => by
      simp only [inputs] at hx
      exact inputs_sourced t x hx
  | .join _ l r, x, hx => by
      simp only [inputs, List.mem_append] at hx
      rcases hx with hx | hx
      · obtain ⟨c, hc, hxc⟩ := inputs_sourced l x hx
        exact ⟨c, by simp only [leaves, List.mem_append]; exact Or.inl hc, hxc⟩
      · obtain ⟨c, hc, hxc⟩ := inputs_sourced r x hx
        exact ⟨c, by simp only [leaves, List.mem_append]; exact Or.inr hc, hxc⟩
  | .conv _ _ _ t, x, hx => by
      simp only [inputs] at hx
      exact inputs_sourced t x hx

/-- A conclusion is independent of an input exactly when no premise uses it. -/
theorem independent_iff (t : Tree) (x : Nat) :
    x ∉ inputs t ↔ ∀ c ∈ leaves t, x ∉ c.inputs := by
  constructor
  · intro h c hc hx
    exact h (inputs_tracked t c hc x hx)
  · intro h hx
    obtain ⟨c, hc, hxc⟩ := inputs_sourced t x hx
    exact h c hc hxc

/-- Frames are declared: every premise reaches the conclusion's frame through declared maps. -/
theorem frames_declared {D : Nat → Nat → Nat → Prop} :
    ∀ (t : Tree), WF D t → ∀ c ∈ leaves t, Reach D c.frame (frame t)
  | .leaf c', _, c, h => by
      simp only [leaves, List.mem_singleton] at h
      subst h
      exact Reach.refl _
  | .step _ t, hw, c, h => by
      simp only [WF] at hw
      simp only [leaves] at h
      exact frames_declared t hw.2 c h
  | .join _ l r, hw, c, h => by
      simp only [WF] at hw
      obtain ⟨_, _, hf, wl, wr⟩ := hw
      simp only [leaves, List.mem_append] at h
      rcases h with h | h
      · exact frames_declared l wl c h
      · have := frames_declared r wr c h
        simp only [frame]
        rw [hf]
        exact this
  | .conv _ g _ t, hw, c, h => by
      simp only [WF] at hw
      simp only [leaves] at h
      exact Reach.snoc g (frames_declared t hw.2.2 c h) hw.2.1

theorem reach_none {a b : Nat} (h : Reach (fun _ _ _ => False) a b) : a = b := by
  induction h with
  | refl => rfl
  | snoc _ _ hD => exact (hD : False).elim

/-- Without declared maps, a well-formed tree never changes frame. -/
theorem no_maps_same_frame (t : Tree) (hw : WF (fun _ _ _ => False) t) :
    ∀ c ∈ leaves t, c.frame = frame t :=
  fun c hc => reach_none (frames_declared t hw c hc)

end QAM.Provenance
