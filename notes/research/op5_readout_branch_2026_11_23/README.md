# Zweig B: Rahmen, Achse und Orientierung als Daten der Auslese, trägt (Erkundung, teilweise nicht blind, 23.11.2026)

**Ergebnis in einem Satz:** Die gerichtete Kopplung des Vergleichsmodells ist exakt die kovariante Auslese −hΠ^{μν}u^αu^βR_{μανβ}
eines Detektors mit Rahmen u und Messachse n (Π = Projektor quer zu n in seinem Ruhesystem); die Zeitorientierung fällt heraus, die
verlangsamte Ausbreitung r_m ist für den führenden Kontrast entbehrlich, und der Zweig sagt eine Abhängigkeit des Kontrasts von der
Bewegung des Detektors relativ zur Präparation voraus. **Nach dem vorab festgelegten strengen Raster: trägt.** Die Zahl der gesetzten
Eingaben sinkt; gesetzt bleiben die Existenz eines massiven Spin-2-Vermittlers mit Masse m und seine Kopplung g_m an den
Higgsradius über die Auslese.

Auftrag des Autors: „Zweig B: Auslese“ nach r45. Verfahren vorab: `Methoden_Notiz.md` (Commit bb7274a1). Teilweise nicht blind (B2, B3).
Skript `readout_branch.wl`, Ausgabe `run/readout_branch.txt`, Wolfram exakt. Qiskit nicht geeignet. Keine H-Nummer.

## Ergebnis
| Schritt | Befund |
|---|---|
| B1a | −hΠ^{μν}u^αu^βR⁽¹⁾_{μανβ} mit Π^{μν} = −η^{μν} + u^μu^ν − n^μn^ν gibt im Ruhesystem genau die Quelle der bifokalen Notizen (Quotient 1). |
| B1b | Πuu R = −R_{uu} − E_{nn} identisch; beide Teilquellen sind erhalten. |
| B1c | Fierz–Pauli-Zähler: gesamt ⅔(x² − ax + a²) = N_m; Ricci-Teil ⅔(a + k_z²)², Achsen-Teil ⅔(k_z² − x)², dazu ein Kreuzterm. N_m kommt aus der ganzen Quer-Auslese, nicht aus einem Teil allein; die k_z-Abhängigkeit hebt sich weg. |
| B2 | Die Quelle ist unter u ↦ −u unverändert, der Zähler unter ω ↦ −ω. Die Zeitorientierung der Auslese spielt für N_m keine Rolle. |
| B3 | Statisch: g_m²·⅔a²/(m² + r_m q) = ⅔g_m²a²/m² − ⅔g_m²a² r_m q/m⁴ + …; das führende Glied hängt nicht von r_m ab. Mit r_m = 1 (gewöhnliches Lorentz-kovariantes Feld) und g_m² = 3/100 sind beide Bedingungen aus r38.2 erfüllt. |
| B4 | Statische Quelle, Detektor mit Geschwindigkeit β. Entlang der Achse: N = ⅔a(a − β²k_z²) + O(β⁴). Quer zur Achse: N = ⅔a² + ⅔a²β²cos²φ + O(β⁴). Die Abhängigkeit ist nicht null. |

## Bilanz nach dem strengen Raster
| vor Zweig B (r45) | nach Zweig B |
|---|---|
| gerichtete Kopplung mit gesetztem Rahmen u und Achse n | Kopplung an die Quer-Auslese; u und n sind Rahmen und Messachse des Detektors |
| verlangsamte Ausbreitung r_m | entbehrlich für den führenden Kontrast; r_m = 1 zulässig |
| Werte r_m, g_m, m | g_m, m |
| Zeitorientierung (r40–r44, H118) | fällt heraus |
| (stillschweigend) Existenz eines massiven Vermittlers | Existenz eines massiven Spin-2-Vermittlers mit Masse m; gesetzt |

Keine neue Eingabe kommt hinzu: u und n sind Angaben der Messung, keine Parameter des Modells. r32.4 nennt den Kontrast selbst schon
„the tidal readout of a ray along the axis“.

## Lesart
- Im Zweig B liest ein Detektor das Gezeitenfeld quer zu seiner Achse in seinem Ruhesystem aus; ein gewöhnliches massives Spin-2-Feld, das
  linear an den Higgsradius gekoppelt ist, gibt dann den gerichteten Term. Das ausgezeichnete Bezugssystem, das r36 verlangt, ist der
  Detektor; ein Medium, ein String oder eine Keimströmung wird dafür nicht gebraucht.
- Die Fragen aus r39–r44 (Entkopplung, Gewichte, Zeitumkehr oder Spiegelung) entfallen in diesem Zweig.
- Unterscheidende Vorhersage: Im Zweig B hängt der Kontrast von der Bewegung des Detektors relativ zur Präparation ab, mit relativer Größe
  β² und der angegebenen Winkelstruktur; im Zweig H hängt er von der Bewegung des Mediums ab, nicht vom Detektor. Für Laborgeschwindigkeiten
  ist β² sehr klein (Erdbahn β ≈ 10⁻⁴, also 10⁻⁸); die Unterscheidung ist grundsätzlich, praktisch schwer.
- Lesart zu r33.3: Ein massives Feld mit r_m = 1 hat ohnehin eine Gruppengeschwindigkeit unter c; die verlangsamte Ausbreitung r_m < 1 ist für
  den führenden Kontrast keine eigene Anforderung.
- Offen und jetzt sauber gestellt: Gibt es im QSC-Modell einen massiven Spin-2-Freiheitsgrad, der linear an den Higgsradius koppelt? W1 und W2
  haben ihn nicht (r33, r34). Das ist die verbleibende Frage der Feldseite, ohne Rahmen- oder Orientierungsfrage.
- OP5 und H96 bleiben offen; OP3 ruht und wird nicht berührt.
