# Ergebnis H123: Die zeitliche Oktant-Auslese trennt die Orientierungen einer Punktierung nur für j ∉ 2ℕ; als Zählregel verfehlt sie die Daten

**23. November 2026. Vorab-Notiz `Vorab_Notiz_H123_Zeitliche_Oktantauslese.md` (Commit 1a4662ef). Skripte `h123_temporal_octant.wl`
(Ausgabe `h123_temporal_octant.txt`) und `k244_h123_qiskit_cycle_test.py` (Ausgabe `k244_out.txt`). Teilweise nicht blind. Status: H123a
bestätigt (exakt, nicht blind), H123b widerlegt (wie erwartet, nicht blind), H123c bestätigt (nicht blind), H123d trägt nicht.**

Werkzeuge: Wolfram Language (exakt) über den Wolfram-Kern dieser Sitzung (keine lokale Installation); Qiskit 2.6.2 als unabhängige Kontrolle der
Setzung S123 als Schaltung (Zyklustest). Kein HDL/MMA-Vergleich (kein RUN_TAPE, kein endlicher Auswahlablauf). Der erste Wolfram-Lauf war
ungültig: 0⁰ an den Polen in `coh[]` ergab „Indeterminate“; nach der Korrektur (`pw[x, 0] = 1`) lief das Skript mit unveränderten Kriterien.
Verbleibende Meldungen sind ein Linter-Hinweis des Kerns und ein Unterlauf bei Summanden unter 10⁻³⁰⁰ in der ersten Maschinenauswertung von
FindRoot (Wurzel mit 40 Stellen bestimmt); beides ändert kein Ergebnis.

## Kontrollen
| Kontrolle | Wert | Schranke | Ergebnis |
|---|---|---|---|
| Θ_j² = (−1)^{2j}, j ≤ 20 | 40 von 40 | exakt | erfüllt |
| R_j, T_j, J_{B,j} bilden extremale auf extremale Zustände ab | exakt j ≤ 4, numerisch j ≤ 20 | exakt / 10⁻¹² | erfüllt |
| Qiskit-Zustandsvektor gegen Formel, j = ½, 1, 2, alle 8 Tripel, beide τ | 6,6·10⁻¹⁶ | 10⁻¹² | erfüllt |
| Qiskit mit 10⁵ Schüssen | höchstens 0,70σ | 5σ | erfüllt |
| Regel (A, 2) ergibt γ_M (r17.3) | 0,2375329580 | 10⁻⁶ zu 0,237533 | erfüllt |
| Restglied jenseits j_max = 4000 | ~10⁻²⁵⁹³ | < 10⁻¹² | erfüllt |

## Ergebnis
| Teil | Messwert | Kriterium | Entscheidung |
|---|---|---|---|
| H123a | B_τ = 2^{−3j} e^{iτεjπ/2}, 640 Fälle Rest 0; umgekehrte Reihenfolge und Θ_j konjugieren je, zusammen bleibt B fest | alle Reste 0 | bestätigt (nicht blind) |
| H123b | gleicher Betrag für alle j; getrennt für j ∈ {½, 1, 3/2, 5/2, 3, …}, nicht getrennt für j ∈ {2, 4, …, 20} (dort B(+j) = B(−j) = (−1)^{j/2} 2^{−3j}) | alle j getrennt | widerlegt (wie erwartet) |
| H123c | Eigenwert e^{∓iπj} von R_j trennt genau die halbzahligen j | genau halbzahlige | bestätigt (nicht blind) |
| H123d | γ_M′ = 0,2341229, γ_L′ = 1,837930, β′ = 0,543379, m_W′ = 80,0994 GeV (−20,3σ), Ω_M′ = 0,2953 (−0,26σ) | alle drei Fenster | trägt nicht (β und m_W verfehlt) |

Nebenrechnung (kein Kriterium): ein Dreieck mit Phase φ = ⅔ je Spin ½ trennt alle j (π irrational); bei φ = π/4 − γ_M/2 = 0,666632 ist der
kleinste Abstand von 2jφ/π zu einer ganzen Zahl über j ≤ 20 gleich 0,00245, also ebenfalls Trennung für alle j ≤ 20.

## Warum es scheitert
Die Oktantphase eines Spin-j-Tripels ist j mal der Raumwinkel π/2. Die beiden Orientierungen geben e^{±ijπ/2}; diese fallen zusammen, sobald
jπ/2 ein Vielfaches von π ist, also für gerade j. Dort ist die Auslese reell und für beide Orientierungen gleich; nach r53.2 werden die beiden
Abbildungen zusammengelegt (Gewicht 1). Die Einfenster-Auslese über den Eigenwert von R_j trennt noch weniger, nur die halbzahligen j. Die Zählregel
mit Gewicht 1 auf j ∈ 2ℕ senkt γ_M um 1,4 %; γ_L fällt von 1,8647 auf 1,8379, und das m_W-Fenster (γ_L auf etwa ± 0,003) und das Leptonfenster
werden verfehlt. Ω_M bleibt im Fenster, weil es schwächer von γ_L abhängt.

## Lesart
- Die zeitliche Oktant-Auslese unterscheidet die Orientierung einer Punktierung, ohne eine auszuwählen (gleiche Beträge, konjugierte Werte), aber
  nur für j ∉ 2ℕ. Sie liefert U2 nicht, und als Zählregel ist sie mit den drei Fenstern von H98 unverträglich. Die beiden Hälften von Q1a sind in
  dieser Form nicht derselbe Datensatz: Das Oktantvorzeichen (Spin ½) liest die Auslese, die Zählung aller j mit Gewicht 2 nicht.
- Das Oktantvorzeichen ist unter der Setzung S123 eine Relation τε zwischen Feldbahn und Zeitrichtung der Auslese und zeitumkehrgerade (r31.2,
  jetzt für alle j geprüft). Die Herkunft von τ ist weiter nicht hergeleitet.
- Grenze für die nächste Runde: Eine phasenempfindliche Dreiecksauslese, die U2 liefert, braucht einen Raumwinkel Ω mit jΩ ∉ πℤ für alle j.
  Nachträglich (Nebenrechnung, kein Test): Das gebogene Dreieck der Restbiegung (φ = π/4 − γ_M/2 ≈ ⅔) erfüllt das für j ≤ 20, ist aber selbst aus
  γ_M gebaut; eine Auslese, die U2 aus der Biegung bezieht, wäre zirkulär, solange die Biegung nicht unabhängig hergeleitet ist. Eine Prüfung
  bräuchte eine eigene Vorab-Notiz.
- Zurückgestellte Ideen: H123d berührt β_sym als Verhältnis zweier Zählungen; damit trifft Auslöser 3 von I1 zu. I1 („T zählt
  Endpunkte offener Strings“, r40.5: zwei Enden mit eigener Zeitorientierung) ist als möglicher Ausweg dem Autor vorzulegen, nicht still umzusetzen.
- Kein Vergleich mit Leptondaten über die Fenster von H98 hinaus. OP1, OP3 und Q1a bleiben offen; kein Guard berührt.
