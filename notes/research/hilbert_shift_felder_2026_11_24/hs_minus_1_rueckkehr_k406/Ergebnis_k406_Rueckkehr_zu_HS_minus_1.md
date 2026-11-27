# k406: Kehrt der Turm beim Hochgehen zu einer Stufe vom Typ HS(−1) zurück? (Erkundung, nicht blind, 27.11.2026)

**Status:** Erkundung ohne Vorab-Notiz, kein Test, keine Runde. **Anlass:** Frage des Autors vom 27.11.2026: Früher wurde geprüft, ob der Turm
beim Hochgehen zyklisch wieder durchlaufen wird, mit HS(0) als Rückkehr (k254: Periode 4). Dasselbe jetzt mit HS(−1) als Rückkehr.
Vergeben: **k406** (k406, k406b, k406c).

**Ergebnis in einem Satz:** Ja. Der Typ von HS(−1) (zwei Hälften, die nur ein Vorzeichen unterscheidet; k405) kehrt beim Hochgehen wieder, zum
ersten Mal schon bei HS(3), den Oktonionen: Dort ist das Vorzeichen der Unterschied zwischen Links- und Rechtsmultiplikation. Die nächste
Rückkehr liegt gemessen bei HS(11), nicht bei HS(7). Dabei zeigt sich, dass die Periode 4 aus k254 ab HS(6) nur eine Obergrenze beschreibt:
Für die Einheiten des Turms selbst geht die Uhr ab den Oktonionen jede Stufe genau eine Stunde weiter, die Periode ist 8.

**Werkzeuge:** Python (numpy) mit exakter Suche (Bron–Kerbosch mit Pivot) über alle Einheiten bis HS(11), Dimension 2048 (`k406_rueckkehr.py`,
`k406_out.txt`); eine zweite, unabhängig geschriebene exakte Suche für n = 4 bis 8 (`k406c_zweite_suche.py`, `k406c_out.txt`); Wolfram Language
exakt für n = 1 bis 5 und die Vorzeichen bei HS(2), HS(3) (`k406b_gegenprobe.wl`, `k406b_out.txt`). Wolfram reicht wegen des Zeitlimits nur bis
n = 5; die neuen Zahlen ab n = 6 stützen sich auf die zwei Python-Suchen. Qiskit nicht eingesetzt (keine Schaltung). Kein HDL/MMA-Vergleich.

## Vorwissen geprüft

- k254 (`../hs4/README.md`): größte Menge verträglicher Kreisachsen 1, 3, 7, 8, 9 für n = 1 … 5 gerechnet, „fortgesetzt 11, 15 | 16, 17, 19, 23“ nach
  der Radon–Hurwitz-Formel; daraus „HS(4)–HS(7) wiederholen HS(0)–HS(3)“, Periode 4. Die Grenze stand dort schon: Die Zählung über Einheiten ist
  eine untere Schranke, Radon–Hurwitz die Obergrenze. n = 6 und n = 7 waren nicht gerechnet.
- k405 (`../hs_minus_1_k405/`): HS(−1) als Typ ℝ ⊕ ℝ (eine zentrale Einheit j mit j² = +1), Stunde −1 = 7 der Clifford-Uhr.
- k253 (dim Der, Regel ψ̇ = uωψ), r59 (Händigkeitsserie), H8 (Konjugation als CP). Keine frühere Rechnung zur Rückkehr auf HS(−1).

## 1 Was „Rückkehr“ heißt

Wie in k254 ist nicht dieselbe Algebra gemeint (die Dimension wächst immer), sondern derselbe Typ auf der Clifford-Uhr: Die a verträglichen
Kreisachsen einer Stufe erzeugen eine Algebra, deren Typ nur von a mod 8 abhängt (Stunden 0 bis 7: ℝ, ℂ, ℍ, ℍ⊕ℍ, ℍ, ℂ, ℝ, ℝ⊕ℝ, jeweils mal
Matrizen). HS(0) ist Stunde 0, HS(−1) ist Stunde 7. Das Kennzeichen der Stunde 7: Das Produkt ω aller Achsen vertauscht mit allen, ω² = +1,
und die erzeugte Algebra ist reell.

