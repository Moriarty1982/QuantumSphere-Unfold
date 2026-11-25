# Vorab-Notiz H134: Bringt die Frame-Korrektur (Maske mit ε = Rapidität des Materie-Frames) die TM1-Klasse aus k262 auf den JUNO-Wert von θ₁₂?

**Stand:** 2026-11-25, vor der Rechnung festgelegt. **Teilweise nicht blind:** Die Daten sind bekannt (JUNO 2026), und die analytisch feststehenden Teile stehen unter
„Vorab offengelegt“. Das Ergebnis der Rechnung selbst ist mir nicht bekannt. Anlass: Autor, 25.11.2026, 11:10 und 11:11 UTC, zum Befund „TM1/H8 nach JUNO disfavorisiert“:
„naja, benutzt juno die idee mit den frames?“ und „naja, wir sitzen doch in dem verschobenen frame oder nicht“; Freigabe „weiter bitte“ (11:12 UTC).
Skripte ab **k263** (Python numpy/scipy; Wolfram Language zur Kontrolle der Stelle ε = 0 und eines Trefferpunkts). Qiskit nicht vorgesehen (keine Schaltung).
Bezug OP3/OP4, Thesen T6 (β_sym), T8 (Mischung). Konvention F: gemessen wird im Materie-Frame M.

## Vorwissen geprüft
- **JUNO misst ohne Frame-Annahme:** sin²θ₁₂ wird aus der Überlebenswahrscheinlichkeit von Reaktor-Antineutrinos im Labor bestimmt. Eine Frame-Umrechnung steckt nicht darin.
  Der Einwand des Autors betrifft die andere Seite: die algebraische Vorhersage (k262, H131) wurde ohne erklärte Abbildung mit einer Messung im Materie-Frame verglichen
  (Regel „Frames“ in AGENTS.md).
- **Die erklärte Abbildung für die Mischung gibt es im Repo schon:** r47 (Maske W_l = diag(0, 0, −3)), r57/H41 (Maske als Korrektur: geladene Leptonen in Form S,
  M_e = D C_e D⁻¹; Majorana-Neutrinos in Form K, M_ν = D M₀ D; D = exp(ε W_l)), r60/H45 (ε = Rapidität des Materie-Frames, ε = η = artanh β_sym = 0,6174;
  mit der TM2-Lesart 120 bzw. 1104 Treffer, sin²θ₂₃ ∈ [0,4913; 0,4975], δ frei; nicht blind), H46 (offene Vorhersage daraus), H44 (ε aus Strukturwerten).
