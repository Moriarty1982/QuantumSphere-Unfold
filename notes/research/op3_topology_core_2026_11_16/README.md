# OP3: Das Kern-Bild topologisch (Erkundung, analytisch, nicht blind)

16. November 2026. Auftrag des Autors: „analysiere das mal topologisch“, nach der Linie Korrekturterm → Verbindung → undurchlässiger Rand
(`../op3_correction_term_2026_11_16/README.md`), die bei zwei Fragen endete: warum genau ein Kern, und warum ΔΦ = γ_M/2. Skript `topology.py`,
Ausgabe `run/topology_stdout.txt`. Kein Zielwert ausgewertet, keine H-Nummer.

## Vorwissen geprüft
- `../op3_guarded_core_flux_2026_11_15/README.md`: Chern-Zahl 1, Schritt 2 (Kugel ohne n Kappen hat n − 1 freie Holonomien; genau ein Kern
  ausgezeichnet), Umkehrwalze als Antipodenabbildung mit Θ² = −1 (Kramers), Faden 3 (Kugel B_ε(K) im S³ bricht Fasern über einer Kappe).
- r16.7 (Oktant, Phase ±π/4, zwei Bahnen nach dem Vorzeichen), v4.9.0-r02.2/r02.3 (Umkehrwalze antilinear, fixpunktfrei).

## 1. Was Topologie festlegen kann und was nicht
- **Ganze Zahlen und Symmetrieanteile, keine stetigen Werte.** Die Generationskugel trägt das Hopf-Bündel (Spin ½, Chern-Zahl 1, Gesamtfluss 2π).
  Der Oktant ist durch die Oktaedersymmetrie genau ein Achtel davon: π/4 = 2π/8. Die Zielphase 2/3 ist dagegen kein rationaler Teil von 2π
  (2/3 : 2π = 1/(3π)). **ΔΦ = π/4 − 2/3 kann deshalb nicht aus Topologie allein kommen**; es braucht eine stetige Eingabe. Im Bestand ist das γ_M aus
  der Zählregel (OP1). Das ist eine harte Grenze, keine Lesart.
- **Die Zahl der Kerne schon.** Die Kugel ohne n Scheiben hat eine Fundamentalgruppe vom Rang n − 1, also n − 1 freie Aharonov-Bohm-Holonomien.
  n = 0 biegt nicht, n = 1 biegt ohne freien Parameter, n ≥ 2 macht die Phase frei (Schritt 2 der Kern-Notiz). Genau ein Kern ist topologisch die einzige
  starre Biegung.

## 2. Neu: die Umkehrwalze als Symmetrie widerspricht Fall A
Θ = iσ_y K bildet den kohärenten Zustand bei n auf den bei −n ab, Θ² = −1 (300 Punkte geprüft). Für die natürliche Verbindung ist Θ eine Symmetrie:
Die Bargmann-Phase des Antipodendreiecks ist das Negative der Phase des Dreiecks (300 Zufallsdreiecke). Weil die Antipodenabbildung die Orientierung
umkehrt, heißt das für die Flussdichte: **F(−n) = F(n).**

Folge: Ist die Umkehrwalze eine **Symmetrie** der Verbindung, dann zieht ein flussfreier Kern bei der Zyklusachse z_c einen ebenso flussfreien Kern bei
−z_c nach sich. Fall A der Kern-Notiz (verdrängter Fluss *sammelt* sich am Gegenpol) verletzt diese Symmetrie. Die Lesart vom 15.11. („was in den Kern
hineinläuft, kommt am Gegenpol heraus“) benutzt die Umkehrwalze als **Abbildung** (Transport), nicht als Symmetrie. Beides zugleich geht nicht. Das ist
eine Präzisierung der Umkehrwalzen-Lesart, keine Widerlegung von H102 (H102 setzt nur φ = π/4 − γ_M/2, nicht den Mechanismus).

