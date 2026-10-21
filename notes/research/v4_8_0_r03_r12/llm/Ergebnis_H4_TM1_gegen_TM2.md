# Ergebnis H4: TM1 gegen TM2 — Vergleich 1:1

Vorab-Notiz: `Vorab_Notiz_H4_TM1_gegen_TM2.md`, Commit 00d297e (2026-10-20 02:46 UTC), vor dem Vergleich.
Skript: `k18_test_h4.py`. Daten und Kriterium unverändert.

## Ergebnisse (NuFIT 6.0 IC24 + SK, NO; Gauß-Näherung mit asymmetrischen Fehlern)

| | TM1 (2,−1,−1)/√6 | TM2 (1,1,1)/√3 |
|---|---|---|
| χ²_min (2 Freiheitsgrade) | **4,43** | **14,72** |
| davon θ₁₂ (nicht blind) | 0,73 | 7,51 |
| davon δ_CP (blind) | 3,65 | 6,43 |
| sin²θ₁₂ | 0,3182 | 0,3409 |
| δ_CP im Bestfit | 262° | 278° |
| δ_CP für sin²θ₂₃ ∈ [0,457; 0,487] | 259–267° (oder 93–101°) | 277–293° (oder 67–83°) |

Δχ² = χ²(TM2) − χ²(TM1) = **10,3**, Bayes-Faktor etwa 170 : 1 für TM1.

## Urteil nach dem festgelegten Kriterium

- **Starke Bevorzugung von TM1** (|Δχ²| ≥ 6).
- **TM2 für sich disfavorisiert** (χ²_min = 14,7 > 9).
- Auch der blinde Teil (nur δ_CP) bevorzugt TM1 leicht (Δχ² = 2,8). Den Hauptteil trägt aber θ₁₂, und der war
  vorher bekannt.

## Einordnung (ehrlich)

- Die naheliegende Triolen-Deutung (erhaltene Skalar-Richtung (1,1,1)) verliert. Gewinner ist die Spalte in der
  Triolen-Ebene. Das Modell begründet bisher nicht, warum gerade diese Spalte erhalten bleibt.
- TM1 hat selbst Spannung bei δ_CP (etwa 1,9σ: 262° gegen 212° +26°). Die NuFIT-Verteilung von δ_CP ist breit und
  nicht gaußförmig; die Gauß-Näherung überzeichnet diese Spannung eher.
- **Nächster echter Test kommt bald:** JUNO misst sin²θ₁₂ auf etwa 0,5 %. TM1 verlangt 0,318. Bleibt der
  Mittelwert bei 0,308, wäre auch TM1 klar ausgeschlossen. δ_CP ≈ 260° (maximale CP-Verletzung) prüfen DUNE und
  Hyper-K in den 2030ern.

## Status

[P] TM1 stark bevorzugt gegenüber TM2, TM2 disfavorisiert. Festgeschriebene Vorhersagen für TM1:
sin²θ₁₂ = 0,318, δ_CP = 259–267° (bei sin²θ₂₃ im 1σ-Bereich). Guards unberührt.
