# Erkundung k374: nötige Konfiguration je Sektor und was die HS-Stufen dazu sagen (26.11.2026)

**Status: Erkundung, nicht blind.** Keine Vorab-Notiz, kein Entscheidungskriterium. Alles hier ist an die Daten angepasst, nichts ist hergeleitet.
Auftrag des Autors (26.11.2026): erst je Teil das System justieren, dann ansehen, welche Konfigurationen gesetzt sein müssen und wie sie zusammenhängen könnten;
dabei beachten, auf welcher HS-Stufe die Teilchen sitzen müssten. Einordnung: OP3/OP4. Vergeben: k374.

Werkzeuge: Python (`k374_konfigurationen.py`, Ausgabe `k374_out.txt`), Wolfram für die beiden CKM-Normen (`k374b_kontrolle.wl`, `k374b_out.txt`). Qiskit nicht geeignet.
Quarkmassen bei M_Z wie in H172; CKM-Zielwerte aus Vorwissen (nicht aus dem Repo): s₁₂ = 0,2250, s₂₃ = 0,0418, s₁₃ = 0,00373, δ = 1,14.

## Vorwissen geprüft
H172 (Brannen-Parameter der Quarks, Skalenabhängigkeit), H38 (ein ε je Sektor: trifft CKM und PMNS nur im Ausläufer), r60.3 (bei exakter A₄ ist V_CKM = 𝟙),
k253 (Erzeugungsregel HS(0) bis HS(3): ℝ, ℂ, ℍ, 𝕆), H158 (Albert-Algebra, Brannen-Form exakt), k262, H173 bis H176. Eine feste Zuordnung „Teilchen X sitzt auf HS(n)“
steht nirgends im Repo; der Autor hat am 25.11. festgehalten, dass es auf HS(0) und HS(1) noch keine Masse im strengeren Sinn gibt.

## 1. Massen: was je Sektor eingestellt sein muss
Brannen-Form λ_k = 1 + √2 ρ cos(δ + 2πk/3), K = (1 + ρ²)/3, λ ∝ √m.

| Sektor | K | ρ | Polwinkel (K = 1/(3cos²θ)) | δ (gefaltet) | δ bei anderer Skala |
|---|---|---|---|---|---|
| Neutrinos | ⅔ gesetzt | 1 | 45° | 0,4802 (aus R) bzw. 0,4788 (H176) | – |
| geladene Leptonen | 0,66666 | 1,0000 | 45,00° | 0,22222 | – |
| Down-Quarks (M_Z) | 0,748 | 1,115 | 48,1° | 0,1001 | 0,1101 (PDG-Skalen), K = 0,731 |
| Up-Quarks (M_Z) | 0,888 | 1,290 | 52,2° | 0,0518 | 0,0746 (PDG-Skalen), K = 0,849 |

- **Zwei Stellgrößen je Sektor:** die Phase δ und der Koide-Wert K (gleichwertig: der Polwinkel θ aus r13 neu). Die Leptonen sitzen beide bei θ = 45°; die Quarks nicht.
- **Beobachtung zur Phase (nachträglich, kein Befund):** In der Reihenfolge Neutrinos, geladene Leptonen, Down, Up halbiert sich δ grob von Stufe zu Stufe:
  0,480 / 0,222 / 0,100 / 0,052 (bei M_Z). Zum Vergleich π/6, π/12, π/24, π/48 = 0,524 / 0,262 / 0,131 / 0,065. Die Abstände dazu sind −0,043 / −0,040 / −0,031 / −0,014
  (M_Z) und für die Quarks bei PDG-Skalen −0,021 / +0,009. Die ersten beiden Werte (π/6, π/12) sind im Projekt schon bekannt (H99); neu wäre nur die Fortsetzung auf
  die Quarks. Sie ist grob, skalenabhängig und an vier Punkten abgelesen. H172 hat eine andere Regel (Phase linear in der Ladung) widerlegt; diese hier ist nicht getestet.

## 2. Mischungen: Baumwert und kleinster Term, der die Dreiersymmetrie bricht
Verfahren: Zielmatrix vorgeben, daraus die Massenmatrix des gebrochenen Sektors bauen (Massen exakt), den zirkulanten Anteil abziehen und über die freien Phasen
minimieren. Norm = Frobenius-Norm des Rests in Einheiten der mittleren Diagonale.

| Mischung | Baumwert | wo gebrochen | kleinste Norm | Anteil reell symmetrisch | Anteil imaginär antisymmetrisch |
|---|---|---|---|---|---|
| CKM | Einheitsmatrix (beide Quarksektoren zirkulant in derselben Basis) | Down | 0,157 | 83 % | 17 % |
| CKM | Einheitsmatrix | Up | 0,166 | 98 % | 2 % |
| nur Cabibbo-Winkel | Einheitsmatrix | Down | 0,085 | 50 % | 50 % |
| PMNS | tribimaximal plus Versatz der Neutrinos (x_R oder H176) | geladene Leptonen | 0,075 | 89 bis 90 % | 10 bis 11 % |
| PMNS | exakt tribimaximal (Neutrinos ohne Versatz) | geladene Leptonen | 0,164 | 70 % | 30 % |

