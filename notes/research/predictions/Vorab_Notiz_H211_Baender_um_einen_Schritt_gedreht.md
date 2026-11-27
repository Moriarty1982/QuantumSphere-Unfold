# Vorab-Notiz H211: Jedes Band ist gegenüber dem Vorgänger um „+1“ weitergedreht — legt das Winkel fest (arccos ⅓, Oktant)?

**Stand:** 2026-11-27, vor dem Rechenlauf festgelegt und committet. Auftrag des Autors vom 27.11.2026, 17:52 UTC („was ist, wenn jedes Band, das
ja jeweils einen HS repräsentiert, zum Vorgänger jeweils +1 weitergedreht ist?“). Skripte **k424** (Python: numpy, scipy) und **k424b** (Wolfram:
Winkelformel und Sonderfälle symbolisch). Werkzeugwahl: Wolfram für die exakte Formel, Python für die Minimierung und die Stichproben; Qiskit nicht
einschlägig. Kein HDL/MMA-Vergleich. Kein Guard berührt.

## Vorwissen geprüft
- **H192, H209, H210 (27.11.):** freie Lagen der Bänder; die offene Größe wanderte Gesetz → Gewicht → Bandbreite. Bilanz in der Ergebnis-Notiz H210:
  Die gemeinsame Sphäre ist gesetzt; Weggabelung beim Autor. H211 ist eine neue Eingabe des Autors an genau dieser Stelle: Die Lagen sind nicht
  mehr frei, sondern durch **eine** feste Drehung von Band zu Band verbunden.
- **k399:** drei gleiche Bänder 90° (Koordinatenebenen), vier 70,53° = arccos ⅓.
- **k407, Fragenliste F18:** Der Typ einer Stufe auf der Clifford-Uhr hat 8 Stellungen; Aussage des Autors „Rotoren haben nur 8 Positionen“.
  Daraus die Lesart des Schritts unten. F18 selbst (legt die Einrastung feine Winkel fest?) ist nicht gerechnet.
- **r70:** Materie-Frame beim Polwinkel 57,569°; magischer Winkel 54,736° (cos² = ⅓).
- **Suchrichtung:** Rückwärts gefragt, was eine feste Drehung überhaupt festlegen kann. Eine Drehung hat einen Winkel (den Schritt) und eine Achse.
  Der Schritt ist durch „+1 von 8“ benannt; die Neigung der Achse gegen das erste Band bleibt als **eine** freie Zahl. Die Frage ist also, ob
  etwas diese Neigung festlegt. Das wird direkt gerechnet.

## Lesart (vorab benannt)
**Hauptlesart L1:** Die Normale des Bands k entsteht aus der des Bands k−1 durch dieselbe Drehung D: n_k = Dᵏ n_0, k = 0 … 4 für R, ℂ, ℍ, 𝕆, 𝕊.
Der Schritt ist **eine Rotorstellung der 8er-Uhr, 360°/8 = 45°**. Die Drehachse steht unter dem Winkel χ zur Normalen n_0; χ ist nicht benannt
und damit frei. Für zwei Bänder mit Stufenabstand s gilt dann cos θ_s = cos²χ + sin²χ · cos(s · 45°).

**Alternativen (nur Stichprobe):** Schritt 22,5° (ein Band hat keine Richtung, also 8 Stellungen auf 180°), 72° (fünf Bänder schließen), 60°, 90°
(ein Viertel, „neue imaginäre Einheit“), 120°; acht Bänder statt fünf (volle Uhr). **Nicht gerechnet:** „+1“ als Versatz des Musters längs des
Bands (Phase): Ohne gemeinsamen Bezugspunkt der Bänder ist eine Phase je Band nicht definiert, und H210 hat gezeigt, dass im Wellenbild die
Bandbreite entscheidet.

## Aussagen und Kriterien
- **H211a (nicht blind, Formel):** Mit Schritt 45° gibt χ = 54,736° (magischer Winkel, cos²χ = ⅓) für Stufenabstand 2 **und** 4 genau arccos ⅓
  (R–ℍ, ℂ–𝕆, ℍ–𝕊 und R–𝕊); χ = 45° gibt für Abstand 4 den Oktant (R ⟂ 𝕊) und für Abstand 2 genau 60°; χ = 90° legt alle Bänder durch zwei
  gemeinsame Punkte, mit R ⟂ ℍ, ℂ ⟂ 𝕆 und 𝕊 auf R. Bestätigt, wenn Wolfram die Formel und diese Fälle exakt gibt.
- **H211b (Test, nicht blind):** Legt die Abstoßung der Bänder (Gesetz 1/sin aus H209, gleiches Gewicht) die Neigung fest, und zwar auf 54,736° ± 1°
  (dann arccos ⅓) oder 45° ± 1° (dann Oktant)? **Bestätigt** bei 54,736° ± 1°, **teilweise** bei 45° ± 1°, sonst **widerlegt**. *Nicht blind:*
  Beim Aufstellen dieser Notiz habe ich die Energie an vier Stellen von Hand überschlagen (χ = 54,7°: 13,0; 62°: 12,69; 65°: 12,69; 70°: 12,86).
  Das Minimum liegt danach bei etwa 63° bis 64°, also bei keinem der beiden Werte. Ich erwarte **widerlegt**; der Lauf bestimmt den genauen Wert.
- **H211c (Bericht, Robustheit):** dasselbe Minimum für Gewicht d_i d_j, min(d_i, d_j), √(d_min/d_max) und Gesetz 1/sin². Wandert χ* um mehr als 3°,
  hängt auch diese Antwort an der Setzung.
- **H211d (Stichprobe, blind):** χ* und die Winkel für die anderen Schritte und für acht Bänder. Treffer auf der Zielliste (90°, 70,53°, 63,43°,
  60°, 57,569°, 54,74°, 45°; ± 1°) zählen nur als nachträglich. Die Fenster decken zwischen 30° und 90° etwa 22 % ab.

## Gesetzt bleibt
Gemeinsame S², starre Großkreise, **eine** Drehung für alle Schritte (gleiche Achse, gleicher Winkel), Schritt = 45°, Reihenfolge R, ℂ, ℍ, 𝕆, 𝕊.
Frei: die Neigung χ. Für H211b zusätzlich gesetzt: gleiches Gewicht.

## Bilanz der Setzungen (vor der Rechnung)
| Größe | Status |
|---|---|
| eine feste Drehung von Band zu Band | gesetzt (Eingabe des Autors) |
| Schritt 45° | gesetzt (Lesart „+1 von 8 Rotorstellungen“); Alternativen als Stichprobe |
| Neigung χ der Achse | **frei**; ob etwas sie festlegt, ist die Frage |
| arccos ⅓ bei χ = 54,736°, Oktant bei χ = 45° | folgt aus der Formel (H211a) |
| Gesetz 1/sin | hergeleitet (H209); Gewicht gesetzt |

## Grenzen
Kein Bezug zu Messdaten; OP1 und OP4 bleiben offen. Vergeben: H211, k424. Nächste frei: H212, k425.
