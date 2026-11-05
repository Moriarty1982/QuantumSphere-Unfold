# Vorab-Notiz H86: CPT-Zuordnung und endliche Beimischung am Urknall (G2, komplexer Übergang)

**Stand:** 5. November 2026, vor der Rechnung festgelegt. **Nicht blind, nachträglich motiviert:** Die Hypothesen stammen aus den Daten von H85 (Δ = 1, tanh-Profil). Geprüft wird deshalb an neuen Einstellungen: Breite Δ = 2 und, wo möglich, ein anderes Profil (Fehlerfunktion). Autor 22:52: „erst rechnen“.

## Vorwissen geprüft
`Ergebnis_H85_weicher_Urknall_Uebergang.md` (Kriterien verfehlt; nachträglich: adiabatisch wird die T-Mode positiver Norm zur M-Mode negativer Frequenz, Beimischung C fällt für kΔ ≳ 1 exponentiell, Drehrichtungen asymmetrisch, geometrisches Mittel von |D| bei den Grenzwerten); `llm/Erkundung_Urknall_Uebergang.md` (scharf: C₀ = (a + b)/(2a), D₀ = (a − b)/(2a)); Autorentscheidung G2; Boyle–Finn–Turok (CPT-Bild).

## Aufbau
Wie H85: (wχ′)′ + wk²χ = 0, w = b^{1−s}a^{s}e^{±iπ(1−s)}, Start e^{+ikτ} bei τ = −L, Zerlegung am Ende in C·e^{−ikτ} + D·e^{+ikτ}, L = 20Δ (Fehlerfunktion: L = 10Δ). Profile: P1 tanh, s = (1 + tanh(τ/Δ))/2; P2 Fehlerfunktion, s = (1 + erf(τ/Δ))/2. Δ = 2.

## Hypothesen und Kriterien
- **H86a (CPT-Zuordnung, P1 und P2):** Für kΔ ≥ 6 gilt |C| < 10⁻² für beide Drehrichtungen, und das geometrische Mittel √(|D₊||D₋|) liegt innerhalb 2 % bei √(b/a).
- **H86b (exponentieller Abfall, P1):** ln|C| ist für kΔ ∈ [2, 8] linear in k (R² > 0,99), und der Betrag der Steigung je Einheit kΔ liegt innerhalb 15 % bei π (Erwartung für ein tanh-Profil, Vorwissen über Übergänge vom tanh-Typ).
- **H86c (Grenzfall langer Wellen, P1 und P2):** Bei kΔ = 0,01 ist |C − C₀|/C₀ < 1 %.
- **H86d (Asymmetrie, P1 und P2):** Bei kΔ = 0,02 ist |D₋|/|D₊| ≠ 1 um mehr als 1 %, und das geometrische Mittel √(|D₊||D₋|) liegt innerhalb 2 % bei D₀.
- **Kontrolle:** holomorphe Wronski-Determinante konstant auf 10⁻⁸.

## Folge, vorab festgelegt
Gelten a–d, ist die nachträgliche Lesart aus H85 an neuen Einstellungen bestätigt: Der Urknall ordnet unter G2 Teilchen der Tachyon-Lesart vor ihm Antiteilchen-artige Zustände danach zu (CPT), mit einer Beimischung, die für lange Wellen durch β_sym festgelegt ist und oberhalb von 1/Δ abfällt; die Drehrichtung erzeugt eine Asymmetrie. Was die Asymmetrie physikalisch bedeutet, entscheidet der Test nicht.

Skript: `llm/k201_cpt_zuordnung.py` (nach dem Commit dieser Notiz).
