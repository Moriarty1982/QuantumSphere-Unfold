# Ergebnis H98: Sonderstellung des Zählregel-Paars DL/M + ABCK

**7. November 2026.** Vorab-Notiz `llm/Vorab_Notiz_H98_Zaehlregel_Sonderstellung.md` (Commit 0cad2d8). Skript `llm/k218_regelraum_paare.py`,
Ausgabe `llm/k218_out.txt`. **Nicht blind gegenüber den Daten** (siehe Vorab-Notiz).

## Ergebnis: bestätigt
Im festgelegten Regelraum S (Spinbereiche A, H, I, S½, S1 × Gewichte 2, 2j + 1; neun verschiedene Regeln) gibt es 36 gültige Paare.

| Fenster | Paare im Fenster |
|---|---|
| Leptonfenster β ∈ [0,545; 0,570] | 2 (A,2 / S½ und A,2 / S1,2j+1) |
| m_W, PDG 2025, 2σ | **1** (A,2 / S½) |
| Ω_M, DESI DR2, 2σ | 2 (A,2 / S½ und H,2j+1 / S1,2j+1) |
| alle drei | **1: A,2 für M und S½ für T, also DL/M mit ABCK** |

Werte des Paars: γ_L = 1,864700, β = 0,54941, m_W = 80,3615 GeV (0,6σ), Ω_M = 0,3018 (0,5σ). Nach dem Kriterium **bestätigt**.

## Was das bedeutet und was nicht
- **Die drei Treffer zusammen sind selten.** Jedes einzelne Fenster lassen auch andere Paare zu; erst m_W wählt eindeutig. Die γ_L-Werte der 36 Paare
  liegen zwischen 1,006 und 3,51; das m_W-Fenster ist etwa ± 0,003 in γ_L breit. Bei gleichmäßiger Streuung erwartet man darin rund 0,08 Paare.
- **Das Gewicht des Befunds hängt an der m_W-Relation**, und die wurde nachträglich gefunden (H15-Offenlegung, Look-elsewhere ≈ 0,17 über drei
  Dokumentkonstanten). Zusammen eine Größenordnung von wenigen Prozent für einen zufälligen Dreifachtreffer; keine Signifikanz im strengen Sinn.
- **Die Zuordnung ist damit nicht hergeleitet.** H98 zeigt nur: Unter natürlichen Zählregeln ist das gewählte Paar das einzige, das alle drei
  bekannten Werte trifft. Warum M voll und T minimal zählt, sagt das nicht. Dazu die Erkundung `llm/Erkundung_Zaehlregel_Prinzip.md`.
- Das SU(2)-Paar der Literatur (A,2j+1 / S½) liegt bei γ_L = 2,1515 und verfehlt alle drei Fenster.
