# Volltextprüfung der OpenAI-Familien 148 und 149 an OP1 und C5 (Erkundung, nicht blind, 23.11.2026)

**Ergebnis in einem Satz:** 148 macht die Moran-Lesart von OP1 in natürlichen Einheiten zu einem bewiesenen Dimensionssatz und zeigt, dass
das Gewicht 2 der M-Zählung genau dann zählt, wenn die Auslese |j, +j⟩ und |j, −j⟩ als verschiedene Abbildungen trennt (sonst γ₁ = 0,1616);
149 zeigt, dass ein Austausch zwischen den Frames mit irgendeinem Rückweg C5_M nie gegen null gehen lässt, und zusammen mit einer klassischen
Tatsache bleiben für einen C5-Zeugen der Form (iii) nur eine nicht-Lipschitz-Dynamik am Nullpunkt oder ein Nulldurchgang.

Auftrag des Autors (Chat 23.11.2026): „148 und 149 prüfen“ (nach der Sichtung in `../openai_math_screening_2026_11_23/`). Keine H-Nummer:
Erkundung ohne Entscheidungskriterium. **Nicht blind:** Die Zählwerte γ_M, γ_T, γ_P und der Wert für Gewicht 1 (D = 1,2685) waren bekannt.

## Quelle
- openai/math @ `4eaee87548250b2682affda7d05d947c05554bae`. 148: „The entropy-rate dimension formula for self-similar measures on the line“
  (24.9.2026), TeX-Abschnitte gelesen (Einleitung, Hauptsatz). 149: „Boundedness and persistence of weakly reversible mass-action systems“
  (25.9.2026) und „Uniform Permanence …“ (5.10.2026), Einleitung und Hauptsatz gelesen.
- Lean (`lean/docs/148.md`, `149.md`): 148 formalisiert den Hauptsatz für jedes endliche reelle selbstähnliche Wahrscheinlichkeitsmaß
  und die Attraktorformel dim_H K = min{1, s} mit Σ|r_i|^s = 1 ohne exakte Überlappungen; 149 formalisiert globale Existenz,
  Beschränktheit und Persistenz (ein ε ∈ (0, 1) mit ε ≤ x_i(t) ≤ 1/ε für alle t ≥ 0). Die Formalisierungen sind nicht von uns geprüft.
- Werkzeugwahl: Wolfram Language (exakte Lösungen, Nullstellen, Entropien mit hoher Genauigkeit). Qiskit ist hier nicht geeignet, es gibt
  keine Quantenschaltung. Skripte und Ausgaben: `op1_148_moran_overlap.wl` / `_stdout.txt`, `c5_149_exchange.wl` / `_stdout.txt`.

## Vorwissen geprüft
`../op1_moran_geometry_2026_11_17/` (Moran-Umschreibung in T-Einheiten, D = γ/γ_T, Fall Gewicht 1 mit D = 1,2685), `../op1_common_premise_2026_11_18/`
(U2), r31.1/H118 (Orientierung des Oktantschritts = Zeitorientierung der Auslese), v4.8.0-r86/r94 (keine endliche Null der Kragenrekursion für
q > 0), r20/r21 (C5_M^(n) = (3/4)^n, Übergangs-, Photonpunkt- und Brückenfrage; r21.12 Score ½ am Nullaugenblick), `../op_cross_map_2026_11_23/` (Q1).

## Teil 1: 148 und die Zählregeln (OP1)
**Satz (laut Volltext):** Für jede endliche Familie φ_i(x) = r_i x + t_i auf ℝ mit 0 < |r_i| < 1 und jeden strikt positiven Wahrscheinlichkeitsvektor
p gilt dim_H μ = min{1, h_RW/χ}; h_RW ist die Entropierate der zufälligen Verkettungen, gezählt nach verschiedenen **Abbildungen** (nicht nach
Adressen), χ = −Σ p_i log|r_i|. Exakte Überlappung heißt Gleichheit der ganzen affinen Abbildung (Steigung mit Vorzeichen und Translation).

