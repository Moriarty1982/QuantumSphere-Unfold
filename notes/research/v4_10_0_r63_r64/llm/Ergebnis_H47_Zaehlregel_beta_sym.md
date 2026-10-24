# Ergebnis H47: β_sym als Verhältnis zweier Horizontzählungen

Vorab-Notiz: `llm/Vorab_Notiz_H47_Zaehlregel_beta_sym.md` (Commit df0c788), Rechnung danach mit `llm/k102_zaehlregeln.py` (Ausgabe `llm/k102_out.txt`).

| Zählung | γ | γ_L = γ/γ_ABCK | β | η | im Fenster [0.545, 0.570] |
|---|---|---|---|---|---|
| ABCK (nur j = ½) | 0.1273840 | 1 | 0 | 0 | – |
| DL/Meissner (Gewicht 2 je Spin) | 0.2375330 | 1.864700 | 0.549406 | 0.6175 | ja |
| Ghosh–Mitra (Gewicht 2j+1) | 0.2740669 | 2.151501 | 0.604468 | 0.7002 | nein |

**A bestanden.** Die Meissner-Gleichung gibt 0.237532957966 (Abweichung 8·10⁻¹⁴). Die Zielzahl γ_L = 1.86444 der Notiz stammt aus dem gerundeten
Eingabewert 0.2375 des Haupttexts; mit dem exakten Wert ist γ_L = 1.86470, β = 0.549406 statt 0.549348. Das ändert kein Ergebnis.

**B trennt, wie erwartet (nicht blind).** Nur die DL/Meissner-Zählung liegt im Fenster; Ghosh–Mitra liegt mit β = 0.604 deutlich darüber.
Die Erwartung war vor der Notiz offengelegt; Versuchsfaktor 2.

## Bedeutung

- Unter dieser Lesart ist β_sym keine Messgröße, sondern eine reine SU(2)-Zahl: das Flächenspektrum √(j(j+1)) und zwei Zählregeln
  (minimal j = ½ gegen alle Spins mit Gewicht 2) legen sie ohne Eingabe fest.
- Zähl- und Lorentz-Lesart (r03 F11 sah einen Gegensatz) sind vereinbar, wenn der Tachyon-Frame minimal und der Materie-Frame voll zählt:
  γ_L = cosh 2η ist der Boost zwischen diesen beiden Gegenüberliegenden.
- Unter der Flavour-Lesart r55–r60 wählen die Leptondaten die DL/Meissner-Konvention, nicht Ghosh–Mitra. Das ist eine Beobachtung, kein Beleg:
  Das Fenster ist selbst nachträglich gewonnen.
- OP1 wird damit umformuliert: nicht mehr „β_sym als Fixpunkt herleiten“, sondern „aus den Frames begründen, warum T nur j = ½ und M alle Spins
  mit Gewicht 2 (nur m = ±j) zählt“ (Teil C, eigene Vorab-Notiz nötig).
- Guards unverändert.
