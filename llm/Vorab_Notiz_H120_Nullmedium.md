# Vorab-Notiz H120: Ein Medium aus lichtartigen Strukturen (Photon-Frame), in M „verbogen“ (Lesart a)

**Stand:** 23. November 2026, vor der Rechnung festgelegt. H120a **nicht blind** (folgt aus einer Zeile Algebra, siehe unten); H120b und
H120c blind im Zahlenwert. Anlass, Autor (23.11.): „was ist wenn das medium nur für den photon frame funktionieren würde und in den anderen
frames müsste es sich verbiegen?“ und „mit (a) anfangen“ (Lesart a: Verbiegung über gewöhnliche Boosts).

## Vorwissen geprüft
- r47: Die metrische Kegelgrenze verlangt, dass alle gekoppelten Ausbreitungen langsamer als die metrische Lichtgeschwindigkeit sind; bei r_i = 1
  muss j_i verschwinden. r49: Ein Feld mit E ∥ B ist unter Boosts entlang seiner Achse invariant; daraus gebaute Ausbreitungen sind entlang der
  Achse lichtschnell. r49.3: Bei c_h² = 1 (W2) ist die Grenze für keine Vermittlergeschwindigkeit zu halten; auch der Higgsradius muss
  verlangsamt werden.
- Konvention F, OP1 Lesart B (`notes/research/op1_two_readings_2026_11_17/`): P ist das Nullfeld (φ = 0, η → ∞), R der Frame mit E ∥ B,
  M bei η_sym.
- These T9 (`wiki/Gesamtbild.md`): „Im Photon-Frame ist Λ = 0; Dunkle Energie ist der Frame-Versatz des Beobachters“, großteils nicht tragfähig.
- r34: Paar-Konnektor mit |v| = e^{−2η}; r41: gleiche Gewichte zweier Gegenströme ⇔ Ruhe im System des Gesamtstroms.
- H78 (r84): Laborgrenzen für Lorentz-Verletzung 10⁻¹³ bis 10⁻¹⁵ (für Fermionen).
- Zurückgestellte Ideen: I3 (Geist-Kondensat, Rahmen) berührt, hier nicht verwendet.

## Präzisierung der Lesart (a)
Ein gewöhnlicher Boost ist eine andere Beschreibung desselben Objekts und ändert nichts Messbares. Messbar „verbogen“ ist ein Medium nur über
Invarianten wie u·l zwischen der Vierergeschwindigkeit u eines Beobachters und den lichtartigen Vektoren l des Mediums. Ein Medium aus
lichtartigen Strukturen ist ein Objekt des Photon-Frames; ein Beobachter in M sieht es mit Doppler-Faktoren e^{±η}.

## Aufbau
Alle drei Felder (Higgsradius h, beide Vermittler) breiten sich auf derselben effektiven Metrik aus (universelle Verlangsamung, wie die im
Vergleichsmodell gleich gesetzten c_h² = r_0 = r_m = ½):
G^{μν} = η^{μν} + κ Σ_s w_s l_s^μ l_s^ν, l_s lichtartig, κ > 0 verengt.
- **Ein Strahl:** l = (1, 0, 0, 1).
- **Zwei Gegenströme:** l_± = (1, 0, 0, ±1) mit Gewichten w_+ = a, w_− = b. Ein Beobachter, der sich mit Rapidität η entlang z bewegt, sieht
  a e^{−2η}, b e^{2η}; Gleichgewicht bei e^{4η} = a/b. Der Photon-Frame P ist der Grenzfall η → ±∞.
Richtungsabhängige Geschwindigkeit r(θ) = größtes v² der Wurzeln von v² − 1 + κ Σ w_s (v − c_s)² … (mit c_s = l̂_s·k̂). Kegelgrenze wie r47
(Z = 1, g_0² = g_m² = 3/100) mit c_h² = r_0 = r_m = r(θ) und α = Anteil von k quer zur Messachse n; n ∥ z und n ⊥ z.
Skript `llm/k240_h120_null_medium.py` (Python, sympy und numpy), Ausgabe `llm/k240_out.txt`. Wolfram nur falls verfügbar; Qiskit nicht geeignet.

## Hypothesen und Kriterien
- **H120a (ein Strahl, nicht blind):** Ein Medium aus einem lichtartigen Strahl lässt die Ausbreitung entlang l lichtschnell (v = 1 ist für jedes κ
  Wurzel), und weil j_m² = ⅔g_m²(r² − rα + α²) ≥ ½g_m² > 0 für alle α, ist die Kegelgrenze dort verletzt. **Bestätigt**, wenn für alle κ > 0
  und beide Lagen von n das größte Geschwindigkeitsquadrat in Richtung l über 1 liegt.
- **H120b (zwei Gegenströme):** Es gibt a, b, κ > 0, für die die Kegelgrenze in allen Richtungen hält (größtes Geschwindigkeitsquadrat ≤ 1 über
  θ ∈ [0, π] und α ∈ [0, 1], Raster 41 × 21, Toleranz 10⁻⁹). Zusatz „nur in P wirksam“: Die Verlangsamung verschwindet für η → ∞ (max_θ(1 − r) → 0).
  **H120b bestätigt**, wenn beides gilt; **teilweise**, wenn nur die Grenze hält; **widerlegt**, wenn kein Parametersatz die Grenze hält.
- **H120c (Schranke, gilt für jedes Medium im Vakuum):** Bei universeller Verlangsamung r verlangt die Kegelgrenze eine Mindestverlangsamung
  ε = 1 − r ≥ k·√(g_m²) mit einem Faktor k der Ordnung eins (exakt aus der oberen Bedingung bei α = 1, r → 1). **Bestätigt**, wenn diese
  Skalierung exakt folgt. Folge mit der Laborgrenze ε ≤ 10⁻¹³: g_m² ≤ (10⁻¹³/k)².
- **Kontrolle:** das Vergleichsmodell (r = ½ überall) gibt 0,675 wie in r47.

## Folge, vorab festgelegt
- H120a bestätigt: Ein Medium aus einem Strahl des Photon-Frames kann die Verlangsamung nicht tragen.
- H120b bestätigt: Zwei Gegenströme des Photon-Frames bilden für M ein Medium mit Ruhesystem (dort, wo sich die Gewichte ausgleichen) und
  heilen die Kegelgrenze; das wäre eine Form der „Verbiegung“. Ob es in P verschwindet, entscheidet der Zusatz.
- H120c bestätigt: Unabhängig vom Medium ist der gerichtete Kontrast im Vakuum durch die Laborgrenzen der Lorentz-Verletzung auf etwa (ε/k)²
  begrenzt; im Material gilt diese Grenze nicht.
- Nichts davon schließt OP5; T9 wird nicht geprüft (Λ in P bleibt offen).
