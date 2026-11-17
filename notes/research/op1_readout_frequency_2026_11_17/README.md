# OP1: Mit welcher Frequenz liest M aus? (Erkundung, nicht blind)

17. November 2026. Auftrag des Autors: „weiter“, nach `../op1_flux_lines_2026_11_17/` (Nachtrag: Die Breite von M setzt eine Frequenz voraus; gesucht ist
die Frequenz, mit der M ausliest). Literatur zuerst, dann eine kurze Rechnung. Skript `qnm_rules.py`, Ausgabe `run/qnm_rules_stdout.txt`. Nicht blind:
Zählgewichte und γ-Werte sind bekannt, die Rechnung ist elementar. Keine H-Nummer.

## Vorwissen geprüft
- Bestand: r17.1 (Photonuhr; Gleichsetzung von Uhr- und Feldfrequenz vom Quelltext abgelehnt, v4.9.0-r12), r17.4 (Barbero-Verbindung als Punkt
  des Dubletts (A₊, A₋): reelles γ auf dem Äquator, γ = ±i an den Polen), r16.8 (zeitharmonische Felder).
- `predictions/Vorab_Notiz_H104_Zaehlregel_Flaechenspektren.md`: (L, A, 2) gibt γ = ln 3/π = 0,3497 (linear, alle Spins, Gewicht 2). Den Bezug
  zu den Quasinormalmoden hatte das Repo nicht (Suche nach „quasinormal“, „Dreyer“: keine Fundstelle vor dieser Notiz).
- r28.3: Mit j statt √(j(j+1)) gibt die Gewicht-2-Regel 0,3497.

