# OP3: Der bewachte Kern schließt Fluss aus, statt ihn zu tragen

15. November 2026, Claude Opus. **Erkundung, nicht blind**: Zielwert 2/3 und γ_M waren bekannt. Idee des Autors:
„muss er den fluss wirklich tragen? was ist wenn er einen fluss nur ausschließt und sich deswegen der ganz andere raum
als flussträger verhält … könnte beim verschieben des kerns von außen nach innen passieren.“ Keine H-Nummer, kein
CT-Eintrag, Guards unverändert. Einordnung T5/T8, OP3; Bezug zu CT-001/CT-002 und H102.

## Vorwissen geprüft
- v470/05: Orbit-Scan mit bewachtem Kern, X = S³ ∖ B_ε(K), Prop. „Hopf completion versus guarded-core remainder“,
  Radius ε frei. v470/14 und v470/15: Julia-Rand als holographische, nur diagnostische Auslesung. Mit OP3 war das
  bisher nicht verbunden (Volltextsuche in den Notizen: kein Treffer).
- `../op3_cs_dixon_map_2026_11_15/README.md`, Nachtrag „gebogene Achsen“: det G = (√2 cos φ − 1)/2; geladene
  Leptonen bei φ = 2/3, flacher Oktant bei π/4.
- CT-001 Schritt 1 (ΔΦ als äußerer Fluss), CT-002 (eine Querung), Vorab-Notiz H102 (Φ_e = π/4 − γ_M/2).

## Aufbau
Spin-½-Berry-Phase auf der Bloch-Kugel: Flussdichte ½ pro Steradiant, Gesamtfluss 2π (Chern-Zahl fest). Der Kern ist
eine Kappe mit Raumwinkel Ω = γ_M, in der kein Fluss ist. Die Kappe wandert auf einem Großkreis von außerhalb des
Oktanten bis zur Zyklusachse (1, 1, 1)/√3. Für den verdrängten Fluss werden zwei Fälle verglichen:
- **A:** Der verdrängte Fluss verlässt das Dreieck ganz, etwa über den Rand der ausgeschnittenen Kugel im S³.
- **B:** Er verteilt sich gleichmäßig auf den Rest der Kugel. Das ist auf einer Fläche das Minimum der Feldenergie.

`core_shift.py`, Monte-Carlo mit 2·10⁶ Punkten, Ausgabe `run/core_shift.json`.

## Ergebnis
1. **Der Kern muss keinen Fluss tragen. Ausschließen reicht, und das Vorzeichen stimmt von selbst.**
   - Liegt der Kern ganz im Dreieck, sinkt die Phase unter π/4. Die Achsen biegen also in die richtige Richtung, in
     den dreidimensionalen Raum mit drei positiven Massen.
   - Liegt er außerhalb, bleibt die Phase bei π/4 (A) oder steigt darüber (B). Über π/4 ist mit Überlappung ½
     unmöglich, denn dann wäre det G < 0. Koide müsste dann brechen.

   Damit ist Stelle 3 aus der Bilanz („warum abziehen statt addieren“) geometrisch beantwortet: durch die Lage.
2. **Die genaue Lage im Innern spielt keine Rolle.** Sobald die Kappe ganz im Dreieck liegt (Mitte näher als etwa
   19° an der Zyklusachse), ist die Phase konstant. Der Kern muss also nicht genau auf der Zyklusachse sitzen.
3. **Die Menge hängt davon ab, wohin der Fluss ausweicht:**
   - **A:** φ = π/4 − γ_M/2 = 0,666632, genau die Beziehung von H102; der Zielwert 2/3 wird bis auf 3,5·10⁻⁵ getroffen.
   - **B:** φ = 0,679475 und damit deutlich daneben. B träfe 2/3 erst bei Ω = 0,265649 sr = 1,118 γ_M.

## Lesart und Grenzen
- Die Idee des Autors ersetzt „Kern trägt einen Fluss“ durch „Kern verdrängt Fluss“. Das macht den Gegenterm
  natürlicher: Die Chern-Zahl bleibt fest, und das Vorzeichen kommt aus der Lage. H102 entspricht dem Fall, in dem
  der verdrängte Fluss das Dreieck verlässt. Im Bild von v470/05 liegt das nahe, denn S³ ∖ B_ε(K) hat einen Rand, über
  den der Fluss gehen kann. Gezeigt ist das nicht.
