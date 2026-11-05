# Vorab-Notiz H87: Wolfram-Gegenprobe zu H86 und der Abfall der Beimischung bei großem kΔ

**Stand:** 5. November 2026, vor der Rechnung festgelegt. **Nicht blind:** H87a und H87c wiederholen bekannte Werte mit einem unabhängigen System; H87b ist eine analytische Erwartung. Autor 23:21: „Use Wolfram for this“ (Wolfram-Connector neu verbunden).

## Vorwissen geprüft
`Ergebnis_H86_CPT_Zuordnung_Urknall.md` und `k201_out.json` (tanh-Profil, Δ = 2, Drehsinn +: |C| = 1,3114·10⁻², 5,2836·10⁻⁵, 2,9407·10⁻⁷, 1,2536·10⁻⁹ bei kΔ = 2, 4, 6, 8; Steigung −2,67, lokal 2,58–2,81, kein erkennbarer Lauf gegen π); `llm/Erkundung_Urknall_Uebergang.md` (scharfer Übergang: C₀ = (a + b)/(2a), D₀ = (a − b)/(2a), α = (1 + x)/(2√x), β = (1 − x)/(2√x)).

## Erwartung für H87b
Mit w = b^{1−s}a^{s}e^{iπ(1−s)} und s = (1 + tanh(τ/Δ))/2 ist w′/w = (L/(2Δ))·sech²(τ/Δ), L = ln(a/b) − iπ. Die nächsten Singularitäten liegen bei τ = ±iπΔ/2. Für Übergänge dieser Art fällt die Mischung wie e^{−πkΔ} mal einer Potenz von k (Vorwissen, Standardergebnis für analytische Profile); die lokale Steigung nähert sich π dann von unten wie π − p/(kΔ).

## Hypothesen und Kriterien
- **H87a (Gegenprobe):** Wolfram (NDSolve, WorkingPrecision ≥ 30) reproduziert |C| aus k201 bei kΔ = 2, 4, 6, 8 auf 10⁻⁵ relativ.
- **H87b:** Die lokale Steigung −d ln|C|/d(kΔ), gemessen zwischen kΔ = 20 und 30, liegt innerhalb 3 % bei π.
- **H87c:** Wolfram bestätigt symbolisch die Formeln des scharfen Übergangs (C₀, D₀, α, β, |α|² − |β|² = 1).
- **Bestätigt** je Teil, wenn das Kriterium erfüllt ist.

## Folge, vorab festgelegt
Gilt H87b, war die Steigung 2,67 in H86 ein Vorlaufeffekt, und der Abfall ist e^{−πkΔ} mit Potenzvorfaktor: Die Abschneideskala ist dann genau 1/(πΔ). Gilt H87a nicht, ist k201 oder die Wolfram-Rechnung fehlerhaft; die Ursache wird gesucht, bevor H87b gewertet wird.
