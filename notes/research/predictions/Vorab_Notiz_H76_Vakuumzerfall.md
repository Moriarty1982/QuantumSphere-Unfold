# Vorab-Notiz H76: Quanten-Zerfall des Vakuums der M–T-Paarung über die Gravitation

**Stand:** 5. November 2026, vor jeder Rechnung festgelegt. **Nicht blind:** Teil (a) und die Skalierung in (b) sind aus der Literatur bekannt (Cline, Jeon, Moore 2004; Kaplan, Sundrum 2005). Neu ist nur der Zahlenfaktor c für unser Modell und die Frage, ob W2 den nötigen Rahmen selbst liefert.

## Anlass
r82 (H75) hat gezeigt: Ist die Gravitation die einzige Kopplung zwischen Materie (M) und dem Tachyonbild (T, Vorzeichen F3), gibt es klassisch keine exponentielle Instabilität. Offen blieb der Quanten-Zerfall des Vakuums in Paare positiver und negativer Energie. Autorentscheidung 5.11.: diesen Punkt zuerst prüfen, weil die Aufhebung der Vakuumenergie (r82.1) sonst nichts trägt.

## Vorwissen geprüft
- Repo: keine frühere Rechnung zum Vakuumzerfall. `predictions/Ergebnis_H75_Gravitationskopplung.md` nennt ihn als offen; `analysis/OP5_Neutral_Pair_Dynamics_Result.md` und `OP5_Native_Pair_Potential_Audit.md` behandeln Geister nur als Eich-Geister bzw. Fluktuationsoperator, nicht als Sektor negativer Energie. H71 (Tachyonbild mit Masse tachyonisch), H74 (direkte Kopplung instabil), H75 (Gravitation allein klassisch tragbar), r70/H70 (Versatz in konformer Zeit fest, also ein mitbewegter Rahmen).
- Zurückgestellte Ideen: I4 (Kondensation tachyonischer Moden, meV-Abschätzung) – Auslöser 1 (Higgs-Sektor) getroffen; wird nach dem Test dem Autor vorgelegt, nicht still eingebaut.
- Literatur: Cline, Jeon, Moore, *The phantom menaced* (hep-ph/0311312): Prozess 0 → 2γ 2φ über Gravitonaustausch, Phasenraum divergiert über die Boosts, mit Lorentz-brechendem Cutoff Γ ~ Λ⁸/M_P⁴, Gammastrahlen-Hintergrund (EGRET) gibt Λ ≲ 3 MeV. Kaplan, Sundrum, *A symmetry for the cosmological constant* (hep-th/0505265): Energieparität mit Geist-Kopie des Standardmodells, Gravitation bricht sie schwach, Vakuumzerfall verlangt Lorentz-brechenden Gravitations-Cutoff μ ≲ 2 meV.

## Modell (vereinfacht, vorab festgelegt)
Je ein masseloses Skalarfeld im M-Sektor (φ, positive Energie) und im T-Sektor (χ, Vorzeichen F3: negative Energie, gleiche Dispersion ω = |k|). Kopplung nur über das Graviton, κ² = 32πG, G = 1/M_P², M_P = 1,22·10¹⁹ GeV. Ein Diagramm: Graviton verbindet das φ-Paar (p₁, p₂) mit dem χ-Paar (p₃, p₄), p₃,₄ = (−|k|, k). Amplitude M = (κ²/4) [T₁₂^{μν}T₃₄_{μν} − ½ T₁₂ T₃₄]/P², P = p₁ + p₂, T_{μν}(p,q) = p_μq_ν + q_μp_ν − η_{μν} p·q. Rate pro Volumen Γ/V = ¼ ∫ Π d³k_i/((2π)³2E_i) (2π)⁴δ⁴(Σp) |M|². Skalare stehen für Photonen und T-Quanten (Vereinfachung wie bei Cline et al.; Ordnung der Größe, nicht Spin-genau). Massive Tachyonmoden (H71) sind hier nicht enthalten.

## Hypothesen und Entscheidungskriterien
- **H76a (Lorentz-Invarianz → Divergenz):** Mit nur einem Lorentz-invarianten Cutoff P² < Λ² ist der Zerfall kinematisch erlaubt und die Rate unbeschränkt. Prüfung: zusätzlicher Rahmen-Cutoff |k_i| < L·Λ, L = 2, 4, 8, 16. **Bestätigt**, wenn Γ(L)/Γ(L/2) ≥ 2 für jedes L und das Verhältnis nicht gegen 1 fällt. **Widerlegt**, wenn Γ(L) für L ≥ 8 innerhalb von 10 % sättigt.
- **H76b (Rahmen-Cutoff → Λ⁸):** Mit einem Cutoff |k_i| < Λ im ausgezeichneten Rahmen ist Γ/V = c·Λ⁸/M_P⁴. Prüfung: Exponent aus Λ = 1, 2, 4 (bei festem M_P) gleich 8 auf ±0,05; c wird angegeben (Monte Carlo, Fehler < 5 %). **Bestätigt**, wenn beides erfüllt ist.
- **H76c (Schranke):** Mit unserem c und der Abschätzung von Cline et al. (deren c ~ 1 gesetzt) verschiebt sich die Schranke um den Faktor c^{−1/7}. **Erwartet:** Λ ≲ 3 MeV · c^{−1/7}, also höchstens einige zehn MeV, jedenfalls weit unter der Higgs-Skala von 100 GeV. Entscheidung: Liegt die Schranke unter 100 GeV, kann der T-Sektor die Higgs-Vakuumenergie aus r82.1 nicht als Lorentz-invariante Kopie bis zur Higgs-Skala aufheben, ohne dem Gammastrahlen-Hintergrund zu widersprechen.
- **H76d (Rahmen):** Vorab-Lesart: Der ausgezeichnete Rahmen kann der mitbewegte Rahmen aus H70 sein (Versatz in konformer Zeit fest). Das ist eine Lesart, kein Testergebnis; ob W2 einen Cutoff in diesem Rahmen *erzeugt*, wird hier nicht geprüft.

## Was der Test nicht entscheidet
Den Wert von Λ aus der Struktur; Spin-1-Photonen und massive Tachyonmoden; Zerfälle über andere Kopplungen (H74 schließt direkte aus). OP5 bleibt offen.

Skript: `llm/k191_vakuumzerfall.py` (wird erst nach dem Commit dieser Notiz geschrieben).
