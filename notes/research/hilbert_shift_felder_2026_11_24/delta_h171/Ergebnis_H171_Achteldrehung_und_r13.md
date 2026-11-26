# Ergebnis H171: Nicht dieselbe Drehung, aber dieselbe Form auf zwei Ebenen; zusammen ergeben sie den Oktanten

**Stand:** 26.11.2026. Vorab-Notiz `Vorab_Notiz_H171_Achteldrehung_und_r13.md` (Commit 4358c36, vor der Rechnung). **Überwiegend nicht blind** (a, b, d exakte
Nachprüfung; c mit offenem Ausgang). Skripte k366 (Python: sympy, dazu numpy mit dem Sedenion-Produkt aus k253) und k366b (Wolfram, für a, b, d).
Übereinstimmung in a, b, d. Teil c hat keine Wolfram-Gegenprobe. Qiskit nicht eingesetzt.

**Ergebnis in einem Satz:** Die Achteldrehung aus r13 dreht vom Singulett in die Dublettebene und legt K = ⅔ fest; die aus H170 dreht innerhalb der
Dublettebene und macht den Schritt neutral → geladen. Es sind zwei verschiedene Drehungen mit verschiedenen Einheiten, die nicht vertauschen. Beide sind
Fixachsen eines Tauschs, und nacheinander angewandt geben sie genau den Baumpunkt des geladenen Sektors, auf einem Zweig den Oktanten mit masselosem Elektron.

## Ergebnisse gegen die Kriterien
| Teil | Befund | Kriterium | Urteil |
|---|---|---|---|
| H171a | K = (A² + B²)/(3A²) = 1/(3 cos² θ), unabhängig von δ; K = ⅔ genau bei θ = π/4. Die Minima des Spin-1-Terms liegen bei δ = χ + nπ, unabhängig von θ. Feld als Dreiervektor n = R_az(δ)·R_pol(θ)·e_A | Nullreste | **bestätigt** |
| H171b | θ = π/4 ist die Fixachse von J (A ↔ B), χ = π/4 die von Cσ (s ↔ v). Baumpunkt: z = (a/√2)·exp(jπ/4) oder j-mal das. Erster Zweig: Eigenwerte a·{(1 − √3)/2, (1 + √3)/2, 2}, det = −a³. Zweiter Zweig: a·{0, (3 − √3)/2, (3 + √3)/2}, det = 0 (Oktant). Gewichte (A², 2s², 2v²) = (½, ¼, ¼) | Nullreste; Eigenwert 0 | **bestätigt** |
| H171c | Sedenionen: e_i·e₈ = +e_{i+8} und e₈·e_i = −e_{i+8} für alle i = 1..7, einheitlich. Der Azimut wird von der Verdopplungseinheit e₈ erzeugt (Rechtsmultiplikation), die polare Einheit u liegt in einer Kopie, steht senkrecht auf e₈ und antivertauscht mit ihr | < 10⁻¹² | **bestätigt** (Abweichung 0) |
| H171d | cos Θ = (2√2 − 1)/4, Θ = 62,80°; Kommutatornorm 0,82 | Nullrest | **bestätigt** |

Zusatz zu c (Bericht), Abgeschlossenheit von O_δ wie k255: 0 bei δ = 0 und π/3; 0,683 bei π/12; 0,866 bei π/6 (größter Wert); 0,500 bei π/4;
0,603 bei δ* = π/12 − x; 0,879 bei π/6 − x.

## Lesart
- **Antwort auf die Frage.** Nein, es ist nicht dieselbe Drehung. Schreibt man das Feld als Dreiervektor (A, B cos δ, B sin δ), dann ist r13 die Drehung um π/4
  von der Singulett-Achse weg (Polarwinkel) und H170 die Drehung um π/4 in der Dublettebene (Azimut). Die erste legt K = ⅔ fest und lässt δ frei, die zweite
  verschiebt δ und lässt K fest. In den Sedenionen gehören sie zu zwei verschiedenen Einheiten: u innerhalb einer Kopie, e₈ zwischen den Kopien.
