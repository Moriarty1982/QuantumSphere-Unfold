# Vorab-Notiz H160: Laufen die iterierten Auslesen zweier Proben am Kern auf eine stabile Kreisbahn zu?

**Stand:** 2026-11-26, vor der Rechnung festgelegt und vor dem ersten Skriptlauf committet. **Teilweise nicht blind** (siehe „Vorab offengelegt“).
Anlass: Autor, 26.11.2026, 07:40 UTC: „wir lassen die beiden teilchen nochmal los aber diesmal halten wir sie an, sobald sich beide proben zeitgleich am minimalem
abstand zum mittelpunkt befinden. von diesen beiden nächsten punkten, schicken wir wieder eine jeweils eine probe zum jeweils anderen und das machen wir so weiter,
meine vermutung ist, dass die addierten auslesen irgendwann eine stabile kreisbahn um den kern erzeugen könnten“; Freigabe zum Rechnen 09:25 UTC.
Skripte **k351** (Python, numpy/scipy) und **k351b** (Wolfram Language, unabhängig über NDSolve). Wolfram ist hier nur Gegenprobe der Bahnstücke; Qiskit nicht
vorgesehen (keine Schaltung). Kein HDL/MMA-Vergleich: der Ablauf ist eine Iteration reeller Bahnen, kein RUN_TAPE-Ablauf. Kein Guard wird berührt.

## Vorwissen geprüft
- `notes/research/licht_vermittler_zeit_2026_11_24/` und die Arbeitsnotiz zum Gedankenexperiment (Projektdateien, 24.11.): Julia-Iteration mit anziehendem
  3-Zyklus (k249), Drei-Mulden-Modell (k248, Schwelle ⅔ rein geometrisch), Kirchhoff-Ellipse als Lesart. Dort keine Bahniteration um einen Kern.
- Zwei-Sonden-Modell: `prop:triadic-two-probe` (v470/10), `notes/research/op5_bifocal_response_2026_11_18/Sondenform.md` (bifokale Sondenform, H96 offen),
  `op3_two_probe_fourier_bridge_2026_11_14.md`. Keine iterierte Auslese am Punkt größter Annäherung.
- Atlas-Lesart HS(1) „Periapsis-Aufspaltung“, HS(2) „stabilisierter Orbit“ (v470/32). Das ist eine Benennung, keine Rechnung.
- H159 (k350): Ellipse aus zwei gegenläufigen Kreisanteilen, Kreis bei b = 0.
- Suche nach „Periapsis“, „Kepler“ unter `notes/research`, `wiki`, `analysis` (26.11.): nur die Benennungen oben.

## Modell (gesetzt)
Ebene, Kern als Punktmasse im Ursprung, Newton, GM = 1. Zustand: zwei Auslesepunkte P₁, P₂.
- **Start:** zwei Proben auf parallelen Strahlen mit Stoßparametern +b₁ und −b₂ (zu beiden Seiten am Kern vorbei), Geschwindigkeit v∞ im Unendlichen. P₁, P₂ sind
  ihre Punkte größter Annäherung. Gleichzeitig dort sind sie nur für b₁ = b₂; für b₁ ≠ b₂ wird jede Probe an ihrem eigenen Punkt angehalten.
- **Schritt:** Von P_i startet eine Probe in Richtung P_j (gerade Zielrichtung). P_i′ ist der Punkt größter Annäherung auf ihrer künftigen Bahn. Zeigt der Start
  nach außen und ist die Bahn ungebunden, ist P_i′ = P_i.
- **Startgeschwindigkeit, drei Regeln:** E (Energie der ursprünglichen Probe bleibt, v² = v∞² + 2/r), V (feste Geschwindigkeit v₀), B (gebunden, feste Energie −1/(2a)).
- **Gitter (vorab):** Regel E: b₁ ∈ {0,5; 1; 2; 4}, b₂/b₁ ∈ {1; 1,1; 1,5; 2}, v∞ ∈ {0,5; 1; 2}. Regel V: dieselben Starts, v₀ ∈ {0,5; 1; 2}. Regel B: 200 Zufallsstarts
  (Radien in [0,5; 3], Winkel beliebig, a ∈ {1; 2}, Startwert des Zufallsgenerators 20261126). Je 400 Schritte.
