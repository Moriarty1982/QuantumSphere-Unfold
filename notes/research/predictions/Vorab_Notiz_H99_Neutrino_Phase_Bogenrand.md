# Vorab-Notiz H99: Neutrino-Phase = Lepton-Phase + π/12 bei gleicher Überlappung

**Stand:** 13. November 2026, ca. 06:10, vor der Rechnung festgelegt. **Nicht blind** (Gründe unter „Offenlegung“). Anlass: Autorenentscheidungen vom 13.11. („dann versuchen wir es mit einer zusätzlichen Bedingung“; Wahl „Indefinites Skalarprodukt“).

## Vorwissen geprüft
- **H2** (v4.8.0-r12, Vorab 434c5a8, k15): K = 2/3 für Neutrinos nur mit negativer leichtester Wurzel; t und δ dort aus beiden Massendifferenzen bestimmt; normale Ordnung, Σm_ν = 0,0592 ± 0,0002 eV; verträglich, schwach trennend. Eine Beziehung der Neutrino-Phase zur Lepton-Phase wurde dort nicht geprüft (Suche nach π/12 mit Neutrino/Brannen in notes/, sources/, wiki/: kein Treffer).
- **v4.8.0-r10** (Phase der geladenen Leptonen: kein kanonischer Winkel, π/12 zweitnächster Kandidat für die Lepton-Phase selbst), **r11** (H1: δ = 2/9 widerlegt für Quarks und laufende Massen).
- **sec:v4110-koide-overlap** (Bogen [−π/12, π/12]) und `op3_gram_eigen_readout_2026_11_13.md` (Bogen als Positivitätsgrenze, K = (1 + 2ρ²)/3).
- `op3_indefinite_form_2026_11_13.md` (Commit fe872b7): bilineare Lorentz-invariante Form nur im neutralen Sektor; negativer Eigenwert genau außerhalb des Bogens.
- Literatur: C. Brannen, „Koide Mass Formula for Neutrinos“ (um 2006) setzt die Neutrino-Phase auf 2/9 + π/12. Aus Vorwissen; am 13.11. nur über eine Sekundärquelle (Physics-Forums-Thread „What is new with Koide sum rules?“) bestätigt, die Originalarbeit wurde nicht gelesen.
- Gesamtbild: T8 (Massen), T13; OP3. Zurückgestellte Ideen I1–I4: kein Auslöser.

## Aufbau
Triolen-Form für beide farbneutralen Sektoren mit derselben Überlappung ρ² = 1/2 (r = 1, K = 2/3):

    v_k = t (1 + √2 cos(θ + 2πk/3)),  m_k = v_k²,  k = 0, 1, 2.

- Geladene Leptonen: θ_e wird aus den Polmassen bestimmt, m_e = 0,51099895 MeV, m_μ = 105,6583755 MeV, m_τ = 1776,93 ± 0,09 MeV (dieselben Referenzwerte wie in sec:v4110-koide-overlap), über cos 3θ_e = 4 x_0 x_1 x_2 / A³ mit x_k = √m_k/Mittel − 1 und A² = (2/3) Σ x_k²; θ_e reduziert auf [0, π/3].
- Neutrinos: **θ_ν = θ_e + π/12**, r = 1 exakt, t_ν frei (fällt aus dem Verhältnis heraus). π/12 ist die halbe Breite des Bogens, an dessen Rand die Signatur der Gram-Matrix wechselt.
- Vorhergesagte Größe, normale Ordnung, Massen sortiert a < b < c:

      R = Δm²₂₁/Δm²₃₁ = (b² − a²)/(c² − a²).

- Skript `notes/research/predictions/k221_test_h99.py`, Ausgabe `k221_out.txt` (k220 ist auf einem lokalen Zweig des Autors vergeben).

## Daten (verbindlich)
- **(a)** NuFIT 6.0, Tabelle 1, Spalte „IC24 with SK atmospheric data“, dieselben Werte wie in H2: Δm²₂₁ = (7,49 ± 0,19)·10⁻⁵ eV², Δm²₃₁ = (2,513 +0,021/−0,019)·10⁻³ eV². Daraus R_obs = 0,029805 mit σ_R = 0,000792 (relative Fehler quadratisch addiert, asymmetrischer Fehler gemittelt).
- **(b)** NuFIT 6.1, dieselbe Spalte bzw. deren Nachfolger, normale Ordnung. Die Werte von Δm²₂₁ und Δm²₃₁ aus 6.1 sind mir beim Festschreiben nicht bekannt; sie werden erst nach dem Commit dieser Notiz nachgeschlagen. Ist 6.1 nicht auffindbar, entfällt (b) ohne Ersatz.

## Hypothesen und Kriterien
- **H99a:** |R_pred − R_obs| ≤ 2 σ_tot gegen (a), mit σ_tot² = σ_R² + σ_pred² und σ_pred aus der Unsicherheit von m_τ (numerische Ableitung). Sonst widerlegt.
- **H99b:** dasselbe Kriterium gegen (b).
- **Kontrolle 1:** die konstruierte Neutrino-Triole hat K = 2/3 auf 10⁻¹².
- **Kontrolle 2:** aus (Mittel, A, θ_e) werden die drei Lepton-Polmassen auf relativ 10⁻¹⁰ zurückgewonnen.
- **Kontrolle 3:** die leichteste Wurzel der Neutrino-Triole ist negativ (Signatur (2,1)); ist sie es nicht, ist der Test ungültig.

Nicht Teil des Kriteriums: die Variante θ_ν = θ_e − π/12, die invertierte Ordnung, absolute Massen. Werden sie gerechnet, heißen sie „nachträglich“.

## Offenlegung
- Vor dem Festschreiben habe ich überschlagen: Aus den H2-Massen (0,36; 8,66; 50,1 meV) folgt eine Neutrino-Phase von etwa 0,478, gegen θ_e + π/12 ≈ 0,484. Die Größenordnung der Übereinstimmung war mir also bekannt, der genaue Wert von R_pred nicht.
- Die Beziehung stammt aus der Literatur (Brannen), nicht aus dem Companion. Die Sekundärquelle sagt, es gebe wegen der ungenauen Neutrinodaten keine empirische Bestätigung.
- Nativ ist nur die Rolle von π/12 als Bogenrand (Signaturwechsel). Warum die Phase um genau die halbe Bogenbreite verschoben sein sollte, ist nicht hergeleitet. Die Annahme „Massenwurzel = Eigenwert“ ist ebenfalls nicht hergeleitet.
- θ_e wird aus Messwerten genommen; der Wert 2/9 wird nicht benutzt.

## Folge, vorab festgelegt
- **Bestätigt (a) und (b):** Die Bedingung „gleiche Überlappung, Phase um π/12 verschoben“ ist mit den Daten verträglich und verbindet beide Sektoren ohne freie Zahl außer der Skala. Wegen (a) nicht blind; als Vorhersage zählt dann nur der Vergleich mit künftigen, genaueren Werten von Δm²₂₁ (JUNO) nach eigener Vorab-Notiz. Keine Herleitung von K oder der Phase; OP3 bleibt offen.
- **Widerlegt:** Die Bedingung verbindet die Sektoren nicht. H2 und die Einordnung über die Signatur bleiben unberührt.
- In keinem Fall folgt etwas für Quarks, für die Lepton-Phase selbst oder für offene Guards.
