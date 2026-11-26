# Ladungsachse und Ladungstyp: Test H162 (k360) und Erkundung k361 (26.11.2026)

Anlass: r64.2 (H130 stützt die Ladungsachse e₈, Platzhalter CT-003, nicht). Auftrag des Autors vom 26.11.: alles Offene rechnen.

## H162 (k360, Vorab-Notiz 080d9a9, weitgehend nicht blind)
Ergebnis: `../../predictions/Ergebnis_H162_Ladungsachse_e7_WegA_CP.md`. Kurz: Mit Q_u = P₀(½ − (i/2)L_u)P₀ + ⅔P₃ + ⅓P₃̄ gelten Weg A
(zwei Generationen), die Familien-su(2) aus den Rechtsmultiplikationen und H125 Stufe A für jede Achse u in Im H_n. e₈ ist nur durch
[Q, ψ] = 0 ausgezeichnet, e₇ durch die Fortsetzung der oktonionischen Ladung der Kopie.
Dateien: `k360_test_h162.py`, `k360_out.txt`, `k360b_exakt.wl`, `k360b_out.txt`.

## Erkundung k361 (nicht blind, ohne Kriterium): Ladung mit Rechtsmultiplikation, und welche Seite die Familie trägt
In H162 als „nicht gerechnet“ vermerkt. Dateien: `k361_rechtsladung.py`, `k361_out.txt` (Abschnitt 5 der Ausgabe ist ein Nachtrag aus einem
Einzeiler, der im selben Lauf angehängt wurde).

**Befunde**
1. **Vollständigkeit.** Jede Ladung auf dem farbneutralen Block H_n mit Spektrum {0, 0, 1, 1} und Q̄ = 1 − Q ist ½ − (i/2)A mit einer reellen
   komplexen Struktur A. Auf H_n ist so(4) = {a·L + b·R}, und A² = −1 gilt genau für A = L_u oder A = R_u. Es gibt also zwei Typen, je mit freier
   Achse. Die Notiz `op3_sedenion_charge_2026_11_13.md` nennt den zweiten Typ („oder mit R_e8“), r13.1 führt ihn als „bis auf zwei Vorzeichen“.
2. **Q^R_u erfüllt dieselben Bedingungen** wie Q^L_u: Spektrum 0 (2), ⅓ (6), ⅔ (6), 1 (2), vertauscht mit su(3)_c, Q̄ = 1 − Q.
   Q^R_{e8} vertauscht mit ψ, Q^R_{e7} setzt Q₈ auf der Kopie 𝕆₀ fort (Leck 0), genau wie beim Linkstyp. Kein Kriterium aus H162 trennt die Typen.
3. **Die Familienalgebra sitzt auf der anderen Seite.** Mit Q^R vertauschen auf den Leptonen die Linksmultiplikationen L_x, die
   Rechtsmultiplikationen nicht (Kommutator 2). Auf dem farbigen Teil vertauschen **beide**, L_x und R_x, mit Ladung und Farbe.
4. **Orientierung** (Vorzeichen in [X_e7, X_e8] = ±2X_e15, Bargmann ¼ ± i/4):

   | Block | L_x | R_x |
   |---|---|---|
   | Leptonen (H_n) | +2, ¼ + i/4 | −2, ¼ − i/4 |
   | Quarks (farbig) | −2, ¼ − i/4 | +2, ¼ + i/4 |

   Auf den Quarks gibt es also zwei native Familien-su(2) mit entgegengesetzter Orientierung. Welche auf den Leptonen zulässig ist, legt der Ladungstyp fest.
5. **Folge für H125 Stufe A.**
   - Trägt **eine** native Multiplikation die Familie auf dem ganzen Träger (R_x beim Linkstyp wie in r13.4, L_x beim Rechtstyp), dann sind Leptonen und
     Quarks entgegengesetzt orientiert. Das gilt für beide Ladungstypen und jede Achse.
   - Nimmt man für Leptonen und Quarks verschiedene Seiten (zulässig, weil auf den Quarks beide vertauschen), sind sie gleich orientiert.
     Gerechnet für Q^R mit L auf den Leptonen und R auf den Quarks: 24 + 24 Zuordnungen, det +1 und +1.

**Lesart.** Das relative Vorzeichen aus r59.6 hängt nicht an der Achse (H162) und nicht am Ladungstyp, aber an einer bisher nicht benannten
Setzung: **dieselbe Seite der Multiplikation für beide Sektoren.** Sie ist die naheliegende (r13.4: „eine native Operation“), folgt aber nicht aus
Ladung und Farbe allein. Der Satz in r59.6, Stufe A sei „der erste Punkt der Serie, der kein Vorzeichen setzt“, ist entsprechend einzuschränken.
H125 Stufe B (sin δ_PMNS < 0) hängt damit an S1 und an dieser Setzung; ihr Status „offen, Vorwahrscheinlichkeit ½“ ändert sich nicht.
Kein Guard berührt; OP3 und OP4 offen.

**Nicht gerechnet:** ob eine Wirkung (W1/W2, Yukawa-Konnektoren) die Seite festlegt.
