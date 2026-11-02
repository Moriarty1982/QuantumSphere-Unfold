# Vorab-Notiz H50: Greift Ω über die ϑ-Richtung auf Ψ zurück?

Festgeschrieben am 2. November 2026, vor der Rechnung. Kontext: `Erkundung_OP5_Symbolstruktur_Grad7.md` und
`Ergebnis_H49_Polarwinkel_Bedingung.md`. Anlass ist die Frage des Autors, ob Ω und Ψ sich gegenseitig beeinflussen.

## Hintergrund

Im festen Vergleichsmodell sieht das Symbol von Ω die freie Richtung δΨ = f·c^μ∂_μΨ mit c = ρ∂_z − z∂_ρ nicht
(θ·k = 0). Wegen c·A = 0 ist dabei c·∂Ψ gleich c·DΨ. Offen ist, ob Ω in niedrigerer Ordnung auf solche Verschiebungen reagiert.

- **Zweite Klasse:** Ω reagiert in niedriger Ordnung. Dann legt Ω = 0 die freie Funktion f mit fest, und es gibt
  einen Kanal, über den Ω auf Ψ zurückwirkt.
- **Erste Klasse:** Ω reagiert nicht. Dann bleibt f von Ω unberührt.

## Rechnung (Skript k135, eigener Aufbau)

1. Die Taylor-Koeffizienten von R = (F, G, dg) bis Grad 3 als Funktion der Ψ-Koeffizienten bis Grad 4 werden mit
   abgeschnittener Potenzreihenarithmetik berechnet. Der Hintergrund wird symbolisch nach Taylor entwickelt. Als
   Ausgangsjets dient der 70-stellige Keim (float64-Auswertung).
2. **Ω** wird so bestimmt: Der Linkskern L der Grad-4-Symbolmatrix ∂(R-Koeffizienten Grad 3)/∂(Ψ Grad 4) wird
   berechnet. Für jedes ℓ ∈ L wird der Gradient von ℓ·R₃ nach den Jets bis Grad 3 gebildet. Davon wird der Zeilenraum
   der Linearisierung A_low der R-Koeffizienten bis Grad 2 abgezogen. Was übrig bleibt, ist dΩ⊥.
3. **Gültigkeitsbedingungen** (sonst Ergebnis „unentschieden“):
   - Die abgezogenen Gradienten haben numerischen Rang 1, mit einer Lücke von mindestens 1e3.
   - Der Grad-3-Anteil von dΩ⊥ ist parallel zum gespeicherten θ, |cos| ≥ 0,999.
4. **Messgröße:** Für v = Jets von f·c'^μ∂_μΨ ist r(f, c') = |dΩ⊥·v| / (|dΩ⊥|·|P_ker v|). Dabei ist P_ker die
   Projektion auf den Kern von A_low. Getestet werden:
   - f aus allen 35 Monomen (x − p)^a mit |a| ≤ 3;
   - c' = ϑ-Feld (Test);
   - c' = ∂_t, ∂_x, ∂_y (Kontrollen; keine davon ist frei).

## Entscheidungskriterium (vorab)

- **Gültigkeit:** Die Kontrollen müssen anschlagen. Für jede Kontrollrichtung gilt max_f r ≥ 1e-2.
- **Bestätigt (zweite Klasse):** max_f r(f, ϑ) ≥ 1e-3.
- **Widerlegt (erste Klasse bis Ordnung 3):** max_f r(f, ϑ) ≤ 1e-6.
- **Unentschieden:** alles dazwischen, oder die Gültigkeit ist verletzt.

Hinweis vorab: Für f = 1 ist am Äquator wegen der Spiegelsymmetrie z ↦ −z ohnehin r ≈ 0 zu erwarten. Die
Entscheidung tragen die nicht konstanten f.

## Grenzen

Linearisierung an einem Keim, Differenzenquotienten in float64, nur bis Ordnung 3. Eine Bestätigung zeigt einen
Kopplungskanal im Vergleichsmodell, nicht, dass das volle System bestimmt ist, und keine physikalische Aussage.
