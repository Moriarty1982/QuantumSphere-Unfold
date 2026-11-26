# Vorab-Notiz H163: Minimalpunkte als neue Startpunkte; welche Kraft macht daraus eine Kreisbahn, und was geschieht beim Schwungholen?

**Stand:** 2026-11-26, vor der Rechnung festgelegt und vor dem ersten Skriptlauf committet. **Überwiegend nicht blind** (siehe „Vorab offengelegt“).
Anlass: Autor, 26.11.2026, 09:57 UTC, als Richtigstellung zu H160: „wenn die proben ihren minimalabstand haben, dass dann gedanklich angehalten wie und diese
beiden punkte dann als neue startpunkte benutzt werden deren spuren wieder am kern vorbei gehen, nur diesmal ist deren bahn halt kürzer und müsste dem minimal
möglichen abstand entsprechen. man könnte dann fragen welche kraft auf die partikel einwirken müsste, dass sie danach in einer kreisbahn um den kern fliegen. und
danach was passieren würde, wenn sie dabei schwung holen und den bereich wieder verlassen, also einmal geschlossener orbei und einmal parabolische flugbahn“.
H160 hatte die neuen Proben aufeinander gezielt; das war nicht gemeint. H162 ist im Physik-Faden vergeben, daher H163.
Skripte **k354** (Python, numpy/scipy) und **k354b** (Wolfram Language, exakt und NDSolve). Kein Qiskit (keine Schaltung). Kein HDL/MMA-Vergleich (kein
RUN_TAPE-Ablauf). Kein Guard wird berührt.

## Vorwissen geprüft
- H160 (k351, k351c): Zielen auf den anderen Punkt gibt Kollaps; Bahnformel über den Exzentrizitätsvektor geprüft (Wolfram 10⁻¹⁹).
- H159 (k350): Schattenellipse z = a·e^{iφ} + b·e^{−iφ} aus zwei gegenläufigen Kreisanteilen, μ = b/a; P bei μ = 1 (Strecke), R bei μ = 0 (Kreis).
- k353: Ablenkwinkel Newton 2m/b, Schwarzschild 4m/b.
- Suche nach „Kreisbahn“, „Fluchtgeschwindigkeit“ unter `notes/research`, `wiki` (26.11.): OP1-Kandidatenliste Geschwindigkeit, Fokusbahn W2 (OP5), Drehrate k251;
  keine Rechnung zu Einschuss in eine Kreisbahn oder zur gebunden/ungebunden-Grenze.

## Modell (gesetzt)
Ebene, Kern im Ursprung, GM = 1. Zwei Proben auf parallelen Strahlen zu beiden Seiten des Kerns (Stoßparameter +b₁, −b₂, Geschwindigkeit v∞ ≥ 0 im Unendlichen).
Auslesepunkt = Punkt größter Annäherung, Radius r_p, dort Geschwindigkeit v_p tangential.
- **Neustart, Auslegung T (Fortsetzung):** Der Auslesepunkt ist Startpunkt, die Probe behält Betrag und Richtung ihrer Geschwindigkeit. „Anhalten“ ist nur gedanklich.
- **Neustart, Auslegung P (parallel):** Der Auslesepunkt ist Startpunkt, die Probe behält den Betrag, die Richtung wird auf die ursprüngliche Einflugrichtung
  zurückgestellt. Wiederholt bis 200 Schritte oder r < 10⁻¹².
- **Kraft:** (i) ein Stoß entlang der Bahn am Auslesepunkt, (ii) eine dauernde zusätzliche Zentralkraft f·(1/r²), die die Bahn zum Kreis macht.
- **Schwung holen:** Von der Kreisbahn (Radius r, Geschwindigkeit v_c) wird die Geschwindigkeit tangential auf k·v_c erhöht.
- **Schwarzschild-Variante:** Geodäten mit m = GM/c², Energie E je Ruhemasse, Drehimpuls L; (dr/dτ)² = E² − (1 − 2m/r)(1 + L²/r²).
- **Gitter (vorab):** b ∈ {0,25; 0,5; 1; 2; 4; 8}, b₂/b₁ ∈ {1; 1,5}, v∞ ∈ {0; 0,5; 1; 2} (v∞ = 0: Parabel mit vorgegebenem r_p ∈ {0,5; 1; 2}); k ∈ {1,1; 1,2; 1,3; 1,4;
  √2; 1,5}; Schwarzschild m = 0,05 mit E ∈ {1; 1,1; 1,5; 3} und Licht.

## Hypothese H163
Die Minimalpunkte laufen auf einen kleinsten möglichen Abstand r_min > 0 zu; dort macht eine angebbare endliche Kraft aus der Bahn eine Kreisbahn; mit
zusätzlichem Schwung wird daraus einmal eine geschlossene Bahn und einmal eine parabolische Flucht.

