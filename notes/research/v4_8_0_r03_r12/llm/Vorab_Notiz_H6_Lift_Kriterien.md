# Vorab-Notiz H6: Was unterscheidet den TM1-Lift vom θ₁₃ = 0-Lift? (Kriterienliste)

Festgelegt am 2026-10-20, **vor** der Auswertung. Bezug: K18.5 (`k22_oktonion_triplett.py`).

## Ausgangslage und Offenlegung

Über jedem Fano-Zentrum c ∈ {e₁, e₂, e₃} liegen zwei Involutionen von Stab(+e₇) ≅ Δ(96): eine gibt TM1, eine die
ausgeschlossene Spalte (0, ½, ½). Bekannt ist bereits, dass die Daten TM1 bevorzugen. Jede jetzt gefundene
Eigenschaft, die TM1 auszeichnet, wäre ohne feste Liste eine Nachhersage. Deshalb wird die Liste hier festgelegt.

Vorab bekannt (aus Theorie, nicht gerechnet): Alle Elemente von G₂ erhalten Produkt, Assoziator und
Determinante; alle Involutionen in G₂ sind konjugiert (Spur −1 auf 7 Dimensionen), alle Involutionen in SU(3)
haben Spur −1. Kriterien, die nur h allein betreffen, trennen deshalb voraussichtlich nicht. Trennen können nur
Kriterien, die h zur Triole g₃ (Zyklik e₄→e₅→e₆) in Beziehung setzen oder die Vorzeichen in einer festen Basis
betreffen.

## Kriterien (verbindlich, in dieser Reihenfolge)

Für eine Involution h und das Dreier-Element g₃:

- **A (Hauptkriterium):** h g₃ h = g₃⁻¹, d. h. h und die Triole bilden zusammen die Diedergruppe S₃.
- B: h und g₃ kommutieren.
- C: Die von g₃ und h erzeugte Gruppe hat Ordnung 24 (schließt ohne den vollen Vorzeichenkern).
- D: h wirkt auf dem Triplett (e₄, e₅, e₆) reell-monomial (keine komplexen Phasen).
- E: h permutiert das Anti-Triplett {e₁, e₂, e₃} ohne Vorzeichenwechsel.
- F: h permutiert das Triplett {e₄, e₅, e₆} ohne Vorzeichenwechsel.
- G: h kommutiert mit allen drei reinen Vorzeichenwechseln (TM2-Elementen).
- H: Die g₃-feste Richtung (Eigenwert 1) ist Eigenvektor von h.

## Verfahren (verbindlich)

- Alle Lifts der Ordnung 3 des Zyklus e₄→e₅→e₆ (mit e₇ fest) werden bestimmt. Als Companion-Lift gilt der
  vorzeichenfreie, falls es ihn gibt; sonst wird das berichtet. Die Auswertung erfolgt für jeden Lift, und es wird
  angegeben, ob das Ergebnis vom Lift abhängt.
- Für jedes Kriterium: gilt es für die TM1-Lifts, für die θ₁₃ = 0-Lifts, für beide oder für keine.

## Bewertung (verbindlich)

- Trennt **A** für den Companion-Lift zugunsten von TM1: „modellinterner Kandidat für die Auswahl von TM1“.
- Trennt A zugunsten der ausgeschlossenen Variante: „Hauptkriterium spricht gegen TM1“.
- Trennt A nicht: kein Kandidat aus dem Hauptkriterium; Nebenkriterien werden berichtet, zählen aber nur als
  Hinweise, weil bei sieben Nebenkriterien ein trennendes zufällig wahrscheinlich ist.
- Hängt die Trennung vom gewählten Lift von g₃ ab, ist die Auswahl eine Konventionsfrage und kein Befund.

Nach dem Commit dieser Notiz wird daran nichts mehr geändert.
