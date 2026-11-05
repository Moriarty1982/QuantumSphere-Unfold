# Vorab-Notiz H84: Quantenmoden bei der Epoche τ* (zweite Lesart, Versatz δ ≠ 0)

**Stand:** 5. November 2026, vor der Rechnung festgelegt. **Nicht blind:** analytisch aus der Erhaltung der Wronski-Determinante. Autor 22:18 „mach weiter“; als Arbeitsannahme gilt mein Vorschlag, die Weyl-Kinetik hat das F3-Gewicht 1 (wie r81, H79), nicht als ausdrückliche Festlegung.

## Vorwissen geprüft
H81 (τ* = β_sym δ/(1 + β_sym) im Strahlungszeitalter, regulär singulär mit Exponenten (0, 0), eine reelle Lösung je k beschränkt, allgemeine ∝ ln|τ − τ*|); H80 (δ = 0 ohne neue Dynamik); `llm/Erkundung_Zweite_Lesart_FRW.md`; `llm/Erkundung_Spinorphase_zweite_Lesart.md`.

## Hypothese
Modengleichung (Kχ′)′ + (Kk² + Pm²)χ = 0 (Strahlung, δ = 1, Materie-Gewichte), Energiedichte einer Mode E = ½K(|χ′|² + k²|χ|²) + ½P m²|χ|².
- **H84a:** Für jede komplexe Lösung ist K·(χχ̄′ − χ̄χ′) konstant. Ist diese Konstante ≠ 0 (kanonische Normierung i), divergiert |χ′| bei τ* wie 1/|τ − τ*|; keine solche Lösung ist regulär.
- **H84b:** Für eine solche Mode gilt E·|τ − τ*| → endlicher Grenzwert ≠ 0, und E wechselt bei τ* das Vorzeichen. Das Integral von E über die Zeit divergiert logarithmisch.
- **Prüfung:** numerische Integration einer Mode mit Wronski-Determinante i (k = m = 1) bis |τ − τ*| = 10⁻⁸ von beiden Seiten; Wronski konstant auf 10⁻⁸ (relativ); E·|τ − τ*| auf den letzten drei Dekaden konstant auf 5 %.
- **Bestätigt**, wenn beides zutrifft.

## Folge, vorab festgelegt
Gilt H84, ist die Variante mit Versatz δ ≠ 0 quantenmechanisch bei τ* singulär: Die Modenauswahl aus H81 gilt nur klassisch, ein Quantenfeld kann sie nicht erfüllen. Für ein Quantenfeld spräche das für δ = 0 (H80). Ob eine Regularisierung (etwa ein endlich schneller Übergang statt der scharfen Nullstelle von K) das ändert, entscheidet der Test nicht.

Skript: `llm/k199_quantenmoden_tau_stern.py` (nach dem Commit dieser Notiz).
