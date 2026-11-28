# Ergebnis H216 (k429) und H217 (k430): Umkehrschleifen und Flächenvarianten

Stand 28.11.2026. Die Vorab-Notizen stehen unter `notes/research/predictions/Vorab_Notiz_H216_Umkehrschleifen.md` und
`..._H217_Flaechenvarianten.md` (Commit 8e0b651, vor der Rechnung).

| Datei | Inhalt |
|---|---|
| `k429_test_h216.py`, `k429_out.txt` | Hauptrechnung, gemeinsamer Fixpunkt-Katalog mit 93 820 Fixpunkten, davon 11 748 anziehend und 81 658 abstoßend |
| `k429c_nachtrag_cluster.py`, `k429c_out.txt` | Nachtrag, nachträglich angesetzt |
| `k429b_gegenprobe.wl`, `k429b_out.txt` | Gegenprobe in Wolfram |

## H216: Umkehrschleifen

**Urteil nach dem Vorab-Kriterium: trägt teilweise. In der Sache ist der Überschuss der schon bekannte Fixpunkt von E.**

- Exakte Treffer gibt es keine. Der kleinste Rest beträgt 8,5·10⁻⁶ (Wort SECHS), der Fixpunkt liegt 3,2·10⁻⁶ neben β_sym.
- N_inv(β_sym) = 240 Wörter ohne das Einzelwort E. Die Zufallskontrollen haben den Median 46 und das 99. Perzentil 174. Nur 0,7 % der
  Kontrollen erreichen 240. Formal ist damit das Kriterium „teilweise“ erfüllt.
- **Nachtrag (nachträglich, k429c):** 182 der 240 Wörter haben genau den Fixpunkt x_E = 0,5493155 von E. Beispiele sind EE, CCEE und
  EEAW, also E samt trivialen Umformungen. Die Vorab-Notiz hatte nur das Einzelwort E ausgenommen, nicht diese Abwandlungen.
- Ohne den x_E-Haufen bleiben 59 Wörter. 33 % der Kontrollen haben mindestens so viele (99. Perzentil 159). Zählt man verschiedene
  Fixpunktwerte statt Wörter, kommt β_sym auf 27 Werte, die Kontrollen im Median auf 29.
- Außerhalb des schon bekannten Punktes ist β_sym also unauffällig.
- Die benannte Kontrolle 2^(1−γ_L) kommt aus demselben Grund auf 246, denn ihr Fenster enthält ebenfalls x_E.

**Lesart:** Die Umkehrschleife E⁻¹: y ↦ √(L/(2 + L)) mit L = −log₂ y zieht einen Punkt an, der 1,6·10⁻⁴ relativ neben β_sym liegt. Das ist
innerhalb des 2σ-Fensters, aber nicht exakt. Ihre Ableitung dort beträgt −0,583. Das ist die Nähe aus k396 in Schleifenform. Ob diese
Nähe Zufall ist, kann die Zählung nicht entscheiden. Ein exakter Zusammenhang besteht nicht, denn der Rest ist 9,0·10⁻⁵.

## H217: Flächenvarianten

**Urteil: nicht trennscharf. Die Suche wählt die Casimir-Fläche nicht.**

| Variante | β | vorwärts: N, Anteil Kontrollen ≥ N, exakte Treffer | umkehr: N, Anteil, exakte Treffer |
|---|---|---|---|
| Casimir √(j(j+1)) | 0,549406 | 3; 0,895; 0 | 240 (59 ohne x_E); 0,007; 0 |
| glatt j + ½ | 1/√3 | 28; 0,108; **18** | 125; 0,031; **88** |
| linear j | 0,475704 | 7; 0,564; 0 | 44; 0,540; 0 |

- Die glatte Fläche j + ½ hat 18 exakte Treffer in der Vorwärtsklasse (z. B. GRWHE) und 88 in der Umkehrklasse (z. B. WDA). Das war vorab
  angekündigt: γ = 2 macht 1/√3 zu einer geschlossenen Form, und die Klasse bevorzugt geschlossene Formen. Nach der Vorab-Notiz zählt das
  nicht gegen das Postulat r67.
- Auch der Treffer, der in der Vorab-Notiz als „E⁻¹G“ angeschrieben ist, gehört zur Umkehrklasse: G = S G⁻¹ S, also E⁻¹ S G⁻¹ S. Das
  Vorwärtswort dazu ist RGRE. Wolfram: RGRE(1/√3) = 1/√3 exakt, Ableitung ln 4 = 1,386, die Umkehrung hat 1/ln 4 = 0,721.
- Die lineare Fläche j ist in beiden Klassen unauffällig, obwohl β_j = E⁻¹(⅔) eine geschlossene Form hat.
- Casimir hebt sich nur über den x_E-Haufen ab (siehe H216). Dieser Haufen gehört zum Gewicht 2^(1−γ) und nicht zur Fläche.

## Gegenprobe

Wolfram bestätigt symbolisch:

- die drei γ: 1,86469976460937, genau 2 und genau log₂ 3;
- E(1/√3) = G(1/√3) = ½ und E(β_j) = ⅔;
- E⁻¹G(1/√3) = 1/√3 mit der Ableitung 1/ln 4;
- RGRE(1/√3) = 1/√3 mit der Ableitung ln 4.

Damit ist auch die Gleichwertigkeit „anziehend in der Umkehrklasse ⇔ abstoßend in der Vorwärtsklasse“ an einem Beispiel geprüft. Die
Zählung selbst läuft wie bei H215 in Python auf dem Katalog. Für die Vorwärtsklasse hat Wolfram sie in H215 unabhängig bestätigt.

## Hergeleitet, gesetzt, nachträglich

- **Gesetzt:** Klassen, Fenster, Kontrollen und Kriterien, alle vorab.
- **Blind gerechnet:** die Zählungen und die exakten Prüfungen.
- **Vorab bekannt (nicht blind):** E⁻¹ allein und die Schlagseite der Klasse zu j + ½.
- **Nachträglich:** die Bereinigung um den x_E-Haufen (k429c). Sie zeigt, dass das formale „teilweise“ in H216 allein am bekannten Punkt
  hängt. Das Vorab-Kriterium hätte alle Wörter mit dem Fixpunkt x_E ausnehmen sollen.

## Folgerung

Weder die Vorwärts- noch die Umkehrschleifen aus Operationen des Rahmens legen β_sym fest. Die Suche bevorzugt geschlossene Formen. Hätte
sie zu entscheiden, wäre j + ½ (1/√3) ihr Favorit, nicht die Casimir-Fläche. Einziger Rest ist die bekannte Nähe von β_sym zum Fixpunkt
von 2^(1−γ), mit 1,6·10⁻⁴ relativem Abstand, nicht exakt. OP1 bleibt offen, die Casimir-Fläche bleibt Postulat.
