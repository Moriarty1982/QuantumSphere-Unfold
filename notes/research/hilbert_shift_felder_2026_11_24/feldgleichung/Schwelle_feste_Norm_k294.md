# Amplituden-Potential gegen Zusatzterme: eine scharfe Schwelle in der Wellenzahl (Erkundung k294, nicht blind, 25.11.2026)

**Ergebnis in einem Satz:** Nimmt man ein Potential λ(N − f²)² dazu, das Schwankungen der Amplitude bestraft, dann entscheidet eine einzige Größe, wo der gegenläufige Anteil
liegt: Für k²k′²W < 4λ/(c₁ + 4c₂) liegt er ganz im Anhang (feste Norm, das Verhalten von HS(2)), darüber ganz in ℂ (schwankende Norm, das Verhalten von HS(1)).
Zwischenstellungen gibt es nicht, der Anteil klappt um. Lange Wellen sehen also die feste Norm, kurze nicht.

Auftrag des Autors (25.11.2026): „dann rechne es mal“ (der in k293 genannte Wettbewerb). **Erkundung, nicht blind:** Die Schwelle ließ sich aus der Tabelle in k293 ablesen. Neu
gerechnet ist die Abhängigkeit vom Winkel zwischen ℂ und Anhang und damit, dass es keine Zwischenstellung gibt. H129 bleibt frei. Vergeben: Skripte **k294, k294b**.

Werkzeuge: Python mit sympy (exakte Phasenmittel). Wolfram Language unabhängig, mit Quaternionen als 2×2-Matrizen (k294b). Qiskit nicht eingesetzt. Kein HDL/MMA-Vergleich.

## Vorwissen geprüft
k290 (Ansatz), k291 (Ruhemasse des Knotens, Größe r₀ = √c̃₁/f), k292 (zwei Lösungen bei HS(2)), k293 (Tabelle der Energien an den beiden Enden), k274 (Duffing-Term bringt eine Skala).

## Aufbau
ψ = a·e^{ip₁} + b·(cos θ + j·sin θ)·e^{−ip₂} mit a² + b² = f², p₁ = k(t − x), p₂ = k′(t − x·cos α − y·sin α). θ = 0 ist die Lösung in ℂ, θ = π/2 die im Anhang.
Energie in erster Ordnung in λ, c₁, c₂, gemittelt über beide Phasen.

## Ergebnisse (k294, k294b)
1. **Abhängigkeit vom Winkel:** Die freie Energie hängt nicht von θ ab. Die Streuung der Norm ist 2a²b²·cos²θ. Die Zusatzterme geben ⟨H₄[K₁]⟩ = ½(1 + sin²θ)·a²b²k²k′²·W
   und ⟨H₄[K₂]⟩ = 2·sin²θ·a²b²k²k′²·W, mit W = 4 − (1 + cos α)².
2. **Die Energie ist linear in s = sin²θ:** E(s)/a²b² = 2λ + ½c₁Q + s·[(½c₁ + 2c₂)·Q − 2λ] mit Q = k²k′²W. Das Minimum liegt deshalb immer an einem Ende.
3. **Schwelle:** Q_c = 4λ/(c₁ + 4c₂). Darunter gewinnt der Anhang, darüber ℂ. Die Schwelle hängt nicht von a und b ab.
4. **In den Größen aus k291:** Die Radialmode hat m_r² = 8λf². Für gleiche Wellenzahl und entgegengesetzte Richtung (W = 4) ist (k_c·r₀)⁴ = (m_r·r₀)²/(8(1 + 4c₂/c₁)), mit der
   Knotengröße r₀ = √c̃₁/f. Die Schwelle liegt also bei Wellenlängen von der Größe des Knotens, wenn m_r·r₀ von der Ordnung eins ist.
5. **Exaktheit der Enden:** Mit Potential und ohne K-Terme ist die Lösung im Anhang eine exakte Lösung (N = f², das Potential übt keine Kraft aus). Die Lösung in ℂ ist es nicht
   (N − f² = 2ab·cos(p₁ + p₂)). Für sie ist die Rechnung nur erste Ordnung.

## Bewertung
- **A und B sind zwei Bereiche derselben Gleichung:** Bei langen Wellen ist die Norm fest (Lesart B, das Bild bei HS(2)), bei kurzen schwankt sie (Lesart A, das Bild bei HS(1)).
  Dazwischen liegt ein scharfer Umschlag. Das ist das bekannte Muster, dass eine feste Amplitude bei hoher Energie wieder frei wird, hier für den gegenläufigen Kreisanteil.
- **Zur Protomasse:** Die Skala f steckt im Potential. Die Rechnung zeigt nicht, woher f kommt, sondern nur, ab welcher Wellenlänge es wirksam ist.
- **Für parallele Wellen (W = 0)** gewinnt immer der Anhang, sobald λ > 0 ist. Eine einzelne Laufrichtung hat also stets feste Norm, erst gekreuzte kurze Wellen heben sie auf.
- Die Schwelle hängt an drei freien Koeffizienten (λ, c₁, c₂). Eine Zahl sagt der Ansatz hier nicht voraus.

## Grenzen
- Erste Ordnung auf ebenen Wellen, zwei Laufrichtungen, Vergleich bei gleichen a, b. Nahe der Schwelle und für die Lösung in ℂ kann die Rückwirkung das Bild ändern; ob der Umschlag
  scharf bleibt, ist dann nicht gesichert.
- Das Potential λ(N − f²)² ist gesetzt. Es ist ein Massenterm mit negativem μ² und widerspricht „keine Masse auf HS(1)“ nur dann nicht, wenn es erst bei HS(2) eintritt.
- K₂ in der Bauart aus D_μψ. OP1, OP3, OP4, OP5 bleiben offen, kein Guard ist berührt.

## Dateien
`k294_schwelle.py` (`k294_out.txt`), `k294b_gegenprobe.wl` (`k294b_out.txt`).
