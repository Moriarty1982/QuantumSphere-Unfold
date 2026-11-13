# Vorab-Notiz H100: Verhältnis der Neutrino-Massendifferenzen im nächsten globalen Fit

**Stand:** 13. November 2026, abends, vor dem Erscheinen der geprüften Daten festgelegt. Autorenauftrag: „vorher
festschreiben, wenn du nebenbei einen Erwartungswert rechnen willst, um das hinterher abzugleichen“. Blind gegenüber
den künftigen Daten; **nicht blind** gegenüber NuFIT 6.1, aus dem die Kandidaten B und C nach Kenntnis der Werte
gewonnen wurden (Gründe unter „Offenlegung“). Skript `k222_test_h100.py`.

## Vorwissen geprüft
- H2 (v4.8.0-r12): K = 2/3 für Neutrinos nur mit negativer Wurzel, normale Ordnung.
- H99 (Vorab 5b23c5a, k221): θ_ν = θ_e + π/12; H99a +1,31σ (NuFIT 6.0), H99b +1,80σ (NuFIT 6.1).
- `../op3_neutrino_phase_candidates_2026_11_13.md`: 24er-Raster; Skala (Pol oder Kopplung); Koide-Spannung; Sumino-Weg
  mit Exponent c; c = 1,8 ± 1,0.
- `../op3_slot_u3_gauging_2026_11_13.md`: Platzindex-U(3), Auslesung A, Zwei-Sonden-Block, Neutrino-Block; c = 1 aus den
  Familienladungen.
- `../nufit_verlauf_2026_11_13.py`: Verlauf 2012–2025; der heutige Bestwert ist die beste Schätzung künftiger Werte.

## Vorhersagen (R = Δm²₂₁/Δm²₃₁, normale Ordnung)

| | Annahme | R_pred | σ_pred (Spannweite der Rechenwahl) |
|---|---|---|---|
| A | H99, Polmassen: θ_ν = θ_e + π/12, ρ² = 1/2 | 0,030839 | 1·10⁻⁶ (m_τ) |
| B | eine Skala, Kopplungsseite: ρ_ν² = ρ_e²(M_Z), θ_ν = θ_e(M_Z) + θ_b(ρ_e²(M_Z)), MS-bar-Yukawas bei M_Z aus r11 | 0,030087 | 3·10⁻⁵ (Skala 5 GeV bis 1 TeV, α(0) oder α(M_Z)) |
| C | Sumino, c = 1: Struktur A; Neutrinomassen erhalten den Faktor exp(−Σ_i \|U_ik\|² ln Q_i), Q_i = 1 + (α/π)(1 + (3/2) ln(M_Z/m_i)), α = α(m_τ) = 1/133,47, PMNS aus NuFIT 6.1 (33,76°; 43,29°; 8,62°; 212°) | 0,030375 | 2·10⁻⁵ (α(0) bis α(M_Z)) |

Die Zahlen sind mit `python k222_test_h100.py` reproduzierbar und vor dem Commit dieser Notiz einmal ausgegeben worden.

## Daten
- Die **nächste NuFIT-Version nach 6.1** (6.2 oder höher), Parametertabelle von nu-fit.org, Spalte „with SK atmospheric
  data“ (IC24 oder deren Nachfolger), **normale Ordnung**, auch wenn die invertierte dort Bestfit sein sollte.
- Δm²₂₁ und Δm²₃ℓ (= Δm²₃₁ in NO) mit ±1σ; asymmetrische Fehler gemittelt. R_obs = Δm²₂₁/Δm²₃₁,
  σ_R aus den relativen Fehlern quadratisch addiert (wie H99).
- Erscheint bis 31.12.2027 keine neue NuFIT-Version, entfällt H100 ohne Ersatz.

## Entscheidungskriterium
- Für jeden Kandidaten z = (R_pred − R_obs)/σ_tot, σ_tot² = σ_R² + σ_pred². **Verträglich** bei |z| ≤ 2, sonst **widerlegt**.
- **H100 bestätigt** („H99 braucht eine Korrektur, und B oder C reicht“): A widerlegt und B oder C verträglich.
- **H100 widerlegt**: B und C beide widerlegt.
- Sonst **nicht entschieden**. Bevorzugt ist der Kandidat mit kleinstem |z|; „trennend gegen A“ nur bei |z_A| − |z_best| ≥ 2.

## Erwartungswert (nicht Teil des Kriteriums)
- Nach dem Verlauf 2012–2025 ist der heutige Wert die beste Schätzung: R ≈ 0,03002. Mit weiteren JUNO-Daten dürfte σ_R
  von 0,00046 auf etwa 0,0003 fallen (dann begrenzt durch Δm²₃₁).
- Bleibt der Mittelwert, wären zu erwarten: z_A ≈ +2,7 (widerlegt), z_B ≈ +0,2, z_C ≈ +1,2; H100 also eher bestätigt,
  mit B bevorzugt, aber nicht trennend zwischen B und C.

## Offenlegung
- Nicht blind gegenüber NuFIT 6.1: B wurde aus einem Fit an diese Daten gefunden, C nach Kenntnis von c ≈ 1,8; beide
  liegen deshalb heute nahe am Messwert. Gezählt werden darf nur der Vergleich mit den künftigen Daten.
- Die Kandidaten sind keine Herleitungen: Skala (B) und Familienkorrektur (C) sind Lesarten; die native Form η
  (Ursprung der Verschiebung) ist offen. OP3/OP4 bleiben offen.

## Bei Bestätigung / Widerlegung
- **Bestätigt:** Die Brannen-Struktur mit Verschiebung um den Bogenrand wird durch eine Korrektur der Lepton-Seite
  getragen; die Frage Kopplungsseite (B) oder Familienkorrektur (C) bleibt offen, bis die Daten sie trennen.
- **Widerlegt:** Keine der beiden Korrekturen genügt; dann ist die Verschiebung π/12 selbst zu prüfen (Idee 1).
