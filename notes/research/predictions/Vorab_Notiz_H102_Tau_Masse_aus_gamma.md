# Vorab-Notiz H102: Die Tau-Masse aus dem Fluss π/4 − γ_M/2

**Stand:** 13. November 2026, spät, vor dem Erscheinen der geprüften Daten festgelegt. Autorenauftrag: „H102 festschreiben“.
Blind gegenüber künftigen Daten; **nicht blind** gegenüber dem heutigen Wert von m_τ, aus dessen Vergleich die Beziehung
nachträglich gefunden wurde (Scan mit 154 Versuchen, ein Treffer, 0,34 zufällig erwartet). Skript `k224_test_h102.py`.

## Vorwissen geprüft
- `../op3_flux_two_thirds_2026_11_13.md`: Scan-Treffer ΔΦ = γ_BI/2; Mechanismus-Suche ohne Herleitung (γ_M nativ aus der
  Zählregel des Materie-Frames, Lesarten als Spin-1/2-Phase mit unbegründeter Einheit).
- `../op3_selection_principle_2026_11_13.md`: Nur ein Fluss erhält Koide; Oktant (π/4) und Abstand der geladenen Leptonen.
- v4.8.0-r11 (H1): δ = 2/9 nur bei Polmassen; v4.10.0-r09/r10 (Zählregel je Frame).

## Vorhersage
- Beziehung: Φ_e = 3θ_e = π/4 − γ_M/2 mit γ_M = 0,237533 aus der Zählregel (alle Spins, Gewicht 2), also θ_e = 0,2222106.
- Mit ρ² aus dem genau bekannten Verhältnis m_e/m_μ (0,51099895 und 105,6583755 MeV) folgen ρ² = 0,5000140 und
  **m_τ = 1777,134 MeV** (Unsicherheit aus m_e und m_μ unter 0,001 MeV).
- Vergleichswert: exaktes Koide aus m_e und m_μ gibt m_τ = 1776,969 MeV.

## Daten
- Die erste Ausgabe der Particle Data Group (Review oder Online-Aktualisierung), die **nach dem 13. November 2026** erscheint,
  mit ihrem Mittelwert für m_τ und dessen Unsicherheit. Ältere Werte zählen nicht, auch wenn sie heute schon veröffentlicht,
  aber hier nicht eingesehen sind (benutzt wurde PDG 2024, 1776,93 ± 0,09 MeV).
- Erscheint bis 31. Dezember 2028 keine solche Ausgabe, entfällt H102 ohne Ersatz.

## Entscheidungskriterium
- z = (1777,134 − m_τ,obs)/σ_obs. **Bestätigt (verträglich)** bei |z| ≤ 2, sonst **widerlegt**.
- **Trennend gegen exaktes Koide** nur, wenn zugleich |z| ≤ 2 und |(1776,969 − m_τ,obs)/σ_obs| > 2.

## Erwartung (nicht Teil des Kriteriums)
Bleibt der Mittelwert bei 1776,93 MeV und fällt σ auf etwa 0,07 MeV, wäre z ≈ +2,9 (widerlegt). Die Beziehung hat also
schon heute Gegenwind (+2,3σ).

## Offenlegung
- Nachträglich gefunden, mit bekanntem m_τ; kein Mechanismus hergeleitet. Gezählt wird nur der Vergleich mit künftigen Daten.
- Die Beziehung hängt an der Zählregel des Companion (γ_M); andere γ-Werte der Literatur geben sie nicht.
