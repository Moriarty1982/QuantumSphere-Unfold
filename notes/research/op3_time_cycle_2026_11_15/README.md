# OP3: Ein Drittel der Periode als Dreierzyklus, rückwärts gerechnet

15. November 2026, Claude Opus. **Erkundung, nicht blind** (Koide 2/3, die Lepton-Phase und die Massen waren bekannt;
Rückwärtssuche). Auftrag des Autors: „Ja, rückwärts rechnen“, nach `../op3_third_invariant_2026_11_15/README.md`. Keine
H-Nummer, kein CT-Eintrag, Guards unverändert. Skript `time_cycle_backsolve.py` (Kandidatenliste, Toleranz und abgeleitete
Größen im Kopf des Skripts vor dem ersten Lauf festgelegt), Ausgabe `run/time_cycle_backsolve_stdout.txt`.

## Ansatz
Die invariante Matrix S = [[s₊, w], [w, s̄₋]] trägt unter Zeitverschiebung die Gewichte −1, 0, +1. Die Verschiebung um ein
Drittel der Periode π/ω von s(t) ist U = diag(ω̄, 1, ω) mit ω = e^{2πi/3}, U³ = 1: ein Dreierzyklus, der allein aus der
Zeitentwicklung des Feldes kommt. Ein Zustand mit Gewichten (p₋, p₀, p₊) auf (s₊, w, s̄₋) hat eine Bahn aus drei Zuständen
(dasselbe Feld zu drei gleich verteilten Zeitpunkten) mit gleicher Überlappung ⟨ψ|Uψ⟩ = p₀ + p₋ω̄ + p₊ω und
Bargmann-Phase 3·arg⟨ψ|Uψ⟩. Die Gram-Matrix ist zirkulant (Brannen-Form).

## Ergebnisse
1. **Die Gewichte sind durch Koide und die Phase bestimmt.** |⟨ψ|Uψ⟩|² = ½ und Phase φ = 2/3 (δ = 2/9) geben
   **p₀ = (1 + √2 cos δ)/3 = 0,7931**, **p₊ − p₋ = √(2/3) sin δ**, also p₋ = 0,0135, p₊ = 0,1934.
   Kontrolle: Die Gram-Matrix der Bahn gibt K = 2/3 und die Massenverhältnisse 1 : 206,77 : 3477,5, die
   Lepton-Verhältnisse. Aus den Massen (PDG 2024) folgt δ = 0,222230 (2/9 = 0,222222).
2. **Lesart der Gewichte.** Fast 80 % der invarianten Leistung liegen im Mittelwertanteil w, der Rest in den beiden
   schwingenden Anteilen, und diese sind stark ungleich: Helizitäts-Asymmetrie A = (p₊ − p₋)/(p₊ + p₋) = 0,870,
   Amplitudenverhältnis |s₋|/|s₊| = 0,264. Die Phase entsteht aus dieser Asymmetrie (r16.2).
3. **Weit vom kohärenten Sektor.** Rang 1 verlangt |w|² = |s₊||s₋|. Nötig ist c = |w|²/(|s₊||s₋|) = 7,78
   (Hilbert–Schmidt) bzw. 3,89 (Parseval). Die Auslesezustände wären also ausgeprägt Rang 2, nicht nahe beim flachen
   Oktanten aus r16.7.
4. **Kein nativer Wert.** Die fünf abgeleiteten Größen (p₀, A, r, c_HS, c_Parseval) wurden mit 24 vorab gelisteten
   Kandidaten verglichen (γ_M, γ_T, γ_L, β_sym, η_sym und Abgeleitete, einfache Brüche und Wurzeln, 2/9, π/4 − 2/3,
   γ_M/2), Toleranz 0,5 %: **kein Treffer**. Zufallserwartung 0,44.

## Folgerungen
- **Der Zeitzyklus ist eine echte native Dreierstruktur,** und er erzeugt die Brannen-Form von selbst. Das ist neu: Die
  zirkulante Gram-Matrix ist hier keine Annahme, sondern folgt aus der Zeitverschiebung um ein Drittel der Periode.
- **Er erklärt Koide nicht.** Die Werte p₀ und p₊ − p₋ sind nur Brannens Parameter (Amplitude √2 und δ), auf die drei
  Frequenzanteile von s(t) umgeschrieben. Eine Begründung, warum die Leistung so verteilt sein sollte, liefert der Bestand
  nicht, und die abgeleiteten Größen treffen keinen nativen Wert.
