# k395: Renderschleife durch den HC, Bandwechsel mit Schranken, Vergleich mit der Lorenz-Maschine (Erkundung, 27.11.2026)

**Status:** Erkundung ohne Vorab-Notiz, kein Test. Teil 4 ist nachträglich. **Anlass:** drei Fragen des Autors vom 27.11.2026:
(1) Lässt sich das Problem auf dem Spinor-Band als Schleife formulieren, die sich von einem Ur-Seed aus ständig selbst justiert (dasselbe
Ursprungsfeld immer wieder durch den HC, mit Störungen aus der letzten Runde)? (2) Kann jede HC-Stufe ein Wechsel des Trägerbands sein, mit
einem Gebilde, das zuerst jedes Band mit jedem verbindet und dann durch Schranken und stetiges Wiederholen Übergänge löscht? (3) Ist das ein
ähnliches Problem wie bei der Lorenz-Chiffriermaschine?
**Werkzeuge:** Qiskit (die Runde ist eine Schaltung mit Messung, deshalb Qiskit; Dichtematrix exakt), Wolfram für die geschlossene Form der Schleife.

## Vorwissen geprüft

- Spinorband (STH) ist eine Hypothese (`sources/research/parts/v470/24_computational_specification.tex`, Zeilen 63–230); die Schleifenrolle
  („routed HC-selected closure“) ist dort eine offene Verpflichtung U_L.
- Das ausführbare Band ist eine binäre Turing-Maschine (`qam/examples/zuse_machine/machine_qiskit.py`, Klasse `FiniteBand`). Es hat keinen
  Befehl für Phase, Spinor oder HC. H137 (k310): Die Bandschaltung ist linear und phasentreu, rechnet aber klassisch; es fehlt ein Schritt, der
  Amplituden mischt.
- Der Hilbert-Shift ist in der QAM bereits als Wechsel des Etiketts definiert: H_QAM(⟨i, x⟩) = ⟨i+1, x⟩ (`07_qam_infrastructure.tex`, Z. 496).
  Der Inhalt x bleibt gleich, nur der Träger wechselt.
- HC als Messung (r70): ρ = ½(1 + b_S σ_z + b_C σ_x), C_HC = ½(1 + σ_x), p₊ = (1 + b_C)/2; nicht selektiv b ↦ (b_C, 0).
- r23: Die reine HC-Iteration ist nach einem Schritt am Fixpunkt R. r28.1(c): Selbstaustausch läuft zum Lichtpunkt. r28.2(c): Mit festem
  Reservoir gibt es einen Attraktor, selbstkonsistent nur bei x = ⅓.
- H160 (wiederholte Proben bremsen), H161 (kein festes Band bei zwei Köpfen). Bauplan Coprozessor: Stufe 0 gebaut, Stufe 2 (MEASURE, JUMP_IF,
  LOOP) nicht gebaut.
- Zurückgestellte Idee I7 (Attraktor einer Dynamik für Ω_M → β²) ist die nächste Verwandte. „Renderschleife“, „Ur-Seed“ oder ein Chiffren-Vergleich
  kamen bisher nicht vor.

## 1 Die Runde als Schaltung

Eine Runde auf einem Qubit (Dublett der Feldzustände): Drehung um α (RY), HC nicht selektiv (Messung entlang σ_x, Ergebnis verworfen), Austausch
mit einem frischen Band im Zustand |+⟩ (Teil-SWAP, Stärke x = sin²θ). Die Schaltung ist auf der HC-Achse genau die Abbildung

b′ = (1 − x) cos(2α) · b + x, b = ⟨σ_x⟩ (Abweichung Schaltung gegen Formel 7,8·10⁻¹⁶).

## 2 Vier Arten, die Schleife zu schließen

| Schleife | Was zurückgeführt wird | Ergebnis |
|---|---|---|
| L0 | nichts; Reservoir, x und α fest | Attraktor x/(1 − (1 − x) cos 2α), unabhängig vom Start (r28.2(c) nachgebaut) |
| L1 | die Ausgabe wird das neue Reservoir | läuft gegen 0, den Lichtpunkt (wie r28.1(c)) |
| L2 | die Stärke justiert sich: x = (1 − b)/(1 + b); α = π/6 fest | b = ½ aus jedem Start |
| L3 | Stärke und Drehwinkel justieren sich: zusätzlich tan²α = x; keine äußere Zahl | b′ = 1 − 2b(1 − b); Fixpunkte b = ½ und b = 1 |

