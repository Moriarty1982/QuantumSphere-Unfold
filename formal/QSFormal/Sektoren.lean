import QSFormal.Ladungen

/-!
# Die Ladungs-Sektoren aus der Oktonionen-Multiplikation (v4.9.0-r48)

In `QSFormal.Ladungen` sind die vier Ladungs-Sektoren als Daten gesetzt: Vorzeichenpaare `(ℓ, r)` von `iL_{e₇}`, `iR_{e₇}` und die
Farbdimension `1, 3, 3, 1` per Definition (`colourDim`). Dieses Modul leitet beides aus der Multiplikation `O.mul` von
`QSFormal.Dixon` her, auf `ℂ ⊗ 𝕆 = CO` mit der äußeren Einheit `i = CO.R` und der Konjugation `T = CO.T`:

* `(iL)² = (iR)² = 1` und `iL iR = iR iL` für alle `x` (`iL_sq`, `iR_sq`, `iL_iR_comm`).
* `P_s = ¼(1 + ℓ iL)(1 + r iR)` (hier `P4 s = 4 P_s`) ist für jeden der vier Sektoren ein Projektor; die vier sind paarweise
  orthogonal, summieren sich zur Eins, und auf dem Bild von `P_s` gilt `iL = ℓ`, `iR = r` (`P4_idem`, `P4_orth`, `P4_sum`,
  `P4_eigen`).
* Spuren über die ℂ-Basis `e₀..e₇`: `Sp L = Sp R = 0`, `Sp(L R) = 4`; `Sp P4 s = 4 · colourDim s`, also Rang `1, 3, 3, 1`
  (`traces`, `colourDim_from_trace`). Dass der Rang eines Projektors seine Spur ist, ist Standard und hier nicht formalisiert.
* Auf dem Bild von `P_s`: `6Q = 3 − iL − 2 iR` wirkt als `q6 s`, und die Abweichungen `Δ₂ = iR − iL`, `Δ₃ = −2 iL − iR`
  (`Δ₁ = 0`) wirken als die Platz-Gewichte `weights s` von r47 (`Q6_on_sector`, `Delta_on_sector`).
* Der Frame `T` kehrt `iL`, `iR` um und bildet `P_s` auf `P_{T s}` ab (`T_iL`, `T_iR`, `T_P4`).
* Die Farbdrehung `σ` aus r36 vertauscht auf der Basis mit `iL`, `iR` und jedem `P_s` (`sigma_comm_basis`), bleibt also in
  jedem Sektor. Die Fortsetzung von der Basis auf alle `x` ist Linearität und hier, wie bei `sigma_respects`, nicht formalisiert.

Damit sind die Tabellen `sectors`, `colourDim`, `q6` und `weights` aus `QSFormal.Ladungen` keine Setzungen mehr, sondern
Eigenschaften von `O.mul`.

* r49 (H33): Mit der Teilchen-Zuordnung von r42.1(b) ist `2(Q − ½) = B − L`, `Y/2 = (B − L)/2 + T₃^R` und
  `Q_em = T₃^L + T₃^R + (B − L)/2` (`b_minus_l`). `Q_em` ist keine Funktion des Sektors (`qem_not_sector_function`), kann also aus
  `iL_{e₇}`, `iR_{e₇}` allein nicht gebaut werden: Die e₇-Achse trägt B − L, das Photon braucht den ℍ-Faktor. Ohne Mathlib: nur Lean-Kern (`decide`, `simp`, `omega`).
-/

namespace QSFormal.Sektoren

open QSFormal.Dixon QSFormal.Ladungen

deriving instance DecidableEq for CO

/-! ## Operatoren auf `ℂ ⊗ 𝕆` -/

def oz : O := ⟨⟨0, 0, 0, 0⟩, ⟨0, 0, 0, 0⟩⟩
def osmul (k : Int) (x : O) : O :=
  ⟨⟨k * x.p.a, k * x.p.b, k * x.p.c, k * x.p.d⟩, ⟨k * x.q.a, k * x.q.b, k * x.q.c, k * x.q.d⟩⟩

def add (x y : CO) : CO := ⟨O.add x.u y.u, O.add x.w y.w⟩
def smul (k : Int) (x : CO) : CO := ⟨osmul k x.u, osmul k x.w⟩
def zero : CO := ⟨oz, oz⟩

