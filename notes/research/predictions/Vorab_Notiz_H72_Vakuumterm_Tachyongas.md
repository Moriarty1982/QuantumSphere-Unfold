# Vorab-Notiz H72: Kann ein Gas tachyonischer Moden einen Λ-artigen Term erzeugen, und legt die Frame-Struktur ihn fest?

**Geschrieben und committet am 5. November 2026 vor der Rechnung. Status: vorregistriert; a und b nicht blind (analytisch vorab gesehen), c offen.**

## Vorwissen geprüft
- H71 (`Ergebnis_H71_Massenpartner.md`): Das Tachyonbild mit F3-Vorzeichen und Masse gibt Moden mit ω² = k² − m². Die Mode λ = +1 hat negative, λ = −1 positive Energiedichte. Keine einzelne Mode hat T ∝ η.
- H69, H70, k177: Masselose Felder geben nie einen Λ-artigen Rest (spurfrei).
- `OP5_Neutral_Pair_Dynamics_Result.md`: Neutralität legt die Vakuumhöhe nicht fest; ein Frame-Vorzeichen ist keine Quanten-Gewichtung. H72 ist klassisch.
- Suche nach „tachyon gas / Tachyongas / equation of state / Zustandsgleichung w“ in `analysis/OP5_*`, `llm/Ergebnis_*`, `Erkundung_*`: keine Rechnung zu einem Gas tachyonischer Moden.

## Analytisch vorab gesehen (offen gelegt)
Für eine ebene Mode ist T_μν = N·p_μp_ν mit p = (ω, k) und Normvorzeichen N (k179: T_tt : T_zz = ω² : k²). Inkohärente, isotrope Mittelung (Kreuzterme verschiedener Impulse fallen heraus) gibt ρ = Σ N_i ω_i² und T_ij = (Σ N_i k_i²/3)δ_ij. Ein Λ-artiger Term T_μν = ρ η_μν verlangt Σ N_i(k_i² + 3ω_i²) = 0 bei ρ ≠ 0. Bei einem einzigen Vorzeichen von N ist das unmöglich (w = k²/3ω² > 0); mit beiden Vorzeichen ist es möglich.

## Aufbau (k180)
Moden aus k179 (V2, s = −1, m = 1), Normierung |ψ|² + |χ|² = 1. Richtungen ±x, ±y, ±z mit gleichem Gewicht (exakt isotrop für zweite Momente, Mittel über n gleich null). Mittelung: Summe der Einzel-T (inkohärent).

## Hypothese H72
- **H72a (Existenz, nicht blind):** Es gibt eine isotrope, inkohärente Überlagerung von V2-Moden mit nichtnegativen Gewichten, deren gemitteltes T gleich ρη mit ρ ≠ 0 ist. Geprüft an einem expliziten Beispiel mit zwei Impulsbeträgen und beiden λ: ‖T − ρη‖/|ρ| ≤ 1e-12.
- **H72b (nicht festgelegt, nicht blind):** In dieser Konstruktion ist ρ nicht festgelegt. Eine Einparameter-Familie von Gewichten gibt beliebige Werte und beide Vorzeichen. Kontrolle: V1-Moden (s = +1) geben nie w = −1 (w ≥ 0).
- **H72c (Frame-Gewichte, offen):** Moden bei einem Impulsbetrag k, Gewicht p₊ auf der einen und p₋ auf der anderen λ-Mode, nach Konvention F im Materie-Frame (x = β_sym² = 0,5493²). Beide Zuordnungen werden gerechnet: (i) p₊ auf λ = −1 (positive Energie), (ii) p₊ auf λ = +1. Frage: Gibt es k*/m ∈ (1, 20], bei dem w = −1 gilt? Bestätigt („die Frame-Gewichte legen einen Λ-Punkt fest“), wenn in mindestens einer Zuordnung genau ein solches k* existiert (Nullstelle von w + 1 mit Vorzeichenwechsel); widerlegt, wenn in keiner. Zusätzlich berichtet: dasselbe für die Photon-Gewichte (½, ½).

## Kontrollen
- Einzel-T der Moden wie in k179 (Feldgleichung ≤ 1e-12, T ∝ pp auf ≤ 1e-12).
- Isotropie der Richtungsmittelung: Mittel von T_ij ∝ δ_ij auf ≤ 1e-12.

## Grenzen (vorab)
Klassisch; inkohärente Mittelung ist eine Annahme, keine Folge der Feldgleichungen. Negative Energiedichten (λ = +1) sind Moden eines Feldes negativer Norm, deren Stabilität offen ist. Selbst ein k* aus H72c legt nur fest, wo w = −1 ist, nicht die Höhe ρ, die mit der Gesamtamplitude skaliert.
