# Vorab-Notiz H59: weitere versteckte Bedingungen auf 7- und 8-Jets?

**Geschrieben und committet am 3. November 2026, bevor gerechnet wird.**

**Status: vorregistriert, nicht blind.** Die Symboldimensionen g''_7 = 594 und g''_8 = 723 sind bekannt (r74.1, Erkundung vom 3.11.). Unbekannt ist die Größe, die hier entschieden wird: die Dimension der Jet-Fasern unter Einbeziehung der Terme niedrigerer Ordnung. Dafür gibt es noch keine Rechnung.

## Frage
Die Spencer-Kohomologie des erweiterten Symbols (r74.2) lässt H^{6,2}(g'') = 4 und H^{7,2}(g'') = 3 zu. Es kann also bis zu 4 weitere versteckte Bedingungen auf 7-Jets und bis zu 3 auf 8-Jets geben. Ob sie tatsächlich auftreten, entscheiden die Terme niedrigerer Ordnung.

## Hypothese H59
Es gibt keine weiteren versteckten Bedingungen:
- Faser der 7-Jets F_7 = 594;
- Faser der 8-Jets F_8 = 723.

## Messung
Das Skript ist `k159_hp_faser.py` mit Parameter q. Es verallgemeinert k157 (q = 6) auf beliebiges q und läuft auf GitHub-Runnern, ein Job je q:
1. Der Jet bis Grad q−1 ist fest; die Gleichungen gehen bis Grad q+1.
2. c_{q+2} wird eliminiert, dann c_{q+1}. Dafür werden Linkskerne in float bestimmt und mit Newton in arb nachgeschärft (70 Stellen).
3. N_q ist der Kern von [R_{q−1}; G_q] auf c_q. Darauf werden die abgeleiteten Bedingungen C bestimmt, dann die Gram-Eigenwerte von C.
4. Der Rang r ist die Stelle der größten Lücke zwischen benachbarten Gram-Eigenwerten. Ausgewertet wird F_q = dim N_q − r.

Datengrundlage ist `hp_work2/AB_taylor2.pkl` (k153b, dps 160) mit Taylorgrad 2 in x. Das genügt: Mit festem Jet bis Grad q−1 treten nur Blöcke mit k+1−m ≤ 2 auf.

## Positivkontrolle
q = 6 muss F_6 = 477 und r = 24 wiedergeben (k157).

## Gültigkeit
Der Test ist gültig, wenn alle drei Bedingungen erfüllt sind:
- die Positivkontrolle stimmt;
- alle Newton-Residuen sind ≤ 1e-40;
- die entscheidende Gram-Lücke beträgt ≥ 1e20 bei q = 7 und bei q = 8.

Sonst ist der Test ungültig.

## Entscheidung
| Ergebnis | Bedingung |
|---|---|
| H59 bestätigt | F_7 = 594 und F_8 = 723 |
| H59 widerlegt | F_7 ∈ {590, …, 593} oder F_8 ∈ {720, 721, 722}; die Zahl der neuen Bedingungen ist 594 − F_7 bzw. 723 − F_8 |
| ungültig (Befund, kein Ergebnis) | jeder andere Wert, also auch F_q größer als das Symbol oder unterhalb der Spencer-Schranke |

## Lesart
Bei Bestätigung folgt mit der Involutivität von g''_8 (r74, Erkundung) nach Goldschmidt die formale Integrabilität des vervollständigten Systems am Keim. Voraussetzung ist, dass zwei Eliminationsstufen alle Hindernisse erfassen; das ist so wie bei den sechsten Ordnungen. Das schließt OP5 nicht: Es bleibt eine Aussage über das Vergleichsmodell.
