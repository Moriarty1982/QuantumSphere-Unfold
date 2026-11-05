# Vorab-Notiz H71: Massiver Partner als Antiteilchen, Tachyonbild oder Spiegelteilchen

**Geschrieben und committet am 5. November 2026 vor der Rechnung. Status: vorregistriert; a und b nicht blind (analytisch bekannt), c offen.**

## Vorwissen geprüft
- H69, H70, k177, k178 (`Erkundung_MT_Luecke.md`, Nachträge 1–5): Das neutrale Paar braucht den T-Anteil mit negativer Norm (F3) und die Photon-Gewichte. Masselose Felder geben nie einen Λ-artigen Rest. Auf der Kompensatorachse sind Tachyon-Abbildung und Zeitumkehr gleich; Massenterme koppeln an einen Partner mit T-Gewichten, der zusätzlich ladungskonjugiert ist.
- r42, Lesart 2: „Matter frame and tachyon frame are in the model particle and antiparticle with mirrored chirality“ (Lesart). r44: Massenterme sind antilinear und enthalten die Zeitumkehr.
- Suche nach „mirror matter / mirror particle / Spiegelteilchen“ in Quellen, `analysis/` und Notizen: nur r42 und Stellen, an denen Materie und Tachyon „mirror images“ auf der s-Achse heißen (v4.8.0-r19). Keine Rechnung zu einem Spiegelsektor.
- Literatur (Vorwissen, nicht nachgeschlagen): Spiegelmaterie (Lee–Yang 1956; Kobzarev–Okun–Pomeranchuk 1966): ungekoppelte Kopie mit gespiegelter Chiralität, positiver Energie, nur gravitativ an uns gekoppelt. Tachyonische Dirac-Gleichung (Chodos–Hauser–Kostelecký 1985) mit ω² = k² − m².
- `OP5_Neutral_Pair_Dynamics_Result.md`: Ein Frame-Vorzeichen ist keine Quanten-Gewichtung; alles hier ist klassisch.

## Aufbau (k179)
Flach, A = 0, Torsion vernachlässigt. Linkshändiges ψ (σ̄^μ∂_μ = ∂_t − σ·∇) und rechtshändiger Partner χ (σ^μ∂_μ = ∂_t + σ·∇):
L = ψ†iσ̄^μ∂_μψ + s·χ†iσ^μ∂_μχ − m(ψ†χ + χ†ψ).
Ebene Wellen e^{−i(ωt − kz)}, ψ mit σ_zψ = λψ, χ aus der Feldgleichung.
- **V1, Antiteilchen bzw. gekoppelter Spiegelpartner:** s = +1. Analytisch gleichwertig: Ein rechtshändiges Feld ist das Konjugierte eines linkshändigen.
- **V2, Tachyonbild:** s = −1 (F3).
- **V3, ungekoppelter Spiegelsektor (Lee–Yang):** eine positive Kopie von V1 ohne Kopplung an M. Wird nur analytisch vermerkt: Ströme und Energien addieren sich.

Gemessen für k ∈ {0,1; 0,5; 1; 2; 5}·m (V2 nur |k| ≥ m), λ = ±1:
- Dispersion;
- K-Strom j = j_ψ + s·j_χ mit j_χ = χ†σ^aχ;
- T_μν = T_ψ + s·T_χ (symmetrisch, auf der Schale) und seine Spur;
- Gewichtsverhältnis |χ|²/|ψ|² (Erkundung: Vergleich mit p₋/p₊ = β_sym² aus Konvention F, ohne Kriterium).

## Hypothese H71
- **H71a (nicht blind):** V1 hat ω² = k² + m², V2 hat ω² = k² − m²; der Partner negativer Norm macht die Masse tachyonisch.
- **H71b (nicht blind):** In V1 ist j⁰ = |ψ|² + |χ|² > 0. Die K-Bedingung ist für jede Lösung verletzt; ebenso in V3.
- **H71c (offen):** In V2 gilt die K-Bedingung j = 0 für alle Moden mit |k| > m und beide λ.

## Kontrollen
- Feldgleichungen der Moden, Residuum ≤ 1e-12.
- ∂^μT_μν = 0 für eine Überlagerung zweier Moden (Differenzen, relativ ≤ 1e-6).
- Grenzfall m → 0 gibt die masselosen Ergebnisse (Spur 0).

## Entscheidung
| Teil | bestätigt | widerlegt |
|---|---|---|
| a | Dispersion auf ≤ 1e-12 wie angegeben | Abweichung ≥ 1e-6 |
| b | min j⁰ > 0 für alle V1-Moden | ein V1-Modus mit j = 0 |
| c | max |j|/(|ψ|² + |χ|²) ≤ 1e-12 für alle V2-Moden | ≥ 1e-3 für einen V2-Modus |
| ungültig | eine Kontrolle verfehlt | |

Zusätzlich berichtet, ohne Kriterium: T_μν, Spur und Gewichtsverhältnis je Variante. Ein Vakuumbeitrag hätte T_μν ∝ η_μν; für einzelne ebene Wellen wird keiner erwartet, das räumliche oder Richtungsmittel bleibt eine spätere Frage.
