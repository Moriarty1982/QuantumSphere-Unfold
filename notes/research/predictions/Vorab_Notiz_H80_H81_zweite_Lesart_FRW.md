# Vorab-Notiz H80 und H81: Die zweite Lesart auf FRW – Spiegelung um den Urknall (δ = 0) und mit Versatz (δ ≠ 0)

**Stand:** 5. November 2026, vor der Rechnung festgelegt. **Nicht blind:** Beide Erwartungen folgen analytisch aus der reduzierten Wirkung; die Rechnung (sympy, Numerik) macht sie nachprüfbar. Autor 21:29: beide Wege durchgehen, weil beide Zustände getrennt zu betrachten sein könnten.

## Vorwissen geprüft
`llm/Erkundung_Zweite_Lesart_FRW.md` (Aufbau, Befunde 1–5); H79 (vollständiger komplexer Boost, holomorphe Adjungierte, Autorentscheidung 21:23); H70 (Versatz in konformer Zeit fest); H78a (Skalar: Kinetik a − b, Potential a + b); Boyle–Finn–Turok, arXiv:1803.08928 (CPT-symmetrisches Universum, Vakuumwahl durch CPT).

## Aufbau
Konforme Zeit τ > 0, Strahlung a(τ) = τ bzw. Materie a(τ) = τ², Gewichte a = p₊, b = p₋ mit b/a = β_sym² (β_sym = 1/1,8203). Reduzierte Wirkung eines Skalars: S = ∫dτ d³x [½K(τ)(χ′² − (∇χ)²) − ½P(τ)m²χ²] mit K = a·a(τ)² − b·a_T², P = a·a(τ)⁴ + b·a_T⁴, a_T = Skalenfaktor, den das Bild sieht. Modengleichung (Kχ′)′ + (Kk² + Pm²)χ = 0.

## H80 (δ = 0, Spiegelung um den Urknall)
- **H80a:** a_T = |a(−τ)| = a(τ) für beide Fortsetzungen a(−τ) = ±a(τ). Dann K = (a − b)a², P = (a + b)a⁴, und die Modengleichung ist exakt die des Materie-Skalars mit m² ↦ (a + b)/(a − b)·m² = γ·m². **Bestätigt**, wenn sympy das für beide Fortsetzungen und beide Zeitalter exakt liefert.
- **Folge, vorab:** δ = 0 liefert keine neue Dynamik. Ein Zusammenhang mit dem CPT-Bild (Boyle–Finn–Turok) kann dann nur über Randbedingungen bei τ = 0 entstehen, die die Wirkung nicht festlegt.

## H81 (δ ≠ 0, Versatz)
a_T = a(|δ − τ|), δ = 1 (Einheiten).
- **H81a:** K verschwindet genau bei a(τ)/a(δ − τ) = β_sym: Strahlung τ* = β_sym/(1 + β_sym) ≈ 0,3546; Materie τ* = √β_sym/(1 + √β_sym) ≈ 0,4257. Vor τ* ist K < 0, danach K > 0.
- **H81b:** τ* ist ein regulär singulärer Punkt der Modengleichung mit Exponenten (0, 0). Allgemeine Lösungen divergieren dort logarithmisch, χ ≈ c₁ + c₂·ln|τ − τ*|; nur eine einparametrige Familie bleibt beschränkt. Numerische Prüfung: Für allgemeine Anfangsdaten wächst |χ| bei Annäherung an τ* linear in ln|τ − τ*| (Steigung ≠ 0, Fit-Güte R² > 0,99 auf den letzten drei Dekaden); die per Schießverfahren gewählte reguläre Lösung bleibt beschränkt (|χ| < 10·|χ(Start)|).
- **H81c:** Für τ < τ* ist P/K < 0: Moden mit k² < |P/K|·m² wachsen (tachyonisch). Prüfung: numerisches Wachstum einer Mode mit k = 0, m = 3 im Intervall (0,05; 0,9·τ*) über einem Faktor 10.
- **Folge, vorab:** Gelten H81a–c, hat die Variante mit Versatz eine ausgezeichnete frühe Epoche τ*, an der die Kinetik das Vorzeichen wechselt. Der Durchgang wählt eine Mode aus. Davor ist der Skalar tachyonisch. Ob das physikalisch tragbar ist (Divergenz, Energie), entscheidet der Test nicht.

Skript: `llm/k196_zweite_lesart_frw.py` (nach dem Commit dieser Notiz).
