# Einordnung der Ideen (1) und (2): zwei Bahnen als Bild der Schwerkraft; 10¹²² als Energie des Trägers

**Stand:** 2026-11-26. **Erkundung**, keine H-Nummer, kein Entscheidungskriterium, keine Vorab-Notiz. Auftrag: beide Ideen so weit präzisieren, wie es ein
Entscheidungskriterium erlaubt. Zahlen: `k353_erkundung_ideen_1_2.py`, Ausgabe `k353_out.txt` (Python/scipy; Lehrbuchwerte, nachgerechnet).

## Idee (1): „Das Bild mit zwei Strahlen, die an einem Mittelpunkt vorbeigehen, ist auch das Bild unserer Schwerkraft; eine Bahn ist reine ART, die andere ihr quantenmechanisches Gegenstück“
**Präzisierung.** Für einen Strahl, der mit Stoßparameter b an der Masse m = GM/c² vorbeigeht, gibt es eine Zahl, die die Kandidaten trennt, den Ablenkwinkel:

| Rechnung | Ablenkwinkel |
|---|---|
| skalare Gravitation (Kopplung an die Spur des Energie-Impuls-Tensors) | 0 |
| Newton, Teilchen mit v = c | 2m/b |
| ART (Schwarzschild, Nullgeodäte) | 4m/b |

Nachgerechnet (k353): Newton 2,00000, Schwarzschild 4,00118 bei m/b = 10⁻⁴; das Verhältnis geht gegen 2. Gemessen ist der ART-Wert auf etwa 10⁻⁴.
Die ART-Bahn ist also nicht „eine von zwei Bahnen“, sondern Newton-Anteil (Zeitkrümmung) plus ein gleich großer Anteil aus der Raumkrümmung.

**Was das für die Idee heißt.**
- Eine genaue Fassung wäre: Die zwei Kreisanteile der Schattenellipse (a, b mit μ = b/a, H159) liefern die zwei gleich großen Hälften des Ablenkwinkels.
  **Entscheidungskriterium, sobald eine Kopplung vorliegt:** Das Modell muss für masseloses Licht 4m/b geben. Gibt es 2m/b, fehlt die Raumkrümmung; gibt es 0,
  ist die Kopplung skalar.
- Der Bestand spricht derzeit für die Null: Nach H147 ist die HS(0)-Linie ein Skalar und kein Graviton, und ein Skalar lenkt Licht nicht ab. Die Rechnung zum
  metrischen Abgleich (OP5/H96) setzt minimale Gravitation von außen ein. Das Modell hat also noch keine eigene Größe, die an den Ablenkwinkel koppelt.
- „Quantenmechanisches Gegenstück“ hat im Bestand noch keine Definition, die eine Zahl liefert. H160 zeigt nebenbei: Die Schwarzschild-Variante der Bahniteration
  unterscheidet sich von Newton nur durch stärkeren Einfang, nicht qualitativ.
- **Status:** als Test formulierbar, aber erst rechenbar, wenn eine Feldgleichung mit Kopplung an eine Metrik vorliegt (im Bestand gibt es sie nicht). Vorher wäre
  jedes Ergebnis eine Folge der Setzung.

## Idee (2): „Die 10¹²² der Quantenmechanik sind die Energie, die nötig ist, um unser Quasi-Graviton zu erzeugen, etwa ein Mikro-Schwarzes-Loch, das sofort verdampft“
**Präzisierung der Zahl** (k353, Planck 2018 gerundet):
- ρ_Planck/ρ_Λ = 8π/(Λ·l_P²) = 8,8·10¹²².
- Dieselbe Zahl ist bis auf den Faktor 8π/3 das Quadrat eines Längenverhältnisses: (L/l_P)² mit dem de-Sitter-Radius L = √(3/Λ) = 1,66·10²⁶ m, L/l_P = 1,03·10⁶¹.
  Die Horizontfläche in Planck-Einheiten (Entropie) ist 3π/(Λ·l_P²) = 3,3·10¹²².
- Die Vakuumenergie im Horizontvolumen ist ½·(L/l_P) = 5·10⁶⁰ Planck-Energien, nicht 10¹²².
- Ein Schwarzes Loch der Planck-Masse hat 2·10⁹ J und verdampft in der Größenordnung der Planck-Zeit (5·10⁻⁴⁴ s).

**Was das für die Idee heißt.**
- 10¹²² ist ein Verhältnis zweier **Dichten**, keine Energiemenge. Als „Energie zum Erzeugen eines Objekts“ lässt es sich nur lesen, wenn man sagt, in welchem
  Volumen und wie oft. Die naheliegende Zählung (ein Planck-Objekt je Planck-Fläche des Horizonts statt je Planck-Volumen) ist die holographische Lesart; sie
  ist in der Literatur bekannt (Cohen, Kaplan, Nelson 1999) und erklärt die Größenordnung, nicht den Wert von Λ.
- In der Sprache der Idee: Der Überschuss wäre nicht verloren, sondern die Zahl der Freiheitsgrade des Trägers, gezählt auf der Fläche. Das passt zum Befund
  aus H159, dass „null“ eine Netto-Aussage ist und die Anteile nicht null sind.
- **Ein Entscheidungskriterium ist derzeit nicht möglich.** Das Modell hat keine von Λ unabhängige Länge: Λ ist Eingabe (OP5), die Skala ist gesetzt (H129, H155),
  und γ_L⁵ aus H159 ist eine Zahl der Ordnung 22, keine 10¹²². Jede Rechnung würde L/l_P hineinstecken und wieder herausholen.
- **Was ein Kriterium möglich machte:** eine Herleitung von L/l_P oder von Λ·l_P² aus Größen des Modells ohne Einsetzen. Dann wäre die Aussage prüfbar:
  Λ·l_P² = 2,85·10⁻¹²² innerhalb der Messgenauigkeit.
- **Status:** Lesart, kein Test. Zurückgestellt mit Auslöser „das Modell liefert eine eigene Länge“.

## Grenzen
Lehrbuchphysik, nachgerechnet; keine neue Aussage über das Modell. Kein Guard berührt. OP1 bis OP5 bleiben offen, OP5 ausdrücklich: Λ bleibt Eingabe.
