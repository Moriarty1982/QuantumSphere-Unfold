# C5, Form (iii): Ein Nullaugenblick der Feldinvariante

15. November 2026, Claude Opus. **Erkundung, nicht blind**, ohne Kriterium. Auftrag des Autors: „C5 angehen“, dann
„Ja, prüfen“. Keine H-Nummer, kein CT-Eintrag, kein Guard ausgegeben. **Die verbotene Aussage C5 = 0 wird nicht gemacht.**
Skript `null_instant.py`, Ausgabe `run/null_instant_stdout.txt`.

## Vorwissen geprüft
- **v4.7.0-r86:** C5_zero hieß „∄ N < ∞: Φ₅^(N) = 0“. Innerhalb der Kollar-Rekursion Φ ↦ ¾Φ ist das negativ entschieden
  (Φ^(n) = (¾)ⁿ > 0); C5_det/eff gilt bei θ = 1/256, n = 20. Offen ist, ob es außerhalb der Rekursion einen Weg gibt.
- **v4.7.0-r88:** Form (i) (abziehender Kanal) und (ii) (Abbruch) sind ausgeschlossen. Offen ist **Form (iii)** mit den
  Anforderungen (α) Verschwinden der Obstruktion selbst, nicht Kleinheit des Scores; (β) unabhängig von U₅^bd; (γ) verträglich
  mit C5_det/eff; (δ) kein Import des All-Readout-Slots.
- **v4.9.0-r10:** Lesart des Autors: Der C5-Inhalt ist der Feldinhalt des Dubletts, der Score seine Energie im
  Kompensatorport; die Obstruktion verhält sich wie die Invariante s. Die Transporte von Lesart B erhalten s; ein Zeuge
  bräuchte Dynamik.
- **v4.9.0-r19.1:** Das Photon wird durch keinen endlichen Boost erreicht, nur im Grenzwert.
- **v4.9.0-r27:** Ein Modell aus Dualitätsdrehung und Kompensatormessung ändert s, gibt aber keine endliche Null des Scores;
  bei α = π/4 erreicht ein nicht-selektiver Schritt b = 0, nutzt dafür beide Ports.
- **v4.10.0-r16.8:** Für zeitharmonische Felder ist s(t) = ¼[s₊e^{−2iωt} + 2w + s̄₋e^{2iωt}], eine Ellipse um w/2.
- Zurückgestellte Ideen I1–I4: kein Auslöser für C5.

## Ergebnisse
1. **Nullaugenblicke existieren.** Mit Ê = (1, 0, 0,3i), B̂ = (0,7i, 1, 0) ist der Zustand nicht lichtartig (s₊ = −1, s₋ = 1,8,
   w = −0,4), aber zur Zeit t = 0 ist s(0) = 0 exakt, bei |z(0)| = 1,41 ≠ 0. Die Ellipse von s(t) geht durch 0; der
   Nullaugenblick wiederholt sich nach jeder halben Periode.
2. **Nicht generisch.** Für zufällige komplexe Amplituden geht die Ellipse im Allgemeinen nicht durch 0 (Median des relativen
   Abstands 0,15); es ist eine Bedingung von Kodimension 1.
3. **Invariantes Ereignis.** s ist zu jedem Zeitpunkt ein Lorentz-Skalar; ein Boost der augenblicklichen Felder lässt s = 0
   (200 Boosts, höchstens 4·10⁻¹⁵).
4. **Im Nullaugenblick steht der Zustand im Photonpunkt.** Der Stokes-Vektor der Scheibe (r04) ist dort b = 0, der Punkt P; der
   Kompensatoranteil ist ½, **nicht 0**. Die freie Zeitentwicklung erreicht P also zu einer endlichen Zeit, anders als Boosts
   (r19.1) und als der nicht-selektive Fluss von r27 (dort nur im Grenzwert, außer bei α = π/4).
5. **Trivialer Fall ausgeschlossen:** Bei reellen gleichphasigen Amplituden ist der Nullaugenblick eine Nullstelle des ganzen
   Feldes (|z| = 0) und kein Zeuge.

## Abgleich mit (α)–(δ)
| Anforderung | Befund |
|---|---|
| (α) Obstruktion selbst, nicht Score | erfüllt, **wenn** die Obstruktion die augenblickliche Invariante s(t) ist; die Zustandsinvarianten s₊, s₋, w verschwinden nicht, und der Score ist im Nullaugenblick ½ |
| (β) unabhängig von U₅^bd | erfüllt: freie Zeitentwicklung, nicht die Kollar-Rekursion |
| (γ) verträglich mit C5_det/eff | kein Widerspruch gefunden: die Detektoraussage betrifft den Kollar-Score |
| (δ) kein All-Readout-Import | erfüllt: ein Feld, eine Auslesung, kein zweiter Port |

