import QSFormal.StateDisk
import Mathlib.Analysis.SpecialFunctions.BinaryEntropy
import Mathlib.Analysis.SpecialFunctions.Trigonometric.ArctanDeriv
import Mathlib.Analysis.SpecialFunctions.Trigonometric.DerivHyp
import Mathlib.MeasureTheory.Integral.IntervalIntegral.FundThmCalculus

/-!
# Entropie und Bures-Abstand der Zustandsscheibe

Formalisiert aus `Quantum_Sphaera_Companion_v4_8_0_source.tex`, Theoremlet v4.9.0-r17.2
(`subsec:v490-r17-entropy`), für einen Zustand mit `|b| = 1/cosh 2η`:

* die Entropie `S = −p₊ log₂ p₊ − p₋ log₂ p₋` ist `0` bei `η = 0`, wächst streng mit `η ≥ 0`
  und bleibt unter `1` Bit; `1` Bit genau beim Photon `p₊ = p₋ = ½`;
* mit `r = sech 2η` ist `¼ (dr/dη)²/(1 − r²) = sech² 2η`, also das radiale Linienelement der
  Bures-Metrik `ds = sech 2η dη`;
* `∫₀^η sech 2x dx = ½ gd(2η)` mit `gd t = arctan (sinh t)`, und dieser Abstand bleibt unter
  `π/4`.

Nicht formalisiert: die Grenzwerte `S → 1` Bit und Abstand `→ π/4` für `η → ∞`, sowie die
Zahlenwerte `0,811` und `0,781` Bit.
-/

namespace QSFormal.Entropy

open Real Set

/-- Der kleinere Eigenwert `p₋ = ½(1 − 1/cosh 2η)`. -/
noncomputable def pMinus (η : ℝ) : ℝ := (1 - 1 / cosh (2 * η)) / 2

/-- Die Entropie in Bit. `binEntropy p = −p log p − (1−p) log (1−p)`, natürlicher Logarithmus. -/
noncomputable def S (η : ℝ) : ℝ := binEntropy (pMinus η) / log 2

theorem pMinus_zero : pMinus 0 = 0 := by simp [pMinus]

theorem pMinus_mem (η : ℝ) : pMinus η ∈ Ico 0 (1 / 2) := by
  have hc : 1 ≤ cosh (2 * η) := one_le_cosh _
  have hp : 0 < 1 / cosh (2 * η) := by positivity
  have hq : 1 / cosh (2 * η) ≤ 1 := by rw [div_le_one (by positivity)]; exact hc
  constructor <;> simp only [pMinus] <;> linarith

theorem pMinus_strictMonoOn : StrictMonoOn pMinus (Ici 0) := by
  intro a ha b hb hab
  have hlt : cosh (2 * a) < cosh (2 * b) := by
    rw [cosh_lt_cosh, abs_of_nonneg (by simp at ha; linarith),
      abs_of_nonneg (by simp at hb; linarith)]
    linarith
  have hpos : 0 < cosh (2 * a) := cosh_pos _
  have : 1 / cosh (2 * b) < 1 / cosh (2 * a) := one_div_lt_one_div_of_lt hpos hlt
  simp only [pMinus]
  linarith

theorem S_zero : S 0 = 0 := by simp [S, pMinus_zero]

/-- Die Entropie wächst streng mit dem Abstand vom Frame `E ∥ B`. -/
theorem S_strictMonoOn : StrictMonoOn S (Ici 0) := by
  intro a ha b hb hab
  have hm : ∀ η, pMinus η ∈ Icc (0 : ℝ) 2⁻¹ := fun η =>
    ⟨(pMinus_mem η).1, by have := (pMinus_mem η).2; norm_num at this ⊢; linarith⟩
  have := binEntropy_strictMonoOn (hm a) (hm b) (pMinus_strictMonoOn ha hb hab)
  exact div_lt_div_of_pos_right this (log_pos (by norm_num))

