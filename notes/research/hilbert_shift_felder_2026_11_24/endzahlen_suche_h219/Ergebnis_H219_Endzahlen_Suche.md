# Ergebnis H219 (k432): Die Endzahlen-Suche findet mit Bausteinen des Rahmens nicht mehr als der Zufall

Stand 28.11.2026. Vorab-Notiz: `notes/research/predictions/Vorab_Notiz_H219_Endzahlen_Suche.md` (Commit 6b5a97e, vor der Rechnung).

| Datei | Inhalt |
|---|---|
| `enum_h219.py` | Aufzählung |
| `k432_test_h219.py`, `k432_out.txt` | Hauptrechnung, Laufzeit 49 s |
| `k432b_gegenprobe.wl`, `k432b_out.txt` | Gegenprobe in Wolfram |

**Alle genannten Formeln sind angepasst (gesucht, nicht hergeleitet).**

## Frage

Der Autor fragte: „was passiert wenn man weniger vorgibt sondern nur sagt welche endzahlen man haben will?“ Vorgegeben sind nur die
Zielzahlen und die Bausteine des Rahmens:

- Blätter 1, 2, 3, π, ln 2;
- einstellig √, x², 1/x, 2^(−x);
- zweistellig + − × ÷.

Durchsucht werden alle Ausdrücke bis Größe 9, das sind 5 779 066 verschiedene Werte. Hinzu kommen Vorlagen f(n) bis Größe 8 mit
1 742 454 verschiedenen Wertvektoren.

## Urteil: widerlegt

| Ziel | rel. Fenster (2σ) | s_min | p | kürzester Treffer (angepasst) |
|---|---|---|---|---|
| sin²θ₁₂ | 8,6 % | 2 | 0,34 | 1/π = 0,3183 |
| sin²θ₂₃ | 13 % | 2 | 0,47 | (ln 2)² = 0,4805 |
| sin²θ₁₃ | 10 % | 5 | 0,94 | (2^(−ln 2))⁸ = 0,02142 |
| Δm²₂₁/Δm²₃₁ | 6,1 % | 5 | 0,95 | 2^(−π·2^(ln 2)) = 0,02958 |
| cot θ_W (on-shell) | 0,30 % | 5 | 0,86 | √(π + ⅓) = 1,86412 |
| sin²θ_W (MS-bar) | 0,069 % | 5 | 0,22 | 1/(3 ln 2)² = 0,231263 |
| m_H/m_Z | 0,35 % | 5 | 0,93 | √(2 − 2^(−π)) = 1,37357 |
| m_t/m_W | 0,69 % | 5 | 0,97 | √(π + 1/ln 2) = 2,14109 |
| m_μ/m_τ | 0,027 % | 7 | 0,67 | 3·(2^(−√2))⁴ = 0,0594619 |
| α_s | 3,1 % | 5 | 0,99 | 2^(−1/ln 2)/π = 0,11710 |
| \|V_us\| | 1,4 % | 5 | 0,98 | √(2^(−3/ln 2)) = 0,22313 |
| \|V_cb\| | 14 % | 4 | 0,86 | 2^(−3)/π = 0,03979 |
| \|V_ub\| | 21 % | 4 | 0,46 | 2^(−8) = 0,00391 |
| Ω_m (DESI) | 12 % | 3 | 0,72 | 2^(−√π) = 0,29271 |
| n_s | 1,7 % | 4 | 0,93 | √(2^(−1/8)) = 0,95760 |
| Ω_b h² | 2,7 % | 5 | 0,76 | (2^(−3))²/ln 2 = 0,02254 |
| β_sym (k358) | 0,13 % | 6 | 0,98 | 1/π + (ln 2)⁴ = 0,549145 |
| m_e/m_μ | 8,7·10⁻⁸ | – | 1,00 | kein Treffer bis Größe 9 |

Spaltenbedeutung: s_min ist die kleinste Größe eines Treffers. p ist der Anteil von 1000 Zufallszielen mit gleicher relativer Fensterbreite
(log-gleichverteilt in [x/3, 3x]), die mindestens so früh getroffen werden.

- Kein Ziel hat p < 0,05. Die Bonferroni-Schwelle liegt bei 0,0028, die Schwelle für „teilweise“ bei 4 Zielen mit p < 0,05.
- Ziele mit breitem Fenster werden mit 2 bis 5 Bausteinen getroffen, ihre Kontrollen genauso. Mit ~6 Millionen Werten ist fast jede Zahl
  mit Prozentgenauigkeit erreichbar.
- β_sym kommt später als der Zufall: s_min = 6, die Kontrollen liegen im Median bei 5.
- **Familien:** Keine Vorlage f(n) trifft eine Familie ganz, weder die Leptonen (m_e/m_μ, m_μ/m_τ) noch CKM (|V_us|, |V_cb|, |V_ub|) noch
  PMNS (sin²θ₁₂, sin²θ₂₃, sin²θ₁₃). Bei den Zufallsfamilien gelingt das bei CKM in 10,1 % und bei PMNS in 10,6 % der Fälle, bei den
  Leptonen nie, wegen m_e/m_μ.
- Am auffälligsten ist sin²θ_W ≈ 1/(3 ln 2)², mit −0,7σ bei ±4·10⁻⁵. Das liegt im Rahmen des Zufalls (p = 0,22) und ist nicht
  hergeleitet, sondern nur nachträglich ausgesucht.

## Gegenprobe

Wolfram zählt die Aufzählung bis Größe 5 unabhängig: 5, 16, 72, 461 und 2624 verschiedene Werte, gleich wie in Python. Die kürzesten
Treffer bis Größe 5 für sechs Ziele stimmen überein. Für β_sym und m_μ/m_τ findet Wolfram keinen Treffer bis Größe 5, Python braucht 6
bzw. 7. Die Werte der gemeldeten Formeln sind nachgerechnet.

## Hergeleitet, gesetzt, nachträglich

- **Gesetzt:** Bausteine, Größengrenzen, Zielkatalog (aus k235), Fenster, Kontrollen und die Zuordnung in den Familien, alle vorab.
- **Hergeleitet:** nichts. Alle Formeln sind angepasst.
- **Nachträglich:** keine Auswahl. Die Tabelle enthält alle Ziele.
- **Grenzen:** Das Urteil gilt für diese Bausteine und Größen. Mehr Bausteine, etwa γ_M, e oder √5, machen die Suche nicht schärfer. Sie
  erhöhen nur die Zufallsquote, die die Kontrollen mitzählen.

## Folgerung

Wer nur Endzahlen vorgibt, findet zu jeder Zahl eine Formel, aber nicht schneller als zu einer Zufallszahl. Ohne Vorgabe der Struktur
entsteht also kein Befund. Das bestätigt die Lage aus H215 bis H217 und aus k235. Eine Zahl wird im Rahmen erst dann aussagekräftig, wenn
ihre Formel vor dem Blick auf die Daten aus einer Herleitung feststeht.
