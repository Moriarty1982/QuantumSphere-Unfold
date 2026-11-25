# Ergebnis H139: Was keiner der drei Kopien zugeordnet ist, ist genau ein Nullteiler; die Überschuss-Anordnungen auf HS(5) sind ganze Nullteiler-Familien

**25.11.2026. Vorab-Notiz `Vorab_Notiz_H139_Nullteiler_jenseits_drei_Kopien.md` (Commit c41040c, vor der Rechnung; teilweise nicht blind,
nachträglich motiviert). Skripte `k322_nullteiler_kopien.py` (`k322_out.txt`), `k322b_gegenprobe.wl` (`k322b_out.txt`, Wolfram exakt),
`k322c_nachkontrolle.py` (`k322c_out.txt`, nachträglich). Status: H139a nach Wortlaut widerlegt (Gegenstück bestätigt), H139b bestätigt,
H139c bestätigt (nicht blind).**

Anlass: Vermutung des Autors (25.11.2026): Mehr als drei Generationen ließen sich nur noch durch Nullteiler oder Familien von Nullteilern darstellen.
Werkzeuge: Python (numpy, scipy) für Stichproben und Minimierung; Wolfram Language exakt für die 84 Basis-Nullteiler und die Determinante von L_x
entlang einer Familie. Qiskit nicht eingesetzt (keine Schaltung).

## Kontrollen
| Kontrolle | Messwert | Schranke | |
|---|---|---|---|
| (e₁ + e₁₀)(e₄ − e₁₅) = 0 | 0,0 | < 10⁻¹⁰ | erfüllt |
| Basis-Diagonalen e_i ± e_j als Nullteiler | 84 (Python und Wolfram) | Literatur 84 | erfüllt |

## Ergebnis
| Teil | Messwert | Kriterium | Entscheidung |
|---|---|---|---|
| H139a, Hauptteil (innerer Nullteiler in den 6 nicht alternativen O_v) | kleinster Singulärwert von L_x auf O_v: 1,00 in allen 6 | < 10⁻¹⁰ | **widerlegt** |
| H139a, Gegenstück (keine Nullteiler von A₅ in den 9 oktonionischen) | min 1,00 | > 10⁻⁶ | bestätigt |
| H139b (Nullteiler von 𝕊 haben flaches Profil) | 84 Basis + 500 aus G₂-Bahn und Kernen: Abweichung ≤ 6·10⁻¹⁵, Singulett-Anteil ≤ 6·10⁻¹⁵ | < 10⁻¹⁰ | **bestätigt** |
| H139c (flaches Profil ⇒ Nullteiler; sonst nicht) | flach: smin ≤ 3·10⁻¹⁶; nicht flach: smin ≥ 5,7·10⁻³ | < 10⁻¹⁰ / > 10⁻⁶ | **bestätigt** (nicht blind) |

**Nachträglich (k322, k322c, nicht vorab festgelegt):** Die 6 nicht alternativen O_v auf HS(5) enthalten zwar keinen Nullteiler *untereinander*,
aber **jedes rein imaginäre Element** von ihnen ist ein Nullteiler von ganz A₅ (smin ≤ 5·10⁻¹⁷ in 200 von 200 Stichproben, Kern jeweils
zwölfdimensional). Ihr ganzer siebendimensionaler Imaginärteil ist also eine Nullteiler-Familie, die nach außen leckt. Die 9 oktonionischen
Kopien enthalten keinen einzigen Nullteiler.
Auf HS(6) (k321c, aus den gerundeten Richtungen von k321) gilt dasselbe: imaginäre Elemente der 128 nicht alternativen Kopien haben smin ≤ 10⁻⁶
(68 % exakt unter 10⁻¹⁰; der Rest liegt an der Rundung von v auf sechs Stellen), die der 79 oktonionischen mindestens 0,37. Die größte orthogonale
Menge (5) besteht nur aus nicht alternativen Kopien.

## Warum es trägt
- **Exakt (k322b):** Für x = c·e₁ + s·e₁₀ ist det L_x = (c − s)⁴(c + s)⁴(c² + s²)⁴. Null genau bei c² = s², also wenn x in den beiden
  Kopienblöcken gleich schwer ist. Für das parallele Paar x = c·e₁ + s·e₉ (Rang 1, eine einzige Kopienrichtung) ist det L_x = (c² + s²)⁸, nie null.
- In der Kopien-Sprache (A₄ = ℝ² ⊕ 7 ⊗ ℝ²) ist ein Element ein 7 × 2-Block M = [a b]. **Nullteiler sind genau die Elemente mit a ⊥ b und
  |a| = |b|**, also mit gleichem Gewicht ½ in jeder Kopienrichtung v, auch in jeder der drei Kopien (k322: Gewicht 0,5 / 0,5 / 0,5). Sie
  gehören keiner Kopie an und keiner Richtung dazwischen. Das ist die Form, die Moreno beschreibt (Literatur), hier in Kopien übersetzt.
- Rang 1 (M = a vᵀ, ein Element einer einzigen Richtung) ist nie Nullteiler (k255 Punkt 7 bestätigt). Der Abstand zum Nullteiler wächst
  stetig mit der Unwucht des Profils (k322: d = 0,01 → smin 0,014; d = 0,5 → smin 1).

## Lesart
- **Marcs Vermutung trifft in folgender Form zu:** Auf HS(4) gibt es genau drei Kopien (H138). Ein Zustand, der „zwischen“ ihnen liegt und
  keiner zugeordnet ist, ist ab der Gleichverteilung ein Nullteiler. Auf HS(5) sind die Anordnungen, die über die 3 × 3 oktonionischen Kopien
  hinausgehen, abgeschlossene, aber nicht alternative Algebren, deren Imaginärteil vollständig aus Nullteilern besteht: **Familien von
  Nullteilern**, wie vermutet.
- **Wo der Wortlaut scheitert:** Innerhalb dieser Überschuss-Algebren gibt es keine Nullteiler. Sie sind nach innen „dicht“, nach außen
  (gegen den Rest von A₅) lecken sie. Das passt zum Leckregister des Atlas (r27.2), nicht zu einem inneren Zerfall.
- **Was nicht folgt:** dass Nullteiler eine vierte Generation darstellen oder physikalisch verbieten. Gezeigt ist nur: Normierte (oktonionische)
  Träger gibt es genau 3 je Verdopplung; alles darüber hinaus ist nullteilerbehaftet. Vorzeichen offen bis zur Feldgleichung. OP3, OP4 offen,
  kein Guard berührt.
- **Mögliche nächste Frage (nur mit neuer Vorab-Notiz):** Bilden die 6 Überschuss-Algebren auf HS(5) zusammen mit den Box-Kites eine
  Struktur, die eine vierte „Leck-Generation“ als Familie beschreibt, und welche Masse- oder Kopplungsform hätte sie?
