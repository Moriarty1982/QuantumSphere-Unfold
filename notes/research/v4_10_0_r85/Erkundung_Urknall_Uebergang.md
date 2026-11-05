# Erkundung: Der Übergang am Urknall bei δ = 0 (5. November 2026)

**Status: Erkundung, analytisch (sympy), ohne Kriterium.** Autor 22:23: Variante 2 (δ = 0, Zustand am Urknall). Grundlage: H80, H84 (Quantenmoden bei τ* singulär, spricht für δ = 0), Arbeitsannahme F3-Gewicht 1.

## Vorwissen geprüft
H80 und `llm/Erkundung_Zweite_Lesart_FRW.md` (Spiegelung um den Urknall, Fortsetzung a(−τ) = ±a(τ)); H84; Boyle–Finn–Turok, arXiv:1803.08928 (CPT-Bild vor dem Urknall, Vakuumwahl durch CPT); H79 (Bild des Wirkungsterms mit Gewicht a − b bzw. Vorzeichen −1 der Kinetik).

## 1. Eine übersehene Modellwahl: das Gebiet
Die Spiegelung Λ(iπ) bildet nicht nur die Felder ab, sondern auch das Gebiet: Das Bild von τ > 0 ist τ < 0. H80 hat beide Lesarten auf der ganzen Zeitachse angenommen (Gebiet G1). Dann gilt H80: keine neue Dynamik. Möglich ist auch **G2**: Die Materie-Lesart lebt auf τ > 0 (Gewicht a), die Tachyon-Lesart auf ihrem Bild τ < 0 (Gewicht b, Kinetik mit Vorzeichen −1). Die Felder hängen nur am Urknall zusammen. Das ist strukturell das Zwei-Blatt-Bild von Boyle, Finn und Turok. H80 bleibt für G1 richtig; G2 hat H80 nicht geprüft.

## 2. Konforme Felder unter G2 (Licht, masselose Teilchen; sympy)
Konforme Felder sehen in konformer Zeit den flachen Raum. Je Mode: vor dem Urknall Gewicht −b, danach a. Übergangsbedingungen aus der Wirkung: Feld stetig, (Gewicht × Zeitableitung) stetig.
- Positive Norm vor dem Urknall (Gewicht −b) hat die Mode e^{+iωτ}. Aus ihr wird danach C·e^{−iωτ} + D·e^{+iωτ} mit C = (a + b)/(2a), D = (a − b)/(2a). Die Norm bleibt erhalten (2bω vorher und nachher).
- Normiert: Bogoliubov-Koeffizienten α = (1 + x)/(2√x), β = (1 − x)/(2√x) mit x = b/a = β_sym², |α|² − |β|² = 1.
- **β/α = (1 − x)/(1 + x) = 1/γ = 0,5363**, und die Teilchenzahl je Mode **n = |β|² = (1 − x)²/(4x) = 0,404**, für jede Wellenzahl gleich.

## Lesart und Grenzen
- Unter G2 entstehen am Urknall Teilchen, und ihre Zahl je Mode ist durch β_sym allein festgelegt, ohne freien Parameter. Das Verhältnis der Koeffizienten ist 1/γ, dieselbe Größe wie die Kinetik-Gewichtung in H78/H79.
- Die Zahl ist für alle k gleich. Das ist eine Folge des scharfen Übergangs: Die Energiedichte divergiert dann im Ultravioletten. Ein endlich schneller Übergang würde hohe k unterdrücken; seine Breite wäre eine neue Skala.
- Für Fermionen (Gleichungen erster Ordnung) ist die Übergangsbedingung bei einem Vorzeichenwechsel des Gewichts nicht eindeutig; nicht gerechnet. Nicht-konforme Felder (Masse, minimale Kopplung) haben am Urknall zusätzlich die übliche Singularität.
- Bei Photon-Gewichten (a = b) wäre β = 0: kein Teilchenübergang, das Bild geht vollständig in positive Frequenz über.

## Entscheidung für den Autor
Soll die Tachyon-Lesart auf der ganzen Zeitachse leben (G1, H80: nichts Neues) oder auf dem Bild vor dem Urknall (G2: Teilchenerzeugung am Urknall mit n = (1 − β_sym²)²/(4β_sym²) je Mode)? Bei G2 wäre der nächste Test, ob ein endlich schneller Übergang ein endliches Spektrum gibt und was dessen Breite festlegt.
