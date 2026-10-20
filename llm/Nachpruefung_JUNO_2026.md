# Nachprüfung von H2, H4, H8 mit JUNO 2026

Stand 2026-10-20. Die Vorhersagen und Kriterien von H2, H4 und H8 bleiben unverändert (Vorab-Notizen 434c5a8,
00d297e, f6734ab). Neu sind nur die Daten: JUNO Collaboration, *Measurement of Neutrino Oscillation Parameters at
JUNO and Indication of the Neutrino Mass Ordering*, arXiv:2609.37895 (29.09.2026), 207,2 Messtage:
sin²θ₁₂ = 0,3036 ± 0,0064; Δm²₂₁ = (7,388 ± 0,078)·10⁻⁵ eV²; Δm²₃₁ = +2,509 (+0,027/−0,025)·10⁻³ eV² (NO),
−2,482 (+0,025/−0,026)·10⁻³ eV² (IO); normale Ordnung bevorzugt mit mindestens 2,1σ (einseitig, über alle δ_CP).

Diese Messung lag beim Festschreiben von H2–H8 schon vor, war aber nicht bekannt und nicht verwendet (Datenbasis
war NuFIT 6.0). Sie ist damit eine unabhängige Nachprüfung, kein im strengen Sinn zukünftiger Test.

**Vor der Rechnung festgelegte Datenwahl:** sin²θ₁₂ = gewichtetes Mittel aus NuFIT 6.0 (0,308 ± 0,0115,
symmetrisiert) und JUNO 2026 = 0,3046 ± 0,0056 (unabhängig, da NuFIT 6.0 älter ist). Für H2 die Massendifferenzen
aus JUNO 2026. Alle übrigen Größen wie zuvor aus NuFIT 6.0.

## Ergebnisse

| Test | vorher (NuFIT 6.0) | jetzt | Urteil nach festem Kriterium |
|---|---|---|---|
| H2 Neutrino-Triole | NO, Σ = 0,0592 eV | NO, Σ = 0,0591 eV (m = 0,36 / 8,60 / 50,09 meV); IO 0,102 eV | verträglich; NO-Vorhersage von JUNO gestützt (≥ 2,1σ) |
| H4 TM1 gegen TM2 | 4,4 gegen 14,7 | **9,6** gegen 49,1 (Δχ² = 39,5) | TM1 bleibt weit vor TM2, ist aber für sich **disfavorisiert** (χ² > 9 bei 2 FG) |
| H8 Cayley–Dickson-CP | 8,8, Spannung | **14,0** (3 FG) | **disfavorisiert** (≥ 11,34) |

Ursache ist θ₁₂: TM1 verlangt 0,3182, die kombinierte Messung liegt bei 0,3046 ± 0,0056 (2,4σ). Der
θ₁₂-Beitrag zum χ² stieg von 0,73 auf 5,87. δ_CP trägt weiter 3,65 (TM1) bzw. 4,98 (H8) bei.

## Einordnung

- Die TM1-Linie (H4, H8) steht nach den neuen JUNO-Daten unter deutlichem Druck. Die genaueren künftigen
  JUNO-Messungen werden sie bestätigen oder widerlegen; bleibt der Mittelwert bei etwa 0,304, ist TM1 bei
  σ ≈ 0,003 mit mehr als 4σ ausgeschlossen.
- Die nachträglich gefundene Relation H9 (sin²θ₁₂ = 0,3086) liegt 0,7σ neben dem kombinierten Wert. Das ist kein
  Beleg (nachträglich, siehe Vorab-Notiz H9), aber der Grund, warum H9 jetzt als eigene Vorhersage festgeschrieben ist.
- H2 bleibt die robusteste Aussage der Neutrino-Linie: normale Ordnung, Σm_ν ≈ 0,059 eV.
