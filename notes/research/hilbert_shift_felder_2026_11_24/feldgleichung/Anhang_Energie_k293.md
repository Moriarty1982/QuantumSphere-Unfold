# Muss der gegenläufige Anteil bei HS(2) in den Anhang? Die Zusatzterme sprechen dagegen (Erkundung k293, nicht blind, 25.11.2026)

**Ergebnis in einem Satz:** Nein, jedenfalls nicht aus Energiegründen. Für zwei Wellen mit verschiedenen Laufrichtungen haben die Lösung mit dem gegenläufigen Anteil in ℂ (wie
bei HS(1)) und die mit dem Anteil im Anhang ℂ·j dieselbe freie Energie, aber im Anhang ist die Energie des Flächenterms K₁ doppelt so groß, und der Kommutatorterm K₂ kommt nur
dort dazu. Mit positiven Koeffizienten c₁, c₂ kostet das Wandern in den Anhang also Energie. Welche Lösung bevorzugt ist, hängt am Vorzeichen von c₁ und c₂, und das positive c₁,
das die Ruhemasse bei HS(2) braucht (k291), spricht gegen das Wandern.

Auftrag des Autors (25.11.2026): „merge und dann bitte rechnen“, gemeint war der in k292 vorgeschlagene Test H129. **Kein blinder Test, sondern Erkundung:** Beim Festlegen des
Entscheidungskriteriums ließ sich das Ergebnis ablesen. Die Ableitungen beider Lösungen haben die Form X_μ = k_μA + k′_μB, also ist jeder Zusatzterm gleich (k∧k′)² mal einer
Größe aus A und B, und im Anhang stehen A und B immer senkrecht. **H129 bleibt frei.** Vergeben: Skripte **k293, k293b**.

Werkzeuge: Python mit sympy (exakte Mittelwerte über beide Phasen). Wolfram Language unabhängig, mit Quaternionen als 2×2-Matrizen (k293b). Qiskit nicht eingesetzt. Kein
HDL/MMA-Vergleich.

## Vorwissen geprüft
k290 (Zusatzterme K₁, K₂; für eine rein zeitabhängige Lösung verschwinden sie), k291 (K₁ auf S³ ist der Skyrme-Term, Ruhemasse M ≈ 103,2·f·√c₁ verlangt c₁ > 0), k292 (zwei
Lösungen bei HS(2), offene Frage „muss“), k253. H128 (Thread Hilbert-Shift, #297) betrifft den Familienteil und berührt diese Frage nicht.

## Aufbau
- S_C: ψ = a·e^{ip₁} + b·e^{−ip₂}, S_J: ψ = a·e^{ip₁} + (b·j)·e^{−ip₂}, mit p₁ = k(t − x) und p₂ = k′(t − x·cos α − y·sin α). Beide lösen die freie Gleichung □ψ = 0.
- Energie der Zusatzterme in erster Ordnung: H₄ = Σ_i K(∂_tψ, ∂_iψ) + Σ_{i<j} K(∂_iψ, ∂_jψ), gemittelt über beide Phasen. Der Beitrag zur Energie ist c₁·⟨H₄[K₁]⟩ + c₂·⟨H₄[K₂]⟩.

## Ergebnisse (k293, k293b)
| | S_C (Anteil in ℂ) | S_J (Anteil im Anhang) |
|---|---|---|
| ⟨N⟩ | a² + b² | a² + b² |
| Streuung von N | 2a²b² | 0 |
| freie Energie | a²k² + b²k′² | a²k² + b²k′² |
| ⟨H₄[K₁]⟩ | ½·a²b²k²k′²·W | a²b²k²k′²·W |
| ⟨H₄[K₂]⟩ | 0 | 2·a²b²k²k′²·W |

mit dem Winkelfaktor W = 4 − (1 + cos α)² = (1 − cos α)(3 + cos α). Er ist null für parallele Wellen (α = 0) und 4 für entgegengesetzte (α = π).

1. Die freie Theorie unterscheidet die beiden Lösungen nicht.
2. Der Unterschied S_J − S_C ist (½c₁ + 2c₂)·a²b²k²k′²·W. Er ist proportional zu a²b², verschwindet also, wenn einer der beiden Kreisanteile fehlt.
3. Für parallele Wellen ist er null. Eine einzelne Laufrichtung entscheidet nichts.

## Bewertung
- **Die Energie treibt den gegenläufigen Anteil nicht in den Anhang**, solange c₁ und c₂ positiv sind. Sie hält ihn in ℂ. Negative Koeffizienten würden ihn hinaustreiben, machen aber die
  Energie nach unten unbeschränkt und nehmen dem Igel aus k291 die Stabilität (Derrick verlangt E₄ > 0).
- **Damit stehen zwei Befunde in Spannung:** k292 zeigt, dass die Norm im Anhang fest wird und die Skala f² = a² + b² geerbt werden kann. k293 zeigt, dass dieselben Terme, die bei HS(2)
  die Ruhemasse tragen, diese Lösung für gekreuzte Wellen teurer machen. Der Übergang von der schwankenden zur festen Norm folgt also nicht aus dem Ansatz k290 allein.
- **Was ihn liefern könnte**, ohne dass es gerechnet ist: ein Potential V(N), das Schwankungen der Norm bestraft (S_C hat die Streuung 2a²b², S_J keine). Ein solcher Term λ(N − f²)² bevorzugt
  S_J um λ·2a²b² und ist der einzige Baustein des Ansatzes, der das tut. Dann entscheidet das Verhältnis von λ zu (½c₁ + 2c₂)k²k′²W: Bei kleinen Wellenzahlen gewinnt die feste Norm, bei
  großen die Lösung in ℂ. Das ist eine Lesart und wäre der Gegenstand eines echten Tests.
- Wieder hängt die Entscheidung an freien Koeffizienten. Das passt zur Vermutung des Autors, dass die Vorzeichen erst aus der fertigen Feldgleichung folgen.

## Grenzen
- Erste Ordnung in c₁, c₂ auf Lösungen der freien Gleichung, nur ebene Wellen, nur zwei Laufrichtungen. Rückwirkung auf die Lösungen ist nicht gerechnet.
- Verglichen wird bei gleichen a, b, k, k′. Die Ladungen der beiden Lösungen sind verschieden (k292), ein Vergleich bei gleichen Ladungen ist nicht gemacht.
- K₂ in der Bauart aus D_μψ; die Stromvariante ist nicht gerechnet.
- OP1, OP3, OP4, OP5 bleiben offen, kein Guard ist berührt.

## Möglicher nächster Schritt
Den Wettbewerb zwischen λ(N − f²)² und den Zusatztermen ausrechnen: Schwelle in k, unterhalb derer die feste Norm gewinnt. Ob das blind geht, hängt daran, ob sich die Schwelle vorab
ablesen lässt; nach der Tabelle oben ist sie in erster Ordnung λ·2a²b² gegen (½c₁ + 2c₂)a²b²k²k′²W, also vermutlich wieder nicht blind.

## Dateien
`k293_anhang_energie.py` (`k293_out.txt`), `k293b_gegenprobe.wl` (`k293b_out.txt`).
