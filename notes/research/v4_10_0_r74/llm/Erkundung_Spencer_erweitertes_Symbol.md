# Erkundung: Spencer-Kohomologie des erweiterten Symbols (Vorprüfung zur formalen Integrabilität)

Stand: 3. November 2026. Erkundung ohne Vorab-Notiz: Sie berechnet eine Obergrenze, prüft keine Vorhersage. Skript
`k149_spencer_erweitert.py` (konsistentes Symbol wie `k148`: J = A(0), θ neu am reparierten Keim, Eichung, σ_k),
Protokoll `k149_log_kurz.txt`. Betrifft nur das OP5-Vergleichsmodell.

## Ergebnis

H^{k,2} = dim ker(δ: g_k ⊗ Λ² → S^{k−1} ⊗ Λ³) − rang(δ: g_{k+1} ⊗ Λ¹ → S^k ⊗ Λ²). Lücken der δ-Ränge ≥ 3e4.

| Symbol | H^{5,2} | H^{6,2} | H^{7,2} |
|---|---|---|---|
| geeicht g' (ohne σ; Probe, r72.5 gab 4) | 4 | 0 | 0 |
| erweitert g'' (mit σ) | 8 | 4 | 3 |

## Lesart

- **Die Probe stimmt:** Für g' kommt wieder H^{5,2} = 4 heraus, und für k = 6, 7 ist nichts übrig. Die vier Bedingungen
  sind damit die einzigen möglichen Hindernisse des geeichten Systems bis k = 7.
- **H^{5,2}(g'') = 8:** Der Kern ist derselbe wie bei g' (1322); das Bild ist um 4 kleiner, weil g''_6 um 4 kleiner ist. Die
  vier zusätzlichen Klassen kommen von den vier neuen Gleichungen selbst. Ob sie weitere Bedingungen an 6-Jets erlauben
  oder nur die schon aufgenommenen σ_k widerspiegeln, sagt die Zählung allein nicht. Bekannt ist: Die vier σ_k sind
  verwirklicht; weitere Bedingungen an 6-Jets wurden in F₈ nicht gesehen (P₅₆ = 848 mit den Gleichungen bis Grad 7).
- **H^{6,2}(g'') = 4 und H^{7,2}(g'') = 3:** Die vier neuen Gleichungen sechster Ordnung erzeugen ihrerseits Raum für
  höchstens 4 versteckte Bedingungen an 7-Jets und höchstens 3 an 8-Jets. Das passt dazu, dass g'' bei p = 6, 7 nicht
  involutiv ist. Ob diese Hindernisse verwirklicht sind, entscheiden die Terme niederer Ordnung, nicht das Symbol.
- Ab k = 8 erwartet man H^{k,2} = 0, weil g'' dort involutiv ist (H56, H58; formal unbestätigt).

## Folgerung

Die Vorprüfung schließt weitere versteckte Bedingungen nicht aus. Es bleiben bis zu 4 an 7-Jets und bis zu 3 an 8-Jets
möglich. Entscheiden kann das nur die Fortsetzungsrechnung mit den Gleichungen bis Grad 9 bzw. 10, und zwar über einem
Jet, der die vier Bedingungen schon erfüllt. Diese Systeme haben 12 000 bis 16 000 Spalten und überschreiten mit dem
bisherigen Verfahren den Speicher der Cloud-Umgebung (8 GB). Nötig wäre eine stufenweise Elimination.
