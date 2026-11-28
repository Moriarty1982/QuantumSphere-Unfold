# Vorab-Notiz H215 (k428): Rückwärtssuche nach Schleifen, die β_sym anziehen

Stand 28.11.2026, vor jeder Rechnung festgeschrieben. Auftrag des Autors (Coprozessor-Plan, letzter Punkt): Stabilitätstest für β_sym,
Λ und die Achsneigung χ gegen Kontrollwerte. Am 27.11.2026 um 23:57 UTC hat der Autor auf der Entscheidungskarte die Option
„Rückwärtssuche mit Vorab-Notiz“ gewählt.

## Frage

Stabil oder instabil ist ein Wert nur gegenüber einer bestimmten Schleife x ↦ f(x), nicht für sich allein. Ein Wert x* ist ein
anziehender Fixpunkt von f, wenn f(x*) = x* und |f′(x*)| < 1 gilt. Für die Rückwärtssuche wird zuerst das Ziel festgelegt. Daraus folgt
die Frage, ob es unter den einfachen Schleifen aus den Operationen des Rahmens welche gibt, die genau dieses Ziel anziehen. Das Ergebnis
wird gegen Kontrollwerte gestellt, damit ein Zufallstreffer nicht als Befund gilt.

**H215:** β_sym ist anziehender Fixpunkt einer kurzen Verkettung von Operationen des Rahmens, und zwar exakt, nicht nur im Datenfenster.
Außerdem häufen sich solche Schleifen bei β_sym stärker als bei Kontrollwerten.

## Ziele und warum nur β_sym getestet wird

- **β_sym** = 0,549405640974529 (30 Stellen aus der Zählregel r67: Σ_{k≥1} 2^(1−γ a_k) = 1 mit a_k = √(k(k+2)/3),
  γ_L = 1,864699764609373, β² = (γ_L − 1)/(γ_L + 1)). Postulat, OP1 offen. Datenfenster aus k358 (2σ): [0,54907; 0,54978].
- **χ:** Nach H211 ist χ frei. Die Kandidaten aus H211 sind algebraisch: magischer Winkel (cos²χ = ⅓), 45° (cos²χ = ½) und die
  Materie-Frame-Neigung (cos χ = 1/γ_L, also wieder β_sym). Algebraische Werte treffen einfache Schleifen ohnehin exakt (½ ist der
  Fixpunkt der HC-Schleife, k394). Eine Rückwärtssuche kann sie daher nicht unterscheiden, und χ hat kein eigenes Ziel. Die einzige
  Schleife für χ ist bisher die Bandenergie (H211b/c), und deren Minimum wandert mit der Setzung. **χ wird nicht getestet.** Es wird nur
  mitgezählt, wie viele Schleifen ⅓ und ½ anziehen (Kontrollen der Art „algebraisch“).
- **Λ:** Λ hat im Rahmen keine eigene Skala (k251, k353). Ohne dimensionslosen Zielwert gibt es nichts, wohin die Suche rückwärts laufen
  könnte. **Λ wird nicht getestet.**

## Vorwissen geprüft

- `op1_herkunft_beta_sym_h165/Sichtung_Herleitungsversuche.md`: 37 Versuche, β_sym herzuleiten, kein einziger trägt. Darunter sind zwei
  Fixpunkt-Schleifen: Nr. 3 Tribonacci γ_L = 1/β(γ_L) mit dem Wert 1,8393, der die Frames mischt, und Nr. 4 Hawking γ ≈ 1/β mit 2,4 %
  Abweichung. Nr. 22 enthält den Nebenwert 2^(1−γ_L) = 0,549161.
