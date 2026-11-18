# OP1: Welche Prämisse teilen die Begründungen der Zuordnung DL → M, ABCK → T? (Erkundung, keine Rechnung)

18. November 2026. Auftrag des Autors: „Gemeinsame Prämisse“ (nach der Zufallsabschätzung `../chance_estimate_2026_11_18/`: Die Treffer tragen nur,
wenn die Zuordnung datenfrei begründet ist). Keine Rechnung, keine H-Nummer. Alle Wege sind nachträglich gefunden; hier wird nur geordnet, was sie
voraussetzen. Der QAM-Server `qsc-qam` und die lokale QAM-Datenbank waren nicht verfügbar; Grundlage sind die Notizen unten und die Annahmenliste r08 (Z1).

## Vorwissen geprüft (die Wege)
| Weg | Quelle | Stand im Repo |
|---|---|---|
| W1 Prinzip P (Unschärfe P1, Energie P2) | `../v4_10_0_r09/Erkundung_Zaehlregel_Prinzip.md` | P2 trägt nicht (`../v4_10_0_r10/Erkundung_Bruecke_P2_Unruh.md`): über das erste Gesetz zählen M und T gleich |
| W2 Irreduzibilität (r17.3) | `../op1_frame_irreducibility_2026_11_15/` | braucht (A) = (S1); (A) ist keine Gleichheit der Gruppen, braucht eine Verriegelung (`../op1_s1_check_2026_11_16/`) |
| W3 masselose Querung (S1′) | `../op1_s1_check_2026_11_16/`, `../op1_u1_check_2026_11_16/` | begründet U1 + U2 zusammen; unter (S1′) fällt (A); passt nicht zum isolierten Horizont (`../op1_flux_lines_2026_11_17/`) |
| W4 Moran-Lesart, Dimensionsleiter | `../op1_moran_geometry_2026_11_17/` | Maximalitätsprinzip nachträglich; kein blinder Test; von (H)/(B) unberührt |
| W5 T zählt Querungen, eine Querung ein Strang (r24.4) | `../op1_i1_crossing_2026_11_16/` | braucht „eine Querung = ein Quant“ (CT-002) |
| W6 I1: T zählt Endpunkte offener Strings | `../op1_i1_string_endpoints_2026_11_15/` | Chan–Paton und „T = String-Sektor“ angenommen (CT-004) |
| (Entropie) | `../op1_entropy_count_2026_11_17/` | erklärt P und R, nicht M; trägt zur Zuordnung nichts bei |

Dazu: Annahmenliste `../v4_10_0_r08/Annahmenliste_Companion.md`, Z1 (Kategorie R, am stärksten belastete Annahme); r10: Z1 ist gleichwertig mit einem
frame-abhängigen Flächenquantum γ_M/γ_T = γ_L; H104: Bei freiem Flächenspektrum trifft ein zweites Paar dieselben Fenster;
`../op1_two_readings_2026_11_17/`: Lesart (B) der Registerbreite gibt den Bestand wieder, (H) nicht.

## Was jede Begründung leisten muss
Die Regel DL/M für M ist (alle Spins, Gewicht 2); ABCK für T ist (nur j = ½). Eine Begründung braucht vier Bausteine:
- **K0 Spektrum:** Fläche einer Punktierung ∝ √(j(j+1)) (Literatur).
- **K1 M, Gewicht 2:** je Spin genau zwei Zustände.
- **K2 M, alle Spins:** kein Spin ausgeschlossen.
- **K3 T, nur j = ½.**

## Welcher Weg welchen Baustein liefert
| Baustein | W1 | W2 | W3 | W4 | W5 | W6 |
|---|---|---|---|---|---|---|
| K0 | gesetzt | gesetzt | gesetzt | gesetzt (Prinzip nur damit eindeutig) | gesetzt | gesetzt |
| K1 | P1: Robertson-sättigend = m = ±j | invariantes Extremdublett m = ±j | Helizität masseloser Quanten: ±j | g = 2 als größte ganze Kopienzahl in der Ebene | – | – |
| K2 | P2 (alle Stufen zugänglich), **getragen nicht** | keine Einschränkung genannt | jeder Spin als masseloses Quant | „maximal“ | – | – |
| K3 | P2 (Tachyon-Boden), **getragen nicht** | T irreduzibel, braucht (A) | – | reichste Regel auf der Linie | eine Querung = ein Strang | Fundamentaldarstellung |