- **Einteilung eines Laufs:** „Kollaps“ (ein Radius unter 10⁻⁹), „konvergent“ (Radien und Lagen ändern sich zuletzt um weniger als 10⁻⁹, r∞ > 0), sonst „anderes“.

## Hypothese H160
Die Folge der Auslesepunkte läuft auf einen festen Radius r∞ > 0 zu, die dort gestarteten Bahnen sind Kreisbahnen, und dieser Zustand zieht benachbarte an.

## Entscheidungskriterien
- **K-a (Konvergenz):** Anteil der Läufe „konvergent“ je Regel. Mindestens 90 % in allen drei Regeln: bestätigt. Mehrheit „Kollaps“ in mindestens einer Regel und
  Mehrheit „konvergent“ in mindestens einer anderen: trägt teilweise. Mehrheit „Kollaps“ oder „anderes“ in allen: widerlegt.
- **K-b (Kreisbahn):** Exzentrizität e∞ der zuletzt gestarteten Bahnen. e∞ < 10⁻³ in mindestens 90 % der konvergenten Läufe (Regeln V und B): bestätigt. Streut e∞
  über ein Intervall und ist null nur auf einem Rand: widerlegt.
- **K-c (Anziehung):** Den Endzustand eines konvergenten Laufs radial um 10⁻³ versetzen und weiter iterieren. Kehrt r zum alten r∞ zurück (Abweichung fällt unter
  10⁻⁶): bestätigt. Bleibt der neue Wert stehen (Kontinuum von Endzuständen): widerlegt.
- **Gesamturteil:** bestätigt nur, wenn K-a, K-b und K-c bestätigt sind. „Trägt teilweise“, wenn K-a mindestens teilweise trägt und K-b oder K-c scheitert.

## Ohne Kriterium (Erkundung)
- Schwarzschild-Variante: Bahngleichung u″ + u = 1/L² + 3·m·u² mit m = GM/c² ∈ {0,01; 0,05}, L = v·(Abstand der Ziellinie vom Kern); Einfang zählt als Kollaps.
- Harter Kern mit Radius R = 0,5: trifft die Bahn die Oberfläche, ist der Auftreffpunkt die Auslese.
- Die „addierten Auslesen“: Menge aller Auslesepunkte eines Laufs, ihr Radiusbereich und der überstrichene Winkel.

## Vorab offengelegt (kein Teil der Vorhersage)
Überschlag beim Aufschreiben (im Kopf, ungeprüft):
- Der Punkt größter Annäherung liegt nie weiter außen als der Startpunkt. Die Radien fallen also monoton oder bleiben stehen, eine Grenze existiert immer.
- Ein Fixpunkt mit r∞ > 0 verlangt tangentialen Start. Die Ziellinie zwischen zwei verschiedenen Punkten kann nicht auf beiden Radien senkrecht stehen. Die Punkte
  müssten also zusammenlaufen, oder der Lauf kollabiert. Was davon geschieht, weiß ich nicht.
- Regel E hat nur Hyperbeln (e > 1), dort gibt es keine Kreisbahn. Regel V: Kreis nur bei r∞ = 1/v₀², darunter fällt der Radius weiter. Regel B: e∞ = 1 − r∞/a.
- Nach dem Zusammenlaufen starten beide Proben am selben Punkt gegenläufig. Das wären zwei gegensinnig durchlaufene Bahnen derselben Form.

## Vorhersage
- K-a: **trägt teilweise** (offen, welcher Anteil kollabiert).
- K-b: **widerlegt** (e∞ streut, Kreis nur am Rand).
- K-c: **widerlegt** (Kontinuum von Endzuständen, keine Anziehung).
- Gesamt: **trägt teilweise**. Offen vor der Rechnung: ob die Punkte wirklich zusammenlaufen, die Anteile, die Verteilung von e∞, das Verhalten der
  Schwarzschild-Variante und des harten Kerns.

## Grenzen (vorab)
Das Modell ist eine Übersetzung des Gedankenexperiments, nicht die einzige: gerade Zielrichtung, Punktmasse, drei Geschwindigkeitsregeln. Klassische Bahnen, keine
Wellen, keine Größe des Companion geht ein. Die Schwarzschild-Variante benutzt die flache Zielgeometrie in Schwarzschild-Koordinaten (Setzung). OP1 bis OP5 bleiben offen.
