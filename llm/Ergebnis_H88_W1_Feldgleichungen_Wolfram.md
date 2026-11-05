# Ergebnis H88: Wolfram erzeugt die W1-Feldgleichungen unabhängig; alles stimmt überein (Einstein-Gleichung nicht geprüft)

Vorab-Notiz `Vorab_Notiz_H88_W1_Feldgleichungen_Wolfram.md`, Commit `06a8380` (nicht blind). Code `k203_w1_feldgleichungen.wl` (Wolfram-Connector).

## Ergebnisse
- **H88a bestätigt (Erzeuger):** Mit Σ^{ab} = ¼(σ^aσ̄^b − σ^bσ̄^a) ist Σ^{ab†}σ̄^c + σ̄^cΣ^{ab} in allen 64 Komponenten das (−1)-fache von η^{bc}σ̄^a − η^{ac}σ̄^b. Mit D = ∂ + ½ω_abΣ^{ab} folgt daraus D_μ j^c = ∂_μ j^c + ω_μ{}^c{}_b j^b, die übliche Konvention. Die Alternative ¼(σ̄^aσ^b − σ̄^bσ^a) gibt gemischte Faktoren (+1 und −1) und ist nicht kovariant.
- **H88b bestätigt (Torsion):** Aus der Definition R^{ab}_{μν} = ∂ω − ∂ω + ωω − ωω, R = e e R, und der symmetrischen Spinorkopplung folgt nach Elimination aller 24 Kontorsionskomponenten für zwei Weyl-Spinoren exakt L_eff = −(3/16)κ·j·j mit dem Gesamtstrom j = j₁ + j₂ (Rest symbolisch 0). Für einen einzelnen Weyl-Spinor verschwindet L_eff, weil sein Strom lichtartig ist (wie in der W1-Notiz).
- **H88c bestätigt (Weyl-Gleichung):** Die Variationsableitung nach ψ† ergibt exakt iσ̄^μ∂_μψ − qJA_μσ̄^μψ − (3κ/8)j_aσ̄^aψ = 0 (Rest {0, 0}), mit j dem Gesamtstrom.
- **H88d bestätigt (Ward):** Die Matrix M = qJA_μσ̄^μ + (3κ/8)j_aσ̄^a ist hermitesch (Rest Nullmatrix). Aus iσ̄^μ∂_μψ = Mψ folgt damit ∂_μ j^μ = 0 auf Lösungen.
- **Nicht geprüft:** die Einstein-Gleichung (Variation nach dem Koframe) und die Bianchi-Identität. Für die Laufzeitgrenze des Connectors (etwa 100 s) ist die volle Rechnung zu groß; sie bleibt offen.

## Folge
Es gab keine Abweichung, also keine Ursache zu suchen. Die Torsionsrechnung k173 ist von einem zweiten System aus den Definitionen bestätigt; die bisher „aus der Standardtheorie übernommenen“ Weyl- und Ward-Aussagen der W1-Notiz sind jetzt hergeleitet. Die Grundlage von r81–r85, soweit sie auf diesen Gleichungen ruht, ist damit fester. Offen bleibt die Einstein-Gleichung von W1.
