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

## Nachtrag 16.11.2026: Zwei Klassen und der Kollapszustand
Frage des Autors: Der Kollapszustand ist der Nullzustand; gibt es auf der untersten Ebene nur „liegt drin oder nicht“? Auftrag:
nachrechnen, die Abbildung zum Kollapszustand prüfen und mit heutigem Wissen neu beschreiben; der Autor weist darauf hin, dass
die Idee des Kollapszustands vom Anfang des Projekts stammt. **Erkundung, nicht blind.** Skript `two_classes.py`, Ausgabe
`run/two_classes_stdout.txt`.

### Vorwissen geprüft
- **k220 (7.11.2026, `../k220_ein_objekt_2026_11_07/`):** Bahnen von SO(3,ℂ) × Dualität auf z = E + iB sind die Schalen |s| = r > 0,
  der punktierte Nullkegel und {0}; M und T liegen auf einer Bahn, s = 0 ist der einzige Fixpunkt der Dualität. Kompensator und
  Mischung verlieren Information; R ≠ P.
- **Hauptkorpus (`thm:unity`, `thm:origin`, `thm:dark-offset`):** z⁻ ist die Frame-Variable; z⁻ = 0 heißt Kollapszustand, wird mit
  dem Photon und dem einzigen frame-invarianten Objekt gleichgesetzt, und „we can never fully reach z⁻ = 0“.
- **v4.9.0-r24.3:** Der „Photon-Frame“ des Hauptkorpus (Versatz null) ist der Bezugsframe R, der reine Zustand |b| = 1; das Photon P
  der Konvention F ist b = 0 und wird erst für β → 1 erreicht. |b_R|/|b_M| = γ_L.
- **`../op5_reconstruction_verdict_2026_11_06.md`:** „Null“ und „Photon“ bezeichneten sechs verschiedene Dinge; ihre Gleichsetzung
  ist keine zulässige Abkürzung.
- **v4.10.0-r11.2(f):** Das Kompensatorbild ist nicht null.

### Ergebnisse
1. **Zwei Klassen.** Nimmt man zu SO(3,ℂ) die Skala z ↦ λz mit komplexem λ ≠ 0 hinzu (Dualitätsphase und Dilatation), bilden alle
   nicht lichtartigen Felder eine einzige Bahn (2000 Paare, Residuum 2·10⁻¹⁴). Die lichtartigen Felder ≠ 0 bilden schon unter
   SO(3,ℂ) eine Bahn (2000 Paare, Residuum 3·10⁻¹²). Unter Lorentz-Gruppe, Dualität und Skala gibt es also genau zwei Klassen von
   Feldern ≠ 0, und die einzige verbleibende Aussage ist: lichtartig oder nicht.
2. **Jede Klasse hat einen ausgezeichneten Vertreter.** Ein nicht lichtartiges Feld kommt durch einen endlichen Boost in den Frame
   E ∥ B; dort ist der Boden φ = 1 (reiner Zustand). Das ist der Bezugsframe R von r24.3. Ein lichtartiges Feld hat φ = 0 in jedem
   Frame; das ist der Photonpunkt P. Unter Boosts nimmt φ in der ersten Klasse alle Werte in (0, 1] an, in der zweiten nur 0.
3. **R und P sind die beiden Enden einer Rapiditätslinie.** Für die Rapidität des Boosts nach R gilt φ = sech 2η_R. R ist η_R = 0,
   P ist η_R = ∞. Entlang des Nullaugenblicks aus r20.1 divergiert η_R (0,74; 1,33; 2,02; 2,83; 3,98 bei t = −0,6; −0,2; −0,05;
   −0,01; −0,001). Die freie Zeitentwicklung erreicht in endlicher Zeit, was Boosts erst bei unendlicher Rapidität erreichen.

### Der Kollapszustand mit heutigem Wissen (Lesart)
Der Hauptkorpus arbeitet in einem einzigen Frame (r24) und schreibt z⁻ = 0 für zwei Dinge, die heute getrennt sind:

| Rolle von z⁻ = 0 im Hauptkorpus | heutige Beschreibung |
|---|---|
| Nullpunkt des Versatzes; Ziel der Umrechnungen γ_L^(−k); Λ = 0 | **R**: φ = 1, η_R = 0; ein Frame, durch endlichen Boost erreichbar (r24.3) |
| das invariante Objekt; das Photon | **P**: φ = 0, die lichtartige Klasse, Fixpunkt der Dualität (k220); η_R = ∞ |
| „we can never fully reach z⁻ = 0“ (`thm:dark-offset`, v4.8.0-r18) | als Aussage über Erreichbarkeit passt sie zu P (kein Transport, Boosts nur im Grenzwert), nicht zu R |
| Kompensator als Projektion auf den Kollapszustand (`thm:unity` (iv)) | keines von beiden: Das Bild ist nicht null (r11.2(f)); eine Projektion verliert Information (k220) |

- **„Kollapszustand = Nullzustand“ gilt für die Rolle des invarianten Objekts.** In dieser Rolle ist er P, die lichtartige Klasse, und
  die Frage „liegt drin oder nicht“ ist genau die Klassenaussage aus Ergebnis 1.
- **Für die Rolle des Nullpunkts gilt es nicht.** Der Nullpunkt des Versatzes ist R, und R ist das Gegenteil eines Nullzustands: Der
  Boden ist dort maximal.
- **Spannung, nicht aufgelöst:** Die dritte Zeile widerspricht der Typisierung von r24.3. „Unerreichbar“ passt zu P, die Rechnungen
  mit dem Versatz (γ_L, Λ) passen zu R. Das ist ein Kandidat für einen Statusvermerk; der Hauptkorpus wird nicht umgeschrieben.

### Folge für die Brückenfrage (B2)
Trägt die unterste Ebene nur die Klassenaussage, dann ist Zugehörigkeit zu einem Augenblick der Grundbegriff: Sie ist
Lorentz-invariant (r20.1(c)); eine Dauer braucht einen Zeitparameter, den die Klassenebene nicht hat. **Der Autor hat die
Ereignis-Lesart am 16.11.2026 als Arbeitsannahme gesetzt.** Sie ist gesetzt, nicht hergeleitet. Offen bleiben (B1) und (B3).

### Grenzen
- Nur der freie Träger in Lesart B. Mit Ladungen ist die Dualität keine Symmetrie (k220), mit Massen die Dilatation nicht.
- Dass Skala und Dualitätsphase auf der untersten Ebene herausgeteilt werden, ist eine Setzung.
- Die Zuordnung der Hauptkorpus-Stellen ist eine Lesart an vier Stellen, keine Durchsicht des ganzen Hauptkorpus.
- Keine C5-Entladung; die Aussage C5 = 0 wird nicht gemacht.
