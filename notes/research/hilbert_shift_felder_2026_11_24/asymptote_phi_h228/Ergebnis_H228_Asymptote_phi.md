# Ergebnis H228 (k442): φ ist weder Grenzwert einer einfachen Schleife noch ein natürlicher Zwischenstand des Flusses

Stand 28.11.2026. Vorab-Notiz `Vorab_H228_Asymptote_phi.md` (Commit 92e43cb, vor der Rechnung). Hauptrechnung `k442_test_h228.py` mit
Ausgabe `k442_out.txt`, Gegenprobe in Wolfram `k442b_gegenprobe.wl` mit Ausgabe `k442b_out.txt`.

## Frage

Der Autor fragte, was wäre, wenn man φ = 0,0395773 als Asymptote behandelt, und wählte „Beides rechnen“. Teil A prüft φ als
anziehenden Fixpunkt einer iterierten Schleife aus Winkeloperationen des Rahmens. Teil B prüft φ als Stand des Gradientenflusses der
gemeinsamen Vakuumenergie (H225) auf dem Weg von 0 zum Minimum π/8, abgelesen zu einer vorab festgelegten natürlichen Uhrzeit.

## Urteil: widerlegt

### Teil A: Schleifen

| Größe | Wert |
|---|---|
| Wörter (Länge 1–5 über h, d, s, t, X, Y, Z, B, U, G) | 111 110, davon 1087 identitätsartig ausgeschlossen |
| anziehende Fixpunkte in (0, π/4) | 46 993 |
| Treffer im Fenster x ± 2σ_φ (± 1,56·10⁻⁶) | **keiner** |
| nächste Fixpunkte | BBGYB (und Umstellungen) 0,0395987, **27σ**; ZGXhh 48σ; hBYt 62σ |
| Häufung N_c(x) im Fenster ± 10⁻³ relativ | **4** |
| Kontrollen (2000 Werte in [0,02; 0,06]) | Mittel 9,7, Median 7, 99. Perzentil 59; 77 % der Kontrollen haben N_c ≥ 4 |

φ ist für diese Schleifen kein besonderer Punkt, seine Umgebung ist sogar dünner besetzt als ein typischer Wert. Zum Vergleich ziehen
die algebraischen Winkel, die die Operationen selbst erzeugen, viele Schleifen an (π/12: 1039, π/8: 396, π/24: 272).

**Grenze der Trennschärfe (nachträglich bemerkt):** Die Dichte der anziehenden Fixpunkte liegt bei etwa 124 000 pro Radiant. Im
2σ-Fenster erwartet man deshalb schon zufällig λ = 0,39 Treffer. Ein einzelner Treffer wäre also nicht signifikant gewesen (p ≈ 0,32);
nach dem Kriterium der Vorab-Notiz hätten es mindestens drei sein müssen (p ≈ 0,008). Das ändert das Urteil nicht, denn es gibt keinen
Treffer. Es zeigt aber, dass eine Schleifensuche mit Länge 5 bei dieser Genauigkeit an ihre Grenze kommt; längere Wörter würden das
Fenster nur dichter füllen, ohne Aussagekraft.

### Teil B: Fluss und Uhr (nicht blind)

In führender Ordnung ist S = 2 cos(π/8) cos(3(φ − π/8)) auf (0, π/4) (Wolfram: Abweichung 4·10⁻¹⁶). Der Fluss hat die geschlossene Form

  φ(t) = π/8 − (2/3) arctan( tan(3π/16) · e^(−t/τ) ),  τ = 1/E″(π/8),

bestätigt durch DSolve (gleichwertige Form u = arccos(tanh(3kt + artanh sin(π/8)))/3) und NDSolve (Abweichung 3·10⁻¹²). Der Datenwert
wird bei **t_x/τ = 0,132105** erreicht (σ_t = 2,7·10⁻⁶). Keine der zehn vorab festgelegten Uhren trifft:

| Uhr t*/τ | φ(t*) | Abstand |
|---|---|---|
| ⅛ | 0,037508 | −2 652σ |
| β_sym² | 0,086762 | +60 494σ |
| 1/γ_L² | 0,082973 | +55 636σ |
| ⅓ | 0,095019 | +71 079σ |
| übrige (1, ½, ln 2, ε, β_sym, 1/γ_L) | 0,136–0,232 | > 120 000σ |
| π/24 (k·t* = π/8, nachträglich bei der Planung bemerkt) | 0,039227 | −449σ |

**Prüfung der Ordnung:** Mit exakter Minimierung in δ und endlichem q hängt t_x/τ von q ab: 0,13096 (q = −0,01), 0,12311
(q = −0,0852), 0,11266 (q = −0,3). Die Kopplung q, die in führender Ordnung herausfällt, kehrt also bei endlichem q zurück. Für keinen
dieser Werte trifft eine Uhr auf 2σ; ⅛ liegt bei q = −0,0852 nur 1,5 % daneben, das ist aber eine Funktion des gesetzten q und kein
Treffer.

## Gegenprobe

- Wolfram bestätigt Teil B vollständig: geschlossene Form, t_x/τ = 0,132105185233, alle Uhrabstände auf die gezeigten Stellen gleich.
- Teil A, unabhängig gezählt für alle 1110 Wörter der Länge ≤ 3: nächster Fixpunkt GsY bei 0,0397459 (Abstand 1,69·10⁻⁴), N_c(x) = 0,
  beides wie in Python. Die Gesamtzahl unterscheidet sich (Wolfram 276, Python 335). Python zählt zusätzlich Fixpunkte, die exakt auf
  Gitterknoten liegen (rationale Vielfache von π bei stückweise linearen Wörtern), ohne sie kommt es auf demselben Gitter auf 286; der
  Rest von 10 sind Einordnungen an Faltungsknicken. Keiner dieser Punkte liegt nahe x.
- Qiskit war nicht geeignet, weil keine Quantenschaltung definiert ist.

## Hergeleitet, gesetzt, nachträglich

- **Hergeleitet:** die geschlossene Form des Flusses in führender Ordnung und die Lage des Datenwerts darauf (t_x/τ = 0,1321).
- **Gesetzt:** die Schleifenklasse (10 Operationen, Länge ≤ 5, Faltung auf [0, π/4]), die Fenster, der Kontrollbereich, die Uhrenliste,
  τ als Einheit, der Start bei φ = 0 und q < 0 (aus H225).
- **Nicht blind:** Teil B. Die Flussform und t_x/τ waren bei der Planung bekannt, die Uhrenliste wurde danach festgelegt.
- **Nachträglich:** die Lesart k·t* = π/8 (0,92 % daneben, 449σ) und die Bemerkung zur Trennschärfe in Teil A.

## Folgerung

Als Asymptote lässt sich φ nicht festlegen. Ein Grenzwert einfacher Schleifen ist es nicht, und auf dem Fluss zum symmetrischen Minimum
π/8 ist es nur ein Zwischenstand, dessen Uhrzeit keine natürliche Zahl des Rahmens ist. Die Lesart „φ als Anfangsbedingung oder
metastabiler Zwischenstand“ bleibt damit möglich, aber sie erklärt den Wert nicht: Sie verschiebt die Messzahl φ nur in eine Messzahl
t_x/τ = 0,1321 (bei endlichem q zusätzlich abhängig von q). Nach H221–H228 ist φ = 0,0395773 die eine Messzahl des Leptonbilds, wie in
r73 festgehalten. OP3 bleibt offen.

Vergeben: H228, k442. Nächste frei: H229, k443 (vor Vergabe gegen `main` prüfen).