**Anwendbarkeit.** In T-Einheiten (Moran-Notiz) ist D_M = 1,8647 > 1; auf der Geraden sättigt die Formel bei 1, 148 sagt dort nichts. In
natürlichen Einheiten r_j = e^{−2π a(j)}, a(j) = √(j(j+1)), lautet jede Zählgleichung Σ_j g(j) r_j^γ = 1; die Dimension ist γ selbst (< 1), und
148 gilt nach Abschneiden der Spinsumme (bei j ≤ 200 Rest ≈ 10⁻¹³⁰). Die Lesart „passt auf eine Fläche“ der Moran-Notiz hängt damit an der
Einheit; das war dort schon als Annahme vermerkt.

**Befunde (Lauf 1 und 2):**
1. Kontrolle: γ_M = 0,237533 (Gewicht 2), γ_T = 0,127384 (nur j = ½), γ_P = 0,274067 (Gewicht 2j + 1).
2. **Identität:** Mit den Gibbs-Gewichten p = r^γ ist H(p)/χ = γ exakt (numerisch 15 Stellen): Die Zählbedingung ist die Dimensionsformel,
   Entropie je Punktierung durch Lyapunov-Exponent. Algebraisch elementar; neu ist nur, dass 148 für diese Form Überlappungen behandelt.
3. **Überlappung:** Fallen |j, +j⟩ und |j, −j⟩ als Abbildungen zusammen, zählt jede Skala einfach: γ₁ = 0,161586 (= 1,2685 γ_T, der Fall
   Gewicht 1 der Moran-Notiz). Für T bleibt eine einzige Abbildung, Dimension 0. **Das Gewicht 2 von M setzt also voraus, dass die Auslese die
   beiden Extremzustände als verschiedene Abbildungen trennt.** Dieselbe Zahl γ₁ entsteht, wenn die Auslese nur einen der beiden Zustände
   zulässt (Auswahl statt Identifikation).
4. **Spiegelung:** Ist die Partnerkopie gespiegelt (negative Steigung) mit eigenem Zentrum, bleibt die volle Rate (abgeschnittenes System
   j ≤ 1: 0,2018 für n = 1 … 4). Spiegelung um dasselbe Zentrum erzeugt Überlappungen in längeren Verkettungen; die Rate fällt
   (0,2018; 0,1725; 0,1628; 0,1579 für n = 1 … 4), Grenzwert nicht bestimmt.
5. **Reihenfolge:** Zwei Kontraktionen vertauschen genau dann, wenn sie denselben Fixpunkt haben. Sollen alle Verkettungen gleicher Multimenge
   gleich sein (Punktierungen ohne Reihenfolge), teilen alle Abbildungen einen Fixpunkt, und der Attraktor ist ein Punkt. Eine Zählung
   ununterscheidbarer Punktierungen lässt sich in dieser Sprache nicht ohne Kollaps darstellen.

**Lesart (Bezug Q1, H118):** m ↦ −m ist die Orientierungsumkehr. Das Gewicht 2 verlangt eine Auslese, die die beiden Orientierungen
**unterscheidet**, aber keine auswählt; wählt sie eine aus oder identifiziert sie beide, folgt γ₁. Das passt zu H118 (der Companion legt die
Orientierung nicht fest) und formuliert U2 als Frage nach der Unterscheidbarkeit der Orientierung durch die Auslese. Lesart, kein Beweis.

**Grenzen:** nur auf der Geraden; endliche Abschneidung; Maß- gegen Mengendimension (die Attraktorformel ist in Lean nur ohne exakte
Überlappungen formalisiert); 148 begründet weder U2 noch die T-Regel; γ₁ = 0,1616 ist kein Zielwert, es wurde kein Treffer gesucht.

## Teil 2: 149 und C5
**Satz (laut Volltext):** Endliches Reaktionsnetz, schwach reversibel (zu jeder Reaktion y → y′ ein gerichteter Weg zurück), positive
konstante Raten, Massenwirkungskinetik ẋ = Σ κ x^y (y′ − y): Jede strikt positive Lösung existiert für alle t ≥ 0, und es gibt ε ∈ (0, 1)
mit ε ≤ x_i(t) ≤ 1/ε.

