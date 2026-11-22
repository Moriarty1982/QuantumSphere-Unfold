# Methoden-Notiz: Zeitumkehr oder Spiegelung am ersten Jet des OP5-Keims (Erkundung, vor der Rechnung festgelegt)

22. November 2026. Auftrag des Autors: „weiter“ nach Runde v4.10.0-r41. Keine H-Nummer.
**Teilweise nicht blind:** Von Hand wurde mit der Hubble-artigen Strömung v = ±x/t skizziert, dass Block 2 in den Ableitungen weder dem
Zeitumkehrbild noch dem Spiegelbild von Block 0 entspricht, sondern einer inneren Umkehr der Ströme ohne Koordinatenwechsel (I unten).
Die Rechnung prüft das am tatsächlichen Jet.

## Vorwissen geprüft
- r41: Am Keim (1, 0,6, 0, 0) ist Block 2 bis auf 7,9·10⁻⁴ das Bild von Block 0 unter Zeitumkehr und ebenso unter der Spiegelung x ↦ −x;
  die Werte allein unterscheiden beide nicht. Die Zeitumkehr wurde gewählt, weil nur sie N_m gibt.
- k168: Strömung v = ±x/t, Spins entlang φ̂ = e_y.
- Keimdatei `analysis/op5-field-slices/state-sufficiency-2026-10-30/precision-first-jet-70.json`: Werte und erste Ableitungen ∂_μψ
  (μ = t, x, y, z) auf 70 Stellen. Gültigkeit laut Datei: „F = 0 und g = 0, numerischer erster Jet; die vervollständigten G-, dg-Bedingungen
  nicht gelöst“. Das ist eine Grenze dieser Prüfung.
- r40.4: Die Entkopplung braucht die relative Zeitumkehr eines Vertex, ω ↦ −ω.

## Werkzeug
Python mit mpmath (40 Stellen), Keimordner als Argument. Wolfram ist hier nicht nötig: Es gibt keine symbolische Rechnung, nur Bilinearformen
und ihre Ableitungen an einem Punkt. Qiskit nicht geeignet. Skript `counterflow_jet.py`, Ausgabe `run/counterflow_jet.txt`.

## Rechnung
Normierte Fierz-Größen F = (Φ, Θ, J^a, K^a)/φ² je Block und ihre ersten Ableitungen ∂_μF am Keim. Drei Bilder von Block 0 (und Block 1),
jeweils lokal um den Keimpunkt:
- **T (Zeitumkehr):** F ↦ T·F mit T = (Φ, −Θ, J⁰, −J^i, K⁰, −K^i); Ableitungen ∂_t ↦ −T∂_t, ∂_i ↦ T∂_i.
- **R (Spiegelung x ↦ −x):** F ↦ R·F mit R = (Φ, −Θ, J⁰, −J^x, J^y, J^z, −K⁰, K^x, −K^y, −K^z); ∂_x ↦ −R∂_x, sonst ∂_μ ↦ R∂_μ.
- **I (innere Umkehr):** F ↦ T·F ohne Koordinatenwechsel; ∂_μ ↦ T∂_μ für alle μ.
Für jedes Bild: relative Abweichung von Block 2 in den Ableitungen, max |∂_μF₂ − ∂_μ(Bild)| / max |∂_μF₀|, getrennt nach μ und gesamt.

## Raster (vorab)
- **Zeitumkehr entschieden:** T passt in allen Ableitungen auf 10⁻², R und I nicht. Dann trägt r41 an diesem Punkt ohne die Wahl über N_m.
- **Spiegelung entschieden:** R passt, T nicht. Dann widerspricht der Jet der Lesart von r41; die Gleichgewichtung beträfe die Spiegelung
  und gäbe nach r41.3 N_m nicht.
- **innere Umkehr:** I passt, T und R nicht. Dann ist der Gegenstrom eine Umkehr der Ströme ohne Umkehr der Zeitrichtung der Auslese; ob sie
  als relative Zeitumkehr eines Vertex wirkt, ist eine eigene Frage.
- **unentschieden:** mehrere passen oder keines.

Frames: Keim im Materie-Frame M, Koordinaten des Vergleichsmodells. OP5 bleibt offen.
