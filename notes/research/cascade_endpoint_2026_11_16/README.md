# Wohin führt die Kaskade? R oder P (offene Frage r22.4)

16. November 2026, Claude Opus 5.5. **Erkundung, nicht blind** (alle Ergebnisse stehen analytisch fest), ohne Kriterium, keine
H-Nummer. Auftrag des Autors: „weiter mit der kaskade“. Frage aus Runde r22.4: Führt die Kaskade des Hauptkorpus, die „alles zurück
zu z⁻ = 0“ projiziert, zum Bezugsframe R (reiner Zustand, φ = 1) oder zum Photonpunkt P (lichtartige Klasse, φ = 0)? Skript
`cascade_endpoint.py`, Ausgabe `run/cascade_endpoint_stdout.txt`.

## Vorwissen geprüft
- **Hauptkorpus:** Die Kaskade hat drei Beschreibungen.
  - `thm:fractal`: K̂: S_n → S_{n−1} transportiert die Nullachse L_n auf L_{n−1}; Endpunkt ist der „terminal compensated photon
    sector“ S₀.
  - `prop:horizon-cascade-singularity`: K̂ = C^μ_ν ∘ Π_J, also Kompensation nach der J-Projektion.
  - `thm:hopf` und `thm:dark-energy`: Hopf-Kette S¹⁵ → S⁸ → S⁴ → S² und Markov-Kette mit absorbierendem Zustand S²
    („photon ground state z⁻ = 0“).
- **v4.8.0-r06:** Die Nullachse von `thm:fractal` ist in Lesart B invariant als s = 0 zu definieren; ihre Richtungen bilden S₀. Der
  Transport selbst ist offen.
- **v4.8.0-r09:** Die Kette S¹⁵ → S⁸ → S⁴ → S² ist keine Verkettung von Hopf-Abbildungen.
- **v4.9.0-r10, r27, v4.10.0-r21.12(a):** „Drehen, dann kompensieren“; jeder kompensierte Zustand liegt auf der Kompensatorachse.
- **v4.9.0-r24.3, r29.1(a):** R ist der reine Zustand auf der Kompensatorachse; Λ = 0 gilt in R.
- **v4.9.0-r61.1(b):** Der Hopf-Wert liest einen reinen Zustand vom Photonpol aus, also in R.
- **v4.9.0-r28.2:** Das Feld allein stabilisiert sich nicht; mit vielen Frequenzen dephasiert es näherungsweise zum Photon. Mit einem
  nachgefüllten Tachyon-Reservoir gibt es einen eindeutigen Attraktor 0 < |b| < 1.
- **k220:** Invertible Abbildungen verbinden die lichtartige Klasse nicht mit den anderen; nur nicht umkehrbare Schritte (Projektion,
  Mischung, Grenzwert) erreichen P.

## Ergebnisse
1. **Kompensator-Kaskade (K̂ = C ∘ Π_J, Kollar-Schritt) → R.** Das Bild jedes Feldes mit E + B ≠ 0 unter der Kompensation hat φ = 1
   (2000 Felder, Abweichung 0). Sogar ein lichtartiges Feld geht nach einer Kompensation auf φ = 1. Diese Kaskade erreicht P nie; sie
   endet auf der Kompensatorachse, und das ist R (r29.1(a)). Die Hopf-Lesart und Λ = 0 gehören zur selben Seite (r61.1(b), r24.3).
2. **Nullachsen-Transport (`thm:fractal` mit r06) trägt P, führt aber nicht hin.** Lorentz-Gruppe und Dualität lassen lichtartige
   Felder lichtartig und |s| nicht lichtartiger Felder unverändert (1000 Abbildungen). Ein Transport der Nullachse von Stufe zu Stufe
   bleibt in der lichtartigen Klasse; „terminal compensated photon sector“ ist dort der Name der Klasse P, nicht das Ziel eines
   Weges aus der anderen Klasse.
3. **Offenes System (r28.2(c)) liegt dazwischen, und die Kopplung entscheidet.** Mit einem Tachyon-Reservoir unter dem Winkel θ hat der
   Zustand den Attraktor |b|∞ = sin²θ / (1 − cos²θ cos 2α). Bei α = π/6 geht er von 0,0006 (θ = 1°) über 0,40 (30°) und 0,86 (60°) bis
   1,0000 (89,9°). Schwache Kopplung führt zu P, starke zu R. Am Hopf-Punkt sin²θ = 1/3 ist |b|∞ = ½ = (1 − x)/(1 + x), wie r28
   nachträglich vermerkt hat.
4. **Viele Frequenzen ohne Reservoir (r28.2(b)) → P nur im Grenzwert.** Die mittlere Kohärenz fällt wie N^(−½) (0,64 bei N = 2,
   0,014 bei N = 4000). Das wiederholt das Uhrmodell von r28 und ist keine unabhängige Prüfung.

## Antwort auf r22.4
**Die Frage ist nicht offen, weil der Hauptkorpus schweigt, sondern weil er zwei Kaskaden unter einem Namen führt.** Ihre Endpunkte
sind genau die beiden Rollen von z⁻ = 0 aus r21.9 und r22:

| Kaskade im Hauptkorpus | Art des Schritts | Endpunkt |
|---|---|---|
| K̂ = C ∘ Π_J, Kollar-Schritt, Hopf-Kette, Markov mit Λ = 0 | selektive Projektion (Kompensator) | **R** |
| Nullachsen-Transport (`thm:fractal`, mit r06) | invertibel, klassenerhaltend | **P** wird getragen, nicht erreicht |
| Dephasierung über viele Frequenzen (r28.2(b)) | effektiv nicht umkehrbar | **P** nur im Grenzwert |
| Offenes System mit Reservoir (r28.2(c)) | Austausch | zwischen P und R, je nach Kopplung |

- „Die Kaskade projiziert alles zurück zu z⁻ = 0“ ist für die Kompensator-Kaskade eine Aussage über R: Sie macht Zustände rein, nicht
  lichtartig.
- Zum Nullzustand P führt im Bestand keine endliche Kaskade. Dahin kommen nur Grenzwerte (Boosts, Dephasierung, schwache Kopplung) oder
  die freie Zeitentwicklung für einen Augenblick (Nullaugenblick, r20.1). Das ist dasselbe Bild wie bei C5 (r21.5, r21.12).
- Die Kaskade von `thm:fractal` ist die einzige, die P von Anfang an trägt; sie entspricht dem Satz aus r21.6, dass ein bleibend
  lichtartiges Feld es von Anfang an war.

## Grenzen
- Die Zuordnung der drei Kaskaden folgt den genannten Stellen und Lesarten (r06, r10, r24, r28, r29); der Hauptkorpus definiert K̂ nicht
  einheitlich.
- Die Markov-Kette läuft auf Schichten, nicht auf Zuständen des Dubletts; ihre Zuordnung zu R folgt nur über Λ = 0 (r24.3).
- Keine neue Zahl, kein Test. OP1–OP5, C5, C6/T2 und die Guards sind unverändert.
