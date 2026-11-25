# Ergebnis H144: Die Rest-Generation trägt keinen eigenen Sektor; unter der Sektorregel sieht sie aus wie eine Kopien-Generation

**25.11.2026. Vorab-Notiz `Vorab_Notiz_H144_Rest_als_Sektoren.md` (Commit 54682ea; a und b nicht blind). Skripte `k327_rest_sektoren.py`
(`k327_out.txt`), `k327b_gegenprobe.wl` (`k327b_out.txt`, Wolfram exakt). Status: H144a bestätigt, H144b bestätigt, **H144c widerlegt**,
H144d formal bestätigt, aber das Kriterium war trivial (nachträglich erkannt, siehe unten).**

Anlass: Autor: „was wäre, wenn diese Generation jetzt quasi die Generationen für die anderen Sektoren hält?“ Setzung: Der Faktor ℂ von ℂ⊗A₅ ist
der C-Faktor der Frames (wie r51), x = E + iB. Sektorgröße in zwei Lesarten: N = Σ x_a² über alle Koordinaten, s = Σ_{a≥1} x_a² (nur
Imaginärteil, T3 wörtlich), über die Träger summiert. Geprüft: alle Auswahlen von drei, vier und fünf Kopien auf HS(5), transportierte
Orientierung. Werkzeuge: Python (numpy); Wolfram exakt für die Leptonwerte; Qiskit nicht eingesetzt.

## Ergebnis
| Teil | Messwert | Kriterium | Entscheidung |
|---|---|---|---|
| H144a | z ↦ z̄ bildet W auf sich ab (max ‖P_W − P_{W̄}‖ 7·10⁻¹⁵), Spektrum q ↦ 1 − q in allen Klassen; kein W-Zustand liegt auf ≤ 2 Trägern | vorab, nicht blind | **bestätigt** |
| H144b | alle Eigenräume mit q ≠ ½ in W unter N total lichtartig (Takagi ≤ 6·10⁻¹⁵), in Kopie und Rest gleich | vorab, nicht blind | **bestätigt** |
| H144c | Rest-Leptonen (q = 0, 1): **\|s\| = ½**, genau wie die Leptonen einer einzelnen Kopie (Wolfram exakt: N = 0, s/\|x\|² = ½); Quarks s = 0 in beiden | Vorhersage \|s\| < 10⁻⁶ | **widerlegt** |
| H144d | Takagi-Werte von N auf K ⊖ W alle = 1 (> 10⁻⁶) | vorab | formal **bestätigt**, aber trivial |

**Übertragung geprüft (Regel des Autors):** Kopien und Rest werden in denselben Koordinaten mit derselben Ladung Q_v verglichen, also im
Materie-Frame der Kopien. In den Tachyon-Frame (z ↦ iz) übertragen wird s ↦ −s, |s| bleibt; im Zeitumkehrbild (z ↦ z̄) s ↦ s̄, |s| bleibt.
Das Urteil c hängt also nicht am Frame. Es hängt an der Setzung „ℂ = C-Faktor“ und der Wahl der Sektorgröße; in beiden Lesarten (N, s) haben
Rest und Kopie dieselbe Signatur.

**Zu H144d (nachträglich):** K ⊖ W ist unter komplexer Konjugation abgeschlossen (K ist reell, W nach a auch). Für jeden solchen Raum sind alle
Takagi-Werte 1. Das Kriterium konnte also gar nicht scheitern. Aussagekräftig ist die Zustandsebene (k327, Spalte „je Zustand“):
- leckende Zustände mit gestauchter Ladung ≠ ½ (¼, ¾, (5 ∓ √10)/10, 1/10, 9/10, (10 ∓ √10)/20): N = 0 und |s| = ½, also **dieselbe Signatur
  wie Leptonen**;
- leckende Singuletts mit ½: N ≠ 0 (0,19 bis 1,0), s = 0 (nur beim Sedenion-Tripel ist auch s ≠ 0).
Die Signatur folgt also der Ladung, nicht der Frage „stabil oder leckend“. Die Lesart „Leck = Sektorwechsel“ wird nicht gestützt.

## Lesart
- **Antwort:** Unter der Sektorregel trägt die Rest-Generation keinen eigenen Sektor. Ihre Zustände haben genau die Signatur einer
  Kopien-Generation: Quarks lichtartig (s = 0), Leptonen |s| = ½. Auch die Frame-Abbildungen verbinden Kopien und Rest nicht: Sie wirken
  innerhalb jedes Trägers, und der Rest liegt immer über mindestens drei Träger verteilt.
- **Warum:** Aus der Antisymmetrie von L_u und R_u folgt N(x, y) = 0 für Ladungseigenzustände, außer q + q′ = 1. Die Sektorgröße ist damit
  durch die Ladung festgelegt und trägt keine zusätzliche Information über „welcher Sektor“.
- **Was sich ergibt (Nebenbefund):** Die Zeitumkehr z ↦ z̄ bildet die Rest-Generation auf sich ab und spiegelt die Ladungen q ↦ 1 − q. Das ist
  derselbe Schritt wie der globale Vorzeichenwechsel der Orientierung (1 − Q_v = Q_{−v}). Das offene globale Vorzeichen ist also genau die Wahl
  der Zeitrichtung (bzw. Teilchen/Antiteilchen); welche gilt, soll weiter die Feldgleichung entscheiden. Materie und Tachyon trennt die
  Sektorgröße auf einem einzelnen Zustand nur bis auf die Dualitätsphase; „Licht oder nicht“ ist die einzige invariante Aussage.
- **Gesetzt bzw. offen:** ℂ als C-Faktor, die Wahl N oder s, Summe über die Träger, k85-Ladung, Orientierung. Eine andere Zuordnung der Sektoren
  (etwa über den Kopienindex wie in der Betrachter-Notiz vom 16.11., HS(8)) ist hier nicht geprüft. T1 bleibt Vermutung; OP3, OP4 offen; kein
  Guard berührt.
- Vergeben: H144, k327. Nächste frei: H145, k328.
