# v4.10.0-r62 und r63: Sedenion-Kopien, Rest-Generation und der Koide-Punkt als Fixpunkt des Frame-Tauschs (H138–H156) (Stand 26.11.)

26. November 2026. Zwei Sammelrunden auf Entscheidung des Autors („ja“ zum Einbau von H138–H156 in den Companion). Die Runden rechnen nichts neu,
sie bündeln die Befunde mit dem Status aus den Ergebnis-Notizen. Alle Tests haben eine Vorab-Notiz; welche Teile nicht blind oder nachträglich
sind, steht je Eintrag in der Runde. Frühere Runden bleiben unverändert. H128–H137 (andere Linien) und H157 (läuft noch) sind nicht enthalten.
Physik-Paper und deutscher Preprint sind noch nicht nachgezogen.

Quellen aller Einträge: `../hilbert_shift_felder_2026_11_24/generationszahl_h138/` (Vorab- und Ergebnis-Notizen, Skripte k321–k339 mit
Wolfram-Gegenproben und tatsächlichen Ausgaben).

## r62: Kopien und Rest-Generation

| Eintrag | Inhalt | Test, Skript |
|---|---|---|
| r62.1 | Genau drei G₂-stabile Oktonion-Kopien in 𝕊 (Im z³ = 0); HS(5): 15, davon 9 oktonionisch; HS(6): ≥ 207 / ≥ 79; unabhängige Kopien nie oktonionisch | H138 (a, b widerlegt), k321 |
| r62.2 | Nullteiler von 𝕊 = gleiches Gewicht in allen Kopienrichtungen; Überschuss-Algebren auf HS(5), HS(6) sind Nullteiler-Familien | H139 (a nach Wortlaut widerlegt), k322 |
| r62.3 | Gleiche Farbe, je Kopie eine Generation, keine gemeinsame Ladung (Leck ≥ 3\|x\|²), 15 statt 24 Zustände | H140, k323 |
| r62.4 | Kern 9 = 1 ⊕ 1 ⊕ 1 ⊕ 3 ⊕ 3̄; Quark-Satz ladungsstabil, Singuletts mit ½ lecken | H141, k324 |
| r62.5 | Vier Kopien auf HS(5): in 9 von 126 Auswahlen vollständige Rest-Generation; Regel n_gen = dim R⁰; fünf Kopien: höchstens eine | H142 (b widerlegt), H143, k325, k326 |
| r62.6 | Rest trägt keinen eigenen Sektor; z ↦ z̄ gibt q ↦ 1 − q = globales Orientierungsvorzeichen | H144 (c widerlegt), k327 |
| r62.7 | K = (D⁰ ⊗ e₀) ⊕ (R ⊗ Im𝕆); Rest-Generation = R⁰ ⊗ ℂ𝕆 über reeller Linie; keine Algebra | H145 (c nach Wortlaut widerlegt), k328 |
| r62.8 | Gram-Auslesung: keine Massen aus den Kopien (max K = 19/32); Rest-Linie c ist exakter Nullvektor | H146, k329 |
| r62.9 | HS(0)-Linie ist Skalar, kein Spin-2-Graviton; freier Mischwinkel θ zwischen e₀ und e₇ (Erkundung) | H147, k330 |

## r63: Koide-Punkt

| Eintrag | Inhalt | Test, Skript |
|---|---|---|
| r63.1 | K = 1/(3cos²θ); K = ⅔ ⇔ θ = π/4; δ = 2/9 eingesetzt (Fit) | H148, k331 |
| r63.2 | θ = π/4 Fixpunkt des Tauschs J (Materie- ↔ Tachyon-Frame); Krümmung ±2(2a − b); δ nur über cos 3δ, ohne Anpassung nur 0, π/3, π/12 | H149, k332 |
| r63.3 | Vorzeichen von 2λ − κ: nur mit „skalenfrei und Kondensation“ (κ < 0); dann K ≈ 0,672 | H150 (b teils, c nach Wortlaut widerlegt), k333 |
| r63.4 | Verschiebung startabhängig, ohne Bezug zu 2/9 oder Setzungen; voller Ansatz: δ ∈ {0, π/3}; Normierung = Umparametrisierung; ⅔ exakt nur mit Schleife über {1, U} | H151–H153, k334–k336 |
| r63.5 | {1, U} nicht erzwungen; K = 0,6666645 ± 0,0000051 (0,43σ, Messrauschen); bedingte Vorhersage m_τ = 1776,969 MeV | H154, k337 |
| r63.6 | Skala gesetzt: Tauschsymmetrie gibt K = ⅔ am Baumgraph, Laufen erst in zweiter Ordnung; δ = 2/9 braucht R* = −0,0075807 (Fit) | H155 (c, d widerlegt), k338 |
| r63.7 | μ_A² = μ_B² nicht aus der Algebra; genau aus J bzw. D₄; J ist Isometrie, kein Automorphismus: Postulat der Frame-Gleichberechtigung | H156 (c teilweise), k339 |

## Bilanz der Setzungen

- **Hergeleitet:** K = ⅔ ⇔ θ = π/4; θ = π/4 ist Fixpunkt von J und stationär für jedes tauschsymmetrische Potential.
- **Postulat:** Gleichberechtigung von Materie- und Tachyon-Frame (J als Symmetrie); vom Autor am 26.11.2026 vorerst angenommen, nicht hergeleitet.
- **Gesetzt:** Skala, Amplituden-Auslesung (r59.9), Generationszahl, Definition der Kopie, Orientierungstransport.
- **Angepasst:** δ = 2/9 (ein Parameter R*; CT-002 bleibt Platzhalter).
- **Nicht gesetzt:** Vorzeichen von 2λ − κ, μ², ζ und die globale Orientierung; beide Fälle sind gerechnet, die Entscheidung bleibt der Feldgleichung.

Runden als Dateien: `rounds/v4100_r62_round.tex`, `rounds/v4100_r63_round.tex`, wörtlich an
`sources/research/parts/v4100-post-release-layers.tex` angehängt.
Prüfung: `python3 scripts/qsc_audit/guard_linter.py … --start 7999` → 0 Treffer; `python3 tools/qs.py guards …` → 0 Kandidaten; Klammern und
Umgebungen ausgeglichen. Lokal kein pdflatex; der Kandidaten-Build läuft in der CI.

OP1–OP5, C5 und C6/T2 offen; T1 bleibt Vermutung; kein Guard berührt.
