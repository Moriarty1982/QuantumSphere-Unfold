# Erkundung: Potential für ρ² = 1/2 und T₁₂ als dynamisches Feld

13. November 2026, spät. Autorenauftrag: „erst die Fäden“ (Fäden „Potential für ρ² = 1/2“ und „T₁₂ als dynamisches Feld“
aus der Übergabe). Erkundung, analytisch mit numerischer Prüfung, nicht blind, kein Datenvergleich. Keine H-Nummer.
Skript `op3_koide_potential_2026_11_13.py`, Ausgabe `..._out.txt`.

## Vorwissen geprüft
- v4.8.0-r16 (H11): invariante Potentiale bis Grad 4 auf dem Tripelraum geben höchstens zwei verschiedene Platznormen;
  v4.9.0-r26 (H16): Grad 6 nötig; r32, r33 (H18) widerlegt.
- Gram-Notiz (K = (1 + 2ρ²)/3), `op3_slot_u3_gauging_2026_11_13.md` (T₁₂ als Feld: Familienbosonen massiv, α_F = 4α in
  Auslesung A), Sumino arXiv:0812.2103 (Potential mit abgestimmten Kopplungen, Bedingung (34)).

## Faden 2: Potential für ρ² = 1/2

1. **Invarianten.** Mit s_k = 1 + 2ρ cos(θ + 2πk/3): tr S = 3, tr S² = 3 + 6ρ², tr S³ = 3 + 18ρ² + 6ρ³ cos 3θ (numerisch
   10⁻¹⁴). Koide ist eine Bedingung an tr S² allein: tr S² = (2/3)(tr S)².
2. **Grad 4 in X** (S quadratisch in X): a tr S² + b (tr S)² ist linear in ρ²; ein Extremum liegt nur am Rand. Kein Koide.
3. **Grad 6:** V = α ρ² + β ρ⁴ + γ ρ³ cos 3θ. ρ² = 1/2 für jedes θ verlangt γ = 0 und α/β = −1. Das Verhältnis ist
   abgestimmt; ein natürlicher Grund fehlt. Das passt zu r16 und r26 und zu Sumino, der ebenfalls abstimmt.
4. **Gleichwertige Lesarten von K = 2/3** (Hinweise auf ein Prinzip, nicht hergeleitet):
   - Reinheit der normierten Gram-Matrix S/3 ist 2/3;
   - K liegt genau in der Mitte des möglichen Bereichs [1/3, 1] (gleiche Massen bis eine Masse);
   - Gleichverteilung zwischen Diagonale und Nebendiagonale: ‖S − 1‖² = ‖1‖² = 3;
   - im zirkulanten Fall paarweise Treue 1/2 (wie Qubit-Zustände an orthogonalen Achsen).
5. **Ein nicht abgestimmter Kandidat scheitert:** V = tr(S² − 2S)² („S ist das Doppelte eines Projektors“) hat bei
   tr S = 3 sein Minimum bei s = (0,145; 0,755; 2,100), K = 0,556. Kein Koide.

**Bewertung Faden 2.** Ein Potential liefert ρ² = 1/2 nur mit einem abgestimmten Verhältnis zweier Kopplungen (Grad 6).
Koide verlangt ein Auswahlprinzip, keinen generischen Potentialterm; die gleichwertigen Lesarten (Mitte des Bereichs,
Gleichverteilung, Treue 1/2) sind Kandidaten für ein solches Prinzip, keines ist im Companion hergeleitet.

## Faden 3: T₁₂ als dynamisches Feld

- Als Feld mit C → U† C U* (Zwei-Sonden-System, L in 3, R in 3̄) hat T₁₂ als U(3)-Invarianten nur die Singulärwerte:
  tr (C C†)ⁿ und |det C|. Ein Potential für T₁₂ ist daher ein Potential in den Gram-Eigenwerten der Auslesung A, also
  genau Faden 2: Koide (ρ) und Phase (θ, über det) brauchen je eine abgestimmte Zahl.
- Der kinetische Term gibt die Familienbosonen mit α_F = 4α (`op3_slot_u3_gauging_2026_11_13.md`); daran ändert die
  Dynamik nichts.
- Die Einheitsdiagonale der Gram-Lesart ist keine U(3)-invariante Bedingung; als Feldtheorie reicht tr S = 3 (Normierung),
  und Koide ist dann tr S² = 6, vollständig invariant.

**Bewertung Faden 3.** T₁₂ lässt sich widerspruchsfrei dynamisch machen (Yukawa-Feld im Sinne der Yukawaon-Modelle von
Koide). Die Brannen-Parameter ρ und θ werden dabei zu zwei abgestimmten Kopplungen; eine Vorhersage entsteht nicht.

OP3/OP4 offen; OP1–OP5, C5, C6/T2 unverändert; H100 unberührt.

## Nachtrag: Auswahlprinzip, Koide als qubitartige Treue (13.11., spät, Autor: „weiter“)

Vorwissen: Gram-Notiz, Punkt 5 (Mittel von K über reelle Einheitsvektoren im R^n ist (1 + 2/n)/3, für n = 2 genau 2/3).
Skript, Abschnitt „Auswahlprinzip“. Nicht blind, kein Datenvergleich.

1. **Auch komplex gilt der Mittelwert.** Für Haar-zufällige Zustände in C^d ist die mittlere Treue 1/d (numerisch
   0,5008; 0,3342; 0,2508 für d = 2, 3, 4), also K im Mittel (1 + 2/d)/3: **2/3 genau für Qubits**.
2. **Qubit-Tripel liegen immer auf dem Rand.** Drei Zustände in C² haben eine Gram-Matrix vom Rang 2 (det = 0); bei
   ρ² = 1/2 ist dann θ = π/12.
3. **Drei Koide-Fakten zeigen auf Qubits.** ρ² = 1/2 ist (a) die mittlere Treue zufälliger Qubits, (b) die Treue der
   Qubits an orthogonalen Achsen (Oktant, Rand des Bogens), (c) unter Spins j an orthogonalen Achsen nur für j = 1/2
   erreicht.
4. **Was das nicht erklärt.** Das Mittel streut: Die Standardabweichung von K über zufällige Qubit-Tripel ist 0,11, kein
   einziges von 20 000 Tripeln trifft 2/3 auf 10⁻⁵. Die Genauigkeit der Pol-Koide-Beziehung (2·10⁻⁶) folgt aus einem
   Mittelwert nicht. Die geladenen Leptonen haben zudem Rang 3 (Bargmann-Phase 0,667 < π/4): qubitartige Treue, aber
   aus der Qubit-Ebene herausgehoben.

**Bewertung.** Koide lässt sich einheitlich als „paarweise Treue wie bei einem Qubit“ lesen; Mittelwert, Oktant und
Spin 1/2 sind drei Seiten derselben Zahl. Ein Auswahlprinzip, das die Treue genau auf 1/2 festlegt und die Plätze
zugleich aus der Qubit-Ebene hebt, fehlt. Lesart, keine Herleitung; Numerologie-Vorbehalt wie in der Gram-Notiz.
