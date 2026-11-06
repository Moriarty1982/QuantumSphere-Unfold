# Vorab-Notiz H91: Abfall der Beimischung am Urknall bis kΔ = 60: Exponent π und ein Wurzelterm im Vorfaktor

**Stand:** 6. November 2026, vor der Rechnung festgelegt. **Nicht blind** für den Bereich bis kΔ = 30 (H87-Werte bekannt). Neu sind der Bereich 30–60, der Drehsinn − und die Form des Vorfaktors. Autor (6.11.): „weiter“; das war Option 2 der Übergabe („vorab festgelegter Test des Abfalls e^{−πkΔ} mit Potenzvorfaktor bis kΔ ≈ 60, Fit-Modell vorab festlegen“).

## Vorwissen geprüft
- `Ergebnis_H85_weicher_Urknall_Uebergang.md`, `Ergebnis_H86_CPT_Zuordnung_Urknall.md` (k201): Gleichung χ'' + (w'/w)χ' + k²χ = 0 mit w = b^{1−s}a^s e^{±iπ(1−s)}, s = ½(1 + tanh(t/Δ)). Also w'/w = L·s', L = ln(a/b) ∓ iπ, s' = sech²(t/Δ)/(2Δ). H86b: Steigung −2,67 je kΔ auf [2, 8].
- `Ergebnis_H87_Wolfram_Gegenprobe_Abfall.md` (k202): |C| bei kΔ = 10, 15, 20, 25, 30 (Drehsinn +, Δ = 2), lokale Steigungen 2,925 … 2,975; nachträglich der Fit (kΔ)^p e^{−s kΔ} mit s ≈ 3,08–3,15 und p ≈ 3–5. Die Methode ist die Integration entlang τ = x + ih unterhalb der Singularität iπΔ/2.
- Keine Notiz enthält einen Wurzelterm √(kΔ) oder eine Herleitung des Vorfaktors (Suche nach „sqrt“, „√(kΔ)“, „Wurzel“ in den Ergebnissen H85–H87).

## Analytische Erwartung (vor der Rechnung)
Mit χ = e^{−½∫p}u wird daraus u'' + Q u = 0, Q = k² − p²/4 − p'/2, mit p = L s'. Nahe der Singularität t₀ = iπΔ/2 gilt s' ≈ −Δ/(2(t − t₀)²). Dann ist p²/4 ≈ L²Δ²/(16(t − t₀)⁴), ein Pol vierter Ordnung im effektiven Potential. Die Umkehrpunkte liegen bei |t − t₀| ~ (|L|Δ/(4k))^{1/2}, und das Phasenintegral zwischen ihnen und t₀ trägt einen Beitrag der Ordnung √(kΔ|L|). Erwartet wird deshalb
ln|C| ≈ c₀ − π·kΔ + c₁·√(kΔ) + q·ln(kΔ),
also exakt der Exponent π aus der Lage der Singularität. Dazu kommt ein Wurzelterm, der die scheinbar zu kleine Steigung von H87 erklärt: Die lokale Steigung ist π − c₁/(2√(kΔ)), sie steigt langsam gegen π. Die Koeffizienten c₁ und q werden nicht vorhergesagt.

## Rechnung
Python/scipy (`llm/k206_abfall_wurzelterm.py`), tanh-Profil, Δ = 2, a, b wie k201, beide Drehsinne ±. Integration entlang τ = x + ih mit h = 0,90 und 0,95·πΔ/2 (DOP853, rtol 10⁻¹², Rand ±60). C ist der Koeffizient von e^{−ikτ} rechts bei einlaufendem e^{ikτ} von links (wie k202). Gitter kΔ = 10, 12,5, …, 60.

## Hypothesen und Kriterien
- **H91a (Genauigkeit):** Die beiden Konturen stimmen für alle kΔ ≤ 60 relativ auf ≤ 10⁻⁶ überein. Die Werte bei kΔ = 10–30 (Drehsinn +) stimmen mit H87 auf ≤ 10⁻⁵ überein. Wenn a nicht erfüllt ist, gelten b–d als ungültig, nicht als widerlegt.
- **H91b (Exponent):** Fit ln|C| = c₀ + c₁√x + q ln x − s x auf x = kΔ ∈ [20, 60], für beide Drehsinne. s liegt innerhalb 1 % bei π.
- **H91c (Wurzelterm nötig):** Bei festem s = π ist der quadratische Mittelwert der Fit-Reste (in ln|C|) mit Wurzelterm (c₀, c₁, q frei) mindestens zehnmal kleiner als ohne Wurzelterm (c₀, q frei), auf [20, 60], für beide Drehsinne.
- **H91d (lokale Steigung):** Die Steigung zwischen kΔ = 50 und 60 liegt innerhalb 3 % bei π (das Kriterium von H87b, weiter außen).

## Umgang mit Abweichungen
Ein Fehllauf wird offengelegt. Wenn b erfüllt ist, c aber nicht, ist der Exponent π bestätigt und die Form des Vorfaktors offen. Wenn b verfehlt wird, ist die Lesart „Abschneideskala 1/(πΔ)“ aus r86 neu zu bewerten.
