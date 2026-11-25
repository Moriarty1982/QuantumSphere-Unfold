# Ergebnis H146: Die Kopien-Struktur gibt keine Massen; sie gibt eine masselose Rest-Generation, aber weder Koide 2/3 noch die Hierarchie

**25.11.2026. Vorab-Notiz `Vorab_Notiz_H146_Massen_aus_Kopien.md` (Commit dbc2a69; a und b nicht blind, Messwerte bekannt). Skripte
`k329_massen_gram.py` (`k329_out.txt`), `k329b_gegenprobe.wl` (`k329b_out.txt`, Wolfram exakt). Status: H146a, b, c bestätigt.**

Anlass: Autor: „was passiert, wenn wir damit versuchen, mal die Massen auszurechnen?“ Setzung: Gram-Auslesung (r14–r16, H101), √m_k =
Eigenwerte der Gram-Matrix der Generationszustände ι_k(y_q), K = Tr G²/(Tr G)², Skala frei. Werkzeuge: Python (numpy), Wolfram exakt;
Qiskit nicht eingesetzt.

## Ergebnis
| Teil | Messwert | Kriterium | Entscheidung |
|---|---|---|---|
| H146a | drei Kopien (84 Auswahlen): max K = **19/32 = 0,594** (Leptonen), **½** (Farbe); Sedenion-Tripel: Leptonen √m = (¾, ¾, 3/2), K = 3/8; Farbe (0, 3/2, 3/2), K = ½ (Wolfram exakt) | vorab | **bestätigt** |
| H146b | vier Kopien mit H142-Relation: in jedem Ladungssektor genau ein Eigenwert 0 (≤ 6·10⁻¹⁶), Eigenvektor exakt c = (−1, −1, 1, 1); übrige ≥ ¾ | vorab | **bestätigt** |
| H146c | die drei massiven: Leptonen √m = (¾, ¾, 5/2), K = 59/128 = 0,461; Farbe (1, 3/2, 3/2), K = 11/32 = 0,344; \|K − ⅔\| ≥ 0,206; m_max/m_min ≤ 11,1 | \|K − ⅔\| > 0,01 und < 100 | **bestätigt** |

Messwerte zum Vergleich: K_ℓ = 0,666664, m_τ/m_e = 3477. **Frame-Prüfung:** Für geladene Leptonen ist die Frame-Maske eine
Ähnlichkeitstransformation (Form S, r57); Eigenwerte und K ändern sich nicht. Das Urteil „verfehlt die Daten“ hängt also nicht am Frame.

## Lesart
- **Antwort:** Mit der Kopien-Struktur allein lassen sich die Massen nicht ausrechnen. Die Überlappungen der Kopien sind kleine rationale Zahlen
  (¼, ⅝, −½), deshalb gibt es weder K = 2/3 (dafür bräuchte man mittlere Überlappung² ½, den Qubit-Oktanten) noch eine Hierarchie (höchstens
  Faktor 75 statt 3477), und bei den S₃-symmetrischen Auswahlen sind zwei Massen gleich.
- **Was die Struktur liefert (Ausgabe):** die Z₃-Phase 2π/3 der Kopien und, in der Gram-Auslesung, eine **exakt masselose Rest-Generation**:
  Der Nullvektor der Gram-Matrix ist genau die HS(0)-Linie c aus H145. Das passt zur Aussage des Autors, dass es auf HS(0) keine Masse gibt.
  Der schwerste Lepton-Zustand ist der gleichgewichtete (1, 1, 1, 1).
- **Was Eingabe bleibt:** die Gram-Auslesung selbst, K = 2/3 (Oktant), die Brannen-Phase, die Hierarchie, die Skala. Die Überlappungen sind reell,
  die Brannen-Phase kann hier nur 0 oder π/3 sein.
- Vorzeichen offen; OP3 offen; kein Guard berührt. Vergeben: H146, k329.