- **Spannung zu r16.7 bestätigt:** Das Oktant dort liegt im kohärenten Sektor (Rang 1, Wurzelgrößen); die Bahn hier
  verlangt Rang 2 mit c ≈ 4–8 und lineare Größen. Die beiden Bilder beschreiben nicht dieselben Zustände.
- **Kein Test.** Ohne Prinzip für die Verteilung (p₋, p₀, p₊) gibt es nichts Blindes zu prüfen. H105 bleibt frei.

OP1–OP5, C5, C6/T2 und die Guards sind unverändert.

## Nachtrag 15.11.2026: Die drei Frequenzanteile als Generationen
Auftrag des Autors: „Festhalten, in r16, PR“, nach Weiterdenken. **Erkundung, nicht blind; Umparametrisierung mit
Deutung, keine Vorhersage.** Skript `harmonics_reading.py`, Ausgabe `run/harmonics_reading_stdout.txt`.

1. **Die Gewichte sind die normierten Massenwurzeln.** Die Gram-Matrix der Bahn ist zirkulant mit Eigenwerten 3p_k, also
   p_k = √m_k/Σ√m (Leptonen: e 0,013450, μ 0,193409, τ 0,793141 gegen die rückwärts bestimmten Gewichte 0,013450, 0,193404,
   0,793146). Zuordnung: τ ↔ Mittelwert w, μ ↔ schwingender Anteil der Mehrheitshelizität (s̄₋), e ↔ schwingender Anteil der
   Minderheitshelizität (s₊). Die Masseneigenzustände sind die Eigenzustände der Zeitverschiebung; die drei
   Auslesezustände sind ihre Bahn unter der Verschiebung um ein Drittel der Periode.
2. **Warum drei (Lesart).** s(t) ist quadratisch im Feld; eine quadratische Größe einer Schwingung der Frequenz ω hat genau
   die drei Anteile −2ω, 0, +2ω. Offen ist, warum die Generationen an s hängen und nicht an einer höheren Invariante.
3. **Koide als Autokorrelation.** Mit Σp = 1 gilt exakt |⟨ψ|Uψ⟩|² = (3Σp² − 1)/2 (geprüft auf 1000 Zufallsgewichten).
   Koide heißt Σp² = 2/3 (= K) oder: Die Autokorrelation der Feldinvariante nach einem Drittel ihrer Periode hat den
   Betrag 1/√2. Ein reelles Feld gibt Σp² = 1/2 (Parseval) bzw. 3/8 (Hilbert–Schmidt), nicht 2/3. Ein Prinzip für 2/3 fehlt.
4. **Leichtes Elektron und Biegung.** Exakt p₋ = (1 − √2 sin(δ + π/6))/3 mit δ = φ/3. Im flachen Grenzfall φ = π/4 ist
   p₋ = 0 (Elektron masselos, s₊ = 0, der Minderheitsanteil F₊ null-artig). Für kleine Biegung p₋ ≈ (π/4 − φ)/9 (bei
   φ = 2/3: 0,01345 gegen 0,01319). Die Biegung, gelesen als γ_M/2, ist hier das Gewicht der schwingenden
   Minderheitshelizität.

**Grenzen:** Die Gewichte sind die Massen; vorhergesagt wird nichts. Die Spannung zu r16.7 (kohärenter Sektor dort, Rang 2
hier) bleibt. Mögliche nächste Frage, nicht gerechnet: ob eine Uhr-Struktur des Papers (Photonuhr, Uhrfenster) eine
Bedingung an die Autokorrelation nach einem Drittel der Periode liefert.

## Nachtrag 15.11.2026: Legt die Photon-Uhr die Autokorrelation fest? Nein
Auftrag des Autors: „weiter“ (die oben genannte nächste Frage). **Erkundung, nicht blind.** Skript `clock_coherence.py`,
Ausgabe `run/clock_coherence_stdout.txt`.