- **Offen:**
  - warum der Fluss das Dreieck verlässt (A) und sich nicht verteilt (B);
  - warum der Raumwinkel gerade γ_M ist;
  - wie der Kern als Kugel B_ε(K) im S³ mit einer Kappe auf S² zusammenhängt. Das Urbild einer Kappe ist ein Volltorus
    aus Fasern, keine Kugel.
- Nichts hiervon ist hergeleitet. Die Rechnung ändert H102 nicht; H102 ist eingefroren. Eine Herleitung von A mit Ω =
  γ_M wäre eine neue Hypothese.

OP1–OP5, C5, C6/T2 und Guards unverändert. I1 berührt (Brücke zum Horizont): Der bewachte Kollapskern wäre ein Ort für
die Punktierung im Hopf-Raum. Dem Autor genannt, nicht umgesetzt.

## Nachtrag: Fläche zwischen den Kurven A und B (Frage des Autors)

`area_between.py`, Ausgabe `run/area_between_stdout.txt`. Die Kurven sehen fast gleich aus, weil sie **exakt
proportional** sind. Mit der Restfläche A_rest = π/2 − f·Ω des Dreiecks gilt φ_A = A_rest/2 und
φ_B = A_rest · 2π/(4π − Ω), also an jeder Stelle

  φ_B/φ_A = 4π/(4π − γ_M) = 1,019266 (numerisch längs des Wegs 1,019265 bis 1,019267).

Daraus folgt:
- **Nur der Fluss unterscheidet A und B.** Die Fläche zwischen den Kurven (0,01722) ist genau 1,93 % der Fläche
  unter A. Form, Lage und Größe des Kerns wirken in beiden Fällen gleich; es zählt nur, ob Fluss abfließt.
- **Das Verhältnis misst den Abfluss.** 1 − φ_A/φ_B = γ_M/(4π) = 0,018902. In A verliert die Kugel genau den Anteil
  des Kerns am Gesamtfluss.
- **Die Rampe liest den Kern von außen aus,** wie es der Orbit-Scan in v470/05 vorsieht. Ihre Breite ist der
  Kappendurchmesser 2α = 31,6° (im Raster 28,2° + 3,5°). Ihre Höhe ist der verdrängte Fluss: γ_M/2 in A, k·γ_M in B.
  Höhe durch Kappenfläche ergibt die Flussdichte, ½ in A, k ≈ 0,51 in B, und unterscheidet damit beide Fälle.
- **Entartung.** Die Daten (φ = 2/3) legen nur eine Kombination aus Kerngröße und Abfluss-Anteil λ fest:

  | λ (Anteil, der abfließt) | 1 | 0,75 | 0,5 | 0,25 | 0 |
  |---|---|---|---|---|---|
  | nötiger Raumwinkel Ω / γ_M | 0,9997 | 1,0274 | 1,0563 | 1,0866 | 1,1184 |

  Ω = γ_M ist der Punkt λ = 1 auf dieser Linie. Wer γ_M herleiten will, muss auch begründen, dass der verdrängte Fluss
  ganz abfließt. Beides zusammen ist eine einzige Bedingung, keine zwei unabhängigen Treffer.

## Faden 1 (15.11.): Warum fließt der verdrängte Fluss ganz ab?

Erkundung, analytisch, mit Quellenabgleich. Gelesen wurden v470/05 (Einleitung und Prop. „Hopf completion versus
guarded-core remainder“), v470/32, Zeile 446 (OP5-Route) und v470/10, Abschnitt „Black Holes and Hawking Radiation“.

**Topologischer Kern.** Auf einer geschlossenen Kugel ist der Gesamtfluss eines U(1)-Bündels quantisiert (Chern-Zahl).
Was eine Kappe nicht enthält, muss dann auf den Rest der Kugel; das ist B, gleichmäßig als Minimum der Feldenergie.
Wird die Kappe dagegen wirklich *entfernt*, hat die Fläche einen Rand, und kein Erhaltungssatz zwingt den Fluss zurück.
Ohne eine eigene Dynamik, die ihn umverteilt, ist das A (λ = 1).

**Das Paper hat genau diese Zweiteilung offen gelassen.** Prop. „Hopf completion versus guarded-core remainder“ (b)
sagt: „the core K is removed **or** shielded.“

