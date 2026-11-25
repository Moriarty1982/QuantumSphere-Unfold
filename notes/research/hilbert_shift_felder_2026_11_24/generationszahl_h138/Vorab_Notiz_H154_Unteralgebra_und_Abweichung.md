# Vorab-Notiz H154: Erzwingt die Algebra die Schleife über {1, U}? Woher kommt die Abweichung zwischen ⅔ und dem Messwert?

**25.11.2026, vor jeder Rechnung committet.** Anlass: Autor „ja und prüfe woher die abweichung kommt“ (nach H153). Gelesen als zwei Fragen: (1) Gibt es einen algebraischen
Grund, dass im Fluss nur die Unteralgebra {1, U} läuft (Auswahlregel, Eichung, Ladungserhaltung, Entkopplung bzw. Masselosigkeit der zweiten Ebenenrichtung)? (2) Woher kommt
die Differenz zwischen K = ⅔ (H153c) und dem Messwert? Getrennt: Messrauschen, Laufen der Massen, Frame-Effekt, δ-abhängige Korrektur. Skalenfrei, kein Vorzeichen gesetzt.
Vergeben: H154, Skripte k337 (Python) und k337b (Wolfram). Qiskit nicht vorgesehen (keine Schaltungsfrage). Kein HDL/MMA-Vergleich.

## Vorwissen geprüft
- H153 (k336): Normierungen sind Umparametrisierungen; nur n_A = n_B = 1 gibt K = ⅔ exakt (Tausch J exakte Symmetrie des Flusses).
- H151 (k334): Verschiebung K ≈ 0,672 kommt aus 1 gegen 2 Komponenten; Form S lässt K exakt invariant; ein Boost hält den Lichtkegel fest.
- H149: Ψ = cos θ + sin θ·U; exp(αU) verschiebt θ um α (die U(1) aus U dreht 1 in U, nicht U in U′).
- H133 (k302): bei voller Norm sind neue Felder Goldstone-Richtungen (m = 0).
- H1 (v4.8.0, Ergebnis_H1_Koide_Phase.md): mit laufenden MS-bar-Massen bei M_Z (Antusch–Hinze–Saad 2025) ist Koide verletzt, K = 0,6678.
- H146-Vorab: Polmassen m_e = 0,51099895, m_μ = 105,6583755, m_τ = 1776,93 MeV.
- **Vor dieser Notiz bemerkt (nicht blind):** Der seit H152 benutzte Messwert 0,666661 ± 0,000007 entspricht dem älteren m_τ = 1776,86 ± 0,12 MeV. Mit m_τ = 1776,93 ± 0,09 MeV
  ist K = 0,6666645 ± 0,0000051, also 0,43σ unter ⅔ statt 0,81σ. Für ⅔ exakt bräuchte es m_τ = 1776,969 MeV.

## Teil 1: Auswahlregel für {1, U}
- **H154a (nicht blind, analytisch):** Eine Symmetrie (Auswahlregel, Ladungserhaltung) beschränkt, welche Operatoren im Potential stehen, nicht, welche Felder in der Schleife
  laufen: Die Spur ½Tr(∂²V)² läuft über alle Felder, die es gibt. Ein Feld fällt nur heraus, wenn es fehlt oder schwer ist (Entkopplung). Im skalenfreien symmetrischen
  Bereich sind alle Massen null, also entkoppelt nichts. *Kriterium:* symbolisch: (1,2)-β = (1,1)-β + Schleife der zweiten Ebenenrichtung y₂, mit Beitrag
  [2κ², 8κλ_B, 8λ_B²] (Vorhersage), der für κ, λ_B ≠ 0 nicht verschwindet.
- **H154b (gewertet):** Ladungserhaltung mit U als Ladungsachse. Die U(1) aus exp(αU) mischt 1 und U (H149b); die U(1), die die Kopien-Ebene dreht, mischt U und U′.
  Vorhersage: Es gibt keine Wirkung einer der beiden auf (φ, y₁, y₂), unter der {1, U} invariant und U′ geladen ist und die zugleich V erhält. *Kriterium:* symbolisch,
  invariante Unterräume der beiden Erzeuger.
- **H154c (gewertet):** Masselosigkeit. Am GW-Punkt des (1,2)-Flusses ist die zweite Ebenenrichtung Goldstone (m = 0) und trägt zum Coleman–Weinberg-Potential längs der
  flachen Richtung nichts bei. Vorhersage: Das ändert den Ort des GW-Punkts nicht, weil der Fluss bis dorthin im symmetrischen Bereich läuft. *Kriterium:* Massen am
  GW-Punkt (y₂ exakt 0) und K unverändert gegenüber H150/H153.
- **H154d (gewertet):** Eichung der Ebenen-Drehung (skalare QED auf y = y₁ + iy₂, φ neutral; 16π²β_λB += −12e²λ_B + (3/2)e⁴, β_κ += −6e²κ, β_e = e³/3, Landau-Eichung).
  Gitter: e₀² ∈ {0,05; 0,1; 0,2; 0,5; 1}, λ ∈ {0,1; 0,2}, κ/λ ∈ {−1,5; −1,0; −0,5; −0,2}, Start λ_A = λ_B = λ. *Kriterien:* startunabhängig, wenn Std(K) < 10⁻³;
  Treffer, wenn |K − ⅔| < 1,5·10⁻⁵ (3σ mit σ = 5,1·10⁻⁶). Vorhersage: startabhängig, kein systematischer Zug auf ⅔ (der Goldstone wird gefressen, aber das Eichfeld läuft mit
  und bricht den Tausch, weil φ neutral ist).

## Teil 2: Woher kommt die Abweichung?
- **H154e (gewertet, Messrauschen):** K aus Polmassen PDG (m_τ = 1776,93 ± 0,09 MeV) mit Fehlerfortpflanzung; Anteil der drei Fehler. *Kriterium:* |⅔ − K|/σ < 2 heißt
  „mit Messrauschen verträglich“. Vorhersage: 0,43σ, Fehler zu > 99 % aus m_τ.
- **H154f (gewertet, Laufen):** K mit einschleifig laufenden QED-Massen m(μ) = M[1 − (α/π)(1 + ¾ ln(μ²/M²))] an gemeinsamer Skala μ ∈ {m_e, m_μ, m_τ, M_Z}, sowie mit
  jeweils eigener Skala m(M). Vorhersage: gemeinsame Skala verschiebt K um ≫ 1σ (weg von ⅔); eigene Skala verschiebt K nur um O(α²), weil der gemeinsame Faktor 1 − α/π in K
  herausfällt. Koide gilt für Polmassen; das Laufen erklärt die Abweichung nicht, es würde sie vergrößern. Vergleich mit H1 (0,6678 bei M_Z).
- **H154g (nicht blind, Frame):** Form S lässt K invariant (H151e). Kriterium: symbolisch K(Form S) − K = 0. Beitrag zur Abweichung 0.
- **H154h (nicht blind, δ):** K = 1/(3 cos²θ) hängt nicht von δ ab. Kriterium: ∂_δK ≡ 0 symbolisch. Eine δ-abhängige Korrektur durch die eingefrorene Richtung gibt es in K
  daher nicht; eine Abweichung bräuchte Δθ = 3ΔK/4 bei π/4, also Δθ ≈ −1,6·10⁻⁶, und dafür einen tauschbrechenden Term.

## Grenzen
- Eine Schleife; skalare QED nur als Modell der Eichung (Landau-Eichung, Normierung wie oben); QED-Laufen einschleifig, ohne Hadronen- und schwache Beiträge.
- OP3 offen; kein Vorzeichen gesetzt; kein Guard wird berührt.