**Vorwissen:** Die Photon-Uhr-Sonde (v4.7.0-r90, Quelle v470-r15) ist C(τ) = 1 + η·|Σ w_m e^{iφ_m}|²/(Σ|w_m|)². Ein Fenster V
erhält den Selektor, solange das Kohärenzfunktional mindestens ρ_V ist (r90: ρ_V3 = 3/5, ρ_V5 = 2/5, ρ_V8 = 7/9; erste
Ordnung 1 − Var(φ) ≥ ρ_V). r12.2(a) (v4.9.0): Eine Dualitätsdrift α je Auslesung ist tolerierbar für sin²α < 1/5,
α < 26,57°. Die Quelle lehnt die Gleichsetzung von Uhrfrequenzen mit physikalischen Frequenzen ausdrücklich ab
(v4.9.0-r12, „What is fixed and what is not“); eine globale Photon-Uhr-Aussage ist durch die Guards verboten.

**Ergebnisse**
1. **Dasselbe Funktional.** Die Koide-Bedingung aus r16.9(b) ist genau das Kohärenzfunktional der Uhr-Sonde, mit den
   Gewichten √m_k/Σ√m und den Phasen −2π/3, 0, +2π/3 nach einem Drittel der Periode: Wert 0,499991 (Koide ½).
2. **Keine Schwelle bei ½.** ρ_V3 = 3/5, ρ_V5 = 2/5, ρ_V8 = 7/9. Der Selektor bliebe nur auf V5 erhalten. Dass ½ in der Mitte
   der Schwellen der Primärkette {V3, V5} liegt, ist nachträglich gesehen und wird nicht verwertet.
3. **Drift weit außerhalb.** Die Auslesungen des Zeitzyklus liegen auf den schwingenden Anteilen 120° auseinander; die Uhr
   toleriert 26,57° je Auslesung. Die erste Ordnung von r90 ist bei dieser Streuung unbrauchbar (1 − Var = 0,23).

**Folgerung:** Die Uhr-Strukturen haben dieselbe mathematische Form wie die Koide-Bedingung, legen den Wert ½ aber nicht
fest. Eine Gleichsetzung der Uhr mit der Feldfrequenz ω würde zudem genau die Identifikation verlangen, die die Quelle
ablehnt, und an die verbotene globale Photon-Uhr-Aussage rühren. Ein Prinzip für Σp² = 2/3 ist damit weiter nicht gefunden.

## Nachtrag 15.11.2026: Treue ½ als maximale Unsicherheit über „dasselbe Objekt?“ (Kandidat für ein Prinzip)
Auftrag des Autors: „Festhalten, dann OP1“. **Lesart, nicht gerechnet, nicht blind.**

**Vorwissen:** `../op3_koide_potential_2026_11_13.md` (Faden 2, Punkt 4) führt seit dem 13.11. vier gleichwertige Lesarten von
K = 2/3 als Kandidaten für ein Prinzip: Reinheit der normierten Gram-Matrix 2/3, Mitte des Bereichs [1/3, 1],
Gleichverteilung Diagonale/Nebendiagonale, paarweise Treue ½. Im Zeitzyklus ist G/3 eine Dichtematrix mit den Eigenwerten
√m_k/Σ√m; Koide heißt Reinheit 2/3 der Mischung der drei Auslesungen.

**Kandidat:** Zwischen zwei Auslesungen eines Objekts ist die Frage „bestätigt die eine die andere?“ ein Bit mit
Wahrscheinlichkeit |⟨k|l⟩|². Orthogonal (0) hieße verschiedene Objekte (ausgeschlossen nach r16.7), gleich (1) hieße keine
verschiedenen Auslesungen. Die Entropie des Bits ist maximal bei **Treue ½**. Prinzip: *Verschiedene Auslesungen eines
Objekts lassen maximal offen, ob sie dasselbe zeigen.* Es gibt im Qubit-Bild das Oktant (r16.7) und im ℂ³-Bild des
Zeitzyklus mit drei Auslesungen K = 2/3 (r16.9), aus derselben Quelle.

**Bewertung:** Neu ist nur die Begründung über maximale Entropie; das Maximieren ist eine Setzung. Kein neuer Test: Für
Neutrinos gibt das Prinzip wieder K = 2/3 (H2, H99, H100); für Quarks gilt Koide nicht, das Prinzip müsste sie als „keine
freien Auslesungen“ ausnehmen (Setzung). Offen bleiben Phase bzw. Biegung (γ_M, OP1) und die Zahl drei.
