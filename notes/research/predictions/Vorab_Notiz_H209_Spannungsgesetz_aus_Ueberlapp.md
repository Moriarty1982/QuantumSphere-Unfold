# Vorab-Notiz H209: Spannungsgesetz der Bänder aus dem Überlapp statt gesetzt — kommt 1/sin heraus, welches Gewicht folgt aus der Schachtelung des Turms, und trägt der Oktant dann noch?

**Stand:** 2026-11-27, vor der Rechnung festgelegt und vor dem ersten Lauf committet. Auftrag des Autors vom 27.11.2026, 14:31 UTC („dann
versuche dich mal am Spannungsgesetz“), nach den Grafiken k420. Skripte **k421** (Python: numpy, scipy) und **k421b** (Wolfram: Überlappfläche
symbolisch, unabhängige Minimierung). Werkzeugwahl: Wolfram für die exakte Überlappfläche und als zweite Minimierung, Python für Vielstart-Minimierung
und Flächenkontrolle auf der Sphäre; Qiskit nicht einschlägig (keine Schaltung). Kein HDL/MMA-Vergleich (kein endlicher Guard-Ablauf). Kein Guard berührt.

## Vorwissen geprüft
- **k399 (27.11.):** gleiche Bänder → platonische Winkel, gesetzesunabhängig; mit Gewicht nach Dimension hängen die Winkel von Gewicht und Gesetz ab.
  Dort ausdrücklich: „Ohne ein hergeleitetes Gewicht und Abstoßungsgesetz liefert das Bild keine Zahl.“ Urbild eines Breitenkreises unter der
  Hopf-Abbildung: Volumen ~ sin^{n−1} θ; 𝕊 hat keine Faserung.
- **H192/k400 (27.11.):** Gewicht = Dimension, Gesetz 1/sin **gesetzt** (Begründung dort nur als Satz: „Kreuzungsdichte geht wie 1/sin“). Ergebnis
  teilweise: 𝕆–𝕊 = 89,54° robust (87,9° bis 89,5° über vier Setzungen), ℂ–ℍ = 49,40° läuft (49° bis 59°).
- **k420 (27.11.):** Auf der runden Sphäre sind alle Großkreise schon maximal lang; Verformung nur mit gesetztem Zug; Stärke und Vorzeichen frei.
- **H191 (27.11.):** Bänder verschiedener Spins erzeugen kein Casimir-Gewichtsprofil (widerlegt). Die Zählregel (r67) ist Postulat; eine Zuordnung
  HS-Stufe → Spin j gibt es im Repo nicht. Ein Casimir-Gewicht je Band wird deshalb hier **nicht** als Herleitung geführt.
- **H193 (27.11.):** getrennte Felder je HS-Stufe als Massenquelle widerlegt. H209 fragt nicht nach Massen, sondern nach dem Gesetz zwischen Bändern.
- **Zurückgestellte Ideen I1 bis I6:** Auslöser geprüft; I1 (String als Brücke, Stringspannung setzt Skala) berührt das Thema „Spannung“, ihr Auslöser
  (gescheiterter Ansatz mit fehlender Skala) trifft erst zu, wenn H209 keine Skala liefert; dann dem Autor nennen.
- **Suchrichtung:** Rückwärts gefragt, was ein Gesetz leisten müsste: (i) eine Funktion des Kreuzungswinkels, (ii) ein Gewicht je Paar ohne freien
  Parameter, (iii) ein Vorzeichen für die Wirkung auf die Fläche. Der Überlapp zweier Streifen liefert alle drei Kandidaten in einem Schritt; deshalb
  wird er vorwärts gerechnet.

## Ansatz
Ein Band ist ein Streifen der Breite a um einen Großkreis und trägt ein Feld φ_i mit Werten in der Algebra A_i seiner Stufe (Dimension d_i =
1, 2, 4, 8, 16), gleichmäßig über den Streifen. Die Energiedichte ist quadratisch im Gesamtfeld, also |Σφ_i|². Der Kreuzterm zweier Bänder lebt
nur auf ihrer Überlappfläche.

**Herzuleiten (H209a):** Zwei Streifen der Breiten a_i, a_j, die sich unter dem Winkel θ kreuzen, überlappen sich in zwei Rauten der Fläche
a_i a_j / sin θ (schmale Streifen). Damit wäre **1/sin** (und nicht 1/sin²) das Gesetz, sobald Überlapp Energie kostet.

**Gewicht aus der Schachtelung (H209b):** Die Algebren sind nach Cayley–Dickson geschachtelt, ℝ ⊂ ℂ ⊂ ℍ ⊂ 𝕆 ⊂ 𝕊. Das Skalarprodukt ⟨φ_i, φ_j⟩ sieht
nur die gemeinsamen d_min = min(d_i, d_j) Komponenten. Zwei Normierungen ohne freien Parameter:
- **N1 (eine Einheit je Komponente):** w_ij = min(d_i, d_j).
- **N2 (eine Einheit je Band, gleichmäßig auf die Komponenten verteilt):** w_ij = √(d_min/d_max).
- Zum Vergleich **N0** (H192): w_ij = d_i d_j (Bänder als skalare Ladungen der Größe d_i, ohne Schachtelung).

