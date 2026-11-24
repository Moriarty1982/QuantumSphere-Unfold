# Erkundung: Restdrehung der Drei-Sektor-Scheibe als Holonomie (k246)

24. November 2026. Autorenauftrag „mach das mal alles“ zum Anschluss (c) des Gedankenexperiments „Zeit als
Restdrehung“ (Zeit = aufsummierte Restdrehung nach einem Formzyklus, Shapere–Wilczek / fallende Katze).
**Erkundung, nicht blind:** Das Ziel ΔΦ = γ_M/2 war bekannt. Es gibt keine H-Nummer, keine Vorab-Notiz, keinen
MMA-Beleg und keine Änderung an Guards. Einordnung T8/T13, OP3 (ruht auf Autorentscheidung, hier nur auf Auftrag
berührt). Skripte `k246_holonomie.py`, `k246_simplexrand.py`, `k246_holonomie.wl` mit Ausgaben `*_out.txt`.

**Frage.** Lässt sich ΔΦ = γ_M·A (I1-Brücke, normierte Fläche A = ½) als Holonomie eines konkreten Formzyklus von drei
Punkten bzw. Bögen auf dem Kreis herleiten? Tritt γ_M dabei als Krümmung oder als Umrechnungsfaktor auf, ohne
eingesetzt zu werden?

## Vorwissen geprüft
- `op3_i1_string_bridge_2026_11_14.md`: ΔΦ = γ_M · A_ws/ℓ², A = ½ bei einer Lichtquerung (Bedingung mit bekanntem Ziel gewählt).
- `counterterms/CT-001_gamma_halbe_einheit_entwurf.md`, Schritte 1–3: ½ als normierte Sektorfläche; γ als γK-Phase pro Radiant (r10.1).
- `op3_string_length_exploration_2026_11_12.md`: Kreismodell mit Bögen ℓ_i, √m_i = c ℓ_i, keine Winkel; Koide-Bögen q:1:1, q = 4 + 3√2.
- `op3_string_energy_source_search_2026_11_12.md` (4.) und `op3_selection_principle_2026_11_13.md`: Brannen-Bögen positiv nur für
  |θ| ≤ π/12; Elektronmasse = Abstand vom Rand; ΔΦ = π/4 − 3θ_e.
- Gedankenexperiment `gedankenexperiment-zeit/notizen.md` (Projektordner, nicht im Repo), Schritte 3, 5, 16 und 17
  (Drei-Mulden-Schwelle: nur 2/n, kein γ).
- Kein Vorbefund zu Formraum, mechanischem Zusammenhang oder Shapere–Wilczek im Repo (Suche nach shapere, wilczek,
  fallende Katze, Formraum, shape space in notes, analysis, wiki und parts; Treffer nur in fremdem Zusammenhang).

**Werkzeugwahl.** Wolfram Language für die exakten Integrale und das Maximum (unabhängige Kontrolle zu sympy);
numerische Integration (scipy) für die direkte J = 0-Dynamik und das Randintegral. Qiskit nicht eingesetzt: Es gibt
keinen Quantenschaltkreis, der Zusammenhang ist klassisch. **Gefundener Fehler:** Das symbolische Doppelintegral in sympy
gab für Modell C −1,2589. Wolfram, das numerische Doppelintegral und das Randintegral (Stokes) geben übereinstimmend −π.
Maßgeblich ist −π.

## Aufbau
Drei Massen auf der Scheibe mit Winkeln θ_i und Radien r_i. Gesamtdrehimpuls J = Σ m_i r_i² θ̇_i = 0 (keine äußere
Drehung). Der Formraum ist die Konfiguration bis auf Drehung; die Faser ist der Drehwinkel. Der mechanische Zusammenhang
ist 𝒜 = Σ m_i r_i² dθ_i / Σ m_j r_j². Die Restdrehung nach einem geschlossenen Formzyklus ist die Holonomie,
gleich dem Fluss der Krümmung ℱ = d𝒜 durch die umlaufene Formfläche.