/-- Links- und Rechtsmultiplikation mit `e₇`, komponentenweise (also ℂ-linear). -/
def L (x : CO) : CO := ⟨O.mul (O.e 7) x.u, O.mul (O.e 7) x.w⟩
def R (x : CO) : CO := ⟨O.mul x.u (O.e 7), O.mul x.w (O.e 7)⟩
/-- `iL_{e₇}`, `iR_{e₇}` mit der äußeren Einheit `i = CO.R`. -/
def iL (x : CO) : CO := CO.R (L x)
def iR (x : CO) : CO := CO.R (R x)

/-- `4 P_s = (1 + ℓ iL)(1 + r iR)`. -/
def P4 (s : Sector) (x : CO) : CO :=
  let y := add x (smul s.r (iR x))
  add y (smul s.l (iL y))

/-- `6Q = 3 − iL − 2 iR` (r35.1(d)). -/
def Q6 (x : CO) : CO := add (smul 3 x) (add (smul (-1) (iL x)) (smul (-2) (iR x)))

/-- Abweichungen `Δᵢ = i(Bᵢ − L_{e₇})`, `B = (L, R, −L − R)` (r47): `Δ₁ = 0`, `Δ₂ = iR − iL`, `Δ₃ = −2 iL − iR`. -/
def Delta2 (x : CO) : CO := add (iR x) (smul (-1) (iL x))
def Delta3 (x : CO) : CO := add (smul (-2) (iL x)) (smul (-1) (iR x))

/-! ## Algebra von `iL`, `iR` -/

theorem iL_sq (x : CO) : iL (iL x) = x := by
  obtain ⟨⟨⟨a0,a1,a2,a3⟩,⟨a4,a5,a6,a7⟩⟩, ⟨⟨b0,b1,b2,b3⟩,⟨b4,b5,b6,b7⟩⟩⟩ := x
  simp [iL, L, CO.R, O.mul, O.e, O.neg, Q.mul, Q.sub, Q.add, Q.conj, Q.neg]

theorem iR_sq (x : CO) : iR (iR x) = x := by
  obtain ⟨⟨⟨a0,a1,a2,a3⟩,⟨a4,a5,a6,a7⟩⟩, ⟨⟨b0,b1,b2,b3⟩,⟨b4,b5,b6,b7⟩⟩⟩ := x
  simp [iR, R, CO.R, O.mul, O.e, O.neg, Q.mul, Q.sub, Q.add, Q.conj, Q.neg]

theorem iL_iR_comm (x : CO) : iL (iR x) = iR (iL x) := by
  obtain ⟨⟨⟨a0,a1,a2,a3⟩,⟨a4,a5,a6,a7⟩⟩, ⟨⟨b0,b1,b2,b3⟩,⟨b4,b5,b6,b7⟩⟩⟩ := x
  simp [iL, iR, L, R, CO.R, O.mul, O.e, O.neg, Q.mul, Q.sub, Q.add, Q.conj, Q.neg]

/-! ## Die vier Projektoren -/

theorem P4_eigen : ∀ s ∈ sectors, ∀ x : CO,
    iL (P4 s x) = smul s.l (P4 s x) ∧ iR (P4 s x) = smul s.r (P4 s x) := by
  intro s hs x
  obtain ⟨⟨⟨a0,a1,a2,a3⟩,⟨a4,a5,a6,a7⟩⟩, ⟨⟨b0,b1,b2,b3⟩,⟨b4,b5,b6,b7⟩⟩⟩ := x
  simp only [sectors, List.mem_cons, List.not_mem_nil, or_false] at hs
  rcases hs with rfl | rfl | rfl | rfl <;>
    simp [P4, iL, iR, L, R, add, smul, osmul, CO.R, O.add, O.mul, O.e, O.neg, Q.mul, Q.sub, Q.add, Q.conj, Q.neg] <;> omega

theorem P4_idem : ∀ s ∈ sectors, ∀ x : CO, P4 s (P4 s x) = smul 4 (P4 s x) := by
  intro s hs x
  obtain ⟨⟨⟨a0,a1,a2,a3⟩,⟨a4,a5,a6,a7⟩⟩, ⟨⟨b0,b1,b2,b3⟩,⟨b4,b5,b6,b7⟩⟩⟩ := x
  simp only [sectors, List.mem_cons, List.not_mem_nil, or_false] at hs
  rcases hs with rfl | rfl | rfl | rfl <;>
    simp [P4, iL, iR, L, R, add, smul, osmul, CO.R, O.add, O.mul, O.e, O.neg, Q.mul, Q.sub, Q.add, Q.conj, Q.neg] <;> omega

