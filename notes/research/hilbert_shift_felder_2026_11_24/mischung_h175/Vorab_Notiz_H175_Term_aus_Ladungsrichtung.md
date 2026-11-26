# Vorab-Notiz H175: Kleine Drehung der geladenen Leptonen aus einem Term der Ladungsrichtung (s–v-Kopplung)

**Stand:** 26.11.2026, vor der Rechnung festgelegt. Anlass: Autor, 26.11.2026, „versuch es mal, sonst schau mal was passiert wenn du die einzeln mit ein paar
stichproben durchgehst die möglichkeiten […] und die dann varieren, evtl. auch mit so einem algorithmus den du zum bilder generieren bentutzt“.
Einordnung: `wiki/Gesamtbild.md`, T8/T13, OP3/OP4, Strang 3. Vergeben: H175, k371 (Test), k372 (anschließende Erkundung); geprüft: frei.
**Blind:** Die Mischungswinkel dieser Konstruktion sind nicht gerechnet. Vor der Festlegung gerechnet ist nur der Aufbau (welche Matrizen die Symmetrie erlaubt, siehe unten).
Bekannt aus H174a: Der nötige Term hat einen imaginären antisymmetrischen Anteil; daher die Vermutung. Insofern ist die Richtung nicht unabhängig von den Daten gewählt.

## Vorwissen geprüft
- **H174** (`../mischung_h174/`): reelle Beimischung der neutralen Form trägt nicht; nötiger Term rund 78° gegen N̂, zur Hälfte imaginär-antisymmetrisch, e–μ-Element 0,045 bis 0,052.
- **k369** (`../mischung_h173/k369/`): freie e–μ-Drehung mit Phase gibt χ² = 2,3 (zwei Parameter).
- **k262** (`../setzungen_k262/`): Die Gruppe wirkt auf s und v getrennt; ein ungerades Element A wirkt auf s als A, auf v als −A. Neutrinos auf s, geladene Leptonen auf z = s + iv.
- **H169/H170**: geladener Term = Mischung von s und v (c = 1), σ-ungerade.
- Suche nach „s–v-Kopplung“, „antisymmetrisch“ zusammen mit „Mischung“ in `notes/research/hilbert_shift_felder_2026_11_24/`, `wiki/`: kein Vorbefund zu dieser Konstruktion.

## Aufbau (vor der Festlegung gerechnet, nur Lineare Algebra)
Eine hermitesche Form auf z = s + iv ist H = S + iK mit S reell symmetrisch und K reell antisymmetrisch; iK ist genau die Kopplung zwischen s und v.
Unter A (s ↦ As, v ↦ −Av) bleibt die Kopplung invariant, wenn AᵀKA = −K. Mit A = {{0,0,−1},{0,1,0},{−1,0,0}} ist dieser Raum zweidimensional:
K₁ = E₁₃ − E₃₁ und K₂ = (−E₁₂ + E₂₁ + E₂₃ − E₃₂)/√2; beide sind nicht zirkulant. Die übrigen Klassen (zum Vergleich): symmetrisch A-gerade (4, davon 3 nicht zirkulant;
enthält N̂), symmetrisch A-ungerade (2), antisymmetrisch A-gerade (1). Zusammen 9 = alle hermiteschen Richtungen; 3 davon sind zirkulant, 6 brechen ℤ₃.

**Hypothese:** M_e = a_e·(Ĉ(ρ, δ) + i(κ₁K₁ + κ₂K₂)), M_ν ∝ N̂(π/6 − x) wie H173. a_e, ρ, δ werden an die drei Massen angepasst (Zweig mit dem Elektron auf dem
T-Eigenwert 1). Daten wie H174. **Werkzeugwahl:** Python (numpy, scipy), Wolfram für die Nachrechnung des besten Punkts. Qiskit nicht geeignet.

## Hypothesen und Kriterien
- **H175a (blind): Die Ladungsrichtung genügt.** Anpassung von (κ₁, κ₂) an sin²θ₁₃, sin²θ₁₂ (JUNO), sin²θ₂₃. **Verträglich**, wenn das Minimum alle drei innerhalb
  2σ/2σ/3σ hat; **widerlegt**, wenn nicht. Zwei Parameter für drei Messgrößen: Ein „verträglich“ ist kein Beleg, nur keine Widerlegung. Zum Vergleich wird dieselbe
  Anpassung für jede der anderen Symmetrieklassen berichtet (Mehrfachvergleich: vier Klassen).
- **H175b (blind): Eine Richtung genügt.** K₁ allein und K₂ allein, je ein freier Parameter. **Trägt**, wenn eine Richtung allein alle drei Größen innerhalb 2σ/2σ/3σ
  trifft (ein Parameter für drei Messgrößen); sonst **trägt nicht**.
- **H175c (blind): Feste Stärke.** κ = ± tan x, ± tan 2x in K₁ allein, K₂ allein und in der Kombination (K₁ ± K₂)/√2 (24 Fälle). **Verträglich**, wenn ein Fall
  2σ/2σ/3σ erfüllt; **widerlegt**, wenn kein Fall sin²θ₁₃ innerhalb 3σ erreicht; sonst **nicht entschieden**. Urteil diesmal ausdrücklich: Ein Fall, der θ₁₃ trifft und
  eine andere Größe um mehr als 5σ verfehlt, zählt als **nicht verträglich**.
- Berichtet wird jeweils sin δ_CP und der Koide-Wert des zirkulanten Teils.

## Danach (Erkundung k372, keine Hypothese, nicht blind)
Alle sechs ℤ₃-brechenden Richtungen einzeln: Ableitungen der drei Winkel, von sin δ und der Massen nach jeder Richtung (welche Eingabe bewirkt was). Dann eine
stochastische Suche im sechsdimensionalen Raum (Rauschen und schrittweises Abkühlen, wie beim Entrauschen in der Bilderzeugung; technisch eine abgekühlte
Metropolis-Suche mit vielen Startpunkten), um die Menge der verträglichen Punkte zu beschreiben: kleinste nötige Stärke, welche Richtungen sie braucht, ob sie in
einem Symmetrie-Unterraum liegt. Alles dort ist angepasst, nicht hergeleitet, und wird so gekennzeichnet.

## Grenzen (vorab)
- Dass die s–v-Kopplung bei den geladenen Leptonen auftritt, ist eine Setzung; ihre Stärke ist in a und b frei. Gleiche Normierung wie H174.
- Die Wahl des ungeraden Elements A ist die aus k262b; die anderen fünf ungeraden ℤ₂ sind nicht geprüft.
- Keine Maske. OP3 und OP4 bleiben offen. Kein Vorzeichen gesetzt.
