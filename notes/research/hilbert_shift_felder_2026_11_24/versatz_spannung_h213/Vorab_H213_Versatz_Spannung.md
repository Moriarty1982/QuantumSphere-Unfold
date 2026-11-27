# Vorab-Notiz H213 (k426): Ist der „4,2σ-Abstand“ zwischen Neutrino-Versatz und Lepton-Versatz echt?

**Datum:** 2026-11-27 (vor der Rechnung committet). **Strang:** 3 (Lepton-Mischung/Massen), Fortsetzung nach H207/H208.
**Anlass:** Autor 27.11. (über den Koordinator): Strang wieder aktiv; nächster offener Punkt laut Stand ist der Abstand
zwischen dem Neutrino-Versatz x_ν = 0,043359 (aus R = Δm²₂₁/Δm²₃₁) und dem Lepton-Versatz x_lepton = 0,0395773 (aus m_e, m_μ, m_τ).
**Nummern:** H213, k426 (H212/k425 laut Koordinator bereits vergeben; gegen `main` geprüft).

## Frage
H207 nannte (x_ν − x_lepton)/σ_x = **4,2σ** mit σ_x = 0,00091. Ist das ein echter Abstand der beiden Sektor-Versätze, oder
(i) eine falsche Fehlerangabe, (ii) eine Frage des Massenschemas der geladenen Leptonen (Pol- gegen laufende Massen), oder
(iii) eine Frage der Fehlerfortpflanzung (nichtlinear, asymmetrisch)?

## Vorwissen geprüft
- `delta_h168/Ergebnis_H168_Skala_und_Sektoren.md`, `k363_test_h168.py`: H168d gibt aus den R-Daten **x_ν = 0,04336 ± 0,00213**
  gegen x = 0,03958, also **−1,78σ** (lineare Fehlerfortpflanzung aus σ(R), Daten NuFIT wie H99b: Δm²₂₁ = 7,537(97)·10⁻⁵,
  Δm²₃₁ = 2,511(21)·10⁻³ eV²).
- `mischung_h175/Ergebnis_H175_Term_aus_Ladungsrichtung.md`, `mischung_h176/Vorab_Notiz_H176_...`: σ = 0,00091 ist die
  **Anpassungs-Unsicherheit des gemeinsamen Vier-Größen-Fits** (R, θ₁₃, θ₁₂, θ₂₃) für x = 0,04478, nicht die Unsicherheit von x_ν aus R.
- `staerke_h168_h207/k417_test_h207.py` Zeile 75: `SX = 0.00091` wurde für den Vergleich x_ν gegen x_lepton übernommen.
- `mischung_h174/k370_test_h174.py`: X_LEP = 0,0395773407 aus Polmassen (m_τ = 1776,93 ± 0,09 MeV), X_R = 0,043359.
- Wiki Forschungsstand/Offene-Probleme (H207-Absätze) und Memory führen die 4,2σ als offene Stelle.

## Nicht blind (offen gesagt)
**Teil a ist nicht blind:** Aus H168 ist σ(x_ν) ≈ 0,00213 bekannt; der korrigierte Abstand ≈ 1,8σ ist absehbar. Er wird hier
nur sauber nachgerechnet und als Korrektur von H207 festgehalten (append-only: H207 bleibt stehen). **Teile b bis d sind blind.**

## Teile und Entscheidungskriterien
**a (nicht blind) — richtige Fehler.** σ(x_ν) aus σ(R) (linear), σ(x_lepton) aus den Fehlern von m_e, m_μ, m_τ.
Spannung T_a = |x_ν − x_lepton| / √(σ_ν² + σ_lep²).
Kriterium: T_a < 2 ⇒ „4,2σ war ein Fehler im Nenner; kein signifikanter Abstand“. T_a ≥ 3 ⇒ echter Abstand.

**b (blind) — nichtlineare Fehlerfortpflanzung.** Monte Carlo (10⁶ Ziehungen, Gauß in Δm²₂₁, Δm²₃₁) → Verteilung von x_ν,
Quantile 16/50/84 %, Anteil der Ziehungen mit x_ν ≤ x_lepton (einseitiger p-Wert, in σ umgerechnet).
Kriterium: weicht die MC-Spannung um mehr als 0,3σ von T_a ab, gilt die MC-Zahl.

**c (blind) — Massenschema der geladenen Leptonen.** x_lepton aus laufenden MS-bar-Massen bei μ = M_Z
(Literaturwerte Xing–Zhang–Zhou 2008: m_e = 0,486570 MeV, m_μ = 102,7181 MeV, m_τ = 1746,24 MeV) statt aus Polmassen.
Da K dort nicht exakt ⅔ ist, wird δ aus der allgemeinen Form √m_k = μ(1 + a cos(δ + 2πk/3)) bestimmt (drei Massen, drei
Größen μ, a, δ, eindeutig); x_lepton(M_Z) = π/12 − δ.
Kriterium: Verschiebung Δx_Schema. Liegt x_lepton(M_Z) innerhalb 1σ(x_ν) von x_ν ⇒ „Schema erklärt den Abstand“;
|Δx_Schema| < 0,3 σ(x_ν) ⇒ „Schema unerheblich“; dazwischen „teilweise“.
Hinweis: Welches Schema das richtige ist, legt der Rahmen nicht fest (Koide gilt empirisch für Polmassen); c prüft nur die Empfindlichkeit.

**d (blind) — Neutrino-Seite: Zweig und Ordnung.** Gibt es außer dem H168-Zweig (δ_ν zwischen π/12 und π/6, normale Ordnung)
einen weiteren Zweig der Brannen-Form mit K = ⅔, der R trifft (auch invertierte Ordnung, R_IO = Δm²₂₁/|Δm²₃₂|)? Wenn ja,
welchen Versatz verlangt er, und wie weit liegt er von x_lepton?
Kriterium: „kein weiterer Zweig“ oder Liste der Zweige mit Abstand in σ.

## Gesamturteil (vorab festgelegt)
- **trägt** (Abstand nicht echt): T (a bzw. b) < 2 und d liefert keinen näheren Konkurrenten, der die Lesart kippt.
- **trägt teilweise:** 2 ≤ T < 3, oder T < 2 nur mit einem bestimmten Schema aus c.
- **widerlegt** (Abstand echt): T ≥ 3 in a und b.

## Werkzeuge
Python (numpy/scipy) für a–d (`k426_test_h213.py` → `k426_out.txt`). Wolfram unabhängig (`k426b_gegenprobe.wl` → `k426b_out.txt`):
exakte Lösung für δ aus den drei Massen (Teil c, beide Schemata), x_ν aus R per FindRoot (Teil a). Qiskit nicht einschlägig.

## Grenzen
Alles unter H99 (Brannen-Form mit K = ⅔ für Neutrinos). Datenstand wie H168/H99b (NuFIT); keine neuen Messwerte eingeführt.
Kein Guard berührt; OP3/OP4 bleiben offen. H207 wird nicht umgeschrieben (append-only); die Korrektur steht hier.
