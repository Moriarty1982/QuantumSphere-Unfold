# Kegelgrenze bei lichtschnellen Vermittlern: Korrektur zu r46 und Ende von Weg 2 (Erkundung, nicht blind, 23.11.2026)

**Ergebnis in einem Satz:** Koppelt der Higgsradius über die Auslese im Hauptteil an einen lichtschnellen Vermittler, so hat das gekoppelte
System Charakteristiken schneller als die metrische Lichtgeschwindigkeit; das gilt für den masselosen und den massiven Kanal. Damit war die
Aussage aus r46.2, r_m = 1 sei zulässig, falsch, und die Bigravitation von M und T (Weg 2, Wahl des Autors) scheitert bei proportionalen
Hintergründen an derselben Bedingung.

Anlass: Auftrag des Autors „versuchen wir 2.“ (Bigravitation von M und T als bewusst neue Zutat). Bei der Vorwissen-Prüfung für die
Vorab-Notiz fiel die Bedingung der Kegelgrenze-Notiz auf. Keine H-Nummer vergeben: Das Ergebnis steht analytisch fest (nicht blind),
ein blinder Test von Weg 2 ist deshalb nicht mehr sinnvoll.

## Vorwissen
`../op5_bifocal_response_2026_11_18/OP5_J_Metrische_Kegelgrenze.md`: Mit K = diag(A, 1, 1) und V = {{b, j_0, j_m}, {j_0, r_0, 0}, {j_m, 0, r_m}}
liegen die Quadrate der gekoppelten Geschwindigkeiten genau dann in (0, 1], wenn V ≻ 0 und K − V ⪰ 0. „Wenn r_i = 1, muss die
entsprechende Hauptkopplung j_i verschwinden. Sonst hat der zugehörige zweidimensionale Hauptminor von K − V die Determinante −j_i² < 0.“
Für die gerichtete Kopplung ist j_0² = g_0²α²/2 und j_m² = ⅔g_m²(r_m² − r_mα + α²); die verlangsamten Werte r_0 = r_m = ½ wurden dort
gewählt, um die Grenze einzuhalten.

## Kontrolle (`cone_check.wl`, Ausgabe `run/cone_check.txt`, Wolfram)
| Fall (Z = 1, g_0² = g_m² = 3/100) | größtes Geschwindigkeitsquadrat über α ∈ [0, 1] |
|---|---|
| Vergleichsmodell, c_h² = r_0 = r_m = ½ | 0,675 |
| r_0 = r_m = 1 | 1,064 |
| r_0 = r_m = 1, c_h² = 1 (W2, r33) | 1,199 |
| nur r_0 = 1 | 1,031 |
| nur r_m = 1 | 1,041 |
Bei r_m = 1 ist j_m² = ⅔g_m²(1 − α + α²) ≥ g_m²/2 > 0 für alle α.

## Folgen
1. **Korrektur zu r46 (append-only):** r46.2 hat r_m nur an den Stabilitätsbedingungen aus r38 gemessen. Für den führenden statischen Kontrast
   ist r_m tatsächlich ohne Einfluss, für die Kausalität des gekoppelten Systems aber nötig: Beide Vermittler müssen langsamer als die
   metrische Lichtgeschwindigkeit laufen. Die verlangsamte Ausbreitung bleibt eine Setzung. Nach dem strengen Raster trägt Zweig B damit nur
   **teilweise**: Rahmen, Achse und Orientierung gehören zur Auslese, die Verlangsamung nicht.
2. **Ein lichtschnelles Graviton genügt nicht:** Schon der masselose Kanal mit r_0 = 1 verletzt die Grenze. Die gerichtete Auslesekopplung des
   Higgsradius ist in diesem reduzierten Modell mit gewöhnlicher, lichtschneller Gravitation nicht verträglich.
3. **Weg 2 (Bigravitation von M und T):** Bei proportionalen Hintergründen laufen beide Spin-2-Zustände lichtschnell; Weg 2 scheitert an
   derselben Bedingung. Helfen könnte nur ein zweiter Kegel, der enger ist als der metrische. H78 gibt für T aber einen weiteren Kegel
   (quer zur Achse das γ-fache), also die falsche Richtung.
4. **Wo die Verlangsamung herkommen müsste:** Ein Lorentz-kovariantes Feld läuft in jedem Rahmen lichtschnell. Ein Kegel enger als der
   metrische braucht ein ausgezeichnetes Bezugssystem auf der Feldseite, also ein Medium. Die Weggabelung aus r45 löst sich damit nicht
   einseitig auf: Die Ausleseseite trägt Rahmen, Achse und Orientierung der Kopplung, die Feldseite muss die Verlangsamung tragen.
- OP5 und H96 bleiben offen.
