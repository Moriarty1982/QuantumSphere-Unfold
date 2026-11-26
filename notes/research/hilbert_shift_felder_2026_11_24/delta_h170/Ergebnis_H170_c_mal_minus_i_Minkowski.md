# Ergebnis H170: c mal −i macht aus der Drehung einen Schub (Minkowski-Signatur) und aus dem neutralen den geladenen Term

**Stand:** 26.11.2026. Vorab-Notiz `Vorab_Notiz_H170_c_mal_minus_i_Minkowski.md` (Commit 9b479a6, vor der Rechnung). **Nicht blind** für a bis d (exakte
Nachprüfung). Skripte k365 (Python, sympy/mpmath), k365b (Wolfram, unabhängig aufgebaut), k365c (Nachtrag). Alle stimmen überein. Qiskit nicht eingesetzt.

**Ergebnis in einem Satz:** Die Multiplikation c ↦ −ic ersetzt die innere Einheit e₇ durch die Einheit k = i·e₇ mit k² = +1: Die Ebene bekommt die Signatur
(1,1), die Ladungsmischung wird ein Schub mit Geschwindigkeit c′ = tanh ε, und der Chiralitätsprojektor ist der Lichtkegel c′ = 1; an der quadratischen
Form ist −i genau der Schritt vom neutralen zum geladenen Term. Dass die innere Richtung die Zeit ist, folgt daraus nicht.

## Ergebnisse gegen die Kriterien
| Teil | Befund | Kriterium | Urteil |
|---|---|---|---|
| H170a | c ↦ −ic hat Ordnung 4; Bahn i → 1 → −i → −1 → i; Fixpunkte 0 (und ∞). Projektor P ↦ c = 1 ↦ Projektor P̄ ↦ c = −1 | Nullreste | **bestätigt** |
| H170b | k = ij, k² = +1; (a + bk)(a − bk) = a² − b² gegen a² + b² auf span(1, j). 1 + c′k = (cosh ε + k sinh ε)/cosh ε mit c′ = tanh ε; e^{εk}P = e^{ε}P, e^{εk}P̄ = e^{−ε}P̄; Addition (c₁′ + c₂′)/(1 + c₁′c₂′). Tr Z² = 2(1 − c′²)\|x\|², Spin-1-Term (1 − c′²)v′², N = 2i·c′(3 + c′²)xyz. Lichtartig genau für c′ = ±1; 1 + k = 2P | Nullreste | **bestätigt** |
| H170c | G_i = −(s + iv)² = −r²e^{2iδ}; Re G_i = 2F₀ − (s² + v²), Im G_i = 2F₁ − (s² + v²) = −2sv; 2F_c − (s² + v²) = −r² cos 2(δ − χ) = Re[e^{−2iχ}G_i] | Nullreste | **bestätigt** |
| H170d | Re[−i·G_i] = c = 1-Form; −i·G_i(δ) = G_i(δ − π/4). Minima gefaltet: ohne Faktor {0, π/3} oder {π/6}; mit −i {π/12, π/4}; mit (−i)² wieder {π/6} oder {0, π/3} mit getauschtem Vorzeichen. Am Feld ist −i die Achteldrehung e^{−iπ/4}; die volle Tachyon-Abbildung gibt G ↦ −G | Nullreste; Minima 10⁻¹² | **bestätigt** |
| H170e | 84 Vergleiche; unter der vorab gesetzten Schwelle 10⁻³ zwei Einträge, beide derselbe Kandidat: arcsin β_sym − arctan β_sym = 0,0792660 gegen tan 2x = 0,0793204 (6,9·10⁻⁴) und dessen Hälfte gegen tan x (8,8·10⁻⁴). Unter 10⁻⁴: keiner | kein Treffer vorhergesagt | **Vorhersage nach dem eigenen Kriterium verfehlt**; als Gleichung ausgeschlossen (siehe unten) |

## Zum Beinahe-Treffer in e (k365c, nachträglich)
Als Gleichung gelesen gibt der Kandidat m_μ/m_e = 206,124 (2x = …), 207,083 (tan 2x = …) oder 206,364 (tan x = …) gegen gemessen 206,7682827(46). Das sind
0,1 bis 0,3 % Abweichung, in δ zwischen 2,7·10⁻⁵ und 5,6·10⁻⁵, also 7·10⁴ bis 1,4·10⁵ Standardabweichungen von δ*. Zum Vergleich: 2/9 liegt 1,75·10⁻⁷ neben δ*.
Die Beziehung ist als exakte Gleichung **ausgeschlossen**. Die Schwelle 10⁻³ war zu weit gewählt (H167 und H168 hatten 10⁻⁴); das ist ein Fehler der
Vorab-Notiz und wird hier offen geführt. Der Versatz x folgt im Schub-Bild nicht aus β_sym.

