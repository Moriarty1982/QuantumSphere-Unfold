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
