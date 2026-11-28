# Ergebnis H215 (k428): Keine einfache Schleife des Rahmens zieht β_sym an

Stand 28.11.2026. Vorab-Notiz: `notes/research/predictions/Vorab_Notiz_H215_Stabilitaet_Rueckwaertssuche.md` (Commit 38045e0, vor der
Rechnung). Hauptrechnung `k428_test_h215.py` mit Ausgabe `k428_out.txt`. Gegenprobe in Wolfram `k428b_gegenprobe.wl` mit Ausgabe
`k428b_out.txt`.

## Frage

Der Autor hatte einen Stabilitätstest für β_sym, Λ und χ verlangt und dafür die Rückwärtssuche gewählt. Gefragt ist, ob eine kurze
Verkettung von Operationen des Rahmens β_sym als anziehenden Fixpunkt hat, und zwar exakt. Zusätzlich wird geprüft, ob solche Schleifen
sich bei β_sym stärker häufen als bei Kontrollwerten.

## Urteil: widerlegt

| Größe | Wert | Kriterium |
|---|---|---|
| Wörter (Länge 1–5 über H, S, R, C, A, W, G, D, E) | 66 429, davon 63 identitätsartig ausgeschlossen | – |
| anziehende Fixpunkte in (0, 1) | 11 748 | – |
| N(β_sym), Fenster ±6,5·10⁻⁴ (k358) | **3** (DWHEH, RWERW, WREWR) | – |
| exakte Treffer, \|f(β) − β\| < 10⁻²⁰ | **keine** (kleinster Wert 1,9·10⁻⁵) | trägt nur mit exaktem Treffer |
| Zufallskontrollen (2000) | Mittel 13,95, Median 7, 95. Perzentil 40, 99. Perzentil 101 | trägt teilweise nur bei N > 101 |
| Anteil Kontrollen mit N ≥ N(β_sym) | 89,5 % | – |

β_sym ist also für diese Schleifen kein besonderer Punkt. Die Umgebung von β_sym ist sogar dünner besetzt als ein typischer Wert. Alle
drei Treffer im Fenster sind Wörter der Länge 5, die E enthalten. Ihre Fixpunkte liegen 1,7·10⁻⁵ bis 1,1·10⁻⁴ von β_sym entfernt, also
weit über der Rechengenauigkeit. Sie liegen nur zufällig im 2σ-Fenster.

Benannte Kontrollen zum Vergleich: N(½) = 530, N(1/√2) = 86, N(1/√3) = 28, N(⅓) = 15, N(2^(1−γ_L)) = 11, N(1/γ_L) = 6. Algebraische
Werte, die die Operationen selbst erzeugen (allen voran ½, der Fixpunkt der HC-Schleife), werden reichlich angezogen. β_sym gehört nicht
dazu.

## Einzelwort E (vorab als nicht blind ausgewiesen)

E: b ↦ 2^(1−γ(b)) hat seinen Fixpunkt bei 0,5493155, also 9,0·10⁻⁵ unter β_sym und damit im Fenster. Dort ist aber E′ = −1,716, der
Fixpunkt **stößt ab**. E allein zieht β_sym also nicht an, und die Umkehrschleife E⁻¹ gehört nicht zur festgelegten Klasse. Nachträglich
gefunden: Die Nähe 2^(1−γ_L) ≈ β_sym aus k396 heißt in Schleifensprache, dass β_sym fast ein abstoßender Fixpunkt von E ist. Das ist
derselbe ungeklärte Zahlenzufall in anderer Form, kein neuer Befund.

## χ und Λ

Wie in der Vorab-Notiz festgelegt, gibt es für beide kein Ziel. Das Minimum für χ wandert mit der Setzung (H211c), und Λ hat keine Skala
(k251). Zur Einordnung der χ-Kandidaten: ½ (cos²χ bei 45°) wird reichlich angezogen, ⅓ (magischer Winkel) nur von 15 Wörtern und von
keinem der Länge ≤ 3. Ein Zielwert für χ folgt daraus nicht.

## Gegenprobe und Prüfwege

- Wolfram berechnet β_sym unabhängig (Summe bis k = 400) und erhält 0,54940564097452899867, gleich der Python-Rechnung.
- Neu gezählt für die 819 Wörter der Länge ≤ 3, mit eigenem Gitter und FindRoot: N(β_sym) = 0, N(½) = 19, N(⅓) = 0. Python kommt auf
  dieselben Werte.
- Fixpunkt von E in Wolfram: 0,549315451920024, E′ = −1,71595. Das stimmt mit Python überein, wo E deshalb nicht unter den anziehenden
  Fixpunkten steht.
- Der Hardware-Weg (`qtune`) entfällt, weil kein Treffer ein Polynom vom Grad ≤ 2 ist.

## Hergeleitet, gesetzt, nachträglich

- **Gesetzt:** die Schleifenklasse (9 Operationen, Länge ≤ 5), die Fensterbreite aus k358 und der Kontrollbereich [0,35; 0,75].
- **Gerechnet (blind):** die Zählung, die exakte Prüfung und der Vergleich mit den Kontrollen.
- **Nachträglich:** die Lesart von E als „fast abstoßender Fixpunkt“.
- **Grenzen:** Das Urteil gilt nur für diese Klasse. Ein Nein für kurze Verkettungen schließt längere Schleifen nicht aus. Auch Schleifen
  mit Parametern sind nicht erfasst, denn jede Gleichung F(β) = 0 lässt sich über Newton zu einer anziehenden Schleife machen. Das wäre
  aber keine Erklärung, sondern ein Umschreiben.

## Folgerung

Stabilität erklärt β_sym nicht: Keine einfache Schleife des Rahmens hält den Wert fest. Damit bleibt es bei der Lage nach den 37
Versuchen. β_sym ruht auf der Zählregel r67 als Postulat, und OP1 ist offen. Der Coprozessor kann einen Fixpunkt messen, sobald eine
Schleife feststeht. Eine solche Schleife gibt es für β_sym, χ und Λ aber nicht.
