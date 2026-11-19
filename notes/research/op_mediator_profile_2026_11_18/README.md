# Profil des Vermittlers: was eine Übersetzungsschicht leisten müsste, und was I1, I4 und k185 davon schaffen (Erkundung, keine Rechnung, 18.11.2026)

**Ergebnis in einem Satz:** Keiner der drei Kandidaten erzeugt alle fünf Übersetzungen. Nur die String-Brücke I1 berührt zwei zugleich (die T-Zählung
von OP1 und die Restbiegung von OP3), und zwar unter den Platzhaltern CT-002 und CT-004. Der Konnektor k185 trägt η nur als Eingabe, das Kondensat I4
bringt als einziger eine Skala, aber keine Übersetzung. Neu als Anforderung: Ein direkt koppelnder Vermittler ist nach H74 nur stabil, wenn M und T
verschiedene Spektren haben; γ_L ≠ 1 erfüllt das, legt es aber nicht fest.

Auftrag des Autors: „Ja, Vermittler-Profil“ (nächster Schritt aus `../op_root_map_2026_11_18/`). Keine Rechnung, keine H-Nummer. Zurückgestellte Idee I1
ist hier Kandidat; ihr Auslöser 3 ist berührt, die Idee wird dem Autor ausdrücklich als möglicher Weg genannt (unten).

## Vorwissen geprüft
- `../op_root_map_2026_11_18/`: fünf Übersetzungen (Versatz, Restbiegung, |U_e2|² und ε, Ω_M, cot θ_W), einzeln gesetzt.
- `../op1_area_quantum_boost_2026_11_18/`: Ein unitärer Frame-Wechsel ändert das Flächenquant nicht (Rovelli–Speziale); der Vermittler braucht einen
  eigenen Zustand.
- k185: `../v4_10_0_w1/Erkundung_Konnektor_Kinematik.md` (Konnektor zwischen Materie und Tachyonbild, q² = 0 bzw. ±2m² sinh 2η).
- I4: `../v4_10_0_w1/Zurueckgestellte_Ideen.md` (Kondensat aus Tachyon-Moden, Skala grob meV bei λ ~ 1, m und λ frei).
- I1: ebenda; `../op3_i1_string_bridge_2026_11_14.md` (eine Lichtquerung, normierte Weltfläche ½, ΔΦ = γ_M/2 = 0,1188, wie H102);
  `../op1_i1_string_endpoints_2026_11_15/` (T zählt Endpunkte offener Strings, j = ½; CT-004).
- `Ergebnis_H74_Stabilitaet_MT.md` (`../predictions/`): Gleiche Spektren in M und T sind gegen jede direkte Kopplung instabil (Rate ε/2ω); stabil nur
  bei Verstimmung |ω₁² − ω₂²| > 2ε. H75: nur über die Gravitation gekoppelt keine Resonanz.
- `../v4_10_0_r82/Erkundung_Torsion_Kondensat.md` (k190): Der Paarungskanal von W1 kondensiert erst an der Planck-Skala; eichinvariant nur ν^c ν^c.
- `../op1_flux_lines_2026_11_17/`: Querungen passen nicht zum isolierten Horizont.

## Das Profil (aus Wurzelkarte und den Grenzen des Bestands)
| | Anforderung | Herkunft |
|---|---|---|
| A1 | trägt **einen** dimensionslosen Wert, der η festlegt (als Ergebnis, nicht als Eingabe) | Wurzelkarte: alle Zahlen hängen an β_sym |
| A2 | koppelt M- und T-Sektor über einen **eigenen Zustand**, nicht über einen unitären Frame-Wechsel | Rovelli–Speziale, r10 |
| A3 | ist **stabil**: bei direkter Kopplung ε nur mit verstimmten Spektren, |Δω²| > 2ε; sonst nur gravitativ | H74, H75 |
| A4 | erzeugt die fünf **Übersetzungen** aus derselben Kopplung | Wurzelkarte |
| A5 | bringt eine **Skala** mit, falls er als Teilchen prüfbar sein soll | Bestand nur dimensionslos |

