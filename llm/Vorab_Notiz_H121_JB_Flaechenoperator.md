# Vorab-Notiz H121: Ändert die Frame-Abbildung J_B das Flächenquant, und bildet sie γ_M auf γ_T ab?

**Stand:** 23. November 2026, vor der Rechnung festgelegt. H121a und H121b **nicht blind** (Lie-Algebra und lineare Algebra, von Hand
absehbar); **H121c blind im Zahlenwert**. Anlass, Autor (23.11.): „J_B am Flächenoperator“ (OP1).

## Vorwissen geprüft
- `notes/research/op1_area_quantum_boost_2026_11_18/`: Nach Rovelli–Speziale (gr-qc/0205108) ändert ein unitärer Boost das Flächenspektrum
  nicht; ein frame-abhängiges Flächenquant braucht eine nicht-unitäre Frame-Abbildung (J_B mit iπ/2) oder eine Mittelwert-Lesart (r30.1).
  Ausdrücklich offen: wie J_B auf den Flächenoperator wirkt; nur die klassische Ebene ist über Holst geprüft.
- r31.3/r31.4 (W1 + Holst): Boosts, auch komplexe, lassen die Wirkung invariant; nur eine Dualitätsdrehung der Krümmung ändert γ
  (arctan γ′ = arctan γ + θ), und kein gelisteter Winkel gibt γ_T.
- OP1-Daten: γ_M = 0,237533 (DL, U(1)), γ_T = 0,127384 = ln 2/(π√3) (ABCK), γ_L = γ_M/γ_T = 1,864700 = cosh 2η_sym; Ghosh–Mitra 0,274067.
- Konvention F: J_B = komplexer Boost mit Rapidität iπ/2 entlang der M–T-Achse; J_B² = −1 auf dem Register. r51: J_B hält lichtartige
  Richtungen entlang der Achse und die Querebene fest.
- Zurückgestellte Idee I5 (Auslöser: OP1 bekommt eine Herleitung der Zählregel oder ruht) nicht berührt.

## Aufbau
Lorentz-Algebra mit Drehungen L_i und Boosts K_i ([L_i, L_j] = ε_ijk L_k, [L_i, K_j] = ε_ijk K_k, [K_i, K_j] = −ε_ijk L_k). Lineare
Simplizitätsbedingung wie EPRL: K = γL; Flächenoperator A = γ·√(L²) in Einheiten 8πℓ_P² (Spektrum γ√(j(j+1))). J_B = Ad(exp(iπ/2 · K_x))
mit e = x als M–T-Achse. Kontrolle: ein reeller Boost (Rapidität 0,6175, η_sym). Skript `llm/k241_h121_jb_area.py` (Python, sympy und numpy),
Ausgabe `llm/k241_out.txt`. Wolfram nur, falls erreichbar; Qiskit nicht geeignet.

## Hypothesen und Kriterien
- **H121a (Automorphismus, nicht blind):** J_B erhält die Vertauschungsrelationen und hält L_x, K_x fest; auf den Querkomponenten gilt
  L′_⊥ = ±iK_⊥, K′_⊥ = ±iL_⊥. Kriterium: exakt.
- **H121b (Spektrum unter Konjugation, nicht blind):** Für einen Operator O und eine (auch nicht-unitäre) Darstellung U von exp(iπ/2·K_x) hat
  U O U⁻¹ dieselben Eigenwerte wie O. Prüfung in den endlichdimensionalen Darstellungen (½, 0), (½, ½), (1, 0) ⊕ (0, 1) für O = L² und
  O = L_z: größte Abweichung der sortierten Eigenwerte ≤ 10⁻¹⁰. Folge bei Bestätigung: Nicht-Unitarität allein ändert kein Flächenspektrum.
- **H121c (induziertes γ, blind im Wert):** Aus K = γL folgt nach J_B eine Beziehung K′ = γ′L′ je Richtung (längs und quer zur Achse).
  Bestimmt werden γ′(γ) und die daraus abgelesenen Flächenquanten von T. **H121c bestätigt**, wenn ein so induziertes γ′ oder das Verhältnis
  γ_M/|γ′| auf 10⁻³ relativ γ_T bzw. γ_L trifft; sonst **widerlegt**.
- **Kontrolle:** Ein reeller Boost mit η_sym erhält K = γL nicht komponentenweise, gibt aber kein reelles γ′ ≠ γ für Zustände mit L ⊥ Boostachse?
  Ergebnis wird nur berichtet, nicht bewertet.

## Folge, vorab festgelegt
- H121b bestätigt und H121c widerlegt: J_B kann das Flächenquant weder durch Nicht-Unitarität noch über die Simplizitätsbedingung von γ_M nach
  γ_T bringen; damit ist der letzte im Bestand benannte strukturelle Kandidat für ein frame-abhängiges Flächenquant ausgeschlossen, und OP1
  hängt allein an der Zuordnung der Zählregeln (U2, T-Regel).
- H121c bestätigt: J_B erzeugt γ_T aus γ_M; das wäre eine Herleitung des Kerns von OP1, unter dem Vorbehalt, wie T die Fläche abliest.
- OP1 bleibt in jedem Fall offen, bis die Zählregeln hergeleitet sind.