## Ergebnisse
**1. Das Kreismodell vom 12.11. erzeugt keine Restdrehung (Modell A).** Bei festem Radius und von der Form unabhängigen
Massen ist 𝒜 = Σ m_i dθ_i / M ein Differential mit konstanten Koeffizienten, also exakt: ℱ = 0. Kein Zyklus der Bögen,
gleich welcher, hinterlässt eine Drehung. Außerdem lässt sich ein voller Umlauf der Brannen-Phase dort nicht als
Bogenzyklus fahren, weil die Bögen außerhalb |θ| ≤ π/12 negativ würden (bekannt). Die Lepton-Phase ist in diesem Modell
also keine Holonomie.

**2. Restdrehung braucht eine formabhängige Trägheit.** Zwei Wege, beide mit ℱ ≠ 0:
- (B) radiale Streckung und tangentiale Verschiebung, phasenversetzt (Wanderwelle);
- (C) Massen, die an den Bögen hängen, m_i = ℓ_i^p (für p = 2 die Auslese √m_i ∝ ℓ_i).
Das präzisiert Schritt 16 des Gedankenexperiments: Radiale Streckung allein dreht nie, tangentiale Bewegung bei fester
Trägheit auch nicht. Erst beides zusammen, mit Phasenversatz, erzeugt Fläche und Drehung.

**3. Modell B exakt.** Mit r_i = R(1 + a cos(δ + 2πi/3)) und θ_i = φ + 2πi/3 + b sin(δ + 2πi/3) ergibt ein voller Umlauf
von δ (Wolfram exakt, für jedes b, numerisch auf 10⁻¹⁰ bestätigt):

  Δφ = −4π a b / (a² + 2) = −2π b · k(a),  k(a) = 2a/(a² + 2).

- k(a) ist **genau bei der Koide-Amplitude a = √2** maximal (K = 1/3 + a²/6 = 2/3), mit k_max = 1/√2.
- Mit tan ψ = a/√2 ist k = sin 2ψ/√2. Das Maximum ist der bekannte 45°-Winkel (Treue ½, ρ² = ½) in anderer Gestalt,
  derselbe Winkel wie das π/4 in ΔΦ = π/4 − 3θ_e. Nachträglich und keine neue Information: Koide ist die Amplitude, bei
  der eine radiale Wanderwelle am stärksten an die Drehung koppelt.
- Der Drehsinn ist das Vorzeichen von a·b, also der relative Phasenversatz von radialer und tangentialer Welle: gesetzt,
  wie in allen bisherigen Bildern.
- γ_M tritt nicht auf. ΔΦ = γ_M/2 verlangt b = γ_M/(2√2π), also eingesetzt.

**4. Modell C: der größte Formzyklus gibt eine halbe Drehung.** Mit m_i = ℓ_i² im Bogenmittelpunkt ist die Krümmung am
gleichverteilten Punkt ℱ = −1/π, am Koide-Punkt (q:1:1) −0,0514. Der Fluss durch den ganzen Formsimplex, also die
Holonomie des Zyklus, bei dem nacheinander jeder Bogen auf null schrumpft und die beiden anderen sich den Kreis teilen,
ist

  Δφ_Rand = −π,  normiert Δφ_Rand / 2π = −½.

Das gilt (numerisch, `k246_simplexrand_out.txt`) für jedes Massengesetz m_i = ℓ_i^p mit p > 0 (geprüft p = ½ … 10) und für p = 2 bei
jeder geprüften Lage der Masse im Bogen (Anteil f = 0 … 1). Für formunabhängige Massen (p = 0) ist es null. Grund: Auf jeder Kante ist ein Bogen leer und trägt kein
Gewicht; die beiden übrigen tauschen spiegelsymmetrisch, und jede Kante trägt ± die Hälfte ihrer Länge 2π (+π, −π, −π). Die ½ ist hier die
Spiegelsymmetrie der Kante, verwandt mit der Sektor-½ aus CT-001 Schritt 2, aber nicht dieselbe Herleitung.