**Die Θ-symmetrische Alternative:** zwei flussfreie Kerne bei ±z_c, der verdrängte Fluss symmetrisch verteilt. Im Quotienten S²/Θ = ℝP² ist das
**eine** Punktierung, also wieder „genau ein Kern“, nur eine Ebene höher. ℝP² ohne Scheibe ist ein Möbiusband; ob die Θ-Bedingung die eine Holonomie
dort festlegt, ist nicht geprüft. Die Phase dieser Konfiguration hängt an Ω und an der Verteilung; ein Vergleich von Ω mit γ_M wäre nachträglich und
müsste vorab registriert werden. **Hier nicht ausgewertet.**

## 3. Neu: Die fermionische Umkehrwalze erzwingt Fluss (Borsuk–Ulam)
Auf dem trivialen Bündel gäbe es eine Struktur Θ mit Θ² = −1 über der Antipodenabbildung nur mit einer stetigen Funktion f: S² → S¹ mit f(−n) = −f(n).
Eine solche ungerade Abbildung gibt es nach dem Satz von Borsuk–Ulam nicht. **Also verlangt eine fermionische Umkehrwalze ein nichttriviales Bündel:**
Die Generationskugel muss eine von null verschiedene Chern-Zahl tragen, also Fluss, also eine von null verschiedene Bargmann-Phase. Das Hopf-Bündel
(Chern-Zahl 1) erfüllt es. Dass allgemein eine ungerade Chern-Zahl nötig ist, halte ich für richtig, habe es aber nicht nachgelesen.

Lesart: Dass die Leptonen überhaupt eine Koide-Phase haben, ist topologisch an ihre Fermion-Natur gebunden (Θ² = −1); welchen Wert sie hat, nicht.

## Ergebnis
1. „Genau ein Kern“ ist topologisch begründbar: auf S² als einzige starre Biegung, mit Umkehrwalze als Symmetrie als ein Kernpaar ±z_c, das in ℝP² eine
   Punktierung ist.
2. ΔΦ = γ_M/2 ist topologisch **nicht** erreichbar (kein rationaler Teil von 2π); die Zahl muss von außen kommen, und das bleibt OP1.
3. Die Umkehrwalze als Symmetrie und Fall A (Fluss sammelt sich am Gegenpol) schließen sich aus; die symmetrische Alternative ist das Kernpaar.
4. Eine fermionische Umkehrwalze erzwingt einen nichttrivialen Fluss (Borsuk–Ulam).

Offen: die Holonomie auf dem Möbiusband unter Θ; die Phase des Kernpaars (nur mit Vorab-Notiz). OP1 und OP3 offen; H102 unverändert.

## Nachtrag (16.11.2026): Mehrere Umkehrwalzen, abgeglichen mit den Kryptologie-Teilen
Frage des Autors: „es könnte sein, dass es mehrere Umkehrwalzen gibt; vergleiche das mit den Teilen über Kryptologie im Paper.“ Skript `reflectors.py`,
Ausgabe `run/reflectors_stdout.txt`.

**Was das Paper zur Kryptologie sagt.** v470/24 („Computational Interpretation, Enigma Analogy, and Bomba-Style Structural Search“, im Hauptkorpus
`sources/parts/08_computational_and_pre_op_foundation/01_computational_surface_to_local_zuse_core.tex`) ist inzwischen auf eine kurze Zitierfläche
verdichtet: ein Reflektor-/Projektor-/Routing-Vergleich (Enigma) und eine Bombe-artige Eliminationssuche über zulässige Menüs (v470/15 „Bombe-guided
compensator menu“, v470/19 „Bombe-sieve persistence“), ausdrücklich ohne kryptanalytischen Identitätsanspruch. v470/09 führt J als
„Umkehrwalze/involution“ mit dem Ausleseprojektor C = ½(id + J). Die physikalische Ausarbeitung steht in **v4.9.0-r02** („The Round Trip about the
Photon and the Umkehrwalze“) und **r04**.

**Der Bestand kennt schon mehrere Umkehrwalzen:**

