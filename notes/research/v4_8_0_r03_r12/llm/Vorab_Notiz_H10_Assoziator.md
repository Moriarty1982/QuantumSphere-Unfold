# Vorab-Notiz H10: Assoziator als Auswahlkriterium für den TM1-Lift

Festgelegt am 2026-10-20, **vor** der Auswertung. Bezug: K19 (H6), K20 (H7), K23.

## Offenlegung (vor der Festlegung gerechnet)

- Assoziator [x,y,z] = (xy)z − x(yz). Für das Generationen-Tripel gilt **[e₄,e₅,e₆] = −2e₇**; für Fano-Linien
  verschwindet er, für Nicht-Linien hat er die Norm 2.
- Folgerung: Jedes Element von Stab(+e₇) ist ein Automorphismus, erhält den Assoziator und hält e₇ fest, lässt also
  [e₄,e₅,e₆] fest. Kriterien, die nur diesen Assoziator benutzen, trennen nicht (Kriterium S3 unten ist deshalb nur
  Kontrolle).
- Bekannt: Die Daten (JUNO 2026) disfavorisieren TM1 inzwischen (K23). Die Auswahlfrage ist damit weniger dringend,
  wird aber wie geplant geprüft.

## Kriterien (verbindlich)

Für eine Involution h (TM1-Lift bzw. θ₁₃ = 0-Lift relativ zum gewählten Triolen-Lift g₃), Triplett-Basis e₄, e₅, e₆:

- **S1 (Haupt):** [x, h(x), e₇] = 0 für alle x ∈ {e₄, e₅, e₆} („h ist assoziativ gegenüber dem Kaskaden-Ende“).
- S2: Für die erhaltene Spalte w = w_R + J w_I (J = Linksmultiplikation mit e₇) verschwindet [w_R, w_I, e₇]; bei
  w_I = 0 wird [w_R, J w_R, e₇] genommen.
- S3 (Kontrolle): h([e₄,e₅,e₆]) = [e₄,e₅,e₆].
- S4: Die feste quaternionische Teilalgebra von h schneidet span(e₄,e₅,e₆) in einer Geraden, die die g₃-feste
  Richtung des Tripletts enthält.

Ausgewertet für alle vier Lifts von g₃.

## Bewertung (verbindlich)

- S1 trennt zugunsten TM1 für alle Lifts: „Assoziator ist modellinterner Kandidat für die Auswahl“.
- S1 trennt nicht oder zugunsten θ₁₃ = 0: kein Auswahlgrund aus dem Assoziator; S2, S4 nur Hinweise.
- Lift-Abhängigkeit: Konventionsfrage, kein Befund.

Nach dem Commit dieser Notiz wird daran nichts mehr geändert.
