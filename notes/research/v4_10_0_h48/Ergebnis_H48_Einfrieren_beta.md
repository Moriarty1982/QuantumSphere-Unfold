# Ergebnis H48: β_sym als eingefrorene Länge des M/T-Zustands

Gerechnet am 2026-10-28 nach der Vorab-Notiz `llm/Vorab_Notiz_H48_Einfrieren_beta.md` (lokal e40a705, GitHub 0ff3ab2).
Skript `llm/k107_test_h48.py`, Ausgabe `llm/k107_out.txt` und `llm/k107_out.json`.

## Urteil: H48 widerlegt (Prüfung A)

Von 288 Läufen frieren alle ein (kein Bounce, kein Lauf ohne Einfrieren). Innerhalb ±1 % von r/(1 + r) liegen nur 21 Läufe, alle mit
H₀ = 10³ und g n₀ = 10⁴. Im übrigen Raster reicht |b_∞| von 10⁻¹² bis 0,87.

|b_∞| für r = 1, ohne Einstein–Cartan, Λ = 0 (Ziel 0,5):

| g n₀ \ H₀ | 10⁻³ | 10⁻¹ | 10 | 10³ |
|---|---|---|---|---|
| 10² | ≈ 0 (4·10⁻¹⁰) | ≈ 0 (2·10⁻⁶) | 0,316 | 0,813 |
| 10³ | ≈ 0 (6·10⁻¹¹) | ≈ 0 (2·10⁻⁷) | 0,045 | 0,104 |
| 10⁴ | ≈ 0 (6·10⁻¹²) | ≈ 0 (8·10⁻⁸) | 3·10⁻⁵ | 0,497 |

Der eingefrorene Wert hängt also an H₀ und g n₀, nicht nur an r. Die Erwartung r/(1 + r) stellt sich nur ein, wenn das Einfrieren
in der dichten Phase liegt **und** die Expansion dort noch schneller als die Drehung ist (H ≫ ω). Sonst läuft der Zustand
zum Photon P (|b| → 0, β² → 1) oder friert irgendwo dazwischen ein. Das entspricht der Kopfschätzung der Vorab-Notiz.

## B: Einstein–Cartan-Spinterm ohne Wirkung

Der Kontaktterm ändert |b_∞| in keinem der 192 Vergleiche um mehr als 1 % (höchstens 1·10⁻⁴); kein Bounce. Grund: In der dichten
Phase liegt der Zustand auf der R/T-Achse, b* = (0, −r/(1 + r)). Die axiale Dichte J_A = n b_x ist dort null, weil die Kompensator-
und Chiralitätsachse x senkrecht dazu steht. Der Spinterm sieht den Zustand gerade dann nicht, wenn die Dichte hoch genug wäre.

## C: Λ wirkt, wenn die späte Expansion mit der Drehung vergleichbar ist

Bei Λ/3 = 10⁻⁶ H₀² ändert sich |b_∞| um bis zu 18 % (Werte über 10⁻³), und zwar bei H₀ = 10³, wo die Λ-Phase H ≈ ω gibt. Λ entkoppelt
also nicht vom eingefrorenen Zustand, wenn das Einfrieren in die Λ-Phase fällt. Bei kleinerem H₀ ist der Einfluss vernachlässigbar.

## D: keine Zahl geprüft

r folgt nicht aus der Struktur; ein Vergleich von β mit dem Fenster entfällt wie vorab festgelegt.

## Numerik

Exakte Fortschreibung des linearen Systems über Schritte konstanter Raten (dt = 10⁻³/H). Kontrolle mit dt = 2,5·10⁻⁴/H: Werte über
10⁻³ ändern sich um höchstens 10⁻⁴ relativ; die sehr kleinen Werte (≲ 10⁻⁶) sind nur der Größenordnung nach bestimmt, was das Urteil
nicht berührt. Ein erster Lauf mit einem ODE-Löser in ln a war bei schnellen Drehungen zu langsam und wurde abgebrochen; er lieferte
keine Ergebnisse.

## Was daraus folgt

1. In dieser Reduktion ist β_sym nicht durch die Dynamik festgelegt. Ein eingefrorener Wert trägt die Raten- und Expansionsgeschichte
   (H₀, g n₀, Λ) in sich, wie bei jeder Relikt-Häufigkeit. Ein dimensionsloser Strukturwert folgt so nicht.
2. Der einzige parameterfreie Grenzfall ist das schnelle Einfrieren bei H ≫ ω: dann |b| = r/(1 + r), β² = 1/(1 + 2r). Das verschiebt
   das Problem auf ein Ratenverhältnis r. Der Hopf-Zustand gehört zu r = 1, der heutige Wert zu r = 1,157.
3. Der Einstein–Cartan-Kontaktterm koppelt nicht, solange Kompensator- und R/T-Achse senkrecht stehen. Eine Rückkopplung der Geometrie
   auf β bräuchte eine Kopplung an die R/T-Komponente b_z, also an den Unterschied zwischen Materie- und Tachyon-Port selbst.
4. Für die Skizze heißt das: β eher als Einzelereignis (r27, Kickwinkel 28,78°) oder als Verhältnis zweier Zählungen (r63) verstehen,
   nicht als Zustand, den eine Dynamik ansteuert.

Guards unverändert; C5, C6/T2 und globale Abschlüsse sind nicht berührt.
