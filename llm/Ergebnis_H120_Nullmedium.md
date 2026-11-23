# Ergebnis H120: Ein Medium aus lichtartigen Strahlen heilt die Kegelgrenze nur nahe seinem Gleichgewichtssystem, nicht im Photon-Frame; im Vakuum begrenzt die Lorentz-Grenze den gerichteten Kontrast auf g_m² ≤ 8,6·10⁻²⁷

**23. November 2026. Vorab-Notiz `llm/Vorab_Notiz_H120_Nullmedium.md` (Commit d3810e58). Skript `llm/k240_h120_null_medium.py`, Ausgabe
`llm/k240_out.txt`. Status: H120a bestätigt (nicht blind); H120b teilweise bestätigt (Grenze hält, Zusatz „nur in P“ widerlegt); H120c bestätigt.**

## Kontrollen
- Vergleichsmodell (r = ½ überall): größtes Geschwindigkeitsquadrat 0,674964, wie in r47.

## Ergebnis
| Teil | Messwert | Kriterium | Entscheidung |
|---|---|---|---|
| H120a, ein Strahl | r = 1 in Richtung l für κw = 0,1 … 100; dort größtes Geschwindigkeitsquadrat 1,199462 | > 1 für alle κ | bestätigt |
| H120b, zwei Gegenströme | Kegelgrenze in allen Richtungen (konservativ, 41 θ × 21 α) für 35 von 49 Parametersätzen, z. B. κa = κb = 0,3: 0,8034 (geometrisch für n ∥ z und n = x ebenso 0,8034) | ein Satz ≤ 1 | erfüllt |
| H120b, Zusatz „nur in P“ | Beobachter mit Rapidität η entlang der Stromachse: größte Verlangsamung max(1 − r) = 0,75 (η = 0), 0,52 (0,6), 0,69 (1), 0,94 (2), → 1 (8); Grenze 0,80 / 0,93 / 1,05 / 1,18 / → 1,1995 | max(1 − r) → 0 | widerlegt |
| H120c, Mindestverlangsamung | obere Bedingung mit r = 1 − ε exakt: ε² − g_m²(⅔ − ⅔α + 7⁄6 α²) ≥ 0, schärfste Stelle α = 1; ε_min = √(7g_m²/6) (Z = 1), numerisch gleich bei g = 3/100, 10⁻⁴, 10⁻⁸ | ε ≥ k√g, k = O(1) | bestätigt, k = √(7/6) |

## Warum es scheitert bzw. trägt
- Ein lichtartiger Strahl lässt v = 1 als Wurzel in seiner Richtung, und der massive Kanal koppelt in jeder Richtung (j_m² ≥ ½g_m²).
- Zwei Gegenströme verengen den Kegel in allen Richtungen, solange keiner dominiert. Für einen Beobachter, der sich entlang der Stromachse bewegt,
  wachsen die Gewichte wie a e^{−2η}, b e^{2η}; zum Photon-Frame hin dominiert ein Strom, und das Medium wird zu einem einzelnen Strahl (H120a).
  Es ist also nur in der Nähe seines Gleichgewichtssystems ein Medium, nicht im Photon-Frame.
- Die obere Bedingung bei universeller Verlangsamung ist exakt quadratisch in ε ohne gemischte Glieder; daraus folgt die Wurzelskalierung.

## Lesart
- Die Idee „wirkt im Photon-Frame, verbiegt sich in den anderen“ erhält in Lesart (a) eine umgekehrte Form: Aus Strukturen des Photon-Frames,
  zwei lichtartigen Gegenströmen, entsteht für Beobachter nahe ihrem Gleichgewicht ein echtes Medium mit Ruhesystem (dort, wo sich die Gewichte
  ausgleichen, wie in r41). Im Photon-Frame selbst ist es kein Medium mehr, sondern ein Strahl. T9 („Λ = 0 in P“) wird davon nicht gestützt.
- Nachträglich, nicht vorab festgelegt: Bei η = 0,6, nahe der Rapidität von M (artanh β_sym = 0,618), hält die Grenze noch (0,93). Die Rapidität
  in r46–H120 läuft aber entlang der Stromachse, die von OP1 quer zur E ∥ B-Achse; das ist keine Bestätigung.
- **Die Schranke H120c gilt für jedes Medium mit universeller Verlangsamung im Vakuum:** Mit einer Laborgrenze der Lorentz-Verletzung ε ≤ 10⁻¹³
  (H78) folgt g_m² ≤ (6/7)·10⁻²⁶ ≈ 8,6·10⁻²⁷. Das Vergleichsmodell (g_m² = 3/100) ist im Vakuum damit um rund 25 Größenordnungen
  ausgeschlossen; ein beobachtbarer gerichteter Kontrast verlangt ein Material, dessen Ruhesystem die Präparation ist. Die Grenze 10⁻¹³ betrifft
  Fermionen; für den Higgssektor ist sie hier übernommen, nicht eigens belegt.
- OP5 und H96 bleiben offen. Nächste Frage nur mit neuer Vorab-Notiz: Lesart (b), die Frame-Abbildung J_B.
