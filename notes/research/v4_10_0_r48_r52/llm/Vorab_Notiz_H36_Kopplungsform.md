# Vorab-Notiz H36: Erklärt eine andere Kopplungsform der Maske die Mischung?

Festgelegt am 2026-10-24, **vor** der Rechnung. Autor: „und danach die kopplungsform“. Bezug: r47 (Maske W_q = diag(0, −2, −1), W_l = diag(0, 0, −3),
Partner im Zeitumkehr-Frame gelesen), r50/H34 (lineare Störung M ↦ M + ε(WM + MW) widerlegt; die Hierarchie begrenzt ε, weil der Term ε²WCW
selbst Massen erzeugt), r51/H35 (die Tachyon-Abbildung z ↦ iz lässt die Sektoren fest, die Zeitumkehr T vertauscht sie).

## Zwei Kopplungsformen (beide aus der Struktur, keine hergeleitet)

- **Form K (Kongruenz, Partner über die Zeitumkehr gelesen wie in r47):** M_X = D_X C_X D_X mit D_X = exp(ε W_X). In erster Ordnung ist das die Form von
  r47; exakt bleibt der Rang von C erhalten, der Term ε²WCW fällt weg.
- **Form S (Ähnlichkeit, Partner über die Tachyon-Abbildung gelesen):** Der rechtshändige Partner bleibt in seinem Sektor (H35a) und trägt dessen Gewicht
  −W. Dann M_X = D_X C_X D_X⁻¹.

C_X hermitesch und ℤ₃-zirkulant, C_X = F diag(λ_X) F†, λ_X reell; W_u = W_d = W_q, W_e = W_ν = W_l; ein gemeinsames ε ≥ 0; Dirac-Neutrinos.
Massen = Singulärwerte von M_X, Mischung aus den linken Singulärvektoren (Spalten nach aufsteigender Masse), V = U_u† U_d, U = U_e† U_ν.

## Offenlegung (vorab analytisch gesehen)

Form K ist eine Froggatt-Nielsen-Textur mit den Ladungen w = (0, 2, 1) (Quarks) bzw. (0, 0, 3) (Leptonen) und λ = e^{−ε}. Für Quarks erwartet man
grob |V_us| ∼ |V_cb| ∼ λ und |V_ub| ∼ λ², die Daten haben |V_cb| ≈ 0.19 |V_us|. Erwartung daher: H36a eher widerlegt. Bei den Leptonen geben die
Ladungen (0, 0, 3) zwei Plätze gleichen Gewichts. Form S nicht vorab gerechnet.

## Daten und Verfahren

Daten wie in H34 (Massen bei M_Z nach Huang/Zhou, NuFIT 6.0 normale Ordnung, PDG 2024, m₁ ∈ {0, 0.001, 0.003, 0.01, 0.02, 0.05, 0.1} eV). Zweige wie in H34
(24 Zuordnungen je Sektor, Start bei ε = 0, relative Toleranz 10⁻⁹, bei m₁ = 0 absolute), aber Schrittweite 0.01 bis ε = 6.

## Hypothesen

- **H36a (Form K, CKM):** Es gibt ε und Zweige für u und d mit |V_us|, |V_cb|, |V_ub| alle innerhalb ±20 % der Daten. Anteil der passenden Kombinationen wird
  mitberichtet.
- **H36b (Form K, gemeinsames ε):** Bei einem ε aus H36a gibt es m₁ und Lepton-Zweige mit allen drei PMNS-Größen in den 3σ-Bereichen.
- **H36c (Form S, CKM):** wie H36a für Form S.
- **H36d (Form S, gemeinsames ε):** wie H36b für Form S.

## Entscheidungskriterium (verbindlich)

- H36a und H36b bestätigt ⇒ Form K erklärt beide Mischungen mit einem Parameter; passende m₁ gelten als Vorhersage. Ein großer Anteil passender Kombinationen
  zählt als schwacher Befund. Ebenso für Form S mit H36c, d.
- Nur H36a (bzw. H36c) bestätigt ⇒ die Form erklärt die Quark-Mischung, ein gemeinsames ε mit den Leptonen ist widerlegt.
- Alle widerlegt ⇒ keine der beiden aus der Struktur nahe liegenden Kopplungsformen erklärt die Mischung; dann fehlt eine weitere Zutat (andere C als
  zirkulant oder verschiedene ε je Sektor), und das ist als offene Wahl festzuhalten, nicht als Ergebnis.

Nach dem Commit dieser Notiz wird daran nichts mehr geändert.