| Lesart in v470/05 | Topologie | Fluss | Ergebnis |
|---|---|---|---|
| removed: X = S³ ∖ B_ε(K) | Fläche mit Rand, Chern-Zahl nicht fest | fließt über den Rand ab | A, φ = π/4 − Ω/2 |
| shielded | geschlossene Kugel, Chern-Zahl fest | verteilt sich um | B, φ = 0,6795 bei Ω = γ_M |

**Was im Paper für „removed“ spricht (Lesart, nicht Herleitung):**
- v470/05 schreibt das Scan-Gebiet ausdrücklich als S³ ∖ B_ε(K): Der Kern gehört nicht zum Auslesegebiet und wird nur
  von außen gemessen.
- v470/32, Zeile 446: Auf der OP5-Route soll gezeigt werden, dass kein zulässiger Zweig den Kollapskern kreuzt; jeder
  hat einen Umkehrpunkt.
- v470/10, Prop. „Horizon as cascade singularity“: Die Sphaera kann nicht über ihren eigenen Horizont hinaus
  projizieren; der Horizont ist die Grenze ihres Zuständigkeitsbereichs. Was jenseits liegt, wird nicht ausgelesen und
  auch nicht in den Rest zurückgeschoben.

**Befund.**
- A ist die Lesart „removed“, B die Lesart „shielded“. Die Daten verlangen „removed“. Das Paper hat diese Lesart schon
  angelegt und stützt sie an drei Stellen, ohne sie zu erzwingen.
- Damit ist λ = 1 kein freier Parameter mehr, sondern eine Lesartwahl, die das Paper an zwei der drei Stellen ohnehin
  nahelegt.
- **Offen bleibt Ω = γ_M:** warum der entfernte Kern auf der Generationskugel gerade den Raumwinkel eines Flächenquants
  der Zählregel hat. Das ist weiter dieselbe Lücke wie bei CT-002, die Brücke zwischen Horizont-Punktierung und
  Generationsraum.
- Dass der Kollapskern ein Horizont ist, steht so im Paper nicht. Die Gleichsetzung ist Lesart.

## Faden 2 (15.11.): Liegt der Kern nur bei geladenen Teilchen im Dreieck? Berichtigung

**Berichtigung einer Aussage im Gespräch.** Die Ausgangsidee lautete, die Neutrinos lägen nach H99 genau auf dem
Oktanten (flach, leichtestes Neutrino masselos), und Ladung lege den Kern ins Dreieck. Das stimmt nicht. Nach der
Vorab-Notiz H99 gilt θ_ν = θ_e + π/12 je Generation, also φ_ν = φ_e + π/4, mit **negativer** leichtester Wurzel
(Kontrolle 3 dort). In H2 ist das leichteste Neutrino 0,36 meV schwer, nicht masselos.

**Richtiges Bild** (`neutrino_phase.py`, Erkundung, nicht blind):

| Sektor | φ | det G | Raumwinkel 2φ |
|---|---|---|---|
| geladene Leptonen (aus Polmassen) | 0,666665 | +0,0557, definit | π/2 − 0,23747 (Oktant minus Kern) |
| Oktant | π/4 | 0, Rand | π/2 |
| Neutrinos nach H99 | 1,452063 | −0,4162, indefinit | π − 0,23747 (90°-Mond minus Kern) |

- **Der Kern ist in beiden Sektoren gleich.** Beide Raumwinkel fehlen um denselben Betrag 0,23747 ≈ γ_M. Gelten H99 und
  H102 zugleich, schneidet derselbe Kern aus beiden Figuren aus.
- **Der Unterschied ist die Größe der Figur, nicht der Kern.** Die geladenen Leptonen umschließen einen Oktanten (π/2),
  die Neutrinos zwei Oktanten (einen Mond von 90°, π). Das zusätzliche Oktant schiebt die Neutrinos über den Rand in das
  indefinite Gebiet, also eine negative Wurzel. Das passt zur indefiniten Form, die nur im neutralen Sektor existiert
  (`../op3_indefinite_form_2026_11_13.md`).
- Die Idee „Ladung legt den Kern ins Dreieck“ ist damit **verworfen**. Tragfähiger wäre: Ladung bestimmt, ob die Figur ein
  oder zwei Oktanten umfasst. Das ist eine Umformulierung von H99, keine neue Vorhersage. Warum der neutrale Sektor das
  doppelte Oktant sieht, ist nicht hergeleitet.
- Keine neue Hypothese. Neue Zahlen ergeben sich nicht; H99, H100 und H102 bleiben unverändert.

