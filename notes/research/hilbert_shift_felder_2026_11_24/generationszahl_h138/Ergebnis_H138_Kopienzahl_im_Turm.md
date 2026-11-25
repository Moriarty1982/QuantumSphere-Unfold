# Ergebnis H138: Drei Kopien je Verdopplung sind erzwungen (Im z³ = 0), aber die Kopienzahl wächst im Turm, und unabhängige Träger sind nie oktonionisch

**25.11.2026. Vorab-Notiz `Vorab_Notiz_H138_Kopienzahl_im_Turm.md` (Commit 31732b4, vor der Rechnung; HS(4) nicht blind, HS(5), HS(6) blind).
Skripte `k321_kopienzahl.py` (`k321_out.txt` für n = 4, 5; `k321_out_n6.txt` für n = 6), `k321b_gegenprobe.wl` (`k321b_out.txt`, Wolfram exakt
für n = 4, 5), `k321c_n6_nachkontrolle.py` (`k321c_out.txt`, nachträglich). Status: H138a widerlegt, H138b widerlegt (nach der vorab
definierten Zählung; in der engeren Lesart „nur oktonionische Kopien“ trüge b, siehe unten).**

Werkzeuge: Python (numpy, scipy) für die Suche (least squares, 400 / 2000 / 600 Zufallsstarts für n = 4 / 5 / 6), Hesse-Matrix, Alternativität,
Orthogonalitäts-Cliquen (Bron–Kerbosch); Wolfram Language exakt (Reduce, Solve über ℝ, Gröbner-Basis) für n = 4 und 5. Für n = 6 brach der
Wolfram-Aufruf nach 60 s ab (Grenze des MCP-Werkzeugs); dort nur Python. Qiskit nicht eingesetzt (keine Schaltung, kein Messablauf).

## Kontrollen
| Kontrolle | Messwert | Schranke | |
|---|---|---|---|
| dim Der(𝕆), blockweise G₂ als Derivation von A₄, A₅, A₆ | 14; Defekt 5·10⁻¹⁴, 6·10⁻¹⁴, ≤ 10⁻¹³ | < 10⁻¹¹ | erfüllt |
| n = 4: N₄ = 3 (0°, 60°, 120°), r₄ = 2, o₄ = 1 | 3, 2, 1; Wolfram exakt gleich | vorab | erfüllt |
| Abschlussdefekt der Lösungen | ≤ 4·10⁻¹⁵ | < 10⁻¹¹ | erfüllt |
| flache Richtungen | keine (kleinster Hesse-Eigenwert ≥ 42) | > 10⁻⁶ | erfüllt |

## Ergebnis
| Stufe | N_n (alle abgeschlossenen O_v) | davon oktonionisch | r_n | o_n (alle) | o_n (nur oktonionisch) |
|---|---|---|---|---|---|
| HS(4), 𝕊 | **3** (exakt) | 3 | 2 | 1 | 1 |
| HS(5) | **15** (exakt, Python und Wolfram) | **9 = 3 × 3** | 4 | 2 | 1 |
| HS(6) | ≥ 207 (Suche nicht gesättigt: 197 nach 500, 207 nach 600 Starts) | ≥ 79 | 8 | ≥ 5 | 1 |

| Teil | Messwert | Kriterium | Entscheidung |
|---|---|---|---|
| H138a | N₅ = 15, N₆ ≥ 207 | N₅ = 9, N₆ = 27 | **widerlegt** |
| H138b | o₅ = 2, o₆ ≥ 5 | o ≤ 3 | **widerlegt** (an n = 6) |

## Was die Rechnung zeigt
1. **Warum genau drei Kopien in den Sedenionen (exakt, k321b).** Die Abschlussbedingung für O_v mit v = (t₁, t₂) ist
   t₂(3t₁² − t₂²) = 0, also **Im((t₁ + i t₂)³) = 0**. Das ist eine kubische Gleichung auf dem Kreis der Kopienrichtungen; sie hat genau drei
   Lösungsgeraden (0°, 60°, 120°). Eine vierte G₂-stabile Oktonion-Kopie gibt es in 𝕊 nicht. Die Dreizähligkeit kommt aus der Konjugation im
   Verdopplungsprodukt (aus z̄ und z wird z̄² ∝ z, also z³ reell). **Status: gezeigt**, unter der Setzung „Kopie = unitale, G₂-stabile,
   achtdimensionale Unteralgebra“.
2. **Die drei sind nicht unabhängig.** Sie spannen nur zwei Richtungen auf (r₄ = 2), keine zwei sind orthogonal. Das ist dieselbe lineare
   Abhängigkeit wie bei K28 und Gillard–Gresnigt (Rang 6 statt 9): drei Etiketten, zwei unabhängige Träger.
3. **Höhere Stufen: drei je Verdopplung.** Auf HS(5) sind die 9 oktonionischen Kopien genau die Produkte v = a ⊗ b mit a, b aus den drei
   Sedenion-Richtungen (nachgeprüft: 9 von 9). Jede Verdopplung ab 𝕊 bringt also wieder eine Dreierwahl. Auf HS(6) sind alle 27 Produkte
   a ⊗ b ⊗ c dabei, es gibt aber mindestens 52 weitere oktonionische Kopien. Die Kopienzahl ist also keine Konstante des Turms; die „3“ ist die
   Zahl **einer** Verdopplung über 𝕆.
4. **Unabhängige Träger sind nie oktonionisch.** Auf keiner Stufe gibt es zwei orthogonale oktonionische Kopien (o = 1 bei n = 4, 5, 6).
   Orthogonale Mengen (2 bei HS(5), mindestens 5 bei HS(6)) bestehen nur aus nicht alternativen Algebren, und deren Imaginärteile sind
   Nullteiler (k322c, k321c; siehe H139).

## Lesart
- **Antwort auf die Frage des Autors:** Ja, die Sedenionen erklären die Zahl 3, aber in einem engen Sinn. Innerhalb einer Verdopplung (𝕆 → 𝕊)
  gibt es genau drei Oktonion-Kopien, weil die Abschlussbedingung kubisch ist. „3 statt 4“ ist dort **erzwungen**. Dass diese drei Kopien
  drei *Generationen* sind, ist **nicht gezeigt** (k255: keine gemeinsamen Ladungen; hier: nur zwei unabhängige Richtungen). Als
  Generationszahl bleibt „3“ eine Eingabe, die der Turm mit genau einer Verdopplung über 𝕆 nahelegt.
- **„Bis 4“:** Eine vierte Kopie ist weder in 𝕊 möglich noch als unabhängiger normierter Träger auf HS(5), HS(6). Weitere orthogonale
  Anordnungen gibt es nur als nicht alternative Nullteiler-Familien (H139). Das spricht gegen eine vierte Generation desselben Typs, verbietet
  sie aber nicht physikalisch.
- **Gesetzt:** G₂-Stabilität und gemeinsame Eins der Kopien. Farbstabile (nur su(3)) Unteralgebren wären mehr (H130: B_±) und sind hier für
  n ≥ 5 nicht gezählt. HS(6) ist nicht vollständig gezählt.
- Vorzeichen nicht berührt (offen bis zur Feldgleichung). OP3, OP4 offen; kein Guard berührt.
- **Mögliche nächste Frage (nur mit neuer Vorab-Notiz):** Gibt die Bedingung Im z³ = 0 zusammen mit der Feldgleichung eine Auswahl unter den
  drei Kopien (eine echte Vorzugsrichtung), oder bleibt S₃ ungebrochen?