## 2 Messung im Turm (Uhr B)

Größte Menge paarweise antikommutierender Linksmultiplikationen L_(e_i), exakt gesucht:

| n | Dimension | Achsen a (gemessen) | Obergrenze (Radon–Hurwitz) | Stunde a mod 8 | Typ | ω |
|---|---|---|---|---|---|---|
| 0 | 1 | 0 | 0 | 0 | ℝ | – |
| 1 | 2 | 1 | 1 | 1 | ℂ | ω² = −1 |
| 2 | 4 | 3 | 3 | 3 | ℍ⊕ℍ | −1 (links), +1 (rechts) |
| 3 | 8 | 7 | 7 | **7** | **ℝ⊕ℝ** | **−1 (links), +1 (rechts)** |
| 4 | 16 | 8 | 8 | 0 | ℝ | 8 mal +1, 8 mal −1; antikommutiert mit den Achsen |
| 5 | 32 | 9 | 9 | 1 | ℂ | ω² = −1 |
| 6 | 64 | **10** | 11 | 2 | ℍ | ω² = −1 |
| 7 | 128 | **11** | 15 | 3 | ℍ⊕ℍ | 64 mal +1, 64 mal −1 |
| 8 | 256 | 12 | 16 | 4 | ℍ | 128 mal +1, 128 mal −1 |
| 9 | 512 | 13 | 17 | 5 | ℂ | ω² = −1 |
| 10 | 1024 | 14 | 19 | 6 | ℝ | ω² = −1 |
| 11 | 2048 | 15 | 23 | **7** | **ℝ⊕ℝ** | **1024 mal +1, 1024 mal −1** |

Befunde:

1. **Erste Rückkehr bei HS(3).** Die sieben Linksmultiplikationen der Oktonionen erzeugen alle reellen 8×8-Matrizen (Rang 64 von 64), ihr Produkt
   ist der Skalar −1; für die Rechtsmultiplikationen ist es +1 (Python und Wolfram). Die zwei Hälften von ℝ ⊕ ℝ sind also Links- und
   Rechtsmultiplikation. HS(3) ist im Typ ein HS(−1), und das Vorzeichen ist die Händigkeit des Produkts.
2. **Ab HS(3) eine Stunde je Stufe.** Für n ≥ 3 ist a = n + 4 (geprüft bis n = 11; die zweite Suche bestätigt n = 4 … 8). Die gefundenen Mengen haben
   ein einfaches Muster: Jede Verdopplung bringt genau eine neue verträgliche Achse (bei n = 6 etwa die Einheiten 32, 48, 56 bis 63).
3. **Zweite Rückkehr bei HS(11), nicht HS(7).** Bei HS(7) stehen 11 Achsen (Stunde 3), nicht 15. Stunde 7 wird erst bei HS(11) wieder erreicht,
   danach nach der Regel a = n + 4 bei HS(19). Entsprechend kehrt der Typ von HS(0) bei HS(4) und dann erst bei HS(12) wieder.
4. **Die Rückkehr ist nicht gleich.** Bei HS(3) ist ω ein Skalar: Die Stufe sieht nur eine Hälfte (links −1), die andere liegt in der
   Rechtsmultiplikation. Bei HS(11) hat ω im selben Raum 1024 mal +1 und 1024 mal −1: Beide Hälften sind zugleich da. Das ist die Spiegelstufe
   aus k405 mit einem wirklichen j (j² = +1, zentral), nicht nur ein Vorzeichen.
5. **Der Schritt HS(−1) → HS(0) entspricht HS(3) → HS(4).** Aus dem Skalar ±1 (zwei getrennte Hälften) wird bei den Sedenionen ein Operator mit
   8 mal +1 und 8 mal −1, der mit den acht Achsen antikommutiert: Die zwei Hälften liegen dann in einem Raum und werden von den Achsen ineinander
   überführt. An dieser Stelle fand k254 die Brüche (Nullteiler, Verlust der Alternativität).

## 3 Berichtigung zu k254 (dort unverändert, hier vermerkt)