## Faden 3 (15.11.): Kugel B_ε(K) im S³ gegen Faser-Volltorus

`ball_vs_torus.py`, Ausgabe `run/ball_vs_torus_stdout.txt`. Analytisch, mit Quadratur und Monte-Carlo-Gegenprobe
(4·10⁵ Punkte).

**Was die Kugel aus v470/05 tut.**
- Sie entfernt für ε < π keine einzige Faser ganz. Sie schneidet aber jede Faser an, deren Basispunkt näher als 2ε am
  Bild von K liegt; die Hopf-Abbildung verdoppelt den Winkel (Monte Carlo: 34,28° gegen 2ε = 34,38° bei ε = 0,3).
- Der abgeschnittene Anteil einer Faser ist f(θ) = arccos(cos ε / cos(θ/2))/π, am Mittelpunkt ε/π.
- Auf der Basis fehlt also kein Punkt. Über der Kappe sind die Fasern aber keine Kreise mehr, sondern Bögen. Dort
  bricht die U(1)-Struktur, und die Chern-Zahl bindet den Fluss nicht mehr. Das passt zu „removed“ (Faden 1), nur mit
  weichem Rand statt scharfer Kappe.

**Zwei Lesarten für den verlorenen Fluss:**

| Lesart | Regel | ε für Raumwinkel γ_M | Rand |
|---|---|---|---|
| binär | Eine angeschnittene Faser ist kein geschlossener Kreis mehr und hat keine Holonomie | 0,137922 rad = 7,90° | scharf, Kappe 2ε |
| gewichtet | Fluss geht anteilig zum abgeschnittenen Faserstück verloren | 0,452751 rad = 25,94° | weich |

- **Binär** ist für eine Phase die natürlichere Lesart: Holonomie braucht einen geschlossenen Umlauf. Sie gibt genau
  das Kappenmodell der Hauptrechnung.
- **Gewichtet** führt zu einer runden Aussage: Der Kern nimmt den Anteil γ_M/(4π) = 0,018902 des Hopf-Raums S³ ein,
  also das Volumen (π/2)·γ_M. Das ist derselbe Abfluss-Anteil wie im Nachtrag zur Fläche zwischen A und B.

**Befund.** Die Kugel des Papers und die Kappe der Rechnung widersprechen sich nicht. Die Kugel bricht die Fasern
über einer Kappe vom Radius 2ε und hebt damit die Flusserhaltung auf. ε selbst ist im Paper frei, und keine der beiden
Lesarten legt es fest. Wer γ_M herleiten will, muss jetzt eine von drei gleichwertigen Formen begründen: Raumwinkel γ_M
auf der Generationskugel (binär, ε = 7,90°), Volumenanteil γ_M/(4π) im S³ (gewichtet, ε = 25,94°) oder Abfluss-Anteil
γ_M/(4π) des Gesamtflusses.

## Schritt 1 der Lückensuche (15.11.): Beschreibt die Zählregel den Kern im S³?

Analytisch, mit Quellenabgleich. Gelesen wurden `../ct002_gamma_angle_2026_11_14.py` mit Ausgabe, CT-001 Schritt 2 und 3
sowie die Fundstellen zu isolierten Horizonten im Paper (v480, Zeile 250: Zählung nach Corichi und Krasnov; v4100,
Zeile 1157: erster Hauptsatz nach Frodden, Ghosh und Perez).

- **Was die Zählregel ist:** Σ_j 2·exp(−2πγ a(j)) = 1 mit a(j) = √(j(j+1)), über alle Spins. Sie normiert
  Boltzmann-Gewichte e^{−A_j/4} von Punktierungsflächen. In der Sektorlesart (CT-001) ist sie eine Gleichung für einen
  Öffnungswinkel θ = γ_M in der Ebene einer Punktierung. Ein Sektor mit Öffnungswinkel γ und Radius 1 hat die Fläche γ/2.
- **Gegen die Kugel im S³:** Die Zählregel enthält keine Geometrie des Hopf-Raums. Weder der Volumenanteil
  (2ε − sin 2ε)/(2π) noch der Kappen-Raumwinkel 2π(1 − cos 2ε) hat in ihr ein Gegenstück. Beide gleich γ/(4π) bzw. γ
  zu setzen, formuliert die Lücke nur um. **Eine Herleitung ergibt sich hier nicht.**
