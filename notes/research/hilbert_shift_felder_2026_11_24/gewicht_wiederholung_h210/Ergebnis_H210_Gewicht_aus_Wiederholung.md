# H210: Folgt das Paargewicht aus der Zahl der Wiederholungen? Nein — die Wiederholung legt keinen Winkel fest; 𝕊 koppelt gar nicht (Test, k423, 27.11.2026)

**Status:** Test mit Vorab-Notiz (`notes/research/predictions/Vorab_Notiz_H210_Gewicht_aus_Wiederholung.md`, committet bfe67e8 vor der Rechnung).
H210a und H210b sind nicht blind, H210c ist der blinde Test, H210d ein Bericht. **Werkzeuge:** Python (numpy, scipy; 240 Starts je Lauf, Minimierung
über Lagen und Phasen), Wolfram (k423b: Paritätsregel symbolisch, vier Kreuzterme unabhängig integriert, Übereinstimmung 4·10⁻⁵).
**Anlass:** „ja bitte“ des Autors (27.11.2026, 15:07 UTC) zur Lesart „gleich lang, wiederholt“.

## Ergebnis

**H210a (nicht blind): bestätigt.** Als reine Belegung (Muster ohne Phase) gibt die Wiederholung nur die zwei schon gerechneten Fälle: Inhalt je
Wiederholung → w = m_i m_j, Energie 322,1532, R–ℂ = 89,54° … 𝕆–𝕊 = 35,59° (k422 Teil 3, H192 gespiegelt); Inhalt je Band → fünf gleiche Bänder,
59,14°/74,03° (k399). Neue Winkel entstehen nicht; welcher der beiden Fälle gilt, ist wieder eine Setzung.

**H210b (nicht blind): bestätigt.** Trägt das Band ein Muster mit Phase, cos(m s − α), so gilt am Gegenpunkt φ(−x) = (−1)^m φ(x) (Wolfram: Rest
exakt 0). Die zwei Kreuzungen eines Paars heben sich auf, wenn m_i + m_j ungerade ist. Mit m = 16, 8, 4, 2, 1 betrifft das genau die Paare mit 𝕊:
größter Kreuzterm mit 𝕊 über Zufallslagen 7·10⁻¹⁷ gegen 1,5·10⁻² bei den geraden Paaren. **𝕊 koppelt an kein anderes Band.** Seine Lage ist frei;
ein Oktant 𝕆 ⟂ 𝕊 folgt in dieser Lesart nicht.

**H210c (Test, blind): widerlegt.**

| Breite σ | R–ℂ | R–ℍ | R–𝕆 | ℂ–ℍ | ℂ–𝕆 | ℍ–𝕆 | Starts im besten Minimum |
|---|---|---|---|---|---|---|---|
| 2° | 18,88° | 33,10° | 34,25° | 32,51° | 26,26° | 12,39° | 1 von 240 |
| 5° | 47,21° | 88,34° | 89,00° | 65,38° | 51,80° | 22,71° | 5 von 240 |

Die Winkel wandern mit der Bandbreite um bis zu 55° (Kriterium: höchstens 3°), keiner liegt bei 70,53°. Die Wiederholung legt also keinen Winkel
fest; es entscheidet die frei gesetzte Bandbreite. Das ist der vorab erwartete Ausgang, aus dem dort genannten Grund: Eine Welle ohne Mittelwert
kann den Kreuzterm durch die Phase negativ machen, die Bänder ziehen sich an (alle Energien sind negativ), bis sich das Muster über die länger
werdende Überlappraute wegmittelt. Diese Länge misst sich in Bandbreiten.

**H210d (Bericht).** Mit Amplitude ~ m: σ = 2°: 38,05°, 55,16°, 46,92°, 29,37°, 31,06°, 59,34°; σ = 5°: 50,32°, 89,05°, 89,09°, 64,74°, 50,41°,
22,65°. Dieselbe Abhängigkeit von σ. Nachträgliche Treffer auf der Zielliste (ohne Aussagekraft): R–ℍ und R–𝕆 nahe 90° bei σ = 5° (89,05°, 89,09°
bzw. 88,34°, 89,00° bei A = 1); bei σ = 2° sind sie weg.

## Vorbehalt zur Numerik
Bei σ = 2° ist die Energielandschaft zerklüftet: Nur einer von 240 Starts erreicht das beste gefundene Minimum, die nächsten liegen 3 % höher mit
anderen Winkeln. Das globale Minimum bei σ = 2° ist damit **nicht gesichert**. Das Urteil hängt nicht daran: Schon die gefundenen Minima bei 2°
haben ganz andere Winkel als das bei σ = 5° mehrfach gefundene, und eine Lage mit vielen fast gleich tiefen Minima legt erst recht keinen Winkel fest.

## Lesart
Die Wiederholung allein liefert kein Gewicht und keinen Winkel. Ohne Phase fällt sie auf eine von zwei Setzungen zurück (H210a). Mit Phase tritt
an die Stelle des Gewichts die Bandbreite als freie Größe (H210c), und das längste Band 𝕊 fällt ganz aus der Wechselwirkung (H210b). Das ist die
dritte Runde zur selben offenen Voraussetzung (H192: Gewicht und Gesetz gesetzt; H209: Gesetz hergeleitet, Gewicht offen; H210: Gewicht nicht aus
der Wiederholung).

## Bilanz der Setzungen (nach AGENTS.md, dritte Runde zur selben Voraussetzung)
| Runde | gesetzt | hergeleitet | wohin die offene Wahl gewandert ist |
|---|---|---|---|
| H192 | gemeinsame S², Gewicht d_i d_j, Gesetz 1/sin | 𝕆 ⟂ 𝕊 (für dieses Gewicht) | zum Gesetz und Gewicht |
| H209 | gemeinsame S², Überlapp kostet, Inhalt erhalten | Gesetz 1/sin, Zug nach außen | zum Paargewicht |
| H210 | gemeinsame S², Wiederholung m = 16/d, Muster als Welle | 𝕊 entkoppelt (Parität) | zur Bandbreite σ |

**Ist das Ziel selbst gesetzt?** Ja. Dass die Stufen des Turms als Bänder auf **einer gemeinsamen** Sphäre liegen und ihre gegenseitige Lage einen
Companion-Winkel tragen soll, ist in allen drei Runden die Eingabe. Jede Runde hat eine freie Größe durch eine andere ersetzt (Gesetz → Gewicht →
Breite). Das spricht dafür, dass die Frage nur in dieser gewählten Zerlegung entsteht. **Weggabelung für den Autor:** (a) das Bild der Bänder auf
einer gemeinsamen Sphäre als Anschauung behalten und keine Winkel mehr daraus erwarten; (b) eine Größe suchen, die Breite oder Gewicht festlegt
(zum Beispiel die Zählregel, 1 Bit je Fläche: Dann wäre die Bandbreite keine freie Zahl mehr); (c) die Bänder nicht auf eine gemeinsame Sphäre
legen, sondern jede Stufe auf ihre eigene (Hopf-Faserungen, k399 Teil 6).

## Grenzen
Starre Streifen, statisches Muster, Gauß-Profil, kein Bezug zu Messdaten. OP1 und OP4 unberührt und offen. Nächste frei: H211, k424.
