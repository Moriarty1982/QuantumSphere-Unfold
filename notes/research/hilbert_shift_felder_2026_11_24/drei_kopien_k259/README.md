# Vollständigkeit zu H130 und die drei Oktonion-Kopien auf den drei Plätzen (Erkundungen k259, k260, nicht blind, 25.11.2026)

**Ergebnis in einem Satz:** Die Suche aus H130 ist jetzt exakt vollständig (genau fünf farbstabile Unteralgebren, davon drei oktonionisch), und setzt man die
drei Oktonion-Kopien auf die drei Plätze von H₃(𝕊), dann bleibt von Familien-SO(3) × S₃ genau die Würfelgruppe **S₄**, mit der Ladung **A₄**.

Auftrag: Autor („ja und weiter“, 25.11.2026) nach H130 (#299). **Nicht blind:** Die fünf Lösungen waren aus H130 bekannt; dass die Vertauschung der Plätze zusammen
mit der S₃ der Kopien eine endliche Gruppe der Ordnung 24 gibt, stand vor der Rechnung fest (je Würfeldrehung genau ein passendes S₃-Element). Gerechnet wurden die
Bestätigung, der Abschluss und die Wirkung der Ladung. Skripte **k259** (Wolfram), **k260** (Python).

Werkzeuge: Wolfram Language exakt (Reduce über ℝ) für die Vollständigkeit; Python (numpy) mit den Modulen aus k283 und k258 für die Gruppen. Qiskit nicht eingesetzt.

## Vorwissen geprüft
H130 (drei Kopien, B_±), H128 (Der(H₃(𝕊)) = g₂ ⊕ su(3), Form K), k254 (S₃, drei Kopien), k275 und r60 (Ladung bricht SO(3) zu A₄; ungerade Elemente konjugieren; „TBM braucht S₄“),
H39/r55 (A₄-Untergruppen als Lesarten), k256 (K∘S₀ hält TM1).

## Ergebnisse
1. **Vollständigkeit (k259, k260 F).** Der Kommutant von su(3)_c auf dem Triplett-Teil ist achtdimensional (M₂(ℂ)); die farbstabilen sechsdimensionalen Teilräume sind
   also genau die Punkte von ℂP¹, wie in H130 parametrisiert. Die Abschlussbedingung ist ein Polynomsystem (14 Gleichungen in Karte 1, 6 in Karte 2). Reduce über ℝ gibt
   als vollständige Lösungsmenge genau O_0, O_120, O_240, B_+ und B_− (jeweils mit u und −u). Damit ist H130 nicht mehr auf Zufallsstarts angewiesen.
2. **S₃ explizit (k260 A).** Die Drehung um 120° in allen Ebenen (e_i, e_{i+8}) ist ein Automorphismus (Rest 9·10⁻¹⁵, bei 90° nicht), ebenso (a, b) ↦ (a, −b). Sie
   permutieren die drei Kopien; die Ladungsrichtungen sind u_k = e₇, −½e₇ ± (√3/2)e₁₅.
3. **Kopie k auf Platz k (k260 B, C).** Der Teilraum W (Diagonale reell, Eintrag k in Kopie k, 27 Dimensionen) ist **keine Unteralgebra** (Abschlussdefekt 0,31, Leck in
   alle Sedenion-Richtungen). Seine Symmetrie in (24 Würfeldrehungen) × S₃ hat **24 Elemente** mit den Ordnungen 1, 2, 3, 4 in den Anzahlen 1, 9, 8, 6, also **S₄**. Reine
   Würfeldrehungen sind davon nur 4 (V₄); jede Platzvertauschung braucht die passende Vertauschung der Kopien. Stetig bleibt nur g₂ (14 von 22 Derivationen).
4. **Mit der Ladung (k260 D).** Mit L_u, R_u je Platz in der Richtung der jeweiligen Kopie vertauschen 12 der 24 Elemente (Ordnungen 1, 2, 3 in den Anzahlen 1, 3, 8), also
   **A₄**. Die anderen 12 erhalten die Ladung bis auf Vorzeichen und den Tausch L ↔ R.
5. **Massenform (k260 E).** K ist auf dem farbneutralen Feld in W weiter 60 für Spin 2 und 54 für Spin 1, ohne Mischterm. In zweiter Ordnung ist die Lage der Kopien
   also nicht sichtbar. Die kubische Spur Tr Z³ unterscheidet sie (0,377 gegen −0,206 bei gleicher Mischung).

## Bewertung
- **Eine endliche Familiengruppe entsteht hier ohne die Ladung.** In H128 konnte der Turm SO(3) nicht brechen, weil reelle Drehungen immer Automorphismen sind. Verteilt man
  aber die drei Kopien, die HS(4) selbst mitbringt, auf die drei Plätze, dann bleibt von SO(3) × S₃ nur die Würfelgruppe S₄, diagonal eingebettet. Die Ladung bricht sie zu A₄.
  Die 12 ungeraden Elemente wirken auf die Ladung wie eine Konjugation. Das passt zur Vermutung aus k275, S₄ könne als verallgemeinerte CP-Symmetrie zurückkehren. Gerechnet
  ist hier nur die Gruppe, keine Mischungsmatrix.
- **Die Zuordnung „Kopie k auf Platz k“ ist eine Setzung**, und W ist kein Algebra-Träger. Wer alle drei Plätze in dieselbe Kopie legt (wie H128), behält SO(3) und bekommt
  A₄ erst durch die Ladung (k275). Welche der beiden Lesarten gilt, entscheidet diese Rechnung nicht.
- Vorzeichen und Feldgleichung sind nicht berührt (anderer Faden). OP3 und OP4 bleiben offen, kein Guard ist berührt.

## Mögliche nächste Schritte
- Blinder Test: Gibt die Restgruppe S₄ mit der Ladung als verallgemeinerter CP eine Mischungsspalte (TM1 oder TBM), ohne weitere Wahl? Das braucht eine Vorab-Notiz.
- Prüfen, ob es einen natürlichen Grund für „Kopie k auf Platz k“ gibt, etwa eine abgeschlossene Erweiterung von W.

## Dateien
`k259_vollstaendig_exakt.wl` (`k259_out.txt`, Wolfram), `k260_drei_kopien_plaetze.py` (`k260_out.txt`). Aufruf aus diesem Ordner; k260 liest `../kollaps_h128/` und `../ladungsrichtung_h130/`.
