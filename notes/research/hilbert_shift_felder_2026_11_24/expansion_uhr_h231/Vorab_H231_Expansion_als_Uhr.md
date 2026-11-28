# Vorab-Notiz H231 (k445): Expansion als Uhr – friert die Hubble-Reibung φ beim Messwert ein?

Stand 28.11.2026, vor der Rechnung festgeschrieben. Anlass ist eine Idee des Autors (13:50 UTC): ein Teilchen rollt von einem Energieberg, und die
Expansion des Raums spielt dabei mit. Der Koordinator hat sie mit H228 verbunden, der Autor stimmte um 13:51 UTC mit „ja“ zu. In H228 fehlte für die Lesart
„φ ist ein Zwischenstand auf dem Weg von 0 zum Minimum π/8“ eine natürliche Uhr. Die Expansion könnte diese Uhr sein: Hubble-Reibung bremst das Rollen.

## Vorwissen geprüft

- H228/k442: Der Gradientenfluss φ(t) = π/8 − (2/3) arctan(tan(3π/16) e^(−t/τ)) erreicht den Messwert bei t_x/τ = 0,1321. Keine natürliche Uhr trifft.
  Bei endlichem q hängt t_x/τ von q ab.
- H225/k439: Potential der gemeinsamen Vakuumenergie in führender Ordnung V(φ) = −A cos 3(φ − π/8) + konst., A = 2|q| cos(π/8); Minimum π/8.
- k251 (`lambda_drehrate_2026_11_24/`): Λ hängt nur über die euklidische de-Sitter-Form Λ = 3Ω² an einer Drehrate. Die Skala bleibt frei, der Rahmen
  hat keine eigene Skala für Λ (k251, k353).
- H221: Der gemeinsame Versatz ist ein Winkel, keine Skala. In `rueckwaerts/` (k270–k274) geht es um Drift im HS(0)-Feld, das ist eine andere Frage.

## Was gesetzt ist (offen gelegt)

1. **φ ist ein dynamisches Feld** mit der Bewegungsgleichung φ̈ + 3Hφ̇ + V′(φ) = 0 und dem Potential aus H225. Die Masse am Minimum m² = V″(π/8) = 9A ist
   der einzige Feldparameter. Die Zerfallskonstante kürzt sich heraus.
2. **Start:** φ = 0, φ̇ = 0 tief in der Strahlungsära (a = 10⁻⁸). Das ist der Punkt ohne Drehung (H221) und der Start von H228. Ein Start auf dem Berggipfel
   (φ = π/8 − π/3) bräuchte eine freie kleine Auslenkung und wird nur erwähnt.
3. **Hintergrund:** flaches ΛCDM mit Ω_m = 0,315, Ω_r = 9,1·10⁻⁵, Ω_Λ = 1 − Ω_m − Ω_r (Planck-Werte aus dem Vorwissen). H₀ = 67,4 km/s/Mpc = 6,89·10⁻¹¹ pro Jahr.
   Die Rückwirkung von φ auf die Expansion wird vernachlässigt.
4. **Frei bleibt** μ = m/H₀. Der Rahmen legt keine Skala fest (k251). Vorab benannte „natürliche“ Werte: μ ∈ {√Ω_Λ (de-Sitter-Rate, k251), 1, 3/2, β_sym, γ_L,
   1/β_sym}.
5. **Drift heute:** Die Elektronmasse hängt über δ_Im = π/12 − φ am Feld (Brannen-Form, Skala μ_e fest). Ein heute rollendes φ ändert m_e/m_p mit
   d ln(m_e)/dt = (d ln m_e/dφ)·φ̇. Grenze aus Atomuhren: |d ln(m_p/m_e)/dt| ≲ 10⁻¹⁶ pro Jahr (Größenordnung aus dem Vorwissen, nicht nachgeschlagen;
   das Urteil hängt nur an Größenordnungen).

**Vorab erwartet (nicht gerechnet):** In einem Universum mit fallendem H bleibt φ eingefroren, solange H ≫ m ist, also beim Startwert 0. Danach rollt es zum
Minimum und schwingt dort mit abnehmender Amplitude. Ein dauerhaftes Einfrieren bei einem Zwischenwert ist nicht zu erwarten. Möglich ist nur, dass φ heute
gerade durch x läuft, und dann müsste die Drift heute groß sein.

## Teile und Kriterien

- **a:** φ(a = 1) und φ′ = dφ/d ln a heute als Funktion von μ ∈ [10⁻², 10³] (logarithmisch, fein). Alle μ*, für die φ heute = x gilt.
- **b:** Für jedes μ* die Drift d ln(m_e)/dt heute, verglichen mit 10⁻¹⁶ pro Jahr.
- **c:** φ(a = 1) für die sechs natürlichen μ-Werte aus Punkt 4.

**Urteil:**
- *trägt:* ein natürlicher μ-Wert (Punkt 4) gibt φ heute innerhalb 2σ von x **und** eine Drift unter der Grenze;
- *trägt teilweise:* nur ein angepasstes μ* gibt x (eine Zahl für eine Zahl), aber die Drift liegt unter der Grenze. Dann wäre die Drift eine Vorhersage;
- *widerlegt:* jedes μ* mit φ heute = x hat eine Drift über der Grenze, oder es gibt kein μ*.

## Werkzeuge

Python `k445_test_h231.py` (scipy solve_ivp in N = ln a, Ausgabe `k445_out.txt`); Wolfram `k445b_gegenprobe.wl` (NDSolve für einige μ, d ln m_e/dφ symbolisch,
Ausgabe `k445b_out.txt`). Qiskit ist nicht geeignet.

Vergeben: H231, k445.
