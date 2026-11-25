# Vorab-Notiz H147: Ist die HS(0)-Linie des Rests das Austauschteilchen der Gravitation?

**Stand:** 25.11.2026, vor der Rechnung festgelegt. **Großteils nicht blind:** Neutralität und Masselosigkeit sind aus H145/H146 bekannt; die
Drehgruppen-Zerlegungen sind Darstellungstheorie und werden nur nachgerechnet. Anlass: Autor (25.11.2026, 20:41): „unser neuer quasi HS(0)
dürfte doch verschwindend klein sein, könnte das unser gesuchtes Austauschteilchen zur Gravitation sein?“ und (20:42): „ist die Tensorstruktur
nicht schon durch den Raum, in dem es erzeugt wird, automatisch gegeben?“ Vorzeichen nicht setzen.

## Vorwissen geprüft
- H145: Rest-Generation = R⁰ ⊗ ℂ𝕆, Linie c = (−1, −1, 1, 1) reell, ohne Ladung und Farbe, zeitumkehrfest; Produkt zweier Rest-Zustände trägt
  die Gewichte c ∘ c = (1, 1, 1, 1). H146: In der Gram-Auslesung ist c der exakte Nullvektor (masselos). H144: Leptonen des Rests |s| = ½,
  Quarks s = 0.
- Gravitation im Projekt: W1/W2 (Einstein–Cartan, r81–r86), Metrik gesetzt, kein Austauschteilchen hergeleitet; für das Maxwell-Feld ist die
  Gravitation frame-blind (r06/r07). Spin-1/Spin-2-Trennung bisher nur auf dem Generationsindex (H128, H130, k278/k279: SO(3) ⊂ SU(3)_Familie),
  nicht im Ortsraum.
- Eine Drehgruppe des Ortsraums ist in A₅ nicht ausgezeichnet. Kandidaten innerhalb der Symmetrie der Kopien (G₂ wirkt auf jede Kopie gleich):
  **(A)** SO(3) ⊂ SU(3)_Farbe als reelle Form (Stabilisator eines total reellen 3-Raums im Farbraum), **(B)** die Hauptuntergruppe SO(3) ⊂ G₂
  (Im𝕆 irreduzibel, Spin 3). Auf dem Kopienindex wirkt nur Diskretes (S₃ × S₃).

## Merkmale eines Gravitons und Hypothesen
- **H147a (nicht blind):** neutral (Q und su(3) trivial auf c) und in der Gram-Auslesung masselos. Übernommen aus H145b, H146b, nachgerechnet.
- **H147b (gewertet, Spin der Linie und des Rests):** Die Linie c ist unter jeder stetigen Gruppe, die auf den Kopien wirkt, ein Skalar (Spin 0).
  Die Rest-Generation hat unter (A) die Spins {0, 0, 1, 1}, unter (B) {0, 0, 3, 3} (komplex gezählt je 1 ⊕ 7), **in keiner Lesart Spin 2**.
  Widerlegt, wenn eine der Zerlegungen Spin 2 enthält.
- **H147c (gewertet, Marcs Teilfrage „Tensor aus dem Raum“):** Ein symmetrischer Spin-2-Anteil entsteht aus zwei Rest-Zuständen nur im äußeren
  Tensorprodukt Sym²(Rest) (unter A und B enthalten), **nicht** über das Produkt der Algebra: Der symmetrische Teil (xy + yx)/2 landet in ℂ𝕆
  und enthält kein Spin 2. Im antisymmetrischen Ableitungskanal D_{x,y} ∈ g₂ liegt dagegen unter (A) ein Spin-2-Anteil (die 5 in su(3) =
  symmetrische spurfreie reelle 3×3-Matrizen). Bestätigt, wenn alle drei Aussagen numerisch stimmen; sonst widerlegt (Abweichung berichten).
- **H147d (gewertet, Universalität):** Die Kopplung zweier Rest-Zustände an die Kopien ist gleichgewichtet (c ∘ c ∝ Einsvektor auf dem Träger der
  Relation) in allen 54 Generationsauswahlen (H142, H143); die Linie selbst koppelt mit wechselndem Vorzeichen.

## Folge, vorab festgelegt
- b, c, d bestätigt: Die Linie ist ein masseloser, neutraler **Skalar** (eher Dilaton-artig als Graviton). Ein Spin-2-Teil mit gleichgewichteter
  Kopplung entsteht nur als Bilinear zweier Rest-Zustände im äußeren Tensorprodukt, also durch eine zusätzliche Regel (Metrik), die die Algebra
  nicht liefert; die Algebra selbst bietet Spin 2 nur antisymmetrisch (Ableitungen). Das ist eine Lesart, keine Herleitung eines Gravitons.
- Was nicht folgt: Kopplungsstärke, Newton-Konstante, Λ, Bezug zu W1/W2. Welche SO(3) der Ortsraum ist, bleibt gesetzt. OP5 und die
  Gravitationsfragen offen; kein Guard berührt.
- Werkzeuge: Python (numpy), Wolfram exakt für die Spin-Zerlegung unter (A). Qiskit nicht eingesetzt. Vergeben: H147, k330.