**Bezug:** Die Kragenrekursion C5_M^(n) = (3/4)^n, C5_T^(n) = 1 − (3/4)^n ist ein einseitiger Übergang M → T. Ihr kontinuierliches
Gegenstück M → T ist nicht schwach reversibel; 149 greift nicht, und C5_M = x₀e^{−kt} ist für jedes endliche t positiv und geht gegen 0
(konsistent mit r86).

**Befunde:**
1. **Aus 149:** Hat der Austausch zwischen den Frames als Massenwirkungsnetz irgendeinen Rückweg, bleibt C5_M ≥ ε > 0 für alle Zeiten; die
   Übergangsfrage (1) aus r21 ist dann auch asymptotisch negativ. Beispiele: M ⇌ T mit Grenzwert k₂/(k₁ + k₂) (exakt, Untergrenze
   min{x₀, k₂/(k₁ + k₂)}); M + T ⇌ 2T mit Gleichgewicht k₂/(k₁ + k₂); ein Netz mit drei Frames (numerisch, min C5_M = Startwert 10⁻⁵).
   **C5_M → 0 verlangt einen Übergang ohne jeden Rückweg**, wie ihn die Kragenrekursion setzt.
2. **Klassisch, nicht aus 149:** Kein Massenwirkungsnetz, reversibel oder nicht, erreicht null in endlicher Zeit (die Verbrauchsterme einer
   Art enthalten deren Konzentration als Faktor). Eine endliche Null verlangt eine am Nullpunkt nicht Lipschitz-stetige Dynamik
   (Beispiel ẋ = −c√x, Null bei t* = 2√x₀/c) oder den Nulldurchgang einer vorzeichenbehafteten oder komplexen Größe. Beim Score S = N² ist
   ein Nulldurchgang von N eine doppelte Nullstelle von S.
3. **Folge für Form (iii):** Ein Zeuge außerhalb der Iteration kann keine Massenwirkungsdynamik sein. Es bleiben zwei Klassen:
   - eine nicht-Lipschitz-Dynamik am Nullpunkt (im Bestand nicht bekannt, hier nicht gesucht);
   - ein Nulldurchgang; für den ursprünglichen Score ist der einzige Kandidat dieser Art gescheitert (r21.12: Boden 0, Score ½).
4. **C6/T2:** Für ein Austauschnetz mit Rückweg ist die positive Untergrenze ε eine benannte bleibende Obstruktion im Sinn des
   Rückgabevertrags, aber nur für diese Modellklasse.

**Grenzen:** C5 ist im Companion diskret definiert; die Modellierung als Massenwirkungsnetz ist eine Setzung. Ob der Übergang zwischen den
Frames einen Rückweg hat, legt der Companion nicht fest (die Frame-Abbildungen sind invertierbar, das macht eine Dynamik noch nicht reversibel).
Eine Attraktor-Lesart für Ω_M (OP5) wird nicht verfolgt: Der Grenzwert k₂/(k₁ + k₂) hängt an gesetzten Raten, das Ziel wäre eine Eingabe.

## Ehrliche Buchführung
- Erkundung, nicht blind; keine H-Nummer, keine Runde. OP1 und C5 offen, kein Guard (C5 = 0, C6/T2) berührt, keine Vorhersage berührt.
- Wolfram-Warnungen: Linter-Hinweise auf „undefinierte“ Hilfssymbole (Lauf 1, harmlos) und interne `Part::pkspec1`-Meldungen bei DSolve
  (Lösung per Einsetzen geprüft, Rest 0); zwei Serverfehler des Konnektors (Block danach zerlegt); ein verworfener Zwischenlauf mit
  Konstruktionsfehler (gemeinsame Fixpunkte), in der Ausgabedatei vermerkt.
- Übernahme in den Companion (als Runde) nur auf Entscheidung des Autors; die Befunde 1.3 (Unterscheidung der Orientierung) und 2.3
  (Restklassen für Form (iii)) wären die Kandidaten.
