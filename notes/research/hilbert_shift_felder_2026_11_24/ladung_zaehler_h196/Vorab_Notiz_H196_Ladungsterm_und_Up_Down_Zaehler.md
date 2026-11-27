# Vorab-Notiz H196: Verschiebt der Ladungsterm (H182) das Quintik-Glied für Up anders als für Down?

**Datum:** 27.11.2026. **Nummern:** H196 (Test), k404 (Rechnung). **Strang:** Quarkmassen; offener Punkt aus H195 (der Zähler
der H188-Form und der Up/Down-Unterschied bleiben frei). **Anlass:** „mach das" des Autors (27.11., 10:13): prüfen, ob der
Ladungsterm aus H182 das Quintik-Glied (l_k²) für Up anders verschiebt als für Down.

## Ausgangspunkt (belegt)
- **H195:** Masse = Krümmung / kinetische Norm; der Nenner (l_i+l_j)² folgt aus der W²-gewichteten Norm (Peirce ½(l_i+l_j),
  verifiziert). Der Zähler ist ein Polynom in l_k; l_k² erscheint ab Potentialgrad 5. a, b je Sektor bleiben frei.
- **H182:** Der Tausch J lässt im Farbblock genau eine ladungsungerade hermitesche Form zu: h = Ψ†(Q₀−½)Ψ. Up (Ladung ⅔) und
  Down (Ladung ⅓) unterscheiden sich durch das **Vorzeichen** des ladungsungeraden Anteils: Größe_s = (gerade) + s·(ungerade),
  s = +1 (Up), −1 (Down).
- **H186:** Die ladungsungeraden Krümmungen (Up−Down)/2 der Mode (i,j) sind (Wolfram exakt): c1 ⅔; c2 ⅓(l_i+l_j); c4/c5
  ⅓(l_i²+l_j²); c7/c9 ⅙(l_i+l_j)²; c11 ½(l_i²+l_j²)+⅓l_il_j. H186 hat sie als **direkte** Massenquelle (Frequenz² = Masse) geprüft
  und widerlegt: die symmetrischen Krümmungen machen die zwei schwersten Moden fast gleich schwer (r₂ ≈ 1 statt 0,05).

## Der neue Punkt
H186 hat **vor** H195 gerechnet und die Krümmung **nicht** durch die kinetische Norm (l_i+l_j)² geteilt. Genau dieser Nenner
verstärkt die schwerste Mode (kleinstes l_i+l_j) und ist der fehlende Baustein. Auf dem festen Vakuum (Tr = 3, K = ⅔ ⇒ e₂ = 3/2)
werden die ladungsungeraden Zähler zu (sympy):

| Kandidat | ladungsungerader Zähler-Anteil |
|---|---|
| c1 | 2/3 |
| c2 | 1 − l_k/3 |
| c4/c5 | 2 − l_k²/3 |
| c7/c9 | 3/2 − l_k + l_k²/6 |
| c11 | 7/2 − l_k − l_k²/6 |

**Mehrere ladungsungerade Terme tragen ein l_k²** (c4/c5, c7/c9, c11). Der Ladungsterm **kann** also das Quintik-Glied zwischen Up
und Down verschieben. Die Frage ist, ob das die gemessenen sechs Massen trägt.

## Modell
Gemeinsame Skala (Yukawa, M_Z; Up und Down schon gleich normiert). Für Generation mit eigenem Index k, Ladung s = ±1:

  **m_s(k) = [ A·l_k + B·l_k² + s·γ·O(l_k) ] / (l_i+l_j)²**,

A, B ladungsgerade (für Up und Down **gemeinsam**), γ eine ladungsungerade Stärke, O(l_k) der **feste** Zähler eines einzelnen
ladungsungeraden Kandidaten aus H186. Drei Parameter (A, B, γ) für sechs Massen.

