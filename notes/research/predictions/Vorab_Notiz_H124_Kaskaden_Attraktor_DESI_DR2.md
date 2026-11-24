# Vorab-Notiz H124: Die rückgekoppelte Kaskade mit Attraktor Ω_M = β² (ε = 3) gegen DESI DR2 BAO

**Stand:** 23. November 2026, vor der Datenrechnung festgelegt. Autor (Projekt-Thread „OP5-Weg entscheiden“, 23.11., 23:22): „jetzt weg b“, also der Attraktor-Weg (Idee I7, zurückgestellt in r56) wird aufgenommen; W1/W2 bleiben eingefroren, gerechnet wird nur an der Kaskade aus r31/r05.5. **Nummer:** H123 ist für Q1a (Orientierung) vorgemerkt, daher H124. **Nicht blind:** DESI DR2 ist veröffentlicht, und aus H97 ist bekannt, dass DR2 bei Ω_M = β² nur ε ≲ 0,4 zulässt; eine Widerlegung ist zu erwarten. Ein Ergebnis bei freiem Ω_M heute ist vorher nicht gerechnet.

## Vorwissen geprüft
- `../v4_10_0_r05/Vorschlag_Bruecke_Kaskade_Friedmann.md`, `Fundstellen_Dynamik_Lambda_Auslesung.md` (Brücke 3, Γ = εH; Zeit und Dichte als offene Setzungen).
- `Vorab_Notiz_H97_Bruecke_DESI_DR2.md`, `Ergebnis_H97_Bruecke_DESI_DR2.md` (ε = 1 bei Ω_M = β² widerlegt, χ² = 105; ε ≲ 0,4 erlaubt).
- `Vorab_Notiz_H96_Omega_M_beta2.md` (Ω_M heute = β², offen).
- r70.3/H48 (eingefrorener Wert hängt an der Expansionsgeschichte), r23.4 (Kaskaden-Attraktor mit Reservoir hängt an der Kopplung), I3/H95 (Mischungen scheitern).
- r56 (Λ als Eingabe in 𝒦; die Auslesung tauscht Λ gegen die Epoche), Idee I7 in `../v4_10_0_w1/Zurueckgestellte_Ideen.md`.
- Zurückgestellte Ideen geprüft: I7 ist genau dieser Weg; I1–I6 nicht ausgelöst.

## Rückwärtssuche (vor der Notiz, Wolfram, `../op5_attractor_2026_11_23/k243_attraktor_fixpunkte.wl`)
Ziel: eine Dynamik der Kaskade, deren Attraktor Ω_M = β² ist. Für Brücke 3 (Vakuum zerfällt mit Rate β²Γ, Γ = εH, in Materie) gilt flach und ohne Strahlung exakt
  dΩ_M/dN = (1 − Ω_M)(εβ² − 3Ω_M),  N = ln a.
Fixpunkte: Ω_M = 1 (Materie-Ära, abstoßend für εβ² < 3) und Ω_M* = εβ²/3 (anziehend). **Ω_M* = β² genau für ε = 3**, also Γ = 3H: ein Kaskadenschritt je Volumen-e-Faltung (die Verdünnungsrate der Materie). Das ist eine Folgerung aus der Attraktorforderung, keine Herleitung aus der Struktur; die Wahl ε = 3 ist damit gesetzt, aber nicht frei. Am Attraktor gilt w_eff = −1 + β² = −0,698 und die Kopplung δ = εβ² = 0,906. Die Bahn läuft von der Materie-Ära zu β²: (Ω_M − β²)/(1 − Ω_M) ∝ e^{−3(1−β²)N}. Heute muss daher Ω_M > β² gelten; H96 (Ω_M heute = β²) ist in diesem Modell nur asymptotisch erfüllt.

## Modell (festgelegt)
Flaches FRW mit
  ρ̇_Λ = −3β²·H·ρ_Λ,  ρ̇_M + 3Hρ_M = 3β²·H·ρ_Λ,  ρ_r ∝ a⁻⁴,  β² = 0,3018465583,
Ω_r = 9,1·10⁻⁵, Ω_Λ = 1 − Ω_M0 − Ω_r. Freie Größen: Ω_M0 im Bereich (β², 1) und die Abstandsskala h·r_d.

## Daten (festgelegt)
Dieselben 13 DESI-DR2-BAO-Werte wie in H97 (arXiv:2503.14738, Tabelle IV, mit Systematik), übernommen aus `../v4_10_0_r05/llm/k216_bruecke_desi_dr2.py`.

## Statistik und Kriterium
- χ²_min über Ω_M0 und h·r_d, 13 Werte, 11 Freiheitsgrade.
- **H124 widerlegt**, wenn p(χ²_min; 11) < 0,01, also χ²_min > 24,72.
- **Nicht ausgeschlossen**, sonst. Berichtet werden dann auch Ω_M0 und Δχ² gegen flaches ΛCDM (freies Ω_m); eine Bestätigung ist das nicht, weil die Daten bekannt sind.

## Gültigkeit
Dieselbe Kontrolle wie H97: Flaches ΛCDM mit freiem Ω_m muss Ω_m = 0,2975 ± 0,003 und h·r_d = 101,54 ± 0,5 Mpc reproduzieren; sonst ist der Test ungültig.

## Nachträglich erlaubt (als Erkundung, nicht Teil des Tests)
Der Bereich von ε bei freiem Ω_M0, den DR2 zulässt, und der dazugehörige Attraktor εβ²/3.
