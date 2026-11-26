# Vorab-Notiz H166: Was legt die Phase der Nebendiagonale fest? Zielwert, notwendige Bedingungen und Übertragung durch die Maske

**Stand:** 26.11.2026, vor der Rechnung der Teile b bis d festgelegt. **Teilweise nicht blind:** Teil a ist schon überschlagen (Zahlen unten), b und c
stehen analytisch fest; nur Teil d ist blind. Anlass: Autor, 26.11.2026, 18:01 UTC: „dann machen wir das mal schritt für schritt“, Punkt 1 der offenen
Stränge („Was legt die Phase der Nebendiagonale in der Albert-Algebra fest?“, offen seit H158). Einordnung: `wiki/Gesamtbild.md`, Thesen zu Generationen
und Massen (T8/T13), OP3/OP4. Vergeben: H166, k359 (geprüft: beide im Repo frei).

## Vorwissen geprüft
- **H158** (PR #327, noch offen; `../generationszahl_h138/Ergebnis_H158_Albert_Zyklus_und_delta.md` auf dem Zweig von #327): P-invariantes Vakuum ist
  Zirkulante W = a + bS + b̄S², δ = arg b, tan δ = v/s (Spin 1 zu Spin 2); 720 einfache Koeffizientenverhältnisse ohne Treffer. Offen: was legt v/s fest.
- **H157, H155, H152, H149** (gleicher Ordner): Polynomiale Potentiale geben δ = 0, π/3, π/12 oder ein angepasstes Verhältnis.
- **v4.8.0-r11 (H1):** δ = K/3 bzw. 2/9 gilt nur für Lepton-Polmassen, nicht für Quarks oder laufende Massen.
- **`../../op3_phase_source_search_2026_11_12.md`, `../../op3_selection_principle_2026_11_13.md`, `../../op3_flux_two_thirds_2026_11_13.md`:**
  Φ = 3θ_e als Fluss durch das Platzdreieck; Scan nativer Zahlen (154 Versuche), ein Treffer ΔΦ = π/4 − 3θ_e = γ_M/2.
- **H102** (`../../predictions/Vorab_Notiz_H102_Tau_Masse_aus_gamma.md`): diese Beziehung verlangt m_τ = 1777,134 MeV (heute +2,3σ).
- **H101** (`../../predictions/Ergebnis_H101_Maske_hebt_Elektron.md`): Maske in Form K ist eine Kongruenz (Rang bleibt), Form S ändert das Spektrum nicht,
  die lineare r47-Form hebt den Rang, bricht aber K um 3·10⁻⁴. Dort nur am Oktanten (δ₀ = π/12) gerechnet, mit angepasstem ε.
- **H154:** Abweichung von K = ⅔ ist Messrauschen (0,43σ, aus m_τ); QED-Laufen an gemeinsamer Skala verschiebt K um 1,2·10⁻³.
- **`../../op3_spin1_triangle_2026_11_15/README.md`:** Spin-1-Dreieck mit Überlappung ½ hat Bargmann-Phase φ₁ = 3 arccos(1 − 1/√2) − π = 0,679042;
  bis 2/3 fehlen 0,012376, unerklärt.
- **`../../holonomie_restdrehung_2026_11_24/README.md`:** Lepton-Phase ist im Kreismodell keine Holonomie; γ_M müsste eingesetzt werden.
- Suche nach „Lindemann“, „transzendent“ in `notes/`, `wiki/`, `sources/research/parts/`: kein Vorbefund zur Transzendenz von tan(2/9).
- Zurückgestellte Ideen: I1 (String als Brücke, CT-002, ΔΦ = γ_M/2) berührt die Frage; Auslöser 4 war am 14.11. schon gezogen, kein neuer Auslöser.

**Suchrichtung (AGENTS, Rückwärtssuche):** Nach H149, H152, H155, H157, H158 mit derselben offenen Voraussetzung wird hier rückwärts gesucht:
erst das Ziel festlegen (a), dann notwendige Bedingungen (b, c), dann die eine noch nicht gerechnete native Abbildung mit festem Parameter prüfen (d).

**Werkzeugwahl:** Python (mpmath, sympy, numpy) für a bis d; Wolfram Language unabhängig für a (hohe Genauigkeit), b und c (symbolisch), d (Eigenwerte).
Qiskit nicht geeignet (keine Schaltung, keine Messsimulation).

## Aufbau (k359, `k359_test_h166.py`; Gegenprobe `k359b_gegenprobe.wl`)
Brannen-Form als Zirkulante C(ρ, δ) = 1 + zP + z̄Pᵀ, z = ρ e^{iδ}, Eigenwerte 1 + 2ρ cos(δ + 2πk/3), K = (1 + 2ρ²)/3.
Daten: m_e = 0,51099895000 MeV, m_μ = 105,6583755 MeV, m_μ/m_e = 206,7682827(46), m_τ = 1776,93 ± 0,09 MeV (wie H146, H154).
ε₀ = artanh β_sym mit β_sym = 0,5494056410 (Zählpostulat r67). Maske wie k223: W = diag(0, 0, −3), Form K: M = D C D mit D = exp(εW);
lineare Form r47: M = C + ε(WC + CW). Auslesung A: √m = Eigenwerte von M. Aus drei Eigenwerten folgen (K′, δ′) eindeutig (δ′ ∈ [0, π/3]).

## Hypothesen und Kriterien
- **H166a (Zielwert, nicht blind, schon überschlagen):** Allein aus m_μ/m_e gilt: (i) mit K = ⅔ exakt ist δ* = 0,2222220471, also 2/9 − 1,75·10⁻⁷;
  (ii) mit δ = 2/9 exakt ist K = ⅔ − 1,42·10⁻⁷; (iii) beide zugleich exakt geben m_μ/m_e = 206,770316 statt 206,768283 und sind auf Polmassen
  ausgeschlossen. Kriterium: Abstand von (iii) größer als 5σ der Messung von m_μ/m_e; Python und Wolfram stimmen auf 10⁻¹² überein. Zusätzlich
  werden die Vorhersagen für m_τ der Ziele K = ⅔, δ = 2/9, 3δ = K und H102 nebeneinandergestellt, und die relative Abweichung wird mit der Größe
  von Strahlungskorrekturen (α/π, (α/π)²) verglichen.
- **H166b (notwendige Bedingung, nicht blind, analytisch):** Ein isolierter stationärer Punkt eines Potentials, das polynomial in (a, s, v) ist und
  algebraische Koeffizienten hat, hat algebraisches tan δ. tan(2/9) ist transzendent (Lindemann–Weierstraß). Also gibt kein solches Potential δ = 2/9 exakt.
  Kriterium: Beweis in der Ergebnis-Notiz; Demonstration am J- und σ-erlaubten Potential aus H158 (Ordnung 4 und 6): die Stationaritätsbedingung
  ist ein Polynom in cos δ mit Koeffizienten im Körper des Verhältnisses β/α (symbolisch, Python und Wolfram).
- **H166c (Bedeutung der Phase, nicht blind, exakt):** (i) W = a + 2r cos(Θ + δ) mit Θ = (2π/3)·L_n, L_n = Spin-1-Erzeuger um die Zyklusachse
  n = (1,1,1)/√3, P = exp(iΘ); (ii) W = c₀ + D·L_n² + B·L_n mit tan δ = −√3 B/D, der δ-Anteil ist der unter der Konjugation σ ungerade Dipol;
  (iii) Φ = arg(w₁₂w₂₃w₃₁) = 3δ ist die einzige unter dem diagonalen Torus invariante Phase; (iv) tan δ = √3(√m_μ − √m_e)/(2√m_τ − √m_μ − √m_e).
  Kriterium: symbolische Nullreste.
- **H166d (blind): Die Maske mit festem ε₀ erzeugt das Lepton-Spektrum aus keinem nativen Winkel.**
  - *Vorwärts:* δ₀ ∈ N = {0, π/12, π/6, π/4, π/3, φ₁/3 = 0,2263473}, ρ² = ½, beide Formen (K, linear), ε = ±ε₀: 24 Kandidaten.
    Treffer, wenn |K′ − 0,666664| ≤ 10⁻⁴ und |δ′ − 0,222222| ≤ 10⁻⁴.
  - *Rückwärts:* Für jede Form und jedes Vorzeichen das unmaskierte Paar (K₀, δ₀) bestimmen, dessen maskiertes Spektrum die Lepton-Wurzeln gibt
    (m_τ = 1776,93 und ±0,09). Treffer, wenn |K₀ − ⅔| ≤ 10⁻⁴ und δ₀ (gefaltet auf [0, π/3]) näher als 10⁻⁴ an einem Element von N liegt.
  - **Vorhersage: kein Treffer**, vorwärts wie rückwärts. Zufallserwartung vorwärts 24 · (2·10⁻⁴/(π/3)) · (Anteil in K) < 0,005.
  - Kontrollen: ε = 0 gibt (K′, δ′) = (⅔, δ₀) auf 10⁻¹²; der Maskenplatz ändert das Spektrum nicht (Zyklus), δ₀ → −δ₀ und δ₀ → δ₀ + 2π/3 auch nicht
    (Schranke 10⁻¹²); Form S (Ähnlichkeit) lässt (K, δ) unverändert.

## Folge, vorab festgelegt
- a bestätigt: Das Ziel ist nicht „2/9 und ⅔“, sondern eine Kurve; unter dem Postulat J (K = ⅔ am Baumgraph) ist der Zielwert δ*. Ob 2/9 exakt gilt,
  ist auf Polmassen nur zusammen mit einer Theorie der Korrekturen entscheidbar. Kein Urteil über die Brannen-Form selbst.
- b bestätigt: Wege über polynomiale Potentiale mit algebraischen Koeffizienten können 2/9 nur annähern. Exakt 2/9 verlangt eine transzendente
  Eingabe (native Konstante im Koeffizientenverhältnis) oder einen Mechanismus, in dem der Winkel linear entsteht (Fluss, Holonomie).
- d ohne Treffer: Die Maske in den Formen K und linear ist nicht die Abbildung, die δ aus einem nativen Winkel erzeugt; in Form S ist δ in jedem
  Frame gleich. d mit Treffer: nur ein Kandidat, der eine eigene Vorab-Notiz mit Vorhersage (m_τ) braucht; kein Schluss ohne sie.
- In keinem Fall wird ein Vorzeichen gesetzt oder ein Guard berührt; OP3 und OP4 bleiben offen.
