# Vorab-Notiz H227 (k441): Bilanz der Leptonenmassen — was eine Zahl φ und zwei Skalen festlegen, festgeschriebene Neutrino-Vorhersagen, Skalenverhältnis

**Datum:** 2026-11-28, vor der Rechnung committet. **Auftrag:** Marc 28.11., 11:21 („was ist wenn man erstmal nur nach den Leptonenmassen sucht?“),
Karte 11:23: „Massen-Bilanz H227“.
**Werkzeuge:** Python (`k441_test_h227.py` → `k441_out.txt`), Wolfram unabhängig (`k441b_gegenprobe.wl` → `k441b_out.txt`). Qiskit nicht einschlägig.

## Modell (gesetzt, aus dem bisherigen Stand)
√m_k = μ_s (1 + √2 cos(δ_s + 2πk/3)), k = 0, 1, 2; K = ⅔ unter J geschützt (a = √2). Geladen (Im-Sektor): δ = π/12 − φ. Neutrinos (Re-Sektor): δ = π/6 − φ,
Zweig nach H222 (normale Ordnung; die umgekehrte Ordnung ist dort mit dem verworfenen Zweig ausgeschlossen). φ gemeinsam (H221), Wert gemessen: φ = x = 0,0395773
(unter J aus m_τ, H158d). Σ√m = 3μ, Σm = 6μ². Massenskala je Sektor M_s = μ_s².
Daten wie im Repo (k426/k435): Polmassen m_e, m_μ, m_τ = 0,51099895 / 105,6583755 / 1776,93 ± 0,09 MeV; Δm²₂₁ = (7,537 ± 0,097)·10⁻⁵ eV², Δm²₃₁ = (2,511 ± 0,0205)·10⁻³ eV².
Mischung für m_β, m_ββ: sin²θ₁₂ = 0,307, sin²θ₁₃ = 0,0220 (Datenzentralwerte, nur für diese beiden Größen).

## Teile und Kriterien
**1 Bilanz (Zählung, kein Kriterium).** Sechs Massen, drei Eingaben (φ, μ_e, μ_ν) plus Setzungen (K = ⅔, Zweigvorzeichen). Ausgabe: welche Massen vorhergesagt werden
und mit welcher Genauigkeit: (i) die dritte geladene Masse aus zwei anderen (Koide; nicht blind, bekannt), (ii) R = Δm²₂₁/Δm²₃₁ aus φ (H213: 1,78σ; nicht blind),
(iii) die absolute Neutrinoskala nach Festlegung von μ_ν durch Δm²₃₁.
**2 Festgeschriebene Vorhersagen (teilweise nicht blind: Massen bei π/6 − x stehen in H168, 0,38 / 8,81 / 50,11 meV).** Mit μ_ν aus Δm²₃₁ (Hauptfall) und zur Kontrolle aus
Δm²₂₁: m₁, m₂, m₃, Σm, m_β = (Σ|U_ei|² m_i²)^½, Bereich von m_ββ über die freien Majorana-Phasen, dazu m_ββ mit der Brannen-Vorzeichenlage (negative leichteste Wurzel als
relatives Vorzeichen gelesen; Lesart, nicht hergeleitet). Fehler aus Δm²₃₁ und φ fortgepflanzt.
**Kriterium 2:** verträglich mit den aktuellen Schranken: KATRIN m_β < 0,45 eV (90 %), Kosmologie Σm < 0,0642 eV (DESI DR2 + CMB, 95 %, ΛCDM), KamLAND-Zen m_ββ < 0,028–0,122 eV.
**3 Skalenverhältnis ρ = M_ν/M_e (Erkundung, nicht blind: die Größenordnung ρ ~ 3·10⁻¹¹ habe ich vor dem Festschreiben überschlagen).** Vorab feste Liste:
(a) ganzzahlige Potenzen ρ = b^n für b ∈ {β_sym, γ_M, 1/γ_L, e^(−2ε)} (ε = artanh β_sym); Treffer, wenn |n − round(n)| < 0,05 (Zufallswahrscheinlichkeit je Basis 10 %);
(b) Seesaw-Lesarten M_X = M_e²/M_ν und v²/M_ν (v = 246,22 GeV) gegen {v, M_Pl = 1,221·10¹⁹ GeV, reduzierte M_Pl = 2,435·10¹⁸ GeV}; Treffer, wenn innerhalb Faktor 1,1.
**Urteil:** **trägt**, wenn 2 verträglich ist und 3 einen Treffer über der Zufallserwartung liefert; **trägt teilweise**, wenn 2 verträglich ist und 3 keinen Treffer liefert
(dann: Bilanz geschlossen, absolute Neutrinoskala als Vorhersage festgeschrieben, Skalenverhältnis frei); **widerlegt**, wenn 2 eine aktuelle Schranke verletzt.

## Vorwissen geprüft
H99 (Brannen-Form, negative Wurzel bei Neutrinos), H158d (x unter J aus m_τ), H168 (Neutrinomassen bei π/6 − x), H176 (Σm = 59,4 meV beim gefitteten x = 0,04478),
H213/H214 (x_ν verträglich 1,78σ; Polmassen sind das Schema), H222 (Zweig, IO aus), H155d (196 bekannte Skalen gegen eine Phasengröße, kein Treffer über Zufall).
Ein Skalenverhältnis μ_ν/μ_e wurde im Repo bisher nicht geprüft (Suche „mu_nu“, „Skalenverhältnis“, „seesaw“ in `notes/research/`: keine Fundstelle zu diesem Verhältnis).

## Grenzen (vorab)
Baumniveau, keine Laufeffekte (Polmassen-Schema nach H214); Neutrinomassen als Dirac-artige Wurzeln gelesen, Majorana-Phasen frei; die Vorzeichen-Lesart für m_ββ ist
nicht hergeleitet. Teil 3 ist eine Erkundung mit kleiner Liste; ein Treffer wäre ein Zahlenhinweis, keine Herleitung.
