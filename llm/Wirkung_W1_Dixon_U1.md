# Wirkung W1: Einstein–Cartan–Dirac auf der Dixon-Ablage mit dem U(1) aus L_{e₇}

**4. November 2026. Status: Aufstellung und erste Identitäten (Erkundung, ohne Kriterium).** Grundlage sind die fünf Autorentscheidungen in `Bestandsaufnahme_Wirkungsansaetze.md`.

## Felder (alle unabhängig variiert, W1)
- Koframe e^a_μ, Lorentz-Verbindung ω_μ^{ab} = −ω_μ^{ba} (Entscheidungen 1 und 3);
- U(1)-Potential A_μ, reell, Erzeuger Q_J = i·L_{e₇} auf der Dixon-Ablage (Entscheidung 4);
- Spinor Ψ: Lorentz-Spinor ⊗ Dixon-Ablage, beschränkt auf das Bild von P_C7 := C_ch = ½(1 + J), J = i·L_{e₇} (Entscheidung 5). Sektorweise über die vier Projektoren P_s aus r48 (Ränge 1, 3, 3, 1).

## Wirkung (Frame M, Entscheidung 2)
S = ∫ e [ (1/2κ) R(e, ω) + ½(Ψ̄ iγ^μ D_μΨ − (D_μΨ)‾ iγ^μ Ψ) − ¼ F_μν F^μν ],
mit D_μ = ∂_μ + (1/8)ω_μab[γ^a, γ^b] + i q A_μ Q_J, Ψ̄ = Ψ†γ⁰, kein Λ-Term. Massenterme fehlen vorerst; nach r44 brauchen sie ein Higgs-artiges Feld.

## QAM-Buchführung (Eingaben, nicht hergeleitet)
- `\qaminput{Pclosure}{M}{conditional}`: P_C7 = C_ch (Wahl, r42/r43);
- `\qaminput{U1e7}{M}{conditional}`: Eichrichtung L_{e₇} (Wahl, r49/r51);
- `\qaminput{adjoint}{M}{conditional}`: Dirac-Adjungierte im Frame M;
- `\qamclaim{sectors}{*}{proved}`: Sektorzerlegung r48 (Lean `Sektoren.lean`).

## Erste Befunde (k170, Erkundung)
1. **Symmetrische Kinetik ist reell.** Im L ≡ 0 punktweise (geprüft, exakt 0). Damit ist Im S = 0 und die K-Lesart fügt bei der symmetrischen Form nichts hinzu: K = R.
2. **Nicht symmetrisierte Kinetik.** Punktweise gilt Im(Ψ̄ iγ^μD_μΨ) = ½(e^μ_a ∂_μ j^a + ω_a{}^a{}_b j^b) mit j^a = Ψ̄γ^aΨ, also ½ e^μ_a D^{(ω)}_μ j^a (geprüft an 200 Zufallspunkten, Residuum ≤ 2e-14). Das U(1)-Potential fällt aus Im L heraus (≤ 1e-14).
3. **Folge für die K-Lesart mit unabhängiger Verbindung.** In Im S kommt ω nur linear über ½ e e^μ_a ω_μ{}^{a}{}_{b} j^b vor. Stationarität nach ω_μ^{ab} verlangt e^μ_{[a} j_{b]} = 0; Kontraktion mit e^c_μ gibt δ^c_a j_b − δ^c_b j_a = 0, also **j^a = 0**. Im Frame M ist j⁰ = Ψ†Ψ ≥ 0, damit **Ψ = 0**.
4. **Inneres gegen äußeres i.** Auf dem Bild von C_ch gilt J = 1, also L_{e₇} = −i. Die K-Frage für die innere Einheit fällt dort mit der für die äußere zusammen (bis auf das Vorzeichen, das an „Im S = 0“ nichts ändert).

## Lesart
- Die K-Lesart ist in diesem Rahmen entweder leer (symmetrische Kinetik) oder tödlich (nicht symmetrisiert, unabhängige Verbindung: keine Spinoren in einem Frame). Sie liefert die Schließung hier also **nicht** dynamisch; die Chiralität bleibt eine Eingabe.
- Das ist kein Widerspruch zu `HC_Null_Axis_Dynamical_Closure.md`: Dort wirkt die komplexe Stationarität in der Kompensator-Gleichung, hier im Dirac-Teil.
- **Offene Lücke, nur als Frage:** j^a = 0 ließe sich ohne Ψ = 0 erfüllen, wenn Komponenten mit negativer Dichte beitragen, etwa ein Tachyon-Frame-Anteil mit umgekehrtem Vorzeichen (Konvention F). Das wäre eine Frame-Kopplung M–T und muss eigens nach Konvention F formuliert werden; hier nicht behauptet. Sie berührt Auslöser 1 von I1 nicht, wohl aber die Frage nach getrennten Sektoren.

## Nächster Schritt
- Euler–Lagrange-Gleichungen der reellen Wirkung (Einstein–Cartan mit algebraischer Torsion aus dem axialen Strom, Maxwell mit Quelle q j^μ_J, Weyl-Gleichung je Sektor) symbolisch aufstellen; Bianchi- und Ward-Identität prüfen.
- Kleiner Test: erfüllt C_ch die Bedingung Tr(M₁₆ P_C7) ≡ 0 mod HC?
