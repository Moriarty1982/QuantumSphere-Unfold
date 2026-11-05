# Vorab-Notiz H70: Welche Kopplung des Versatzes an die Expansion erhält das M–T-Paar, und entsteht ein Vakuumterm?

**Geschrieben und committet am 5. November 2026 vor der Rechnung. Status: vorregistriert, nicht blind (siehe „analytisch vorab bekannt“).**

## Vorwissen geprüft
- H69 (`Ergebnis_H69_MT_Paar_flach.md`): Im flachen Raum hat das Paar aus zwei gegenläufigen Weyl-Wellen und ihrem um δ versetzten T-Bild (s_T = −1) keinen Nettostrom (genau bei Δω·δ ≡ π mod 2π) und keinen Nettoenergie-Impuls.
- `thm:expansion` (Monolith ~Z. 6925): a(t) ∼ τ_n = √(t_n² − β_sym²), β_sym als Frame-Versatz; die Riemann-Herleitung ist zurückgezogen (r04).
- `OP5_Neutral_Pair_Dynamics_Result.md`: Neutralität legt die Vakuumhöhe nicht fest; ein Frame-Vorzeichen ist keine Quanten-Gewichtung. H70 bleibt klassisch.
- `Ergebnis_H48_Einfrieren_beta.md`: anderer Mechanismus (eingefrorene Länge), nicht der Versatz eines Paares.

## Aufbau (k176)
- Räumlich flaches FRW, g = a(τ)²η in konforma­ler Zeit τ, Weyl-Felder masselos. Konforme Invarianz: ψ = a^{−3/2}χ mit χ als Lösung der flachen Weyl-Gleichung in (τ, x); T^μ_ν = a^{−4}·T^μ_ν[flach, χ]. Kontrolle unten.
- Paar wie in H69 in konformen Koordinaten: χ_M = a₁e^{−iω₁(τ−z)}u₁ + a₂e^{−iω₂(τ+z)}u₂, χ_T(τ, z) = −iσ_z χ_M(τ + Δτ(τ), z), s_T = −1.
- Der Versatz δ(t) ist in kosmischer Zeit t gegeben; der konforme Versatz ist Δτ(t) = ∫_t^{t+δ(t)} dt′/a(t′).
- **Kandidaten** (vorab, Einheiten H₀ = 1):
  - **C1:** δ = c/H(t), die Hubble-Zeit;
  - **C2:** δ mitbewegt fest, also Δτ = c konstant;
  - **C3:** aus `thm:expansion`: δ(t) = t − √(t² − β²) mit β = β_sym = 0,5493.
- Hintergründe: Materie, a = (t/t₀)^{2/3} mit t₀ = 2/3, und Strahlung, a = (t/t₀)^{1/2} mit t₀ = 1/2. Fenster a ∈ [0,5; 2].
- Δω wird so gesetzt, dass Δω·Δτ = π bei a = 1 (heute). c = 0,1 für C1 und C2.

## Analytisch vorab bekannt (offen gelegt)
- Ist Δτ zeitabhängig, so löst χ_T die Weyl-Gleichung nicht mehr; der Fehler ist ∝ Δτ′(τ)·∂_τχ. Die Bilanzen gelten nur, wo Δω·Δτ ≡ π.
- C2 erhält alles exakt. Für C1 ist Δτ ≈ c/(aH) nur bei ä = 0 konstant; für C3 ist Δτ ≈ β²/(2ta) nie konstant.
- Diagonalanteile der Wellen heben sich unabhängig vom Versatz auf. Ein Rest kann nur aus den Kreuztermen kommen, und diese laufen ∝ e^{∓i(ω₁+ω₂)z}; ihr räumliches Mittel ist null.

## Hypothese H70
- **H70a (welche Kopplung):** Nur C2 erhält das Paar über das ganze Fenster: Weyl-Residuum von χ_T, Strombilanz und Energiebilanz ≤ 1e-12 relativ. C1 und C3 verletzen alle drei mit relativen Resten ≥ 1e-3 irgendwo im Fenster, in beiden Hintergründen.
- **H70b (kein Vakuumterm):** In keinem Kandidaten entsteht ein homogener Rest. Das räumliche Mittel des Energierests über eine Periode in z ist ≤ 1e-12 relativ zur Amplitude des Rests, in beiden Hintergründen.

## Kontrollen (Gültigkeit)
- Konforme Invarianz: e^μ_a σ̄^a(∂_μ + Γ_μ)(a^{−3/2}χ) = 0 mit der Spin-Verbindung des FRW-Koframes (e^a_μ = aδ^a_μ), an 50 Zufallspunkten für zufälliges a(τ), Residuum ≤ 1e-10.
- Bei a ≡ 1 reproduziert k176 H69 (Residuen ≤ 1e-12).

## Entscheidung (je Teil)
| Ergebnis | Bedingung |
|---|---|
| bestätigt | wie in H70a bzw. H70b formuliert |
| widerlegt | H70a: C2 verletzt etwas (≥ 1e-3), oder C1 bzw. C3 erhalten das Paar im ganzen Fenster (≤ 1e-12). H70b: räumliches Mittel ≥ 1e-3 in einem Kandidaten |
| unentschieden | dazwischen |
| ungültig | eine Kontrolle verfehlt |

## Grenzen (vorab)
- Klassisch; die Quanten-Vakuumenergie und die Konstante C bleiben unberührt.
- s_T = −1 bleibt Eingabe. Die Felder sind Testfelder auf vorgegebenem FRW (keine Rückwirkung auf a); wegen T_gesamt = 0 in C2 ist das dort konsistent, in C1 und C3 nicht.
- Eine Bestätigung von H70b heißt: Ein Paar mit falscher Kopplung erzeugt Inhomogenität (wellenartige Spannungen), keinen Λ-artigen Term.
