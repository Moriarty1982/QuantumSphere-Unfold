# OP1: Lesart (H) gegen (B) der Registerbreite, beide getestet (Erkundung, nicht blind)

17. November 2026. Auftrag des Autors: „teste beides“, zur offenen Voraussetzung aus `../op1_backward_search_2026_11_17/`: Ist die Registerbreite b von
Konvention F eine Helizitätsbreite des Feldzustands (H) oder eine Beobachtergröße (B)? Skript `two_readings.py`, Ausgabe `run/two_readings_stdout.txt`;
Kandidatenliste für (B) vor der Rechnung committet (`Kandidatenliste_Geschwindigkeit.md`, 4677bc1). Nicht blind. Keine H-Nummer.

## Definitionen
- **(H)** b_H = (|s₊| − |s₋|)/(|s₊| + |s₋|) aus den komplexen Amplituden, Lorentz-invariant (r16.3); die Ports sind die Pole (r16.2(b), U1-Notiz).
- **(B)** φ = |s|/(|E|² + |B|²) für das Feld, das ein Beobachter misst; r21.8: φ = sech 2η_R, R mit φ = 1, P mit φ = 0.

## Test 1: Verträglichkeit mit den Bestandsaussagen

| Feld | (B) φ | (H) b_H |
|---|---|---|
| R (E ∥ B, reell) | 1 | 0 |
| M (R mit Rapidität η geboostet) | 0,5363 | 0 |
| T (J_B-Bild von M) | 0,5363 | 0 |
| P (Nullfeld) | 0 | kein Punkt |
| Pol (selbstdual, komplexe Amplitude) | – | 1 |

| Bestandsaussage | (B) | (H) |
|---|---|---|
| S1 (r21.8(c)): R ist der Frame mit E ∥ B, φ = 1, „reiner Zustand“ | ja | **nein**: dasselbe reelle Feld liegt bei b_H = 0, in der Lage von P |
| S2 (r21.8(c), r69.1): P ist das Nullfeld, Breite 0, maximal gemischt | ja | unbestimmt |
| S3 (Konvention F): M und T haben dieselbe Sichtbarkeit 0,5363, T = J_B-Bild | ja; das Vorzeichen von Re s trennt M (Materie) von T (Tachyon) | nein für reelle Felder |
| S4 (r16.3): die Breite auf χ ist beobachterunabhängig | nein | ja |

**(B) gibt alle Aussagen über das Register wieder** (S1–S3, mit dem Vorzeichen von Re s auch die Trennung von M und T). S4 betrifft die χ-Kugel, nicht das
Register. **(H) widerspricht der Definition von R** im Bestand: Der Bezugsframe R ist ein reelles Feld mit E ∥ B und hätte als Helizitätsbreite den Wert 0.

## Test 2: Quellensuche je Lesart
- **(B):** Gesucht war eine ausgezeichnete Geschwindigkeit v = β_sym = 0,549406 des Beobachters M relativ zu R. Vorab festgelegte Liste mit 9 Kandidaten
  (Kreisbahnen und freier Fall bei Photonring, ISCO, marginal gebundener Bahn, Energiedichte × 2, Zählparameter als Rapidität): **0 Treffer.** Am nächsten
  1/√3 (freier Fall bei 6M und Energiedichte × 2, 5,1 %), 0,5 (ISCO, 9 %).
- **(H):** Gesucht wäre eine natürliche Helizitätsasymmetrie |s₋|/|s₊| = β². Im Bestand ist der einzige Kandidat, der Koide-Zustand, schon in r16.9(d)
  ohne Treffer geprüft. Thermische Strahlung ist unpolarisiert (b = 0). Eine Asymmetrie aus Rotation (Kerr, Superradianz) ist nicht gerechnet.

## Folgen
1. **Konvention F ist in Lesart (B) widerspruchsfrei**, in Lesart (H) nicht. Das Register misst φ = sech 2η, also die Lage eines Beobachters zwischen R
   (Ruheframe des Feldes, η = 0) und P (Nullfeld, η → ∞); M liegt bei η mit tanh η = β_sym. Das ist genau die Rapiditätskoordinate aus der Notiz zur Lage
   von P (`../op1_hc_blur_2026_11_16/`).
2. **Was nur unter (H) gilt und deshalb bedingt wird:** die Kette „Breite ≠ 0 ⇒ relative Phasen ⇒ Frequenz“ (`../op1_flux_lines_2026_11_17/`, Nachtrag),
   „Flächenauslesung ⇒ b > b_c ⇒ Frequenz ⇒ nicht statisch“ (`../op1_moran_geometry_2026_11_17/`, Nachtrag Spannung zu P) und die Suche nach einer
   Auslesefrequenz von M (`../op1_readout_frequency_2026_11_17/`), soweit sie diese Kette als Begründung nimmt. Die Rechnungen selbst bleiben richtig;
   ihre Deutung für das Register von M fällt unter (B). Die Moran-Lesart, die Dimensionsleiter und ω_M/ω_T = γ_L als Identität sind davon unberührt.
3. **Unter (B) ist OP1 die Frage nach β_sym:** Warum bewegt sich der Beobachter M mit v = 0,5494 relativ zum Ruheframe des Feldes? Das ist die Frage von T6
   und H48, jetzt mit einer klaren Rolle: β_sym ist die Geschwindigkeit der Flächenauslesung. Neun ausgezeichnete Geschwindigkeiten eines
   Schwarzschild-Horizonts treffen sie nicht.
4. **Die U1-Gleichsetzung (Ports = Helizitätspole)** bleibt für die Ports richtig (r16.2(b)), aber die Breite des M-Registers ist nach (B) keine
   Helizitätsbreite. Dass M „über den Kompensator-Port definiert“ ist, betrifft das Vorzeichen (welcher Port), nicht die Breite.

## Ergebnis in einem Satz
Beide Lesarten getestet: (B) gibt alle Definitionen des Registers wieder, (H) widerspricht der Definition von R; damit ist die Registerbreite eine
Beobachtergröße φ = sech 2η, die Frequenzkette der letzten Notizen gilt nur bedingt, und OP1 ist die Frage, warum der Beobachter M sich mit β_sym bewegt
(neun Horizontgeschwindigkeiten, kein Treffer). OP1 offen.
