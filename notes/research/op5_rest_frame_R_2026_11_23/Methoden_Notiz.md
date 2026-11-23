# Methoden-Notiz: Kann das Feldruhesystem R aus OP1 die verlangsamte Ausbreitung des OP5-Vergleichsmodells tragen? (Erkundung, vor der Rechnung festgelegt)

23. November 2026. Auftrag des Autors: „weiter“ nach Runde v4.10.0-r48. Keine H-Nummer.
**Nicht blind:** Vor der Rechnung ist durch eine Symmetrieüberlegung absehbar, dass ein Feld mit E ∥ B unter Boosts entlang seiner Achse
unverändert bleibt; jede daraus gebaute Ausbreitungsstruktur wäre entlang der Achse lichtschnell. Die Rechnung prüft das und bestimmt, was
daraus für die Kegelgrenze folgt.

## Vorwissen geprüft
- r48: Die Auslese von OP1 (B) und des Vergleichsmodells sind verwandt; benannte Zuordnung: Messachse n = E ∥ B-Achse, Bezug auf R. R wäre
  Kandidat für das Bezugssystem der Verlangsamung. r48.1(c): Ein Beobachter entlang der Achse sieht φ = 1 für jede Rapidität.
- r47: Mit lichtschnellen Vermittlern verletzt das gekoppelte System die metrische Kegelgrenze; im Kanal i muss bei r_i = 1 die Hauptkopplung
  j_i verschwinden. j_0² = g_0²α²/2, j_m² = ⅔g_m²(r_m² − r_mα + α²), α = a/q ∈ [0, 1] (α = 0: Wellenvektor entlang der Achse).
- OP1, Lesart B (`../op1_two_readings_2026_11_17/README.md`): R ist der Frame mit E ∥ B.

## Werkzeug
Wolfram Language exakt (Lorentz-Boosts, invariante Tensoren, Eigenwerte des Hauptteils). Qiskit nicht geeignet. Skript `rest_frame_R.wl`,
Ausgabe `run/rest_frame_R.txt`.

## Rechnung
1. **Symmetrie von R:** Ändert ein Boost entlang der Achse das Feld F mit E ∥ B? Welche symmetrischen Tensoren zweiter Stufe sind unter Boosts
   entlang der Achse und Drehungen um sie invariant? Insbesondere: der Energie-Impuls-Tensor des Feldes.
2. **Effektive Ausbreitung aus R:** Allgemeiner invarianter Ausbreitungstensor G^{μν}; Geschwindigkeit entlang der Achse und quer dazu.
   Beispiel G^{μν} = η^{μν} + λT^{μν} mit dem Energie-Impuls-Tensor des Feldes.
3. **Kegelgrenze mit richtungsabhängiger Geschwindigkeit:** r_0(α) = r_m(α) = r(α) aus Schritt 2, übrige Werte wie r47 (Z = 1, g_0² = g_m² = 3/100,
   c_h² = ½ und c_h² = 1); größtes Geschwindigkeitsquadrat über α, und gesondert bei α = 0.

## Raster (vorab)
- **trägt:** Eine aus R gebaute Ausbreitung macht beide Vermittler für alle Richtungen hinreichend langsam, und die Kegelgrenze hält für alle α.
- **trägt teilweise:** Die Grenze hält quer zur Achse, aber nicht in allen Richtungen; benannt wird, welche Struktur zusätzlich nötig wäre.
- **trägt nicht:** Keine aus R gebaute Ausbreitung verlangsamt überhaupt, oder die Grenze bricht in allen Richtungen.

Frames: R ist das Ruhesystem des Feldes aus Konvention F, M der Materie-Frame; Geschwindigkeiten beziehen sich auf die flache Metrik mit c = 1.
OP1 und OP5 bleiben offen.
