# Abgleich der OP5/QAM-Arbeitsstände mit r85–r93

Stand: 14. Oktober 2026. Reine Querverweis-Notiz, keine neue Aussage und keine
Änderung an den Guard- oder Residualvektoren.

## Ausgangslage

Die Dateien in diesem Ordner (`OP5_QAM_Nulluebergang.md`,
`OP5_QAM_Zustand_Operator.md`, `OP5_QAM_Residual_Lift.tex`,
`OP5_Relay_C5_Check.py`) entstanden am 12.–14. Oktober 2026 im GitHub-Repository
`Moriarty1982/QuantumSphere-Unfold` (Commits `e457760`, `091d859`, `3a0ce01`).
Sie wurden aus `github/main` (`9fa4d26`) unverändert übernommen.

Ihre Quellbasis ist die veröffentlichte v4.7.0-Quelle mit
SHA256 `019e7a35…`. Das ist byte-identisch mit
`Quantum_Sphaera_Companion_v4_7_0_RC19_concept_doi_restore_source.tex` in diesem
Repository, also **Stand r84**. Alle Zeilenangaben in den Analysedateien beziehen
sich auf diesen RC19-Snapshot, nicht auf die Arbeitsdatei
`Quantum_Sphaera_Companion_v4_7_0_source.tex`.

Die Runden r85–r93 waren bei der Entstehung nicht bekannt. Diese Notiz ordnet
die Ergebnisse den späteren Runden zu.

## Guard-Prüfung

In den vier Dateien wurde nach den verbotenen Aussagen gesucht: `C5 = 0`,
`0_termdata ⇒ 0_all`, C6/T2-Schließung, `W_γ^glob`, `W_all` und das Ausgeben von
`β₄`. Es gibt keinen Treffer, der eine davon behauptet. Die Texte schließen sie
ausdrücklich aus, zum Beispiel mit „No C4 absorption, C6 unblocking, exact finite
zero … claim is implied“ am Ende von `OP5_QAM_Residual_Lift.tex`. Damit gelten
weiterhin `Γ_guard = (1,1,1,1,1)`, `R_glob = (0,1,1,1,1)` und `β₄ = 1/256`
ungespendet.

## Zuordnung im Einzelnen

