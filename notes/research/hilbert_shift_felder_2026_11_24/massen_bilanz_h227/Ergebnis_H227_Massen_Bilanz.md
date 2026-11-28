# Ergebnis H227 (k441): Drei Zahlen tragen alle sechs Leptonenmassen; die absolute Neutrinoskala ist vorhergesagt, das Skalenverhältnis ist frei

**Datum:** 2026-11-28. **Vorab:** `Vorab_H227_Massen_Bilanz.md` (Commit a7451dc, vor der Rechnung). **Urteil: trägt teilweise** (Vorhersagen verträglich und
festgeschrieben, kein Treffer für das Skalenverhältnis).
**Werkzeuge:** Python (`k441_test_h227.py` → `k441_out.txt`), Wolfram unabhängig (`k441b_gegenprobe.wl` → `k441b_out.txt`); alle Zahlen stimmen überein. Qiskit nicht
einschlägig. Teil 1 und die Massen in Teil 2 waren nicht blind (Koide, H213, H168), m_β und m_ββ neu, Teil 3 Erkundung (nicht blind, Größenordnung vorab überschlagen).

## Frage
Marc: „Was ist, wenn man erstmal nur nach den Leptonenmassen sucht?“ Wie viele Massen legt das jetzige Bild mit wie vielen Eingaben fest, welche Neutrino-Größen folgen
daraus, und ist das Verhältnis der beiden Sektorskalen eine Rahmenzahl?

## Ergebnis
**1 Bilanz.** Sechs Massen, drei Eingaben (φ, μ_e, μ_ν), gesetzt: K = ⅔ (a = √2), Zweigvorzeichen.
| Vorhersage | Wert | Daten | Abstand |
|---|---|---|---|
| m_τ aus m_e, m_μ (Koide) | 1776,969 MeV | 1776,93 ± 0,09 | +0,43σ |
| R = Δm²₂₁/Δm²₃₁ aus φ | 0,030839 | 0,030016 ± 0,000457 | +1,80σ |
| absolute Neutrinoskala | Teil 2 | noch nicht gemessen | Vorhersage |

φ aus m_e und m_μ allein ist identisch mit dem Wert aus m_τ unter J (Differenz 1·10⁻¹²). Neutrino-Wurzeln (aufsteigend): −0,1958; 0,9440; 2,2518 (eine negative, H99).

**2 Festgeschriebene Vorhersagen** (normale Ordnung; μ_ν aus Δm²₃₁; Fehler aus Δm²₃₁ und φ):
| Größe | Vorhersage | aktuelle Schranke |
|---|---|---|
| m₁, m₂, m₃ | 0,379 ± 0,002 / 8,808 ± 0,036 / 50,11 ± 0,20 meV | — |
| Σm | **59,30 ± 0,24 meV** | < 64,2 meV (DESI DR2 + CMB, 95 %) |
| m_β | 8,87 ± 0,04 meV | < 450 meV (KATRIN) |
| m_ββ | 1,29 bis 4,00 meV (Majorana-Phasen frei); 3,49 meV mit der Brannen-Vorzeichenlage (Lesart) | < 28–122 meV (KamLAND-Zen) |
Kontrolle mit μ_ν aus Δm²₂₁: Σm = 58,50 meV (der Unterschied ist die 1,8σ-Spannung in R). **Kriterium 2: verträglich.**

**3 Skalenverhältnis (Erkundung).** M_e = μ_e² = 313,856 MeV, M_ν = μ_ν² = 9,883 meV, ρ = M_ν/M_e = 3,149·10⁻¹¹ (μ_ν/μ_e = 5,61·10⁻⁶).
Potenzen: β_sym^40,38; γ_M^16,82; (1/γ_L)^38,81; e^(−2ε·19,58): keine ganze Zahl innerhalb 0,05 (Zufallserwartung 0,4). Seesaw-Lesarten: M_e²/M_ν = 1,0·10¹⁰ GeV,
v²/M_ν = 6,1·10¹⁵ GeV; keine innerhalb Faktor 1,1 von v oder der Planck-Masse. **Kein Treffer.**

**Gesamturteil nach Vorab: trägt teilweise.**

## Lesart
- **Die Leptonenmassen sind im jetzigen Bild fast geschlossen.** Drei Zahlen (ein Winkel, zwei Skalen) tragen sechs Massen; zwei der drei Vorhersagen sind heute geprüft
  (Koide 0,4σ, R 1,8σ), die dritte (absolute Neutrinoskala) ist festgeschrieben.
- **Die schärfste kommende Prüfung ist Σm = 59,3 meV.** Das liegt knapp über dem Minimum der normalen Ordnung (≈ 58,7 meV bei m₁ = 0), weil m₁ = 0,38 meV sehr klein ist.
  Kosmologische Messungen (DESI, Euclid, CMB-S4) mit Empfindlichkeit um 15–20 meV prüfen das. Eine Messung Σm < 58 meV oder ein Nachweis der umgekehrten Ordnung
  widerlegt das Bild. Nachträglicher Hinweis: Die DESI-DR2-Auswertung bevorzugt im ΛCDM-Fit sehr kleine Σm; falls sich das erhärtet, gerät jede normale Ordnung mit
  m₁ ≈ 0 unter Druck, auch diese.
- **Was frei bleibt:** φ (gemessen, H221–H226 ohne Herleitung) und das Verhältnis der Skalen ρ ≈ 3·10⁻¹¹. Das Verhältnis ist keine einfache Rahmenzahl und keine einfache
  Seesaw-Größe mit v oder der Planck-Masse. v²/M_ν ≈ 6·10¹⁵ GeV liegt in der Größenordnung üblicher Vereinheitlichungsskalen; das ist kein Treffer nach der Vorab-Liste
  und wird nicht gewertet.

## Hergeleitet, gesetzt, nachträglich
- **Hergeleitet/gerechnet:** Bilanz (m_τ, R), Neutrinomassen, Σm, m_β, m_ββ-Bereich, ρ.
- **Gesetzt:** Brannen-Form, K = ⅔, gemeinsames φ (H221), Zweig/normale Ordnung (H222), Polmassen-Schema (H214), Mischungsdaten für m_β/m_ββ; Vorzeichen-Lesart für m_ββ.
- **Nachträglich:** Hinweis auf die DESI-DR2-Tendenz; v²/M_ν in der Größenordnung von Vereinheitlichungsskalen (nicht gewertet).

## Grenzen
Baumniveau, keine Laufeffekte; Majorana-Phasen frei; die δ_CP-Phase in U_e3 ist für m_ββ nicht berücksichtigt (Bereich bleibt gültig, die Vorzeichen-Lesart ist eine
Näherung). Teil 3 mit kleiner Liste, nicht blind. Kein Guard berührt; OP3/OP4 offen.

## Dateien
`Vorab_H227_Massen_Bilanz.md`, `k441_test_h227.py`/`k441_out.txt`, `k441b_gegenprobe.wl`/`k441b_out.txt` (erster Wolfram-Lauf teils auf falschem Zweig, siehe Kopf), `README.md`.

Vergeben: H227, k441. Nächste frei: H228, k442 (vor Vergabe gegen `main` prüfen).
