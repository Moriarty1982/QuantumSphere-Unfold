# Vorab-Notiz H85: Weicher Übergang am Urknall unter G2 – endliches Spektrum der Teilchenerzeugung?

**Stand:** 5. November 2026, vor der Rechnung festgelegt. **Teilweise nicht blind:** H85a folgt aus den Übergangsbedingungen (Grenzfall des scharfen Übergangs, schon in der Erkundung gerechnet); H85b ist eine Erwartung aus der WKB-Näherung, nicht gerechnet; H85c ist offen. Autor 22:46 „mach das so“: **Gebiet G2** (Materie-Lesart nach, Tachyon-Lesart vor dem Urknall) und der Test mit weichem Übergang.

## Vorwissen geprüft
`llm/Erkundung_Urknall_Uebergang.md` (scharfer Übergang: C = (a + b)/(2a), D = (a − b)/(2a), n = 0,404 je Mode, k-unabhängig); H84 (Nullstelle des Kinetik-Gewichts macht Quantenmoden singulär); H79 und Autorentscheidung (holomorphe Adjungierte); r81/K (komplexe Lesart); `llm/Erkundung_Spinorphase_zweite_Lesart.md` (teilweise Wick-Drehung); Gesamtbild T11 (Wick-Drehung als Teilungsmechanismus, Lesart).

## Aufbau
Konformes Feld, eine Mode k, konforme Zeit τ. Gewicht w(τ) von −b (τ ≪ 0) nach a (τ ≫ 0), Gleichung (wχ′)′ + w·k²χ = 0. Ein reeller Verlauf hätte eine Nullstelle (H84: singulär). Deshalb komplex: w(τ) = b^{1−s}·a^{s}·e^{±iπ(1−s)}, s(τ) = (1 + tanh(τ/Δ))/2, |w| > 0 überall. Erhalten ist die holomorphe Wronski-Determinante w(χ₁χ₂′ − χ₂χ₁′). Start bei τ = −20Δ mit der Mode e^{+ikτ}; am Ende Zerlegung χ = C·e^{−ikτ} + D·e^{+ikτ}. Materie-Gewichte a = p₊, b = p₋, Δ = 1.

## Hypothesen
- **H85a:** Für kΔ → 0 gehen C und D in die Werte des scharfen Übergangs über: relative Abweichung < 1 % bei kΔ = 0,01, für beide Drehrichtungen.
- **H85b:** Für große kΔ verschwindet die Mischung: |D/C| < 10⁻³ bei kΔ = 5 (Erwartung aus WKB: χ ≈ w^{−1/2}e^{±ikτ}, adiabatisch keine Mischung). Dann ist das Spektrum endlich, und Δ legt die Skala fest, oberhalb derer keine Teilchen entstehen.
- **H85c (offen):** Ob beide Drehrichtungen (±iπ) dasselbe |D| geben; angegeben wird das Ergebnis.
- **Kontrolle:** Die holomorphe Wronski-Determinante bleibt über die Integration konstant (relativ < 10⁻⁸).

## Folge, vorab festgelegt
Gelten H85a und b, gibt G2 mit komplexem (teilweise Wick-gedrehtem) Übergang eine Teilchenerzeugung am Urknall mit n ≈ 0,404 bei großen Wellenlängen, abgeschnitten bei k ~ 1/Δ. Die Höhe ist durch β_sym festgelegt, die Abschneideskala Δ ist eine neue, freie Größe. Gilt H85b nicht, ist das Spektrum auch weich nicht endlich.

Skript: `llm/k200_weicher_urknall.py` (nach dem Commit dieser Notiz).
