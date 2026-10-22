# Ergebnis H14: Tachyon-Kegelwinkel und Weinberg-Winkel

Gerechnet am 2026-10-21 nach dem Commit der Vorab-Notiz (`llm/Vorab_Notiz_H14_Kegelwinkel_Weinberg.md`, Commit
`5911161`). Skript `llm/k43_test_h14.py`. Verfahren und Kriterien unverändert.

## Daten

PDG, S. Navas et al., Phys. Rev. D 110, 030001 (2024) und Update 2025, abgerufen am 2026-10-21 von pdg.lbl.gov:

| Größe | Wert | Quelle |
|---|---|---|
| m_W | 80,3692 ± 0,0133 GeV | Summary Tables „Gauge and Higgs Bosons“ (erstellt 2025-05-30) |
| m_Z | 91,1880 ± 0,0020 GeV | dieselbe Tabelle |
| sin²θ_eff | 0,23148 ± 0,00013 | dieselbe Tabelle |
| ŝ²_Z (MS-bar) | 0,23122 ± 0,00006 | Review „Electroweak Model and Constraints on New Physics“ |
| s²_W on-shell, SM-Fit | 0,22342 ± 0,00009 | derselbe Review; nur berichtet, das Verfahren rechnet aus den Massen |

## Ergebnis

| | Wert |
|---|---|
| β_sym = tanh(½ arcosh γ_L) | 0,54935 (Dokumentwert 1/1,820: 0,54945) |
| Vorhersage sin²θ_W = (1 − β_sym)/2 | **0,22533** (mit Dokumentwert 0,22527) |
| On-shell aus den Massen, 1 − m_W²/m_Z² | **0,22321 ± 0,00026** |
| Δ = Vorhersage − Messung | +0,00212 |
| z | **+8,2** |
| Band B (On-shell bis MS-bar, je ±3σ) | [0,22243; 0,23140], Vorhersage liegt darin |
| Look-elsewhere | Trefferwahrscheinlichkeit 0,018 je Beziehung, 0,087 für fünf Kandidaten |

Winkel: ϑ_c = 56,678°, dagegen 2θ_W = 56,387° (on-shell), 57,482° (MS-bar), 57,518° (effektiv). Der Kegel liegt
zwischen den Definitionen, 0,29° über dem On-shell-Wert und 0,80° unter dem MS-bar-Wert.

## Entscheidung (nach Kriterium der Notiz)

- **(A) Exakte Beziehung, on-shell: widerlegt** (|z| = 8,2 ≥ 3).
- **(B) Baumgraphen-Beziehung: nicht entscheidbar.** Die Vorhersage liegt innerhalb der Spanne, die die
  Renormierungsschemata selbst aufmachen.
- **Kein Beleg.** Die Hypothese ist nachträglich formuliert. Eine beliebige einfache Beziehung träfe das Band mit etwa
  2 % Wahrscheinlichkeit, bei fünf gleich einfachen Kandidaten mit etwa 9 %. Der Ausgang entspricht der in der Notiz
  offengelegten Erwartung.

## Folgen

- ϑ_c = 2θ_W ist als exakte Beziehung ausgeschlossen. Als Näherung bleibt sie offen, ist aber nicht prüfbar, solange keine
  Vorschrift festlegt, auf welcher Skala oder in welchem Schema β_sym mit θ_W zu vergleichen wäre.
- Ein echter Test bräuchte eine Größe, die vor der Festlegung unbekannt ist. Ein Beispiel wäre eine Vorschrift für das
  Schema, aus der ein Wert für den laufenden Mischungswinkel bei einer noch nicht gemessenen Energie folgt. Ohne eine solche
  Vorschrift wird diese Route nicht weiter verfolgt.
- Der Kegelwinkel selbst bleibt ungemessen. Guards unverändert.