Zu A3, analytisch: Die Wurzelzahl ist selbst ein Spektralverhältnis (ω_M/ω_T = γ_L, Auslesefrequenz-Notiz). Ein direkt koppelnder Vermittler wäre also
nur deshalb stabil, weil γ_L ≠ 1 ist. Das ist eine Verträglichkeit, keine Herleitung; die Größe von γ_L folgt daraus nicht.

## Die Kandidaten gegen das Profil
| | k185 Konnektor | I4 Kondensat | I1 String-Brücke |
|---|---|---|---|
| A1 η als Ergebnis | nein: η ist Eingabe (μ² = 2m² sinh 2η) | nein: m, λ frei | nein: γ_string ist Eingabe |
| A2 eigener Zustand zwischen den Sektoren | ja (Bilinear aus M und T) | teilweise (sitzt im T-Sektor) | ja (Weltfläche) |
| A3 stabil | nur verstimmt; bei gleichem m instabil (H74) | offen | offen (Kopplung des Strings unbestimmt) |
| A4 Übersetzungen | 0 von 5 | 0 von 5 (berührt höchstens Λ und die Neutrino-Skala, nicht β²) | **2 von 5:** T-Zählung (OP1, über CT-004) und Restbiegung γ_M/2 (OP3, über CT-002) |
| A5 Skala | nein (m frei) | **ja**, grob meV (Vorwissen) | nein (γ_string dimensionslos) |

## Befund
1. **Kein Kandidat erfüllt das Profil.** Alle drei setzen η oder die Grundzahlen voraus, statt sie zu liefern (A1).
2. **I1 ist der einzige Kandidat mit zwei Übersetzungen zugleich.** Die String-Brücke gibt die Zählung von T (Endpunkte, j = ½) und die Restbiegung
   (eine Lichtquerung, Weltfläche ½, ΔΦ = γ_M/2) aus demselben Objekt. Beides hängt an Platzhaltern (CT-002 eine Querung, CT-004 T = String-Sektor),
   und Querungen passen nicht zum isolierten Horizont (17.11.). Für OP4, OP5 und cot θ_W hat I1 nichts.
3. **I4 ist der einzige Kandidat mit Skala**, liefert aber keine der fünf Zahlen. Eine Verbindung von I1 (Zahlen ohne Skala) und I4 (Skala ohne Zahlen)
   ist im Bestand nicht angelegt.
4. **k185 ist kein Vermittler im Sinn des Profils**, sondern eine Folge der Frame-Kinematik bei gegebenem η. Als direkte Kopplung bräuchte er nach H74
   verschiedene Massen in M und T.
5. **Neue Anforderung A3:** Ein Vermittler mit direkter Kopplung verlangt verstimmte Spektren. Das Projekt hat genau eine solche Verstimmung, γ_L. Das
   passt zusammen, erklärt aber den Wert nicht.

## Mögliche nächste Schritte (nicht gerechnet)
- **I1 auf eine dritte Übersetzung prüfen (Vorschlag an den Autor nach der Regel für zurückgestellte Ideen):** Gibt die String-Brücke ohne neue Wahl
  auch |U_e2|² = β² oder Ω_M = β²? Vorab festzulegen ist, welche Größe des Strings (Weltfläche, Endpunktzahl, Spannung) welcher Übersetzung entspricht.
  Gelingt das nicht, ist I1 eine Lesart für OP1 und OP3, keine Übersetzungsschicht.
- **A1 direkt:** Gibt es im Bestand eine Größe, die η als Gleichgewicht festlegt, etwa ein Extremum der Kopplungsenergie bei verstimmten Spektren
  (A3)? Das wäre der erste Versuch, η herzuleiten statt einzusetzen; er bräuchte eine Wirkung (gemeinsamer Kern).
- OP1 bis OP5, C5, C6/T2 offen; keine Vorhersage berührt.
