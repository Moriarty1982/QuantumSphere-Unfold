# Ergebnis H211 (k424): jedes Band um einen Schritt zum Vorgänger gedreht

Stand 27.11.2026. Vorab-Notiz: `notes/research/predictions/Vorab_Notiz_H211_Baender_um_einen_Schritt_gedreht.md` (Commit 93b0bc0, vor dem Lauf).
Skript `k424_test_h211.py`, Ausgabe `k424_out.txt`; Wolfram-Gegenprobe `k424b_gegenprobe.wl`, Ausgabe `k424b_out.txt`.

## Frage und Lesart

Frage des Autors: Was ist, wenn jedes Band, das jeweils eine HS-Stufe darstellt, zum Vorgänger um +1 weiter gedreht ist?

Gerechnete Lesart: Die Normale des Bands k entsteht aus der des Bands 0 durch k-malige Drehung um eine feste Achse, n_k = D^k n_0.
Der Schritt ist ein Schritt der Achter-Uhr, also 45° (k407). Die Neigung χ zwischen Achse und n_0 ist dabei eine freie Größe.
Der Winkel zweier Bänder mit Stufenabstand s folgt aus

    cos θ_s = cos²χ + sin²χ · cos(s·φ).

## Urteil

| Teil | Urteil | Befund |
|---|---|---|
| H211a (nicht blind) | bestätigt | Formel exakt (Wolfram, Rest 0). Die Winkel hängen nur vom Stufenabstand ab und von χ. |
| H211b (Test, nicht blind wegen Überschlag) | **widerlegt** | Die Abstoßung wählt χ* = 63,63°, nicht den magischen Winkel 54,74° und nicht 45°. Kein Winkel trifft einen Zielwert. |
| H211c (Robustheit) | hängt an der Setzung | χ* wandert je nach Gewicht und Gesetz zwischen 63,6° und 71,1°. |
| H211d (Stichprobe) | Erkundung | Schritt 72° gibt genau die freie Lage von fünf gleichen Bändern. Nachträglich. |

Kurz: Die feste Drehung legt die Winkel nicht fest. Sie ersetzt zehn freie Winkel durch eine freie Neigung χ. Das ist weniger Freiheit,
aber die verbleibende Zahl folgt weder aus der Drehung noch stabil aus der Abstoßung.

## H211a: was die Drehung allein festlegt

Schritt 45°, Winkel in Grad für Stufenabstand 1, 2, 3, 4:

| Neigung χ | s = 1 | s = 2 | s = 3 | s = 4 |
|---|---|---|---|---|
| 54,736° (magischer Winkel) | 36,42 | 70,53 | 82,06 | 70,53 |
| 45° | 31,40 | 60,00 | 81,58 | 90,00 |
| 90° | 45 | 90 | 45 | 0 (ℝ und 𝕊 fallen zusammen) |
| 57,569° (Materie-Frame) | 37,69 | 73,29 | 77,52 | 64,86 |

Exakt (Wolfram): Beim magischen Winkel ist cos θ = (1+√2)/3, 1/3, (1−√2)/3, −1/3. Der Winkel arccos ⅓ = 70,53° entsteht also
zweimal, für Stufenabstand 2 und 4. Bei χ = 45° ist cos θ = (2+√2)/4, 1/2, (2−√2)/4, 0: Dort stehen ℝ und 𝕊 senkrecht (Oktant),
allerdings für den Stufenabstand 4, nicht für das Nachbarpaar 𝕆–𝕊 wie in H192.

Beide Zielwerte kommen in der Schar also vor, aber bei verschiedenen Neigungen, und keine davon ist ausgezeichnet, solange χ frei ist.

## H211b: wählt die Abstoßung die Neigung?

Gesetz 1/sin θ aus H209, gleiche Gewichte, fünf Bänder, Schritt 45°:

- Minimum bei χ* = 63,6327°, E = 12,679291 (Wolfram: 63,632659°, 12,6792907).
- Winkel dort: 40,10° / 78,62° / 68,26° / 52,73°.
- Zum Vergleich: E(54,74°) = 13,000181, E(45°) = 14,163363.
- Freie Lage derselben fünf Bänder ohne Drehvorschrift: E = 11,0254. Die Schraube liegt um 1,6539 höher, sie ist also eine echte Einschränkung.

