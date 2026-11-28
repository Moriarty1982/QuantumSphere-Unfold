# Ergebnis H222 (k435): Das Vorzeichen der kubischen Spektralinvariante wählt den Zweig in beiden Lepton-Sektoren — ohne Skala

**Datum:** 2026-11-28. **Vorab:** `Vorab_H222_Zweigwahl_skalenfrei.md` (Commit 2300774, vor der Rechnung). **Urteil: trägt** — mit dem vorab genannten Vorbehalt:
das **Vorzeichen** des kubischen Terms bleibt gesetzt; die Skala ist durch ein Vorzeichen ersetzt, nicht hergeleitet.
**Werkzeuge:** Python (`k435_test_h222.py` → `k435_out.txt`), Wolfram unabhängig (`k435b_gegenprobe.wl` → `k435b_out.txt`, Teil d und die Wahl im Grenzfall symbolisch);
alle gemeinsamen Zahlen stimmen auf die angegebenen Stellen überein. Qiskit nicht einschlägig. a nicht blind, b und c teilweise nicht blind (H221, H213d), d und e blind.

## Frage
Nach H221 verschiebt eine gemeinsame Drehung χ → χ + φ beide Sektoren exakt gleich, lässt aber in jedem Sektor zwei gleich tiefe Minima (verschiedene Spektren:
δ und δ + π/3 unterscheiden sich im Vorzeichen der Wurzeln). Bisher wählte nur der Term sechster Ordnung mit Skala. Gibt es eine skalenfreie Regel, die in beiden
Sektoren den Zweig der Daten wählt?

## Ergebnis
| Teil | Messwert | Kriterium | Entscheidung |
|---|---|---|---|
| a (nicht blind) | Im-Sektor, Zweige π/12 − φ und π/4 + φ, cos 3δ = ±cos(π/4 − 3φ) (bei φ = x_lepton ±0,786); Regel wählt **π/12 − φ = δ*** für φ = 0,01…0,06 | ja für alle φ | **erfüllt** |
| b (teilw. nicht blind) | Re-Sektor, Zweige π/6 ∓ φ, cos 3δ = ±sin 3φ (bei φ = x_lepton ±0,118); Regel wählt **π/6 − φ** (x_ν > 0) für φ = 0,01…0,06 | ja für alle φ | **erfüllt** |
| c (teilw. nicht blind) | gewählter Zweig π/6 − x_lepton: R_NO = 0,03084 (+1,8σ); verworfener π/6 + x_lepton: R_NO = 0,05332 (**+50,9σ**), IO weit außerhalb; für keinen Versatz x′ ∈ [0; 0,1] liegt π/6 + x′ innerhalb 2σ | > 3σ | **ausgeschlossen** |
| d (blind, symbolisch) | ∏(1 + a cos(δ + 2πk/3)) = (4 − 3a² + a³ cos 3δ)/4 exakt; cos 3δ invariant unter δ → −δ und δ → δ + 2π/3, wechselt Vorzeichen unter δ → δ + π/3; unter n = 1…6 sind nur cos 3δ und cos 6δ invariant | alle exakt | **erfüllt** |
| e (blind) | q = −ε: globales Minimum eindeutig auf dem gewählten Zweig; Abstand 4,6·10⁻³ / 4,6·10⁻⁵ / 4,6·10⁻⁷ (Im) und 7,4·10⁻³ / 7,5·10⁻⁵ / 7,5·10⁻⁷ (Re) bei ε = 10⁻²/10⁻⁴/10⁻⁶; q = +10⁻⁴ wählt jeweils den anderen Zweig. Symbolisch: V₁ − V₂ = q·(cos 3δ₁ − cos 3δ₂) mit 2 sin(3φ + π/4) (Im) und 2 sin 3φ (Re) | eindeutig, < 10⁻⁵ bei 10⁻⁶ | **erfüllt** |

**Gesamturteil nach Vorab: trägt** (a, b, d, e erfüllt, c schließt den verworfenen Zweig mit 51σ aus).

