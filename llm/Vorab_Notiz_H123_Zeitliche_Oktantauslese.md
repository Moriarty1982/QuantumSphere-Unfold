# Vorab-Notiz H123: Unterscheidet eine zeitlich geordnete Oktant-Auslese die Orientierungen, ohne eine zu wählen (Q1a)?

**Stand:** 23. November 2026, vor der Rechnung festgelegt. **Teilweise nicht blind** (Gründe je Teil unten): H123a ist die Identität aus
r31.2, auf Spin j gehoben; H123b und H123c folgen aus bekannten Formeln (Phase des Spin-kohärenten Dreiecks = j · Raumwinkel; Eigenwerte von
exp(−iπJ_k)) und sind per Kopfrechnung absehbar; für H123d liegt eine Kopfschätzung vor. Neu ist die exakte Prüfung, die Verbindung beider Hälften
von Q1a an einer Stelle und der Datenabgleich der daraus folgenden Zählregel. Anlass: Übergabe vom 23.11. („H123 für Q1a Orientierung
vorgemerkt“), r55.6 („größter Hebel nach r54 ist Q1a; H118 lässt die Variante mit zeitlicher Umlaufreihenfolge ungeprüft“); der Autor hat den Faden
„Auslesegesetz Q1a als H123 testen“ am 23.11.2026 gestartet.

## Worum es geht
Q1a (r55.2) hat zwei Hälften: das Vorzeichen des Oktantschritts (r31.1, H118: eine Zeitorientierung der Auslese, vom Bestand nicht festgelegt)
und die Zählung von OP1, deren Gewicht 2 eine Auslese verlangt, die die beiden Orientierungen |j,+j⟩ und |j,−j⟩ einer Punktierung
**unterscheidet, ohne eine auszuwählen** (r53.2, r53.4). r31.2 hält fest: Ist die Umlaufreihenfolge selbst zeitlich, kippt die Zeitumkehr τ und ε
zugleich, und die Phase ist zeitumkehrgerade; das ist eine Identität, kein Test. Der Test hier fragt daher nicht, ob die Phase gerade wird,
sondern was eine solche zeitlich geordnete Auslese **auf einer Punktierung vom Spin j** leistet: Unterscheidet sie m = +j von m = −j bei
gleichem Gewicht für jedes j (dann wäre sie ein Kandidat für U2 aus derselben Quelle wie das Oktantvorzeichen), und wenn nicht, ist die
Zählregel, die sie liefert, mit den Daten verträglich?

## Vorwissen geprüft
- r16.7 (`sources/research/parts/v4100-post-release-layers.tex`): acht Oktant-Tripel auf χ, zwei Bahnen, Vorzeichen offen.
- r17.3 (ebenda): Annahme (A), die Frame-Abbildungen wirken auf eine Punktierung vom Spin j als exp(−iπJ_k) um drei orthogonale Achsen; das
  extremale Dublett |j,±j⟩ ist invariant; für halbzahlige j antikommutieren die Abbildungen, für ganzzahlige kommutieren sie (Charaktere);
  Regel „M zählt das extremale Dublett je j, Gewicht 2“ gibt γ_M = 0,237533.
- r31.1 / H118 (`llm/Vorab_Notiz_H118_…`, `llm/Ergebnis_H118_…`, Commit 371f14d7): Bargmann-Phase τ · ε · π/4; Zeitumkehr der Feldamplituden
  wirkt auf χ als K und kehrt ε um; kein Kandidat in Klasse U.
- r31.2: zeitliche Umlaufreihenfolge macht die Phase gerade (Identität); die Feld-Dynamik liefert keine zeitliche Ordnung der drei Auslesen;
  sie müsste aus dem Ausleseprotokoll kommen (zwei Fenster, H117). OP3 ruht auf Autorentscheidung vom 22.11.
- H116, H117 (`llm/Ergebnis_H116_…`, `llm/Ergebnis_H117_…`): Beträge und Endpunkte legen das Vorzeichen nicht fest; zwei Fenster verlegen die Wahl
  ins zweite Fenster.
- r40.4/r40.5: gleiche Gewichtung p = ½ ⇔ Austausch gerade unter relativer Zeitumkehr (dieselbe komplexe Konjugation wie in r31.1); benannt,
  nicht hergeleitet; Bezug zu I1 (zwei Enden mit eigener Zeitorientierung).
- r53.1–r53.4 (`notes/research/openai_148_149_fulltext_2026_11_23/`): Zusammenlegen oder Auswählen der beiden Orientierungen gibt
  Σ_j r_j^γ = 1, γ₁ = 0,161586; Gewicht 2 verlangt zwei verschiedene Abbildungen.
