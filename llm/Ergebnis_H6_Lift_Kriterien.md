# Ergebnis H6: Was unterscheidet den TM1-Lift vom θ₁₃ = 0-Lift?

Vorab-Notiz: `Vorab_Notiz_H6_Lift_Kriterien.md`, Commit e1e2393 (2026-10-20 03:34 UTC), vor der Auswertung.
Skript: `k23_test_h6.py`. Kriterien und Bewertung unverändert.

## Lifts der Triole

Der Zyklus e₄→e₅→e₆ (e₇ fest) hat 4 Lifts der Ordnung 3. Einer ist vorzeichenfrei (e₄→e₅→e₆, e₁→e₃→e₂→e₁ bis
auf Vorzeichen: e₁→−e₃, e₂→−e₁, e₃→+e₂); er gilt als Companion-Lift. **Alle Ergebnisse sind für alle 4 Lifts
gleich**, also keine Konventionsfrage.

## Kriterien

| Kriterium | TM1-Lifts | θ₁₃ = 0-Lifts | trennt zugunsten |
|---|---|---|---|
| **A (Haupt): h g₃ h = g₃⁻¹ (Diedergruppe S₃)** | nein | ja | **θ₁₃ = 0** |
| B: kommutiert mit g₃ | nein | nein | — |
| C: ⟨g₃, h⟩ hat Ordnung 24 | ja (≅ S₄ nach Ordnungsstatistik) | nein (Ordnung 6, S₃) | TM1 |
| D: reell-monomial auf dem Triplett | ja | ja | — |
| E: Anti-Triplett ohne Vorzeichen | nein | nein | — |
| F: Triplett ohne Vorzeichen | nein | nein | — |
| G: kommutiert mit Vorzeichenwechseln | nein | nein | — |
| H: g₃-feste Richtung ist Eigenvektor | nein | ja | θ₁₃ = 0 |

## Urteil nach der festgelegten Bewertung

**Das Hauptkriterium spricht gegen TM1.** Die Spiegelung, die mit der Triole die kleinste gemeinsame Struktur
bildet (S₃), ist die ausgeschlossene Variante mit θ₁₃ = 0. Das Nebenkriterium C trennt zugunsten von TM1, zählt
nach der Regel aber nur als Hinweis.

## Einordnung

- A und C sind zwei Seiten derselben Sache: Entweder schließt die Spiegelung mit der Triole zur kleinen Gruppe
  S₃ (Minimalität), oder sie erzeugt mit ihr die volle Gruppe S₄, also den ganzen Fano-Punkt-Stabilisator
  (Vollständigkeit). Die Natur wählt, wenn TM1 stimmt, die zweite Möglichkeit.
- Dass die minimale Wahl θ₁₃ = 0 gibt, ist bekannt: Triole plus μ-τ-Spiegelung führt auf tribimaximale Struktur.
  Gerade diese ist seit 2012 widerlegt. Ein Prinzip „minimale Symmetrie“ wäre also schon empirisch falsch.
- C als Prinzip („Triole und Restsymmetrie erzeugen die volle Punkt-Symmetrie der Fano-Ebene“) ist nachträglich
  gefunden. Es kann nur dann zählen, wenn es sich aus dem Modell begründen lässt, ohne auf TM1 zu schielen.

## Status

[S] H6: Hauptkriterium spricht gegen TM1; kein modellinterner Auswahlgrund aus A. Hinweis aus C: TM1 ⇔
⟨Triole, Restspiegelung⟩ = S₄. Guards unberührt.
