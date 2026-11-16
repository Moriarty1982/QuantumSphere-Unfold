# Vorab-Notiz H109: Schließt eine generationsabhängige Frame-Lesung den Rest der Biegung?

Festgelegt am 2026-11-16, **vor** der Rechnung. Auftrag des Autors: „Neue Familie prüfen“, nach der Erkundung
`../op3_frame_typed_halves_2026_11_16/` (Frage des Autors: „Partitionierungen in verschiedenen Frames lesen?“). Einordnung OP3, r16.7, r25,
H106–H108. Skript `k231_test_h109.py` (nach dieser Notiz geschrieben, ausgeführt erst nach dem Commit der Notiz).

## Anlass
Die Erkundung zeigte: Liest man alle drei Generationen im selben Frame (halbe Drehung $R=\sigma_z$, $T=\sigma_x$ oder $J_B=\sigma_y$ auf jedem
Kopien-Qubit), brechen die Kastengewichte die Generationsgleichheit; zykluserhaltende gemeinsame Lesungen geben nichts Neues. Die drei
Frame-Achsen werden aber von der Drehung um die Zyklusachse $(1,1,1)/\sqrt3$ zyklisch vertauscht. Ordnet man jeder Generation einen
**eigenen** Frame zu, und zwar zyklisch, dann ist die Lesung wieder generationsgleich (dieselben Kastengewichte für alle drei; in der
Erkundung sichtbar: die Gewichtsvektoren laufen unter $R$, $T$, $J_B$ zyklisch um). Das ist die neue Familie.

## Vorwissen geprüft
- `../op3_frame_typed_halves_2026_11_16/`: gemeinsame Frame-Lesung bricht die Generationsgleichheit; zykluserhaltende Lesungen = H107-Werte.
- `../op3_frame_mass_normalization_2026_11_12.md`: Zeile „Native generationsabhängige Rückauslesung? In den geprüften Quellen nicht
  ausgewertet“; kein Vorbefund, keine native Begründung.
- `../v4_10_0_r16/` (r16.7): höchstens drei paarweise nicht orthogonale Auslesungen eines Objekts; sie bilden ein Oktant.
- `Ergebnis_H106_*`, `Ergebnis_H107_*`, `Ergebnis_H108_*`, `../op3_renormalisation_2026_11_16/`: vier Wege widerlegt bzw. ohne Erfolg.
- Suche nach „generationsabhängig“, „Frame je Generation“ in `notes/research/`: sonst nur Sumino-/Schwellen-Notizen (anderer Gegenstand).

## Festgelegte Familie
Generationszustände wie in der Erkundung: $g_k=|n_k\rangle|n_k\rangle$, $n_k$ auf dem Kegel mit halbem Öffnungswinkel $\psi$ um die
Zyklusachse, Azimut $2\pi k/3$. Frame-Abbildungen $F\in\{R,T,J_B\}=\{\sigma_z,\sigma_x,\sigma_y\}$. Zulässig sind nur die drei **zyklischen**
Zuordnungen Generation → Frame (die drei anderen Permutationen brechen die Generationsgleichheit und werden nicht gezählt):

| Zuordnung | Generation 0, 1, 2 |
|---|---|
| Z1 | $R$, $T$, $J_B$ |
| Z2 | $J_B$, $R$, $T$ |
| Z3 | $T$, $J_B$, $R$ |

Zwei Lesungen je Zuordnung:

| Lesung | Operator auf Generation k | Bedeutung |
|---|---|---|
| L1 | $F_k\otimes F_k$ | ganze Generation im eigenen Frame |
| L2a | $P_0\otimes 1 + P_1\otimes F_k$ | Hälfte H0 im Bezugsframe (keine Abbildung), Hälfte H1 im Frame der Generation |
| L2b | $P_0\otimes F_k + P_1\otimes 1$ | umgekehrt |

$P_0,P_1$ sind die Projektoren des ersten Kopien-Bits in der Basis der Zyklusachse (wie die Hälften in H107). Das ergibt **9 Mechanismen**
(3 Zuordnungen × 3 Lesungen). $\psi$ folgt aus $|\langle g'_j|g'_k\rangle|^2=\tfrac12$ für die gelesenen Zustände $g'_k$ (alle Lösungen in
$(0,\pi)$, jede Lösung ein Versuch). Vorhersage ist die Bargmann-Phase $\varphi=|\arg(\langle g'_0|g'_1\rangle\langle g'_1|g'_2\rangle
\langle g'_2|g'_0\rangle)|$. Kontrolle (nicht gezählt): ohne Abbildung muss 0,679042 herauskommen; die Generationsgleichheit wird je
Mechanismus geprüft (gleiche Kastengewichte), ein Bruch wird gemeldet.

## Entscheidungskriterium (vor der Rechnung festgelegt)
- Zielwert: Lepton-Phase aus Polmassen 0,666665.
- **bestätigt**, wenn genau ein Mechanismus eine Lösung mit $|\varphi-0{,}666665|\le 0{,}0002$ rad hat; **mehrdeutig** bei mehr als einem;
  **widerlegt** bei keinem.
- Zufallserwartung, vorab geschätzt: 9 Mechanismen, bis zu etwa 18 Lösungen, je etwa 0,7 % Trefferwahrscheinlichkeit, also etwa 0,1.

## Offenlegung
- Der Zielwert war bekannt; blind ist der Test nur darin, dass Familie und Versuchszahl vor der Rechnung festgelegt sind.
- Die generationsabhängige Zuordnung hat im Bestand **keine native Begründung** (siehe Vorwissen). Sie ist eine Setzung, die einzig durch
  die Zyklussymmetrie eingeschränkt ist. Ein Treffer wäre eine Lesart des Rests, keine Herleitung; er bräuchte danach eine Begründung, warum
  Generation k im Frame $F_k$ gelesen wird.
- Andere Lesungen (z. B. Hälften in zwei verschiedenen Frames, beliebige Achsen) werden nicht geprüft.

## Ablauf
1. Diese Notiz und das Skript committen.
2. `k231_test_h109.py` ausführen (Ausgabe `k231_out.txt`).
3. Ergebnis-Notiz `Ergebnis_H109_Generationsabhaengige_Frames.md`.
