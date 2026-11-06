# Erkundung: Fermionen am Urknall-Übergang (G2): keine Beimischung, exakte CPT-Zuordnung, Amplitude β_sym

**6. November 2026. Status: Erkundung, analytisch, ohne Kriterium.** Das Ergebnis steht vor jeder Rechnung analytisch fest, deshalb ist es kein Test und hat keine H-Nummer. Der Autor sagte „weiter“; das betrifft den offenen Punkt „Übergangsbedingung für Fermionen am Urknall (G2)“ aus der Übergabe und aus `Erkundung_Urknall_Uebergang.md`. Symbolische Kontrolle in `k209_fermionen_urknall.py` (Ausgabe `k209_out.txt`).

## Vorwissen geprüft
- `Erkundung_Urknall_Uebergang.md`: Für Fermionen sei die Übergangsbedingung bei einem Vorzeichenwechsel des Gewichts „nicht eindeutig; nicht gerechnet“.
- H79: Das T-Bild ist −L_M für die ganze Wirkung (holomorphe Adjungierte).
- `Erkundung_Spinorphase_zweite_Lesart.md`: Arbeitsannahme F3-Gewicht 1.
- Autorentscheidung 2: symmetrische Kinetik.
- H85, H86, r02 (H91–H93): Skalare und konforme Felder zweiter Ordnung mischen am Übergang, C ≠ 0, Asymptotik ln|C| = −πkΔ + c√(kΔ) − ½ln(a/b).
- Keine frühere Notiz rechnet Fermionen am Übergang.

## Rechnung
Unter G2 und der zweiten Lesart steht vor dem Urknall −b·L_M, danach a·L_M. Mit einem glatten (auch komplexen) Profil ist das c(τ)·L_M mit c von −b nach a. Für die symmetrische Dirac- bzw. Weyl-Wirkung ½[c ψ̃(iγ∂ − m)ψ + c.c.-Teil] gibt die Variation
  c(iγ^μ∂_μ − m)ψ + (i/2)c' γ⁰ψ = 0.
Mit **ψ = c^{−1/2}χ** wird daraus exakt c^{1/2}(iγ∂ − m)χ = 0 (sympy, Rest 0, auch mit Masse). χ ist eine freie Lösung, für **jedes** Profil c(τ) und jede Wellenzahl.

## Befunde
1. **Keine Beimischung.** Positive und negative Frequenzen mischen nicht, für alle kΔ und jedes Profil (scharf, tanh, komplex um 0 herum). Das Gewicht lässt sich bei einer Gleichung erster Ordnung wegskalieren, bei den Skalaren und Eichfeldern (zweite Ordnung, (wχ')' + k²wχ = 0) nicht. **Fermionen entstehen am Urknall unter G2 nicht**, Bosonen mit Materie-Gewichten schon (n = 0,404 je Mode im scharfen Grenzfall, oberhalb 1/(πΔ) abfallend).
2. **Übergangsfaktor.** ψ_nach/ψ_vor = (c_vor/c_nach)^{1/2} = (−b/a)^{1/2}, entlang des Weges w = b^{1−s}a^s e^{±iπ(1−s)} stetig fortgesetzt: **±i·√(b/a) = ±i·β_sym = ±0,5494i**. Die beiden Drehsinne unterscheiden sich nur im Vorzeichen der Phase. Der Hauptzweig der Wurzel gäbe für beide +i, maßgeblich ist der stetige Zweig. Im Betrag gleich, wie bei den Skalaren (r02.1).
3. **Unitär.** |c|·|ψ|² ist vor und nach gleich (b|ψ_vor|² = a|ψ_nach|²). Normierte Zustände gehen in normierte über; nichts wird erzeugt oder vernichtet.
4. **Exakte CPT-Zuordnung.** Die Frequenz bleibt erhalten. In der T-Lesart (Gewicht −b) hat e^{+iωτ} positive Energie; nach dem Urknall (Gewicht a) ist dieselbe Mode eine Mode negativer Frequenz. Ein Teilchen der T-Lesart vor dem Urknall geht also vollständig in einen Antiteilchen-artigen Zustand der M-Lesart über, für alle k. Bei den Skalaren gilt das nur für kurze Wellen (H85, H86), bei Fermionen exakt. Das ist das CPT-Bild von Boyle–Finn–Turok in reiner Form.
5. **Masse.** Die Masse ändert nichts, weil die zweite Lesart die ganze Wirkung mit demselben c gewichtet (H79, H82). Erzeugung durch die Expansion selbst (Masse bricht die konforme Invarianz, a(τ) in m·a(τ)) ist davon getrennt und hier nicht betrachtet.
6. **Voraussetzungen.** Die Befunde gelten für die symmetrische Kinetik (Autorentscheidung 2). Mit nicht symmetrisierter Kinetik c ψ̃ iσ̄∂ψ wäre ψ stetig und die Ladung c ψ̃ψ spränge; das ist nicht die W1-Form. F3-Gewicht 1 ist vorausgesetzt (Arbeitsannahme). Mit Gewicht ½ stünde vor dem Urknall −i·b statt −b, die Phase wäre dann e^{±iπ/4}; sonst ändert sich nichts.

## Folge
- Unter G2 trennt der Urknall Bosonen und Fermionen. Bosonen mit Materie-Gewichten bekommen eine Beimischung und werden erzeugt, Fermionen nicht. Fermionen gehen exakt CPT-gespiegelt hindurch, mit dem Amplitudenfaktor β_sym in ψ (unitär in der gewichteten Norm).
- Mögliche Folgefrage (Test): Hat die Asymmetrie Bosonen/Fermionen eine beobachtbare Folge? Etwa über das Verhältnis der Strahlungsdichten nach dem Urknall, das für Bosonen von n = 0,404 je Mode (bis 1/(πΔ)) und für Fermionen von 0 käme; Δ bleibt die freie Skala.

## Nachtrag (6.11., H94)
Die Aussage zu den Bosonen (Befund 1 und Folge: „Bosonen mit Materie-Gewichten werden erzeugt, n = 0,404 je Mode“) gilt nur im Bild des reellen scharfen Sprungs. Beim glatten komplexen Übergang ist die gewichtete Norm der Bosonen nur für kΔ → 0 (+1) und kΔ ≫ 1 (−1, CPT) erhalten; dazwischen wird sie kleiner, verstärkt oder 0 (Nullstelle bei k*Δ = 0,74 bzw. 0,26 je Drehsinn). Die Fermion-Aussagen bleiben (N_F = −1 exakt). Siehe `Ergebnis_H94_Norm_Bosonen_Fermionen.md`.
