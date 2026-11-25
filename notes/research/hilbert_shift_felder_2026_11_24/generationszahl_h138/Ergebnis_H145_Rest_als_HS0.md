# Ergebnis H145: Der Rest ist kein eigenes HS(0), aber er ist auf HS(0) gebaut: Rest-Generation = reelle Koeffizientenlinie ⊗ eine ganze Oktonion-Kopie

**25.11.2026. Vorab-Notiz `Vorab_Notiz_H145_Rest_als_HS0.md` (Commit 6e5a6b5; großteils nicht blind). Skripte `k328_rest_hs0.py` (`k328_out.txt`),
`k328b_transportiert.py` (`k328b_out.txt`, Auswertung nach Orientierung getrennt, teils nachträglich), `k328c_gegenprobe.wl` (`k328c_out.txt`,
Wolfram exakt). Status: H145a für K bestätigt, für W nur bei transportierter Orientierung (bei gemischten Vorzeichen in der Vorab-Form
widerlegt, berichtigte Form nachträglich bestätigt); H145b bestätigt (transportierte Orientierung); **H145c nach Wortlaut widerlegt** (bei
transportierter Orientierung exakt erfüllt); H145d bestätigt.**

Anlass: Autor: „hört sich blöd an, aber prüfe mal, ob die Restgeneration evtl. wieder ein HS(0) sein könnte.“ Werkzeuge: Python (numpy) für alle
3360 Auswahl-Orientierungs-Fälle mit 3, 4, 5 Kopien; Wolfram exakt für eine H142-Auswahl. Qiskit nicht eingesetzt.

## Ergebnis
| Teil | Messwert | Kriterium | Entscheidung |
|---|---|---|---|
| H145a, K | K = (D⁰ ⊗ e₀) ⊕ (R ⊗ Im𝕆) in allen 3360 Fällen (Projektor-Abstand ≤ 2·10⁻¹⁴; dim K = (m − 1) + 7·dim R immer; Wolfram exakt); ι_k exakt Algebren-Isomorphismus | < 10⁻¹⁰ | **bestätigt** |
| H145a, W | transportierte Orientierung: W = (R⁰ ⊗ {e₀, e₇}) ⊕ (R ⊗ Farbe₆) exakt (≤ 4·10⁻¹⁵); gemischte Vorzeichen: Abstand bis 0,5 | alle Orientierungen | **nach Wortlaut widerlegt**; berichtigt (nachträglich): Farbteil (R ∩ s∘R) ⊗ Farbe₆, dann ≤ 4·10⁻¹⁵ in allen Fällen |
| H145b | transportierte Orientierung: Q(c ⊗ y) = c ⊗ Q₈y (≤ 7·10⁻¹⁶), c reell, Ladung und Farbe wirken nicht auf c | vorab | **bestätigt** |
| H145c | Σ c_k³ = 0 bei transportierter Orientierung in allen 54 Generationsauswahlen (Wolfram exakt); bei gemischten Vorzeichen (5 Kopien) bis 0,265 | alle Orientierungen < 10⁻¹² | **nach Wortlaut widerlegt** |
| H145d | Produkt zweier Rest-Zustände liegt zu 71 % bis 100 % außerhalb des Rests (H142-Auswahlen: 100 %, Wolfram exakt) | > 10⁻⁶ | **bestätigt** |

**Warum die Vorzeichen stören (nachträglich):** Bei Vorzeichen s_k = −1 ist der Transport der Kopie y ↦ (y₀, −y_im), also die Konjugation. Die
ist ein Anti-Isomorphismus (sie dreht die Reihenfolge der Multiplikation um). Eine solche Kopie trägt dann das gespiegelte Oktonion, und die
einfache Form c ⊗ y gilt nur, wenn alle Kopien gleich orientiert sind. Das ist dieselbe offene Orientierung wie in H142–H144.

## Lesart
- **Antwort:** Der Rest ist kein HS(0) im Sinn einer eigenen Algebra ℝ: Er ist unter dem Produkt nicht abgeschlossen (das Produkt zweier
  Rest-Zustände landet bei den H142-Auswahlen ganz im sichtbaren Teil), und bei gleich orientierten Kopien trägt die Koeffizientenlinie kein
  eigenes Produkt (Σ c³ = 0).
- **Aber HS(0) steckt zweifach im Rest:**
  1. Die Rest-Generation ist **R⁰ ⊗ ℂ𝕆**: eine ganze Oktonion-Kopie über einer reellen Linie R⁰ mit c = (−1, −1, 1, 1) bzw.
     (−1, −1, 0, 1, 1). Die Linie hat die HS(0)-Merkmale: reell, nur ±c als Wahl, zeitumkehrfest, ohne Ladung und Farbe. Sie ist die
     „Vielfachheit“ der Generation, nicht die Generation selbst.
  2. Der Teil **D⁰ ⊗ e₀** sind die reellen Einheiten der Kopien, also ihr HS(0), die sich gegenseitig aufheben. Die Leptonen des Rests
     (Ladung 0 und 1, aus e₀ ± i e₇) entstehen genau dort, wo diese aufgehobenen HS(0)-Teile mit einer Richtungsrelation zusammenfallen.
     Alle übrigen Anteile von D⁰ ⊗ e₀ lecken (die ½-Singuletts).
- **Fängt der Turm neu an?** Nein: Aus der Linie wächst kein HS(1) usw. Die Koeffizientenräume wachsen mit der Kopienzahl wie 1, 1, 2, 2, 3, 4,
  nicht wie 1, 2, 4, 8 (k326c, bekannt).
- **Masse:** nicht berührt. Zur Aussage des Autors passt nur die Einordnung: Der HS(0)-Anteil des Rests ist ladungsfrei und ohne eigene
  Dynamik; ob „keine Masse auf HS(0)“ hier etwas bedeutet, zeigt die Rechnung nicht.
- **Nebenbefund:** Die Formel K = (D⁰ ⊗ e₀) ⊕ (R ⊗ Im𝕆) erklärt die Regel aus H143a (Rest-Generationen = dim R⁰) und die Zahl der
  leckenden Zustände ((m − 1 − dim R⁰) + (dim R − dim R⁰)) analytisch, bei transportierter Orientierung.
- Gesetzt bzw. offen: Orientierung (gemischte Vorzeichen = gespiegelte Kopien), k85-Ladung. Vorzeichen offen; OP3, OP4 offen; kein Guard berührt.
- Vergeben: H145, k328. Nächste frei: H146, k329.
