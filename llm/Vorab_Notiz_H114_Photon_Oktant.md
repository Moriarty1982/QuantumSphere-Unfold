# Vorab-Notiz H114: Photon-Eigenpunkt und Rangverlust des Oktanten

22. November 2026. Nicht blind. Anlass ist die Frage des Autors, ob der Photonpunkt die Oktantphase 45 Grad erzwingt und ob zur Stabilität eine zweite Kontraktion von fünf auf vier Dimensionen nötig wäre. Geprüft werden interne lineare Vergleichsräume.

## Vorwissen geprüft

- [Konvention F und Zustandsdisk](../sources/research/parts/v490-post-release-layers.tex), r17/r22: P ist b=0 und hat die Dublett-Dichtematrix I/2. Die radiale Bures-Distanz vom reinen Rand nach P ist π/4.
- [Flacher Oktant](../notes/research/op3_dixon_copies_2026_11_16/README.md), r14/r25: die komplexe Gram-Determinante des Generationsraums verschwindet bei der Bargmann-Phase π/4.
- [Frame-Lesungen H109](../notes/research/predictions/Vorab_Notiz_H109_Generationsabhaengige_Frames.md) und [Massennormierung](../notes/research/op3_frame_mass_normalization_2026_11_12.md): andere Frame-Lesungen, kein natives Phasengesetz für P; die bisherige skalare Normierung ist am Photon-Endpunkt singulär.
- [Helizitätsachse](../notes/research/op3_helicity_axis_2026_11_15/README.md) und [Frames und Generationsachsen](../notes/research/op3_frame_map_generations_2026_11_15/README.md): Photonseite der invarianten Oktantkonstruktion und zentraler Photon-Eigenpunkt sind verschieden.
- [Gesamtbild](../wiki/Gesamtbild.md), T5/T8; in den geprüften OP3-/OP5-Notizen fehlt eine native interne 6→5→4-Kette. Der elastische Fünfraum in den OP5-Antriebsrichtungen betrifft eine andere Größe.

## Kriterien

- **H114a:** Aus b=0 und den festen paarweisen Überlappungsbeträgen 1/√2 folgt φ=π/4. Gegenprobe: dieselbe P-Dichtematrix I/2 mit den beiden normierten Gram-Matrizen für φ=0 und φ=π/4. Sind beide positiv semidefinit, haben dieselben Überlappungsbeträge und verschiedene Ränge, ist die Folgerung aus diesen Eingaben widerlegt.
- **H114b, bedingter Vergleich:** Setze die Bargmann-Phase gleich der nativen radialen Bures-Distanz vom reinen Rand, φ(r)=½ arccos(r), r=|b|. Prüfe die Gram-Determinante, ihr Verhalten für r↓0 und Rang zwei bei P. Bestätigung prüft die gesetzte Identifikation, ihre native Herleitung bleibt eine eigene Frage.
- **H114c:** Der komplexe Gram-Rangverlust erzwingt einen internen reellen Fünfraum als Zwischenstufe und die 5→4-Projektion liefert Stabilität. Prüfe Ränge der Reellifizierung und die Verträglichkeit einer explizit reellen Zwischenprojektion mit der komplexen Struktur. Als unabhängige Dynamikkontrolle vergleiche zwei kontinuierliche Generatoren mit demselben invarianten vierdimensionalen Schnitt und entgegengesetztem Vorzeichen der fünften Eigenrate. Der stabile Fall im Fünfraum widerlegt die Notwendigkeit der Kontraktion für Stabilität. Bei positiver fünfter Eigenrate ist der vierdimensionale Schnitt nur für genau darin startende Daten stabil.

Wolfram Language prüft symbolisch und exakt. Keine numerische Anpassung und keine Identifikation des internen Raums mit Raumzeit.
