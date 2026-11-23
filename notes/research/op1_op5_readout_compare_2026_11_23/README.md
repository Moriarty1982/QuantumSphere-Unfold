# OP1 (Lesart B) und das OP5-Vergleichsmodell: verwandte, nicht gleiche Auslesebegriffe (Erkundung, teilweise nicht blind, 23.11.2026)

**Ergebnis in einem Satz:** Beide Auslesen lesen den elektrischen Teil einer Feldstärke relativ zur Vierergeschwindigkeit des Beobachters und
hängen gerade von seiner Rapidität ab, als Funktion von 2η; sie unterscheiden sich aber darin, wem Achse und Ruhesystem gehören. Bei OP1 sind
beide Eigenschaften des Feldes (Ruhesystem R mit E ∥ B und dessen Achse), beim Vergleichsmodell gehört die Achse dem Detektor und die
Geschwindigkeit bezieht sich auf die Präparation. **Nach dem vorab festgelegten Raster: verwandt, nicht gleich.**

Auftrag des Autors: „mach das“ (Konsistenzprüfung nach r47). Verfahren vorab: `Methoden_Notiz.md` (Commit 498f0578). Skript
`readout_compare.wl`, Ausgabe `run/readout_compare.txt`, Wolfram exakt. Qiskit nicht geeignet. Keine H-Nummer.

## Kontrollrechnung
- OP1: Für ein Feld mit E ∥ B entlang z ist φ = 1 im Ruhesystem R. Ein Beobachter, der sich quer zur Achse mit Rapidität η bewegt, misst
  |E′|² + |B′|² = (E₀² + B₀²) cosh 2η und φ = sech 2η, gerade in η. Die Energiedichte ist |T_{μν}u^μu^ν| = ½(|E′|² + |B′|²). Ein Beobachter
  entlang der Achse sieht φ = 1 für jedes η.
- OP5 (Zähler aus r46.3 mit β = tanh η): entlang der Achse N(η) = [8a² + 4ak_z² + 3k_z⁴ − 4k_z²(a + k_z²) cosh 2η + k_z⁴ cosh 4η]/12; quer zur
  Achse ein Polynom in cosh 2η und cosh 4η mit Winkelabhängigkeit. Beide sind gerade in η; Ruhewert ⅔a² in beiden Richtungen.

## Vergleich
| Kriterium | OP1, Lesart B | OP5, Ausleseseite (r46/r47) | gleich? |
|---|---|---|---|
| K1 was gelesen wird | elektrischer und magnetischer Teil von F relativ zu u, normiert durch die Energiedichte T_{uu} | elektrischer Teil des Riemann-Tensors R_{μανβ}u^αu^β, quer zu n projiziert | ja, beide: elektrischer Teil relativ zu u |
| K2 Abhängigkeit von u | gerade, sech 2η | gerade, Polynom in cosh 2η, cosh 4η | ja |
| K3 Achse | E ∥ B-Achse des Feldes in R; Bewegung entlang der Achse unsichtbar | Messachse n des Detektors; Bewegung entlang der Achse sichtbar | nein |
| K4 Bezugssystem der Geschwindigkeit | Ruhesystem R des Feldes | Präparation (Materiequelle); die Verlangsamung braucht nach r47 zusätzlich ein Bezugssystem auf der Feldseite | nein |
| K5 Normierung | dimensionsloses Verhältnis Invariante/Energiedichte, hängt nur von η ab | absolute Gezeitengröße | nein |

## Lesart
- Gemeinsam ist der Kern: Auslese heißt in beiden Fällen, den elektrischen Teil einer Feldstärke im Ruhesystem des Beobachters zu nehmen.
  Weil das quadratisch in u ist, fällt die Zeitorientierung in beiden heraus; bei OP1 trennt nur das Vorzeichen der Invariante Re s die
  Frames M und T.
- Verschieden ist die Zuordnung: OP1 hat ein Ruhesystem und eine Achse **auf der Feldseite** und nur die Rapidität beim Beobachter. Das
  Vergleichsmodell legt die Achse zum Detektor und bezieht die Geschwindigkeit auf die Präparation.
- Damit beide denselben Begriff benutzten, müsste (i) die Messachse n des Vergleichsmodells die E ∥ B-Achse des Feldruhesystems sein und
  (ii) sich die Geschwindigkeit des Detektors auf das Ruhesystem R beziehen. Dann wäre R auch ein Kandidat für das Bezugssystem auf der
  Feldseite, das r47 für die Verlangsamung verlangt. Das ist eine benannte Zuordnung, nicht hergeleitet und nicht geprüft.
- Kein Widerspruch: Die beiden Begriffe schließen sich nicht aus, sie verteilen Achse und Ruhesystem verschieden.
- OP1 und OP5 bleiben offen.