## Befund
1. **K0 ist allen gemeinsam.** Jede Begründung setzt das Spektrum √(j(j+1)) fest. Mit freiem Spektrum gibt es ein zweites passendes Paar (H104), und
   die Moran-Lesart ist nur mit diesem Spektrum eindeutig. Das ist Literatur, keine Projektannahme, aber ein gemeinsamer Punkt, an dem alles hängt.
2. **Für K1 gibt es einen gemeinsamen Kern: dieselbe Zustandsmenge.** W1, W2 und W3 wählen genau die Zustände |j, ±j⟩, nur aus verschiedenen Gründen
   (Unschärfe, Invarianz, Helizität). Mathematisch ist das eine Menge mit drei Kennzeichnungen. Die gemeinsame Prämisse ist also **U2: M liest nur die
   Extremzustände einer Punktierung.** Strittig ist allein, warum. W4 verlangt nur die Zahl 2, nicht diese Zustände; es verträgt sich mit U2, braucht es
   aber nicht.
3. **Für K2 gibt es keinen eigenen Grund.** Die Wege nehmen „alle Spins“ entweder als Maximalität an (W1, W4) oder schließen nur nichts aus (W2, W3).
   Der einzige ausdrückliche Grund (P2) trägt nach r10 nicht.
4. **Für K3 gibt es keine gemeinsame Prämisse.** Fünf Wege geben fünf verschiedene Gründe für j = ½ (Boden, Irreduzibilität, Linie, eine Querung,
   Fundamentaldarstellung). Zwei davon sind im Repo schon belastet: P2 trägt nicht (r10), und (A) fällt, sobald (S1′) gilt. W3 und W2 stützen sich also
   nicht gegenseitig, sondern schließen sich teilweise aus: W3 begründet K1 am besten und nimmt W2 den Grund für K3.
5. **Ein gemeinsames Prinzip für M und T zugleich liefert nur W4** (Dimension 2 gegen 1, je maximal). Die Zuordnung Frame ↔ Dimension ist dort aber
   gesetzt. Der zweite Kandidat für ein gemeinsames Prinzip, die Energie (W1, P2), ist widerlegt.

## Ergebnis in einem Satz
Es gibt **keine einzelne gemeinsame Prämisse.** Die Zuordnung ruht auf drei getrennten Lesarten: U2 für M (gemeinsamer Kern dreier Wege),
„M zählt alle Spins“ (nur als Maximalität) und „T zählt nur j = ½“ (fünf verschiedene, teils unverträgliche Gründe). Dazu kommt das Spektrum K0 als
Literaturvoraussetzung.

## Folge für OP1
- **Der am besten bestimmte Angriffspunkt ist U2.** Drei unabhängige Kennzeichnungen derselben Zustandsmenge; zu klären ist nur, welche davon der
  Bestand erzwingt. Unter Lesart (B) (M als geboosteter Beobachter, η = artanh β_sym) wäre zu prüfen, ob ein Beobachter mit Rapidität an einer
  Punktierung nur Extremzustände auflöst. Das ist eine konkrete, noch nicht gestellte Frage.
- **Die schwächste Stelle ist K3, die Regel von T.** Fünf Gründe für dasselbe Ergebnis sind hier kein Beleg, sondern zeigen, dass keiner zwingt.
  ABCK ist zudem der in der Literatur überholte Wert (v4.8.0-r03 F11). Wer die Zuordnung datenfrei begründen will, muss hier anfangen oder einen der fünf
  Gründe aus dem Bestand ableiten.
- **K2 ist bisher nur gesetzt.** Eine Begründung, warum M keinen Spin ausschließt, gibt es nicht.
- Kein blinder Test folgt aus dieser Ordnung; sie benennt nur, was zu begründen bleibt. OP1 offen; H98, H102, H112 unverändert.
