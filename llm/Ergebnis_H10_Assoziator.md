# Ergebnis H10: Assoziator als Auswahlkriterium für den TM1-Lift

Vorab-Notiz: `Vorab_Notiz_H10_Assoziator.md`, Commit a6b5bcb (2026-10-20 13:00 UTC), vor der Auswertung.
Skript: `k27_test_h10.py`. Kriterien und Bewertung unverändert.

## Ergebnisse (alle vier Triolen-Lifts identisch)

| Kriterium | TM1-Lifts | θ₁₃ = 0-Lifts | trennt |
|---|---|---|---|
| S1 (Haupt): [x, h(x), e₇] = 0 für x ∈ {e₄, e₅, e₆} | keine | keine | nein |
| S2: [w_R, J w_R, e₇] = 0 für die erhaltene Spalte | alle | alle | nein |
| S3 (Kontrolle): h erhält [e₄,e₅,e₆] = −2e₇ | alle | alle | nein (wie erwartet) |
| S4: feste Teilalgebra ∩ Triplett enthält die g₃-feste Richtung | keine | keine | nein |

Die feste quaternionische Teilalgebra jeder Involution ist dreidimensional und schneidet das Triplett in genau
einer Geraden.

## Urteil nach der festgelegten Bewertung

**Kein Auswahlgrund aus dem Assoziator.** S1 trennt nicht; die Nebenkriterien ebenfalls nicht.

## Einordnung

- Strukturbefund (M): Der Assoziator des Generationen-Tripels ist −2e₇. Die Nicht-Assoziativität der drei
  Generationen zeigt genau auf das SU(3)-Singulett, das Ende der Kaskade und die komplexe Struktur der Lesart B.
- Damit ist die Liste der modellinternen Auswahlkandidaten erschöpft: Minimalität (H6), Kaskade (K19.3),
  Kompensator (H7) und Assoziator (H10) wählen den TM1-Lift nicht. Nach JUNO 2026 ist TM1 zudem selbst
  disfavorisiert (K23), sodass die Auswahlfrage an Gewicht verloren hat.

## Status

[S] H10: kein Auswahlgrund. Strukturbefund [e₄,e₅,e₆] = −2e₇. Guards unberührt.