/-- Für jedes endliche `η` bleibt die Entropie unter `1` Bit. -/
theorem S_lt_one (η : ℝ) : S η < 1 := by
  have h : pMinus η ≠ 2⁻¹ := by
    have := (pMinus_mem η).2; norm_num at this ⊢; linarith
  rw [S, div_lt_one (log_pos (by norm_num))]
  exact binEntropy_lt_log_two.mpr h

/-- Das Photon, `p₊ = p₋ = ½`, hat genau `1` Bit. -/
theorem photon_one_bit : binEntropy (1 / 2) / log 2 = 1 := by
  rw [one_div, binEntropy_two_inv, div_self (log_pos (by norm_num)).ne']

/-! ## Bures-Abstand -/

/-- `r(η) = sech 2η`. -/
noncomputable def r (η : ℝ) : ℝ := 1 / cosh (2 * η)

theorem hasDerivAt_r (η : ℝ) :
    HasDerivAt r (-(2 * sinh (2 * η)) / cosh (2 * η) ^ 2) η := by
  have h := ((hasDerivAt_cosh (2 * η)).comp η ((hasDerivAt_id η).const_mul 2)).inv
    (cosh_pos _).ne'
  convert h using 1
  · ext x; simp [r]
  · simp; ring

/-- Das radiale Linienelement der Bures-Metrik `ds² = ¼ dr²/(1 − r²)` ist `sech² 2η dη²`. -/
theorem bures_radial (η : ℝ) (hη : η ≠ 0) :
    (1 / 4) * (-(2 * sinh (2 * η)) / cosh (2 * η) ^ 2) ^ 2 / (1 - r η ^ 2)
      = (1 / cosh (2 * η)) ^ 2 := by
  have hc : cosh (2 * η) ≠ 0 := (cosh_pos _).ne'
  have hsq : cosh (2 * η) ^ 2 = sinh (2 * η) ^ 2 + 1 := cosh_sq _
  have hc1 : 1 < cosh (2 * η) := one_lt_cosh.mpr (by intro h; apply hη; linarith)
  have hs : sinh (2 * η) ^ 2 ≠ 0 := by nlinarith
  simp only [r]
  rw [show 1 - (1 / cosh (2 * η)) ^ 2 = sinh (2 * η) ^ 2 / cosh (2 * η) ^ 2 by
    field_simp; linarith]
  field_simp; ring

/-- Der Bures-Abstand `½ gd(2η)` mit `gd t = arctan (sinh t)`. -/
noncomputable def dist (η : ℝ) : ℝ := arctan (sinh (2 * η)) / 2

theorem hasDerivAt_dist (η : ℝ) : HasDerivAt dist (1 / cosh (2 * η)) η := by
  have h := (((hasDerivAt_sinh (2 * η)).comp η ((hasDerivAt_id η).const_mul 2)).arctan).div_const 2
  have hc : cosh (2 * η) ≠ 0 := (cosh_pos _).ne'
  have hsq : cosh (2 * η) ^ 2 = sinh (2 * η) ^ 2 + 1 := cosh_sq _
  convert h using 1
  · ext x; simp [dist]
  · simp only [Function.comp_apply]
    rw [show 1 + sinh (2 * η) ^ 2 = cosh (2 * η) ^ 2 by linarith]
    field_simp

/-- `∫₀^η sech 2x dx = ½ gd(2η)`. -/
theorem integral_sech (η : ℝ) : ∫ x in (0 : ℝ)..η, 1 / cosh (2 * x) = dist η := by
  have hcont : Continuous fun x : ℝ => 1 / cosh (2 * x) :=
    continuous_const.div (by fun_prop) fun x => (cosh_pos _).ne'
  rw [intervalIntegral.integral_eq_sub_of_hasDerivAt (fun x _ => hasDerivAt_dist x)
    (hcont.intervalIntegrable _ _)]
  simp [dist]

/-- Der Abstand bleibt unter `π/4`: das Photon liegt in endlichem Abstand, wird aber bei
endlichem `η` nicht erreicht. -/
theorem dist_lt (η : ℝ) : dist η < π / 4 := by
  have := arctan_lt_pi_div_two (sinh (2 * η))
  simp only [dist]
  linarith

end QSFormal.Entropy
