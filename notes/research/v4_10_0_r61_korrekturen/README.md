# Runde v4.10.0-r61: Korrekturen zu r56.4 und r07.4 (25.11.2026)

Die Runde ist wörtlich an [`sources/research/parts/v4100-post-release-layers.tex`](../../../sources/research/parts/v4100-post-release-layers.tex) angehängt. Sie ist kein Release, und die Guard-Vektoren bleiben unverändert. Der Ordnername trägt den Zusatz `_korrekturen`, weil `v4_10_0_r61/` bereits die ältere Schicht v4.9.0-r61 enthält.

Anlass ist die Gegenprüfung des englischen Artikels „One Object, Three Frames“ (`paper/physics-standalone/`). Marc hat die Korrektur am 25.11.2026 beauftragt. Die Runde ist eine Erkundung, nicht blind, und vergibt keine H-Nummer.

| Theoremlet | Inhalt | Wirkung |
|---|---|---|
| r61.1 | In r56.4 steht ρ_Λ = 3Λ/κ, richtig ist ρ_Λ = Λ/κ. Damit wird x*³ = κρ_M0(1−β²)/(β²Λ). | Nur die Formel für x*³ ändert sich, um den Faktor 3. Λ = 3(1−β²)H*² = 2,0944603 H*², r56.5, r57.1, r59.5 und H96 bleiben unverändert. |
| r61.2 | In r07.4(c) steht β_sym = (γ_L−1)/(γ_L+1), richtig ist β_sym = √((γ_L−1)/(γ_L+1)) = 0,5494056. | Keine Zahl im Bestand wurde mit der falschen Formel gerechnet, und die Aussage von r07.4 (der Vorfaktor kürzt sich) bleibt bestehen. |

| Pfad | Inhalt |
|---|---|
| `rounds/v4100_r61_round.tex` | die Runde |
| `llm/k320_korrektur_r56_r07.wl`, `llm/k320_out.txt` | Wolfram-Prüfung (exakt) mit den tatsächlichen Print-Ausgaben |