| Umkehrwalze | Quelle | Art | auf Feldern | auf der Generationskugel χ |
|---|---|---|---|---|
| C = PT (z ↦ −z) | r02.2 | linear, zentral, Holonomie des seitenwechselnden Rundwegs | fixpunktfrei („fixes no non-zero field“) | **Identität** (s± unverändert) |
| J_B (E ↔ B) | r02.3 | antilinear, Involution, Reflektor | Eigenkanäle E = ±B, je eine Seite des Photons | Halbdrehung um y (σ_y), Fixpunkte = Eigenkanäle |
| Rotor-Konjugate R_α⁻¹ J_B R_α = R_{−2α} J_B | r02.5 (Enigma-Muster), r04 (O(2)) | ein Reflektor, durch die „Walzenstellung“ α verschoben | bei α = π/4 genau T | Halbdrehungen um alle Achsen der Äquatorebene (senkrecht zur Helizitätsachse), Periode 90° |
| Familie iR z̄ (R ∈ O(3,ℂ), R R̄ = 1) | r02.3(b) | antilineare Involutionen, die Materie und Tachyon tauschen | – | nicht einzeln geprüft |

Das ist das Enigma-Bild: **eine** feste Umkehrwalze, deren wirksame Form sich mit der Walzenstellung ändert (Konjugation durch den Rotor, hier die
Dualitätsdrehung). r02.5 sagt es ausdrücklich: Hin, Reflexion, zurück ergibt die direkte Reflexion gefolgt von der Rundweg-Umkehrwalze C.

**Abgleich mit dem Kern-Bild (nachgerechnet):**
1. **Genau eine Walzenstellung tauscht Kern und Gegenpol.** Das Rotor-Konjugat bei Dualitätswinkel α = 22,5° = π/8 ist die Halbdrehung um
   (1, −1, 0)/√2; sie bildet z_c auf −z_c ab und den Oktanten der geladenen Leptonen auf den gegenüberliegenden Oktanten. Bei α = 0 ist es J_B, bei
   α = 45° T; keine dieser beiden tauscht Kern und Gegenpol.
2. **Auch sie erzwingt als Symmetrie ein Kernpaar.** Sie ist auf χ eine Drehung (Determinante +1), erhält also die Flussdichte, F(Mn) = F(n). Als
   Symmetrie der Verbindung zieht ein Kern bei z_c einen Kern bei −z_c nach sich, wie bei Θ. Das Ergebnis aus Abschnitt 2 gilt also für jede
   Umkehrwalze, die Kern und Gegenpol verbindet.
3. **Die Enigma-Eigenschaft „kein Buchstabe auf sich selbst“ gilt auf χ für keine Umkehrwalze des Bestands.** C ist auf χ die Identität; J_B, T und alle
   Rotor-Konjugate haben auf χ zwei Fixpunkte (ihre Eigenkanäle). Fixpunktfrei auf χ ist nur die Antipodenabbildung Θ = iσ_y K (antiunitär), und die
   steht nicht in r02/r04. Die Umkehrwalze der Kern-Notiz vom 15.11. ist damit eine **zusätzliche**: die Zeitumkehr des Dubletts χ selbst.
4. **Mehrere Umkehrwalzen gleichzeitig als Symmetrie gehen nicht.** Wären alle Rotor-Konjugate zugleich Symmetrien, wäre die Flussdichte unter allen
   Drehungen um die Helizitätsachse und unter deren Umkehr invariant; das verträgt sich nicht mit einem Oktanten. Im Enigma-Bild ist das natürlich: Zu
   jedem Zeitpunkt wirkt **eine** Walzenstellung, und sie wechselt. Eine zeitabhängige wirksame Umkehrwalze wäre die Form, in der die Idee des
   zeitabhängigen Korrekturterms und das Enigma-Bild zusammenkommen. Lesart, nicht gerechnet.

