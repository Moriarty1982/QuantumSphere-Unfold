# Erkundung: Woher kommt ein Fluss von 2/3 rad durch das Platzdreieck der geladenen Leptonen?

13. November 2026, spät. Autorenauftrag: „Fluss 2/3 rad suchen“. Erkundung, **nicht blind** (Zielwert bekannt), kein
Test. Keine H-Nummer. Skript `op3_flux_two_thirds_2026_11_13.py`, Ausgabe `..._out.txt`.

## Vorwissen geprüft
- `op3_selection_principle_2026_11_13.md`: Nur ein Fluss erhält Koide; geladene Leptonen tragen Φ_e = 3θ_e = 0,666674,
  vom Oktanten (π/4) aus ΔΦ = 0,118724.
- v4.8.0-r11 (H1): δ = K/3 bzw. 2/9 widerlegt (Quarks, laufende Massen); gilt nur bei Polmassen (Kalibrierung).
- `op3_phase_source_search_2026_11_12.md`: native ρ-ungerade Größen (Chiralität, Assoziator, Q_J, Frame-Versatz) tragen
  keinen Betrag. η-Notiz: native Phasen nur Vielfache von π/6.
- Annahmenliste r08: native Zahlen γ_BI = 0,237533 (L1, Literatur, kalibriert), γ_string, γ_L, β_sym, Ω_M, η, ε, β₄.

## Ergebnis
1. **Mechanismen für einen nicht quantisierten Fluss.** (a) Berry-Phase: Als Qubit-Phase verlangt Φ_e einen Raumwinkel von
   4/3 sr (der Oktant hat π/2). (b) U(1)-Fluss mit stetigem Feld. (c) Selbstbezug Φ = K (Brannens δ = K/3): von H1 als
   allgemeines Gesetz widerlegt. Keiner ist im Companion angelegt.
2. **Fester Scan nativer Zahlen** (Liste im Skript vor dem Vergleich festgelegt): 11 Konstanten × 7 einfache Faktoren ×
   2 Ziele = 154 Versuche, Fenster 1 %. **Ein Treffer:** ΔΦ = γ_BI/2 = 0,118766 gegen 0,118724 (+0,036 %). Bei zufälligen
   Werten wären 0,34 Treffer zu erwarten; ein einzelner Treffer ist also nicht auffällig.
3. **Schärfe des Treffers.** Nimmt man θ aus der Beziehung, θ = (π/4 − γ_BI/2)/3 = 0,2222106, und legt ρ² über das genau
   bekannte m_e/m_μ fest, folgen ρ² = 0,500014, K = 0,666676 und **m_τ = 1777,13 MeV** (PDG 1776,93 ± 0,09: **+2,3σ**).
   Exaktes Koide mit m_e, m_μ gibt dagegen 1776,97 MeV. Die Beziehung steht also bereits in Spannung mit m_τ.
4. **Abhängigkeit von der Zählweise.** γ_BI hängt von der Zählung ab: 0,2375 (Domagała–Lewandowski/Meissner, im Companion
   L1) passt, 0,2740 (ABCK, SU(2)) und γ_string geben 0,137 bzw. 0,064. Der Treffer hängt an der Wahl, die der Companion
   für die Lepton-Zählung schon getroffen hat.

## Bewertung
- Eine native Quelle für 2/3 rad ist nicht gefunden. Der einzige Scan-Treffer, ΔΦ = γ_BI/2 (Fluss vom Qubit-Oktanten zu den
  geladenen Leptonen gleich dem halben Barbero-Immirzi-Parameter), ist nachträglich, statistisch unauffällig und liegt
  bei 2,3σ gegen m_τ.
- Er ist aber scharf prüfbar: Er verlangt m_τ = 1777,13 MeV. Ein künftiger Wert von m_τ (Belle II, BES III) entscheidet;
  dafür wäre eine eigene Vorab-Notiz nötig. Ein Mechanismus, der γ_BI als Fluss durch das Generationsdreieck ausweist, fehlt.
- OP3/OP4 offen; OP1–OP5, C5, C6/T2 unverändert; H100 unberührt.
