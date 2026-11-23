# Methoden-Notiz: Benutzen OP1 (Lesart B) und das OP5-Vergleichsmodell (r46/r47) denselben Begriff von Auslese? (Erkundung, vor dem Vergleich festgelegt)

23. November 2026. Auftrag des Autors: „mach das“ (Konsistenzprüfung der Auslese nach r47). Keine H-Nummer.
**Teilweise nicht blind:** Beide Definitionen wurden vor dieser Notiz gelesen; dass beide quadratisch in der Vierergeschwindigkeit des
Beobachters sind, ist absehbar. Die Zuordnung von Achse und Ruhesystem wird erst im Vergleich festgestellt.

## Die beiden Definitionen
- **OP1, Lesart (B)** (`../op1_two_readings_2026_11_17/README.md`, r21.8): Das Register misst φ = |s|/(|E|² + |B|²) des Feldes, das ein Beobachter
  misst; s ist die komplexe Invariante. R ist der Frame mit E ∥ B (φ = 1), P das Nullfeld (φ = 0); M liegt bei der Rapidität η mit tanh η = β_sym,
  φ = sech 2η. OP1 ist unter (B) die Frage, warum M sich mit β_sym relativ zum Ruhesystem R des Feldes bewegt.
- **OP5-Vergleichsmodell, Ausleseseite** (r46, r47): Die gerichtete Kopplung ist −hΠ^{μν}u^αu^βR_{μανβ}, die Auslese des Gezeitenfelds quer zur
  Messachse n eines Detektors mit Ruhesystem u. Der Kontrast hängt in der Ordnung β² von der Bewegung des Detektors relativ zur Präparation ab
  (r46.3). Nach r47 braucht die verlangsamte Ausbreitung ein Bezugssystem auf der Feldseite.

## Vergleichskriterien
- **K1 Was gelesen wird:** Ist es in beiden Fällen der elektrische Teil einer Feldstärke relativ zur Vierergeschwindigkeit u des Beobachters
  (F_{μν}u^ν bzw. R_{μανβ}u^αu^β)?
- **K2 Abhängigkeit von u:** gerade in u (Zeitorientierung fällt heraus) und als Funktion der Rapidität von der Form f(2η)?
- **K3 Achse:** Wem gehört die Achse, dem Feld oder dem Beobachter bzw. Detektor?
- **K4 Bezugssystem der Geschwindigkeit:** Relativ wozu wird die Geschwindigkeit des Beobachters gemessen, und wem gehört dieses Ruhesystem?
- **K5 Normierung:** dimensionsloses Verhältnis mit einer Invarianten oder absolute Größe?

## Kontrollrechnung (Wolfram, exakt; Skript `readout_compare.wl`, Ausgabe `run/readout_compare.txt`)
1. OP1: Feld mit E ∥ B in R, Beobachter quer zu dieser Achse mit Rapidität η: φ(η) = sech 2η nachrechnen; |E′|² + |B′|² = 2T_{μν}u^μu^ν
   prüfen; Boost entlang der Achse zum Vergleich.
2. OP5: die Zähler aus r46.3 für Bewegung entlang und quer zur Achse als Funktion von η (β = tanh η); gerade in η? als Polynom in cosh 2η, sinh 2η?

## Raster (vorab)
- **gleicher Begriff:** K1 und K2 stimmen überein, und Achse und Ruhesystem liegen in beiden Fällen auf derselben Seite.
- **verwandt, nicht gleich:** K1 und K2 stimmen überein, Achse oder Ruhesystem liegen aber verschieden; dann wird die nötige Zuordnung benannt.
- **verschieden:** K1 oder K2 weichen ab.

Frames: Materie-Frame M; R ist das Ruhesystem des Feldes aus Konvention F. Tachyon-Abbildung und Zeitumkehr werden nicht verwechselt.
OP1 und OP5 bleiben offen.
