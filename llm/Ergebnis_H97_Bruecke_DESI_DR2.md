# Ergebnis H97 widerlegt: Die rückgekoppelte Kaskade mit einem Schritt je Hubble-Zeit (ε = 1) ist an DESI DR2 BAO deutlich ausgeschlossen

Vorab-Notiz `Vorab_Notiz_H97_Bruecke_DESI_DR2.md`, Commit `de36fcc` (nicht blind; Widerlegung nach der Vorschau erwartet). Code `k216_bruecke_desi_dr2.py`, Ausgabe `k216_out.txt`. Ein Lauf.

## Gültigkeit erfüllt
Flaches ΛCDM mit freiem Ω_m gibt mit den übertragenen 13 DESI-DR2-Werten Ω_m = 0,2970 (+0,0085/−0,0080) und h·r_d = 101,56 Mpc. DESI selbst gibt 0,2975 ± 0,0086 und 101,54 ± 0,73 an. Das liegt innerhalb der Toleranz (0,003 bzw. 0,5 Mpc), die Daten sind also richtig übertragen und der Code rechnet richtig.

## Ergebnis
- **H97, Kaskade mit ε = 1 bei Ω_M = β²:** χ²_min = 105,0 bei 12 Freiheitsgraden, p = 6·10⁻¹⁷. **Widerlegt** (Schwelle 26,2).
- Vergleich, kein Test: Flaches ΛCDM mit Ω_M = β² = 0,30185 hat χ² = 10,9 (p = 0,54). H96 ist mit DR2 verträglich, was vorher bekannt war.

## Erkundung (nachträglich erlaubt): welches ε DR2 bei Ω_M = β² zulässt
| ε | 0 | 0,05 | 0,1 | 0,2 | 0,3 | 0,5 | 1 |
|---|---|---|---|---|---|---|---|
| χ² | 10,87 | 10,44 | 10,36 | 11,39 | 14,14 | 25,74 | 105,0 |
| p | 0,54 | 0,58 | 0,58 | 0,50 | 0,29 | 0,012 | 6·10⁻¹⁷ |

Erlaubt ist etwa ε ≲ 0,4, also ein Kaskadenschritt höchstens alle 2–3 Hubble-Zeiten. Eine Vorliebe für ε > 0 gibt es nicht (Δχ² ≈ 0,5).

## Folge
- **Die einfachste Brücke von der r31-Kaskade zur Friedmann-Gleichung, ohne freien Parameter, ist ausgeschlossen.** Mit einem freien ε ist sie mit den Daten verträglich, sagt dann aber nichts mehr voraus. ε ist ein neuer freier Parameter, und die Daten sind mit ε = 0 (ΛCDM) gleich gut beschrieben.
- Damit bleibt die Λ-Auslesung eine Aussage über eine Epoche (H96: Ω_M heute = β², mit DR2 verträglich, Prüfung an DR3 oder Euclid steht aus), ohne Dynamik aus der Struktur.
- Weil der Ansatz gescheitert ist, habe ich die Auslöser der zurückgestellten Ideen geprüft: Keiner trifft zu. I3 ist bereits als gescheitert vermerkt.
