# H209: Spannungsgesetz der Bänder aus dem Überlapp — 1/sin folgt, das Gewicht aus der Schachtelung trägt den Oktant nicht (Test, k421, 27.11.2026)

**Status:** Test mit Vorab-Notiz (`notes/research/predictions/Vorab_Notiz_H209_Spannungsgesetz_aus_Ueberlapp.md`, committet 406b2b6 vor der
Rechnung). H209a ist nicht blind, H209c eine Herleitung unter genannter Setzung, H209d ein Bericht. **Werkzeuge:** Python (numpy, scipy) für
Flächenkontrolle und Vielstart-Minimierung (600 Starts), Wolfram (k421b) für die exakte Überlappfläche und eine unabhängige Minimierung. Beide
einig (Energien auf neun Stellen, alle Winkel auf 0,01°). **Anlass:** Auftrag des Autors vom 27.11.2026 („versuche dich mal am Spannungsgesetz“).

## Ergebnis

**H209a (nicht blind): bestätigt.** Zwei Streifen der Breiten a, b unter dem Winkel θ überlappen sich je Kreuzung in einer Raute der Fläche
a b / sin θ (Wolfram exakt). Auf der Sphäre gemessen: bei halber Breite 2° Abweichung ≤ 0,12 % für θ ≥ 30° (0,6 % bei 15°); bei halber Breite 10°
und θ = 15° sind es 22 %. **Sobald Überlapp Energie kostet, ist das Gesetz 1/sin** (nicht 1/sin²), mit Korrekturen nur für breite Bänder unter
flachem Winkel.

**H209b (Test): widerlegt, für beide Normierungen.**

| Gewicht je Paar | 𝕆–𝕊 | ℂ–ℍ | Urteil |
|---|---|---|---|
| N0: d_i d_j (H192, Vergleich) | 89,54° | 49,40° | teilweise (wie H192) |
| N1: min(d_i, d_j) | 87,60° | 62,06° | **widerlegt** (Oktant um 2,4° verfehlt) |
| N2: √(d_min/d_max) | 84,40° | 67,19° | **widerlegt** (Oktant um 5,6° verfehlt) |

Mit dem Gewicht, das aus der Cayley–Dickson-Schachtelung folgt, steht 𝕆 nicht mehr senkrecht auf 𝕊, und ℂ–ℍ trifft keinen der benannten Winkel.
Der einzige robuste Befund aus H192 (Oktant) hängt damit an der Setzung „Band = skalare Ladung der Größe Dimension“. Er ist keine Folge der
Geometrie allein. Das deckt sich mit der vorab offengelegten Erwartung für N2; für N1 war der Ausgang offen.

Unter N2 hängt das Gewicht nur vom Stufenabstand ab. Die Lage ist dann spiegelsymmetrisch unter ℝ ↔ 𝕊, ℂ ↔ 𝕆 (ℍ fest): R–ℂ = 𝕆–𝕊 = 84,40°,
R–ℍ = ℍ–𝕊 = 72,73°, ℂ–ℍ = ℍ–𝕆 = 67,19°, R–𝕆 = ℂ–𝕊 = 54,09°.

**H209c (Herleitung unter der Setzung „Inhalt je Band erhalten“).** Die Kreuzenergie geht dann wie 1/(L_i L_j); jedes Band gewinnt Energie, wenn
es länger wird. Die Regel des Autors („Band maximal gedehnt“) ist damit eine Folge, und das Vorzeichen ist **Zug nach außen**, nicht Einschnüren.
Die Stärke je Band ist seine gesamte Kreuzenergie E_i:

| | ℝ | ℂ | ℍ | 𝕆 | 𝕊 |
|---|---|---|---|---|---|
| N0 (Anteil) | 5 % | 10 % | 18 % | 29 % | 38 % |
| N1 | 8 % | 14 % | 21 % | 28 % | 28 % |
| N2 | 17 % | 21 % | 23 % | 21 % | 17 % |

Der Zug ist viel gleichmäßiger verteilt als in k420 gesetzt (dort ~ Dimension: 3 %, 6 %, 13 %, 26 %, 52 %). Die größte Beule der Fläche (Rechnung
wie k420, m² = 2, 6, 20) liegt für N0 und N1 an der Kreuzung 𝕆/𝕊, für N2 an der Kreuzung ℂ/ℍ. Die Dellen werden tiefer (Delle zu Beule −0,31 bis
−0,36 für N0, −0,41 bis −0,52 für N1, −0,63 bis −0,83 für N2).

**H209d (Bericht): keine Zahl.** Keine Skala: Die Energie ist homogen in Bandbreite und Feldbetrag; das Verhältnis von Zug zu Elastizität der
Fläche bleibt frei. Von den Winkeln θ, δ, β_sym kommt über die benannten Paare keiner heraus.

**Nachträglich (kein Test).** Unter N1 liegen sechs der zehn Paare innerhalb ±1° eines Zielwinkels, darunter R–𝕆 = 57,65° (Materie-Frame 57,569°,
Abstand 0,08°), R–ℍ = 60,43° (Hopf 60°), R–𝕊 = 53,88° (magisch 54,74°). Keines war vorab benannt. Die Winkel liegen zwischen 54° und 88°; dort
decken die Zielfenster etwa 31 % ab (die Vorab-Notiz nannte 16 % für den ganzen Bereich bis 90°, das ist für diesen Bereich zu niedrig). Sechs
oder mehr Treffer von zehn haben dann eine Zufallsquote von mehreren Prozent. Ohne neue Vorab-Notiz ist das kein Befund.

## Lesart
Das Gesetz zwischen zwei Bändern lässt sich herleiten: Überlapp → 1/sin; erhaltener Inhalt → Zug nach außen. Nicht herleiten lässt sich bisher,
**wie stark** zwei Stufen einander sehen. Die drei geprüften Gewichte geben drei verschiedene Bilder, und der Oktant steht nur bei der gröbsten
Setzung. Die offene Wahl ist also vom Gesetz (H192) zum Paargewicht gewandert.

## Bilanz der Setzungen
| Größe | Status |
|---|---|
| Winkelfunktion 1/sin | **hergeleitet** aus dem Überlapp schmaler Streifen (H209a) |
| Vorzeichen: Zug nach außen | **hergeleitet** unter der Setzung „Inhalt je Band erhalten“ (H209c) |
| Paargewicht (N0, N1, N2) | **offen**; trägt alle Winkel, auch den Oktant |
| Kreuzterm positiv, quadratische Energie, gleiche Breite, gemeinsame S² | gesetzt |
| Stärke gegen die Elastizität der Fläche, Skala | frei |

Bilanz nach AGENTS.md (zweite Runde „teilweise/offen“ zur selben Voraussetzung nach H192): H192 setzte Gewicht und Gesetz und leitete den Oktant her;
H209 leitet das Gesetz her und zeigt, dass der Oktant am Gewicht hängt. Die offene Wahl liegt jetzt allein beim Paargewicht. Ob das Ziel (ein
Companion-Winkel zwischen Bändern auf einer gemeinsamen S²) selbst eine gesetzte Eingabe ist: ja, die gemeinsame S² ist gesetzt. Diese Weggabelung
liegt beim Autor.

## Grenzen
Starre Großkreis-Streifen, kein dynamisches Feld, kein Bezug zu Messdaten. OP1 bis OP5 unberührt und offen. Zurückgestellte Idee I1
(Stringspannung setzt die Skala) ist der naheliegende Ausweg für die fehlende Skala; ihr Auslöser trifft hier zu. Nächste frei: H210, k422.