## Literatur
- **Dreyer** ([gr-qc/0211076](https://arxiv.org/abs/gr-qc/0211076)): Bohr-Korrespondenz mit der Quasinormal-Frequenz ω = ln 3/(8πM) (Hod; analytisch
  Motl) gibt das Flächenquant ΔA = 4 ln 3; mit Standardspektrum und 2j + 1 Zuständen folgt j_min = 1 und γ = ln 3/(2π√2) = 0,1236 (SO(3) statt SU(2)).
- **Corichi** ([gr-qc/0212126](https://arxiv.org/abs/gr-qc/0212126)): j_min = 1 aus Fermionzahl-Erhaltung, SU(2) bleibt; derselbe Wert 0,1236.
- **Polychronakos** ([hep-th/0304135](https://arxiv.org/abs/hep-th/0304135)): Ein äquidistantes Spektrum versöhnt Quasinormalmoden und
  Bekenstein–Hawking, mit Entartung n + 1 (Kondensat aus Spin 1) oder 2n + 1 (nur ganze Spins, unterscheidbare Kanten). Gewicht 2 kommt dort nicht vor.
- **Frodden–Geiller–Noui–Perez** ([1212.4060](https://arxiv.org/abs/1212.4060)): Mit γ = ±i (selbstduale Ashtekar-Variablen) und der Fortsetzung
  j → is − ½ (Hauptserie von SU(1,1)) ergibt sich S = A/4 ohne Festlegung von γ; ein makroskopischer Zustand verlangt die Hawking-Temperatur.
  Im Bild von r17.4 sind γ = ±i die Pole des Dubletts, also die Lage der Ports.

## Rechnung

| Spektrum | Regel | γ | kleinstes Flächenquant 8πγ a(½) |
|---|---|---|---|
| √(j(j+1)) | M (alle j, Gewicht 2) | 0,237533 | 5,170 |
| √(j(j+1)) | P (alle j, 2j + 1) | 0,274067 | 5,965 |
| √(j(j+1)) | T (nur j = ½, Gewicht 2) | 0,127384 | 2,773 = 4 ln 2 |
| linear j | **M (alle j, Gewicht 2)** | **0,349699 = ln 3/π** | **4,394 = 4 ln 3** |
| linear j | P (alle j, 2j + 1) | 0,390868 | 4,912 |
| linear j | T (nur j = ½, Gewicht 2) | 0,220636 = ln 2/π | 2,773 = 4 ln 2 |

Quasinormal-Quant nach Dreyer: ΔA = 4 ln 3 = 4,394.

1. **Nur die Regel von M mit linearem Spektrum trifft das Quasinormal-Quant.** Mit a(j) = j ist die Zählgleichung eine geometrische Reihe,
   Σ_{n≥1} 2xⁿ = 1 mit x = e^{−πγ}, also x = ⅓ und γ = ln 3/π; der kleinste Schritt (Δj = ½) hat die Fläche 8π·γ·½ = 4 ln 3, genau Dreyers ΔA.
   Die Bohr-Frequenz dieses Schritts ist damit die Quasinormal-Frequenz ln 3/(8πM). In der Sprache von Polychronakos (unterscheidbare Kanten,
   Z₁ = 1): Entartung 2 je Kante, Fläche n·4 ln 3 (n = 2j ≥ 1), β_c = ¼, also Bekenstein–Hawking und Quasinormal-Quant zugleich, ohne SO(3) und ohne
   j_min = 1. Diese Kombination steht in keiner der gelesenen Arbeiten; ob sie anderswo steht, ist nicht geprüft.
2. **Mit dem Spektrum √(j(j+1)) des Bestands passt keine Regel.** M hat das kleinste Quant 5,170, P 5,965; beide weichen vom Quasinormal-Quant ab.
   T trifft in beiden Spektren 4 ln 2, das Bit-Quant von Bekenstein; das ist die bekannte ABK-Lesart, keine Quasinormal-Frequenz.
3. **Preis.** Mit linearem Spektrum wird γ_L = γ_M/γ_T = log₂ 3 = 1,585 (exakt) und β² = Ω_M = 0,226 statt 0,302. Das widerspricht den Fenstern von
   H98 (Ω_M, m_W) und dem Leptonfenster; die Datenpaarung des Bestands verlangt √(j(j+1)).

## Einordnung
- **Antwort auf die Frage (Lesart):** Die einzige Frequenz, die die Literatur einem Horizont ohne Zusatzannahme zuordnet, ist die asymptotische
  Quasinormal-Frequenz. Sie passt genau zur Gewicht-2-Regel von M, aber nur mit äquidistantem Spektrum. Das ist eine Gabel: Liest M mit der
  Quasinormal-Frequenz aus, dann ist das Flächenspektrum linear, und die Datenpaarung von H98 (γ_L = 1,8647) fällt; hält man an √(j(j+1)) fest, hat
  M keine Quasinormal-Frequenz.
- **Zweiter Kandidat:** Die Hawking-Temperatur bei γ = ±i (FGNP). Sie gehört zu den Polen des Dubletts (A₊, A₋), also zur Lage der Ports, und gibt
  keine Zahl für γ, weil γ dort nicht festgelegt wird. Die Breite von M liegt zwischen Äquator (reelles γ) und Pol (γ = ±i).
- **Bezug zu `../op1_flux_lines_2026_11_17/`:** Quasinormalmoden sind gedämpfte, zeitharmonische Felder mit komplexer Frequenz; sie haben
  relative Phasen und damit eine Breite ungleich null. Sie sind also der Art nach der Feldtyp, den die Breite von M verlangt.
- Nicht blind, keine H-Nummer. Ein Test wäre nur sinnvoll, wenn ein Datum das Flächenspektrum unabhängig entscheidet; im Bestand ist es gesetzt.
  OP1 offen.

## Ergebnis in einem Satz
Die Quasinormal-Frequenz ist genau die Übergangsfrequenz der Gewicht-2-Regel von M, aber nur bei linearem Flächenspektrum (γ = ln 3/π, Schritt
4 ln 3); mit dem Spektrum √(j(j+1)) des Bestands und seiner Datenpaarung passt sie nicht. OP1 offen.

## Nachtrag (17.11.2026): Die Gabel hängt nicht vom Spektrum ab
Auftrag des Autors: „Gabel weiter prüfen“. Skript `fork.py`, Ausgabe `run/fork_stdout.txt`. Erkundung, nicht blind.

**Identität.** Für jedes Flächenspektrum a(j) gilt: T (nur j = ½, Gewicht 2) hat das kleinste Quant 8πγ_T a(½) = 4 ln 2, denn 2e^{−2πγ_T a(½)} = 1.
M (alle j, Gewicht 2) hat das kleinste Quant 8πγ_M a(½). Das Verhältnis ist γ_M/γ_T = γ_L. Mit der Bohr-Korrespondenz ω = ΔA·T_H/4
(T_H = 1/(8πM)) heißt das:

  ω_T = ln 2 · T_H,  ω_M = γ_L · ln 2 · T_H,  ω_M/ω_T = γ_L.

Der Frame-Faktor ist also das Verhältnis der Übergangsfrequenzen der kleinsten Schritte beider Auslesungen (Lesart; als Identität trivial, weil
a(½) gemeinsam ist).

| Spektrum | γ_M | γ_T | γ_L | Quant M | ω_M/T_H | Quasinormal (Quant M = 4 ln 3) |
|---|---|---|---|---|---|---|
| √(j(j+1)) (Bestand) | 0,237533 | 0,127384 | 1,864700 | 5,170 | 1,2925 | nein |
| j | 0,349699 | 0,220636 | 1,584963 = log₂ 3 | 4,394 | 1,0986 = ln 3 | erfüllt |
| j + ½ | 0,220636 | 0,110318 | 2 | 5,545 | 1,3863 = ln 4 | nein |
| √(j(j+1) + ¼) | 0,220636 | 0,110318 | 2 | 5,545 | 1,3863 | nein |
| j^0,8 (Testform) | 0,344030 | 0,192074 | 1,791126 | 4,966 | 1,2415 | nein |

**Folgerungen.**
1. **„M liest mit der Quasinormal-Frequenz aus“ ist gleichwertig mit γ_L = log₂ 3, für jedes Spektrum,** solange T die ABK-Regel (nur j = ½)
   behält. Die Gabel ist damit kein Streit um das Spektrum: Das lineare Spektrum ist nur das einfachste, das die Bedingung erfüllt; jedes andere,
   das sie erfüllt, gibt dasselbe γ_L und dasselbe Ω_M = 0,226.
2. **Die Datenpaarung von H98 (γ_L = 1,8647) legt die Auslesefrequenz von M fest:** ω_M = 1,2925 · T_H, nicht ln 3 · T_H = 1,0986 · T_H. Eine
   Quelle dieser Frequenz kennt weder der Bestand noch die gelesene Literatur.
3. **Auswege, falls M doch mit der Quasinormal-Frequenz liest:** (a) T zählt nicht nach ABK, dann ändert sich ω_T und γ_L ist nicht mehr an
   log₂ 3 gebunden; (b) der für M maßgebliche Übergang ist nicht das Verschwinden einer Punktierung mit j = ½. Beides wäre eine neue Setzung.
4. **Nachträglich gesehen, nicht verwendet:** Der Anteil der Punktierungen mit j = ½ in der M-Zählung ist 2e^{−2πγ_M a(½)} = 2^{1−γ_L} = 0,549161;
   β_sym = 0,549406. Abweichung 2,5·10⁻⁴, also nicht exakt (dieselbe Größenordnung wie die Zufallsnähe 2 arctan γ_M ≈ arctan ½ aus r17.4).

**Ergebnis des Nachtrags.** Die Gabel ist spektrumfrei: Mit T nach ABK erzwingt eine Quasinormal-Auslesung von M den Frame-Faktor log₂ 3 und
widerspricht damit der Datenpaarung; umgekehrt legt die Datenpaarung die Auslesefrequenz von M auf 1,2925 · T_H fest, ohne bekannte Quelle.
OP1 offen.

## Nachtrag (17.11.2026): Quelle für ω_M = 1,2925 · T_H gesucht, keine gefunden
Auftrag des Autors: „Quelle 1,2925 suchen“. Vor der Rechnung festgelegt und committet: `Kandidatenliste_1_2925.md` (9fce085), 16 physikalisch
ausgezeichnete Frequenzen eines Schwarzschild-Horizonts und zwei Größen des Bestands; Treffer bei relativer Abweichung ≤ 10⁻³, Kombinationen
zählen nicht. Skript `candidates.py`, Ausgabe `run/candidates_stdout.txt`. Nicht blind (Zielwert bekannt).

**Ergebnis: 0 Treffer von 16.** Nächste Kandidaten: 2η aus γ_L = cosh 2η (1,2351, 4,4 %), ln 4 aus dem Halbschritt-Spektrum (1,3863, 7,3 %),
asymptotische Quasinormal-Frequenz ln 3 (1,0986, 15 %), Maximum der Photonenzahl im Planck-Spektrum (1,5936, 23 %). Grundtöne der Quasinormalmoden,
Photonring und Maggiore-Lesart liegen um Faktoren 2 bis 12 daneben.

**Einordnung.** Wegen ω_M = γ_L ln 2 · T_H ist eine Quelle für 1,2925 gleichwertig mit einer Herleitung von γ_L; die Frequenzsprache bringt
nur dann einen neuen Zugang, wenn eine ausgezeichnete Horizontfrequenz den Wert trifft. Das ist für die festgelegte Liste nicht der Fall. Die
Suchrichtung „Frequenz der Auslesung“ ist damit für Schwarzschild-Frequenzen ausgeschöpft; offen bleiben nicht geprüfte Frequenzen (geladene oder
rotierende Horizonte, Graukörper-gewichtete Spektren). OP1 ist wieder bei der Ausgangsfrage: Warum ist γ_L = 1,8647, also warum zählt M mit
Gewicht 2 im Spektrum √(j(j+1)). OP1 offen.
