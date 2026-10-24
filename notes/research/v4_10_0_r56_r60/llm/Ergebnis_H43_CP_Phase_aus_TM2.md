# Ergebnis H43: Die korrigierte TM2-Lesart legt die CP-Phase nicht fest

Vorab-Notiz: `Vorab_Notiz_H43_CP_Phase_aus_TM2.md`, Commit 59d8d04 (2026-10-24 21:09 MESZ), vor der Rechnung. Skript `k98_test_h43.py` (Modelle und Gitter wie k97),
Ausgabe `k98_out.txt`; die Treffer von H41 werden dort reproduziert (776 bzw. 3 808).

## Ergebnisse

| Hypothese | Ergebnis | Befund |
|---|---|---|
| H43a Variante A | **widerlegt** | \|sin δ\| ∈ [0.174, 0.999], cos δ ∈ [−0.980, 0.985]; δ-Quantile 5/50/95 %: 14°, 180°, 346° |
| H43b Variante B | **widerlegt** | \|sin δ\| ∈ [0.172, 0.999], cos δ ∈ [−0.981, 0.985]; δ-Quantile 13°, 180°, 347° |

Keine neue Vorhersage H44.

## Einordnung

1. **δ ist durch die Lesart nicht festgelegt.** Die Treffer überdecken fast den ganzen Bereich; ausgeschlossen ist nur |sin δ| < 0.17, also δ sehr nahe bei 0° oder 180°
   (eine kleine, aber nicht scharfe Einschränkung, die zudem vom Gitter abhängen kann).
2. Die korrigierte TM2-Lesart bleibt damit eine Anpassung mit zwei Einstellungen: θ₁₂ trifft, θ₂₃ ist nur nach oben begrenzt (H42, ausstehend), δ ist frei.
3. Für eine schärfere Lesart müsste die Korrektur selbst aus der Struktur festgelegt werden (etwa ε aus einem Strukturwert statt frei), sonst bleibt die Zahl der
   Einstellungen zu groß.
