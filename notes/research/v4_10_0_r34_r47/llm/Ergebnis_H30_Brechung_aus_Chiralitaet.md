# Ergebnis H30: Die Brechung der Spiegelung ρ folgt aus der Chiralität; die Triality τ bleibt, Mischung ist nicht erklärt

Vorab-Notiz: `Vorab_Notiz_H30_Brechung_aus_Chiralitaet.md`, Commit d755a08 (2026-10-23 21:26 MESZ), vor der Rechnung. Vorab analytisch offengelegt:
c L_{e₇} c = −R_{e₇}. Skript `k86_test_h30.py`, Ausgabe `k86_out.txt`.

## Ergebnisse

| Hypothese | Ergebnis | Befund |
|---|---|---|
| H30a ρ tauscht links/rechts | **bestätigt** | c L_{e₇} c = −R_{e₇}, c R_{e₇} c = −L_{e₇}; das reine Vertauschen (x, z, y) ist keine Symmetrie von t, die Transposition enthält notwendig c |
| H30b Modell I | **bestätigt** | Von den sechs Symmetrien von t erhalten genau 1, τ, τ² die Chiralität; ρ, τρ, τ²ρ bilden sie auf die anomale Wahl ½(1 − iR_{e₇}) ab |
| H30c Modell II, τ | **bestätigt** | (L_{e₇}, L_{e₇}, L_{e₇}) liegt nicht in 𝔤; die Fortsetzung von A = L_{e₇} ist (L_{e₇}, R_{e₇}, −L_{e₇} − R_{e₇}), nicht τ-invariant |
| H30d Modell II, Generationen | **bestätigt** | Platz 2 bekommt iR_{e₇} (anomal), Platz 3 −i(L_{e₇} + R_{e₇}), keine Involution |

## Einordnung

1. **Die Brechung von ρ folgt aus der Struktur.**
   - Die Transpositions-Symmetrie der Triality-Form enthält notwendig die Oktonion-Konjugation.
   - Die Konjugation tauscht Links- und Rechtsmultiplikation.
   - Die Anomaliefreiheit hat links gewählt (r43).
   - Also kann ρ keine Symmetrie der chiralen Theorie sein. Daran ändert auch die Kombination mit dem Frame-Wechsel T nichts, denn T ändert
     nur das Vorzeichen, nicht die Seite.
   - Damit ist die Bedingung aus r44 strukturell erfüllt: Die Kopplungen auf den Plätzen sind im Allgemeinen ρ-asymmetrisch. Es gibt drei
     verschiedene Massen in Brannen-Form, und die Widerlegungen von H11 und H16 bis H18 erklären sich dadurch, dass jene Potentiale die
     Chiralität nicht kannten.
   - Nicht festgelegt ist, **wie stark** ρ gebrochen ist, also die Phase θ und das Verhältnis |b|/a.
2. **Die Triality τ bleibt erhalten**, aber nur in Modell I, in dem die drei Plätze gleiche Kopien mit gleicher Chiralität sind:
   - Die mit der Triality mitgehende Chiralität (Modell II) scheitert. Platz 2 wäre anomal, Platz 3 hätte gar keine Chiralität.
   - Konsequenz für r37: Die Generationen können nicht die drei **inäquivalenten** Triality-Darstellungen (Vektor, zwei Spinoren) mit
     eigener Chiralität sein. Sie müssen äquivalente Kopien sein, und τ wirkt als Vertauschung der Kopien.
   - Die Triality-Form bleibt Träger der ℤ₃, aber die Inäquivalenz der Plätze ist mit der Chiralität nicht verträglich. Das passt zu den
     gleichen Quantenzahlen aller Generationen.
3. **Mischung bleibt offen.** In Modell I ist τ erhalten, und nach r44 gibt es dann keine Mischung. Die Chiralität bricht τ nicht in
   verträglicher Weise; die Brechung für die Mischung muss aus einer anderen, schwächeren Quelle kommen.
4. **Reihenfolge der Brechungen**, wie sie sich jetzt aus der Struktur ergibt:
   - Die Chiralität (Anomaliefreiheit, links) bricht ρ zwingend. Das gibt die Massenaufspaltung.
   - τ bleibt, also gibt es zunächst keine Mischung.
   - Die Mischung verlangt eine zusätzliche Brechung von τ, die die Struktur bisher nicht liefert.
