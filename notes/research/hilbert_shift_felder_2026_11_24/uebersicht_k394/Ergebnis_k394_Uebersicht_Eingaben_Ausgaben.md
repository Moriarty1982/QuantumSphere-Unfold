# k394: Welche Eingabe bewegt welche Ausgabe? Übersicht nach H184 bis H190 (Erkundung, 27.11.2026)

**Status:** Erkundung ohne Vorab-Notiz, kein Test. Alle Zahlen sind angepasst oder Empfindlichkeiten, keine ist eine Vorhersage.
**Anlass:** Auftrag des Autors vom 27.11.2026: Übersicht, welche Eingaben welche Ausgaben beeinflussen und welche Einstellungen nötig sind, um
eine Ausgabe oder zwei zusammen möglichst genau zu treffen. **Werkzeuge:** Python (numpy, scipy); die Formeln der Mechanismen sind in H184 bis H190
jeweils mit Wolfram gegengerechnet, hier kommt keine neue Formel dazu.

## Vorwissen geprüft

H184 bis H190 (Ordner `ein_vakuum_h184` bis `generationsdrehung_h190`), k376/k378 (Stellgrößen ρ, x je Sektor), H182 (ladungsungerade Invariante),
H186/H187 (Funktionenmenge R), H188 (Ableitungsterme), H189 (bewegtes Vakuum), H190 (Drehung in den Generationen). Daten bei M_Z wie in k376.

## Teil A: die drei Stellgrößen der Brannen-Form

√m_g = M (1 + √2 ρ cos(δ + 2πg/3)), K = (1 + ρ²)/3. Drei Eingaben je Sektor treffen drei Massen immer exakt.

| Sektor | M | ρ | K | δ |
|---|---|---|---|---|
| geladene Leptonen | 17,7156 | 0,99999 | 0,66666 | 0,22223 |
| Down | 0,0496962 | 1,11506 | 0,74779 | 0,10013 |
| Up | 0,34856 | 1,28952 | 0,88762 | 0,05181 |

Empfindlichkeit d ln m / d Eingabe (leichteste, mittlere, schwerste Masse):

| Eingabe | Leptonen | Down | Up |
|---|---|---|---|
| ln M | 2; 2; 2 | 2; 2; 2 | 2; 2; 2 |
| ρ | −47,6; −1,45; 1,16 | −20,9; −3,3; 1,1 | −202; −7,5; 1,0 |
| δ | 51,5; −4,65; 0,26 | −32,4; 8,17; −0,12 | 402; −19; 0,07 |

Lesehilfe: M bewegt alle drei Massen gleich. ρ und δ bewegen fast nur die leichteste Masse, die mittlere zehn- bis dreißigmal schwächer, die
schwerste kaum. Wer die leichteste Masse treffen will, muss ρ und δ auf vier bis fünf Stellen kennen (Up: 1 % in ρ ändert m_u um den Faktor 7).

## Teil B: die Mechanismen aus H184 bis H190 gegen die vier Verhältnisse

Ausgaben: m_u/m_t, m_c/m_t, m_d/m_b, m_s/m_b. Die Skala je Sektor (m_t, m_b) ist in jedem Mechanismus eine eigene freie Zahl. „Optionen“ sind
diskrete Wahlen (Funktionen aus R, Zuordnung, Lesart √m, m, m²); „Stellgröße“ ist die stetige Zahl.

| Mechanismus | Stellgröße | eine Ausgabe allein | zwei Ausgaben im selben Sektor | Paar über die Sektoren | alle vier |
|---|---|---|---|---|---|
| M1 eine Potentialfunktion (H184–H187) | keine | nur m_c/m_t (2,3σ); sonst ab 45σ | Up 46σ, Down 52σ | – | – |
| M2 zwei Potentialfunktionen (H187) | Mischwinkel je Sektor | exakt in 28 bis 139 von 216 Optionen | Up 0,72σ, Down 7,7σ | wie einzeln | wie Up + Down |
| M3 zwei Funktionen über kinetischem Nenner (H188) | Mischwinkel je Sektor | exakt in 367 bis 846 von 1728 | Up 0,36σ, Down 1,15σ | wie einzeln | wie Up + Down |
| M4 Ausbreitung bei drehendem Vakuum (H189) | eine Kopplung, gemeinsam | jede exakt | Up 15σ, Down 6,4σ | m_u/m_t mit m_d/m_b 0,29σ; m_c/m_t mit m_d/m_b 0,20σ; m_c/m_t mit m_s/m_b 3,0σ; m_u/m_t mit m_s/m_b 7,3σ | 30σ |
| M5 Drehung in den Generationen (H190) | Drehrate je Sektor | exakt in 11 bis 74 von 162 | Up 7,3σ, Down 2,5σ | wie einzeln | wie Up + Down |
| M6 gemeinsamer Term ± Ladungsterm (H182, H186) | eine Stärke c, gemeinsam | jede exakt (≤ 0,02σ) | Up 0,72σ, Down 7,7σ | m_u/m_t mit m_d/m_b 0,40σ; sonst 5,6σ bis 34σ | 43σ |

Die genauen Einstellungen (welche Funktionen, welcher Wert der Stellgröße) stehen je Zeile in `k394_out.txt`.

## Lesart

1. **Eine Ausgabe** trifft jeder Mechanismus mit einer Stellgröße, und zwar in einem großen Teil der Optionen. Ein Einzeltreffer sagt nichts.
2. **Zwei Ausgaben im selben Sektor** mit einer Stellgröße sind die erste echte Hürde. Sie gelingt für Up mit zwei Funktionen (0,4σ bis 0,7σ), für
   Down nur mit kinetischem Nenner (1,15σ) oder der Generationsdrehung (2,5σ). Kein Mechanismus schafft Up und Down mit derselben diskreten Wahl
   (das waren die widerlegten Kriterien in H187 bis H190).
3. **Paare über die Sektoren** mit einer gemeinsamen Stellgröße gelingen bei M4 und M6 für die jeweils leichtesten Verhältnisse, aber nie für alle
   vier (30σ, 43σ).
4. **Wo die Schwierigkeit sitzt:** Die leichteste Masse reagiert überall am stärksten (Teil A), und sie ist die, die zwischen Up und Down am
   weitesten auseinanderliegt (m_u/m_t = 7·10⁻⁶ gegen m_d/m_b = 9·10⁻⁴). Was Up trifft, verfehlt Down.

## Bilanz der Setzungen

| Größe | Status |
|---|---|
| Vakuum (K = ⅔, δ = 2/9) | Eingabe aus dem Lepton-Sektor |
| Funktionenmenge R, Lesarten, Zuordnungen | benannte Auswahl aus H186 bis H190 |
| Stellgrößen (Mischwinkel, Kopplung, Drehrate, c) | angepasst |
| Skala je Sektor | frei |
| hergeleitet | nichts Neues; die Formeln stammen aus H184 bis H190 |

## Grenzen

Kein Test, keine Zufallskontrolle über die hier gezeigten besten Treffer hinaus (die Quoten stehen in H187 bis H190). Massen bei M_Z; das Laufen
ist nicht variiert. OP3 und OP4 bleiben offen.
