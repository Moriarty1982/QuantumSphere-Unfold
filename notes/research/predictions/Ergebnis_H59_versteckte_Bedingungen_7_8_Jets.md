# Ergebnis H59: keine weiteren versteckten Bedingungen auf 7- und 8-Jets, bestätigt

Grundlage sind die Vorab-Notiz H59 (Commit e99331e) und ihr Nachtrag (4a447b5), beide vor der Rechnung. Gerechnet hat `ci/hp/k159_hp_faser.py` auf GitHub-Runnern (Lauf 41712811097, 3. Nov. 2026), mit arb auf 70 Stellen.

## Werte
| q | dim N_q | Rang C | F_q | Gram-Lücke (Verhältnis) | größtes Newton-Residuum | RAM | Zeit |
|---|---|---|---|---|---|---|---|
| 6 (Kontrolle) | 501 | 24 | **477** | 5.0e-13 \| 3.1e-71 (1.6e58) | 9e-52 | 4.0 GB | 20 min |
| 7 | 637 | 43 | **594** | 8.0e-13 \| 2.8e-71 (2.8e58) | 1.1e-51 | 8.0 GB | 37 min |
| 8 | 789 | 66 | **723** | 6.8e-15 \| 1.7e-71 (3.9e56) | 7.2e-52 | 15.2 GB | 82 min |

Die Eliminationen stimmen mit k157 überein. Bei q = 6 ergeben c8 und c7 die Ränge 3171 und 2274. Bei q = 7 ergeben c9 und c8 die Ränge 4323 und 3215, bei q = 8 ergeben c10 und c9 die Ränge 5723 und 4382.

## Prüfung der Kriterien
- Die Positivkontrolle stimmt: F_6 = 477, Rang 24.
- Alle Residuen liegen bei höchstens 1.1e-51, also unter 1e-30, und mindestens 1e36-mal unter dem kleinsten echten Gram-Eigenwert.
- Die Gram-Lücken sind größer als 1e20.

Der Test ist gültig. F_7 = 594 und F_8 = 723. **H59 ist bestätigt.**

## Lesart
- Das um die vier Bedingungen erweiterte System hat am Keim keine weiteren versteckten Bedingungen auf 7- und 8-Jets: Die Spencer-Schranken 4 und 3 werden nicht ausgeschöpft.
- Mit der Involutivität von g''_8 (Erkundung vom 3.11., Charaktere 723, 130, 12, 0) ist das System nach dem Kriterium von Goldschmidt am Keim formal integrabel. Vorausgesetzt ist dabei, dass zwei Eliminationsstufen alle Hindernisse erfassen.
- Die allgemeine formale Lösung hängt von 12 Funktionen dreier Variablen ab; nach H60 sind das 6 masselose Moden.
- Das gilt nur für das Vergleichsmodell und schließt OP5 nicht.

## Hinweis zu den Ressourcen
q = 8 brauchte 15.2 GB von 16 GB. Höhere Ordnungen gehen auf diesen Runnern nur mit dünnbesetzten Blöcken.
