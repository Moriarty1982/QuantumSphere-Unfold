# v4.10.0-r75: Datiertes Register des Modellstands und seiner Vorhersagen für Version v5.6.0 (Stand 28.11.2026)

Register-Runde ohne Rechnung. Anlass: Dauerauftrag des Autors vom 28.11.2026 (17:21): Jede öffentliche Version hält ihren Modellstand mit den
Vorhersagen fest (Datum, DOI; ältere Versionen bleiben sichtbar); hergeleitet und gesetzt werden gekennzeichnet; Korrekturen nur in einer neuen
Version mit Begründung (Modellfortschritt oder Fehler), nie Nachjustieren nach einer neuen Messung; als Test zählt die Version, die vor der Messung
festgeschrieben war. r75 ist das erste Register (für v5.6.0, Version-DOI noch zu reservieren); es gilt als Bezug ab der Veröffentlichung von v5.6.0.

| Teil | Inhalt |
|---|---|
| r75.1 | Regel „datierter Modellstand je Version“ (Definition) |
| r75.2 | Eingaben des Modellstands: Zählpostulat (r67) → β_sym = 0,5494056410 (berechnet, nicht hergeleitet); J → K = ⅔ (Postulat); Brannen-Form, H99 (Setzung); φ = 0,0395773 (gemessene Eingabe); Zweigvorzeichen (Setzung des Autors), q → 0⁻ (H236); μ_e, μ_ν angepasst; Messwerte; Platzhalter CT-001/002/004, Setzungen S1, V1 |
| r75.3 | Tabelle der offenen Vorhersagen mit Wert, Quelle und Datum, Prüfdaten und Widerlegungskriterium: Massenordnung, Σm_ν = 59,30 ± 0,24 meV, m₁,₂,₃ = 0,379/8,808/50,11 meV, m_β = 8,87 ± 0,04 meV, m_ββ = 1,29–4,00 meV (H227); R (H100 A/B/C); sin²θ₁₂ (H9 0,30862; H176 0,3019; Strukturlesart H206–H208 ≈ 0,318–0,3195 bzw. 0,3155 nur mit maximaler CP); sin²θ₂₃ (H42, H46, H176, H207); sin²θ₁₃ (H176, H207); δ_CP (H176 ±77,7°, H125 sin δ < 0); Ω_m = β_sym² = 0,30185 (H96); H112; m_W = 80,3615 ± 0,0018 GeV (H15); m_τ (H102 1777,134 gegen Koide 1776,969 MeV); H105 |
| r75.4 | je Vorhersage: hergeleitet / gesetzt / gemessen / nachträglich |
| r75.5 | Reichweite: H173–H212 nur in Forschungsnotizen, keine Runde; der Eintrag ins Register behauptet nichts über ihre Ergebnis-Notizen hinaus; Abhängigkeiten zwischen den Zeilen |

Quellen: `wiki/Pruefbare-Vorhersagen.md`, Tabelle „Offene Vorhersagen“ in `wiki/Vorhersagen-und-Tests.md`; jede Zahl gegen die Vorab- bzw.
Ergebnis-Notiz geprüft. Empfindlichkeiten der Experimente sind Literatur-Richtwerte, nicht nachgerechnet. Kriterien und Urteile unverändert.

Rundentext: `rounds/v4100_r75_round.tex` (wörtlich angehängt an `sources/research/parts/v4100-post-release-layers.tex`).
Keine Rechnung, kein Qiskit, kein HDL/MMA-Vergleich. Guard-Prüfung `tools/qs.py guards`: 0 Kandidaten. Guards unverändert.
