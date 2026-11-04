# Notiz: Was „mod HC“ und P_C7 in den Quellen bedeuten (Fundstellen, 5. November 2026)

**Status: Quellenprüfung, keine Rechnung.** Anlass: Test Tr(M₁₆ P_C7) ≡ 0 mod HC in `Wirkung_W1_Dixon_U1.md`; Autorhinweis „in den Dateien nachsehen“.

## Fundstellen (Monolith = `Quantum_Sphaera_Companion_v4_8_0_source.tex`)
- **Z. 7703** (`def` Meta-Septum closure, Teil 10, GitHub Z. 1955): Tr(M₁₆ P_C7) ≡ 0 (mod HC) wählt den „admissible septonic cluster“. Keine Definition der Kongruenz.
- **Z. 7887** (`prop:closure-equation`): dieselbe Bedingung, dynamisch H_C = Λ[M₁₆, P_C7]; „stabile Sondenzustände liegen genau im C₇-Sektor“.
- **Z. ~7993–8040** (`sec:closure-field-system`): Restterm 𝔑_C = (1 − P)M₁₆P + PM₁₆(1 − P); `prop:equivalent-closure-criteria`: 𝔑_C = 0 ⇔ [M₁₆, P_C7] = 0 ⇔ M₁₆ blockdiagonal in im P ⊕ ker P. `thm:closed-master-system` verlangt zusätzlich **(1 − P_C7)Ψ = 0**.
- **Z. 17712, 21900:** „bis auf Kompensator-Projektion“, „HC-kompensierter Transport“; die Klasse K_ncl identifiziert Träger bis auf HC-kompensierten Transport, zulässigen Frame-Versatz und zulässige Verfeinerung. Das ist die einzige Stelle, die eine Äquivalenz „modulo HC“ beschreibt, und auch sie nur verbal.
- **`native-operator-link.tex`** (v4.8.0): „Die Meta-Septum-Definition legt einen zulässigen Projektor durch eine Spurbedingung modulo HC fest; sie nennt seine Einträge nicht.“ Und: **„Der HC-Projektor C bleibt von P verschieden.“**
- **`analysis/OP5_M16_PC7_Frame_Origin_Audit.md`:** Strukturkern (Teil 12, T1–T4) verlangt J² = 1, C² = C, [M, J] = [M, C] = 0; P_C7 durch Tr(M₁₆P) mod HC, P² = P, PΨ = Ψ; keine Eigenvektoren, keine Orientierung zum Taktgeber.

## Ergebnis
1. **„mod HC“ ist nirgends als Rechenregel definiert.** Operativ wird die Schließung im Companion durch das Kommutator-Kriterium [M₁₆, P_C7] = 0 (Blockdiagonalität) und durch (1 − P_C7)Ψ = 0 ausgedrückt. Die Spurbedingung kommt in keiner Rechnung vor.
2. **HC und P_C7 sind im Companion zwei verschiedene Projektoren.** C (Kompensator, C = ½(1 + J)) gehört zum Strukturkern mit [M, C] = 0; P_C7 ist der Schließungsprojektor. Der eigene Text in v4.8.0 sagt ausdrücklich, dass beide verschieden sind.
3. **Folge für W1:** Die Gleichsetzung P_C7 := C_ch in Entscheidung 5 (mein Vorschlag) verwechselt beide. C_ch hat die Form des **Kompensators** (r42.1(e): Spektralprojektor von 𝓜 = λ₀C_ch + λ₁(1 − C_ch)); in W1 spielt er richtig die Rolle des HC (Chiralität), und [𝓜, C_ch] = 0 gilt. P_C7 bleibt offen. Mit (1 − P_C7)Ψ = 0 kann P_C7 nicht C_ch sein, sonst fielen die Singuletts weg (k171).
4. Eine mögliche Lesart von „mod HC“ (nicht aus den Quellen, nur Vorschlag): Die Spur wird nur auf dem von C nicht erfassten Teil gezählt, also modulo Beiträgen, die der Kompensator ausgleicht. Das müsste der Autor bestätigen oder verwerfen.
