# Vorab-Notiz H108: Schließen verschränkte Generationszustände auf zwei Kopien-Qubits den Rest der Biegung?

Festgelegt am 2026-11-16, **vor** der Rechnung. Auftrag des Autors: „Verschränkte Zustände“, nach H107. Einordnung OP3, r25, H106, H107.
Skript `k230_test_h108.py` (wird nach dieser Notiz geschrieben; ausgeführt erst, wenn der Autor die Familie freigibt).

## Anlass
H107 zeigte: Für kohärente Produktzustände |n⟩|n⟩ trägt eine verschachtelte Normierung HS(8) = HS(7) ⊕ HS(6) ⊕ HS(6) nichts über HS(7) hinaus.
Information trägt sie erst bei Zuständen, die über die beiden Kopien-Bits verschränkt sind. Gesucht ist eine verschränkte Familie ohne freien
Parameter, die den Rest 0,012376 zwischen dem Spin-1-Dreieck (0,679042) und der Lepton-Phase schließt.

## Vorwissen geprüft
- `Ergebnis_H106_*`, `Ergebnis_H107_*`: Singulettbeimischung und verschachtelte Normierung widerlegt; Produktzustände tragen keine Information
  über HS(7) hinaus.
- `../op3_spin1_triangle_2026_11_15/`: Spin-1-Dreieck (kohärente Zustände), Phase 0,679042.
- `../op3_dixon_copies_2026_11_16/` (r25): Triplett der zwei Kopien-Qubits = Spin 1.
- `../op3_majorana_vector_n_2026_11_14.md`: Majorana-Vektor auf dem neutralen Qubit (anderer Gegenstand).
- Suche nach „Majorana-Darstellung“, „stellar“, „polar state“: keine Vorbefunde zu Generationszuständen.

## Grundlage: die Majorana-Darstellung
Jeder Zustand des Tripletts (symmetrischer Teil von C² ⊗ C²) ist bis auf eine Phase eindeutig durch zwei Punkte a, b auf der Kugel bestimmt:
g ∝ |a⟩|b⟩ + |b⟩|a⟩ (|·⟩ kohärente Spin-½-Zustände). Für a = b ist g kohärent (Produktzustand, unverschränkt); für a ≠ b ist g verschränkt;
für b = −a ist g der polare Zustand |1, 0⟩_a, maximal verschränkt.

## Festgelegte Familie
Die drei Generationen sitzen wie bisher auf dem Kegel: n_k mit halbem Öffnungswinkel ψ um die Zyklusachse z, Azimut 2πk/3. Generation k hat
den ersten Majorana-Punkt n_k; der zweite Punkt ist einer der **natürlichen Punkte der Konstruktion** (die anderen Kegelpunkte, die Pole der
Zyklusachse, die Gegenpunkte):

| Name | zweiter Punkt | Bemerkung |
|---|---|---|
| E1 | n_{k+1} (Nachbar) | n_{k−1} gibt den gespiegelten Fall mit gleichem \|φ\|, nicht doppelt gezählt |
| E2 | +z (Pol der Zyklusachse) | gemeinsamer Bezugspunkt aller drei Generationen |
| E3 | −z | |
| E4 | −n_k (Gegenpunkt) | polarer Zustand; analytisch Phase 0 oder π erwartet (reelle Vektoren), als Kontrolle mitgezählt |
| E5 | −n_{k+1} (Gegenpunkt des Nachbarn) | −n_{k−1} wie bei E1 nicht doppelt gezählt |

ψ folgt aus |⟨g_j|g_k⟩|² = ½ (K = 2/3); jede Lösung ist ein Versuch. Vorhersage ist die Bargmann-Phase φ. Kein Singulettanteil (die Zustände
liegen ganz im Triplett).

## Entscheidungskriterium (vor der Rechnung festgelegt)
- Zielwert: Lepton-Phase aus Polmassen 0,666665.
- **bestätigt**, wenn genau ein Mechanismus eine Lösung mit |φ − 0,666665| ≤ 0,0002 rad hat; **mehrdeutig** bei mehr als einem; **widerlegt**
  bei keinem.
- Zufallserwartung, vorab geschätzt: bis zu zehn Lösungen, je etwa 0,7 % Trefferwahrscheinlichkeit, also etwa 0,07.

## Offenlegung
- Der Zielwert war bekannt; blind ist der Test nur darin, dass die Familie vor der Rechnung festgelegt ist.
- Die Wahl „erster Punkt n_k, zweiter aus den natürlichen Punkten“ ist eine Setzung. Andere verschränkte Familien (mit freien Parametern)
  werden nicht geprüft.
- Ein Treffer wäre eine Lesart des Rests, keine Herleitung der Überlappung ½.

## Ablauf
1. Diese Notiz committen.
2. `k230_test_h108.py` schreiben; nach Freigabe ausführen (Ausgabe `k230_out.txt`).
3. Ergebnis-Notiz `Ergebnis_H108_Verschraenkte_Generationen.md`.
