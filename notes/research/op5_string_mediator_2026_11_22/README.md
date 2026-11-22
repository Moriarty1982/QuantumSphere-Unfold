# Gespannter String als Vermittler des OP5-Falls: trägt teilweise (Erkundung, nicht blind, 22.11.2026)

**Ergebnis in einem Satz:** Ein zwischen M- und T-System gespannter String, dessen Spannung vom Higgsradius abhängt, liefert Rahmen
(Ruhesystem der Endpunkte) und Achse (Spannrichtung) selbst. Seine Zwei-Quanten-Zustände der Grundmode geben einen Pol bei 2ω₁ mit dem
Residuum ∝ a_⊥² − a_⊥x + x²/2. Die gerichteten Anteile stimmen damit exakt mit N_m = ⅔(x² − a_⊥x + a_⊥²) überein, der ungerichtete Anteil
x² ist halb so groß. Dazu kommt ein zweiter Pol bei ω₁ mit Zähler a_⊥. **Nach dem vorab festgelegten Raster: trägt teilweise.**

Auftrag des Autors: „weg c“. Verfahren vorab: `Methoden_Notiz.md` (Commit 7ecb9fce), mit den Annahmen S1 (Nambu–Goto-String zwischen den
Systemen, feste Enden), S2 (Spannung T₀(1 + τη/v)) und S3 (langwellig längs der Achse, k_zL ≪ 1). Skript `string_mediator.wl`, Ausgabe
`run/string_mediator.txt`, Wolfram exakt im Fock-Raum zweier Oszillatoren. Keine H-Nummer.

## Ergebnis
| Schritt | Befund |
|---|---|
| Kopplung | Aus −∫T(h(X))√(−γ): Ein-Quanten-Term ∝ i k_⊥·q, Zwei-Quanten-Term ½(τ/v)η[k_ik_jq^iq^j + q̇² − ω₁²q²]. Mode 2 koppelt nicht (∫s₂ = 0). |
| (1) Pol bei ω₁ | Amplituden ∝ i k_i; Residuum a_⊥ c₁²T₀τ²/v² mit c₁ = 2√(2L)/π: gerichteter Vektor, Zähler a_⊥ (wie r35). |
| (2) Pol bei 2ω₁ | Amplituden ∝ k_ik_j − 2ω₁²δ_ij; Residuum τ²(a_⊥² − 4a_⊥ω₁² + 8ω₁⁴)/(2v²ω₁). Am Pol x = 4ω₁²: ∝ 2a_⊥² − 2a_⊥x + x². |
| Vergleich | Auf den a_⊥²-Koeffizienten von N_m skaliert: ⅔a_⊥² − ⅔a_⊥x + ⅓x². Differenz zu N_m: −⅓x². |

## Lesart
- Der String beantwortet die offene Frage von r36 zur Hälfte: Rahmen und Achse sind keine Setzung mehr, sondern Ruhesystem und Richtung des
  gespannten Strings. Die Polarisationsstruktur folgt aus seinen Querschwingungen, ohne Wahl.
- Die beiden gerichteten Anteile von N_m (a_⊥² und −a_⊥x) kommen im Verhältnis exakt heraus. Der Mischterm entsteht aus der Spannungsänderung
  (Ẋ² − X′²), die auf die Spur wirkt, gegen die Krümmung von η quer zur Achse (k_ik_j).
- Abweichend: der ungerichtete Anteil (⅓x² statt ⅔x²) und ein zusätzlicher Pol bei ω₁ mit Zähler a_⊥. Das Verhältnis der Polmassen 1 : 2 ist
  eine Vorhersage dieses Bildes.
- Annahmen S1–S3 sind gesetzt; insbesondere ist die Abhängigkeit der Spannung vom Higgsradius (S2) nicht hergeleitet. Die Zahlenfolge der
  Konnektoren aus I1 (Stufen N = 0, 1, 2) wird hier nicht geprüft.
- OP5 und H96 bleiben offen.