- **Was übereinstimmt, und warum es nichts beweist:** Die normierte Sektorfläche γ/2 (CT-001) und die Berry-Phase einer
  Kappe mit Raumwinkel γ (Spin ½: Phase = Raumwinkel/2) sind dieselbe Zahl. Das liegt am Faktor ½ beider Lesarten,
  nicht an einer Abbildung. Gesucht bleibt eine Abbildung, die den Punktierungssektor in der Horizontebene auf die
  Kernkappe der Generationskugel bringt.
- **Spur außerhalb des Papers** (aus Vorwissen, ungeprüft, kein Literaturwerkzeug benutzt): In der Literatur zu
  quantisierten isolierten Horizonten ist der Horizont eine Zwei-Sphäre mit U(1)-Zusammenhang, dessen Krümmung in den
  Punktierungen sitzt. Das ist dasselbe Objekt wie unsere Generationskugel mit Kern. Dort hängt der Fluss einer
  Punktierung aber nach meiner Erinnerung von der Horizontfläche ab. Ein fester Winkel γ bräuchte dann eine zusätzliche
  Skalenbedingung. Der Companion enthält diese Geometrie nicht, nur die Zählung.

**Befund Schritt 1:** Die Zählregel bindet den Kern nicht. Sie liefert γ_M als Winkel nur in der Ebene einer
Punktierung, nicht im Generationsraum. Die Lücke ist damit genau benannt: eine Abbildung Punktierungsebene →
Generationskugel. Die nächstliegende Quelle, die Geometrie isolierter Horizonte, steht nicht im Companion und müsste
erst mit Literatur geprüft werden.

## Literaturprüfung (15.11.): Geometrie quantisierter isolierter Horizonte

Auf „Erst Literatur prüfen“ des Autors. Gelesen über alphaXiv: Ashtekar, Baez und Krasnov, „Quantum Geometry of
Isolated Horizons and Black Hole Entropy“, arXiv:gr-qc/0005126 (ABK), sowie Engle, Noui und Perez, „Black hole
entropy and SU(2) Chern-Simons theory“, arXiv:0905.3168 (ENP). Damit sind die ungeprüften Angaben aus Schritt 1 geprüft.

**Bestätigt.**
- **ABK:** Der Horizont ist eine punktierte Zwei-Sphäre mit U(1)-Chern-Simons-Zusammenhang. Er ist überall flach
  außer in den Punktierungen. Die Holonomie um Punktierung i ist exp(2πi a_i/k) mit dem Level k = a₀/(4πγℓ_P²)
  (Gl. 15). Der Winkeldefekt des Levi-Civita-Zusammenhangs ist 4π a_i/k; die Defekte summieren sich modulo 4π zu
  null, als Quantenfassung von Gauß-Bonnet. Die Zuordnung zum Volumenzustand ist 2m_i = −a_i mod k.
- **ENP (SU(2)):** Die Kopplung der Defekte ist 16π²β(1 − β²)ℓ_P²√(j(j+1))/a_H, nach den Autoren das Verhältnis
  des Flächenquants des Defekts zur gesamten Horizontfläche.

**Folgerungen für den Kern.**
1. **Gleiche Struktur.** Eine Sphäre mit U(1)-Zusammenhang, dessen Krümmung in Punktierungen sitzt, ist dasselbe
   Objekt wie unsere Generationskugel mit Kern. Spin ½ passt: Die Spinor-Holonomie 2π a/k ist die Hälfte des Defekts
   4π a/k, wie unsere Phase γ/2 zum Raumwinkel γ.
2. **Aber im Horizontbild *trägt* die Punktierung die Krümmung.** Dort ist die Fläche überall sonst flach, und die
   Defekte addieren sich zu 4π. Das ist das Gegenteil unseres Bildes, in dem die Krümmung gleichmäßig verteilt ist und
   der Kern sie ausschließt. Die Analogie ist also nur teilweise.
3. **Der Defekt hängt von der Horizontfläche ab.** Eine minimale Punktierung (|m| = ½, a = 1) hat den Defekt
   4π/k = 16π²γℓ_P²/a₀. Ein Defekt genau γ verlangt a₀ = 16π² ℓ_P² ≈ 157,9 ℓ_P², unabhängig von γ, und damit den
   Level k = 4π/γ_M = 52,90. Der muss aber ganzzahlig sein (Präquantisierung). Das nächste Level, k = 53, gibt
   γ = 0,237101, also 4,3·10⁻⁴ unter γ_M. Die verlangte Genauigkeit liegt bei etwa 4·10⁻⁵, das schließt es aus.
