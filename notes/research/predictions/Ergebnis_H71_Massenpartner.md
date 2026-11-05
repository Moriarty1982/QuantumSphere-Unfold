# Ergebnis H71: Kein massiver Partner erfüllt die K-Bilanz; der Partner negativer Norm macht die Masse tachyonisch

**5. November 2026. Vorab-Notiz `Vorab_Notiz_H71_Massenpartner.md` (Commit 4a3b802). Skript `k179_test_h71.py`, Ausgabe `k179_out.json`. Status: H71a und H71b bestätigt (nicht blind), H71c widerlegt.** Offenlegung: Dass j_z in V2 nie verschwindet, ist mir beim Schreiben des Skripts nach dem Commit der Notiz aufgefallen (j_z = −λ(|ψ|² + |χ|²)); die Rechnung bestätigt es.

## Kontrollen (gültig)
Feldgleichungen ≤ 9e-15; ∂^μT_μν = 0 für Überlagerungen zweier Moden relativ 1,2e-9 (V1 und V2).

## Ergebnis
- **H71a bestätigt:** V1 hat ω² = k² + m², V2 hat ω² = k² − m² (Residuen ≤ 4e-15). Ein Partner negativer Norm, über die Masse gekoppelt, macht die Mode tachyonisch: Für |k| < m gibt es keine reelle Frequenz, bei |k| = m ist ω = 0.
- **H71b bestätigt:** In V1 ist j⁰ = |ψ|² + |χ|² > 0 für alle Moden. Die K-Bedingung ist verletzt, ebenso im ungekoppelten Spiegelsektor V3, dessen Ströme sich nur addieren.
- **H71c widerlegt:** In V2 ist |j|/(|ψ|² + |χ|²) = 1 für alle Moden, weit über 1e-3. Der Strom ist dort **raumartig** (|j_z| > |j⁰|), wie für einen Tachyon zu erwarten, verschwindet aber nie.
- **Energie-Impuls (ohne Kriterium):**
  - V1: T_tt > 0, Spur > 0, materieartig.
  - V2: Die Mode λ = +1 hat negative Energiedichte (T_tt = −22 bei k = 2), die Mode λ = −1 positive; die Spur hat je nach Mode beide Vorzeichen.
  - Keine einzelne Mode hat T ∝ η, also gibt es keinen Λ-artigen Beitrag. T_xx = 0 überall.
- **Gewichtsverhältnis** |χ|²/|ψ|² = (ω + kλ)²/m² hängt vom Impuls ab. Eine strukturelle Übereinstimmung mit p₋/p₊ = β_sym² gibt es nicht.

## Lesart
1. **Tachyonbild mit Masse = Tachyon.** Koppelt man Materie über eine Masse an ihr Tachyonbild mit dem Vorzeichen aus F3, entsteht genau die tachyonische Dirac-Gleichung: überlichtschnelle Moden, raumartiger Strom, Energie mit beiden Vorzeichen. Das ist eine innere Bestätigung der Frame-Zuordnung. Das Vorzeichen aus F3 macht aus der Masse eine Tachyonmasse.
2. **Die K-Bilanz trägt nur masselos.** Mit Masse erfüllt keine Partner-Variante die Bedingung der komplexen Lesart: weder Antiteilchen noch gekoppeltes Spiegelteilchen (V1), noch Tachyonbild (V2), noch ungekoppelter Spiegelsektor (V3). Die neutrale M–T-Paarung aus H69 und H70 ist damit ein Merkmal masseloser Felder.
3. **Spiegelteilchen (Autoridee):** Klassisch ist ein über die Masse gekoppelter Spiegelpartner dasselbe wie ein gewöhnlicher Dirac-Partner. Als ungekoppelter Sektor (Lee–Yang) trägt er positive Energie und wäre ein Kandidat für dunkle Materie, nicht für Λ. Eine Vorhersage für sein Gewicht ergibt sich hier nicht.
4. **OP5:** Kein Λ-artiger Term aus einzelnen Moden. Ein Vakuumbeitrag bräuchte eine Konfiguration mit T ∝ η, also gleiche Spannung in allen Richtungen und Druck = −Dichte. Weder V1 noch V2 liefern das in einer Mode; ob eine Überlagerung tachyonischer Moden das kann, ist offen.