**Folgerung.** Es gibt mehrere Umkehrwalzen, und das Paper hat sie schon (C, J_B, die Rotor-Familie, die Familie aus r02.3(b)). Für das Kern-Bild zählt
die eine Walzenstellung α = π/8, die Kern und Gegenpol tauscht. Als Symmetrie gibt jede von ihnen ein Kernpaar, nicht Fluss am Gegenpol. Eine
fixpunktfreie Umkehrwalze auf χ wäre ein neues Element (Θ). Die Bedeutung von α = π/8 (halber Oktantenwinkel) ist nicht geprüft und wird nicht
gedeutet. OP3 offen.

## Nachtrag (16.11.2026): Wechselnde Walze
Auftrag des Autors: „Wechselnde Walze“. Skript `rotor_steps.py`, Ausgabe `run/rotor_steps_stdout.txt`. Erkundung, analytisch, kein Zielwert.

**Der Walzenschritt im Bestand.** r13.1/r14.1: Der Kompensator wirkt, wenn arg s eine der sechs Auslese-Richtungen Triole ∪ J_B(Triole) passiert, also alle
30° Dualitätswinkel, sechs Kicks je Schlag; ein Schlag ist ein Umlauf von s um das Photon und gleich der Rundweg-Umkehrwalze C (r14.1(c)). Die wirksame
Umkehrwalze in der Walzenstellung α ist R_α⁻¹ J_B R_α (r02.5). r14.1(b) nennt als Alternative das Viertelraster (45° in arg s, 22,5° Dualitätswinkel),
das den Faktor ½ statt ¾ gäbe und deshalb nicht übernommen wurde.

**Ergebnis (nachgerechnet):**

| Raster | Achsen der wirksamen Walzen auf χ | Produkt zweier aufeinanderfolgender Walzen | Bahn der Zyklusachse z_c |
|---|---|---|---|
| Triole ∪ J_B(Triole) (r14, sechs Kicks je Schlag) | drei Achsen in der Äquatorebene bei 90°, 150°, 30°, Periode drei Kicks | Drehung um die Helizitätsachse um **120°** | sechs Punkte bei ±1/√3 Höhe, keine Oktantenmitten außer (−1, 1, −1); nächster Abstand zu −z_c 24,4° |
| Viertelraster (r14.1(b), abgelehnt) | vier Achsen bei 90°, 135°, 0°, 45° | Drehung um die Helizitätsachse um **90°** | nur Oktantenmitten: (−1, 1, −1), (−1, −1, −1), (1, −1, −1), (1, 1, −1); bei α = 22,5° genau −z_c |

1. **Im Bestandsraster setzen zwei aufeinanderfolgende Walzen einen Generationsschritt zusammen.** Zwei Kicks sind ein Drittel des Schlags, und das
   Produkt der beiden wirksamen Umkehrwalzen ist die Drehung um 120° um die Helizitätsachse. Das ist genau der Drittelzyklus von r16.9 (Zeitverschiebung
   um ein Drittel der Periode als Generationszyklus). Eine wechselnde Walze verbindet damit das Enigma-Bild (r02, r14) mit dem Generationszyklus. Die
   Drei steckt dabei schon in der Triole von r14; neu ist nur, dass sie als Produkt zweier Reflexionen erscheint.
2. **Die Walze, die Kern und Gegenpol tauscht (α = π/8), liegt nicht im Bestandsraster, sondern im Viertelraster.** Das Viertelraster ist die
   Maschine der Oktanten: Es führt die Zyklusachse nur über Oktantenmitten, und sein Grundschritt ist 90°. Das Triolenraster ist die Maschine der
   Generationen (120°) und berührt die Oktantenmitten fast nie.
3. **Lesart, nicht gerechnet:** Das Kern-Bild (Oktant, Umkehrwalze bei π/8) und der Generationszyklus (Triole, 120°) gehören zu zwei verschiedenen
   Walzenrastern. Der Faktor des Viertelrasters ist ½, die Oktanten-Überlappung; der des Triolenrasters ist ¾. Ob die Biegung vom Oktanten weg mit dem
   Unterschied der beiden Raster zusammenhängt, wäre eine eigene Frage; sie wird hier nicht beantwortet und nicht numerisch geprüft.