Zu L3 (Wolfram, exakt): Die Abbildung ist b′ = 2b² − 2b + 1. Der Fixpunkt b = ½ hat die Steigung 0 (er zieht quadratisch an; nach sieben Runden
steht er auf zehn Stellen), der Fixpunkt b = 1 (Ruheframe, reiner Zustand) hat die Steigung 2 und ist instabil. Aus jedem Start 0 < b < 1 landet
die Schleife bei b = ½. Dort ist x = ⅓, γ = 2, β = 1/√3, α = π/6: der Hopf-Punkt, dieselbe Zahl wie die Zählregel mit der Fläche j + ½.

**Die Schleife landet nicht bei der Zahl des Modells:** 1/γ_L = 0,536279, β_sym = 0,5494056. Angepasst (keine Herleitung): L2 landet bei 1/γ_L,
wenn der feste Drehwinkel 25,617° ist statt 30°.

**Unterschiede werden gelöscht.** Zwei Läufe mit leicht verschiedener Störung nähern sich je Runde an (L3: 10⁻² → 10⁻⁷ in vier Runden → 0). Die
Schleife vergisst den Ur-Seed. Ein Fraktal im Sinn „kleine Unterschiede im Seed wachsen zu verschiedenen Strukturen“ entsteht in diesem
kleinsten Modell nicht.

## 3 HC-Stufe als Wechsel des Trägerbands; Schranken durch Wiederholen

Modell: vier Bänder |Farbe, Sektor⟩ (ν, e, d, u), zu Beginn jedes mit jedem verbunden (vollständiger Graph). Eine Schranke ist eine nicht
selektive Messung, die N-mal in fester Gesamtzeit wiederholt wird.

| Schranke | Ergebnis bei N = 1024 (Start auf ν) |
|---|---|
| keine | Abfluss in die Quark-Bänder 0,413 (unabhängig von N) |
| Farbe (Z) | Abfluss 0,0019; ν und e bleiben verbunden |
| Farbe und Sektor (Z, Z) | alles friert auf ν ein (0,997) |
| Farbe (Z) und HC auf dem Sektor (X) | Abfluss 0,0019; ν und e je 0,499, Kohärenz 0,001 |

Der Abfluss fällt wie 1/N (0,413; 0,229; 0,099; 0,029; 0,008; 0,002 für N = 1, 4, 16, 64, 256, 1024). Das ist der bekannte Zeno-Effekt.

Lesart: Das Bild trägt qualitativ. Eine oft wiederholte Schranke löscht genau die Übergänge, die sie unterscheidet. Der HC unterscheidet die
zwei farblosen Bänder nicht; er lässt ihren Übergang offen und besetzt beide gleich stark. Das Ergebnis ist ein Gemisch zu gleichen Teilen,
keine ausgewählte Überlagerung. Das Modell liefert damit eine Auswahlregel (welche Übergänge überleben), aber keine Zahl. Welche Schranken es
gibt, ist hier gesetzt.

Zur Frage „HC-Stufe = Bandwechsel“: In der QAM ist der Hilbert-Shift schon so definiert (Etikett i → i+1, Inhalt gleich). Neu wäre, dass eine
Menge von Bändern die Reihenfolge selbst bestimmt. H161 spricht dagegen, dass es dafür ein festes Band gibt, sobald zwei Köpfe lesen; als
Auswahl durch Schranken ist es formulierbar, wie hier gezeigt.

## 4 Vergleich mit der Lorenz-Maschine (vorsichtig)

Bekannt (Quellen unten): Die SZ40/42 hatte zwölf Räder. Fünf χ-Räder (41, 31, 29, 26, 23 Nocken) rückten bei jedem Zeichen weiter. Fünf
ψ-Räder (43, 47, 51, 53, 59) rückten gemeinsam und nur, wenn zwei Motorräder (61, 37) es zuließen. Der Schlüssel war die Summe (XOR) beider
Radsätze. Tuttes „1+2“-Angriff bildete Differenzen aufeinanderfolgender Zeichen. Weil die ψ-Räder oft stillstehen, weicht die Differenz zweier
Impulse leicht von 50 % ab; Colossus zählte diese kleinen Abweichungen und fand so die Stellung der χ-Räder.

| Lorenz | hier | trägt der Vergleich? |
|---|---|---|
| mehrere Räder überlagern sich zum Schlüssel | mehrere Bänder oder Stufen überlagern sich zur Ausgabe | als Bild ja |
| ein Radsatz rückt regelmäßig, einer unregelmäßig, gesteuert von einem dritten | Bänder schreiben sich vor, welches als Nächstes dran ist | als Bild ja; im Repo nicht definiert |
| Differenzen löschen den regelmäßigen Anteil; eine kleine Abweichung von 50 % bleibt | Differenz Up − Down löscht Gemeinsames (siehe unten); β als Abweichung von ½ (k396) | rechnerisch nachvollzogen, kein Test |
| die Maschine ist umkehrbar und verbreitet Unterschiede | die Schleife mit HC ist nicht umkehrbar und löscht Unterschiede | **nein**, hier liegt der Unterschied |
| der Angreifer kennt das Bauprinzip und sucht die Stellung | wir kennen weder Bauprinzip noch Stellung sicher | der Angriff setzt mehr voraus, als wir haben |
| viele Zeichen (Tausende) für die Statistik | sechs Quarkmassen, drei Leptonmassen, wenige Winkel | zu wenig Text für einen statistischen Angriff |