theorem P4_orth : ∀ s ∈ sectors, ∀ s' ∈ sectors, s ≠ s' → ∀ x : CO, P4 s (P4 s' x) = zero := by
  intro s hs s' hs' hne x
  obtain ⟨⟨⟨a0,a1,a2,a3⟩,⟨a4,a5,a6,a7⟩⟩, ⟨⟨b0,b1,b2,b3⟩,⟨b4,b5,b6,b7⟩⟩⟩ := x
  simp only [sectors, List.mem_cons, List.not_mem_nil, or_false] at hs hs'
  rcases hs with rfl | rfl | rfl | rfl <;> rcases hs' with rfl | rfl | rfl | rfl <;>
    first
    | exact absurd rfl hne
    | simp [P4, zero, oz, iL, iR, L, R, add, smul, osmul, CO.R, O.add, O.mul, O.e, O.neg,
        Q.mul, Q.sub, Q.add, Q.conj, Q.neg] <;> omega

theorem P4_sum (x : CO) :
    add (add (P4 ⟨1, 1⟩ x) (P4 ⟨-1, 1⟩ x)) (add (P4 ⟨1, -1⟩ x) (P4 ⟨-1, -1⟩ x)) = smul 4 x := by
  obtain ⟨⟨⟨a0,a1,a2,a3⟩,⟨a4,a5,a6,a7⟩⟩, ⟨⟨b0,b1,b2,b3⟩,⟨b4,b5,b6,b7⟩⟩⟩ := x
  simp [P4, iL, iR, L, R, add, smul, osmul, CO.R, O.add, O.mul, O.e, O.neg, Q.mul, Q.sub, Q.add, Q.conj, Q.neg] <;> omega

/-! ## Spuren und Farbdimension -/

/-- Reeller Basisvektor `eⱼ` in `ℂ ⊗ 𝕆`. -/
def b (j : Nat) : CO := ⟨O.e j, oz⟩

/-- Spur einer ℂ-linearen Abbildung über die ℂ-Basis `e₀..e₇`: (Realteil, Imaginärteil). -/
def tr (f : CO → CO) : Int × Int :=
  (List.range 8).foldl (fun acc j => (acc.1 + comp (f (b j)).u j, acc.2 + comp (f (b j)).w j)) (0, 0)

theorem traces :
    tr L = (0, 0) ∧ tr R = (0, 0) ∧ tr (fun x => L (R x)) = (4, 0) ∧
    sectors.map (fun s => tr (P4 s)) = [(4, 0), (12, 0), (12, 0), (4, 0)] := by decide

/-- Die Farbdimension von `QSFormal.Ladungen` ist der Rang `Sp P_s` des Sektor-Projektors. -/
theorem colourDim_from_trace : ∀ s ∈ sectors, tr (P4 s) = (4 * colourDim s, 0) := by decide

/-! ## Ladung und Platz-Gewichte auf den Sektoren -/

theorem Q6_on_sector : ∀ s ∈ sectors, ∀ x : CO, Q6 (P4 s x) = smul (q6 s) (P4 s x) := by
  intro s hs x
  obtain ⟨⟨⟨a0,a1,a2,a3⟩,⟨a4,a5,a6,a7⟩⟩, ⟨⟨b0,b1,b2,b3⟩,⟨b4,b5,b6,b7⟩⟩⟩ := x
  simp only [sectors, List.mem_cons, List.not_mem_nil, or_false] at hs
  rcases hs with rfl | rfl | rfl | rfl <;>
    simp [Q6, q6, P4, iL, iR, L, R, add, smul, osmul, CO.R, O.add, O.mul, O.e, O.neg,
      Q.mul, Q.sub, Q.add, Q.conj, Q.neg] <;> omega

theorem Delta_on_sector : ∀ s ∈ sectors, ∀ x : CO,
    Delta2 (P4 s x) = smul (weights s).2.1 (P4 s x) ∧ Delta3 (P4 s x) = smul (weights s).2.2 (P4 s x) := by
  intro s hs x
  obtain ⟨⟨⟨a0,a1,a2,a3⟩,⟨a4,a5,a6,a7⟩⟩, ⟨⟨b0,b1,b2,b3⟩,⟨b4,b5,b6,b7⟩⟩⟩ := x
  simp only [sectors, List.mem_cons, List.not_mem_nil, or_false] at hs
  rcases hs with rfl | rfl | rfl | rfl <;>
    simp [Delta2, Delta3, weights, P4, iL, iR, L, R, add, smul, osmul, CO.R, O.add, O.mul, O.e, O.neg,
      Q.mul, Q.sub, Q.add, Q.conj, Q.neg] <;> omega

/-! ## Der Frame T -/

def neg (x : CO) : CO := ⟨O.neg x.u, O.neg x.w⟩

theorem T_iL (x : CO) : CO.T (iL x) = neg (iL (CO.T x)) := by
  obtain ⟨⟨⟨a0,a1,a2,a3⟩,⟨a4,a5,a6,a7⟩⟩, ⟨⟨b0,b1,b2,b3⟩,⟨b4,b5,b6,b7⟩⟩⟩ := x
  simp [neg, iL, L, CO.R, CO.T, O.mul, O.e, O.neg, Q.mul, Q.sub, Q.add, Q.conj, Q.neg]

theorem T_iR (x : CO) : CO.T (iR x) = neg (iR (CO.T x)) := by
  obtain ⟨⟨⟨a0,a1,a2,a3⟩,⟨a4,a5,a6,a7⟩⟩, ⟨⟨b0,b1,b2,b3⟩,⟨b4,b5,b6,b7⟩⟩⟩ := x
  simp [neg, iR, R, CO.R, CO.T, O.mul, O.e, O.neg, Q.mul, Q.sub, Q.add, Q.conj, Q.neg]

/-- r34.1(d) aus der Struktur: `T P_s T⁻¹ = P_{T s}`, Ladungskonjugation `Q ↦ 1 − Q`. -/
theorem T_P4 : ∀ s ∈ sectors, ∀ x : CO, CO.T (P4 s x) = P4 (frameT s) (CO.T x) := by
  intro s hs x
  obtain ⟨⟨⟨a0,a1,a2,a3⟩,⟨a4,a5,a6,a7⟩⟩, ⟨⟨b0,b1,b2,b3⟩,⟨b4,b5,b6,b7⟩⟩⟩ := x
  simp only [sectors, List.mem_cons, List.not_mem_nil, or_false] at hs
  rcases hs with rfl | rfl | rfl | rfl <;>
    simp [frameT, P4, iL, iR, L, R, add, smul, osmul, CO.R, CO.T, O.add, O.mul, O.e, O.neg,
      Q.mul, Q.sub, Q.add, Q.conj, Q.neg] <;> omega

/-! ## Die Farbdrehung σ bleibt in jedem Sektor -/

def sc (x : CO) : CO := ⟨applySP sigmaImg x.u, applySP sigmaImg x.w⟩

theorem sigma_comm_basis : ∀ j < 8,
    sc (iL (b j)) = iL (sc (b j)) ∧ sc (iR (b j)) = iR (sc (b j)) ∧
    ∀ s ∈ sectors, sc (P4 s (b j)) = P4 s (sc (b j)) := by decide

/-! ## r49 (H33): Die e₇-Achse trägt B − L, nicht die elektrische Ladung -/

/-- `3(B − L)` der Zustände eines Sektors nach der Teilchen-Zuordnung von r42.1(b): (ν, e) −3, (d^c, u^c) −1, (u, d) 1, (e^c, ν^c) 3. -/
def bl3 (s : Sector) : Int :=
  if s = ⟨1, 1⟩ then -3 else if s = ⟨-1, 1⟩ then -1 else if s = ⟨1, -1⟩ then 1 else 3

/-- H33b: `6(Q − ½) = 3(B − L)`; mit `J = iL_{e₇}`, `s = −½`: `Y/2 = (B − L)/2 + T₃^R` und `Q_em = T₃^L + T₃^R + (B − L)/2`
(alles mal 6, `T₃^L = C T₃`, `T₃^R = (1 − C) T₃`). -/
theorem b_minus_l : ∀ st ∈ states,
    q6 st.1 - 3 = bl3 st.1 ∧
    y6 ⟨1, true⟩ (-3) st = bl3 st.1 + (if inImage ⟨1, true⟩ st.1 then 0 else st.2) ∧
    qem6 st = (if inImage ⟨1, true⟩ st.1 then st.2 else 0) + (if inImage ⟨1, true⟩ st.1 then 0 else st.2) + bl3 st.1 := by
  decide

/-- H33c: `Q_em` ist keine Funktion des Sektors; jeder Operator aus `1, iL, iR` ist es (`P4_eigen`), also kann keiner `Q_em` sein. -/
theorem qem_not_sector_function : ∃ a ∈ states, ∃ b ∈ states, a.1 = b.1 ∧ qem6 a ≠ qem6 b := by decide

end QSFormal.Sektoren
