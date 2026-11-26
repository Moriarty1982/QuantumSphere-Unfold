# Ergebnis H163: Für die Kreisbahn braucht es bei Newton die doppelte Schwerkraft; einen kleinsten Abstand gibt es erst relativistisch, bei 4m

**Stand:** 2026-11-26. Vorab-Notiz: `notes/research/predictions/Vorab_Notiz_H163_Minimalpunkte_Kreisbahn_Kraft.md` (Commit e0a3fd2, vor dem ersten Lauf).
**Überwiegend nicht blind** (Lehrbuchwissen, in der Vorab-Notiz offengelegt). Skripte: `k354_test_h163.py` (numpy/scipy), `k354b_gegenprobe.wl` (Wolfram, exakt und
NDSolve). Ausgaben: `k354_out.txt`, `k354b_out.txt`. Kein Qiskit (keine Schaltung), kein HDL/MMA-Vergleich (kein RUN_TAPE-Ablauf). Kein Guard berührt.
H163 ersetzt die Auslegung von H160: Dort waren die neuen Proben aufeinander gezielt, das war nicht gemeint (Richtigstellung des Autors, 26.11.2026, 09:57 UTC).

## Frage
Die Punkte größter Annäherung werden zu neuen Startpunkten, deren Spuren wieder am Kern vorbeigehen; die Bahn wird kürzer und sollte dem kleinsten möglichen
Abstand entsprechen. Welche Kraft macht daraus eine Kreisbahn? Was geschieht, wenn die Proben Schwung holen: geschlossene Bahn oder parabolische Flucht?

## Urteil nach den vorab festgelegten Kriterien
| Kriterium | Vorhersage | Ergebnis |
|---|---|---|
| K-a kleinster Abstand r_min > 0 (Newton) | widerlegt | **widerlegt** |
| K-b Kraft für die Kreisbahn (Newton) | bestätigt | **bestätigt** |
| K-c Schwung holen (Newton) | bestätigt | **bestätigt** |
| K-d kleinster Abstand ohne nötige Kraft (Schwarzschild) | bestätigt | **bestätigt** |
| Gesamt | trägt teilweise | **trägt teilweise** |

## Befunde
1. **Kein kleinster Abstand bei Newton (K-a).** Startet die Probe am Auslesepunkt mit ihrer dortigen Geschwindigkeit (Auslegung T), ist es dieselbe Bahn; der Punkt
   bleibt stehen, nichts wird kürzer (18 Fälle, Abweichung 10⁻¹⁶). Der Auslesepunkt selbst kann beliebig nah am Kern liegen: r_p = (√(1 + b²v∞⁴) − 1)/v∞² geht
   mit dem Stoßparameter b gegen null. Stellt man die Richtung auf die ursprüngliche Einflugrichtung zurück (Auslegung P), fliegt die Probe vom Auslesepunkt weg
   nach außen. Nur wenn man die ganze Spur nimmt (auch rückwärts), entsteht eine kürzer werdende Folge mit b′ = r_p·√(1 − 1/e²), und die fällt gegen null
   (z. B. 0,41; 0,042; 7·10⁻⁵; 3·10⁻¹³). Das Newton-Feld einer Punktmasse kennt keine Länge, an der etwas stehen bleiben könnte.
   *Beim Umsetzen gefunden, nach der Vorab-Notiz:* Dass P vorwärts nach außen läuft, stand nicht in der Vorab-Notiz; am Urteil ändert es nichts.
2. **Die Kraft für die Kreisbahn (K-b).** Am Auslesepunkt ist die Probe zu schnell für einen Kreis: v_p/v_c = √(2 + v∞²·r_p). Zwei gleichwertige Antworten:
   - ein Bremsstoß entlang der Bahn von v_p auf v_c, abzugebende Energie (1 + v∞²·r_p)/(2r_p);
   - eine dauernde zusätzliche Anziehung zum Kern von (1 + v∞²·r_p)-facher Schwerkraft, sodass insgesamt das (2 + v∞²·r_p)-Fache wirkt.
   In 21 Fällen ist die integrierte Bahn danach ein Kreis (Radiusschwankung unter 10⁻¹² über fünf Umläufe).
   **Für Einfall aus der Ruhe (Parabel) ist es genau das Doppelte der Schwerkraft**, das Geschwindigkeitsverhältnis genau √2, und die abzugebende Energie ist
   genau die Bindungsenergie 1/(2r) der Kreisbahn. Diese Zahlen hängen nicht vom Radius ab.
3. **Schwung holen (K-c).** Von der Kreisbahn mit k-facher Geschwindigkeit: für k < √2 eine geschlossene Ellipse mit fernstem Punkt r·k²/(2 − k²) (k = 1,1: 1,53r;
   1,3: 5,45r; 1,4: 49r), die nach einem Umlauf auf 10⁻⁹ schließt; bei k = √2 die Parabel; darüber die Hyperbel. Die Schwelle ist derselbe Stoß wie in Befund 2,
   rückwärts: Was der Einfang abgibt, braucht die Flucht. Geschlossene Bahn und Parabel sind eine Familie mit einem Parameter, und √2 ist die Grenze.