k254 hat n = 1 … 5 gerechnet und die Folge mit der Radon–Hurwitz-Formel fortgesetzt (11, 15 für n = 6, 7). Die Rechnung hier zeigt: Diese Zahlen
werden von den Einheiten des Turms nicht erreicht (10 und 11). Die Aussage „HS(4)–HS(7) wiederholen HS(0)–HS(3), Periode 4“ gilt für die
Obergrenze, also für beliebige verträgliche Drehungen im Raum der Dimension 2ⁿ, nicht für die Linksmultiplikationen der Turm-Einheiten. Für diese
springt die Uhr bis HS(3) (0, 1, 3, 7) und tickt danach einzeln: Periode 8. Auch „HS(6) hat 11 = 1 + 3 + 7 Achsen“ gilt nur für die Obergrenze.
Ob Linksmultiplikationen mit allgemeinen Richtungen (nicht Einheiten) mehr als n + 4 erreichen, ist nicht gerechnet.

## 4 Zum Vergleich: das Clifford-Geschwister (Uhr A)

Cl(0, n) hat dieselbe Dimension 2ⁿ und dieselbe Beschriftung wie HS(n), ist aber assoziativ. Dort ist das Zentrum ℝ ⊕ ℝ bei n = 3 und n = 7; der
reelle Fall (Stunde 7) liegt bei n = 7, 15, …, Periode 8. Bis n = 2 sind Turm und Geschwister gleich (ℝ, ℂ, ℍ). Bei n = 3 trennen sie sich: Das
Geschwister ist ℍ ⊕ ℍ, der Turm nimmt die Oktonionen und springt damit vier Stunden vor. Danach laufen beide im gleichen Takt, der Turm mit vier
Stunden Vorsprung.

## 5 Rückwärts fortgesetzt (Formel, nicht Messung)

Setzt man die Obergrenze rückwärts fort (a(n − 4) = a(n) − 8), erhält man a = −1, −5, −7, −8 für n = −1 … −4. Eine negative Achsenzahl liest sich
als Achsen mit Quadrat +1; das gibt für n = −1 wieder ℝ ⊕ ℝ (wie k405). Mit der gemessenen Regel a = n + 4 gäbe es dagegen kein natürliches
Rückwärts unter n = 3, weil die Regel dort bricht (a = 3 statt 6 bei n = 2). Die Fortsetzung nach unten ist also Lesart.

## Was hergeleitet ist und was Lesart

| Aussage | Status |
|---|---|
| HS(3): L₁…L₇ = −1, R₁…R₇ = +1, erzeugte Algebra M₈(ℝ) | exakt (Python, Wolfram) |
| Achsenzahl der Einheiten 0, 1, 3, 7, 8, 9, 10, 11, 12, 13, 14, 15 für n = 0 … 11 | exakte Suche; n ≤ 5 Wolfram, n = 4 … 8 zweite Suche, n = 9 … 11 nur eine Suche |
| a = n + 4 für alle n ≥ 3 | Muster bis n = 11, nicht bewiesen |
| Typ je Stunde (Clifford-Klassifikation) | Standard |
| „HS(3) ist ein HS(−1) eine Runde höher“, Vorzeichen = Händigkeit | Lesart |
| Zahl für β_sym, Winkel, Massen | keine |

## Grenzen

- Nicht blind, kein Entscheidungskriterium.
- Gezählt sind nur Linksmultiplikationen mit Einheiten e_i. Für allgemeine Richtungen liegt die wahre Zahl zwischen n + 4 und der Obergrenze.
- „Rückkehr“ ist Gleichheit des Typs, nicht der Stufe. Ab HS(4) ist das Produkt nicht mehr alternativ; die Achsen sind dort Operatoren auf dem
  Träger, keine Drehungen durch Multiplikation im strengen Sinn.
- Die Verbindung zur Händigkeit im Modell (r59, H8) ist nicht gerechnet.
- OP1, OP3 offen; kein Guard berührt.

## Möglicher nächster Schritt

Prüfen, ob allgemeine Richtungen in HS(6) elf verträgliche Achsen erreichen (dann gälte die Periode 4 doch für den Turm) oder ob n + 4 die wahre
Grenze ist. Das ist eine endliche, aber größere Suche; als Erkundung möglich.
