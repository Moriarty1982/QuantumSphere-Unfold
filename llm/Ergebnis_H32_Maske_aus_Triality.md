# Ergebnis H32: Die Abweichung der triality-kovarianten Chiralität liefert eine Generationen-Maske mit fester Form

Vorab-Notiz: `Vorab_Notiz_H32_Maske_aus_Triality.md`, Commit 65c5b44 (2026-10-23 22:01 MESZ), vor der Rechnung. Vorab offengelegt: die Platz-Gewichte
und T Δ T⁻¹ = −Δ (aus der Sektortabelle von r43). Skript `k88_test_h32.py`, Ausgabe `k88_out.txt` (mit gekennzeichneter Nachkontrolle).

**Modellannahme (nicht hergeleitet):** Die Abweichung Δ = J_II − J_I zwischen triality-kovarianter und gleicher Chiralität wirkt als schwache
Störung der Kopplungen, M ↦ M + ε(WM + MW); der rechtshändige Partner wird im T-Frame gelesen.

## Ergebnisse

| Hypothese | Ergebnis | Befund |
|---|---|---|
| H32a Gewichte | **bestätigt** | Δ ist auf jedem Q-Sektor skalar: Sektor 0 (0, 0, −3), 1/3 (0, 2, 1), 2/3 (0, −2, −1), 1 (0, 0, 3) |
| H32b Frame | **bestätigt** | T Δ T⁻¹ = −Δ, Gewichte antisymmetrisch unter q ↔ 1 − q; Partner im T-Frame gleich: W_q = diag(0, −2, −1) für up und down, W_l = diag(0, 0, −3) |
| H32c Mischung, linear | **widerlegt** (Linearität) | Mischung in allen 200 Fällen von null verschieden; linear in ε aber nur in 196 von 200 bei den vorab festgelegten ε = 10⁻³, 10⁻⁴ |
| H32d Fourier-Form | **bestätigt** | In der Generationen-Basis alle Nebendiagonal-Einträge gleich groß: \|W_q\| = 1/√3, \|W_l\| = 1; Verhältnis √3 |

**Nachkontrolle zu H32c (nach der Auswertung, kein Teil des Kriteriums).** Die 4 nichtlinearen Fälle sind fast entartet: relative Lücke höchstens
3·10⁻³, Median aller Fälle 7·10⁻². Dort ist ε = 10⁻³ nicht mehr klein gegen den Massenabstand. Bei ε = 10⁻⁶ und 10⁻⁷ sind alle 200 Fälle linear. Das
Urteil „widerlegt“ bleibt, weil das Kriterium die beiden ε-Werte festlegte. Inhaltlich gilt die Linearität im Störungsbereich ε ≪ Lücke.

## Einordnung

1. **Unter der Modellannahme kommt die Generationen-Maske aus der Struktur.** Die triality-kovariante Chiralität ist als exakte Symmetrie
   verboten (r45). Ihre Abweichung von der gleichen Chiralität ist aber auf jedem Sektor eine feste Zahl pro Platz. Damit gilt:
   - Die **Form** der Maske ist festgelegt: für Quarks diag(0, −2, −1), für Leptonen diag(0, 0, −3).
   - Gewählt ist nur das Gewicht ε.
   - Up und down bekommen dieselbe Maske. Mischung entsteht trotzdem, weil ihre Kopplungen verschieden sind (r46).
2. **In der Generationen-Basis ist die Maske „demokratisch“.** Alle Paare von Generationen koppeln gleich stark, bei den Leptonen um √3 stärker
   als bei den Quarks. Bei gleichem ε hieße das: stärkere Lepton-Mischung als Quark-Mischung, zusätzlich verstärkt durch die dichten
   Neutrinomassen. Qualitativ ist das die Richtung der Beobachtung (große PMNS-, kleine CKM-Winkel). Zahlen folgen nicht.
3. **Der Referenzplatz:** Auf Platz 1 ist das Gewicht immer 0, weil dort beide Chiralitäten übereinstimmen. Welcher Platz die Referenz ist, ist
   eine Wahl, nach r38 dieselbe Art Wahl wie die, welcher Platz „Photon“ ist. Die τ-Brechung kommt in diesem Bild aus der Wahl eines
   Referenzplatzes.
4. **Grenzen:**
   - Die Modellannahme, die Abweichung als Störung zu lesen, ist nicht hergeleitet.
   - ε, die Zirkulanten-Parameter (|b|/a, θ) und damit alle Zahlenwerte bleiben offen.
   - Die Linearität gilt nur im Störungsbereich.
