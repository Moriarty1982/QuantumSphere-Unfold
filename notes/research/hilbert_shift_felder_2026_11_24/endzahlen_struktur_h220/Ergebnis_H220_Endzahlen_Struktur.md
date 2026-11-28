# Ergebnis H220 (k433): Auch mit strukturellen Bausteinen und passender Dichte kein Treffer

Stand 28.11.2026. Vorab-Notiz: `notes/research/predictions/Vorab_Notiz_H220_Endzahlen_Struktur.md` (Commit 00d09c8, vor der Rechnung).

| Datei | Inhalt |
|---|---|
| `bausteine_h220.py` | Bausteine |
| `k433_test_h220.py`, `k433_out.txt` | Hauptrechnung |
| `k433c_nachtrag_tiefe.py`, `k433c_out.txt` | Nachtrag, nachträglich |
| `k433b_gegenprobe.wl`, `k433b_out.txt` | Gegenprobe in Wolfram |

**Alle genannten Formeln sind angepasst.**

## Aufbau

- **Blätter:** 1, 2, 4, 8, 16, 3, 7, ½, ⅔, √(j(j+1)) für j = ½ bis 2, γ_L.
- **Operationen:** + − × ÷, √, x², 1/x.
- **Größengrenze nach der Dichte-Regel:** S_max ist die größte Größe, bei der für das breiteste Fenster höchstens die Hälfte der Kontrollen
  getroffen wird. Das breiteste Fenster hat sin²θ_W mit relativ ±3,5·10⁻⁴. Es ist knapp breiter als das von m_W/m_Z (±3,3·10⁻⁴). Die
  Vorab-Notiz hatte m_W/m_Z genannt, die Regel rechnet aber nach Breite. Getroffene Kontrollen je Größe:

  | Größe | 1 | 2 | 3 | 4 | 5 | 6 |
  |---|---|---|---|---|---|---|
  | getroffen | 0 | 0,001 | 0,021 | 0,101 | 0,549 | 0,989 |

  Daraus folgt **S_max = 4**, also 2090 Werte.

## Urteil: widerlegt

Bis Größe 4 trifft kein Ziel, kein p liegt unter 1. Die nächsten Werte:

| Ziel | nächster Wert bis Größe 4 | Abstand |
|---|---|---|
| m_e/m_μ | (½/7)² = 0,005102 | 2,5·10⁶ σ |
| m_μ/m_τ | 1/(16 + √3/2) = 0,059291 | 43σ |
| sin²θ_W | (√3/2)/(15/4) = 0,230940 | 8,7σ |
| α_em⁻¹ | 16²/γ_L = 137,2875 | 1,2·10⁷ σ |
| m_W/m_Z (nicht blind) | 1/(2 − √3/2) = 0,881854 | 3,4σ |

Die Kontrollen werden bei dieser Tiefe zu 0 bis 20 % getroffen. Ein Treffer wäre also aussagekräftig gewesen, es gab aber keinen.

## Nachtrag (nachträglich, nicht gewertet, k433c): wie tief man gehen müsste

| Ziel | erster Treffer | Abstand | Kontrollen bis zu dieser Größe getroffen |
|---|---|---|---|
| m_μ/m_τ | Größe 5: 1/(16 + √(⅔)) = 0,0594654 | +0,35σ | 13,2 % |
| sin²θ_W | Größe 6: 1/7 + √2/16 = 0,2312455 | −1,1σ | 98,9 % |
| m_W/m_Z | Größe 6: 2/(√15/2 + ⅓) = 0,8811252 | −1,6σ | 100 % |
| m_e/m_μ, α_em⁻¹ | kein Treffer bis Größe 8 (6,9 Mio. neue Werte bei Größe 8) | – | – |

1/(16 + √(⅔)) für m_μ/m_τ ist der auffälligste Fund. Mit 13 % Zufallsquote ist er aber nicht signifikant (p ≈ 0,13), er liegt jenseits der
vorab festgelegten Tiefe und ist nicht hergeleitet. Die bekannte Lesart γ_L/√(1 + γ_L²) = 0,88127 für m_W/m_Z (H15, −0,6σ) hat Größe 7.
Sie liegt damit in einer Tiefe, in der jede Zahl getroffen wird.

## Gegenprobe

Wolfram zählt bis Größe 4 unabhängig 14, 29, 318 und 1729 neue Werte, gleich wie in Python. Auch Wolfram findet bis S_max keinen Treffer.
Die Werte aller genannten Formeln sind mit 25 Stellen nachgerechnet.

## Hergeleitet, gesetzt, nachträglich

- **Gesetzt:** Bausteine, Ziele und die Dichte-Regel, alle vorab.
- **Hergeleitet:** nichts.
- **Nachträglich:** die Tiefen-Tabelle.
- **Grenzen:** Die Dichte-Regel macht die Suche für die genauesten Ziele sehr flach. Das ist gewollt, denn nur dort ist ein Treffer mehr als
  Zufall. Eine tiefere Suche würde zwar treffen, aber genauso oft wie bei Zufallszahlen (siehe H219 und die Kontrollquoten oben).

## Folgerung

Auch die strukturellen Bausteine des Rahmens (Dimensionen, Casimir-Flächen, ⅔, γ_L) erzeugen keine der genau gemessenen Zahlen in einer
Tiefe, in der ein Treffer etwas bedeuten würde. Zusammen mit H219 heißt das: Eine Endzahlen-Suche liefert in diesem Rahmen nichts, was
über den Zufall hinausgeht. Zahlen müssen aus Herleitungen kommen.