4. Defekt und Fläche einer Punktierung skalieren verschieden: der Defekt mit |m|, die Fläche mit √(j(j+1)). Für
   j = ½ ist das Verhältnis 1/√3.

**Befund.** Die Horizontgeometrie liefert keinen festen Winkel γ_M für einen Kern, weder aus einer Punktierung (der
Defekt hängt von a₀ ab, und k = 4π/γ_M ist nicht ganzzahlig) noch begrifflich (dort trägt die Punktierung die
Krümmung). Diese Spur ist damit geprüft und **trägt nicht**. Der Companion zitiert die Zählung (v480, Zeile 250), nicht
diese Geometrie. Es wird nichts davon übernommen.

## Schritt 2 (15.11.): Warum genau ein Kern? Topologie, mit Berichtigung zu Faden 1

`core_count.py`, Ausgabe `run/core_count_stdout.txt`. Phasenbuchhaltung über Holonomien, Erkundung, nicht blind.
Vorwissen: Ein Grund für „genau eine Querung“ (CT-002) wurde in `../op3_i1_string_bridge_2026_11_14.md` und
`../op3_ct002_t11_shift_2026_11_14.md` gesucht, nicht gefunden. Ein topologischer Ansatz war nicht darunter.

**Grundtatsache.** Eine Holonomie hängt nur vom Zusammenhang *auf* der Schleife ab. Die Kugel ohne n Kappen hat
n − 1 unabhängige Schleifen um Löcher, also n − 1 freie Aharonov-Bohm-Holonomien (für n = 1 ist der Rest eine Scheibe
und einfach zusammenhängend).

| Zahl der Kerne | Rest | freie Parameter | Biegung |
|---|---|---|---|
| 0 | geschlossene Kugel | keiner, Gesamtfluss 2π fest | keine; Oktant starr bei π/4 |
| 1 | Scheibe | keiner | möglich, aber festgelegt durch die Lage des verdrängten Flusses |
| 2 | Ring | eine Holonomie t | φ = π/4 − γ_M/2 + t, beliebig verschiebbar |
| n | Scheibe mit n − 1 Löchern | n − 1 | frei |

**Befund 1, genau ein Kern ist ausgezeichnet.** Es ist die einzige Zahl, die überhaupt Biegung erlaubt und dabei keinen
freien Parameter einführt. Null Kerne biegen nicht, ab zwei Kernen ist die Phase eine freie Zahl und sagt nichts mehr
vorher. Das ist ein topologischer Grund für die „eine Querung“ von CT-002: Sie ist die einzige vorhersagefähige Zahl.
Hergeleitet ist damit nicht, dass es *überhaupt* einen Kern gibt; das verlangen die Daten (Biegung).

**Befund 2, Berichtigung zu Faden 1.** Dort stand, bei „removed“ fließe der Fluss über den Rand ab, weil keine
Chern-Zahl ihn binde. Für genau einen Kern ist das ungenau. Der Rest ist einfach zusammenhängend, der Fluss kann nicht
entweichen, und die Holonomie um das Loch ist durch den Rest festgelegt. Die Rechnung zeigt:
- Nur ausschneiden, mit unverändertem Zusammenhang, ändert nichts: φ = π/4.
- Ein flussfreier Kern verdrängt Fluss, der auf der Kugel bleibt. Entscheidend ist, wohin er geht:
  - ins Dreieck: φ = π/4, keine Biegung;
  - gleichmäßig verteilt (B): φ = 0,679475;
  - ganz außerhalb des Dreiecks, etwa am Gegenpol (A): φ = 0,666632, die H102-Beziehung.

A heißt also richtig: **Der Kern ist flussfrei, und der verdrängte Fluss sitzt außerhalb des Dreiecks**, zum Beispiel
am Gegenpol des Kerns. Der Gesamtfluss 2π bleibt dabei erhalten. Das passt zu einem Dirac-Faden vom Kern durch die
Kugel zum Gegenpol. Die Lesart „removed“ aus Faden 1 bleibt als Stütze für einen flussfreien Kern, aber nicht für ein
„Abfließen“.

**Was offen bleibt:** warum der verdrängte Fluss zum Gegenpol geht und sich nicht gleichmäßig verteilt (B wäre das
Energieminimum), und warum der Kern die Größe γ_M hat.
