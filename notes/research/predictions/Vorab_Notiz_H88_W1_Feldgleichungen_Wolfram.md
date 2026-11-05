# Vorab-Notiz H88: Unabhängige Herleitung der W1-Feldgleichungen mit Wolfram

**Stand:** 5. November 2026, vor der Rechnung festgelegt. **Nicht blind:** Die Sollwerte stehen in der W1-Notiz; geprüft wird, ob ein unabhängiges System sie aus der Wirkung erzeugt. Autor 23:34: „ja, und wenn sie nicht übereinstimmen, wäre die Frage wieso.“

## Vorwissen geprüft
`notes/research/v4_10_0_w1/Wirkung_W1_Dixon_U1.md`: Wirkung S = ∫e[(1/2κ)R(e, ω) + ½(Ψ†iσ̄^μD_μΨ + c.c.) − ¼F²], D_μ = ∂_μ + (1/8)ω_μab(σ^aσ̄^b − σ^bσ̄^a) + iqA_μJ, σ̄^a = (1, −σ_i), η = diag(1, −1, −1, −1). Befund 6 (k173): Kopplung an die Verbindung total antisymmetrisch ∝ ε_abcd j^d, R(K) = 6k·k, nach Elimination L_eff = −(3/16)κ j·j mit dem Gesamtstrom; Kontrolle Dirac −(3/16)κ(j₅)² (Hehl–Datta). Feldgleichungen 1–3 dort: Weyl mit −(3κ/8)j_aσ̄^aψ_s, Maxwell ∇̃_μF^{μν} = q j^ν_J, Einstein ohne Λ; laut Notiz „Rest aus der Standardtheorie übernommen“, die symbolische Herleitung und die Prüfung von Bianchi- und Ward-Identität standen aus.

## Was geprüft wird (flacher Hintergrund, konstante Kontorsion, wo nötig)
- **H88a (Erzeuger):** Mit Σ^{ab} = ¼(σ^aσ̄^b − σ^bσ̄^a) transformiert j^c = ψ†σ̄^cψ als Vektor, d. h. Σ^{ab†}σ̄^c + σ̄^cΣ^{ab} ist proportional zum Vektor-Erzeuger (η^{bc}σ̄^a − η^{ac}σ̄^b). Geprüft wird auch die Alternative ¼(σ̄^aσ^b − σ̄^bσ^a).
- **H88b (Torsion):** Aus R(ω̃ + K) mit den Definitionen R^{ab}_{μν} = ∂_μω_ν^{ab} − ∂_νω_μ^{ab} + ω_μ^a{}_cω_ν^{cb} − ω_ν^a{}_cω_μ^{cb}, R = e^μ_ae^ν_bR^{ab}_{μν}, und der Spinorkopplung in symmetrischer Form folgt nach Elimination aller 24 Komponenten von K: L_eff = −(3/16)κ·j·j für einen Weyl-Spinor bzw. die Summe der Ströme mehrerer Weyl-Spinoren; für Dirac −(3/16)κ·(j₅)².
- **H88c (Weyl-Gleichung):** Die Euler-Lagrange-Gleichung von ½(ψ†iσ̄^μD_μψ + c.c.) + L_eff (flach, A_μ konstant) ist iσ̄^μ∂_μψ − qJA_μσ̄^μψ − (3κ/8)j_aσ̄^aψ = 0.
- **H88d (Ward):** Auf Lösungen der Weyl-Gleichung gilt ∂_μ j^μ = 0 (symbolisch für ebene Wellen und mit der Vier-Fermionen-Kopplung als Identität geprüft).
- Die Einstein-Gleichung wird hier **nicht** geprüft (zu groß für die Laufzeitgrenze); das wird im Ergebnis so vermerkt.

## Umgang mit Abweichungen (vorab festgelegt)
Weicht ein Teil ab, wird vor jeder Wertung die Ursache gesucht, in dieser Reihenfolge: (1) Konventionen (Vorzeichen der Metrik, σ̄, Erzeuger, Definition von R, κ), (2) Rechenfehler in k173 oder in der Wolfram-Rechnung (dritte Rechnung als Schiedsrichter), (3) ein Fehler in der W1-Notiz. Erst wenn die Ursache benannt ist, wird bewertet, ob r81–r85 betroffen sind. Ein Konventionsunterschied, der sich durch Umbenennung auflöst, gilt als Übereinstimmung, wird aber vermerkt.

Code: `llm/k203_w1_feldgleichungen.wl` (nach dem Commit dieser Notiz).