## Teile und Kriterien
- **H196a (nicht blind).** Reduktion der ladungsungeraden Krümmungen auf l_k (oben, sympy; Wolfram-Gegenprobe).
- **H196b (Test — fester Kandidat, 3 Parameter).** Für jeden einzelnen Kandidaten O ∈ {c1, c2, c4/c5, c7/c9, c11}: gemeinsamer
  Fit (A, B, γ) über beide Sektoren.
  - **bestätigt:** ein einzelner Kandidat bringt beide Sektoren alle drei Massen < 3σ mit nur (A, B, γ) — dann erklärt der
    Ladungsterm aus der Feldgleichung den Up/Down-Unterschied, und der H195-Nenner behebt H186.
  - **teilweise:** ein Kandidat trifft einen Sektor < 3σ, nicht beide; oder die volle Ladungsstruktur (A,B,C,D, 4 Parameter, freie
    ungerade Form) trifft und zeigt, dass der ladungsungerade l_k²-Anteil D ≠ 0 mit dem richtigen Vorzeichen ist, aber kein fester
    Kandidat mit 3 Parametern reicht.
  - **widerlegt:** auch die volle Ladungsstruktur gibt den Unterschied nicht, oder das ladungsungerade l_k² hat das falsche
    Vorzeichen (Down würde quadratischer als Up).
- **H196c (Bericht).** Die volle Ladungsstruktur m_s = [A l_k + B l_k² + s(C l_k + D l_k²)]/(l_i+l_j)² (4 Parameter, 2 dof): C, D
  und ihre Vorzeichen; ist D (ungerades l_k²) nötig und mit welchem Vorzeichen? Vergleich mit H194 (dieselbe Parameterzahl).
- **Kontrolle.** 2000 erfundene Massenpaare durch denselben 3-Parameter-Fit je Kandidat, Trefferquote eichen.

## Erwartung (offen gelegt)
Offen. H186 (ohne Nenner) scheiterte an r₂ ≈ 1; der H195-Nenner (l_i+l_j)² verstärkt die schwerste Mode und könnte das beheben —
das ist der Grund, warum der Test lohnt. Ich halte **teilweise** für wahrscheinlich (die volle Ladungsstruktur trägt wie H194,
ein fester Kandidat mit 3 Parametern eher nicht), aber ein Treffer eines einzelnen Kandidaten wäre ein echter Befund: dann käme der
Up/Down-Unterschied aus der Ladung und der Feldgleichung, nicht aus vier freien Zahlen. Entscheidend ist das Vorzeichen des
ladungsungeraden l_k².

## Werkzeuge
Python (numpy, sympy) für die Reduktion, die gemeinsamen Fits und die Kontrolle; Wolfram Language für die exakten ladungsungeraden
Krümmungen als Gegenprobe. Qiskit nicht nötig.

## Vorwissen geprüft
- `.../ladung_h182/` (H182): J, h = Ψ†(Q₀−½)Ψ, Vorzeichen s je Ladung, V_± = (A±C)t + (B±D)t².
- `.../ladungsterm_h186/` (H186): ladungsungerade Krümmungen c1–c11, als direkte Quelle widerlegt (r₂ ≈ 1, ohne Nenner).
- `.../feldgleichung_form_h195/` (H195): Nenner (l_i+l_j)² hergeleitet, Zähler frei.
- `.../h188_form_h194/` (H194): Up ~ l_k²/z (b/a −57,9), Down ~ l_k/z (b/a −0,085), Faktor 680.
- Memory: Ladungsterme als Massenquelle bisher widerlegt (H184–H190); hier neu: ladungsungerade **Zähler** über dem H195-Nenner.

## Grenzen (vorab)
Zweite Variation um das ruhende Vakuum; die ladungsungeraden Krümmungen sind aus H186 übernommen (dort Python über vier Vakua und
Wolfram exakt). Die Wahl „ein einzelner Kandidat" ist die scharfe Vorhersage; die volle Struktur (4 Parameter) ist nur Bericht.
OP3/OP4 bleiben offen.
