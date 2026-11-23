# Ergebnis H122: Bei OP1 legt das Feld den Ausleserahmen fest, bei OP5 nicht

**23. November 2026. Vorab-Notiz `Vorab_Notiz_H122_Auslese_Extremum.md` (Commit d861db0e). Skript `h122_readout_extremum.wl`, Ausgabe
`h122_readout_extremum.txt`. Teilweise nicht blind (H122a; modeweise H122b/c). Status: H122a bestätigt, H122b und H122c widerlegt; nach dem
vorab festgelegten Kriterium trägt H122 nicht.**

Werkzeug: Wolfram Language (exakt, symbolisch) über den Wolfram-Kern dieser Sitzung; Funktionen der Ausleseseite unverändert aus r46. Qiskit nicht
geeignet, kein HDL-Vergleich (kein endlicher Auswahlablauf). Zwei Läufe brachen mit einem Serverfehler des Konnektors ab und wurden ohne die
Minimierungsteile wiederholt; die Kriterien blieben unverändert.

## Kontrollen
| Kontrolle | Wert | Ergebnis |
|---|---|---|
| Detektorrahmen u·u, n·n, u·n | 1, −1, 0 | erfüllt |
| N im Ruhesystem | ⅔(k₁² + k₂²)² | gleich r46 |
| Reihe entlang der Achse | ⅔a(a − b²k_z²) | gleich r46.3 |
| Monome des Zählers | alle vom Grad 4 in k | isotropes Mittel über Momente zulässig |

## H122a (OP1, nicht blind): bestätigt
Q_F(u) − Q_F(R) = 2(E₀² + B₀²) sin²θ sinh²η ≥ 0 exakt, für jede Boostrichtung (Polarwinkel θ zur Achse) und Rapidität η. Gleichheit genau für
Boosts entlang der Achse; Hessesche 4(E₀² + B₀²) sin²θ, Kern genau die Achse. Der Rahmen E ∥ B ist das eindeutige Minimum der Auslese bis auf Boosts
entlang der Achse, und die Achse ist die Entartungsrichtung.

## H122b (OP5, Ruhesystem als Extremum): widerlegt in allen drei Stufen
| Stufe | entlang der Achse | quer zur Achse | Urteil |
|---|---|---|---|
| (i) modeweise, k = (1, 0, 1), b = ½ | −0,148 | +0,296 | Sattel |
| (ii) Azimutmittel, a = k_z = 1, b = ½ | −0,148 | +0,139 | Sattel |
| (iii) isotrop, \|k\| = 1, b = ½ | −0,0148 | +0,0741 | Sattel |

Isotrop exakt: entlang 2b²(5b² − 2)/(45(1 − b²)²), negativ für b² < 2/5; quer 2b²(4 − b²)/(45(1 − b²)²) > 0.

## H122c (OP5, Achse als Entartungsrichtung): widerlegt
Entlang der Achse ändert sich N, modeweise und im Azimutmittel für jedes k_z ≠ 0 (Faktor b²k_z²), im isotropen Mittel um 2b²(5b² − 2)/(45(1 − b²)²).
Im isotropen Mittel gibt es keine Richtung mit N = N(0) für alle b: Das verlangte 8 − 24 cos 2t = 0 und zugleich 13 + 24 cos 2t + 3 cos 4t = 0, unverträglich.

## Folge (vorab festgelegt): trägt nicht
Bei OP1 ist der Ausleserahmen ein Extremum des Feldes (Minimum der Energiedichte im Rahmen E ∥ B), entartet genau entlang der Achse. Bei OP5
ist das Ruhesystem der Präparation ein Sattel der Gezeitenauslese, und die Achse ist keine Entartungsrichtung: Rahmen und Achse sind dort eine
äußere Setzung des Detektors. Das schärft r48.2 („verwandt, nicht gleich“) zu einem strukturellen Unterschied. Die in r48.2 benannte Zuordnung
(Messachse = E∥B-Achse, Geschwindigkeit bezogen auf R) ist mit der Auslese von OP5 verträglich, wird von ihr aber nicht ausgewählt.

## Nachträglich (nicht in der Vorab-Notiz, ohne Gewicht für die Entscheidung)
- **Präparation nur quer zur Achse (k_z = 0), Azimutmittel:** N − N(0) = a² b² sin²t/3 + O(b⁴), null genau entlang der Achse, sonst positiv
  (Raster t = 0 … π/2, b = 0,1 … 0,99; kleinster Wert außerhalb der Achse 1,3·10⁻⁴). Diese Präparation hat dieselbe Struktur wie OP1: Minimum
  im Ruhesystem, entartet genau entlang der Achse (OP1: 2 sin²θ sinh²η). Die Achse wäre dann eine Eigenschaft der Präparation, nicht des
  Detektors. Das ist eine neue Setzung und bräuchte eine eigene Vorab-Notiz; der Strahl entlang der Achse (r32.4) ist gerade der entgegengesetzte
  Fall (k ∥ n, dort ist N = 0).
- Im isotropen Mittel verschwindet der Term zweiter Ordnung bei cos²t = 2/3. Das ist die gewöhnliche Quadrupolstruktur (Legendre P₂) und
  wird nicht gewertet.

## Lesart
Q1b hat damit eine klare Antwort: Ein gemeinsames Auslesegesetz für Rahmen und Achse gibt es zwischen OP1 und OP5 nur unter einer zusätzlichen
Setzung, entweder der Zuordnung aus r48.2 (Detektor nach dem Feld ausgerichtet) oder einer Präparation quer zur Achse. Die Auslese selbst wählt
den Rahmen bei OP5 nicht. Für OP1 bestätigt die Rechnung, dass Lesart B einen ausgezeichneten Rahmen hat. Kein Vergleich mit Messdaten. OP1, OP5 und
Q1 offen.
