# Ergebnis H41: Die Maske kann θ₁₂ auf den JUNO-Wert senken, legt θ₂₃ aber nicht fest

Vorab-Notiz: `Vorab_Notiz_H41_TM2_mit_Maskenkorrektur.md`, Commit 74bd018 (2026-10-24 20:05 MESZ), vor der Rechnung. Skript `k97_test_h41.py`, Ausgabe `k97_out.txt`.

## Ergebnisse

| Hypothese | Ergebnis | Befund |
|---|---|---|
| H41a Variante A (nur geladene Leptonen, Form S) | **bestätigt** | 776 von 3 965 760 Fällen: θ₁₂ im JUNO-2σ-Bereich, θ₁₃ und θ₂₃ in NuFIT 3σ; ε_e von 0.03 bis 0.64 |
| H41b Variante B (gemeinsames ε, ν in Form K) | **bestätigt** | 3 808 von 20 998 368 Fällen; ε mit Treffern um 0.04–0.06 und um 0.62–0.64, alle drei zulässigen m₁ |
| H41c Schärfe von θ₂₃ (Breite < 0.05) | **widerlegt** | bei θ₁₂ (JUNO 2σ) und θ₁₃ (3σ): sin²θ₂₃ ∈ [0.309, 0.537] (A), [0.314, 0.515] (B) |

## Einordnung

1. **Die Spannung der TM2-Lesart mit JUNO ist auflösbar.** Eine kleine Korrektur durch die Maske, mit derselben Form wie in r47, senkt sin²θ₁₂ von 0.341 auf den
   JUNO-Bereich, während θ₁₃ und θ₂₃ in den gemessenen Bereichen bleiben. Die Lesart aus r55 ist damit nicht widerlegt.
2. **Aber es ist eine Anpassung mit zwei Einstellungen, keine Vorhersage.** θ₂₃ bleibt breit (Breite 0.2 statt < 0.05).
3. **Beobachtung nach der Auswertung (kein Kriterium):** In beiden Varianten liegt sin²θ₂₃ bei passendem θ₁₂ und θ₁₃ höchstens bei 0.54 (A) bzw. 0.52 (B). Die
   Lesart bevorzugt also θ₂₃ unterhalb von etwa 47°; ein Messwert deutlich im oberen Oktanten (sin²θ₂₃ > 0.55) spräche gegen sie. Das ist eine einseitige Grenze,
   nachträglich bemerkt, und müsste als eigene Vorhersage vorab festgelegt werden.
