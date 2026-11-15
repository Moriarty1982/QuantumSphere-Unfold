# C5 frame-sauber neu gestellt

16. November 2026, Claude Fable. **Erkundung, nicht blind** (alle Rechnungen stehen analytisch fest), ohne Kriterium. Auftrag des
Autors: „C5 neu stellen“, als Antwort auf die offene Autorentscheidung aus r20.4. Keine H-Nummer, kein CT-Eintrag, kein Guard
ausgegeben. **Die verbotene Aussage C5 = 0 wird nicht gemacht; C5 bleibt offen.** Skript `restatement_checks.py`, Ausgabe
`run/restatement_checks_stdout.txt`. Festgehalten als Runde v4.10.0-r21 (`../v4_10_0_r21/`).

## Vorwissen geprüft
- **v4.7.0-r86:** C5_zero = „∄ N < ∞: Φ₅^(N) = 0“, zerlegt in (a) innerhalb der Kollar-Rekursion (negativ entschieden, r86.2) und
  (b) außerhalb (offen).
- **v4.7.0-r88:** Formen (i) und (ii) ausgeschlossen; Form (iii) offen mit (α)–(δ).
- **v4.9.0-r10:** Lesart: Inhalt = Feldinhalt des Dubletts, Score = Energie im Kompensatorport. r10.2(a): Ein isometrischer Zeuge,
  der den Kompensatorport leert, legt den Inhalt in den Partnerport und verletzt (δ). r10.2(b): Boden |s| unter Boosts.
- **v4.9.0-r19.1, r27, r28:** Photonpunkt durch Boosts nur im Grenzwert; nicht-selektiver Fluss nur im Grenzwert (außer α = π/4);
  Tachyon-Abbildung z ↦ iz tauscht die Scheiben-Ports.
- **v4.9.0-r61:** Vorbild: Frame-Audit von OP1–OP5, das OP4 als „in der jetzigen Form schlecht gestellt“ einordnet. C5 fehlte dort.
- **v4.10.0-r20:** Nullaugenblick (r20.1), Abgleich mit r88 (r20.2), Zeit gegen Kollar-Stufe (r20.3), Frame-Audit (r20.4) mit der
  Frage an den Autor, ob C5 neu gestellt wird.
- Zurückgestellte Ideen I1–I4: kein Auslöser für C5.

## Die Neufassung
Größen auf dem Dublett (E, B) von r04, mit 2u = E² + B² und s = (E + iB)²:

| Größe | Definition | Frame-Typ |
|---|---|---|
| C5_M | (1 + b_x)/2, Anteil im Kompensatorport, b_x = 2E·B/2u | Materie-Frame |
| C5_T | (1 − b_x)/2, Anteil im Partnerport | Tachyon-Frame (liest nach r28 die getauschten Ports) |
| Boden | \|s\|/2u = \|b\| | frame-frei: fest unter R, T und J_B |

Für die Kollar-Rekursion sind die kumulierten Anteile C5_M^(n) = (3/4)ⁿ und C5_T^(n) = 1 − (3/4)ⁿ (r20.4(b)). In beiden Fällen gilt
C5_M + C5_T = 1.

Die alte Frage C5_zero zerfällt in drei Fragen:

1. **Übergangsfrage (frame-typisiert), C5_tr:** Gibt es eine endliche Stufe mit C5_M = 0, also C5_T = 1?
2. **Photonpunkt-Frage (frame-frei), C5_P:** Erreicht ein nicht lichtartiger Zustand mit Inhalt ≠ 0 bei endlichem Parameter den
   Boden |s| = 0?
3. **Brückenfrage, C5_br:** Ist das Erreichen von |s| = 0 eine Entladung der Obstruktion im Sinn von r86 und r88?

## Ergebnisse
1. **Summe und Tausch.** C5_M + C5_T = 1 für jedes Feld; R tauscht die beiden Anteile; der Boden |s|/2u ist unter allen drei
   Frame-Abbildungen fest (1000 Felder, Abweichung 0).
