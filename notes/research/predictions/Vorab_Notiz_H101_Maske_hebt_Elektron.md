# Vorab-Notiz H101: Hebt die Generationsmaske aus r47 das Elektron aus dem Qubit-Oktanten?

**Stand:** 13. November 2026, spät, vor der Rechnung festgelegt. Autorenauftrag: „Maske r47 vorab prüfen“. **Nicht blind**
gegenüber den Daten (Leptonmassen bekannt); die Vorhersage für m_μ/m_τ ist vor dem Commit dieser Notiz nicht gerechnet.
Skript `k223_test_h101.py`.

## Vorwissen geprüft
- v4.9.0-r47 (H32): Lepton-Maske W_l = diag(0, 0, −3) aus der Abweichung der trialitätskovarianten Chiralität, unter einer
  Modellannahme; Form der Störung M → M + ε(WM + MW); ε frei.
- v4.9.0-r57 (H41): geladene Leptonen in **Form S** (M_e = D C D⁻¹, D = exp(ε W_l)), Neutrinos in **Form K** (M = D M₀ D).
  Form S ist eine Ähnlichkeitstransformation und ändert die Eigenwerte nicht; sie kann das Elektron nicht heben (analytisch,
  vorab festgestellt, kein Test).
- `op3_selection_principle_2026_11_13.md`: In A_4 ist K = 2/3 der einzige Wert; die exakte Konstruktion (Qubit-Oktant)
  gibt ein masseloses Elektron; die Elektronmasse ist ein A_4-Bruch; √m_e/⟨√m⟩ ≈ π/12 − θ_e.

## Verfahren
- Ausgangspunkt: das exakte Oktanten-Tripel als Massenwurzel-Operator (Auslesung A), C = 1 + zP + z̄P² mit z = e^{iπ/12}/√2,
  P die zyklische Vertauschung; Eigenwerte 1 + √2 cos(π/12 + 2πk/3), einer davon null.
- Störung in **Form K**: M(ε) = D C D, D = exp(ε W_l), W_l = diag(0, 0, −3) (Maske auf Platz 3; die Plätze 1 und 2 werden
  zur Kontrolle ebenfalls gerechnet und müssen dasselbe Spektrum geben).
- Massen: m_k ∝ (Eigenwert_k)², sortiert.
- ε wird so bestimmt, dass m_min/m_max = m_e/m_τ = 2,8757·10⁻⁴ (Polmassen 0,51099895; 105,6583755; 1776,93 MeV). Beide
  Vorzeichen von ε werden gesucht; maßgeblich ist die Lösung mit kleinstem |ε|. Gibt es keine Lösung, ist H101 widerlegt.
- Ausgegeben werden m_μ/m_τ, K und θ (aus den Massen).
- Nebenrechnung, nicht Teil des Kriteriums: die lineare Form von r47, M = C + ε(W C + C W).

## Entscheidungskriterium
- **H101a:** |(m_μ/m_τ)_pred − 0,0594649| / 0,0594649 ≤ 1 %: bestätigt, sonst widerlegt.
- **H101b:** |K_pred − 0,666661| ≤ 10⁻³: verträglich, sonst nicht.
- H101 gilt als bestätigt, wenn a und b gelten.

## Bei Bestätigung / Widerlegung
- **Bestätigt:** Die Maske aus r47 ist ein nativer Kandidat für den A_4-Bruch; mit einer Zahl (ε) folgen zwei
  Massenverhältnisse aus dem Oktanten. Herkunft von ε und Wahl der Form K bleiben offen.
- **Widerlegt:** Die Maske in dieser Form hebt das Elektron nicht richtig aus dem Oktanten; der Bruch muss anders entstehen.

## Offenlegung
- Die Daten sind bekannt; das Ergebnis der Rechnung nicht. Form K für die geladenen Leptonen weicht von r57 ab (dort Form S),
  weil Form S die Massen nicht ändert. Die Modellannahme von r47 bleibt unbegründet.
