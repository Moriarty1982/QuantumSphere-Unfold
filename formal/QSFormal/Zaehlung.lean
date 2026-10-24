import Mathlib

/-!
# Zählregeln und Tachyon-Boden (v4.9.0-r63)

Formalisiert aus `Quantum_Sphaera_Companion_v4_8_0_source.tex`, Runde v4.9.0-r63:

* **Robertson-Sättigung.** Für einen Drehimpulszustand `|j, m⟩` (ħ = 1) ist
  `⟨Jx²⟩ + ⟨Jy²⟩ = j(j+1) − m²` und `⟨Jx⟩ = ⟨Jy⟩ = 0`, `ΔJx = ΔJy`; die Robertson-Schranke
  `ΔJx·ΔJy ≥ |⟨Jz⟩|/2` lautet damit `|m| ≤ j(j+1) − m²`. Gleichheit gilt genau für `|m| = j`,
  also für die zwei Zustände `m = ±j`. Das ist das Gewicht 2 der Zählung von Domagała–Lewandowski
  und Meissner (H47). Bei `j = ½` ist `ΔJx = ½`.
  Die Operatorwerte selbst stehen nicht in Lean; sie sind in `llm/k103_robertson_tachyon.py`
  für `j ≤ 6` exakt nachgerechnet. Hier steht die Arithmetik.
* **Tachyon am Boden.** Ein Tachyon mit `E = 0`, `p = μ` erscheint nach einem Boost mit
  Geschwindigkeit `u` (`γ²(1 − u²) = 1`) mit `E' = −γuμ`, `p' = γμ`, also `v' = p'/E' = −1/u`
  und negativer Energie; die Invariante `E² − p² = −μ²` bleibt.
-/

namespace QSFormal.Zaehlung

open Real

/-! ## Robertson-Sättigung -/

/-- `⟨Jx²⟩ + ⟨Jy²⟩` im Zustand `|j, m⟩` (ħ = 1). -/
def perp (j m : ℝ) : ℝ := j * (j + 1) - m ^ 2

theorem perp_sub_abs (j m : ℝ) : perp j m - |m| = (j - |m|) * (j + |m| + 1) := by
  unfold perp
  rw [← sq_abs m]
  ring

variable {j m : ℝ}

/-- Robertson-Schranke `ΔJx·ΔJy ≥ |⟨Jz⟩|/2`, ausgeschrieben für `|j, m⟩`. -/
theorem robertson (hm : |m| ≤ j) : |m| ≤ perp j m := by
  have e := perp_sub_abs j m
  have h1 : 0 ≤ j - |m| := by linarith
  have h2 : 0 ≤ j + |m| + 1 := by linarith [abs_nonneg m]
  have h3 := mul_nonneg h1 h2
  linarith

/-- Die Schranke ist genau für `|m| = j` gesättigt. -/
theorem robertson_eq_iff (hm : |m| ≤ j) : perp j m = |m| ↔ |m| = j := by
  constructor
  · intro h
    have e := perp_sub_abs j m
    have hz : (j - |m|) * (j + |m| + 1) = 0 := by rw [← e, h, sub_self]
    have hp : 0 < j + |m| + 1 := by linarith [abs_nonneg m]
    rcases mul_eq_zero.mp hz with h1 | h1 <;> linarith
  · intro h
    have e := perp_sub_abs j m
    rw [h] at e ⊢
    have hz : (j - j) * (j + j + 1) = 0 := by ring
    linarith

/-- Gesättigt sind genau die zwei Zustände `m = ±j`. -/
theorem saturating_iff (hj : 0 ≤ j) : |m| = j ↔ m = j ∨ m = -j := abs_eq hj

/-- Bei `j = ½` ist die transversale Varianz je Achse `(½)²`, also `ΔJx = ½`. -/
theorem spin_half_sd : perp (1 / 2) (1 / 2) / 2 = (1 / 2) ^ 2 := by norm_num [perp]

/-- Nicht jeder Zustand ist minimal: `|1, 0⟩` liegt über der Schranke. -/
theorem spin_one_zero_not_saturating : perp 1 0 ≠ |(0 : ℝ)| := by norm_num [perp]

/-! ## Tachyon am Boden -/

variable {u γ μ : ℝ}

/-- Die Invariante `E² − p² = −μ²` bleibt unter dem Boost. -/
theorem floor_invariant (hγ : γ ^ 2 * (1 - u ^ 2) = 1) :
    (γ * (0 - u * μ)) ^ 2 - (γ * (μ - u * 0)) ^ 2 = -μ ^ 2 := by
  linear_combination (-μ ^ 2) * hγ

/-- Der Boden `E = 0` erscheint mit Geschwindigkeit `−1/u`. -/
theorem floor_speed (hu : u ≠ 0) (hγ : γ ≠ 0) (hμ : μ ≠ 0) :
    (γ * (μ - u * 0)) / (γ * (0 - u * μ)) = -1 / u := by
  have hden : γ * (0 - u * μ) ≠ 0 := by
    have e : γ * (0 - u * μ) = -(γ * u * μ) := by ring
    rw [e]
    exact neg_ne_zero.mpr (mul_ne_zero (mul_ne_zero hγ hu) hμ)
  rw [div_eq_iff hden]
  rw [show -1 / u * (γ * (0 - u * μ)) = γ * μ * (u / u) by ring, div_self hu]
  ring

/-- Für `u, γ, μ > 0` hat der Boden im bewegten Frame negative Energie. -/
theorem floor_energy_neg (hu : 0 < u) (hγ : 0 < γ) (hμ : 0 < μ) :
    γ * (0 - u * μ) < 0 := by
  have h := mul_pos (mul_pos hγ hu) hμ
  have e : γ * (0 - u * μ) = -(γ * u * μ) := by ring
  rw [e]
  linarith

end QSFormal.Zaehlung