- H165 (`Ergebnis_H165_…`) ist widerlegt. k358 legt das 2σ-Fenster fest.
- k394 (`uebersicht_k394/`): Die HC-Schleife b′ = 1 − 2b(1 − b) läuft auf ½ zu, nicht auf β_sym.
- k396 (`beta_erwartungswert_k396/`): 2^(1−γ_L) ≈ β_sym auf 0,045 %, nachträglich gefunden und ungeklärt.
- H164: β_sym als Überlapp, die Boost-Identitäten 2β/(1 + β²) und 1/γ_L = (1 − β²)/(1 + β²).
- k405: Die Schleife L3 ist c ↦ c². H211 behandelt χ, k251 Λ.
- Coprozessor `qtune.sv` (PR #400) misst |f′| am Fixpunkt über d_last/d_prev, aber nur für Polynome vom Grad ≤ 2 in Q2.30.

**Bekannt vor der Rechnung, also nicht blind:** Die Abbildung E (siehe unten) hat bei β_sym den Wert 0,549161. Ihr Fixpunkt liegt deshalb
vermutlich nahe am Fenster. E allein wird darum getrennt berichtet und zählt nicht für das Urteil.

## Schleifenklasse (fest)

Grundoperationen auf [0, 1], jede mit ihrer Fundstelle im Rahmen:

| Zeichen | Abbildung | Herkunft |
|---|---|---|
| H | b ↦ 1 − 2b(1 − b) | HC-Schleife (k394) |
| S | b ↦ b² | Schleife L3 (k405) |
| R | b ↦ √b | Umkehrung von S |
| C | b ↦ 1 − b | Spiegelstufe / Komplement (k405) |
| A | b ↦ 2b/(1 + b²) | Boost-Addition β ⊕ β (H164) |
| W | b ↦ b/(1 + √(1 − b²)) | halbe Rapidität, Umkehrung von A |
| G | b ↦ (1 − b²)/(1 + b²) | Bloch-Länge 1/γ (H164) |
| D | b ↦ 2b√(1 − b²) | Doppelwinkel sin 2θ (Hopf) |
| E | b ↦ 2^(1 − γ(b)), γ(b) = (1 + b²)/(1 − b²) | 1-Bit-Gewicht der Zählregel (r67, k396) |

Schleifen sind alle Wörter der Länge 1 bis 5 über diesen 9 Zeichen, also 66 429 Wörter. Ausgeschlossen werden Wörter, deren Abbildung
auf mehr als 1 % des Gitters mit der Identität übereinstimmt (etwa CC, SR, AW), weil dort jeder Punkt Fixpunkt ist. Fixpunkte werden auf
einem Gitter von 20 001 Punkten in (0, 1) über Vorzeichenwechsel von f(x) − x gesucht und mit Brent verfeinert. Anziehend heißt
|f′(x*)| < 1 − 10⁻⁹.

## Kontrollen und Kriterium

- **Zählgröße N(x₀):** Zahl der Wörter mit einem anziehenden Fixpunkt im Fenster x₀·(1 ± 6,5·10⁻⁴). Das ist dieselbe relative Breite
  wie das k358-Fenster um β_sym.
- **Kontrollen:** 2000 Zufallsziele, gleichverteilt in [0,35; 0,75] (Startwert 215), sowie die benannten Werte ½, ⅓, 1/√3 (die Fläche
  j + ½), 1/√2, 1/γ_L und 2^(1−γ_L).
- **Exakter Treffer:** Für jedes Wort mit Fixpunkt im Fenster wird |f(β_sym) − β_sym| in mpmath mit 30 Stellen berechnet. Exakt heißt
  < 10⁻²⁰.

**Urteil (für Wörter ohne das Einzelwort E):**
- **trägt**, wenn es mindestens einen exakten anziehenden Treffer gibt;
- **trägt teilweise**, wenn es keinen exakten Treffer gibt, N(β_sym) aber über dem 99. Perzentil der Zufallskontrollen liegt;
- **widerlegt**, wenn beides nicht zutrifft. Dann zieht keine einfache Schleife des Rahmens β_sym an, und die Gegend um β_sym ist nicht
  auffälliger als ein beliebiger Wert.

**Erwartung (keine Rechnung):** β_sym ist über eine unendliche Summe festgelegt. Ein exakter Treffer durch endlich viele algebraische
Operationen ist daher unwahrscheinlich, bei Wörtern mit E aber nicht ausgeschlossen. Erwartet wird „widerlegt“.

## Prüfwege

1. Hauptrechnung in Python: `k428_test_h215.py`, Ausgabe `k428_out.txt`.
2. Gegenprobe in Wolfram: `k428b_gegenprobe.wl`, Ausgabe `k428b_out.txt`. Sie berechnet β_sym unabhängig, zählt N für die Wörter der
   Länge ≤ 3 neu (819 Wörter) und prüft die Fixpunkte aller Treffer mit FindRoot.
3. Hardware: Ist ein Treffer ein Polynom vom Grad ≤ 2 mit Koeffizienten im Q2.30-Bereich, läuft er zusätzlich auf `qtune` (Icarus).
   Sonst entfällt dieser Weg, und das wird festgehalten.

Ordner für Rechnung und Ergebnis: `notes/research/hilbert_shift_felder_2026_11_24/stabilitaet_rueckwaerts_h215/`.
