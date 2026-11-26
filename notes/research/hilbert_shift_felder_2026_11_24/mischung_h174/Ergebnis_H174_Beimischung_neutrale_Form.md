# Ergebnis H174: Eine Beimischung der neutralen Form liefert die nötige kleine Drehung nicht

**Stand:** 26.11.2026. Vorab-Notiz `Vorab_Notiz_H174_Beimischung_neutrale_Form.md` (Commit d1aebfe, vor der Rechnung). b und c blind, a nicht blind.
Skripte k370 (Python), k370b (Wolfram, Hauptfälle unabhängig nachgerechnet, stimmen überein). Qiskit nicht eingesetzt.

**Ergebnis in einem Satz:** Die nötige Drehung der geladenen Leptonen steht fast senkrecht (rund 78°) zur Richtung, in die eine Beimischung der neutralen Form
dreht; mit den vorab festgelegten Stärken tan x und tan 2x ist kein Zweig mit den Daten verträglich, und der Aufbau am Baumpunkt ist widerlegt.

## Ergebnisse gegen die Kriterien
| Teil | Befund | Kriterium | Urteil |
|---|---|---|---|
| H174a (nicht blind) | Nötige Störung der zirkulanten Matrix: e–μ-Element 0,0516 (x) bzw. 0,0450 (x_R) in Einheiten von λ_μ − λ_e; zu 99,7 % (Normquadrat) nicht zirkulant; reeller symmetrischer und imaginärer antisymmetrischer Anteil gleich groß. Phase gegen das e–μ-Element von N̂: ±1,371 rad (x) bzw. ±1,322 rad (x_R), also 78,5° bzw. 75,7°. Überlapp mit dem nicht zirkulanten Teil von N̂: Kosinus 0,08 bzw. 0,10 | Rekonstruktion 10⁻⁸ | **bestätigt** (Rest 10⁻¹⁶) |
| H174b (blind) | 48 Zweige je Versatz, davon 4 physikalisch verschiedene mit kleinem θ₁₃. η = +tan x: sin²θ₁₃ = 0,0121 (−18,6σ). η = −tan x: 0,0174 (−9,0σ), θ₁₂ +6,8σ. η = +tan 2x: 0,0106 (−21,1σ). η = −tan 2x: 0,0218 (−1,1σ), aber sin²θ₁₂ = 0,371 (+10,6σ) und sin²θ₂₃ = 0,537 (+4,0σ). Verträglich: 0 Zweige. Kontrolle x_R: kein Zweig mit θ₁₃ innerhalb 3σ (nächster +4,1σ) | verträglich / widerlegt / nicht entschieden | nach dem Wortlaut **nicht entschieden** (ein Zweig trifft θ₁₃ innerhalb 3σ); in der Sache **nicht verträglich**: derselbe Zweig verfehlt θ₁₂ um 10,6σ |
| H174c (blind) | 12 Fälle. Kein Fall mit sin²θ₁₃ innerhalb 3σ. Zweig mit dem Elektron auf dem T-Eigenwert 1: η = −0,1320, sin²θ₁₃ = 0,0039 (−33σ), m_τ = 2534 MeV (+43 %). Bester Massenwert überhaupt: −6,2 %, dort θ₁₃ unbrauchbar | trägt / teilweise / widerlegt | **widerlegt** |

Kontrolle: η = 0 gibt H173 zurück (0,01426; 0,32369; 0,5). Zusatz, nicht vorab festgelegt: Auch ein frei gewähltes η erreicht nur χ² = 115 (x) bzw. 86 (x_R).
Die Beimischung zieht θ₁₃ zwar hoch (für η < 0), schiebt dabei aber θ₁₂ nach oben, also weg vom Messwert. Der zirkulante Teil verlässt dabei K = ⅔
(η = −tan 2x: K = 0,634).

## Lesart
- **Warum es nicht geht.** Die Beimischung η·N̂ ist reell und symmetrisch. Sie dreht e gegen μ in einer festen Phasenlage. Die Daten verlangen eine Drehung, die
  dazu um rund 78° verschoben ist. Der Betrag hätte gepasst (die Abschätzung vorab gab 0,06 bis 0,1), die Phase nicht.
- **Was der nötige Term ist.** Er hat einen reellen symmetrischen und einen gleich großen imaginären antisymmetrischen Anteil. Einen imaginären antisymmetrischen
  Term kann keine reelle Form liefern; naheliegend ist die Ladungsrichtung (die geladenen Leptonen stehen auf z = s + iv, die Neutrinos auf s); gezeigt ist das nicht.
- **Was ebenfalls nicht hilft (exakt, ohne Rechnung):** Jede Drehung der geladenen Seite, die eine Funktion von N̂ ist (etwa exp(iκN̂)), vertauscht mit N̂ und
  ändert nur Phasen der Mischungsmatrix, keinen Winkel.

## Bilanz der Setzungen (Strang 3)
| Schritt | gesetzt | hergeleitet | wohin die offene Wahl gewandert ist |
|---|---|---|---|
| H173 | Ein-Feld-Form, Brannen-Spektrum für Neutrinos | Winkel aus der Phase; Baumwert tribimaximal | θ₁₃ zu klein, Faktor 1,58 |
| k369 | nichts Neues | Lücke im Versatz, Faktor 1,5 bis 1,64; vier mögliche Stellen | welche der vier Stellen |
| H174 | Beimischung η·N̂ mit η aus x, gleiche Normierung | nötiger Term: Betrag 0,045 bis 0,052, Phase rund 78° gegen N̂, halb imaginär-antisymmetrisch | woher ein imaginärer antisymmetrischer Term bei den geladenen Leptonen kommt |

Das Ziel selbst (θ₁₃ und θ₁₂ aus einer kleinen Drehung der geladenen Leptonen) ist eine Anpassung an zwei Messgrößen mit zwei Zahlen. Die Frage entsteht nur in
der Zerlegung „Neutrinos tragen die Ein-Feld-Form, geladene Leptonen sind zirkulant“. Ob diese Zerlegung richtig ist, ist nicht gezeigt.

## Grenzen
- Die Beimischung, ihre Stärken und die gleiche Normierung waren Setzungen; widerlegt ist diese Konstruktion, nicht jede Drehung der geladenen Leptonen.
- Berichtigung vor der Auswertung: Kontrolle und Teil a benutzten zuerst den falschen ℤ₃-Zweig für das Elektron (im Skript vermerkt). Die blinden Teile b und c
  durchlaufen alle Zweige und waren nicht betroffen. Im Wolfram-Skript war zuerst die Sortierung falsch (in `k370b_out.txt` vermerkt).
- Keine Maske (Materie-Frame) gerechnet; bei einem negativen Befund dieser Größe (10σ in θ₁₂) wäre sie nur mit dem postulierten ε zulässig, und das ist in H173c
  schon weit weg. Polmassen; laufende Massen nicht geprüft.
- OP3 und OP4 bleiben offen. Kein Vorzeichen gesetzt; kein Guard berührt.
- Vergeben: H174, k370. Nächste frei: H175, k371.
