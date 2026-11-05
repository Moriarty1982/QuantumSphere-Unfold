# Vorab-Notiz H77: Welche Lesart des Tachyonbilds einer Wirkung ist mit r07, r20, r81 und F3 verträglich?

**Stand:** 5. November 2026, vor der Rechnung festgelegt. **Nicht blind:** Das erwartete Ergebnis steht unten und ist weitgehend analytisch absehbar; die Rechnung (sympy) macht es nachprüfbar. Autorentscheidung 5.11.: erst prüfen, dann zwischen A und B wählen.

## Vorwissen geprüft
- `llm/Erkundung_Lesarten_Tachyonbild.md` (Lesarten A, B; Geist-Kondensation unter B).
- r07.2 (v4.8.0): Dualitätsdrehung z ↦ iz, s ↦ −s; Tachyon-Sektor s < 0.
- r20.2 (v4.8.0): Rapidität η + iπ/2, Vierergeschwindigkeit u ↦ i·w mit w raumartig; cosh und sinh tauschen.
- r19, r22 (v4.9.0): Gewicht k, Umrechnung e^{kη}; F3: Phase (−1)^k nach T aus γ ↦ −γ; r22.2: Länge k = 3/2, ihr Quadrat Phase −1 (ℓ_T² = −λ_T²).
- r81 (k174): masseloses Tachyonbild mit Kinetik-Vorzeichen s_T = −1. H71: Partner negativer Norm, über die Masse gekoppelt, macht die Mode tachyonisch. r82.1(b): „gesamter Energie-Impuls-Tensor des Bildes wechselt das Vorzeichen, einschließlich der Vakuumenergie“ (Lesart A).
- Beobachtung vorab: Wendet man F3 nach Dimension auf *alle* Größen an (Felder, Impulse, Konstanten), ist jeder Term der Lagrangedichte (Dimension 4, Gewicht −6) phasenfrei; das ist ein komplexer Einheitenwechsel ohne Physik. Eine Lesart muss also festlegen, was fortgesetzt wird.

## Lesarten (reelle Variablen, ein Skalar χ, Materie L_M = ½(χ_t² − χ_x²) − ½m²χ²)
- **A (Energieparität):** L_A = −L_M.
- **B (Kinematik fortgesetzt, Konstanten fest):** X ↦ −X, Potential bleibt: L_B = −½(χ_t² − χ_x²) − ½m²χ².
- **B′ (Konstanten fortgesetzt, Kinematik fest):** m² ↦ −m²: L_B′ = ½(χ_t² − χ_x²) + ½m²χ² = −L_B.

## Kriterien (eine Lesart ist verträglich, wenn sie alle drei erfüllt)
- **K1 (r20.2, r07.2, H71):** Die Dispersion ist tachyonisch, ω² = k² − m² (raumartiger Impuls, Invariante mit gewechseltem Vorzeichen).
- **K2 (r81, k174):** Masselos gilt L_T = −L_M (Kinetik s_T = −1).
- **K3 (F3 auf Auslesegrößen, γ ↦ −γ; u ↦ iw macht ρ u u ↦ −ρ w w):** Eine laufende Mode (k > m) hat im Zeitmittel eine Energiedichte mit entgegengesetztem Vorzeichen zur Materie-Mode.

## Erwartung (nicht blind)
Nur B erfüllt K1–K3. A verletzt K1 (normale Dispersion ω² = k² + m², Geist statt Tachyon). B′ verletzt K2 und K3 (Kinetik und Energie mit Materie-Vorzeichen).

## Folge, vorab festgelegt
- Erfüllt nur B die Kriterien, so ist das Tachyonbild einer Wirkung nach B zu bilden. Dann behält ein Potential ohne Ableitungen sein Vorzeichen, auch V_min. **r82.1(b) (Aufhebung der Higgs-Vakuumenergie bei Photon-Gewichten) ist dann nicht gedeckt** und wird in der nächsten Runde korrigiert (append-only). r82.2, r82.3 (H74, H75) und H76 betreffen Oszillatoren, Flüssigkeiten bzw. masselose Quanten negativer Energie und werden einzeln auf ihre Abhängigkeit von A geprüft.
- Erfüllt A die Kriterien oder keine Lesart alle, bleibt r82.1(b) stehen bzw. die Frage geht an den Autor zurück.

Skript: `llm/k192_lesart_tachyonbild.py` (nach dem Commit dieser Notiz).
