# k420: Zwei Grafiken zu den Bändern auf der Sphäre (Erkundung, Entwurf, 27.11.2026)

**Status:** Erkundung ohne Vorab-Notiz, kein Test. Entwurfsstand der Bilder; die Wahl „Bänder ziehen nach außen“ gegen „Bänder schnüren ein“
ist offen und liegt beim Autor. **Anlass:** Auftrag des Autors vom 27.11.2026 („eine Sphäre, auf deren Oberfläche die Bänder liegen, so wie es
die aktuellen Daten zeigen“; „wie sich die Geometrie dieser Sphäre verändert, nachdem man unsere Bänder darum gelegt hat“; „speichere die Bilder
erstmal ab“). **Werkzeuge:** Python (numpy, scipy, matplotlib) für Minimierung und Zeichnung; Wolfram (k420b) als unabhängige Auswertung der
Verformung. Kein HDL/MMA-Vergleich (kein endlicher Guard-Ablauf). Kein Guard berührt.

## Grafik 1: `baender_sphaere_{de,en}.{png,pdf}` (Skript `k420_baender_sphaere.py`)
Die fünf Bänder R, ℂ, ℍ, 𝕆, 𝕊 als Großkreise in den Lagen der Minimierung aus H192 (k400): E = Σ w_i w_j / sin θ_ij, Gewicht = Dimension. Die
Lagen werden im Skript neu gerechnet; die zehn Winkel stimmen mit `k400_out.txt` überein (Ausgabe in `k420_out.txt`). Dünne Linien: dieselben
Bänder bei den drei anderen Setzungen aus H192c. Rechte Tafel: Winkel je Paar mit der Spanne über die vier Setzungen.
Nur Darstellung (keine Aussage): 𝕊 als Äquator, 𝕆 in der Meridianebene, Bandbreite ~ log₂ Dimension, Blickrichtung.

## Grafik 2: `baender_verformung_{de,en}.{png,pdf}` (Skript `k420_baender_verformung.py`)
Auf der runden Sphäre sind alle fünf Großkreise schon gleichzeitig maximal lang (k399, Teil 4). Die Regel „die Sphäre verformt sich, bis das Band
wieder maximal lang ist“ erzwingt für Großkreise deshalb keine Verformung. Sie entsteht erst mit einem Zug je Band. **Gesetzt** (nicht hergeleitet):

| | Setzung |
|---|---|
| S1 | Jedes Band will möglichst lang sein; Zug nach außen proportional zum Gewicht w_i = Dimension. |
| S2 | Die Sphäre ist eine elastische Haut: Energie ½∫(|∇u|² + m² u²), u = radiale Auslenkung, Volumen fest; m² = 6 gezeichnet. |
| S3 | Die Bänder bleiben auf ihren Lagen aus H192 (keine Rückwirkung der Form auf die Lage). |
| S4 | Die Stärke der Kopplung ist frei; gezeichnet mit größter Auslenkung 28 %. |

Lineare Antwort: u(x) = Σ_i w_i G(n_i·x) mit G(c) = Σ_{l gerade ≥ 2} (2l+1)/2 · P_l(0) P_l(c) / (l(l+1) + m²), abgeschnitten bei l = 80.

## Was die Rechnung zeigt
- Die größte Beule sitzt für m² = 2, 6, 20 an der Kreuzung von 𝕆 und 𝕊 (zwei Gegenpunkte). Verhältnis tiefste Delle zu größter Beule:
  −0,38, −0,34, −0,26. Anteile der Multipole (m² = 6): l = 2: 39 %, l = 4: 46 %, l = 6: 7 %.
- Auslenkung auf den drei Achsen bei m² = 6 und größter Auslenkung 28 %: Kreuzung 𝕆/𝕊 +28 %, Pol von 𝕆 +17 %, Pol von 𝕊 +6 %. Die Form ist
  dreiachsig und wird fast nur von 𝕊 und 𝕆 getragen.
- Gegenprobe k420b (Wolfram): dieselben Werte auf zehn Stellen bei l ≤ 80. Mit l ≤ 200 ändern sich die Werte auf dem Grat um etwa 2 %
  (Abschneidefehler der Reihe), die Lage von Beule und Delle nicht.

## Was aus den Bildern folgt (Lesart)
1. 𝕊 wird zum Äquator, 𝕆 und ℍ werden Meridiane (89,5° und 89,0° zu 𝕊, untereinander 70°). Robust über die Setzungen ist nur 𝕆 ⟂ 𝕊.
2. Die leichten Bänder werden von den schweren geschoben und wandern mit jeder Setzung; die kleinen Winkel liefert diese Geometrie nicht (wie H192).
3. Die Regel des Autors allein verformt die Sphäre nicht; eine Verformung braucht ein Spannungsgesetz, dessen Stärke hier frei ist. Bild 2 gibt
   eine Form, keine Zahl.
4. Die Form hat eine ausgezeichnete Achse durch die Kreuzung von 𝕆 und 𝕊.

## Bilanz der Setzungen
| Größe | Status |
|---|---|
| Lagen der Bänder | aus H192 übernommen (dort: Gewicht und Gesetz gesetzt) |
| Zug nach außen, Stärke ~ Dimension | gesetzt (S1); Vorzeichen offen (außen ziehen oder einschnüren) |
| elastische Haut, m², Volumen fest | gesetzt (S2) |
| Stärke der Kopplung | frei (S4) |
| Lage der größten Beule (Kreuzung 𝕆/𝕊) | folgt aus S1 bis S3, stabil für m² = 2 bis 20 |

## Grenzen
Lineare Antwort, keine Rückwirkung auf die Bandlagen, starre Großkreise; kein Bezug zu Messdaten. OP-Fragen bleiben offen. Nächster Schritt
(Auftrag des Autors, 27.11., 14:31 UTC): ein Spannungsgesetz herleiten statt setzen, mit Vorab-Notiz H209. Nächste frei: H209, k421.
