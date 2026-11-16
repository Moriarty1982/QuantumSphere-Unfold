# Ergebnis H106: Die vierte Dixon-Kopie schließt den Rest der Biegung nicht (widerlegt)

**16.11.2026.** Vorab-Notiz `Vorab_Notiz_H106_Singulett_Restbiegung.md` (Commit abf54a0), Skript `k228_test_h106.py`, Ausgabe
`k228_out.txt`. Blind nur darin, dass die Mechanismen M1 und M2 vor der Rechnung festgelegt waren; der Zielwert 2/3 war bekannt.

## Ergebnis: widerlegt

| Mechanismus | Kegelwinkel ψ | Phase φ | φ − 2/3 | det G | Singulettgewicht | Urteil |
|---|---|---|---|---|---|---|
| M0 (Kontrolle, Spin-1-Dreieck) | 38,68° | 0,679042 | +0,012376 | 0,0503 | 0 | – |
| M1 (Singulettgewicht ¼) | 45,30° | 0,640384 | −0,026282 | 0,0670 | 0,25 | kein Treffer |
| M2 (Normalen-Paare \|n_k⟩\|n_{k+1}⟩), zwei Lösungen | 38,68° / 141,32° | 0,679042 | +0,012376 | 0,0503 | 0,146 | kein Treffer |

Drei Versuche, kein Treffer innerhalb 0,001 rad. Nach dem Kriterium **widerlegt**.

## Was die Rechnung zeigt
- **M2 ändert nichts.** Die Überlappungen der Paarzustände sind Produkte der Spin-½-Überlappungen, und die Phase ist dieselbe wie beim
  Spin-1-Dreieck. Die Paare tragen zwar ein Singulettgewicht von 0,146, aber es verschiebt weder Überlappung noch Phase: Die
  „Normalen“ der Paare sind in diesem Bild nur eine andere Schreibweise desselben Dreiecks.
- **M1 schießt über das Ziel hinaus.** Ein gemeinsamer Singulettanteil senkt die Phase, mit Gewicht ¼ aber auf 0,640, also um das Doppelte
  des Rests zu weit. Die Lepton-Phase liegt zwischen „kein Singulett“ und „Gewicht ¼“.

## Nachträglich, ausdrücklich nicht Teil des Tests
Zwischen M0 und M1 gibt es ein Gewicht, das die Lepton-Phase genau trifft: **w = 0,0979** (Amplitude 0,313) bei ψ = 40,91°
(`k228_nachtraeglich.txt`). Dieser Wert ist an das Ziel angepasst und **wird nicht gedeutet**. Er liegt zufällig nahe am Gewicht 0,0976 der
Kästen |01⟩ und |10⟩ aus r25.5; diese Nähe ist nachträglich bemerkt, und ein Test dazu bräuchte eine neue Vorab-Notiz mit einem
Mechanismus, der das Gewicht vorher festlegt.

## Einordnung
- Das Singulett aus r25 speichert die Biegung (|det V|² = det G), legt ihren Wert aber auf diesen beiden einfachen Wegen nicht fest.
- Die Spin-1-Notiz bleibt gültig: Der Rest 0,012376 ist offen; ein gemeinsamer Singulettanteil kann ihn in beide Richtungen verschieben,
  braucht aber ein festgelegtes Gewicht.
- OP3 bleibt offen. H102 (m_τ aus dem Fluss) ist davon unberührt.