Kriterium der Vorab-Notiz: bestätigt bei χ* innerhalb 1° von 54,736°, teilweise bei 45° ± 1°, sonst widerlegt. χ* liegt 8,9° vom magischen
Winkel. **Widerlegt.** Die Energie war vor der Vorab-Notiz von Hand überschlagen; der Test ist deshalb nicht blind.

## H211c: Robustheit

χ* in Grad, Schritt 45°, fünf Bänder:

| Gewicht | 1/sin | 1/sin² |
|---|---|---|
| gleich | 63,63 | 64,85 |
| d_i·d_j | 69,32 | 69,63 |
| min(d_i, d_j) | 71,11 | 71,09 |
| √(d_min/d_max) | 69,45 | 69,77 |

Die Neigung hängt am gesetzten Gewicht (Spanne 7,5°). Das ist dieselbe offene Wahl wie in H192 und H209.

## H211d: Stichprobe anderer Schritte (Erkundung)

Fünf Bänder, gleiche Gewichte, 1/sin:

| Schritt | χ* | E | Winkel s = 1..4 |
|---|---|---|---|
| 22,5° | 90° (Rand) | | 22,5 / 45 / 67,5 / 90 |
| 45° | 63,633° | 12,6793 | 40,10 / 78,62 / 68,26 / 52,73 |
| 60° | 57,881° | 11,4457 | 50,11 / 85,64 / 64,24 / 85,64 |
| 72° | 57,097° | 11,0254 | 59,14 / 74,03 / 74,03 / 59,14 |
| 90°, 120° | Bänder fallen zusammen | | |

Acht Bänder (volle Uhr): Schritt 22,5° gibt χ* = 77,230°, E = 44,4084; Schritt 45° gibt χ* = 59,503°, E = 34,0048 mit Winkeln
38,51 / 75,08 / 74,49 / 60,99 / 74,49 / 75,08 / 38,51. Die Schritte 60°, 72°, 90°, 120° lassen bei acht Bändern Bänder zusammenfallen.

**Nachträglicher Befund, kein Test:** Beim Schritt 72° = 360°/5 erreicht die Schraube exakt die Energie der freien Lage (11,0254).
Die freie Lage von fünf gleichen Bändern ist also selbst eine Schraube mit Fünftelschritt. Das ist eine Symmetrieaussage über fünf
gleiche Bänder und kein Schritt der Achter-Uhr. Die Neigung dort, 57,097°, liegt 0,47° neben dem Winkel des Materie-Frames (57,569°).
Das war in der Vorab-Notiz nicht als Ziel genannt und wird hier nur festgehalten, nicht gewertet.

## Bilanz der Setzungen (vierte Runde zur selben Frage)

| Runde | gesetzt | hergeleitet | wo die freie Größe sitzt |
|---|---|---|---|
| H192 | Gesetz, Gewicht d_i·d_j | Oktant 𝕆–𝕊 | Gesetz |
| H209 | Inhalt je Band | Gesetz 1/sin | Gewicht |
| H210 | Wiederholung 16/d | 𝕊 entkoppelt (Parität) | Bandbreite |
| H211 | Drehschritt 45°, feste Achse | cos θ_s = cos²χ + sin²χ cos(sφ) | Neigung χ der Achse |

Die freie Größe ist wieder gewandert, diesmal in die Neigung der Achse. Neu ist, dass sie auf eine einzige Zahl geschrumpft ist.
Wer χ aus einer anderen Quelle festlegt, hat alle zehn Winkel. Zwei naheliegende Quellen sind genannt, aber nicht getestet:
der magische Winkel (gibt arccos ⅓ exakt) und der Winkel des Materie-Frames.

## Nicht gerechnet

- Lesart „+1 als Phase längs des Bands“ (Drehung des Musters, nicht der Lage). Nach H210 hängt dort alles an der Bandbreite.
- Drehung um eine Achse, die selbst von Stufe zu Stufe wandert.
- Bezug zu Messdaten: keiner. Die offenen Probleme OP1 bis OP5 bleiben offen.

## Werkzeuge und Grenzen

Python (numpy, scipy) für Minimierung und Stichprobe, Wolfram Language für die exakte Formel, die Sonderfälle und drei Minima.
Wolfram meldete zweimal FindMinimum::lstol; die Minima stimmen mit Python auf alle gezeigten Stellen überein. Qiskit ist für diese
rein geometrische Frage nicht geeignet und wurde nicht eingesetzt.
