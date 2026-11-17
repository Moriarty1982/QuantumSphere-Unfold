# OP4: Bestandsaufnahme der Mischungs-Linie gegen den Datenstand vom 17.11.2026 (Erkundung, keine Rechnung)

17. November 2026. Auftrag des Autors: „OP4 aufgreifen“. Erster Schritt nach den Abschlusskriterien von Issue #11: Definition und Eingaben festhalten,
Hergeleitetes von Angepasstem trennen, offene Prüfungen und Abweichungen benennen. Keine neue Rechnung, keine H-Nummer.

## Datenstand (geprüft am 17.11.2026)
- **NuFIT:** neueste Version v6.1, Datenstand November 2025 (nu-fit.org, Seite „Results“); keine Version nach dem 24.10.2026. H42, H46 und H100
  haben damit noch keine Prüfdaten.
- **JUNO:** neueste Messung arXiv:2609.37895 (29.09.2026), sin²θ₁₂ = 0,3036 ± 0,0064 (`v4_8_0_r03_r12/llm/Nachpruefung_JUNO_2026.md`); die erste
  Messung (arXiv:2511.15978, Nov. 2025) gab 0,3092 ± 0,0087. Keine neuere Messung gefunden. H9 verlangt σ ≤ 0,004 und ist noch nicht prüfbar.

## Definition und Rahmen
- Quelle des Problems: OP4-Abschnitt der Vollquelle v4.8.0 (Issue #11, Fundstelle Zeile 19123). Die veröffentlichte Scope-Sperre beansprucht **keine**
  CKM/PMNS-Herleitung.
- Eingaben der aktuellen Linie: Lesart je Teilchenart als Untergruppe der A₄ (r55, H39: Dirac ℤ₃, Majorana ℤ₂ ⇒ TM2), Maske aus r47 als Korrektur (r57,
  H41), Zeitzyklus als Dirac-Zyklus (r18, `op4_time_cycle_mixing_2026_11_15/`).

## Hergeleitet, angepasst, offen

| Aussage | Art | Stand gegen Daten | Quelle |
|---|---|---|---|
| Normale Ordnung, Σm_ν ≈ 0,059 eV (Neutrino-Triole) | Vorhersage, vorab | verträglich; normale Ordnung von JUNO gestützt (≥ 2,1σ) | H2 |
| TM1 vor TM2 | Vergleich, vorab | TM1 χ² 9,6 gegen TM2 49,1 (mit JUNO 2026); TM1 allein **disfavorisiert** (θ₁₂ 2,4σ) | H4, Nachprüfung JUNO |
| CP aus Cayley–Dickson-Involution | Vorhersage, vorab | **disfavorisiert** (χ² 14,0 bei 3 FG) | H8 |
| sin²θ₁₂ = β_sym²/cos²θ₁₃ = 0,3086 (\|U_e2\|² = β_sym²) | nachträglich gefunden, danach vorab festgelegt | 0,7σ neben dem kombinierten Wert; **offen** bis JUNO mit σ ≤ 0,004 | H5 (Nachbefund), H9 |
| sin²θ₁₂ aus der Drei-Frame-Zuordnung = 0,2991 ± 0,0057 | Vorhersage, vorab | verträglich; von H9 durch JUNO nicht trennbar (Grenze durch Planck) | H12 |
| TM2 aus der Lesart je Teilchenart | Lesart, Rechnung | θ₁₂ ohne Korrektur 3,6σ über JUNO | H39, Zeitzyklus-Notiz |
| Maske als Korrektur senkt θ₁₂ auf JUNO | Anpassung (ε frei) | bestätigt als möglich; ε aus keinem Strukturwert (H44) | H41, H44 |
| ε = artanh β_sym (Rapidität des Frames M) legt θ₂₃ fest: [0,4913; 0,4975] | Lesart, nicht blind | **offen**: H42 (≤ 0,54), H46 ([0,49; 0,50]) warten auf die nächste globale Auswertung | H45, H42, H46 |
| δ_CP | – | durch die Lesart nicht festgelegt | H43 |
| Neutrino-Phase = Lepton-Phase + π/12 | Vorhersage, vorab | H99a verträglich (nicht blind); H99b an der 2σ-Grenze, nicht entschieden | H99 |
| Verhältnis R = Δm²₂₁/Δm²₃₁ (drei Kandidaten) | Vorhersage, vorab | **offen** bis NuFIT nach 6.1 (Frist 31.12.2027) | H100 |
| CKM aus der Maske | Anpassung | H34 widerlegt; Form S mit vier ε nur im Ausläufer (H38), keine Struktur über Zufall (H40) | H34, H38, H40 |

## Verbleibende Abweichungen und Zusatzannahmen
1. **θ₁₂:** TM1 2,4σ, TM2 ohne Korrektur 3,6σ neben JUNO; nur mit freier Korrektur (ε) oder mit H9/H12 verträglich.
2. **ε:** frei bis auf die Lesart ε = η (H45, nicht blind); kein Strukturwert aus einer festen Liste trifft (H44).
3. **δ_CP:** frei.
4. **Quarks:** keine Herleitung; die Maskenformen passen die CKM-Daten nur als Anpassung.

## Verbindung zu OP1 (neu, Lesart)
Zwei der drei schärfsten offenen OP4-Vorhersagen hängen an der Zahl von OP1:
- H9: \|U_e2\|² = β_sym² = 0,30185.
- H45/H46: ε = artanh β_sym = η; nach v4.10.0-r29.5 ist η die Rapidität des Beobachters M gegen den Ruheframe des Feldes.
Die künftigen JUNO- und NuFIT-Daten prüfen damit indirekt auch die OP1-Zahl γ_L = cosh 2η. Fällt H9 oder H46, fällt nicht γ_L selbst, aber seine
Verwendung in der Mischung. Keine neue Vorhersage; die bestehenden Kriterien bleiben unverändert.

## Stand der Abschlusskriterien von Issue #11
- [x] Definition, Eingaben und Zielgrößen mit Fundstellen (diese Notiz; Quellstelle der Vollquelle wie im Issue).
- [x] Freie Kalibrierung von Hergeleitetem getrennt (Tabelle).
- [x] Verbleibende Abweichung und Zusatzannahmen benannt.
- [ ] Eine geprüfte Herleitung oder ein ausdrücklich eingeschränkter Ersatzsatz: **nicht vorhanden.** OP4 offen.