4. **Mit der relativistischen Bahngleichung gibt es den kleinsten Abstand (K-d).** In der Schwarzschild-Geometrie (m = GM/c²) ist das Verhältnis
   L²(Einfall aus der Ruhe mit nächstem Punkt r)/L²(Kreisbahn bei r) = 2(r − 3m)/(r − 2m). Weit draußen ist es 2 (Newton, Befund 2), bei **r = 4m ist es 1**: Dort
   ist die ankommende Probe schon auf der Kreisbahn, ohne jede Zusatzkraft (Wolfram exakt: E = 1, L = 4m, V_eff′ = 0). Näher kommt keine Probe heran, die wieder
   entkommt. Für schnellere Proben liegt der Radius zwischen 3m und 4m (E = 1,1: 3,571m; 1,5: 3,2m; 3: 3,04m), für Licht bei 3m (Stoßparameter 3√3·m).
   Numerisch: Knapp über dem kritischen Drehimpuls umrundet die Probe den Kern immer öfter (bei relativem Abstand 10⁻⁸: 3,4 bis 4,9 Umläufe, je Faktor 100 etwa ein
   Umlauf mehr) und entkommt; knapp darunter fällt sie hinein. Der innerste Punkt geht gegen r(E) (E = 1: 4,6532m; 4,0574m; 4,0057m; 4,0006m).
   Bei Newton gibt es diese Grenze nicht: Jede Probe mit Drehimpuls entkommt.
5. **Diese Kreisbahn ist ein Grat, kein Tal (Erkundung).** Die Bahn bei 4m ist instabil (V_eff″ = −1/(16m²)). Ein Stoß nach außen um 10⁻⁶ lässt die Probe nach 3,5
   Umläufen entkommen, mit E knapp über 1, im Grenzfall also auf der Parabel; ein Stoß nach innen lässt sie nach 3,2 Umläufen hineinfallen. Stabile Kreisbahnen
   gibt es erst ab 6m. Dort führt Schwungholen auf gebundene Bahnen, die nicht schließen, sondern sich drehen (bei 400m: 2,47° je Umlauf, Näherung 2,45°; bei 20m: 61°).
6. **Addierte Auslesen (Erkundung).** Die zwei Proben laufen gegensinnig um. Die Summe ihrer Orte ist z(t) = r₁·e^{iω₁t} + r₂·e^{−iω₂t}. Bei gleichen Radien ist das
   exakt eine Strecke durch den Kern, 2r·cos(ωt): die Form der Schattenellipse am Photonpunkt P (μ = 1, H159). Bei ungleichen Radien ist es eine Ellipse mit
   μ = kleinerer/größerer Radius, deren Achse sich dreht, weil die zwei Kreise nach Kepler verschieden schnell laufen; über lange Zeit füllt die Spur den Ring
   zwischen |r₁ − r₂| und r₁ + r₂. Die Zuordnung zur Schattenellipse ist eine Lesart, keine Herleitung: In H159 haben beide Kreisanteile dieselbe Drehrate.

## Antwort auf die drei Fragen
- **Kleinster möglicher Abstand:** bei Newton keiner; relativistisch 4m für Einfall aus der Ruhe, 3m für Licht.
- **Welche Kraft:** bei Newton eine zweite Schwerkraft obendrauf (Einfall aus der Ruhe) oder gleichwertig ein Bremsstoß um den Faktor √2. Relativistisch schrumpft
  der Bedarf mit 2(r − 3m)/(r − 2m) und ist bei 4m null.
- **Schwung holen:** geschlossene Bahn unterhalb des Faktors √2, Parabel genau bei √2. An der relativistischen Grenzbahn genügt ein beliebig kleiner Stoß für die
  parabolische Flucht; eine geschlossene Bahn gibt es dort nicht, die Alternative ist der Sturz.

## Zwei Zahlen ohne behauptete Verbindung
Der Faktor 2 der Kraft (Befund 2) und der Faktor 2 des Ablenkwinkels von Licht (ART gegen Newton, k353) sind beides Lehrbuchzahlen. Der erste folgt aus dem
Energiesatz, der zweite aus der Raumkrümmung. Ob dahinter dasselbe steht, ist hier nicht untersucht.

## Korrekturen während der Rechnung (offengelegt)
Im ersten Lauf von k354 erkannte die Abbruchbedingung „wieder draußen“ für E = 1 die Rückkehr nicht (die Bahn berührt u = 0 nur), sodass 63,7 Umläufe gemeldet
wurden; die Schwelle liegt jetzt bei r = 1000m. Die innersten Radien waren davon nicht betroffen. Die Periheldrehung wurde zusätzlich bei 100m und 400m gerechnet.

## Grenzen
Übersetzung gesetzt (Punktmasse, zwei Auslegungen des Neustarts, Stoß oder Zentralkraft). Klassische Bahnen, keine Wellen. Die Schwarzschild-Rechnung ist
Lehrbuch-ART und keine Aussage des Modells; nach H147 hat das Modell keine eigene Kopplung an eine Metrik. Keine Größe des Companion geht ein. OP1 bis OP5
bleiben offen.