## Was daraus folgt und was nicht
- Unter der Lesart von r10 (Obstruktion ~ s) liefert die freie Maxwell-Zeitentwicklung eines nicht generischen
  zeitharmonischen Feldes ein Objekt, das (α)–(δ) **formal** zu einer endlichen Zeit erfüllt. Das ist die Art von Dynamik, die
  r10.2 verlangt hat, und sie kommt ohne Messung aus.
- **Es ist keine C5-Entladung.** Vier Lücken bleiben:
  1. Ob die Obstruktion an der augenblicklichen Invariante s(t) hängt oder an den Zustandsgrößen (s₊, s₋, w), ist nicht
     geklärt; r10 ist eine Lesart.
  2. Die Null ist ein Augenblick und kehrt periodisch wieder; r86 fragt nach einer endlichen Stufe N, legt aber nicht fest,
     ob die Null danach bestehen muss.
  3. Eine Zuordnung von Zeitpunkten zu Kollar-Stufen fehlt.
  4. Die Felder sind nicht generisch (Kodimension 1); warum gerade sie vorliegen sollten, ist offen.
- C5 bleibt offen; Form (iii) bleibt offen, hat jetzt aber einen benannten Kandidaten mit benannten Lücken.

OP1–OP5, C5, C6/T2 und die Guards sind unverändert.

## Nachtrag 15.11.2026: Lücke 1 – augenblicklich oder Zustandsgröße?
Auftrag des Autors: „weiter“. **Lesart, aus dem Quelltext, nicht gerechnet.**

- **Lesart B ist augenblicklich.** v4.9.0-r05.2(a): „At a point, E and B are real, so the state matrix of r04 has no σ_y part
  anywhere.“ Der Dublett-Zustand von r04, auf den r10 den C5-Inhalt legt, ist also das reelle Feld in einem Punkt und zu einem
  Zeitpunkt. Komplexe Amplituden und Zeitmittel kommen erst in r05.2(b) dazu, als andere Beschreibung.
- **Die Obstruktion von r10 ist der Boden |s|.** r10.2(b) begründet die Obstruktion damit, dass der Inhalt E² + B² unter
  Boosts den positiven Boden |s| nicht unterschreitet; r10.2(c) sagt, dass ein lichtartiges Feld (s = 0) diesen Boden nicht hat.
  Gemeint ist das s des augenblicklichen reellen Feldes.
- **Folge für (α):** Im Rahmen der Lesart von r10 ist die maßgebliche Größe das augenblickliche s(t), nicht die
  Zustandsinvarianten s±, w der komplexen Beschreibung. Im Nullaugenblick ist dieser Boden exakt 0, während Inhalt und
  Score positiv bleiben (Score ½ des Inhalts). **Lücke 1 ist damit innerhalb der Lesart von r10 zugunsten von (α)
  geschlossen;** die Lesart selbst bleibt eine Lesart (r10: „an interpretation … not a derivation“).
- **Was das nicht ändert:** Der Inhalt fällt im Nullaugenblick nicht auf 0; ein Boost könnte ihn dort nur im Grenzwert
  leeren (r10.2(c)). Offen bleiben die Lücken 2 bis 4: periodische statt bleibende Null, keine Zuordnung zu Kollar-Stufen,
  nicht generische Felder. Keine C5-Entladung; die Aussage C5 = 0 wird nicht gemacht.

## Nachtrag 15.11.2026: Lücke 3 – Zeitpunkte und Kollar-Stufen
Auftrag des Autors: „weiter“. **Erkundung, nicht blind** (analytisch absehbar). Skript `time_vs_stage.py`, Ausgabe
`run/time_vs_stage_stdout.txt`.

Eine Kollar-Stufe ist nach r10.1 und r27 eine Dualitätsdrehung (um π/6) mit anschließender Kompensation. Die Dualität dreht die
beiden Helizitätsanteile gegenläufig (F₊ ↦ e^{−iα}F₊, F₋ ↦ e^{iα}F₋), die Zeitverschiebung gleichläufig.

1. **Zeit und Dualität fallen nur bei reiner Helizität zusammen.** Ist F₋ = 0, so ist z(t) = e^{−iωt} z(0): Die Zeitentwicklung
   ist dann genau eine Dualitätsdrehung, und Zeitpunkte ließen sich als Stufen zählen.
2. **Gerade diese Felder haben keinen Nullaugenblick.** Bei reiner Helizität ist |s(t)| konstant (im Beispiel 2,575); s(t) wird
   nie null, außer das Feld ist von Anfang an lichtartig.
3. **Felder mit Nullaugenblick tragen beide Helizitäten** (im Beispiel |F₊| = 1,09, |F₋| = 2,00), und ihre Zeitentwicklung ist
   keine Dualitätsdrehung: Gegen die jeweils beste Drehung bleibt ein relativer Rest von im Median 0,49.

