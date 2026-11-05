# Erkundung: Die Phase der Spinoren unter der zweiten Lesart (−1 aus F3 oder −i aus g ↦ −g)? (5. November 2026)

**Status: Erkundung, analytisch, ohne Kriterium.** Anschluss an H83 (Regel R2: aus g ↦ −g folgt für die Weyl-Kinetik die Phase −i, nicht das F3-Minus aus H79).

## Vorwissen geprüft
H79 (holomorphe Adjungierte; das Minus der Weyl-Kinetik über F3 als Gewicht 1 gesetzt); r81/k174 (s_T = −1 für die masselose Weyl-Kinetik, „Gewicht 1, Phase −1“); r81.2–3 und k170 (komplexe Lesart K: bei symmetrischer Kinetik leer, bei nicht symmetrisierter mit unabhängiger Verbindung j = 0, also Ψ = 0 in einem Frame); r22.2 (F3 gibt für halbzahlige Gewichte die Phase ∓i, etwa die Länge mit k = 3/2); Autorentscheidung 2 (reelle Wirkung R als Hauptlinie, K parallel).

## Befunde
1. **Wirkung unter R2:** S = (a − b)·S_EC + (a − i·b)·S_Weyl + (a + b)·S_Potential, also Re S = (a − b)S_EC + a·S_Weyl + (a + b)S_V und Im S = −b·S_Weyl (sympy).
2. **Reelle Lesart R:** Nur Re S zählt. Die Fermionen gehen mit a ein, ihr T-Bild trägt nichts bei (es steht ganz im Imaginärteil). Unter R2 ist das Bild der Fermionen in der reellen Lesart unsichtbar.
3. **Komplexe Lesart K:** Auch Im S = −b·S_Weyl muss stationär sein. Die Variation nach dem Koframe verlangt dann, dass der Energie-Impuls-Tensor der Fermionen verschwindet, die Variation nach der Verbindung, dass ihre Spindichte (für Weyl-Fermionen der Strom j) verschwindet. Das ist der Befund aus k170 in neuer Form: Unter R2 und K gäbe es keine Fermionen (für b > 0).
4. **Quantenmechanisch:** Das Gewicht e^{i(a − ib)S} ist eine teilweise Wick-Drehung um θ = arctan(b/a): bei Materie-Gewichten θ = arctan(β_sym²) = 16,8°, bei Photon-Gewichten 45°. e^{bS} ist für Fermionen nicht beschränkt, die Theorie wäre nicht unitär. Nur als Lesart vermerkt: Der Companion nennt die Wick-Drehung als Teilungsmechanismus (T11).
5. **Warum R2 für Spinoren nicht eindeutig ist:** g ↦ −g ist für Tensoren wohldefiniert, für Spinoren nicht: Die Clifford-Algebren der Signaturen (1,3) und (3,1) sind nicht isomorph (Cl(1,3) ≅ M₂(ℍ), Cl(3,1) ≅ M₄(ℝ); Vorwissen, Standard). Das Vierbein e ↦ i·e ist eine Wahl, keine Folge. Die Phase −i in H83 hängt an dieser Wahl.
6. **Was F3 erlaubt:** F3 gibt für ein Gewicht ½ die Phase ∓i (wie r22.2 für halbzahlige Gewichte). R2 entspricht also der Weyl-Kinetik mit Gewicht ½, H79 und r81 dem Gewicht 1.

## Folge
- Mit Gewicht ½ (Phase −i) sind die Fermionen entweder ohne sichtbares T-Bild (R) oder es gibt keine (K). Mit Gewicht 1 (Phase −1, H79) bleibt alles wie in r84: isotrop, stabil, Fermionen und Skalare mit Kinetik a − b.
- Die Spannung aus H83 ist damit eine Frage nach dem F3-Gewicht der Spinor-Kinetik, nicht nach der Gravitation.

## Entscheidung für den Autor
Welches Gewicht hat die Weyl-Kinetik unter F3: 1 (wie r81, H79; Fermionen mit sichtbarem T-Bild) oder ½ (wie R2; dann ist das Bild der Fermionen unsichtbar oder verbietet sie)? Vorschlag: bei 1 bleiben, weil R2 für Spinoren nicht eindeutig ist (Befund 5) und Gewicht ½ die Fermionen entweder vom T-Anteil entkoppelt oder auslöscht.