- **Gleiche Größenordnung.** Beide Mischungen verlangen einen Bruch der Dreiersymmetrie von 0,08 bis 0,17 der Diagonale. Die CKM-Winkel sind klein, weil die Quarkmassen
  weit auseinanderliegen, nicht weil der Bruch klein wäre: θ·(λ_j − λ_i) ist für Down 0,061 / 0,093 / 0,009 (12 / 23 / 13).
- **Gleiche Art.** Der kleinste Term ist in allen Fällen überwiegend reell symmetrisch, mit einem kleineren imaginären Anteil. Der zirkulante Teil bleibt dabei fast
  unverändert (Leptonen: ρ = 0,9990, δ = 0,2220).
- **Der Versatz der Neutrinos halbiert den nötigen Bruch bei den Leptonen** (0,164 ohne, 0,075 mit). Ein Teil der Mischung steckt also schon im Versatz x.
- Wolfram bestätigt die beiden CKM-Normen (0,1570 und 0,1656).

## 3. HS-Stufen: was die Zahlbereiche hergeben
| Stufe | Algebra | hermitesche 3×3-Formen | davon zirkulant | brechen die Dreiersymmetrie | imaginäre antisymmetrische Richtungen |
|---|---|---|---|---|---|
| HS(0) | ℝ | 6 | 2 | 4 | 0 |
| HS(1) | ℂ | 9 | 3 | 6 | 3 |
| HS(2) | ℍ | 15 | 5 | 10 | 9 |
| HS(3) | 𝕆 | 27 (Albert-Algebra) | 9 | 18 | 21 |

Was daraus folgt (Abzählung, sicher):
- Eine **reelle** zirkulante Form hat nur δ = 0 oder π/3 (gefaltet). Jede andere Phase braucht mindestens ℂ. Alle vier Massensektoren haben eine Phase zwischen 0 und π/6,
  kommen als zirkulante Form also frühestens auf HS(1) vor.
- Die Neutrinos sind im Aufbau die Ausnahme: reelle Form auf s, **nicht** zirkulant. Das ist der einzige Sektor, dessen Massenform schon auf HS(0) Platz hat.
- Der imaginäre antisymmetrische Anteil, den beide Mischungen brauchen, existiert erst ab HS(1). Auf HS(1) gibt es davon 3 Richtungen (2 ungerade unter A, 1 gerade), ab HS(2) 9.

Was nur eine Lesart ist (nicht gezeigt):
- Mindeststufe nach Zahlbereich: Neutrinos HS(0), geladene Leptonen HS(1); Quarks tragen Farbe und brauchen damit HS(3). Für Down und Up getrennte Stufen
  (etwa HS(2) und HS(3)) gibt die Abzählung nicht her; sie wäre nur durch die grobe Halbierung von δ aus Abschnitt 1 nahegelegt.
- Der Koide-Wert steigt mit der Reihenfolge (⅔, ⅔, 0,75, 0,89). Ob das mit der Zahl der imaginären Einheiten je Stufe (0, 1, 3, 7) zusammenhängt, ist nicht geprüft.

## 4. Was je Teil gesetzt sein muss (Zusammenstellung)
| Teil | Stellgrößen | Werte | Status |
|---|---|---|---|
| Massen geladene Leptonen | K, δ | ⅔; π/12 − 0,0396 | K = ⅔ aus J (Postulat); Versatz offen |
| Massen Neutrinos | K, δ | ⅔ gesetzt; π/6 − 0,043 bis 0,045 | Versatz offen; K nicht messbar ohne weitere Annahme |
| Massen Down, Up | K, δ | 0,75; 0,10 und 0,89; 0,05 | beide offen, skalenabhängig |
| PMNS | Bruch bei den Leptonen | Norm 0,075; oder H176: tan x in (K₁ + K₂)/√2 | Richtung und Stärke angepasst |
| CKM | Bruch bei Down oder Up | Norm 0,16 | angepasst; welcher Sektor bricht, ist offen |

Gemeinsam ist allen Teilen: ein Baumwert mit hoher Symmetrie (π/6, π/12, tribimaximal, Einheitsmatrix) und eine kleine Abweichung der Größe 0,04 bis 0,17.
Ob diese Abweichungen eine gemeinsame Quelle haben, ist die offene Frage; diese Erkundung legt nur die Größen nebeneinander.

## Grenzen
- Quarkmassen und damit K, δ und die Normen hängen von der Skala ab; gerechnet ist bei M_Z. CKM-Werte aus Vorwissen.
- Die kleinste Norm ist ein Maß, keine Vorhersage: Die Natur muss nicht den kleinsten Term wählen. Die Aufteilung in A-gerade/ungerade benutzt das A der Neutrinos auch
  für die Quarks; dort hat es keine begründete Rolle.
- Die Frobenius-Norm hier ist nicht dieselbe Größe wie die Koeffizienten-Norm in k372 (Nebendiagonalen zählen doppelt).
- Die Beobachtung zur Halbierung von δ ist nachträglich und nicht gegen Zufall abgesichert.
- Im Wolfram-Skript war beim ersten Lauf die Sortierung falsch (in `k374b_out.txt` vermerkt).
- OP3 und OP4 bleiben offen. Kein Vorzeichen gesetzt; kein Guard berührt. Nächste frei: H177, k375.