## Lesart
- **Antwort auf die Frage.** Die Multiplikation mit −i ist kein Kunstgriff. Mit c = ic′ wird 1 + c·e₇ zu 1 + c′·(i e₇), und i e₇ ist genau der Operator iL_e₇
  aus dem Chiralitätsprojektor (r42, r51). Er quadriert zu +1. Die reelle Familie dreht in der Ebene (1, e₇) um den Winkel χ = arctan c; die gedrehte
  Familie schiebt in der Ebene (1, i e₇) mit der Rapidität ε = artanh c′. Die Norm 1 + c² wird 1 − c′².
- **Minkowski.** Die Ebene (1, i e₇) hat die Signatur (1,1). c′ verhält sich wie eine Geschwindigkeit: Addition nach der relativistischen Formel, |c′| < 1 für
  nicht verschwindende Norm, und bei c′ = ±1 liegt der Lichtkegel. Dort sitzen die beiden Chiralitätsprojektoren; der Schub streckt P um e^{ε} und staucht P̄
  um e^{−ε}. Das ist das bekannte Bild „Chiralität = lichtartiger Grenzfall“, hier aus der Algebra. **Nicht gezeigt** ist, dass diese Ebene ein Stück der
  Raumzeit ist: Die Rechnung gibt eine Signatur, keine Zuordnung von e₇ oder i e₇ zur Zeit. Der Vorschlag des Autors („erster Teil eines Minkowski-Raums“) ist
  damit ein tragfähiger Kandidat, kein Ergebnis. Welche der beiden Achsen zeitartig heißt, ist in der Ebene allein Konvention.
- **Die beiden Sektoren aus einer Form.** Am Projektorpunkt ist die quadratische Form holomorph, G = −(s + iv)². Ihr Realteil ist der neutrale Term (c = 0),
  ihr Imaginärteil der geladene (c = 1). Jede reelle Mischung ist eine Phasenlage derselben Form. −i dreht von der einen Lage in die andere; gefaltet ist das
  die Verschiebung π/12 aus H99. Zweimal −i ist die Tachyon-Abbildung an der Form (Vorzeichenwechsel), viermal die Identität.
- **Was am Feld passiert.** −i an der quadratischen Form ist eine Achteldrehung e^{−iπ/4} am Feld, also die Wurzel der Tachyon-Abbildung z ↦ iz, nicht diese
  selbst. Eine Achteldrehung kennt das Projekt schon: Ψ = exp(uπ/4) in r13 neu (Koide), der Oktantschritt (r30, H118). Ob es dieselbe ist, ist nicht geprüft.

## Bilanz der Setzungen
| Schritt | gesetzt | hergeleitet | wohin die offene Wahl gewandert ist |
|---|---|---|---|
| H167 | Skala, J, c = 1 | Oktant; Phase aus dimensionslosen Termen | warum c = 1; ein kleines Verhältnis |
| H168 | dazu: Brannen-Form für Neutrinos, c = 0 neutral | π/12 zwischen den Sektoren | gemeinsamer Versatz x; warum c = 0 und 1 |
| H169 | nichts Neues | Projektor = c = i; c ∈ {0, ±1} = feste σ-Parität | warum der geladene Term σ-ungerade ist |
| H170 | nichts Neues | c ↦ −ic = Drehung ↦ Schub, Signatur (1,1), Projektor = Lichtkegel; beide Sektoren = Re und Im einer holomorphen Form | warum der geladene Sektor den Imaginärteil liest (eine Achteldrehung am Feld); der Versatz x |

Die offene Wahl ist jetzt ein einziger Schritt: eine Achteldrehung zwischen neutralem und geladenem Feld, dazu die Zahl x.

## Grenzen
- Nur die Ebene span(1, e₇) mit äußerem i; keine Raumzeit, keine Dynamik. Frames: im M-Bild formuliert; nach r51 lässt die Tachyon-Abbildung Sektoren und
  Chiralität fest, und die Ladungskonjugation ist der Zeitumkehr-Teil, nicht z ↦ iz. Die Achteldrehung ist keines von beiden.
- Sektorzuordnung weiter unter H99. Kein Vorzeichen gesetzt; kein Guard berührt; OP3 und OP4 offen. Keine neue Datenvorhersage.
- Vergeben: H170, k365. Nächste frei: H171, k366.
