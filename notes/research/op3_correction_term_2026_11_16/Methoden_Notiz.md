# Methoden-Notiz: Rückwärts rekonstruierter, zeitabhängiger Korrekturterm (OP3)

Festgelegt am 2026-11-16, **vor** jeder Rechnung. Idee des Autors: „einen Korrekturterm einfügen, der von der zeitlichen Entwicklung abhängt und
die Werte erst einmal in die richtige Richtung biegt (mit etwas Spielraum); dann untersuchen, wie sich dieser Term in jedem Schritt ändern müsste,
und daraus etwas über die Dynamik lernen.“ Status: **Erkundung, nicht blind** (Ziel bekannt). Keine H-Nummer; eine H-Nummer wird erst für einen
Übertragungstest vergeben (Abschnitt 7). Skript (wird nach dem Commit dieser Notiz geschrieben): `correction_term.py`.

## 1. Vorwissen geprüft
- **Statische Korrekturterme im Bestand:** Gegenterm-Register CT-001–CT-004 (`../counterterms/`); bewachter Kern und H102 (φ = π/4 − γ_M/2,
  `../op3_guarded_core_flux_2026_11_15/`); Zwirbel-Wahrscheinlichkeit p = 0,0308 mit n·σ (`../op3_native_kappa_2026_11_16/`).
- **Zeitstruktur:** r16.8 (Invariantenmatrix S, Zeitverschiebung wirkt auf (s₊, w, s̄₋) mit Gewichten −1, 0, +1), r16.9 (Drittel der Periode als
  Generationszyklus U = diag(ω̄, 1, ω); |⟨ψ|Uψ⟩|² = ½(3Σp² − 1); Zielgewichte 0,793146 / 0,193404 / 0,013450), r17.1 (Koide als Kohärenzfunktional
  der Photon-Uhr-Sonde), `../op3_time_cycle_2026_11_15/`.
- **Bisherige Wege:** H106–H110, Renormierung, Frame- und Betrachter-Lesarten (`../op3_chain_diagnosis_2026_11_16/` mit Nachtrag): Die zweite
  Zahl δ ist eine Eigenschaft des Feldzustands bzw. der Verbindung; im Bestand fehlt ein Auswahlgesetz (Dynamik).
- **Rückrechnungen:** `../op3_mass_backsolve_2026_11_12/` (notwendige Schranken aus gemessenen Massen, keine Operatorrekonstruktion).
- **Steuerung in QAM:** `../qam_hc_flaechenquantum_2026_11_07.md` (Pulsfolgen auf Transferblöcken, Z. 935 ff.), ohne Bezug zu OP3.
- Eine zeitabhängige Rekonstruktion des Korrekturterms für OP3 gibt es im Bestand nicht.

## 2. Vorab festgehaltene Vereinfachung (analytisch, nicht blind)
Für einen Zustand ρ auf ℂ³ = span(s₊, w, s̄₋) mit Populationen p = (p₊, p₀, p₋) und dem Zyklus U = diag(ω̄, 1, ω) gilt Tr(ρU) = Σ p_k u_k. Damit
hängen φ = 3 arg Tr(ρU) und K = Σ p_k² (r16.9(b), Frame-Operator-Lesart) **nur von den Populationen ab**, für reine wie für gemischte Zustände.
Der Korrekturterm muss also die Populationen von einem Start- zu einem Zielpunkt im Simplex führen. Kohärenzen wirken nur mittelbar (unitär lassen
sich Populationen nur über Kohärenzen verschieben).

## 3. System
- Basis (s₊, w, s̄₋), ω = 1. Freie Entwicklung $H_0=2\,\mathrm{diag}(-1,0,+1)$ (Zeitverschiebung nach r16.8).
- Zeitfenster τ = π (eine Periode von s(t)).
- **Startzustände:** S1 = kohärenter Spin-1-Zustand auf dem Kegel θ₀ = 38,6763° (Spin-1-Dreieck, φ = 0,679042); S2 = Rand des Koide-Kreises
  δ = π/12 (p₋ = 0, flacher Oktant, φ = π/4), reelle nichtnegative Amplituden.
- **Ziel:** Populationen aus δ mit 3δ = 0,666674 (Polmassen mit PDG 2024 = PDG 2026) auf dem Kreis K = 2/3. **Spielraum:** |K − 2/3| ≤ 1·10⁻⁴,
  |φ − 0,666674| ≤ 2·10⁻⁴.