- r54 / H122: Q1b (Rahmen, Achse) beantwortet; beide Auslesen dort zeitorientierungsblind (r48.2).
- r55.2, r55.6 und `notes/research/op_cross_map_2026_11_23/README.md`: Q1a offen, größter Hebel.
- H98 (`notes/research/predictions/Vorab_Notiz_H98_…`, `Ergebnis_H98_…`): Regelraum S (Bereiche A, H, I, S½, S1; Gewichte 2, 2j+1) und die drei
  Datenfenster; das Paar (A, 2)/(S½) trifft alle drei (γ_L = 1,864700, β = 0,54941, m_W = 80,3615 GeV, Ω_M = 0,3018). Die hier entstehende Regel
  (Gewicht 2 außer auf j ∈ 2ℕ) liegt **nicht** in S.
- Suche nach „Kirkwood“, „schwache Messung“, „weak measurement“ in `llm/`, `notes/research/`, `analysis/`: keine Fundstelle; „Bargmann“ nur
  in H114–H118 und den Vorhersagen H106–H109 (Spin ½, keine Punktierung vom Spin j).
- Gesamtbild (`wiki/Gesamtbild.md`): berührt T6 (Zählregel je Frame, OP1) und T8/OP3 (Oktant). Zurückgestellte Ideen I1–I6: kein Auslöser
  getroffen; I1 wird im Ergebnis genannt, falls die Auslese scheitert (r40.5 verbindet zwei Zeitorientierungen mit I1).
- Rückwärtssuche (AGENTS.md, „Suchrichtung prüfen“): Ziel U2 = Gewicht 2 für jedes j. Notwendig: der Auslesewert für m = +j und m = −j ist
  verschieden bei gleichem Betrag. Ein Dreieck mit Raumwinkel Ω gibt e^{±ijΩ}; das trennt genau dann, wenn jΩ ∉ πℤ. Für das Oktant
  (Ω = π/2) scheitert das bei j ∈ {2, 4, 6, …}. Diese Erwartung macht H123b nicht blind.

## Aufbau
- Punktierung vom Spin j ∈ {½, 1, …, 20}, Frame-Abbildungen R_j = exp(−iπJ_z), T_j = exp(−iπJ_x), J_{B,j} = exp(−iπJ_y) (Annahme (A) aus r17.3).
- Oktant-Tripel vom Spin j: |a⟩ = |j, s_z j⟩_z, |b⟩ = |j, s_x j⟩_x, |c⟩ = |j, s_y j⟩_y, acht Vorzeichenwahlen, ε = s_x s_y s_z.
- **Setzung S123 (zeitlich geordnete Auslese):** drei Fenster in der Reihenfolge R → T → J_B (τ = +1) oder umgekehrt (τ = −1); der Auslesewert ist
  die Bargmann-Invariante B_τ = ⟨a|b⟩⟨b|c⟩⟨c|a⟩ (τ = +1) bzw. ihr Gegenstück in umgekehrter Reihenfolge, operativ der Imaginärteil der
  Kirkwood-Dirac-Quasiwahrscheinlichkeit Tr(P_c P_b P_a) eines Ablaufs aus drei Fenstern. Zeitumkehr des Protokolls = Reihenfolge umkehren und
  die antiunitäre Θ_j = exp(−iπJ_y) K auf die Zustände anwenden. Woher τ kommt, wird nicht hergeleitet (r31.2).
- **Orientierung einer Punktierung:** m ↦ −m, also s_z ↦ −s_z bei festen s_x, s_y (r53.4).
- **Einfenster-Vergleich:** Eigenwert von R_j auf |j, ±j⟩_z.
- **Zählregel M₁₂₃:** Σ_j g_j e^{−2πγ√(j(j+1))} = 1 mit g_j = 2, wenn die zeitliche Auslese ±j unterscheidet, sonst g_j = 1 (zusammengelegt wie in
  r53.2); T unverändert j = ½ mit g = 2, sofern j = ½ unterschieden wird. Summen bis j_max = 4000, Restglied < 10⁻¹². Daten wie H98:
  β = √((γ_L − 1)/(γ_L + 1)) ∈ [0,545; 0,570]; m_W = m_Z γ_L/√(1 + γ_L²), m_Z = 91,1880 GeV, gegen PDG 2025 80,3692 ± 0,0133 GeV (2σ);
  Ω_M = β² gegen DESI DR2 0,2975 ± 0,0086 (2σ).
- **Werkzeuge:** Wolfram Language (exakt, symbolisch) für H123a–d, Skript `llm/h123_temporal_octant.wl`, Ausgabe `llm/h123_temporal_octant.txt`.
  Qiskit als unabhängige Kontrolle der Setzung S123 als Schaltung: Zyklustest (Hilfsqubit, Hadamard-Test mit kontrollierter zyklischer
  Vertauschung dreier Register, Re und Im getrennt) für j = ½ (1 Qubit je Register), j = 1 (2 Qubits, symmetrischer Teilraum) und j = 2 (4 Qubits),
  Skript `llm/k242_h123_qiskit_cycle_test.py`, Ausgabe `llm/k242_out.txt`. Kein HDL/MMA-Vergleich: kein RUN_TAPE, keine Guard- oder
  Auswahlfolge; die Entscheidung hängt an exakten Phasen und an einer Wurzel einer Reihe.

