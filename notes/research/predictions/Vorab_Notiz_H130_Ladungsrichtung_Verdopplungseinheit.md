# Vorab-Notiz H130: Legt der Turm die Ladungsrichtung relativ zur Verdopplungseinheit fest?

**Stand:** 2026-11-25, vor der Rechnung festgelegt. **Teilweise nicht blind** (siehe „Vorab offengelegt“). Anlass: Autor, 25.11.2026, 10:19 UTC: „merge und dann bitte rechnen“,
auf die in H128 genannte nächste Frage. Skripte **k258** (Python numpy/scipy; Wolfram Language exakt zur Kontrolle der gefundenen Unteralgebren). Qiskit nicht vorgesehen
(keine Schaltung). Bezug OP3 (#131). H129 ist an den Feldgleichungs-Faden vergeben, deshalb H130.

## Vorwissen geprüft
- **H128** (#297, k283): Der(H₃(𝕊)) = g₂ ⊕ su(3); für ein Feld in H₃(ℂ_u) ist das Massenverhältnis r(u) = 1 − (1 − u₈²)/10. Offen blieb, was u₈ festlegt; r42 setzt u = e₇.
- **k254** (#280): Aut(𝕊) = G₂ × S₃; drei Oktonion-Kopien O_0, O_120, O_240 (Schnitt nur ℝ), jede von einer Spiegelung festgehalten; 𝕊 = (1,1) ⊕ (1,sgn) ⊕ (7,2).
- **k253** (#279), **k270–k272** (#283): Bei HS(3) genau eine feste Einheit u in 𝕆 mit C = ½(1 + iL_u), Stabilisator su(3); die Richtung von u ist dort frei (G₂ transitiv auf S⁶).
  Leiterzahl N_c = 0, 1, 3, 3, 4 für n = 1 … 5.
- **r42/r43** (Projektor ½(1 + iL_e₇)), `op3_dixon_times_sedenions_2026_11_16/`, `op3_dixon_copies_2026_11_16/`.
- Im Repo gibt es keine Klassifikation der su(3)-stabilen Oktonion-Unteralgebren von 𝕊 (Suche 25.11.). Literatur dazu ist mir nicht bekannt (aus Vorwissen, ungeprüft).

## Aufbau
- 𝕊 mit der Konvention aus k253. su(3)_c := Stabilisator von e₇ in Der(𝕊) = g₂ (Dimension 8). Unter su(3)_c zerfällt 𝕊 in die Singuletts Q = span(1, e₇, e₈, e₁₅)
  und den Triplett-Teil T (12 reelle Dimensionen, zwei Kopien von ℂ³).
- **Zulässiges Paar (u, 𝔸):** 𝔸 ⊂ 𝕊 ist eine achtdimensionale Unteralgebra, die unter su(3)_c stabil ist und in der su(3)_c wie bei HS(3) wirkt (1 ⊕ 1 ⊕ 3 ⊕ 3̄),
  also 𝔸 = span(1, u) ⊕ V mit u ∈ Q imaginär, |u| = 1, und V ⊂ T sechsdimensional und su(3)_c-stabil. „Oktonionisch“ heißt zusätzlich alternativ und normmultiplikativ.
  Das ist die Forderung, dass die Konstruktion einer Generation aus HS(3) (Ladungsrichtung u, Träger 𝔸) in 𝕊 unverändert möglich ist.
- **Parametrisierung:** u = u₇e₇ + u₈e₈ + u₁₅e₁₅ auf S²; V(a, b, c, d) = {(a + bJ)x + ((c + dJ)x)·e₈ : x ∈ span(e₁ … e₆)} mit J = L_e₇, (a, b, c, d) auf S³ (ein Punkt von ℂP¹).
  Das sind alle su(3)_c-stabilen sechsdimensionalen Teilräume von T (Kontrolle unten).
- **Suche:** Abschlussdefekt D(u, V) = Σ ‖(1 − P_𝔸)(pq)‖² über eine Basis p, q von 𝔸. Nullstellen per kleinster Quadrate aus mindestens 400 Zufallsstarts; Lösung, wenn D < 10⁻²⁰.
  Je Lösung: u₈², Alternativität und Normmultiplikativität auf Zufallselementen von 𝔸, Rang der Jacobi-Matrix (flache Richtungen), r = 1 − (1 − u₈²)/10.

## Vorab offengelegt (analytisch, kein Teil der Vorhersage)
1. O_0 = span(e₀ … e₇) mit u = e₇ ist ein zulässiges Paar, ebenso die Bilder O_120, O_240 (dort u = cos·e₇ + sin·e₁₅). Alle haben u₈ = 0.
2. Die Symmetrien, die su(3)_c erhalten, sind diskret bis auf Phasen, die u₈ nicht ändern (S₃ wirkt auf (e₇, e₁₅) als Drehspiegelung, auf e₈ als Vorzeichen). Eine stetige
   Schar von Lösungen mit veränderlichem u₈ wäre also keine Symmetriebahn.
3. **Hinweis auf ein mögliches Gegenbeispiel zu H130b:** Für u = e₈ und V = {x + (Jx)e₈} heben sich die e₇- und e₁₅-Anteile der Produkte in einer Überschlagsrechnung
   paarweise auf. Ob das eine abgeschlossene, alternative Algebra gibt, habe ich nicht gerechnet. Ich halte H130b deshalb für unsicher.

## Hypothesen und Kriterien
- **H130a (der Turm lässt nur endlich viele Werte zu):** Die Menge der Werte u₈² über alle zulässigen oktonionischen Paare ist endlich.
  - **Bestätigt:** Alle Lösungen fallen auf höchstens sechs Werte von u₈² (Abstand < 10⁻⁶), und an keiner Lösung gibt es eine flache Richtung, die u₈ ändert.
  - **Widerlegt:** Es gibt eine stetige Schar von Lösungen mit veränderlichem u₈ (dann ist der Winkel frei).
- **H130b (das Verhältnis 9/10 ist festgelegt):** Es kommt nur u₈ = 0 vor.
  - **Bestätigt:** u₈² < 10⁻⁸ für alle oktonionischen Lösungen. **Widerlegt:** Eine oktonionische Lösung mit u₈² > 10⁻⁶.
- **Kontrollen:** (i) dim su(3)_c = 8, Singuletts genau Q, V(a, b, c, d) ist su(3)_c-stabil (Rest < 10⁻¹¹). (ii) Die Suche findet O_0 und beide Bilder (D < 10⁻²⁰).
  (iii) Wolfram rechnet Abschluss und Alternativität jeder Lösungsklasse exakt nach, soweit sie rationale oder einfache algebraische Koordinaten hat.
  Fehlt (i) oder (ii), ist der Lauf ungültig.
- Abgeschlossene, aber nicht alternative Unteralgebren werden getrennt berichtet und zählen nicht als Lösung.

## Folge, vorab festgelegt
- **a und b bestätigt:** Verlangt man, dass eine Generation wie bei HS(3) gebaut werden kann, liegt die Ladungsrichtung senkrecht zur Verdopplungseinheit. Dann ist SU(3) → SO(3)
  erzwungen und das Verhältnis 9/10 der Form K ein Ergebnis und keine Wahl von u. Gesetzt bleibt die Forderung selbst und die Form K.
- **a bestätigt, b widerlegt:** Es gibt endlich viele Lagen, darunter eine mit u₈ ≠ 0. Dann stehen mehrere Verhältnisse zur Wahl, die Auswahl bleibt offen und wird benannt.
- **a widerlegt:** Der Winkel ist frei; der Turm legt das Verhältnis nicht fest. Dann wird er wie das Vorzeichen als offene Eingabe an die Feldgleichung übergeben.
- In jedem Fall bleiben OP3 und OP4 offen, kein Guard wird berührt. Nicht gezeigt wird, dass die Plätze Generationen sind.
