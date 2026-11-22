# Ergebnis H118: Der Bestand legt die Orientierung des Oktanten nicht fest; sie ist eine Zeitorientierung

**22. November 2026. Vorab-Notiz `Vorab_Notiz_H118_Oktant_Orientierung.md` (Commit 371f14d7). Skript `h118_octant_orientation.wl`,
Ausgabe `h118_octant_orientation.txt`. Teilweise nicht blind. Status: H118a bestätigt (exakt), H118b widerlegt (kein Kandidat in
Klasse U).**

Werkzeug: Wolfram Language (exakt) über den Wolfram-Kern dieser Sitzung; eine lokale Installation war nicht vorhanden. Kein HDL/MMA-
Vergleich, weil die Entscheidung an einer algebraischen Parität hängt, nicht an einem endlichen Auswahlablauf. Der erste Lauf scheiterte
an zwei Programmierfehlern (Klammerung in `pole[]`, Simplify mit komplexen Symbolen); nach der Korrektur lief das Skript ohne Warnung,
die Kriterien blieben unverändert.

## Kontrollen
| Kontrolle | Wert | Schranke | Ergebnis |
|---|---|---|---|
| Θ² auf χ | −1 | exakt | erfüllt |
| R, T, J_B bilden Tripel auf Tripel ab, Phase erhalten | 8 von 8 | exakt | erfüllt |
| umgekehrter Umlauf gibt die konjugierte Phase (wie H116) | 8 von 8 | exakt | erfüllt |
| 200 zufällige Unitäre / antiunitäre Gegenstücke | 7,8·10⁻¹⁶ / 1,0·10⁻¹⁵ | 10⁻¹² | erfüllt |

## H118a (exakt): bestätigt
Für die acht Tripel aus je einem Pol von R = σ_z, T = σ_x, J_B = σ_y gilt die Bargmann-Phase **τ · ε · π/4**: τ = +1 für den Umlauf
R → T → J_B, τ = −1 für den umgekehrten, ε = Produkt der drei Polvorzeichen. Alle 16 Reste sind null, der Betrag der
Bargmann-Invariante ist immer 1/(2√2). R, T, J_B erhalten ε (die beiden Bahnen aus r16.7), Θ = iσ_y K kehrt ε um.

## H118b (Entscheidung): widerlegt
| | Kandidat | Klasse | Begründung |
|---|---|---|---|
| K1 | Frame-Abbildungen R, T, J_B | G | erhalten jede Bahn (Rechnung (2)) |
| K2 | Kompensator C, reelle Halbierung C_n | G | reelle Ränge; die Wahl n gegenüber in ist selbst unbestimmt (H115) |
| K3 | Übergangswahrscheinlichkeiten, Ränge, L_loc, Θ/R-Closure, Teichmüller-Verzerrung | G | Beträge, Ränge, boolesche Zertifikate |
| K4 | Umkehrwalze Θ | S | vertauscht die Bahnen, wählt keine |
| K5 | Richtung von U (r16.9) | Z | Im⟨ψ\|Uψ⟩ = (√3/2)(p₊ − p₋): ungerade unter U ↦ U⁻¹ und unter Helizitätstausch, aber die Gewichte p_k stammen aus den Leptonmassen; außerdem ist der Orbit von r16.9 nicht das Oktant von r16.7 (Rang zwei), eine Abbildung fehlt |
| K6 | Polwahl der drei Feldvorzeichen | O | die Pole sind die Ecken des Oktanten, aber der Bestand legt nur den Materiepol fest (Materiefeld s = 1); E·B-Vorzeichen und Helizität (selbstdual) sind in r16.3 Beispiele, keine Festlegung |
| K7 | Index/Maske des doppelten Hilbert-Shifts | O | Kodierung; keine Abbildung auf den Umlauf (H117) |
| K8 | mitgeführtes Phasenregister | O | ungerade, wenn vorzeichenbehaftet; Vorbereitung und Abbildung offen |
| K9 | Residuum Im ζ_sh | O | ungerade unter Konjugation, definiert im historischen Antiphasenkorridor; keine Abbildung auf den Oktanten |

Kein Kandidat liegt in Klasse U. Nach dem vorab festgelegten Kriterium ist H118b widerlegt: Das Vorzeichen der Oktantphase ist im Bestand
eine zusätzliche Wahl, wie die Überlappung ½.

## Zusatz (im Skript, in der Vorab-Notiz nicht als Kriterium genannt)
- **Zeitumkehr der Feldamplituden** (E ↦ Ē, B ↦ −B̄ für E(t) = Re(E e^{−iωt})) bildet s± exakt auf s̄± ab, wirkt auf χ also als
  komplexe Konjugation K (bis auf die Zweigwahl, die nach r16.3 ein R ist und die Bahn erhält). K kippt nur den Pol der J_B-Achse
  (sign Im s = sign E·B) und kehrt damit die Oktantphase um.
- **Parität** (E ↦ −E, B ↦ B) vertauscht s₊ und s₋, wirkt auf χ wie σ_x und erhält die Bahn.
- Damit ist die Orientierung des Oktanten **ungerade unter Zeitumkehr und gerade unter Parität und den Frame-Abbildungen**. Bei
  festem Materiepol hängt sie am Produkt sign(E·B) · sign(Helizität), das unter Parität gerade ist.

## Lesart
- Die Wahl des Rückwegs aus H116/H117 hat auf dem invarianten Dublett eine bestimmte Gestalt: Sie ist eine Wahl der Zeitorientierung
  der Auslesung, nicht der räumlichen Händigkeit. Eine native Herleitung müsste eine Zeitrichtung der Auslesung auszeichnen und zugleich
  die Reihenfolge des Umlaufs (τ) festlegen. Nachträglich: Ist die Reihenfolge selbst zeitlich, kippt die Zeitumkehr τ und ε zugleich,
  und die Phase wäre dann zeitumkehrgerade; diese Variante ist nicht geprüft und bräuchte eine eigene Vorab-Notiz.
- K5 zeigt, wo eine Zeitrichtung im Bestand schon vorkommt (Translation um ein Drittel der Periode), aber nur mit Gewichten aus den
  Leptonmassen.
- Kein Vergleich mit Leptondaten. OP3 bleibt offen; Restbiegung und Kerngröße (OP1) sind unberührt.
