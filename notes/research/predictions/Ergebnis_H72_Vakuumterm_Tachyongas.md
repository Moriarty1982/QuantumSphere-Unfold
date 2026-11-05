# Ergebnis H72: Ein Λ-artiger Term entsteht aus einem Gas tachyonischer Moden, aber nicht festgelegt

**5. November 2026. Vorab-Notiz `Vorab_Notiz_H72_Vakuumterm_Tachyongas.md` (Commit bc85519). Skript `k180_test_h72.py`, Ausgabe `k180_out.json`, Nachprüfung im Ergebnis vermerkt. Status: H72a und H72b bestätigt (nicht blind), H72c widerlegt.**

## Kontrollen
- Isotropie der Richtungsmittelung exakt (Nebendiagonale 0, Anisotropie 0).
- Die Kontrolle „T ∝ pp“ meldete im Skript 1,96, weil die Prüfformel p mit oberem statt unterem Index nahm. Mit p_μ = (ω, 0, 0, −k) gilt T = N p_μp_ν auf 3e-16. Ein Fehler der Kontrollformel, nicht der Daten; die Ergebnisse unten hängen nicht davon ab (die Mittelung entfernt T_tz).

## Ergebnis
- **H72a bestätigt:** k_A = 1,2 (λ = +1, N = −0,83, negative Energie) und k_B = 3,0 (λ = −1, N = +0,33) mit Gewichtsverhältnis 0,209 geben gemittelt T = ρη mit ρ = 0,191, Residuum 3e-16. Das ist ein **Λ-artiger Term: Druck = −Dichte, isotrop**.
- **H72b bestätigt:** Für die Familie k_B ∈ {1,05; …; 10} gibt es jeweils ein positives Gewichtsverhältnis mit exakt Λ-artigem T (Residuen ≤ 6e-16). ρ nimmt beide Vorzeichen an (±0,11 bis ±0,21 bei Gewicht 1 für A) und skaliert mit der Gesamtamplitude. Die Höhe ist also frei. Kontrolle V1 (normale Masse): w ≥ 0,0033 > −1, nie Λ-artig.
- **H72c widerlegt:** Bei einem einzigen Impulsbetrag haben beide λ-Moden dasselbe w = k²/3ω² ≥ ⅓.
  - Mit den Gewichten des Materie-Frames (beide Zuordnungen) bleibt w ∈ [0,334; 334], es gibt keinen Λ-Punkt.
  - Mit den Photon-Gewichten (½, ½) ist T identisch null, exakt neutral wie in H69; die gemeldeten „Nullstellen“ waren 0/0-Rauschen.

## Wie der Vakuumterm entsteht
1. Er braucht Moden **beider Normvorzeichen**, also positive und negative Energie, und **mindestens zwei verschiedene Impulsbeträge**. Bei einem Impuls und einer Normsorte ist w ≥ ⅓.
2. Mischt man eine negative Tachyon-Mode nahe der Massenschale (|k| ≈ m, ω ≈ 0, fast nur Spannung) mit einer positiven bei größerem |k|, so hebt sich der Druck gegen die Dichte so auf, dass p = −ρ übrig bleibt.
3. Höhe und Vorzeichen von ρ legt das Gewichtsverhältnis fest, und das ist frei. Die Frame-Gewichte von Konvention F legen es bei einem Impuls nicht fest. Das bestätigt den Vorbefund aus `OP5_Neutral_Pair_Dynamics_Result.md`: Die Struktur liefert die *Möglichkeit* eines Vakuumterms, aber nicht seine Größe.

## Was ihn festlegen könnte (Vorschlag, nicht getestet)
Aus H69 ist ein Frequenzabstand zwischen zwei Moden bekannt: der Versatz der Frames, Δω = π/δ. Wenn der Versatz die zwei Impulsschalen festlegt und die Frame-Gewichte ihre Besetzung, wäre w und damit das Λ-Verhältnis bestimmt. Das wäre H73, vorab zu formulieren.

## Grenzen
Klassisch; inkohärente Mittelung angenommen; negative Energie gehört zu einem Feld negativer Norm, dessen Stabilität offen ist.