| Analyse-Ergebnis | Fundstelle | Spätere Runde | Verhältnis |
|---|---|---|---|
| Die skalare C5-Folge erreicht bei n = 20 die Detektorschwelle, aber keine exakte Null. | `OP5_QAM_Nulluebergang.md`, Abschnitt „Ergebnis“ | **r86**, Theoremlet r86.1 (`n_min(θ) = ⌈log_{4/3}(1/θ)⌉`, `n_min(1/256) = 20`) und r86.2 (keine endliche Null bei rein multiplikativer Rekursion mit `q > 0`) | **Doppelt.** Gleiche Aussage, unabhängig hergeleitet. r86.2 ist die kanonische Fassung. |
| Eine endliche exakte Null braucht einen anderen Mechanismus als die positive 3/4-Kontraktion; Schwellenbildung und Umbenennung einer Nullklasse leisten das nicht. | `OP5_QAM_Nulluebergang.md`, Abschnitt 6, „dritte Möglichkeit“ | **r86** (Formentabelle (i)–(iii)) und **r88** (Theoremlet r88.1/r88.2, Korollar r88.3) | **Doppelt, aber r88 geht weiter.** r88 schließt auch den subtraktiven Kanal aus: Er trifft die Null nur bei maßnull-abgestimmtem `c_⋆(N)`, verlässt danach `D_5^bd` und braucht eine Stoppregel, die `LG_5^bd` verbietet. Offen bleibt nur Form (iii). |
| Lokale Existenz- und Grenzwertaussagen gelten für jedes `q ∈ (0,1)`, nicht nur für 3/4. | `OP5_QAM_Residual_Lift.tex`, Abschnitt 2355 ff. („Coefficient verdict“) | **r86.2**: „depends only on `q > 0`, not on the particular value `q = 3/4`“ | **Übereinstimmend.** |
| Der erste Schwellendurchgang bei n = 20 legt `q` nur auf das Intervall `((1/256)^{1/19}, (1/256)^{1/20}] ≈ (0.7469, 0.7579]` fest, nicht auf 3/4. | `OP5_QAM_Residual_Lift.tex`, Abschnitt 2355 | **r86.1** rechnet in Gegenrichtung: von `q = 3/4` auf `n_min = 20` | **Ergänzend, neu.** r86.1 nennt die Übereinstimmung bei 1/256 selbst nur eine „consistency check“. Die Analyse zeigt, dass die Prüfung `q` nicht festlegt. In den Runden ist das nicht festgehalten. |
| Für die 3/4 gibt es keine unabhängige Herleitung. Sie ist ein Fit-Tabellenwert aus r04 (RC19 um Zeile 52359), und `Δ_5 = −1/4` ist nur die Differenz der Scores. | `OP5_QAM_Residual_Lift.tex`, Abschnitte 2254–2323 | Keine Runde behandelt die Herkunft von 3/4 eigens. r86.1 übernimmt sie aus Theorem r09. | **Neu.** Kandidat für eine eigene Runde: „3/4 ist kalibriert, nicht hergeleitet“. Guard-neutral. |
| Grenzwert-/Abschlusslinie: Nonstandard-Halo, Standardteil, Witness-zu-Closure-Brücke, lokale C5-Normalform mit Rückkehroperator | `OP5_QAM_Residual_Lift.tex`, Abschnitte 157–399 und 2023–2253 | **r13** (Abschluss im Punkt ∞) und **r88** Form (iii) | **Abgrenzung nötig.** Diese Linie arbeitet am *Grenzzustand*, nicht an einer *endlichen* Entladung. Sie ist deshalb **nicht** die offene Form (iii) aus r88 (ein Zeuge außerhalb der Kollar-Iteration, der die Obstruktion selbst erreicht). Beide Fragen bleiben getrennt offen. |
| `β₄ = 1/256` kann ungespendet bleiben; aufgehoben wird nur die Projektionsschuld, nicht das C4-Residuum. | `OP5_QAM_Residual_Lift.tex`, um Zeile 3449 | **r91**: `β₄` ist grundsätzlich nicht ausgebbar, weil `0_M^ε ⇏ 0_all` | **Übereinstimmend.** r91 ist stärker: nicht nur „kann bleiben“, sondern muss bleiben. |
| Die „compressed `Δ_γ < 1/5` selector condition“ beschränkt `δ̇` nicht und legt das Benchmark-Intervall nicht fest. | `OP5_QAM_Residual_Lift.tex`, um Zeile 5268 | **r92**: `1/5 = min_{V∈R_A}(1 − G^req/G^avail)`, angenommen bei V3 (`G^req = 8/5`, `G^avail = 2`) | **Teilweise überholt.** Die Bezeichnung „compressed“ ist seit r92 falsch, denn die Schranke ist aus r14/r15 exakt rekonstruiert. Die Sachaussage bleibt richtig: r92 erklärt die *Herkunft* der Fenstergrenze, liefert aber keine Schranke für `δ̇` und kein Benchmark-Intervall. |
| QAM-Tensorrollen-Prüfer: Kontraktion nur bei entgegengesetzter Varianz; Vergleich gleicher Varianz nur mit deklariertem Vergleichstensor | `scripts/qsc_audit/TENSOR_GRAMMAR.md`, `tensor_grammar_check.py` (nur auf GitHub) | **r93**: dieselbe zweiseitige Grammatik als Routing-/Forwarding-Disziplin über einem gerichteten Chart-Graphen | **Ergänzend.** Der Prüfer setzt die Regeln um, die r93 als Weiterleitungsdisziplin liest. Er arbeitet gegen die modularen Quellteile (`sources/parts/…`), nicht gegen den Monolithen. |

## Was daraus folgt

1. **Doppelt:** Die Finite-Null-Ausschlüsse der Analyse sind durch r86.2 und r88 abgedeckt. Kanonisch sind die Runden.
2. **Neu und übernehmbar:** die Herkunftsprüfung der 3/4 und die Intervallaussage zu `q`. Beide sind guard-neutral und könnten als eigene Runde (r94) in den Monolithen aufgenommen werden.
3. **Zu korrigieren:** In `OP5_QAM_Residual_Lift.tex` die Bezeichnung „compressed“ für `Δ_γ < 1/5` mit einem Verweis auf r92 versehen. Das sollte auf GitHub geschehen, wo die Datei gepflegt wird.
4. **Offen wie zuvor:** Form (iii) aus r88. Die Grenzwertlinie der Analyse beantwortet sie nicht.