- **k262** (#304): Majorana-Neutrinos auf dem Realteil s, ℤ₃ und eine ungerade ℤ₂ aus der Gruppe von k260: TM1 mit θ₂₃ = 45°, |sin δ| = 1 (sin²θ₁₂ = 0,3183) oder θ₁₃ = 0.
- **H4, H8, Nachprüfung JUNO 2026** (`v4_8_0_r03_r12/llm/Nachpruefung_JUNO_2026.md`): JUNO 2026 sin²θ₁₂ = 0,3036 ± 0,0064 (arXiv:2609.37895); TM1 liegt 2,3σ darüber.
- **H9** (|U_e2|² = β_sym², offen), **H112**: andere Lesart derselben Zahl; hier nicht benutzt.
- **k297** (#303): HC mit μ = β_sym², Tausch μ → 1/μ als Frame-Wahl. Der Schatten z ↦ z + μ z̄ wird unten unter „Vorab offengelegt“ behandelt.
- Im Repo ist die Maskenkorrektur bisher **nur** auf die TM2-Lesart angewandt (Suche nach „TM1“ zusammen mit „Maske“, 25.11.). Die TM1-Klasse mit ε = η ist nicht gerechnet.

## Aufbau (Regel unverändert aus H41/H45 übernommen, keine neue Einstellung)
- Platzbasis wie k262. Geladene Leptonen: zirkulantes C_e = F diag(λ) F†, M_e = D C_e D⁻¹, D = exp(ε W_l), W_l = diag(0, 0, −3); λ exakt an die Massen angepasst,
  alle Zweige wie in k100 (`charged`), U_e aus den linken Singulärvektoren.
- Neutrinos (Lesart B aus k262): M₀ = Q_φ diag(μ) Q_φᵀ reell, invariant unter der ungeraden ℤ₂ = ⟨A⟩. A ist eine vorzeichenbehaftete Vertauschung der Plätze q, r bei
  festem Platz p; ihr einfacher Eigenvektor w = (e_q ± e_r)/√2 ist die erste Spalte von Q_φ, die beiden anderen entstehen durch Drehung um φ in der Ebene senkrecht zu w.
  **Alle sechs A** (p = 0, 1, 2; beide Vorzeichen), φ auf 0°, 2°, …, 178°, alle Zuordnungen der Spalten zu ν₁, ν₂, ν₃.
- **Variante A:** ε_ν = 0, ε_e = η. **Variante B:** ε_ν = ε_e = η, M_ν = D M₀ D, |μ| an die Massen angepasst (m₁ ∈ {0; 0,001; 0,003} eV, Δm² wie k100), alle Vorzeichen.
- **ε ist fest:** η = artanh(0,5493) = 0,6174. Zum Vergleich wird ε = 0 mitgerechnet (Kontrolle) und der Hopf-Wert artanh(1/√3) (wie H45c, ohne Kriterium).
- **Daten:** sin²θ₁₃ ∈ [0,02023; 0,02376] und sin²θ₂₃ ∈ [0,430; 0,596] (NuFIT 6.0, 3σ, normale Ordnung, wie k100). sin²θ₁₂: **JUNO 2026, 2σ: [0,2908; 0,3164]**.
  Zusätzlich berichtet, ohne Kriterium: der 1σ-Bereich [0,2972; 0,3100].

## Vorab offengelegt (analytisch, kein Teil der Vorhersage)
1. Ohne Korrektur (ε = 0) gibt die TM1-Klasse sin²θ₁₂ = 1 − 2/(3 cos²θ₁₃) ∈ [0,3172; 0,3196] für θ₁₃ im 3σ-Bereich. Das liegt **außerhalb** des JUNO-2σ-Bereichs
   (obere Grenze 0,3164). Ohne Frame-Korrektur gibt es also keinen Treffer; das ist die Kontrolle (i).
2. Frame-Abbildungen, die mit der Gruppe vertauschen, ändern eine von der Restsymmetrie festgelegte Spalte **nicht**. Das gilt für die Tachyon-Abbildung z ↦ iz, die
   Zeitumkehr z ↦ z̄ und den HC-Schatten z ↦ z + μ z̄ (k297): Sie wirken auf s und v je Platz gleich und vertauschen mit den reellen Matrizen A und mit der Konjugation.
   Über diese Abbildungen kann μ = β_sym² die Spalte (2/3, 1/6, 1/6) deshalb nicht verschieben. Wirksam werden kann nur eine Abbildung, die die Plätze unterscheidet;
   die einzige erklärte im Repo ist die Maske D = exp(ε W_l).
3. Die Maske zeichnet Platz 3 aus. Die sechs ungeraden ℤ₂ sind unter ihr nicht mehr gleichwertig; deshalb werden alle gerechnet. In Variante A bleibt die
   Neutrino-Seite exakt A-symmetrisch, nur U_e ändert sich.
4. Aus H41 allgemein bekannt: Korrekturen der geladenen Leptonen können θ₁₂ verschieben. Ob bei **festem** ε = η und der TM1-Klasse ein Treffer entsteht und in welche
   Richtung θ₁₂ geht, habe ich nicht gerechnet.
5. Treffer bedeuten hier Verträglichkeit, nicht Beleg: φ bleibt frei, es gibt diskrete Wahlen (A, Zweig, Zuordnung), β_sym ist eingesetzt (OP1 offen), und die Lesart
   ε = η ist eine Idee ohne Herleitung aus einer Wirkung (H45).

## Hypothesen und Kriterien
- **H134a (Verträglichkeit):** Mit ε = η gibt es in Variante A oder B Fälle mit sin²θ₁₃ und sin²θ₂₃ in den 3σ-Bereichen und sin²θ₁₂ im JUNO-2026-2σ-Bereich.
  - **Bestätigt:** mindestens ein Treffer in A oder B. **Widerlegt:** kein Treffer in A und B.
- **H134b (Schärfe):** Unter allen Fällen mit θ₁₃ (3σ) und θ₁₂ (JUNO 2σ) bei ε = η liegt sin²θ₂₃ in einem Bereich der Breite < 0,05 **und** |sin δ| in einem Bereich der
  Breite < 0,3, je Variante.
  - **Bestätigt:** für mindestens eine Variante mit Treffern erfüllt. **Widerlegt:** sonst. Ohne Treffer nicht anwendbar.
- **H134c (Richtung):** Unter allen Fällen mit θ₁₃ (3σ) und θ₂₃ (3σ) bei ε = η, die bei ε = 0 zur TM1-Klasse gehören, liegt der dem JUNO-Mittelwert 0,3036 nächste Wert
  von sin²θ₁₂ näher als 0,3172 − 0,3036 = 0,0136.
  - **Bestätigt:** ja (die Frame-Korrektur kann die Spannung verkleinern). **Widerlegt:** nein (sie lässt sie gleich oder vergrößert sie).
- **Kontrollen:** (i) ε = 0: TM1-Klasse mit sin²θ₂₃ = 0,5, |sin δ| = 1 und sin²θ₁₂ = 1 − 2/(3 cos²θ₁₃) auf 10⁻⁹, kein Treffer im JUNO-2σ-Bereich. (ii) Der übernommene
  Code gibt für die TM2-Lesart mit den Bereichen von k100 die 120 Treffer der Variante A aus H45 wieder. (iii) Massen der geladenen Leptonen auf 10⁻⁹ getroffen (wie k100).
  (iv) Wolfram rechnet ε = 0 und einen Trefferpunkt (falls vorhanden) unabhängig nach. Schlägt eine Kontrolle fehl, ist der Lauf ungültig.

## Folge, vorab festgelegt
- **a und b bestätigt:** Die Lesart „TM1 auf dem Realteil, gesehen im Materie-Frame“ ist mit JUNO verträglich und sagt θ₂₃ und δ voraus; daraus wäre eine eigene
  Vorhersage festzulegen. Der Satz „TM1 nach JUNO disfavorisiert“ gilt dann nur für TM1 ohne Frame-Korrektur.
- **a bestätigt, b widerlegt:** Der Einwand des Autors trägt (die Spannung löst sich bei festem ε = η), aber es ist eine Verträglichkeit mit freiem φ, keine Vorhersage.
- **a widerlegt, c bestätigt:** Die Frame-Korrektur geht in die richtige Richtung, reicht bei festem ε = η aber nicht.
- **a und c widerlegt:** Die erklärte Frame-Abbildung hilft der TM1-Klasse nicht; die Spannung mit JUNO bleibt.
- In jedem Fall: OP3 und OP4 bleiben offen, kein Guard wird berührt. H46 und H9 bleiben unverändert. Physik-Paper und Preprint werden nicht angefasst.

Nach dem Commit dieser Notiz wird daran nichts mehr geändert.
