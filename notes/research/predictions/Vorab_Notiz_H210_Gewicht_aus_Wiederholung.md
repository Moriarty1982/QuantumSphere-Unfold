# Vorab-Notiz H210: Folgt das Paargewicht der Bänder aus der Zahl der Wiederholungen, und liefert es feste Winkel?

**Stand:** 2026-11-27, vor der Rechnung festgelegt und vor dem ersten Lauf committet. Auftrag des Autors vom 27.11.2026, 15:07 UTC („ja bitte“ zum
Vorschlag, in der Lesart „gleich lang, wiederholt“ zu testen, ob das Gewicht aus der Wiederholung selbst folgt). Skripte **k423** (Python: numpy,
scipy) und **k423b** (Wolfram: Paritätsregel symbolisch, eine Energie unabhängig integriert). Werkzeugwahl: Python für die Minimierung über Lagen
und Phasen, Wolfram für die exakte Regel und eine unabhängige Quadratur; Qiskit nicht einschlägig. Kein HDL/MMA-Vergleich. Kein Guard berührt.

## Vorwissen geprüft
- **H209/k421:** Überlapp zweier Streifen = a·b/sin θ je Kreuzung, daher Gesetz 1/sin; Paargewicht offen, es trägt alle Winkel, auch den Oktant.
- **k422, Teil 3:** Lesart „gleich lang, aber wiederholt“ mit Gewicht = Windungszahl m = 16/d **gesetzt** gibt H192 gespiegelt (R ⟂ ℂ 89,54°).
- **k399:** gleiche Bänder: 3 → 90°, 4 → 70,53° = arccos ⅓, 5 → 59,1°/74,0° (gesetzesabhängig).
- **Fragenliste F18** (Autor: „8 Bit, jedes trägt doppelt so viel“; Rotor mit 8 Stellungen): nicht gerechnet; H210 berührt sie (Muster mit
  Periode 2ⁿ), beantwortet sie aber nicht.
- **H191:** Schleife über Bänder verschiedener Spins gibt kein Casimir-Profil (anderes Modell, kein Bezug zur Lage auf der Sphäre).
- **Suchrichtung:** Rückwärts gefragt, wodurch sich „wiederholt“ von „dichter belegt“ unterscheidet: nur dadurch, dass das Muster eine **Phase**
  hat. Ein Muster ohne Phase (reine Belegung) führt auf die zwei schon gerechneten Fälle zurück (H210a). Neu ist allein das Muster mit Phase
  (H210b, H210c); deshalb wird genau das gerechnet.

## Modell
Alle fünf Bänder sind Großkreis-Streifen gleicher Breite (Querprofil Gauß mit Breite σ). Das Band der Stufe mit Dimension d trägt ein Muster, das
sich m = 16/d-mal wiederholt: m = 16, 8, 4, 2, 1 für R, ℂ, ℍ, 𝕆, 𝕊. Energie wie in H209: Kreuzterm ∫ φ_i φ_j dA über die Sphäre.

- **Belegung (Muster mit Mittelwert, ohne Phase):** φ_i = konstant auf dem Band.
- **Welle (Muster ohne Mittelwert, mit Phase):** φ_i = A_i cos(m_i s − α_i), s = Bogenlänge auf dem Band, α_i frei.

## Aussagen und Kriterien
- **H210a (nicht blind, Einordnung):** Für die Belegung gibt die Wiederholung genau zwei parameterfreie Gewichte: Inhalt je Wiederholung erhalten
  → w_ij = m_i m_j (das ist k422 Teil 3, H192 gespiegelt); Inhalt je Band erhalten → w_ij = 1 (das ist k399, fünf gleiche Bänder). Beide sind
  gerechnet, neue Winkel entstehen nicht. Bestätigt, wenn k423 beide Winkellisten reproduziert.
- **H210b (nicht blind, Herleitung):** Für die Welle gilt an den zwei Gegenpunkten einer Kreuzung φ_i(−x) = (−1)^{m_i} φ_i(x). Der Kreuzterm
  zweier Bänder verschwindet deshalb exakt, wenn m_i + m_j ungerade ist. Mit m = 16, 8, 4, 2, 1 ist nur 𝕊 ungerade: **𝕊 koppelt an kein anderes
  Band**, seine Lage ist frei, ein Oktant 𝕆 ⟂ 𝕊 folgt nicht. Bestätigt, wenn die numerischen Kreuzterme mit 𝕊 für Zufallslagen unter 10⁻⁸ der
  übrigen liegen und Wolfram die Regel symbolisch gibt.
- **H210c (Test, blind):** Für die vier geraden Bänder R, ℂ, ℍ, 𝕆 wird die Wellenenergie über Lagen und Phasen minimiert (A_i = 1; σ = 2° und
  σ = 5°; mindestens 200 Starts). **Bestätigt**, wenn alle sechs Winkel für beide Breiten bei 70,53° ± 1° liegen (arccos ⅓, die Lage von vier
  gleichen Bändern; cos = ⅓ ist die Zahl des Mischungsstrangs). **Teilweise**, wenn die Winkel zwischen σ = 2° und σ = 5° um weniger als 3°
  wandern, aber nicht alle bei 70,53° liegen (dann gibt die Wiederholung feste Winkel, nur andere). **Widerlegt**, wenn ein Winkel um mehr als 3°
  mit σ wandert oder Bänder zusammenfallen (Winkel < 5°): Dann legt die Wiederholung keinen Winkel fest, sondern die freie Bandbreite.
- **H210d (Bericht):** dasselbe mit A_i = m_i (Inhalt je Wiederholung); Treffer auf der Zielliste aus H192 (90°, 70,53°, 63,43°, 60°, 57,569°,
  54,74°, 45°) nur als nachträglich; im Bereich 45° bis 90° decken die Fenster etwa 29 % ab.

## Vorab offengelegt (Erwartung)
H210a und H210b stehen analytisch fest. Bei H210c kenne ich das Ergebnis nicht. Meine Erwartung ist **widerlegt**: Eine Welle ohne Mittelwert
kann den Kreuzterm durch Wahl der Phase negativ machen, die Bänder ziehen sich dann an, bis die Überlappraute länger wird als die Wellenlänge und
sich das Muster wegmittelt. Der Winkel wäre dann etwa durch m·σ bestimmt und wanderte mit der Breite. Träte „bestätigt“ ein, wäre das ein echter
Hinweis, weil dann cos θ = ⅓ ohne Setzung eines Gewichts herauskäme.

## Bilanz der Setzungen (vor der Rechnung)
| Größe | Status |
|---|---|
| alle Bänder Großkreise, Wiederholung m = 16/d | gesetzt (Lesart des Autors, Empfehlung vom 27.11.) |
| Gesetz: Kreuzterm über den Überlapp | hergeleitet in H209 |
| Muster als reine Welle cos(m s − α), gleiche Breite, Gauß-Profil | gesetzt |
| Phasen α_i, Lagen | frei, werden minimiert |
| Bandbreite σ | frei; genau daran hängt das Kriterium von H210c |
| Entkopplung von 𝕊 | herzuleiten (H210b) |

## Grenzen
Starre Streifen, statisches Muster, kein Bezug zu Messdaten. OP1 und OP4 bleiben offen, was immer herauskommt. Vergeben: H210, k423.
Nächste frei: H211, k424.
