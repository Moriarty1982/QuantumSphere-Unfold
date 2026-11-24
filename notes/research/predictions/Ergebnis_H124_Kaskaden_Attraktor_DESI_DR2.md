# Ergebnis H124: Kaskade mit Attraktor Ω_M = β² (ε = 3) an DESI DR2 BAO nicht ausgeschlossen, aber mit Ω_M heute ≈ 0,50 und Δχ² = 7,9 gegen ΛCDM

Vorab-Notiz `Vorab_Notiz_H124_Kaskaden_Attraktor_DESI_DR2.md`, Commit `7b2b665` (nicht blind). Code `../op5_attractor_2026_11_23/k243_test_h124.py`, Ausgabe `k243_out_teilB.txt`. Ein Lauf.

## Gültigkeit erfüllt
Flaches ΛCDM mit freiem Ω_m: 0,2970 und h·r_d = 101,56 Mpc (DESI: 0,2975, 101,54), χ² = 10,55.

## Ergebnis
- **H124, Kaskade mit ε = 3 (Attraktor Ω_M* = β²), Ω_M0 frei:** χ²_min = 18,42 bei 11 Freiheitsgraden, p = 0,072, bei Ω_M0 = 0,5006 und h·r_d = 95,49 Mpc. **Nicht ausgeschlossen** (Schwelle 24,72).
- Gegen flaches ΛCDM (gleiche Zahl freier Größen) liegt das Modell um Δχ² = 7,87 schlechter. Das ist keine Widerlegung nach dem Kriterium, aber eine deutliche Bevorzugung von ΛCDM durch dieselben Daten.
- **Was das Modell über heute sagt:** Ω_M heute ≈ 0,50, nicht β². Der Wert β² wird erst asymptotisch erreicht. H96 (Ω_M heute = β² in flachem ΛCDM) und dieses Modell beschreiben verschiedene Größen; das Modell erklärt das „warum heute“ also nicht, es verschiebt β² in die Zukunft.

## Erkundung (nachträglich erlaubt): ε bei freiem Ω_M0
| ε | Attraktor εβ²/3 | bestes Ω_M0 | χ² | p(11) |
|---|---|---|---|---|
| 0,1 | 0,010 | 0,304 | 10,29 | 0,51 |
| 0,5 | 0,050 | 0,333 | 9,54 | 0,57 |
| 1 | 0,101 | 0,368 | 9,35 | 0,59 |
| 2 | 0,201 | 0,436 | 11,78 | 0,38 |
| 3 | 0,302 | 0,501 | 18,42 | 0,072 |

Bei freiem Ω_M0 ist BAO allein mit kleinen ε gleich gut wie ΛCDM. Nur ε = 3 liefert den Attraktor β²; gerade dort steigt χ² deutlich. H97 hatte ε = 1 nur bei festem Ω_M0 = β² ausgeschlossen.

## Grenzen
- Nur BAO, wie vorab festgelegt. CMB (Schallhorizont, frühe Materiedichte), Supernovae und Strukturwachstum sind nicht geprüft; eine Kopplung δ = 0,906 und Ω_M0 ≈ 0,5 dürften dort stark unter Druck geraten (Vorwissen, nicht gerechnet).
- ε = 3 folgt aus der Attraktorforderung, nicht aus der Struktur; die Übersetzung Fluss → Dichte (Inhalt von S² = Vakuum, w = −1) ist die Setzung von Brücke 3 (r05.5).

## Bilanz der Setzungen
- **Gesetzt:** Brücke 3 (S²-Inhalt ist Vakuum, Rückweg mit Γ = εH), ε = 3 aus der Forderung „Attraktor = β²“.
- **Hergeleitet:** Fixpunkte, Stabilität, Bahn (k243 Teil A); das Datenergebnis.
- **Wohin die offene Wahl wandert:** vom Wert von Λ und der Epoche (r56) zur Rate Γ; Ω_M heute ist wieder frei (0,50 aus den Daten), also bleibt die Epoche eine Eingabe.

## Folge
Zurückgestellte Ideen geprüft: I7 ist dieser Weg; kein anderer Auslöser trifft zu. Ein blinder Test wäre derselbe Modellvorschlag gegen DESI DR3 (erst nach Freigabe vorab festzulegen).
