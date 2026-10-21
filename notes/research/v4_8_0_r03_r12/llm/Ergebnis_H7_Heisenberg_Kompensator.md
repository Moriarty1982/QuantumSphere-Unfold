# Ergebnis H7: Wählt der Heisenberg-Kompensator zwischen TM1-Lift und θ₁₃ = 0-Lift?

Vorab-Notiz: `Vorab_Notiz_H7_Heisenberg_Kompensator.md`, Commit e6da7db (2026-10-20 03:45 UTC), vor der Rechnung.
Skript: `k25_test_h7.py`. Kriterien und Bewertung unverändert.

## Ergebnisse (alle vier Triolen-Lifts identisch)

| J (feste Linie) | Typ | K4: J kommutiert mit Triole | K1 TM1 / θ₁₃=0 | K2 TM1 / θ₁₃=0 | K3 TM1 / θ₁₃=0 |
|---|---|---|---|---|---|
| (2,5,7) | Haupt | nein | 1/3 / 1/3 | 1/3 / 1/3 | keine / keine |
| (3,4,7) | Haupt | nein | 1/3 / 1/3 | 1/3 / 1/3 | keine / keine |
| (1,6,7) | Neben | nein | 1/3 / 1/3 | 1/3 / 1/3 | keine / keine |
| (1,4,5), (2,4,6), (3,5,6) | Neben | nein | 1/3 / 1/3 | n/a (antilinear) | n/a |
| (1,2,3) | Neben | **ja** | alle / alle | n/a (antilinear) | n/a |

## Urteil nach der festgelegten Bewertung

**K1 trennt nicht** (für kein J und keinen Lift); K2 und K3 trennen ebenfalls nicht. Die strukturelle Erwartung aus
der Notiz ist bestätigt: TM1- und θ₁₃ = 0-Lift unterscheiden sich um ein Element der abelschen Vorzeichengruppe und
verhalten sich gegenüber jedem Vorzeichen-Automorphismus gleich.
**Kein Auswahlgrund aus dem Heisenberg-Kompensator.**

## Nebenbefunde (M)

- Die beiden Haupt-Kandidaten für J (negieren e₁, halten e₇) kommutieren **nicht** mit der Triole. Ein Kompensator
  dieser Form ist mit der ℤ₃-Struktur der Generationen nicht verträglich.
- Der einzige Vorzeichen-Automorphismus, der mit der Triole kommutiert, hält die Linie (1,2,3) fest und negiert
  e₄…e₇: das ist die **Cayley–Dickson-Involution** p + qℓ ↦ p − qℓ der Companion-Konvention. Sie kommutiert mit
  allen vier Triolen-Lifts und allen sechs TM1- und θ₁₃ = 0-Involutionen (24 von 96 Elementen von Stab(+e₇)),
  negiert aber e₇ und wirkt auf dem Generationen-Triplett **antilinear**, also wie eine CP-artige Transformation.

## Einordnung

- Der Kompensator in seiner bisherigen Form (e₁-Spiegelung, als Automorphismus repariert) liefert keine Auswahl
  und passt nicht zur Triole.
- Die Cayley–Dickson-Involution ist ein neuer, modellinterner Kandidat, aber für eine andere Rolle: als
  verallgemeinerte CP-Symmetrie. In der Literatur legt eine solche Symmetrie zusammen mit einer Restspiegelung die
  CP-Phasen fest. Ob das hier δ_CP vorhersagt, wäre eine **neue** Hypothese (H8) und braucht eine eigene
  Vorab-Notiz.

## Status

[S] H7: kein Auswahlgrund aus dem Kompensator. Nebenbefund: Cayley–Dickson-Involution als CP-artige Symmetrie,
verträglich mit Triole und beiden Lifts. Guards unberührt.
