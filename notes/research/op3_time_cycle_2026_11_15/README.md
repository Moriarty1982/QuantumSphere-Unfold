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