**Vorzeichen für die Fläche (H209c):** Ist der Inhalt je Band erhalten (Feld mal Bandlänge fest), so geht die Kreuzenergie wie 1/(L_i L_j). Dann
will jedes Band möglichst lang sein. Das wäre die Regel des Autors („maximal gedehnt“) als Folge und nicht als Definition, mit Zug **nach außen**
und Stärke je Band proportional zu seiner gesamten Kreuzenergie E_i = Σ_j w_ij / sin θ_ij.

## Gesetzt bleibt (auch im besten Fall)
Gemeinsame S² für alle Stufen; Bänder als starre Großkreis-Streifen gleicher Breite; quadratische Energiedichte; Kreuzterm positiv (Felder im
Überlapp gleich ausgerichtet); gleichmäßige Verteilung auf die Komponenten; Erhaltung des Inhalts je Band (für H209c); Elastizität der Fläche
(k420, S2). Hergeleitet werden kann höchstens: die Winkelfunktion, das Paargewicht bis auf die Wahl N1/N2, das Vorzeichen des Zugs.

## Aussagen und Kriterien
- **H209a (nicht blind, Herleitung):** Überlappfläche zweier schmaler Streifen = 2 a_i a_j / sin θ. Bestätigt, wenn Wolfram die ebene Fläche exakt
  gibt und die numerisch auf der Sphäre gemessene Fläche für halbe Breite 2° und θ = 30°, 45°, 60°, 90° auf < 1 % übereinstimmt. Berichtet wird die
  Abweichung bei breiten Streifen und kleinen Winkeln.
- **H209b (Test):** Mit Gesetz 1/sin und Gewicht N1 sowie N2, ohne Parameter, dasselbe Kriterium wie H192b mit denselben vorab benannten Paaren:
  **bestätigt**, wenn 𝕆–𝕊 = 90° ± 1° **und** ℂ–ℍ = 57,569° oder 54,736° (± 1°); **teilweise**, wenn nur 𝕆–𝕊 = 90° ± 1°; **widerlegt**, wenn 𝕆–𝕊
  nicht bei 90° ± 1° liegt. Gewertet wird je Normierung getrennt; N1 und N2 werden beide berichtet, keine wird nachträglich bevorzugt.
- **H209c (Herleitung unter genannter Setzung, kein Test):** Vorzeichen und Stärke des Zugs je Band aus der Kreuzenergie bei erhaltenem Inhalt;
  berichtet werden E_i je Band für N0, N1, N2 und die Lage der größten Beule in der Verformungsrechnung aus k420 mit E_i statt d_i als Zug.
- **H209d (Bericht):** Kommt eine Skala oder einer der Winkel θ, δ, β_sym (über die Zielliste aus H192: 90°, 70,53°, 63,43°, 60°, 57,569°, 54,74°,
  45°) heraus? Als Befund zählen nur die vorab benannten Paare; alle anderen Treffer sind nachträglich und bei zehn Paaren und sieben Zielen ohne
  Aussagekraft (Zufallsquote je Paar etwa 16 %).

## Vorab offengelegt (Erwartung)
H209a erwarte ich bestätigt (elementare Geometrie, deshalb nicht blind). Bei H209b kenne ich das Ergebnis nicht. Meine Erwartung: Unter N2 liegen
alle Gewichte zwischen ¼ und 1, die Lage dürfte nahe an der von fünf gleichen Bändern sein (59,1°/74,0°), und der Oktant 𝕆–𝕊 ginge dann verloren
(**widerlegt**). Unter N1 dominieren die schweren Paare schwächer als bei N0; ob 𝕆–𝕊 bei 90° ± 1° bleibt, ist offen. Träte „widerlegt“ ein, so
hinge der einzige robuste Befund aus H192 (Oktant) an der Setzung „skalare Ladung = Dimension“ und nicht an der Geometrie. Eine Skala erwarte ich
nicht: Die Stärke des Zugs gegen die Elastizität der Fläche bleibt frei.

## Bilanz der Setzungen (vor der Rechnung)
| Größe | Status |
|---|---|
| Winkelfunktion 1/sin | herzuleiten aus dem Überlapp (H209a) |
| Paargewicht | aus der Schachtelung, zwei Normierungen N1, N2 ohne Parameter; die Wahl zwischen ihnen ist offen |
| Kreuzterm positiv, quadratische Energie, gleiche Breite, gemeinsame S² | gesetzt |
| Vorzeichen des Zugs auf die Fläche | herzuleiten unter der Setzung „Inhalt je Band erhalten“ (H209c) |
| Stärke gegen die Elastizität der Fläche | frei |
| vorhergesagte Paare (𝕆–𝕊, ℂ–ℍ), Zielwinkel | wie H192, vorab benannt |

## Grenzen
Starre Großkreise, kein dynamisches Feld, kein Bezug zu Messdaten. OP1 bis OP5 bleiben offen. Vergeben: H209, k421. Nächste frei: H210, k422.