## Lesart
- **Die Zweigwahl braucht keine Skala, nur ein Vorzeichen.** Auf den Spektralklassen (δ bis auf Konjugation und Umbenennung) ist cos 3δ die niedrigste nicht konstante
  Invariante, und sie ist bis auf Konstanten die Determinante der Wurzelmatrix: det Y/μ³ = −½ + cos 3δ/√2 bei a = √2. Die Regel „größeres cos 3δ“ (gleichwertig: größere
  Determinante) wählt in **beiden** Sektoren mit **demselben** Vorzeichen den Zweig der Daten. Das ist der Grenzfall q → 0⁻ des Terms sechster Ordnung: der Betrag, also
  die Skala Λ, fällt heraus; die Verschiebung durch q geht linear gegen null, die Wahl bleibt.
- **Damit ist das Bild ohne Skala geschlossen, bis auf zwei Zahlen-freie Setzungen:** Versatz = gemeinsamer Drehwinkel φ (H221), Zweig = Vorzeichen der kubischen
  Invariante (H222). Es bleiben gesetzt: das Vorzeichen (q < 0) und der Wert φ = x selbst.
- **Die Daten prüfen die Regel.** Der verworfene Re-Zweig ist kein harmloser Doppelgänger: Er gäbe R = 0,053 statt 0,030 (51σ). Ohne die Regel wäre der neutrale Zweig
  eine freie Wahl, die die Daten zufällig richtig getroffen hätten.

## Hergeleitet, gesetzt, nachträglich
- **Hergeleitet/gerechnet:** det Y als Funktion von cos 3δ (symbolisch), D₃-Invarianz und Vorzeichenwechsel unter δ → δ + π/3, Zweigpaare beider Sektoren nach der Drehung,
  Wahl im Grenzfall (symbolisch), Abstand des verworfenen Zweigs von den Daten.
- **Gesetzt:** das Vorzeichen des kubischen Terms (q < 0, gleich in beiden Sektoren); die gemeinsame Drehung und ihr Wert φ (H221); Zirkulantensektor, Baumniveau, K = ⅔, H99;
  α′_ν = −1 (H168).
- **Nachträglich bemerkt:** (i) Die Wahl im Re-Sektor hängt am Vorzeichen von φ (2 sin 3φ): Bei φ < 0 wählte die Regel im Re-Sektor π/6 − |φ|, im Im-Sektor aber
  π/12 + |φ|, also entgegengesetzte Versätze. Gleich gerichtete Versätze, wie die Daten sie zeigen, verlangen φ > 0; das ist mit der Regel verträglich, wird von ihr aber nicht
  erzwungen. (ii) Im Im-Sektor fällt die Regel mit „alle Wurzeln positiv“ zusammen (det Y > 0); im Re-Sektor haben beide Zweige eine negative Wurzel, Positivität allein
  entschiede dort nicht. Die Determinantenregel ist die schärfere.

## Grenzen
Zirkulantensektor, Baumniveau; nicht zirkulante Richtungen nicht gerechnet. Ein Potentialterm ∝ det Y/μ³ wäre nicht polynomial; geprüft ist eine Auswahlregel bzw. der
Grenzfall q → 0⁻, keine Feldgleichung, die das Vorzeichen liefert. Nach den Vorgaben des Autors soll ein offenes Vorzeichen aus der finalen Feldgleichung folgen; das ist
hier nicht geleistet. Kein Guard berührt; OP3/OP4/OP5 offen.

## Dateien
- `Vorab_H222_Zweigwahl_skalenfrei.md` — Vorab-Notiz (vor der Rechnung committet).
- `k435_test_h222.py`, `k435_out.txt` — Python-Rechnung und Ausgabe.
- `k435b_gegenprobe.wl`, `k435b_out.txt` — Wolfram-Gegenprobe und Ausgabe (Warnungen und Rückgabewert im Kopf der Ausgabe).

Vergeben: H222, k435. Nächste frei: H223, k436 (vor Vergabe gegen `main` prüfen).