OP3 offen; keine H-Nummer.

## Nachtrag (16.11.2026): Die zwei Walzenraster verglichen
Auftrag des Autors: „Zwei Raster vergleichen“. Skript `two_rasters.py`, Ausgabe `run/two_rasters_stdout.txt`. Erkundung, analytisch; keine Zahl wird mit dem
Zielwert verglichen.

| | Triolenraster (r14, Bestand) | Viertelraster (r14.1(b), verworfen) |
|---|---|---|
| erzeugte Gruppe auf χ | Diedergruppe der Ordnung 6 (Dreierachse = Helizitätsachse) | Diedergruppe der Ordnung 8 (Viererachse = Helizitätsachse) |
| in der Symmetriegruppe O des Oktanten (Würfelgruppe) | **nein** | **ja** |
| enthält die Frame-Abbildungen 1, R, T, J_B | nur 1 und J_B | **alle vier** (die Kleinsche Vierergruppe der HS(8)-Kopien) |
| Grundschritt zweier Walzen | 120° (Drittelzyklus r16.9, Generationsschritt) | 90° |
| Faktor (r14) | ¾ | ½ (Oktanten-Überlappung) |

Gemeinsam haben beide Raster nur **1 und J_B**; zusammen erzeugen sie eine Diedergruppe der Ordnung 24 um die Helizitätsachse (nicht die Würfelgruppe).

**Befunde (nachgerechnet):**
1. **Die Frame-Struktur gehört zum Viertelraster.** Die Kleinsche Vierergruppe {1, R, T, J_B}, also das Kopienregister von HS(8) und die Frame-Abbildungen,
   liegt ganz im Viertelraster, und das Viertelraster liegt ganz in der Symmetrie des Oktanten.
2. **Der Generationszyklus gehört zum Triolenraster** und liegt **nicht** in der Symmetrie des Oktanten.
3. **Die beiden Dreierachsen stehen im magischen Winkel.** Die Dreierachse des Triolenrasters ist die Helizitätsachse; die Symmetrieachse des
   Frame-Oktanten ist (1, 1, 1). Der Winkel zwischen ihnen ist genau arccos(1/√3) = 54,7356°.
4. **Es gibt zwei verschiedene Oktanten.** Der Frame-Oktant (Ecken = Eigenzustände von R, T, J_B, r16.7) ist keine Bahn des Drittelzyklus; seine Ecke auf
   der Helizitätsachse ist Fixpunkt des Zyklus. Eine Bahn des Drittelzyklus mit Überlappung ½ ist ebenfalls ein Oktant (paarweise orthogonale
   Bloch-Vektoren), aber um die Helizitätsachse herum gelegt. Beide haben dieselbe Phase π/4, denn sie gehen durch eine Drehung ineinander über.

**Einordnung.** Das Projekt hat beide Bilder benutzt: r16.7 (drei Auslesungen = Frame-Oktant) und r16.9 (Generationen = Drittelzyklus der Zeit). Der
Vergleich zeigt, dass sie zu zwei verschiedenen Walzenrastern gehören, deren Dreierachsen im magischen Winkel stehen, und dass sie nur J_B gemeinsam
haben. Solange beide Bilder für sich allein bleiben, geben sie dieselbe Phase π/4. Eine Biegung entstünde erst aus einer Konstruktion, die beide
verbindet, zum Beispiel Generationen aus dem Zeitzyklus, ausgelesen über die Frame-Abbildungen. Eine solche Konstruktion hätte keinen freien Parameter
nur dann, wenn J_B (das gemeinsame Element) die Lage festlegt. **Sie wird hier nicht gerechnet:** Ihr Ergebnis wäre eine Zahl, die mit 2/3 verglichen
würde; sie braucht deshalb zuerst eine Vorab-Notiz mit festgelegter Konstruktion. OP3 offen; keine H-Nummer.