- **Was sie gemeinsam haben.** Beide haben die Form exp(Einheit·π/4), und beide sind die Fixachse eines Tauschs zweier gleich schwerer Anteile: J tauscht
  Singulett und Dublett, Cσ tauscht Spin 2 und Spin 1. Am Baumpunkt des geladenen Sektors stecken beide in einer Zahl, z = (a/√2)·exp(jπ/4): der Betrag ist
  r13, die Phase ist H170. Das Gewicht teilt sich zweimal hälftig, (½, ¼, ¼).
- **Oktant.** Beide Achteldrehungen zusammen geben auf einem der zwei Zweige genau den Oktanten mit Eigenwert 0, also das masselose Elektron aus H101. Das
  ist dort bekannt; neu ist die Zerlegung in zwei gleichartige Schritte. Welcher Zweig gilt, entscheidet weiter erst Ordnung 6 (H167).
- **Was das nicht leistet.** K = ⅔ und c = 1 kommen nicht aus einer einzigen Operation. „Dieselbe Regel bei zwei aufeinanderfolgenden Verdopplungen“ ist
  eine Lesart, keine Herleitung: J ist ein Postulat (H156), und für Cσ im geladenen Sektor gibt es keinen Grund (H169).
- **Unteralgebren (Zusatz).** Die Richtungen 0 und π/3 sind Unteralgebren. Der neutrale Baumwert π/6 liegt genau in der Mitte, dort ist die Abweichung von
  einer Unteralgebra am größten; der geladene Wert π/12 liegt auf dem Viertel. Kein Sektor sitzt auf einer Unteralgebra. Nur berichtet.

## Bilanz der Setzungen
| Schritt | gesetzt | hergeleitet | wohin die offene Wahl gewandert ist |
|---|---|---|---|
| H167 | Skala, J, c = 1 | Oktant; Phase aus dimensionslosen Termen | warum c = 1; ein kleines Verhältnis |
| H168 | dazu: Brannen-Form für Neutrinos, c = 0 neutral | π/12 zwischen den Sektoren | gemeinsamer Versatz x; warum c = 0 und 1 |
| H169 | nichts Neues | Projektor = c = i; c ∈ {0, ±1} = feste σ-Parität | warum der geladene Term σ-ungerade ist |
| H170 | nichts Neues | c ↦ −ic = Schub, Signatur (1,1); Sektoren = Re und Im einer Form | eine Achteldrehung am Feld; x |
| H171 | nichts Neues | zwei Achteldrehungen (polar, azimutal), verschiedene Einheiten, zusammen der Oktant | zwei Tauschsymmetrien: J (Postulat) und Cσ (ohne Grund); x |

Vier Schritte in Folge haben die Setzung umformuliert und nicht entfernt. Die offene Wahl ist jetzt klar benannt: **Warum gilt im geladenen Sektor die
Tauschsymmetrie Cσ, und woher kommt der Versatz x?** Weitere Umformulierungen bringen hier nichts mehr; es braucht eine neue Zutat (Dynamik, also die
Feldgleichung, oder die Quarks als Prüfstein für die Zuordnung Ladung ↔ Phasenlage).

## Grenzen
- Teil c in der Sedenion-Darstellung aus k253/k255; die Albert-Darstellung (H158) benutzt e₇ als innere Einheit. Dass beide Darstellungen dieselbe
  Azimut-Einheit meinen, ist Lesart („die Einheit des Verdopplungsschritts“), nicht gezeigt.
- Unter H99 für die Sektorzuordnung. Kein Vorzeichen gesetzt; kein Guard berührt; OP3 und OP4 offen. Keine neue Datenvorhersage.
- Vergeben: H171, k366. Nächste frei: H172, k367.
