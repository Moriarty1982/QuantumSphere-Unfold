# Vorab-Notiz H94: Die Norm am Urknall-Übergang: Bosonen von +1 nach −1 mit einer Nullstelle, Fermionen exakt −1

**Stand:** 6. November 2026, vor der Rechnung festgelegt. Autor (6.11.): „Folge der Asymmetrie“ (Bosonen gegen Fermionen am Urknall, `Erkundung_Fermionen_Urknall.md`). **Teilweise nicht blind:** Die k201-Werte für kΔ = 0,01–8 (H86) sind bekannt, und aus ihnen lassen sich die Vorzeichen bei 0,01 und ab 2 ablesen. Neu sind die Lage der Nullstelle, der Verlauf zwischen 0,05 und 2 und die Werte bis kΔ = 20.

## Vorwissen geprüft und Begründung
- H85, H86 (k201): Bei der Mode, die vor dem Urknall mit positiver Norm (Gewicht −b) einläuft, ist C der Anteil e^{−iωτ} danach, D der Anteil e^{+iωτ}. Lange Wellen: C → C₀, D → D₀ (scharfer Fall). Kurze Wellen: C → 0, √(|D₊||D₋|) = √(b/a).
- Im scharfen Fall mit reellem Sprung ist die gewichtete Norm erhalten: a(|C₀|² − |D₀|²) = b. Im adiabatischen Fall läuft das komplexe Profil um 0 herum, und die Norm kehrt das Vorzeichen: a(0 − b/a) = −b. Das ist die CPT-Zuordnung.
- Fermionen (`Erkundung_Fermionen_Urknall.md`, k209): ψ = c^{−1/2}χ exakt, die gewichtete Ladung c|ψ|² kehrt für jedes kΔ das Vorzeichen.
- Die in `Erkundung_Fermionen_Urknall.md` genannte Bosonen-Erzeugung „n = 0,404 je Mode“ gilt nur im Bild des reellen scharfen Sprungs. Für den glatten komplexen Übergang ist die Bogoliubov-Deutung nicht selbstverständlich. Das prüft dieser Test.
- Eine kosmologische Beobachtungsgröße folgt ohne Δ und ohne Zuordnung der Bosonen-Arten zu den Frames nicht. Geprüft wird deshalb die strukturelle Folge: die Erhaltung der Norm.

## Größe
N(kΔ) := a(|C|² − |D|²)/b. N = +1 heißt: Ein Teilchen bleibt ein Teilchen, Bogoliubov, unitär. N = −1 heißt: exakte CPT-Zuordnung, ebenfalls normerhaltend bis aufs Vorzeichen. |N| ≠ 1 heißt: Die Norm ist nicht erhalten. Für Fermionen gilt analytisch N_F ≡ −1.

## Rechnung
`llm/k210_norm_uebergang.py` (Python/scipy). Gleichung und Profil wie k201 (tanh, Δ = 2, beide Drehsinne). Integration auf der reellen Achse mit rtol 10⁻¹², holomorphe Wronski-Kontrolle. Gitter kΔ = 0,01, 0,02, 0,05, 0,1, 0,2, …, 1 (Schritt 0,1), 1,5, 2, 3, 4, 6, 8, 12, 16, 20. Nullstellen durch Bisektion.

## Hypothesen und Kriterien
- **H94a:** |N±(0,01) − 1| ≤ 0,05 und |N±(20) + 1| ≤ 0,05 für beide Drehsinne.
- **H94b:** N± hat auf [0,01; 20] genau einen Vorzeichenwechsel je Drehsinn. Die Lage k*Δ wird berichtet, ohne Vorhersage des Werts.
- **H94c:** Bei der Nullstelle ist |N| < 1, die Norm also nicht erhalten. Auf dem Gitter gibt es Punkte mit 0,1 < |N±| < 0,9. Dieser Teil folgt aus a und b, sobald N stetig ist; er wird mitgeprüft.
- **H94d (analytisch, nicht blind):** Für Fermionen gilt N_F = −1 auf allen Gitterpunkten. Numerisch wird das mit der Weyl-Gleichung bei gleichem Profil nachgerechnet (Rest ≤ 10⁻⁸).
- **Gültigkeit:** Die holomorphe Wronski-Determinante ist relativ auf ≤ 10⁻⁸ konstant, sonst sind a–d ungültig.

## Umgang mit Abweichungen
Wenn N bei kurzen Wellen nicht gegen −1 geht, sondern zum Beispiel gegen ∓(Asymmetrie der Drehsinne), wird das berichtet. Gilt etwa nur für das Mittel beider Drehsinne N̄ → −1, so ist auch das ein Befund, nicht angepasst. Wenn es mehr als eine Nullstelle gibt, ist b widerlegt.