**5. Wo γ_M stehen kann.** In beiden Modellen ist die Krümmung eine rationale Funktion der Form, und alle kanonischen
Flüsse sind elementare Zahlen (π, √2). γ_M = 0,237533 ist dagegen die Wurzel der Zählgleichung über alle Spins. Aus der
Formgeometrie allein entsteht γ_M deshalb nicht; jede Schleife mit Holonomie γ_M wäre nach dem Ziel gewählt. γ_M kann nur
als **Umrechnungsfaktor** eintreten: als Kopplung des Zusammenhangs selbst, wie beim Ashtekar–Barbero-Zusammenhang
A = Γ + γK, dessen γK-Teil die γK-Phase pro Radiant aus r10.1 und CT-001 Schritt 3 ist. Dann lautet die Lesart:

  ΔΦ = γ_M · (Restdrehung des größten Formzyklus in Umläufen) = γ_M · ½ = γ_M/2.

Die ½ käme damit aus einer Rechnung statt aus der Wahl „eine Lichtquerung“, und sie ist unabhängig vom Massengesetz.
Gesetzt bleiben aber drei Dinge:
- γ_M als Kopplung, also der Frame M und die Zählregel;
- die Wahl gerade des größten Zyklus (Rand des Formraums);
- die Normierung auf einen Umlauf 2π.

## Bewertung
- **Teilweise getragen, nicht hergeleitet.** Die Restdrehung als Holonomie ist eine saubere Rechnung. Sie liefert
  eine ½ ohne |m| = ½ und ohne Lichtquerung. γ_M entsteht nicht aus der Geometrie; es bleibt Kopplung bzw.
  Umrechnungsfaktor und ist eingesetzt.
- Das Kreismodell ohne formabhängige Trägheit hat überhaupt keine Restdrehung. Für das Zeitbild heißt das: Zeit
  (Holonomie) setzt voraus, dass die Gewichte an der Form hängen. Das passt zur Abfolge HS(0) → HS(2) im
  Gedankenexperiment (erst mit formabhängigen Gewichten und zwei Formrichtungen entsteht Fläche), ist aber nur eine Lesart.
- Der Koide-Befund in Modell B ist eine Umschreibung des bekannten 45°-Winkels und zählt nicht als Bestätigung.
- Drehsinn: wie in allen Bildern gesetzt (Vorzeichen von a·b bzw. Umlaufsinn des Zyklus).
- Datenbezug: −½ ist exakt, die Daten verlangen κ·s = 0,49982 (2,3σ, Spannung von H102, unverändert).
- Bilanz der Setzungen: Die offene Wahl wandert von „eine Lichtquerung“ (I1, 14.11.) zu „größter Formzyklus“. Beide
  sind Auswahlen mit bekanntem Ziel. Ein Grund, warum die Natur den Randzyklus durchläuft (etwa: jeder Sektor einmal
  leer, also jede Generation einmal masselos), fehlt.
- Zurückgestellte Ideen: I1 berührt (Lesart der ½), kein neuer Auslöser. OP1–OP5, C5, C6/T2 und alle Guards
  unverändert; CT-001/CT-002 nicht umgestuft; H100, H102 unberührt.

## Mögliche nächste Schritte (nur auf Entscheidung)
- Prüfen, ob der Randzyklus eine Bedeutung im Companion hat (Rand des Bogens |θ| = π/12, Rang-2-Rand der Gram-Notiz:
  leichtester Zustand masselos). Wenn ja, wäre „größter Zyklus“ keine freie Wahl mehr. Dafür vorher eine Vorab-Notiz.
- Den Zusammenhang statt mechanisch als Ashtekar–Barbero-Holonomie einer Punktierung aufstellen, damit γ als Kopplung
  nicht eingesetzt, sondern aus r10.1 übernommen wird.