## 4. Korrekturterm (feste Generatormenge)
Unitär: $H(t)=H_0+\sum_k u_k(t)G_k$ mit
- Dipol (Δm = ±1): D1 = J_x, D2 = J_y;
- Quadrupol (Δm = ±2): Q1 = (J₊² + J₋²)/2, Q2 = (J₊² − J₋²)/(2i);
- J_z und J_z² sind ausgeschlossen (sie ändern p nicht) und laufen nur als Kontrolle mit.

Dissipativ (getrennter Lauf): Lindblad-Sprünge J₋, J₊, J₋², J₊² mit Raten γ_k(t) ≥ 0, ohne Steuerfelder.

## 5. Auswahlprinzip und Lösung
- Hauptlauf: minimaler Eingriff $A=\int_0^\tau\sum_k u_k^2\,dt$ (unitär) bzw. $\int_0^\tau\sum_k\gamma_k\,dt$ (dissipativ), unter der Zielbedingung.
- Diskretisierung: 200 stückweise konstante Schritte; Gradientenverfahren (GRAPE-artig) mit 20 Zufallsstarts; berichtet wird die beste Lösung und
  die Streuung über die Starts.
- **Robustheitsvarianten (fest):** V1 glattester Verlauf ($\int|u'|^2$ plus 10⁻³ $\int|u|^2$); V2 τ = π/3 (ein Generationsschritt) und τ = 3π;
  V3 beide Startzustände S1, S2.

## 6. Ausgewertete Formmerkmale und was als Befund zählt
- **M1 Richtung:** Anteil des Eingriffs auf Dipol- gegen Quadrupol-Generatoren.
- **M2 Charakter:** minimaler unitärer gegen minimalen dissipativen Eingriff; welcher ist billiger, und braucht das Ziel überhaupt Dissipation?
- **M3 Zeitverlauf:** Verlauf und Spektrum der u_k(t) im Wechselwirkungsbild (H₀ herausgerechnet).
- **M4 Integral:** Pulsfläche $\int|u|\,dt$ im Wechselwirkungsbild und Fubini–Study-Abstand zwischen Start und Ziel; Vergleich nur mit dieser
  vorab festgelegten Liste: γ_M/2 = 0,118767, γ_M = 0,237533, π/4 − 0,666674 = 0,118724, γ_T/2 = 0,063692, 1/(4π) = 0,079577.

**Erwartete Artefakte (zählen nicht als Befund):** Resonanz mit den Aufspaltungen von H₀ (2 und 4) im Laborbild; die Form einer
Fubini–Study-Geodäte beim minimalen Eingriff; die Wirkungslosigkeit von J_z, J_z².

**Befund** ist nur ein Merkmal, das (a) über V1–V3 und beide Startzustände qualitativ gleich bleibt und (b) kein erwartetes Artefakt ist. Ein
Zusammentreffen in M4 zählt nur bei relativer Abweichung ≤ 10⁻³; Zufallserwartung bei fünf Konstanten und zwei Messgrößen je Lauf grob 0,02 je
Lauf, über alle Läufe aufaddiert anzugeben. Für S2 ist der Vergleich mit γ_M/2 und π/4 − φ halb zirkulär (H102 sitzt schon in der Zielverschiebung)
und wird so gekennzeichnet.

## 7. Übertragungstest (erst nach einem Befund, mit eigener H-Nummer)
Ein Befund wird erst dann ein Ergebnis, wenn derselbe rekonstruierte Term etwas vorhersagt, das nicht hineingesteckt wurde. Zulässige Kandidaten,
jeweils vor der Rechnung mit H-Nummer festzulegen: (i) Neutrinosektor (Startpunkt und Ziel nach H99), (ii) Laufen der Phase bis M_Z (Vergleich mit
der Renormierungs-Erkundung), (iii) ein Quarksektor, falls eine Koide-artige Zielgröße vorab definiert wird.

## 8. Offenlegung
- Das Ziel ist bekannt; die Rekonstruktion selbst ist kein Beleg, nur eine Beschreibung des nötigen Eingriffs.
- Die Generatormenge ist eine Setzung: Auf S wirken nativ nur die Zeitverschiebung (diagonal) und antilineare Frame-Abbildungen (r16.8);
  jeder populationsändernde Term ist deshalb nicht nativ. Genau das ist der Zweck: Er zeigt, was der Bestand nicht liefert.
- Änderungen an dieser Notiz nach dem Commit nur als Nachtrag.
