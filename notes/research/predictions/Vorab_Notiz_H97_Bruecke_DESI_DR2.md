# Vorab-Notiz H97: Die rückgekoppelte Kaskade (Brücke 3, ε = 1) gegen DESI DR2 BAO

**Stand:** 6. November 2026, vor der Rechnung festgelegt. Autor (6.11.): „Ja, H97 festlegen“, also Brücke 3 aus `Vorschlag_Bruecke_Kaskade_Friedmann.md` mit ε = 1. **Nicht blind:** Eine grobe Vorschau (H(z = 1) ≈ 6 % unter ΛCDM) ist bekannt und lässt eine Widerlegung erwarten. Außerdem sind die DESI-DR2-Daten veröffentlicht.

## Vorwissen geprüft
`Fundstellen_Dynamik_Lambda_Auslesung.md`, `Vorschlag_Bruecke_Kaskade_Friedmann.md` (mit Vorschau), r31 (Markov-Kaskade), r29 (Rückweg Paarerzeugung), H96 (Ω_M = β² heute), v4.8.0-r17 (Epoche), v4.8.0-r03 F11 (Herkunft von γ_L).

## Modell (festgelegt)
Flaches FRW mit
  ρ̇_Λ = −β²·H·ρ_Λ,  ρ̇_M + 3Hρ_M = β²·H·ρ_Λ,  ρ_r ∝ a⁻⁴,
heute Ω_M = β² = 0,301847, Ω_r = 9,1·10⁻⁵, Ω_Λ = 1 − Ω_M − Ω_r. Keine freie Größe außer der Abstandsskala h·r_d, die BAO allein nicht festlegt (wie bei DESI).

## Daten (festgelegt)
DESI DR2 BAO (arXiv:2503.14738, Tabelle IV, mit systematischem Fehler):
- BGS als D_V/r_d;
- LRG1, LRG2, LRG3+ELG1, ELG2, QSO und Lyα als D_M/r_d und D_H/r_d mit Korrelation r_{M,H};
- zusammen 13 Werte.

LRG3 und ELG1 einzeln werden nicht verwendet (wie bei DESI). Die Werte stammen aus der HTML-Fassung der Arbeit.

## Statistik und Kriterium
- χ²_min über h·r_d, 13 Werte, 12 Freiheitsgrade.
- **H97 widerlegt**, wenn p(χ²_min; 12) < 0,01, also χ²_min > 26,2.
- **Nicht ausgeschlossen**, sonst.
- Zum Vergleich wird flaches ΛCDM mit demselben Ω_M = β² berichtet, also H96 an DR2. Das ist kein Test, weil DR2 vor H96 bekannt war.

## Gültigkeit
Kontrolle der übertragenen Daten und des Codes: Flaches ΛCDM mit freiem Ω_m und h·r_d muss die DESI-Werte Ω_m = 0,2975 ± 0,0086 und h·r_d = 101,54 ± 0,73 Mpc auf ±0,003 bzw. ±0,5 Mpc reproduzieren. Gelingt das nicht, ist der Test ungültig.

## Nachträglich erlaubt (als Erkundung, nicht Teil des Tests)
Der Bereich von ε, den DR2 bei Ω_M = β² zulässt.