Hergeleitet ist davon nur: Korrelationen unabhängiger Bänder multiplizieren sich (⟨X⊗X⟩ = b₁b₂, in k396 mit Qiskit nachgerechnet); das ist die
Regel, die Tuttes Angriff trägt. Alles Übrige ist Analogie.

**Differenzen an den Quarkmassen (nachträglich, kein Test).** Δ_g = ln(m_u,g/m_d,g) = (−0,783; 2,454; 4,083). Was beiden Sektoren gemeinsam ist,
fällt heraus. Die ersten Differenzen sind 3,237 ± 0,033 und 1,629 ± 0,022, ihr Verhältnis 1,987 ± 0,043. Verhältnis 2 hieße
(m_c/m_s)³ = (m_u/m_d)(m_t/m_b)²: links 1574,7, rechts 1608,9, Abstand 0,31σ. Zufallskontrolle: 7,0 % von 20000 erfundenen Datensätzen liegen so
nah an einer der einfachen Zahlen ⅓, ½, 1, 2, 3. Das ist unauffällig; als Kandidat nur mit neuer Vorab-Notiz prüfbar, und nur an genaueren
leichten Quarkmassen.

## 5 Lässt sich das auf dem Spinor-Band formulieren?

Ja, als Schaltung; nein, noch nicht auf dem Band des Repos.

- Die Schleife braucht drei Dinge, die das ausführbare Band nicht hat: einen Schritt, der Amplituden mischt (Drehung; fehlt laut H137), eine
  Messung mitten im Lauf (HC), und eine Rückführung des Messergebnisses oder Zustands in die nächste Runde. Das sind genau die Befehle der
  nicht gebauten Stufe 2 des Coprozessors (MEASURE, JUMP_IF, LOOP), dazu ein Drehbefehl.
- Als Programm in dieser Sprache wäre L3: `LOOP { ROT(α(b)); MEASURE_X (verwerfen); SWAP_PART(x(b), frisches Band) }`, mit b aus der Statistik
  der letzten Runden. Die Regel x(b), α(b) ist dabei gesetzt, nicht hergeleitet.
- Auslöser 2 der zurückgestellten Idee I7 (eine Regel für die Zeit je Kaskadenschritt, die aus der Struktur folgt) ist nicht erfüllt: Die
  Schleife zählt Runden, sie liefert keine Zeit je Runde.

## Bilanz der Setzungen

| Größe | Status |
|---|---|
| Runde = Drehung, HC nicht selektiv, Austausch mit |+⟩ | gesetzt (aus r28 übernommen) |
| Rückführregeln x = (1 − b)/(1 + b), tan²α = x | gesetzt (Wörterbuch b = 1/γ, x = β²; Hopf-Beziehung) |
| Fixpunkt b = ½, Steigung 0, Löschen der Unterschiede | hergeleitet (Wolfram exakt, Qiskit) |
| α = 25,617° für 1/γ_L | angepasst |
| vier Bänder, vollständiger Graph, Wahl der Schranken | gesetzt |
| Abfluss ~ 1/N, HC lässt ν–e offen | hergeleitet im Modell |
| Verhältnis 1,987 der Differenzen | nachträglich beobachtet, Zufallsquote 7 % |

## Grenzen

Ein Qubit je Band; keine Generationen, keine Farbe als Triplett, keine Dynamik in Raum und Zeit. Die Schleife ist das kleinste Modell, das die
Frage trägt. OP1 bis OP5 bleiben offen; es wird keine Zahl hergeleitet.

## Quellen

- [Lorenz cipher (Wikipedia)](https://en.wikipedia.org/wiki/Lorenz_cipher)
- [Cryptanalysis of the Lorenz cipher (Wikipedia)](https://en.wikipedia.org/wiki/Cryptanalysis_of_the_Lorenz_cipher)
- [Anoraks Corner: the statistics used to attack Lorenz](https://codesandciphers.org.uk/anoraks/lorenz/stats.htm)
- [Stanford, Colossus: Wheel Breaking](https://cs.stanford.edu/people/eroberts/courses/soco/projects/2008-09/colossus/wheelbreaking.html)
- [W. T. Tutte (Wikipedia)](https://en.wikipedia.org/wiki/W._T._Tutte)
