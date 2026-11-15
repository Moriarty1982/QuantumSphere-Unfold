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