## Hypothesen und Kriterien
- **H123a (exakt, nicht blind; r31.2 auf Spin j gehoben):** Für alle j ∈ {½, …, 20}, alle acht Tripel und beide τ gilt
  B_τ = 2^{−3j} e^{iτεjπ/2}; umgekehrte Reihenfolge konjugiert, Θ_j konjugiert, beides zusammen lässt B unverändert. Kriterium: alle Reste exakt 0.
- **H123b (Entscheidung, nicht blind):** Die zeitliche Oktant-Auslese unterscheidet |j,+j⟩ von |j,−j⟩ bei gleichem Betrag für **jedes** j ≤ 20.
  Bestätigt, wenn für alle j |B(+j)| = |B(−j)| und B(+j) ≠ B(−j) exakt gilt; widerlegt, wenn ein j scheitert. Berichtet wird die Menge D₁₂₃ der
  unterschiedenen j. Erwartung: widerlegt genau auf j ∈ {2, 4, …, 20}.
- **H123c (Vergleich, nicht blind):** Der Eigenwert von R_j unterscheidet ±j genau für halbzahlige j. Kriterium exakt für j ≤ 20. Damit steht die
  Einfenster-Auslese (Bereich H in S) neben der zeitlichen (D₁₂₃).
- **H123d (Daten, Ausgang per Kopfschätzung erwartet):** Das Paar M₁₂₃ / T trifft alle drei Fenster von H98. Trägt, wenn alle drei getroffen werden;
  trägt nicht, wenn eines verfehlt wird. Kopfschätzung vor der Rechnung: γ_M′ ≈ 0,234, γ_L′ ≈ 1,84, m_W-Fenster (γ_L auf etwa ± 0,003) verfehlt.
  Berichtet werden γ_M′, γ_L′, β′, m_W′, Ω_M′ und die Lage gegen jedes Fenster. γ_M′ ist kein Zielwert; Nähe zu Korpuswerten zählt nicht.
- **Kontrollen:** Θ_j² = (−1)^{2j}; R_j, T_j, J_{B,j} bilden extremale Zustände auf extremale Zustände ab; Qiskit-Zustandsvektor gegen die exakte Formel,
  Abweichung ≤ 10⁻¹² für j = ½, 1, 2 und beide Reihenfolgen; Qiskit mit 10⁵ Schüssen je Messung innerhalb 5σ; die Regel (A, 2) dieses Skripts gibt
  γ_M = 0,237533 (r17.3) auf 10⁻⁶.
- **Nebenrechnung, kein Kriterium:** für ein gebogenes Dreieck mit Phase φ je Spin ½ (Restbiegung, r16.7) wird nur berichtet, für welche j ≤ 20 es
  trennt.

## Folge, vorab festgelegt
- **H123b bestätigt:** Die zeitliche Oktant-Auslese wäre ein Kandidat, der beide Hälften von Q1a aus einer Quelle bedient (Oktantvorzeichen als
  Relation τε, Gewicht 2 von M). U2 wäre damit als Ausleseregel formuliert, nicht hergeleitet; τ bliebe gesetzt.
- **H123b widerlegt:** Das Oktant liefert U2 nicht; die beiden Hälften von Q1a sind dann nicht derselbe Datensatz in dieser Form. H123d entscheidet,
  ob die abweichende Regel M₁₂₃ wenigstens mit den Daten verträglich ist. Trägt H123d nicht, ist die zeitliche Oktant-Auslese als Zählregel
  ausgeschlossen, und eine U2 liefernde Auslese bräuchte einen Raumwinkel Ω mit jΩ ∉ πℤ für alle j (Grenze für die nächste Runde).
- In jedem Fall: Die Auslese unterscheidet ε, sie wählt keine Bahn; das Vorzeichen des Oktantschritts bleibt als Relation zwischen Feld und
  Zeitrichtung der Auslese offen, die Herkunft von τ bleibt offen (r31.2). OP1, OP3 und Q1a bleiben offen; keine Leptondaten; kein Guard berührt.
  Das Ergebnis kommt als Runde v4.10.0-r56 in den Companion.

Nach dem Commit dieser Notiz wird an Kriterien und Schranken nichts mehr geändert; Änderungen nur als datierter Nachtrag vor einem weiteren Lauf.

## Nachtrag 23.11.2026 (nach der Rechnung, nur Nummern)
Runde v4.10.0-r56 und k242 waren parallel im OP5-Faden vergeben worden (PR #271). Die Runde dieses Tests heißt deshalb **v4.10.0-r57**, das
Qiskit-Skript `llm/k243_h123_qiskit_cycle_test.py` mit Ausgabe `llm/k243_out.txt` (gelaufen unter dem Namen k242, Inhalt unverändert). Kriterien,
Schranken und Rechnungen sind davon nicht berührt.