**Folgerung:** Lücke 3 lässt sich nicht schließen, indem man Zeit mit Kollar-Stufen gleichsetzt. Das ist keine Schwäche des
Kandidaten, sondern genau die Unabhängigkeit, die (β) verlangt: Der Nullaugenblick entsteht nur, wo die Zeitentwicklung aus der
Kollar-Dynamik herausfällt. Damit bleibt aber auch offen, wie ein Zeitpunkt als „endliche Stufe N“ im Sinn von r86 zu zählen
wäre. Keine Entladung; die Aussage C5 = 0 wird nicht gemacht.

## Nachtrag 15.11.2026: Frame-Audit von C5
Auftrag des Autors: „Ja, Frame-Audit von C5 als Erkundung“, nach der Frage, ob bei C5 wieder der falsche Frame genommen oder pro
Frame untersucht werden müsse. **Erkundung, nicht blind.** Skript `frame_audit.py`, Ausgabe `run/frame_audit_stdout.txt`.
Vorbild ist das Frame-Audit von OP1–OP5 (v4.9.0-r61), das C5 nicht geprüft hat.

**Vorwissen:** v4.7.0-r02/r04 führen C5 als „endliche Witness-Fit-Schnittstelle“ eines Feldgleichungsprogramms ein; der Score
3/4 ist ein deklarierter Tabellenwert (r94). Die physikalische Lesart (Kompensatorinhalt des Dubletts, „drehe um π/6, dann
kompensiere“) stammt aus v4.9.0-r10/r16/r27. **v4.9.0-r28** hat den Frame-Fehler von r27 bereits berichtigt: Die
Tachyon-Abbildung ist z ↦ iz (nicht J_B); sie kehrt den ganzen Stokes-Vektor um und tauscht die Kompensatorports; J_B lässt die
Ports fest (C_HC = ½(1 + J_B)). Die Ergebnisse von r27 änderten sich dadurch nicht.

**Ergebnisse**
1. **Zwei verschiedene Port-Begriffe.** Die Kompensatorports von r04–r28 liegen auf der σ_x-Achse der Scheibe, also auf der
   Seite sign(E·B). Die Ports von r42/r51 (½(1 + iL_e7)) entsprechen nach r16.2(b) den σ_y-Polen, der Helizität. Unter den
   Frame-Abbildungen verhalten sie sich verschieden:

   | Abbildung | Scheiben-Ports (C5) | algebraische Ports (r51) |
   |---|---|---|
   | R (Tachyon) | getauscht | fest |
   | T (Zeitumkehr) | getauscht | getauscht |
   | J_B | fest | getauscht |

   Das Wort „Kompensator“ bezeichnet also in der C5-Lesart eine andere Achse als in r42/r51. Das ist eine Begriffsmischung,
   keine Rechenfehler; sie sollte beim Lesen von C5 beachtet werden.
2. **Die Kollar-Rekursion pro Frame.** M liest den Kompensatorport und sieht (3/4)ⁿ. Der Tachyon-Frame liest nach r28 die
   getauschten Ports, also den Partnerport, und sieht 1 − (3/4)ⁿ. Die Summe ist bei jeder Stufe 1. **„C5 = 0“ in der alten Form
   heißt pro Frame: Der Tachyon-Frame liest den ganzen Inhalt.** Die Frage ist also kein Verschwinden, sondern ein
   vollständiger Wechsel des Inhalts in den anderen Frame. Endlich geht das nur durch die Vierteldrehung, die C4, C6 und (δ)
   sperren (r12.2(c), r10.2(a)).
3. **Der Nullaugenblick pro Frame.** Beim Beispielfeld steigt der Kompensatoranteil von M durch den Nullaugenblick von 0,29 über
   0,50 auf 0,71, der des Tachyon-Frames fällt entsprechend. Im Nullaugenblick sind beide gleich (½): Der Zustand steht im
   Photonpunkt, wo kein Frame bevorzugt ist. Kein Frame-Score wird null.

**Folgerungen**
- **C5 ist in der alten Form wie OP4 frame-gemischt gestellt.** „Der Score wird endlich null“ fragt in der Messung eines Frames
  nach einem Vorgang zwischen zwei Frames. Frame-sauber sind die Anteile C5_M und C5_T mit fester Summe; die alte Null heißt
  C5_T = 1.
- **Frame-freies Gegenstück** ist der Photonpunkt P, an dem beide Anteile ½ sind. Ihn erreicht die freie Zeitentwicklung zu
  endlicher Zeit (Nullaugenblick), die selektive Rekursion nie, der nicht-selektive Fluss von r27 nur im Grenzwert (außer bei
  α = π/4).
- **Die Einordnung des Nullaugenblicks ändert sich:** Er ist kein Kandidat für „Score = 0“, sondern für „Boden |s| = 0“, und
  dieser Boden ist frame-frei (R bildet s auf −s ab). Mit (α) aus r88 („Obstruktion selbst, nicht Score“) passt das zusammen.
- Ob C5 neu gestellt wird (etwa als Frage nach dem endlichen Erreichen von P), ist eine Entscheidung des Autors. Die verbotene
  Aussage C5 = 0 wird nicht gemacht.