2. **Berichtigung zu r20.4:** „Beide Anteile ½“ kennzeichnet den Photonpunkt nicht. Gleiche Anteile heißen E·B = 0; das gilt auf
   der ganzen M–T-Achse der Scheibe, auch für ein reines E-Feld (Anteile ½, Boden 1). Der Photonpunkt ist durch |s| = 0
   gekennzeichnet; gleiche Anteile sind dafür notwendig, nicht hinreichend. r20.4 nannte P den Punkt, „an dem beide Anteile ½
   sind“; das stimmt, aber nicht umgekehrt.
3. **Die Übergangsfrage ist Verlagerung.** C5_M = 0 gilt genau für E = −B. Ein solches Feld gibt es schon statisch; dort ist
   C5_T = 1 und der Boden maximal (|s| = 2u). Ein leerer Kompensatorport senkt den Boden also nicht, er verlegt den Inhalt in den
   Partnerport. Das ist r10.2(a) in typisierter Form: Wegen der festen Summe gibt es in der frame-typisierten Frage kein
   Verschwinden, nur einen Wechsel des Frames, und der fällt unter (δ). In der selektiven Rekursion tritt C5_M = 0 bei keiner
   endlichen Stufe ein (r86.2).
4. **Die Photonpunkt-Frage hat eine positive Antwort als Aussage über Felder.** Boosts und die Drehungen von Lesart B lassen |s|
   fest (r10.2, r19.1); der nicht-selektive Fluss von r27 erreicht P nur im Grenzwert (außer bei α = π/4); die freie
   Zeitentwicklung erreicht |s| = 0 zu endlicher Zeit für die Familie von Kodimension 1 aus r20.1. Die kumulierten Anteile der
   Rekursion sind bei keiner ganzzahligen Stufe gleich ((3/4)ⁿ = ½ bei n = 2,409; (3/4)² = 0,5625, (3/4)³ = 0,4219).
5. **Bleibende Null.** Das Zeitmittel von |s(t)|² ist (|s₊|² + 4|w|² + |s₋|²)/16 (300 Felder, relative Abweichung 9·10⁻¹⁶). Also
   ist s(t) = 0 für alle t genau dann, wenn s₊ = s₋ = w = 0. Die Beträge dieser drei Größen ändert die freie Zeitentwicklung nicht.
   **Ein Feld, das bleibend im Photonpunkt steht, stand dort von Anfang an** (Beispiele: ebene Wellen, zirkular und linear). Die
   freie Zeitentwicklung führt in keine bleibende Null hinein. Das Beispielfeld aus r20.1 hat Zeitmittel 0,305.

## Was daraus für die Brückenfrage folgt
Die alte offene Frage sitzt nach der Neufassung allein in C5_br. Sie hängt an drei Punkten:

- **(B1) Lesart der Obstruktion:** Obstruktion = Boden |s| des augenblicklichen Feldes (r10, r20.2). Bleibt eine Lesart.
- **(B2) Augenblick oder Dauer:** r86 fragt nach einer endlichen Stufe N mit Φ₅^(N) = 0 und sagt nicht, ob die Null danach bestehen
  muss.
  - *Ereignis-Lesart:* Ein invarianter Augenblick genügt. Dann ist der Nullaugenblick aus r20.1 ein Kandidat, abhängig von (B1)
    und (B3).
  - *Dauer-Lesart:* Die Null muss bestehen bleiben. Dann liefert die freie Zeitentwicklung nach Ergebnis 5 keinen Zeugen, und der
    Kandidat aus r20 scheidet aus.
- **(B3) Vorliegen:** Warum Felder der Familie von Kodimension 1 vorliegen sollten, ist offen (r20).

**(B2) ist eine Entscheidung des Autors.** Diese Notiz trifft sie nicht.

## Was das nicht ist
- Keine C5-Entladung. Die Aussage C5 = 0 wird nicht gemacht.
- C5_tr ist nur innerhalb der Lesart von r10 und für die Transporte von Lesart B als Verlagerung eingeordnet.
- C5_P ist eine Aussage über Felder, kein Abschluss von C5.
- OP1–OP5, C6/T2 und die Guards sind unverändert.
