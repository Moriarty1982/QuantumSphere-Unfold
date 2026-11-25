# Ergebnis H143: Eine fünfte Kopie bringt keine neue Generation; jede Rest-Generation stammt aus einer der 9 Vierer-Relationen von H142, der Rest wächst nur um Leck

**25.11.2026. Vorab-Notiz `Vorab_Notiz_H143_Fuenf_Kopien_HS5.md` (Commit 5a68040; teilweise nicht blind, siehe dort). Skripte
`k326_fuenf_kopien.py` (`k326_out.txt`), `k326b_gegenprobe.wl` (`k326b_out.txt`, Wolfram exakt) und `k326c_herkunft.py` (`k326c_out.txt`,
nachträglich). Status: H143a bestätigt, H143b bestätigt, H143c bestätigt, H143d bestätigt, Kontrolle erfüllt.**

Anlass: Autor: „prüfe jetzt bitte, was passiert, wenn du noch eine Generation dazu nimmst.“ Fünf der 9 oktonionischen Kopien v = a ⊗ b auf HS(5),
getrennte Träger V = ⊕ C_v (40 Zustände), Rest = Kern K von V → ℂ⊗A₅. Neu gegenüber H142: der größte ladungsstabile Teilraum W ⊂ K wird
iterativ bestimmt; n_gen = Zahl der Eigenwerte 0 in W. Werkzeuge: Python (numpy, scipy) für alle 126 Fünferauswahlen × 16 Orientierungen;
Wolfram Language exakt für je eine Auswahl jeder Klasse. Qiskit nicht eingesetzt (keine Schaltung).

## Ergebnis
| Teil | Messwert | Kriterium | Entscheidung |
|---|---|---|---|
| Kontrolle | Vierer-Teilauswahlen: 9 mit n_gen = 1, Regel n_gen = dim R⁰ in allen 126 | H142 reproduziert | erfüllt |
| H143a | n_gen = dim R⁰ in **2016 von 2016** Fällen (126 Auswahlen × 16 Orientierungen); stets #EW 0 = #EW 1 | keine Abweichung | **bestätigt** |
| H143b | transportierte Orientierung: **45** Auswahlen mit n_gen = 1, **keine** mit n_gen ≥ 2; auch über alle 16 Orientierungen max n_gen = 1 (360 von 2016 Fällen) | beides | **bestätigt** |
| H143c | min Leck² der gemeinsamen Ladung 6,0 / 5,88 / 5,5 / 5,5 je Klasse | > 10⁻³ | **bestätigt** (keine gemeinsame Ladung) |
| H143d | in jeder Klasse leckende Singuletts mit ½ (2 bzw. 3), Leck 0,5; Kern-Komponenten nie Nullteiler (min smin 0,0025) | vorab | **bestätigt** |

**Die vier Klassen (transportierte Orientierung; Spektren Wolfram exakt):**
| Auswahlen | Rang v | dim K | dim W | W (ladungsstabil) | Rest K ⊖ W (leckt) |
|---|---|---|---|---|---|
| 9 | 3 | 18 | 14 | **eine Generation** 0, ⅓³, ⅔³, 1 **plus ein zusätzlicher Quark-Satz** ⅓³, ⅔³ (su(3): 2 Singuletts, 12 Farbe) | ½², (10 ∓ √10)/20 |
| 36 | 4 | 11 | 8 | **eine Generation** 0, ⅓³, ⅔³, 1 (1 ⊕ 1 ⊕ 3 ⊕ 3̄) | ½³ |
| 72 | 4 | 11 | 6 | nur Quark-Satz ⅓³, ⅔³ | ½³, (5 ∓ √10)/10 |
| 9 | 4 | 11 | 6 | nur Quark-Satz ⅓³, ⅔³ | ½³, 1/10, 9/10 |

**Herkunft (k326c, nachträglich):** Alle 45 Fünferauswahlen mit einer Rest-Generation enthalten **genau eine** der 9 Viererauswahlen von H142
(9 × 5 = 45, keine Überschneidung). Eine neue Fünf-Term-Relation mit Summe 0 gibt es nicht. Die fünfte Kopie fügt also nichts Vollständiges hinzu:
Sie bringt drei Zustände mehr, die entweder als zweiter Quark-Satz (wenn sie mit zwei anderen eine Relation mit Summe ≠ 0 bildet) oder als
leckende Zustände mit irrationaler gestauchter Ladung ((5 ∓ √10)/10, 1/10, 9/10, (10 ∓ √10)/20) auftreten.

## Lesart
- **Antwort:** Mit fünf Kopien entsteht keine zweite Rest-Generation. Höchstens eine vollständige, ladungsstabile Generation bleibt, und sie ist
  immer die aus H142 (Wechselrelation von vier Kopien). Was die fünfte Kopie zusätzlich bringt, ist ein weiterer Quark-Satz ohne Leptonen oder
  Leck mit Ladungen, die keine Quark- oder Leptonladungen sind (½ und irrationale Werte).
- **Die Regel (H143a):** Die Zahl vollständiger Rest-Generationen ist genau die Zahl unabhängiger Relationen Σ c_k v_k = 0 mit Σ c_k = 0, in allen
  Orientierungen. Sie ist damit eine lineare Eigenschaft der Kopienrichtungen. Weil die Orientierung in die Relationen eingeht, hängt die Zählung
  am offenen Vorzeichen (über alle 16 Orientierungen 360 von 2016 Fällen mit n_gen = 1; die Höchstzahl 1 ändert sich nicht).
- **Nullteiler (Vermutung des Autors):** Auch mit fünf Kopien ist keine Rest-Komponente ein Nullteiler; das Leck ist ein Ladungs-, kein
  Nullteilerphänomen.
- **Keine gemeinsame Ladung** (H143c); das Leck wächst gegenüber H142 sogar (5,5–6,0 statt 3,5–5,0).
- **Ausblick, nicht geprüft:** Nach reinem Abzählen von dim R⁰ wären zwei Rest-Generationen erst ab sechs Kopien möglich (max dim R⁰ = 2 bei 6 und
  7 Kopien, 3 bei 8, 4 bei allen 9). Ob die Regel dort weiter gilt, ist nicht gerechnet (nur mit neuer Vorab-Notiz).
- **Gesetzt bzw. offen:** Orientierung (transportiert, Vorzeichen offen bis zur Feldgleichung), Wahl der Kopien, k85-Ladung. Ob Rest-Zustände
  physikalisch sind, ist nicht gezeigt. Massen, Mischung nicht berührt. OP3, OP4 offen; kein Guard berührt.
- Vergeben: H143, k326. Nächste frei: H144, k327.
