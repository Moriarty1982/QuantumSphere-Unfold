# Vorab-Notiz H224 (k438): Ist der gemeinsame Drehwinkel φ eine Wigner-Drehung aus zwei Frame-Boosts?

**Datum:** 2026-11-28, vor der Rechnung committet. **Auftrag:** Marc 28.11. (Karte: Vorzeichen setzen, „weiter mit Winkel φ“). Weg „Wigner-Drehung“ ist meine
Empfehlung auf der Folgekarte; begonnen, während die Wahl aussteht.
**Werkzeuge:** Python (`k438_test_h224.py` → `k438_out.txt`), Wolfram unabhängig (`k438b_gegenprobe.wl` → `k438b_out.txt`). Qiskit nicht einschlägig.

## Ausgangslage
H221: Der gemeinsame Versatz beider Lepton-Sektoren ist eine Drehung χ → χ + φ, dimensionslos und für beide Sektoren gleich. H222/H223 + Wahl des Autors: Zweig über
ein gesetztes Vorzeichen. Offen ist nur der Wert φ = x_lepton. Unter J (K = ⅔) ist x = π/12 − δ* = 0,0395773 mit σ ≈ 7,8·10⁻⁷ (H158d, nur m_τ); mit freiem a
(H213) 0,0395746 ± 0,0000063. Neutrino: x_ν = 0,04336 ± 0,00213.

## Idee (Hypothese H224)
Eine Drehung, die dimensionslos ist und alle Sektoren gleich trifft, entsteht in der Relativitätstheorie von selbst: Zwei nicht kollineare Boosts hintereinander ergeben
einen Boost und eine **Wigner-Drehung** ω, tan(ω/2) = sin θ / (coth(a/2) coth(b/2) + cos θ) (Rapiditäten a, b, Winkel θ zwischen den Boost-Richtungen). Der Rahmen hat
feste Rapiditäten: ε = artanh β_sym = 0,61752 (Frame-Versatz R → M bzw. R → T, Maske H45) und 2ε = arcosh γ_L = 1,23504 (M ↔ T). Er hat feste Winkel zwischen
Richtungen: π/2 (Tachyon-Abbildung z ↦ iz, Re ↔ Im), π/4 (Achteldrehung, Sektorschritt H171), 2π/3 und π/3 (Generationsdreieck).
**H224:** φ = ω/n für eine dieser Kombinationen, n aus einer kleinen Liste.

## Vorwissen geprüft
- Wertsuchen ohne Treffer: H151d (540 Vergleiche, Setzungen), H158d (720 Kandidaten, δ = 2/9), H167d1 (42 Kandidaten, α/α′), op3_time_cycle, op3_correction_term.
- CT-002 (I1, `counterterms/`, `op3_i1_string_bridge_2026_11_14.md`, H102): x = γ_M/6 = 0,0395888; mit freiem a 2,2σ, unter J (σ 7,8·10⁻⁷) rund 15σ daneben.
- Frame-Größen: β_sym = 0,5494056410, γ_L = 1,8646997646 (r67, Zählpostulat); ε = artanh β_sym (H45); β_sym² = (γ_L − 1)/(γ_L + 1), also 2ε = arcosh γ_L.
- Eine Wigner-/Thomas-Drehung ist im Repo nicht gerechnet (Suche „Wigner“, „Thomas“ in `notes/research/`, `analysis/`: keine Fundstelle zu φ).

## Kandidatenliste (vorab, vollständig)
- Rapiditätspaare (a, b): (ε, ε), (2ε, 2ε), (ε, 2ε).
- Winkel θ: π/2, π/4, 2π/3, π/3.
- Teiler n: 1, 2, 3, 6.
- Zusammen 3 × 4 × 4 = 48 Kandidaten φ_pred = ω(a, b, θ)/n.

## Kriterien (vorab)
- **Treffer (streng):** |φ_pred − 0,0395773| < 3 · 7,8·10⁻⁷ (unter J).
- **Nah (locker):** |φ_pred − 0,0395773| / 0,0395773 < 1 %; dazu Zufallserwartung der lockeren Treffer aus der Verteilung der 48 Werte (gleichverteilte Lage im Bereich
  der Kandidaten) und die Zahl der Kandidaten innerhalb 2σ von x_ν (nur als Bericht, nicht trennscharf).
- **Urteil:** trägt bei mindestens einem strengen Treffer; trägt teilweise, wenn nur lockere Treffer über der Zufallserwartung liegen; sonst widerlegt.
- **Gegenprobe:** Wolfram rechnet ω unabhängig aus der Komposition zweier 4×4-Boostmatrizen (Polarzerlegung), nicht aus der Formel.

## Grenzen (vorab)
Die Zuordnung „Boost-Richtungen im Winkel θ“ ist eine Lesart; welcher physikalische Vorgang die zwei Boosts hintereinanderschaltet, ist nicht hergeleitet. Ein Treffer
wäre ein Zahlenhinweis, keine Herleitung, solange diese Zuordnung offen ist.