## Entscheidungskriterien
- **K-a (kleinster Abstand, Newton):** Gibt es in Auslegung T oder P einen Grenzradius r_min > 0, der nicht nur der erste Auslesepunkt ist und unter den keine
  Bahn kommt? Ja: bestätigt. Bleibt in T einfach der erste Punkt stehen und läuft P gegen null: widerlegt.
- **K-b (Kraft für die Kreisbahn, Newton):** Formeln v_p/v_c = √(2 + v∞²·r_p) für den Stoß und f = 1 + v∞²·r_p für die Zusatzkraft (zusammen mit der Schwerkraft
  also das (2 + v∞²·r_p)-Fache). Nach Anwenden ist die integrierte Bahn ein Kreis (Radiusschwankung über 5 Umläufe unter 10⁻⁸) in allen Gitterpunkten: bestätigt.
- **K-c (Schwung holen, Newton):** Für k < √2 geschlossene Ellipse mit fernstem Punkt r·k²/(2 − k²), die nach einem Umlauf am Startpunkt schließt (Abweichung
  unter 10⁻⁸); für k = √2 Parabel (Energie null, kein Umkehrpunkt bis r = 10⁴); für k > √2 Hyperbel: bestätigt. Sonst widerlegt.
- **K-d (kleinster Abstand, Schwarzschild):** Es gibt einen Radius, an dem die für die Kreisbahn nötige Zusatzkraft null ist: r = 4m für E = 1 (Einfall aus der
  Ruhe im Unendlichen), allgemein r(E) zwischen 3m und 4m, r = 3m für Licht. Numerisch: Der kritische Stoßparameter trennt Einfang und Entkommen, die Zahl der
  Umläufe wächst bei Annäherung an ihn unbeschränkt (mindestens 3 Umläufe bei relativem Abstand 10⁻⁸), und der innerste Punkt der entkommenden Bahnen geht gegen
  r(E). Trifft das für alle E des Gitters zu: bestätigt.
- **Gesamturteil:** bestätigt, wenn K-a bis K-d bestätigt sind. „Trägt teilweise“, wenn K-b und K-c bestätigt sind und genau eines von K-a, K-d scheitert.

## Ohne Kriterium (Erkundung)
- **Addierte Auslesen:** Summe der Orte der zwei gegenläufig umlaufenden Proben, z(t) = r₁·e^{iω₁t} + r₂·e^{−iω₂t} mit ω = r^{−3/2}; Form der Spur für r₁ = r₂ und
  r₁ ≠ r₂, Vergleich mit der Schattenellipse aus H159.
- Schwarzschild: Was geschieht bei kleinem Stoß nach außen und nach innen von der Grenzbahn bei 4m; Lage der innersten stabilen Kreisbahn; Vergleich des
  Faktors „doppelte Schwerkraft“ aus K-b mit dem Faktor 2 des Ablenkwinkels (k353).

## Vorab offengelegt (kein Teil der Vorhersage)
Beim Aufschreiben bekannt (Lehrbuch und Überschlag):
- Auslegung T ändert nichts: Die Bahn ist dieselbe, der Auslesepunkt bleibt stehen. In Auslegung P ist der neue Stoßparameter b′ = r_p·√(1 − 1/e²) < r_p < b; die
  Folge fällt gegen null. Im Newton-Feld einer Punktmasse gibt es keinen kleinsten Abstand: r_p → 0 für b → 0. K-a steht damit als widerlegt fest.
- Energieerhaltung gibt v_p² = v∞² + 2/r_p und v_c² = 1/r; daraus K-b. Für Einfall aus der Ruhe (v∞ = 0) ist das Verhältnis genau √2 und die nötige Zentralkraft
  genau das Doppelte der Schwerkraft.
- K-c ist die Vis-viva-Gleichung.
- Schwarzschild: gebunden/ungebunden-Grenzbahn bei r = 4m mit L = 4m, Lichtring bei 3m mit b = 3√3·m, innerste stabile Kreisbahn bei 6m. Die Kreisbahnen zwischen
  3m und 6m sind instabil. K-d steht damit als bestätigt fest; offen sind die Zahlen (Umläufe je Abstand, Verhalten nach kleinem Stoß).
- Zwei gegenläufige Kreisanteile gleichen Radius und gleicher Drehrate addieren sich zu einer Strecke durch den Kern.

## Vorhersage
- K-a: **widerlegt.** K-b: **bestätigt.** K-c: **bestätigt.** K-d: **bestätigt.**
- Gesamt: **trägt teilweise.** Den kleinsten möglichen Abstand gibt es nicht bei Newton, wohl aber mit der relativistischen Bahngleichung.

## Grenzen (vorab)
Übersetzung gesetzt (Punktmasse, zwei Auslegungen des Neustarts, Stoß oder Zentralkraft). Klassische Bahnen, keine Wellen. Die Schwarzschild-Variante ist
Lehrbuch-ART und keine Aussage des Modells; nach H147 hat das Modell keine eigene Kopplung an eine Metrik. Keine Größe des Companion geht ein. OP1 bis OP5
bleiben offen.
