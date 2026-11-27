# H192: Bänder als HS-Stufen auf der Sphäre, Gewicht nach Dimension — kommt ein Companion-Winkel heraus? (Test, k400, 27.11.2026)

**Status:** Test mit Vorab-Notiz (`notes/research/predictions/Vorab_Notiz_H192_Baender_Sphaere_HS_Dimension.md`, committet c1c8d4f vor der Rechnung).
H192a ist nicht blind (Kontrolle), H192c ein Bericht. **Werkzeuge:** Python (numpy, scipy) für die Minimierung, Wolfram für die exakten
symmetrischen Winkel. **Anlass:** „ja“ des Autors (27.11.) zum Vorschlag aus k399 und die gewählte Richtung „Lesart wechseln“ für die Quarkmassen
(HS-Stufe statt Farbschwingung).

## Modell
Fünf Großkreise auf der Einheitssphäre, eines je Stufe R, ℂ, ℍ, 𝕆, 𝕊 (Normalen n_i ∈ S²). Gewicht w_i = Dimension (1, 2, 4, 8, 16). Energie
E = Σ_{i<j} w_i w_j / sin θ_ij, minimiert über die Lagen. Kein Winkel wird eingegeben.

## Ergebnis

**H192a (nicht blind, bestätigt).** Bei gleichem Gewicht reproduziert die Minimierung die platonischen Winkel aus k399: n = 2 → 90°, n = 3 → 90°,
n = 4 → 70,53° = arccos ⅓, n = 6 → 63,43° = arccos 1/√5 (Abweichung < 0,1°, Wolfram exakt). Die Bausteine stimmen.

**H192b (Test): teilweise.** Mit Gewicht = Dimension und Gesetz 1/sin:
- Das vorab benannte Paar **𝕆–𝕊 = 89,54°** trifft den Oktant (90°) auf ±1°: **ja**.
- Das vorab benannte Paar **ℂ–ℍ = 49,40°** trifft weder 57,569° (Materie-Frame) noch 54,736° (magisch): **nein** (nächster Companion-Wert
  Koide 45°, Abstand 4,4°).

Damit ist das Kriterium für „bestätigt“ (beide Paare) nicht erfüllt, das für „teilweise“ (nur die Oktant-Struktur) schon: **teilweise**. Das ist
genau der vorab offengelegte erwartete Ausgang.

**H192c (Robustheit).** Über die vier Kombinationen (Gewicht Dimension/√Dimension, Gesetz 1/sin, 1/sin²):

| | 𝕆–𝕊 | ℂ–ℍ |
|---|---|---|
| dim, 1/sin | 89,54° | 49,40° |
| dim, 1/sin² | 89,26° | 51,59° |
| √dim, 1/sin | 88,17° | 58,36° |
| √dim, 1/sin² | 87,90° | 59,43° |

𝕆–𝕊 bleibt stabil nahe 90° (87,9 bis 89,5°), ℂ–ℍ läuft über 10° (49 bis 59°). Der Oktant folgt aus der Symmetrie der zwei schwersten Bänder;
der kleine Winkel hängt von der freien Wahl von Gewicht und Gesetz ab und ist damit angepasst, nicht hergeleitet. Dass ℂ–ℍ bei √Dimension nahe
den Materie-Frame-Winkel 57,569° rückt (58,4°), ist nur eine andere Setzung, kein Treffer des Tests.

**Nachträglich (kein Test).** Bei Gewicht = Dimension, 1/sin, liegen zwei nicht vorab benannte Paare nah an Companion-Winkeln: 𝕆–ℂ = 63,40°
(arccos 1/√5 = 63,43°, Abstand 0,03°) und 𝕆–ℍ = 70,01° (arccos ⅓ = 70,53°, Abstand 0,51°). Nachträglich gefunden, bei zehn Paaren und sieben
Zielen ohne Aussagekraft.

## Lesart
Geometrie auf einer Sphäre mit Gewicht nach der HS-Dimension liefert robust die **Oktant-Struktur** (die zwei schwersten Stufen stehen
senkrecht), aber nicht die kleinen Winkel des Companion: diese hängen von der frei gesetzten Kombination aus Gewicht und Spannungsgesetz ab. Die
Lesart „Quarkwinkel aus der Lage der HS-Stufen auf der Sphäre“ ist in dieser einfachen Form damit erledigt. Der nächste Schritt der gewählten
Richtung „Lesart wechseln“ (getrennte Felder je Stufe statt Geometrie auf einer gemeinsamen Sphäre) liegt beim Autor.

## Bilanz der Setzungen
| Größe | Status |
|---|---|
| Zuordnung Stufe → Band auf gemeinsamer S², Gewicht = Dimension | gesetzt (vorab) |
| Spannungsgesetz 1/sin | gesetzt; trägt den Wert von ℂ–ℍ (H192c zeigt die Abhängigkeit) |
| 𝕆–𝕊 ≈ 90° (Oktant), stabil | hergeleitet (Symmetrie, gesetzesunabhängig) |
| ℂ–ℍ-Winkel | angepasst (läuft mit Gewicht/Gesetz) |
| Companion-Zielwinkel | nicht eingegeben |

## Grenzen
Starre Großkreise auf einer S², Punkt-Abstoßung statt echter Flächenspannung; kein Bezug zu Messdaten. OP3/OP4 (Quarkmassen) bleiben offen.
Nächste frei: H193, k401.
